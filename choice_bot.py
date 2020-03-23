import bots
from state import State
import utility as u
import functions as fn

EXCEPTION_MESSAGE = "Something went wrong during the handling of this message.\n what can i precisely do for you please ?"


class BotsManager:
    botList = []  # we assume that we don't have two forms of the same type on the same webpage

    def run_action(self, state, userInput, tag):
        try:
            # for the moment we assume that the user input goes to registration form which
            # is the only type we have up to now
            bot = None
            for element in self.botList:
                if element["tag"] == tag:
                    bot = element["bot"]
            if bot == None:
                print(
                    "Trying to access a non existing form type with tag >> {} <<".format(tag))
                # the bot requested is not available yet, so we are going to handle the message
                # using the registration_form_bot
                bot = element[u.tag_registration_form]
            latest_message = bot.interpreteMessage(userInput)
            # update the state
            state.add_latest_message(latest_message)
            # here we could look if there are some slots in the message and set them in the state

            # find the intent
            intent = latest_message["intent"]["name"]
            state.set_warning_present(False)
            utterance = bot.findActionAndRun(state=state, intent=intent)
            return utterance
        except:
            if state.warning_present:
                utterance = state.warning_message
            else:
                utterance = EXCEPTION_MESSAGE
                print("A problem occured while trying to run the action for user input <<{}>> and bot tag <<{}>>".format(
                        userInput, tag))
            return utterance

    def create_bots(self, driver):
        form_elements = driver.find_elements_by_tag_name('form')
        for form_element in form_elements:
            self.parse_web_form(form_element)

    def parse_web_form(self, form_element):
        try:
            bot_tag = form_element.get_attribute('bot-tag')
            slots = fn.get_input_fields(form_element)
            constructs = {
                "text": None,
                "list": None,
                "form": {
                    "slots": slots
                }
            }
            my_state = State(form_element=form_element, constructs=constructs)
            try:
                new = {}
                if bot_tag == u.tag_registration_form:
                    new = {
                        "bot": bots.RegistrationForm(),
                        "state": my_state,
                        "tag": bot_tag
                    }
                elif bot_tag == u.tag_login_form:
                    new = {
                        "bot": bots.LoginForm(),
                        "state": my_state,
                        "tag": bot_tag
                    }
                self.botList.append(new)
            except:
                print("Fail to constitute the bots list")
                raise Exception
        except:
            print('Fail to parse the Web Form')
            raise Exception

    def get_bot(self, bot_tag):
        try:
            for bot in self.botList:
                if bot['tag'] == bot_tag:
                    return bot
        except:
            print('Fail to get the bot')
            raise Exception
