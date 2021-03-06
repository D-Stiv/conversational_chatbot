import state
import utility as u


class Form:
    def __init__(
        self,
        state,
        bot_tag,
        model_folder,
        nlu_data_file_path,
        nlu_config_file_path
    ):
        # initialize the form
        self.state = state
        self.bot_tag = bot_tag
        self.model_folder = model_folder
        self.nlu_data_file_path = nlu_data_file_path
        self.nlu_config_file_path = nlu_config_file_path

    def get_bot_tag(self):
        return self.bot_tag
    
    def get_state(self):
        return self.state

    def train_model(self):
        self.train_model()

    def interpret_message(self, user_input):
        try:
            message = self.interpretMessage(user_input)
            if u.DEBUG:
                print("FORM INTERFACE interpretMessage")
            return message
        except:
            print("A problem occured while trying to interpret the user input <<{}>>".format(
                user_input))
            raise Exception

    def get_utterance(self, intent):
        function_name = 'get_utterance'
        if u.DEBUG:
            print(f'Form: {function_name}')
        try:
            if self.state.get_reset_alarm_enabled():
                # we disable the alarm mainly in case intent not in [affirm, reset_all_fields]
                if intent not in [u.affirm_action, u.reset_all_fields_action]:
                    self.state.set_reset_alarm_enabled(False)
            elif self.state.get_submit_alarm_enabled():
                # we disable the alarm mainly in case intent not in [affirm, submit_form]
                if intent not in [u.affirm_action, u.submit_action]: 
                    # In case all the fields are completed, we tend to submit the Web Form
                    if self.state.get_next_slot(only_name=True) is None :
                        intent = u.affirm_action
                    else:                 
                        self.state.set_submit_alarm_enabled(False)
            if self.state.get_spelling_interrupted():
                # In the past the user interrupted a spelling and we wait for the response on whether to save the state or not
                if intent not in [u.affirm_action, u.deny_action]:
                    utterance = ('Please i would like to have a clear answer.\nWould you like to save the state of the field ' +
                        'that you started spelling ?\nIn case of negative response, that input will simply be canceled')
                    self.state.set_warning_message(utterance)
                    raise Exception
                self.state.set_spelling_interrupted(False)
                self.state.set_close_prompt_enabled(False)
                if intent == u.affirm_action:
                    # we insert the first element of the spelling list in the saved spelling
                    spelling_list = self.state.get_spelling_list()
                    field = spelling_list[0]
                    self.state.add_spelling_field_to_save(field)
                    spelling_list.remove(field)
                    # we insert the current spelling value in the list of saved values 
                    self.state.add_spelling_value_to_save(self.state.get_current_spelling_input_value())
                    # we reset the value of that field keeping the state unchanged: same next field, ...
                    self.state.filling_procedure(field, None, interrupt=True)
                # we reset the current value
                self.state.reset_current_spelling_input_value()
                # the user interrupted a spelling and decided eiher to save or not to save. Now we go on with the action 
                # that interrupted the spelling
                waiting_message = self.state.get_waiting_message()
                # we add the message as the latest message
                self.state.add_latest_message(waiting_message)
                intent = waiting_message["intent"]["name"]
                self.state.set_waiting_message(None)
                utterance = self.find_action_and_run(intent=intent)
            elif intent not in [u.spelling_action, u.fill_form_action] and self.state.get_current_spelling_input_value() != '':
                # we are going to find a solution ad hoc for the spelling special characters
                latest_message = self.state.get_latest_message()
                if latest_message["text"] in u.special_characters:
                    # misinterpretation
                    intent = u.spelling_action
                    latest_message["intent"]["name"] = u.spelling_action
                    utterance = self.find_action_and_run(intent=intent)
                    return utterance
                # the user started to spell an input and suddently interrupts it
                self.state.set_spelling_interrupted()
                # we get the latest message of the user
                message = self.state.get_latest_message()
                # we cancel the message from the massage history
                self.state.message_history.remove(message)
                # we save the latest message
                self.state.set_waiting_message(message)
                utterance = ('Do you want to save the state of the field that you started spelling?\nIn case of negative response, ' +
                    'that input will simply be canceled')
                self.state.set_warning_message(utterance)
                raise Exception
            else:
                latest_message = self.state.get_latest_message()
                if intent != u.spelling_action and len(latest_message["text"]) == 1:
                    # There is probably a misinterpretation
                    intent = u.spelling_action
                    latest_message["intent"]["name"] = u.spelling_action
                # normal path, there is no spelling issue
                utterance = self.find_action_and_run(intent=intent)
            return utterance
        except:
            if self.state.get_warning_present():
                # the message of the user was either out of context or not understood
                self.state.set_possible_next_action(None)
                utterance = self.state.get_warning_message()
            else:
                utterance = u.EXCEPTION_MESSAGE
                print('Fail to get a valid utterance')
            return utterance
    
    def find_action_and_run(self, intent):
        try:
            # find the action corresponding to the intent and run it
            action = self.get_action(intent)
            if action is None:
                next_step_string = self.state.manage_next_step()
                utterance = f"No action matches the intent.\n{next_step_string}"
                self.state.set_warning_message(utterance)
                raise Exception
            utterance = action(self)
            return utterance
        except:
            if not self.state.get_warning_present:
                print("A problem occured while trying to find an action to run")
            raise Exception

    def get_action(self, action_name):
        try:
            for action in self.actions:
                if action.__name__ == action_name:
                    return action
        except: 
            print(f'Fail to get the action {action_name}')
            raise Exception

    def fillForm(self):
        try:
            message = self.fillForm()
            if u.DEBUG:
                print("FORM INTERFACE fillForm")
            return message
        except:
            if not self.state.get_warning_present():
                print("A problem occured while trying to fill the form")
            raise Exception

    def submitForm(self):
        try:
            message = self.submitForm()
            if u.DEBUG:
                print("FORM INTERFACE submitForm")
            return message
        except:
            if not self.state.get_warning_present():
                print("A problem occured while trying to submit a form")
            raise Exception

    def fillGenericField(self):
        try:
            message = self.fillGenericField()
            if u.DEBUG:
                print("FORM INTERFACE fillGenericField")
            return message
        except:
            if not self.state.get_warning_present():
                print("A problem occured while trying to fill a camp")
            raise Exception

    def repeatValueField(self):
        try:
            message = self.repeatValueField()
            if u.DEBUG:
                print("FORM INTERFACE repeatValueField")
            return message
        except:
            if not self.state.get_warning_present():
                print("A problem occured while trying to repeat a camp")
            raise Exception

    def modifyValueGenericField(self):
        try:
            # almost identical to fillGenericField
            message = self.fillGenericField()
            if u.DEBUG:
                print("FORM INTERFACE modifyValueGenericField")
            return message
        except:
            if not self.state.get_warning_present():
                print("A problem occured while trying to modify a generic camp")
            raise Exception
        
    def resetAllFields(self):
        try:
            message = self.resetAllFields()
            if u.DEBUG:
                print("FORM INTERFACE resetAllFields")
            return message
        except:
            if not self.state.get_warning_present():
                print("A problem occured while trying to reset all the camps")
            raise Exception

    def skipField(self):
        try:
            message = self.skipField()
            if u.DEBUG:
                print("FORM INTERFACE skipField")
            return message
        except:
            if not self.state.get_warning_present():
                print("A problem occured while trying to skip the camp")
            raise Exception

    def repeatRequiredFields(self):
        try:
            message = self.repeatRequiredFields()
            if u.DEBUG:
                print("FORM INTERFACE repeatRequiredFields")
            return message
        except:
            if not self.state.get_warning_present():
                print("A problem occured while trying to repeat the Required labels")
            raise Exception

    def repeatOptionalFields(self):
        try:
            message = self.repeatOptionalFields()
            if u.DEBUG:
                print("FORM INTERFACE repeatOptionalFields")
            return message
        except:
            if not self.state.get_warning_present():
                print("A problem occured while trying to repeat the optional labels")
            raise Exception
    
    def repeatAllFields(self):
        try:
            message = self.repeatAllFields()
            if u.DEBUG:
                print("FORM INTERFACE repeatAllFields")
            return message
        except:
            if not self.state.get_warning_present():
                print("A problem occured while trying to repeat all the labels")
            raise Exception

    def giveRemainingRequiredFields (self):
        try:
            message = self.giveRemainingRequiredFields ()
            if u.DEBUG:
                print("FORM INTERFACE giveRemainingRequiredFields ")
            return message
        except:
            if not self.state.get_warning_present():
                print("A problem occured while trying to give the remaining Required labels")
            raise Exception

    def giveRemainingOptionalFields (self):
        try:
            message = self.giveRemainingOptionalFields ()
            if u.DEBUG:
                print("FORM INTERFACE giveRemainingOptionalFields ")
            return message
        except:
            if not self.state.get_warning_present():
                print("A problem occured while trying to give the remaining optional labels")
            raise Exception

    def giveAllRemainingFields(self):
        try:
            message = self.giveAllRemainingFields()
            if u.DEBUG:
                print("FORM INTERFACE giveAllRemainingFields")
            return message
        except:
            if not self.state.get_warning_present():
                print("A problem occured while trying to give all the remaining labels")
            raise Exception

    def verifyValueFilledFields(self):
        try:
            message = self.verifyValueFilledFields()
            if u.DEBUG:
                print("FORM INTERFACE verifyValueFilledFields")
            return message
        except:
            if not self.state.get_warning_present():
                print("A problem occured while trying to verify the value of the filled camps")
            raise Exception

    def repeatFormTitle(self):
        try:
            message = self.repeatFormTitle()
            if u.DEBUG:
                print("FORM INTERFACE repeatFormTitle")
            return message
        except:
            if not self.state.get_warning_present():
                print("A problem occured while trying to repeat the form's name")
            raise Exception

    def repeatFormExplanation(self):
        try:
            message = self.repeatFormExplanation()
            if u.DEBUG:
                print("FORM INTERFACE repeatFormExplanation")
            return message
        except:
            if not self.state.get_warning_present():
                print("A problem occured while trying to repeat the form explanation")
            raise Exception

    def verifyPresenceOfField(self):
        try:
            message = self.verifyPresenceOfField()
            if u.DEBUG:
                print("FORM INTERFACE verifyPresenceOfField")
            return message
        except:
            if not self.state.get_warning_present():
                print("A problem occured while trying to verify the presence of a label in the label list")
            raise Exception

    def explainField(self):
        try:
            message = self.explainField()
            if u.DEBUG:
                print("FORM INTERFACE explainField")
            return message
        except:
            if not self.state.get_warning_present():
                print("A problem occured while trying to explain the label")
            raise Exception

    def affirm(self):
        try:
            message = self.affirm()
            if u.DEBUG:
                print("FORM INTERFACE affirm")
            return message
        except:
            if not self.state.get_warning_present():
                print("A problem occured while trying to get an affirmation")
            raise Exception

    def deny(self):
        try:
            message = self.deny()
            if u.DEBUG:
                print("FORM INTERFACE deny")
            return message
        except:
            if not self.state.get_warning_present():
                print("A problem occured while trying to get a denial from the user")
            raise Exception

    def spelling(self):
        try:
            # if the spelling is not yet operational, we treat the spelling as fillGenericField
            if not u.USE_SPELLING:
                message = self.fillGenericField()
            else:
                message = self.spelling()
            if u.DEBUG:
                print("FORM INTERFACE spelling")
            return message
        except:
            if not self.state.get_warning_present():
                print("A problem occured while trying to get a spelling character")
            raise Exception


    actions = [submitForm, fillGenericField, modifyValueGenericField, repeatValueField, skipField, 
        repeatRequiredFields, repeatOptionalFields, repeatAllFields, giveRemainingRequiredFields, 
        verifyValueFilledFields, giveRemainingOptionalFields, giveAllRemainingFields, repeatFormTitle, 
        repeatFormExplanation, verifyPresenceOfField, explainField, affirm, deny, spelling, fillForm, 
        resetAllFields]
