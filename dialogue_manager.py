import choice_bot
from selenium import webdriver
import utility as u
import functions as fn
import writers as w
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
        # initialize the the dialogue manager
        self.url = url
        self.browser = browser
        self.user = None
        self.driver = None
        self.log_writer = None
        self.counter = 0
        self.user_view = None
        self.chatbot_view = None
        self.bot_manager = choice_bot.BotsManager()
        self.current_bot = None
        self.in_session = False
        self.restart = False
        self.connected = True
        self.states_list = []
        self.total_iterations = u.MAX_DIALOGUES  # randint(1, u.MAX_DIALOGUES)
        self.iteration_number = 0
        self.number_fields = 0

    def initialize_views(self):
        self.log_writer = w.LogWriter()
        self.user_view = ViewChatPannel(self.log_writer, u.user_marker)
        self.chatbot_view = ViewChatPannel(self.log_writer, u.chatbot_marker)

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
            # we start a dialogue
            self.in_session = True
            self.current_bot = self.bot_manager.get_bot(bot_tag)
            self.number_fields = len(
                self.current_bot.get_state().form_slots()) - 1
            if u.simulation_enabled:
                text_fields = self.get_text_fields()
                choices_lists = self.get_choices_lists()
                self.user = User(text_fields, choices_lists)
            if u.train_model:
                self.current_bot.train_model()
            self.conversation_prologue()
            self.start_dialogue()
            if self.restart:
                # we reset the botList for the new dialogue
                self.bot_manager.botList = []
                self.create_form_bots()
                if u.DEBUG:
                    print('About to start the new dialogue')
                self.start(bot_tag)
            self.close_window()
        except:
            if self.connected:
                print(PREPROCESSING_EXCEPTION)
                self.close_window()

    def close_window(self):
        # we effectively close the windows only if we are not supposed to write the report
        # since the report requires the windows to be open in order to fetch the form elements
        if not u.write_report or True:
            # we close the driver
            try:
                self.driver.close()
            except:
                pass

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
            elif self.browser == 'edge':
                driver = webdriver.Edge()
            else:
                driver = webdriver.Chrome()
            if u.simulation_enabled:
                i = self.iteration_number % len(u.urls)
                self.url = u.urls[i]
            driver.get(self.url)
            driver.minimize_window()
            self.driver = driver
        except:
            print('Fail to instantiate the driver')
            raise Exception

    def conversation_prologue(self):
        try:
            # call fillForm woith a predefined message and present the form
            initial_string = 'fill the form'
            message = self.current_bot.interpret_message(initial_string)
            introduction = self.current_bot.find_action_and_run(
                message["intent"]["name"])
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
                    control = self.counter % min(
                        u.COEFF*self.number_fields, u.CONTROL_FREQUENCE)
                    if self.counter > 1 and control in [0, 1]:
                        answer = input(
                            '[Control Message: Do you want to proceed with the simulation?\t0 - No, 1 - Yes]\n[Your response: ')
                        if answer != '1':
                            a = u.stop
                    """end of the control, the simulation can proceed normally"""
                else:
                    a = input("Your input: ")
                if a == u.stop:
                    self.restart = False
                    break
                if a != "":
                    text = f'Your input: {a}'
                    self.user_view.show_text(self.counter, text)
                    self.counter += 1
                    response = self.bot_manager.run_action(
                        user_input=a, tag=u.tag_registration_form)
                    text = f"response: {response}"
                    # we verify whether or not the submission have benn done
                    if not my_state.get_submit_done():
                        self.chatbot_view.show_text(self.counter, text)
                        self.counter += 1
                        # we verify that we are still connected, if we are not connected the exception will be raised
                        try:
                            my_state.form_element.parent.title
                        except:
                            self.connected = False
                            raise Exception
                    else:
                        self.after_submit()
                    if self.in_session:
                        # we frequently show the situation of the fields
                        notification = self.counter % min(
                            u.COEFF*self.number_fields, u.NOTIFICATION_FREQUENCE)
                        if notification in [0, 1]:
                            text = self.current_bot.get_state().get_slots_value()
                            self.chatbot_view.show_notifications(text)
                else:
                    text = 'You did not insert any value'
                    self.chatbot_view.show_text(self.counter, text)
                    self.counter += 1
        except:
            if self.connected:
                print('Problem during the dialogue')
                self.conclude_log()
                self.write_log()
            else:
                print('ERROR: Connection lost')
            raise Exception

    def after_submit(self):
        try:
            """Here we conclude the submission of the form and then we start or not a new
            dialogue. If we start a new dialogue, we restart from the beginning.
            Each time, the state is saved to write the final report"""
            # we increment the nunmer of iteration
            self.iteration_number += 1

            newPageTitle = self.driver.title
            good_style = styles.get_good()
            text = f"{good_style} you have been moved to the page with title {newPageTitle}"
            self.chatbot_view.show_text(self.counter, text)
            self.counter += 1
            # we conclude this log
            self.conclude_log()
            # we add the state to the list
            self.states_list.append(self.current_bot.get_state())
            # we sample the reports not to loose everything in case of problem
            if self.iteration_number in [30]:
                # write the report
                w.ReportWriter(self.states_list).start()
                self.write_log()
            if self.iteration_number >= self.total_iterations:
                self.restart = False
                self.in_session = False
                return
            restart = None
            while restart is None:
                text = '\n[ALERT: Would you like to start a new dialogue ?\t1- Yes\t0- No\n>>> Response: '
                if u.simulation_enabled:
                    dialogue_state = self.get_dialogue_state()
                    answer = self.user.get_answer(dialogue_state)
                else:
                    answer = input(text)
                try:
                    restart = int(fn.convert_to_int(answer))
                    if restart is None:
                        sorry_style = styles.get_sorry()
                        print(f'{sorry_style} your input is not valid')
                except:
                    sorry_style = styles.get_sorry()
                    print(f'{sorry_style} your input is not valid')
            if restart:
                good_style = styles.get_good()
                print(f'{good_style} we are going to start a new dialogue')
                self.restart = True
                # in any case here in_session should be False to stop the dialogue
                # then we can restart a new dialogue or completely finish
                self.update_parameters()
            else:
                self.restart = False
                self.in_session = False
        except:
            print('Fail to manage the after submission')
            raise Exception

    def update_parameters(self):
        try:
            self.in_session = False
            self.counter = 0
            self.current_bot = None
            self.close_window()
        except:
            print('Fail to update the parameters')
            raise Exception

    def get_dialogue_state(self):
        try:
            state = self.current_bot.get_state()
            next_slot_name = state.get_next_slot(only_name=True)
            if next_slot_name is None:
                value_name = None
                value_type = None
            else:
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

            if next_slot_name is not None and value_type in u.number_types_list:
                dialogue_state[u.min_value] = slot[u.min_value]
                dialogue_state[u.max_value] = slot[u.max_value]
                dialogue_state[u.precision] = slot[u.precision]

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
        try:
            # retrieves the fields of type text
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

    def write_log(self):
        if u.write_log:
            self.log_writer.start()
            if u.DEBUG:
                print('Log written')

    def conclude_log(self):
        try:
            self.chatbot_view.show_end_of_conversation(self.counter)
            self.chatbot_view.show_new_dialogue(self.iteration_number)
            self.counter = 0
        except:
            print('Fail to conclude the log')
            raise Exception
