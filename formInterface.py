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

    def interpretMessage(self, userInput):
        try:
            message = self.interpretMessage(userInput)
            if u.DEBUG:
                print("FORM INTERFACE interpretMessage")
            return message
        except:
            print("A problem occured while trying to interprete the user input <<{}>>".format(
                userInput))
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
                    # we reset the value of that field
                    self.state.filling_procedure(field, None)
                # we reset the current value
                self.state.reset_current_spelling_input_value()
                # the user interrupted a spelling and decided eiher to save or not to save. Now we go on with the action 
                # that interrupted the spelling
                waiting_message = self.state.get_waiting_message()
                # we add the message as the latest message
                self.state.add_latest_message(waiting_message)
                intent = waiting_message["intent"]["name"]
                self.state.set_waiting_message(None)
                utterance = self.findActionAndRun(intent=intent)
            elif intent not in [u.spelling_action, u.fill_form_action] and self.state.get_current_spelling_input_value() != '':
                # we are going to find a solution ad hoc for the spelling special characters
                if self.state.get_latest_message()["text"] in u.special_characters:
                    intent = u.spelling_action
                    utterance = self.findActionAndRun(intent=intent)
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
                # normal path, there is no spelling issue
                utterance = self.findActionAndRun(intent=intent)
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
    
    def findActionAndRun(self, intent):
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

    def fillGenericCamp(self):
        try:
            message = self.fillGenericCamp()
            if u.DEBUG:
                print("FORM INTERFACE fillGenericCamp")
            return message
        except:
            if not self.state.get_warning_present():
                print("A problem occured while trying to fill a camp")
            raise Exception

    def repeatValueCamp(self):
        try:
            message = self.repeatValueCamp()
            if u.DEBUG:
                print("FORM INTERFACE repeatValueCamp")
            return message
        except:
            if not self.state.get_warning_present():
                print("A problem occured while trying to repeat a camp")
            raise Exception

    def modifyValueGenericCamp(self):
        try:
            # almost identical to fillGenericCamp
            message = self.fillGenericCamp()
            if u.DEBUG:
                print("FORM INTERFACE modifyValueGenericCamp")
            return message
        except:
            if not self.state.get_warning_present():
                print("A problem occured while trying to modify a generic camp")
            raise Exception
        
    def resetAllCamps(self):
        try:
            message = self.resetAllCamps()
            if u.DEBUG:
                print("FORM INTERFACE resetAllCamps")
            return message
        except:
            if not self.state.get_warning_present():
                print("A problem occured while trying to reset all the camps")
            raise Exception

    def skipCamp(self):
        try:
            message = self.skipCamp()
            if u.DEBUG:
                print("FORM INTERFACE skipCamp")
            return message
        except:
            if not self.state.get_warning_present():
                print("A problem occured while trying to skip the camp")
            raise Exception

    def repeatRequiredLabels(self):
        try:
            message = self.repeatRequiredLabels()
            if u.DEBUG:
                print("FORM INTERFACE repeatRequiredLabels")
            return message
        except:
            if not self.state.get_warning_present():
                print("A problem occured while trying to repeat the Required labels")
            raise Exception

    def repeatOptionalLabels(self):
        try:
            message = self.repeatOptionalLabels()
            if u.DEBUG:
                print("FORM INTERFACE repeatOptionalLabels")
            return message
        except:
            if not self.state.get_warning_present():
                print("A problem occured while trying to repeat the optional labels")
            raise Exception
    
    def repeatAllLabels(self):
        try:
            message = self.repeatAllLabels()
            if u.DEBUG:
                print("FORM INTERFACE repeatAllLabels")
            return message
        except:
            if not self.state.get_warning_present():
                print("A problem occured while trying to repeat all the labels")
            raise Exception

    def giveRemainingRequiredLabels (self):
        try:
            message = self.giveRemainingRequiredLabels ()
            if u.DEBUG:
                print("FORM INTERFACE giveRemainingRequiredLabels ")
            return message
        except:
            if not self.state.get_warning_present():
                print("A problem occured while trying to give the remaining Required labels")
            raise Exception

    def giveRemainingOptionalLabels (self):
        try:
            message = self.giveRemainingOptionalLabels ()
            if u.DEBUG:
                print("FORM INTERFACE giveRemainingOptionalLabels ")
            return message
        except:
            if not self.state.get_warning_present():
                print("A problem occured while trying to give the remaining optional labels")
            raise Exception

    def giveAllRemainingLabels(self):
        try:
            message = self.giveAllRemainingLabels()
            if u.DEBUG:
                print("FORM INTERFACE giveAllRemainingLabels")
            return message
        except:
            if not self.state.get_warning_present():
                print("A problem occured while trying to give all the remaining labels")
            raise Exception

    def verifyValueFilledCamps(self):
        try:
            message = self.verifyValueFilledCamps()
            if u.DEBUG:
                print("FORM INTERFACE verifyValueFilledCamps")
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

    def verifyPresenceOfLabel(self):
        try:
            message = self.verifyPresenceOfLabel()
            if u.DEBUG:
                print("FORM INTERFACE verifyPresenceOfLabel")
            return message
        except:
            if not self.state.get_warning_present():
                print("A problem occured while trying to verify the presence of a label in the label list")
            raise Exception

    def explainLabel(self):
        try:
            message = self.explainLabel()
            if u.DEBUG:
                print("FORM INTERFACE explainLabel")
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
            # if the spelling is not yet operational, we treat the spelling as fillGenericCamp
            if not u.READY_FOR_SPELLING:
                message = self.fillGenericCamp()
            else:
                message = self.spelling()
            if u.DEBUG:
                print("FORM INTERFACE spelling")
            return message
        except:
            if not self.state.get_warning_present():
                print("A problem occured while trying to get a spelling character")
            raise Exception


    actions = [submitForm, fillGenericCamp, modifyValueGenericCamp, repeatValueCamp, skipCamp, 
        repeatRequiredLabels, repeatOptionalLabels, repeatAllLabels, giveRemainingRequiredLabels, 
        verifyValueFilledCamps, giveRemainingOptionalLabels, giveAllRemainingLabels, repeatFormTitle, 
        repeatFormExplanation, verifyPresenceOfLabel, explainLabel, affirm, deny, spelling, fillForm, 
        resetAllCamps]
