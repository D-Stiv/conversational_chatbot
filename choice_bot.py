import bots
from state import State
import utility as u
import functions as fn


class BotsManager:
    botList = []  # we assume that we don't have two forms of the same type on the same webpage

    def create_bots(self, driver):
        form_elements = driver.find_elements_by_tag_name('form')
        for form_element in form_elements:
            self.parse_web_form(form_element)

    def parse_web_form(self, form_element):
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
        try:
            for bot in self.botList:
                if bot.get_bot_tag() == bot_tag:
                    return bot
        except:
            print('Fail to get the bot')
            raise Exception

    def run_action(self, user_input, tag):
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
            latest_message = bot.interpret_message(user_input)
            # update the state
            state.add_latest_message(latest_message)
            # here we could look if there are some slots in the message and set them in the state

            # find the intent
            intent = latest_message["intent"]["name"]
            state.set_warning_present(False)
            utterance = bot.get_utterance(intent)
            return utterance
        except:
            print(f'Problem during the selection of the bot with tag <{tag}> and tha analysis of the user_input <{user_input}>')
            return u.EXCEPTION_MESSAGE

    