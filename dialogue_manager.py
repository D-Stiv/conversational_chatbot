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
            if u.simulation_enabled:
                self.instantiate_driver(True)
            else:
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
                text_fields = self.get_text_fields()
                choices_lists = self.get_choices_lists()
                self.user = User(text_fields, choices_lists)
            if u.train_model:
                self.current_bot.train_model()
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

    def instantiate_driver(self, random=False):
        try:
            if random:
                browsers = u.browsers
                index = randint(0, len(browsers)-1)
                browser = browsers[index]
                self.browser = browser
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
            # call fillForm woith a predefined message and present the form
            initial_string = 'fill the form'
            message = self.current_bot.interpreteMessage(initial_string)
            introduction = self.current_bot.findActionAndRun(message["intent"]["name"])
            stop_string = f"Start of the conversation, to end your should type <<{u.stop}>>."
            text = f'{stop_string}\n{introduction}'
            self.chatbot_view.show_text(self.counter, text)
            self.counter += 1
        except:
            print('Fail to implement the prologue of the conversation')
            raise Exception

    def start_dialogue(self):
        try:
            my_state = self.current_bot.get_state()
            # beginning of the interaction
            text = ''
            while True and self.in_session:
                if u.simulation_enabled:
                    dialogue_state = self.get_dialogue_state()
                    a = self.user.get_answer(dialogue_state)
                    """we insert a control to be be able to manually stop the simulation"""
                    control = self.counter % u.CONTROL_FREQUENCE
                    if self.counter > 1 and control in [0, 1]:
                        answer = input('[Control Message: Do you want to proceed with the simulation?\t0 - No, 1 - Yes]\n[Your response: ')
                        if answer != '1':
                            a = u.stop
                    """end of the control, the simulation can proceed normally"""
                else:
                    a = input("Your input: ")
                if a == u.stop:
                    self.chatbot_view.show_end_of_conversation(self.counter)
                    self.restart = False
                    break
                if a != "":
                    text = f'Your input: {a}'
                    self.user_view.show_text(self.counter, text)
                    self.counter += 1
                    response = self.bot_manager.run_action(
                        userInput=a, tag=u.tag_registration_form)
                    text = f"response: {response}"
                    # we verify whether or not the submission have benn done
                    if not my_state.get_submit_done():
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
            self.states_list.append(self.current_bot.get_state())
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

    def get_dialogue_state(self):
        try:
            state = self.current_bot.get_state()
            next_slot_name, _ = state.get_next_slot()
            slot = state.get_slot(next_slot_name)
            value_name = slot[u.value_name]
            value_type = slot[u.value_type]

            dialogue_state = {
                u.close_prompt_enabled: state.get_close_prompt_enabled(),
                u.spelling_interrupted: state.get_spelling_interrupted(),
                u.warning_present: state.get_warning_present(),
                u.all_required_filled: state.get_all_required_filled(),
                u.submit_alarm_enabled: state.get_submit_alarm_enabled(),
                u.reset_alarm_enabled: state.get_reset_alarm_enabled(),
                u.submit_done: state.get_submit_done(),
                u.possible_next_action: state.get_possible_next_action(),
                u.value_name: value_name,
                u.value_type: value_type,
                u.slot_name: next_slot_name
            }
            return dialogue_state
        except:
            print('Fail to get the state of the dialogue')
            raise Exception

    def get_choices_lists(self):
        try:
            # give the choices lists and the list of fields
            state = self.current_bot.get_state()
            slots = state.get_slots()
            choices_lists = {}
            for slot in slots:
                if u.choice_list in slot.keys():
                    choices_lists[slot[u.value_name]] = slot[u.choice_list]
            return choices_lists
        except:
            print('Fail to get the choices lists')
            raise Exception

    def get_text_fields(self):
        # retrieves the fields of type text
        try:
            state = self.current_bot.get_state()
            slots = state.get_slots()
            text_fields = []
            for slot in slots:
                if slot[u.slot_name] != u.REQUESTED_SLOT:
                    if slot[u.value_type] == u.text:
                        text_fields.append(slot[u.slot_name])
            return text_fields
        except:
            print('Fail to get the fields of type text')
            raise Exception
