import rasa.train
import choice_bot
import state
from selenium import webdriver
import utility as u
import functions as fn
import writers as w
import asyncio
from views import ViewChatPannel
import styles
from user_manager import User
from random import randint

PREPROCESSING_EXCEPTION = "A problem occured during the preprocessing phase, take a look into the code and restart later"


class DialogueManager:

    def __init__(
        self,
        url,
        browser
    ):
        # initialize the the preprocessor
        self.url = url
        self.browser = browser
        self.user = None
        self.driver = None
        self.log_writer = w.LogWriter()
        self.counter = 0
        self.user_view = ViewChatPannel(self.log_writer, u.user_marker)
        self.chatbot_view = ViewChatPannel(self.log_writer, u.chatbot_marker)
        self.bot_manager = choice_bot.BotsManager()
        self.current_bot = None
        self.in_session = False
        self.restart = False
        self.states_list = []
        self.total_iterations = randint(1, u.MAX_DIALOGUES)
        self.iteration_number = 0

    def create_form_bots(self):
        try:
            self.instantiate_driver()
            self.bot_manager.create_bots(self.driver)
        except:
            print('Fail to create the form bots')
            raise Exception

    def start(self, bot_tag):
        try:
            # we start a session
            self.in_session = True
            self.current_bot = self.bot_manager.get_bot(bot_tag)
            if u.simulation_enabled:
                # we initialize the user
                self.user = User(self.current_bot['state'])
            if u.train_model:
                self.current_bot['bot'].train_model()
            self.conversation_prologue()
            self.start_dialogue()
            if u.write_log:
                self.log_writer.start()
            if self.restart:
                if self.iteration_number > self.total_iterations:
                    return
                # we increment the nunmer of iteration
                self.iteration_number += 1
                # we reset the botList for the new session
                self.bot_manager.botList = []
                self.create_form_bots()
                self.start(bot_tag)
        except:
            print(PREPROCESSING_EXCEPTION)

    def instantiate_driver(self):
        try:
            if self.browser == 'chrome':
                driver = webdriver.Chrome()
            elif self.browser == 'firefox':
                driver = webdriver.Firefox()
            elif self.browser == 'egde':
                driver = webdriver.Edge()
            else:
                driver = webdriver.Chrome()
            driver.minimize_window()
            driver.get(self.url)
            self.driver = driver
        except:
            print('Fail to instantiate the driver')
            raise Exception

    def conversation_prologue(self):
        try:
            bot = self.current_bot['bot']
            my_state = self.current_bot['state']
            # call fillForm woith a predefined message and present the form
            initial_string = 'fill the form'
            message = bot.interpreteMessage(initial_string)
            introduction = bot.findActionAndRun(my_state, message["intent"]["name"])
            stop_string = "Start of the conversation, to end your should type 'stop'."
            text = f'{stop_string}\n{introduction}'
            self.chatbot_view.show_text(self.counter, text)
            self.counter += 1
        except:
            print('Fail to implement the prologue of the conversation')
            raise Exception

    def start_dialogue(self):
        try:
            my_state = self.current_bot['state']
            # beginning of the interaction
            text = ''
            while True and self.in_session:
                if u.simulation_enabled:
                    a = self.user.get_answer(text)
                else:
                    a = input("Your input: ")
                if a == 'stop':
                    self.chatbot_view.show_end_of_conversation(self.counter)
                    self.restart = False
                    break
                if a != "":
                    text = f'Your input: {a}'
                    self.user_view.show_text(self.counter, text)
                    self.counter += 1
                    response = self.bot_manager.run_action(
                        state=my_state, userInput=a, tag=u.tag_registration_form)
                    text = f"response: {response}"
                    # we verify wheteher or not the submission have benn done
                    if not my_state.submit_done:
                        self.chatbot_view.show_text(self.counter, text)
                        self.counter += 1
                    else:
                        self.after_submit()
                else:
                    text = 'you did not insert any value'
                    self.chatbot_view.show_text(self.counter, text)
                    self.counter += 1
        except:
            print('Problem during the dialogue')
            raise Exception

    def after_submit(self):
        try:
            """Here we conclude the submission of the form and then we start or not a new
            session. If we start a new session, we restart from the beginning.
            Each time, the state is saved to write the final report"""
            newPageTitle = self.driver.title
            good_style = styles.get_good()
            text = f"{good_style} you have been moved to the page with title {newPageTitle}"
            self.chatbot_view.show_text(self.counter, text)
            self.counter += 1
            # we add the tate to the list
            self.states_list.append(self.current_bot['state'])
            restart = 1
            if u.interactive_enabled or u.simulation_enabled:
                restart = None
                while restart is None:
                    text = 'do you want to start a new session ?\t1- Yes\t0- No\n>>> Response: '
                    if simulation_enabled:
                        answer = self.user.get_answer(text)
                    else:
                        answer = input(text)
                    restart = fn.convert_to_int(answer)
                    if restart is None:
                        sorry_style = styles.get_sorry()
                        print(f'{sorry_style} your input is not valid')
            if restart:
                good_style = styles.get_good()
                print(f'{good_style} we are going to start a new session')
                self.restart = True
            else:
                self.restart = False
            # in any case here in_session should be False to stop the session
            # then we can restart a new session or completely finish
            self.update_parameters()
        except:
            print('Fail to manage the after submission')
            raise Exception

    def update_parameters(self):
        self.in_session = False
        self.counter = 0
        self.current_bot = None
        self.driver = None