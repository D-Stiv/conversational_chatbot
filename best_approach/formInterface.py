import state
import utility as u


class Form:
    def __init__(
        self,
        domain_file_path,
        model_folder,
        nlu_data_file_path,
        nlu_config_file_path
    ):
        # initialize the form
        self.domain_file_path = domain_file_path
        self.model_folder = model_folder
        self.nlu_data_file_path = nlu_data_file_path
        self.nlu_config_file_path = nlu_config_file_path

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

    def get_action(self, action_name):
        try:
            for action in self.actions:
                if action.__name__ == action_name:
                    return action
        except: 
            print(f'Fail to get the action {action_name}')
            raise Exception

    def fillForm(self, state):
        try:
            message = self.fillForm(state)
            if u.DEBUG:
                print("FORM INTERFACE fillForm")
            return message
        except:
            if not state.warning_present:
                print("A problem occured while trying to fill the form")
            raise Exception

    def submitForm(self, state):
        try:
            message = self.submitForm(state)
            if u.DEBUG:
                print("FORM INTERFACE submitForm")
            return message
        except:
            if not state.warning_present:
                print("A problem occured while trying to submit a form")
            raise Exception

    def fillGenericCamp(self, state):
        try:
            message = self.fillGenericCamp(state)
            if u.DEBUG:
                print("FORM INTERFACE fillGenericCamp")
            return message
        except:
            if not state.warning_present:
                print("A problem occured while trying to fill a camp")
            raise Exception

    def repeatValueCamp(self, state):
        try:
            message = self.repeatCamp(state)
            if u.DEBUG:
                print("FORM INTERFACE repeatCamp")
            return message
        except:
            if not state.warning_present:
                print("A problem occured while trying to repeat a camp")
            raise Exception

    def modifyValueGenericCamp(self, state):
        try:
            message = self.modifyValueGenericCamp(state)
            if u.DEBUG:
                print("FORM INTERFACE modifyValueGenericCamp")
            return message
        except:
            if not state.warning_present:
                print("A problem occured while trying to modify a generic camp")
            raise Exception

    def modifyValueSpellingCamp(self, state):
        try:
            if not u.READY_FOR_SPELLING:
                message = self.modifyValueGenericCamp(state)
            else:
                message = self.modifyValueSpellingCamp(state)
            if u.DEBUG:
                print("FORM INTERFACE modifyValueSpellingCamp")
            return message
        except:
            if not state.warning_present:
                print("A problem occured while trying to modify a spelling camp")
            raise Exception

    def findActionAndRun(self, intent):
        try:
            message = self.findActionAndRun(state)
            if u.DEBUG:
                print("FORM INTERFACE findActionAndRun")
            return message
        except:
            print("A problem occured while trying to find an action to run")
            raise Exception
        
    def resetAllCamps(self, state):
        try:
            message = self.resetAllCamps(state)
            if u.DEBUG:
                print("FORM INTERFACE resetAllCamps")
            return message
        except:
            if not state.warning_present:
                print("A problem occured while trying to reset all the camps")
            raise Exception

    def skipCamp(self, state):
        try:
            message = self.skipCamp(state)
            if u.DEBUG:
                print("FORM INTERFACE skipCamp")
            return message
        except:
            if not state.warning_present:
                print("A problem occured while trying to skip the camp")
            raise Exception

    def repeatRequiredLabels(self, state):
        try:
            message = self.repeatRequiredLabels(state)
            if u.DEBUG:
                print("FORM INTERFACE repeatRequiredLabels")
            return message
        except:
            if not state.warning_present:
                print("A problem occured while trying to repeat the Required labels")
            raise Exception

    def repeatOptionalLabels(self, state):
        try:
            message = self.repeatOptionalLabels(state)
            if u.DEBUG:
                print("FORM INTERFACE repeatOptionalLabels")
            return message
        except:
            if not state.warning_present:
                print("A problem occured while trying to repeat the optional labels")
            raise Exception
    
    def repeatAllLabels(self, state):
        try:
            message = self.repeatAllLabels(state)
            if u.DEBUG:
                print("FORM INTERFACE repeatAllLabels")
            return message
        except:
            if not state.warning_present:
                print("A problem occured while trying to repeat all the labels")
            raise Exception

    def giveRemainingRequiredLabels (self, state):
        try:
            message = self.giveRemainingRequiredLabels (state)
            if u.DEBUG:
                print("FORM INTERFACE giveRemainingRequiredLabels ")
            return message
        except:
            if not state.warning_present:
                print("A problem occured while trying to give the remaining Required labels")
            raise Exception

    def giveRemainingOptionalLabels (self, state):
        try:
            message = self.giveRemainingOptionalLabels (state)
            if u.DEBUG:
                print("FORM INTERFACE giveRemainingOptionalLabels ")
            return message
        except:
            if not state.warning_present:
                print("A problem occured while trying to give the remaining optional labels")
            raise Exception

    def giveAllRemainingLabels(self, state):
        try:
            message = self.giveAllRemainingLabels(state)
            if u.DEBUG:
                print("FORM INTERFACE giveAllRemainingLabels")
            return message
        except:
            if not state.warning_present:
                print("A problem occured while trying to give all the remaining labels")
            raise Exception

    def verifyValueFilledCamps(self, state):
        try:
            message = self.verifyValueFilledCamps(state)
            if u.DEBUG:
                print("FORM INTERFACE verifyValueFilledCamps")
            return message
        except:
            if not state.warning_present:
                print("A problem occured while trying to verify the value of the filled camps")
            raise Exception

    def repeatFormName(self, state):
        try:
            message = self.repeatFormName(state)
            if u.DEBUG:
                print("FORM INTERFACE repeatFormName")
            return message
        except:
            if not state.warning_present:
                print("A problem occured while trying to repeat the form's name")
            raise Exception

    def repeatFormExplanation(self, state):
        try:
            message = self.repeatFormExplanation(state)
            if u.DEBUG:
                print("FORM INTERFACE repeatFormExplanation")
            return message
        except:
            if not state.warning_present:
                print("A problem occured while trying to repeat the form explanation")
            raise Exception

    def verifyPresenceOfLabel(self, state):
        try:
            message = self.verifyPresenceOfLabel(state)
            if u.DEBUG:
                print("FORM INTERFACE verifyPresenceOfLabel")
            return message
        except:
            if not state.warning_present:
                print("A problem occured while trying to verify the presence of a label in the label list")
            raise Exception

    def explainLabel(self, state):
        try:
            message = self.explainLabel(state)
            if u.DEBUG:
                print("FORM INTERFACE explainLabel")
            return message
        except:
            if not state.warning_present:
                print("A problem occured while trying to explain the label")
            raise Exception

    def affirm(self, state):
        try:
            message = self.affirm(state)
            if u.DEBUG:
                print("FORM INTERFACE affirm")
            return message
        except:
            if not state.warning_present:
                print("A problem occured while trying to get an affirmation")
            raise Exception

    def deny(self, state):
        try:
            message = self.deny(state)
            if u.DEBUG:
                print("FORM INTERFACE deny")
            return message
        except:
            if not state.warning_present:
                print("A problem occured while trying to get a denial from the user")
            raise Exception

    def fillSpellingCamp(self, state):
        try:
            if not u.READY_FOR_SPELLING:
                message = self.fillGenericCamp(state)
            else:
                message = self.fillSpellingCamp(state)
            if u.DEBUG:
                print("FORM INTERFACE fillSpellingCamp")
            return message
        except:
            if not state.warning_present:
                print("A problem occured while trying to fill a spelling camp")
            raise Exception

    def spelling(self, state):
        try:
            # if the spelling is not yet operational, we treat the spelling as fillGenericCamp
            if not u.READY_FOR_SPELLING:
                message = self.fillGenericCamp(state)
            else:
                message = self.spelling(state)
            if u.DEBUG:
                print("FORM INTERFACE spelling")
            return message
        except:
            if not state.warning_present:
                print("A problem occured while trying to get a spelling character")
            raise Exception


    actions = [submitForm, fillGenericCamp, modifyValueGenericCamp, repeatValueCamp,  
                skipCamp, repeatRequiredLabels, repeatOptionalLabels,
                repeatAllLabels, giveRemainingRequiredLabels, verifyValueFilledCamps,
                giveRemainingOptionalLabels, giveAllRemainingLabels, repeatFormName,
                repeatFormExplanation, verifyPresenceOfLabel, explainLabel, affirm, 
                deny, spelling, fillSpellingCamp, fillForm, modifyValueSpellingCamp,
                resetAllCamps]
