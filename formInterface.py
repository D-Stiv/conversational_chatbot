import state
import utility as u


class Form:
    def __init__(
        self,
        state,
        bot_tag,
        domain_file_path,
        model_folder,
        nlu_data_file_path,
        nlu_config_file_path
    ):
        # initialize the form
        self.state = state
        self.bot_tag = bot_tag
        self.domain_file_path = domain_file_path
        self.model_folder = model_folder
        self.nlu_data_file_path = nlu_data_file_path
        self.nlu_config_file_path = nlu_config_file_path

    def get_bot_tag(self):
        return self.bot_tag
    
    def get_state(self):
        return self.state

    def train_model(self):
        self.train_model()

    def interpreteMessage(self, userInput):
        try:
            message = self.interpreteMessage(userInput)
            if u.DEBUG:
                print("FORM INTERFACE interpreteMessage")
            return message
        except:
            print("A problem occured while trying to interprete the user input <<{}>>".format(
                userInput))
            raise Exception

    def findActionAndRun(self, intent):
        try:
            # find the action corresponding to the intent and run it
            utterance = "No action matches the intent"
            action = self.get_action(intent)
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
