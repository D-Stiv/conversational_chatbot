import bots
from state import State
import utility as u
import functions as fn

EXCEPTION_MESSAGE = "Something went wrong during the handling of this message.\n what can i precisely do for you please ?"

class_name = 'BotsManager'
class BotsManager:
    botList = []  # we assume that we don't have two forms of the same type on the same webpage

    def create_bots(self, driver):
        form_elements = driver.find_elements_by_tag_name('form')
        for form_element in form_elements:
            self.parse_web_form(form_element)

    def parse_web_form(self, form_element):
        function_name = 'parse_web_form'
        if u.DEBUG:
            print(f'{class_name}: {function_name}')
        try:
            bot_tag = form_element.get_attribute(u.bot_tag)
            slots = fn.get_input_fields(form_element)
            constructs = {
                u.text_construct: None,
                u.list_construct: None,
                u.form_construct: {
                    u.slots: slots
                }
            }
            my_state = State(form_element=form_element, constructs=constructs)
            try:
                if bot_tag == u.tag_registration_form:
                    bot = bots.RegistrationForm(my_state, bot_tag)
                elif bot_tag == u.tag_login_form:
                    bot = bots.LoginForm(my_state, bot_tag)
                self.botList = [bot] + self.botList
            except:
                print("Fail to constitute the bots list")
                raise Exception
        except:
            print('Fail to parse the Web Form')
            raise Exception

    def get_bot(self, bot_tag):
        function_name = 'get_bot'
        if u.DEBUG:
            print(f'{class_name}: {function_name}')
        try:
            for bot in self.botList:
                if bot.get_bot_tag() == bot_tag:
                    return bot
        except:
            print('Fail to get the bot')
            raise Exception

    def run_action(self, userInput, tag):
        function_name = 'run_action'
        if u.DEBUG:
            print(f'{class_name}: {function_name}')
        try:
            # for the moment we assume that the user input goes to registration form which
            # is the only type we have up to now
            bot = None
            for my_bot in self.botList:
                if my_bot.get_bot_tag() == tag:
                    bot = my_bot
                    break
            if bot == None:
                print(
                    "Trying to access a non existing form type with tag >> {} <<".format(tag))
                # the bot requested is not available yet, so we are going to handle the message
                # using the registration_form_bot
                bot = self.get_bot(u.tag_registration_form)
            # we get the state of the bot
            state = bot.get_state()
            latest_message = bot.interpreteMessage(userInput)
            # update the state
            state.add_latest_message(latest_message)
            # here we could look if there are some slots in the message and set them in the state

            # find the intent
            intent = latest_message["intent"]["name"]
            state.set_warning_present(False)
            utterance = self.get_utterance(bot, intent)
            return utterance
        except:
            if state.get_warning_present():
                # the message of the user was either out of context or not understood
                state.set_possible_next_action(None)
                utterance = state.get_warning_message()
            else:
                utterance = EXCEPTION_MESSAGE
                print("A problem occured while trying to run the action for user input <<{}>> and bot tag <<{}>>".format(
                        userInput, tag))
            return utterance

    def get_utterance(self, bot, intent):
        function_name = 'get_utterance'
        if u.DEBUG:
            print(f'{class_name}: {function_name}')
        try:
            # we get the state of the bot
            state = bot.get_state()
            if state.get_reset_alarm_enabled():
                # we disable the alarm mainly in case intent not in [affirm, deny]
                if intent not in [u.affirm_action, u.deny_action, u.reset_all_fields_action]:
                    state.set_reset_alarm_enabled(False)
            elif state.get_submit_alarm_enabled():
                # we disable the alarm mainly in case intent not in [affirm, deny]
                if intent not in [u.affirm_action, u.deny_action, u.submit_action]:                        
                    state.set_submit_alarm_enabled(False)
            if state.get_spelling_interrupted():
                # In the past the user interrupted a spelling and we wait for the response on whether to save the state or not
                if intent not in [u.affirm_action, u.deny_action]:
                    utterance = ('Please i would like to have a clear answer.\nWould you like to save the state of the field ' +
                        'that you started spelling ?\nIn case of negative response, that input will simply be canceled')
                    state.set_warning_message(utterance)
                    raise Exception
                state.set_spelling_interrupted(False)
                state.set_close_prompt_enabled(False)
                if intent == u.affirm_action:
                    # we insert the first element of the spelling list in the saved spelling
                    spelling_list = state.get_spelling_list()
                    field = spelling_list[0]
                    state.add_spelling_field_to_save(field)
                    spelling_list.remove(field)
                    # we insert the current spelling value in the list of saved values 
                    state.add_spelling_value_to_save(state.get_current_spelling_input_value())
                # we reset the current value
                state.reset_current_spelling_input_value()
                # the user interrupted a spelling and decided eiher to save or not to save. Now we go on with the action 
                # that interrupted the spelling
                intent = state.get_waiting_intent()
                state.set_waiting_intent(None)
                utterance = bot.findActionAndRun(intent=intent)
            elif intent not in [u.spelling_action, u.fill_form_action] and state.get_current_spelling_input_value() != '':
                # we are going to find a solution ad hoc for the spelling 'dot'
                if state.get_latest_message()["text"] == 'dot':
                    intent = u.spelling_action
                    utterance = bot.findActionAndRun(intent=intent)
                    return utterance
                # the user started to spell an input and suddently interrupts it
                state.set_spelling_interrupted()
                state.set_waiting_intent(intent)
                utterance = ('Do you want to save the state of the field that you started spelling?\nIn case of negative response, ' +
                    'that input will simply be canceled')
                state.set_warning_message(utterance)
                raise Exception
            else:
                # normal path, there is no spelling issue
                utterance = bot.findActionAndRun(intent=intent)
            return utterance
        except:
            if not state.get_warning_present():
                print('Fail to get the utterance')
            raise Exception