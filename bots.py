from rasa.nlu.model import Interpreter
import styles
import json
import os
from os import path
import utility as u
from formInterface import Form
import functions as fn
import asyncio
import rasa
import shutil


EXCEPTION_MESSAGE = "Something went wrong during the handling of this message, please try another message !!"


class LoginForm(Form):
    root_folder = f'./{u.login_form_folder}'

    def __init__(
        self,
        domain_file_path=f'{root_folder}/{u.training_folder}/{u.domain_file}',
        model_folder=f'{root_folder}/{u.models_folder}',
        nlu_data_file_path=f'{root_folder}/{u.training_folder}/{u.nlu_data_file}',
        nlu_config_file_path=f'{root_folder}/{u.training_folder}/{u.nlu_config_file}'
    ):
        super().__init__(domain_file_path, model_folder,
                         nlu_data_file_path, nlu_config_file_path)
        self.restricted_actions = u.restricted_actions

class_name = 'RegistrationForm'
class RegistrationForm(Form):
    root_folder = f'./{u.registration_form_folder}'

    def __init__(
        self,
        state,
        bot_tag,
        domain_file_path=f'{root_folder}/{u.training_folder}/{u.domain_file}',
        model_folder=f'{root_folder}/{u.models_folder}',
        nlu_data_file_path=f'{root_folder}/{u.training_folder}/{u.nlu_data_file}',
        nlu_config_file_path=f'{root_folder}/{u.training_folder}/{u.nlu_config_file}'
    ):
        super().__init__(state, bot_tag, domain_file_path, model_folder,
                         nlu_data_file_path, nlu_config_file_path)
        self.restricted_actions = u.restricted_actions
        self.model_path = None
        self.model_path_found = False

    def train_model(self):
        function_name = 'train_model'
        if u.DEBUG:
            print(f'{class_name}: {function_name}')
        try:
            # if a previous training folder exists, we remove it
            previous_model = f'{self.model_folder}/{u.tag_registration_form}'
            if path.exists(previous_model):
                shutil.rmtree(f'{previous_model}', ignore_errors=True)
            # nlu training
            loop = asyncio.get_event_loop()
            loop.run_until_complete(rasa.nlu.train(
                nlu_config=self.nlu_config_file_path, data=self.nlu_data_file_path, path=self.model_folder, fixed_model_name=u.tag_registration_form))[1]
        except:
            print('Fail to train the conversational model')
            raise Exception

    def interpreteMessage(self, userInput):
        function_name = 'interpreteMessage'
        if u.DEBUG:
            print(f'{class_name}: {function_name}')
        try:
            def get_model_path():
                m_path = f'{self.model_folder}/{u.tag_registration_form}'
                json_file = 'metadata.json'
                found = False
                while not found:
                    if path.exists(f'{m_path}/{json_file}'):
                        found = True
                    else:
                        m_path = f'{m_path}/{u.tag_registration_form}'
                return m_path
            if not self.model_path_found:
                self.model_path = get_model_path()
                self.model_path_found = True
            interpreter = Interpreter.load(self.model_path)
            latest_message = interpreter.parse(userInput)
            if u.DEBUG:
                print(f"interpreteMessage - message: \n{latest_message['intent']}")
            return latest_message
        except:
            print("A problem occured while a registration form bot tries to interprete the input <<{}>>".format(
                userInput))
            raise Exception

    def fillForm(self):
        function_name = 'fillForm'
        if u.DEBUG:
            print(f'{class_name}: {function_name}')
        try:
            # if the filling did not start, we give the form info to the user, otherwise we continue
            # with the next input_field.state variables to observe are num_camps, num_remaining, ...

            # we start by checking if the filling already started or not
            if self.state.get_filling_started():
                if self.state.get_close_prompt_enabled():
                    # we set the message to be returned to the user
                    string = fn.next_char_string()
                else:
                    string = self.state.manage_next_step()
                return string
            # the filling did not start
            self.state.set_filling_started()
            form_title = self.state.get_form_title()
            if form_title is None:
                form_intro = "this form does not have a title."
            else:
                form_intro = "the title of this form is {}.".format(form_title)
            form_desc = self.state.get_form_description()
            if form_desc is None:
                desc_intro = "it does not have a description."
            else:
                desc_intro = "{}.".format(form_desc)
            # we format the string to retrieve
            first_string = self.state.manage_next_step()
            string = (f"{form_intro} {desc_intro} this form contains the following fields {self.state.get_fields_list()}, from which {self.state.num_required_fields} are required" +
                      f" and {self.state.num_optional_fields} are optional.\nhere we go:\n{first_string}")
            return string
        except:
            if not self.state.get_warning_present():
                print(
                    "A problem occured while a registration form bot tries to start filling the form")
            raise Exception

    def fillGenericCamp(self):
        function_name = 'fillGenericCamp'
        if u.DEBUG:
            print(f'{class_name}: {function_name}')
        try:
            entities = self.state.get_latest_message()["entities"]
            intent = self.state.get_latest_message()["intent"]["name"]
            count = len(entities)
            if count == 0:
                # the user wants to modify a field but did not specify which field
                modify_style = styles.get_modify()
                insert_style = styles.get_insert()
                string = (f"Which field exactly do you want to {modify_style}, and which value" +
                          f" do you want to {insert_style} for that field?")
                return string
            slot_name_list, slot_value_list = fn.extract_fields_names_and_values(
                entities)
            # we first verify if each slot_name corresponds to a field in the dorm
            correct, string = self.state.all_fields_present(slot_name_list)
            if not correct:
                return string
            """we extract now the spelling field and we insert them in the spelling list
            after that we fill the generic fields before passing the floor to 
            fillSpellingCamp to complete the fields in spelling list."""
            slot_name_list, slot_value_list = self.state.set_spelling_list(
                slot_name_list, slot_value_list)
            # the spelling list have been set and we can continue
            if len(slot_value_list) + len(slot_name_list) >= 1:
                # there is at least one generic info
                # the use of possible_next_action here is to mitigate training error. with a perfect training they are not necessary
                if len(slot_value_list) == 1 and len(slot_name_list) == 0 and (self.state.get_possible_next_action() == u.fill_field_action or intent == u.fill_field_action):
                    # we are inserting a value for the current field
                    slot_name = self.state.get_next_slot(only_name=True)   # return also if the next slot is required or not
                    slot_value = slot_value_list[0]
                    # the slot value can change, being put in the right format
                    # we go to the filling procedure insuring that the field is not spelling
                    string = self.state.filling_procedure(slot_name, slot_value)
                elif self.state.get_possible_next_action() != u.fill_field_action and intent != u.fill_field_action:
                    # probably bad destination due to training
                    sorry_style = styles.get_sorry()
                    please_style = styles.get_please()
                    text = f'{sorry_style} i did not understood your request, could reformulate {please_style}?'
                    self.state.set_warning_message(text)
                    raise Exception
                else:
                    # we have a list of fields with their values
                    string = self.state.fill_generic_slots(slot_name_list=slot_name_list,
                                                     slot_value_list=slot_value_list)
            # we verify if the spelling_list is empty or not
            if len(self.state.get_spelling_list()) != 0:
                string = self.fillSpellingCamp()
            return string
        except:
            if not self.state.get_warning_present():
                print(
                    "A problem occured while a registration form bot tries to fill a camp")
            raise Exception

    def fillSpellingCamp(self):
        function_name = 'fillSpellingCamp'
        if u.DEBUG:
            print(f'{class_name}: {function_name}')
        try:
            # we have to verify if we just finished the spelling of a field
            if self.state.get_after_spelling():
                # after spelling is desabled since we are going to insert the vale for a field
                self.state.set_after_spelling(False)
                slot_name = self.state.get_spelling_list()[0]
                slot_value = self.state.get_current_spelling_input_value()
                # we go to the filling procedure
                string = self.state.filling_procedure(slot_name, slot_value)
                self.state.reset_current_spelling_input_value()
                # verify if all the fields in spelling list have been completed
                if len(self.state.get_spelling_list()) - 1 == 0:
                    self.state.reset_spelling_list()
                else:
                    # there are still fields to spell
                    self.state.update_spelling_list(slot_name)
                    next_field = self.state.get_spelling_list()[0]
                    please_style = styles.get_please()
                    string = (f"Now you are going to spell the value for the field {next_field}.\n" +
                            f"{please_style} insert the first character")
                # after the spelling we insert the value for the given field and we reset the string
                self.state.reset_current_spelling_input_value()
                return string
            """we are not after spelling so the fillGenericCamp directly called this function(at the
            previous step it was triggered by the spelling function) or it is triggered by
            the mofifySpellingCamp function"""

            # we add styles to the output
            please_style = styles.get_please()
            end_style = styles.get_end()
            slot_name_list = self.state.get_spelling_list()
            fields_string = fn.get_string_from_list(slot_name_list)
            if len(slot_name_list) == 1:
                intro = f"you will have to spell the value of the field {slot_name_list[0]}."
            else:
                intro = (f"you will have to spell the values of the following fields {fields_string}.\n" +
                         f"We start by the field {slot_name_list[0]}.")
            # we set the message to be returned to the user
            string = (f'{intro}\n{please_style} insert the first character, you will be able to use SPACE for spacing' +
                      f'and TERMINATE to {end_style} the spelling')
            return string
        except:
            if not self.state.get_warning_present():
                print(
                    "A problem occured while a registration form bot tries to fill a spelling camp")
            raise Exception

    def spelling(self):
        function_name = 'spelling'
        if u.DEBUG:
            print(f'{class_name}: {function_name}')
        try:
            if len(self.state.get_spelling_list()) == 0:
                string = self.fillGenericCamp()
                return string
            if self.state.get_current_spelling_input_value() == '':
                # we enable the close prompt because we receive the first character
                self.state.set_close_prompt_enabled()
            alphabet = u.alphabet
            special_characters = u.special_characters
            spec_char_symbol = u.spec_char_symbol
            terminator = u.terminator
            all_types = alphabet + special_characters + terminator
            text = self.state.get_latest_message()["text"]
            # verify if text is a number
            is_number = False
            new_text = fn.convert_to_int(text)
            if new_text is not None:
                text = new_text
                is_number = True
            # verify if the text is valid
            if text.lower() not in all_types and not is_number:
                string = f'Your input {text} is not valid, try to insert only the character again please'
                self.state.set_warning_message(string)
                raise Exception
            # verify if the input is for termination of the spelling
            for term in terminator:
                if term in text.lower():
                    # we make sure the current spelling string is not void
                    value = self.state.get_current_spelling_input_value().replace(' ', '')
                    if value == '':
                        # we ask the user to insert at least one value different from blank.
                        text = self.state.manage_next_step()
                        string = f"You should insert at least one character different from blank.\n{text}"
                        return string
                    # we finished the spelling of a field and we have to fill it
                    self.state.set_after_spelling()
                    self.state.set_close_prompt_enabled(False)
                    # we proceed with the filling of the last field just spelt
                    # and we get the message for the next field to fill
                    string = self.fillSpellingCamp()
                    return string
            # we manage the case of special character which needs a translation
            if text.lower() in special_characters:
                index = special_characters.index(text)
                text = spec_char_symbol[index]
            # we proceed by completting the current spelling input value
            self.state.complete_spelling_value(text)
            # we set the message to be returned to the user
            string = fn.next_char_string()
            return string
        except:
            if not self.state.get_warning_present():
                print(
                    "A problem occured while a registration form bot tries to get a spelling")
            raise Exception

    def verifyPresenceOfLabel(self):
        function_name = 'verifyPresenceOfLabel'
        if u.DEBUG:
            print(f'{class_name}: {function_name}')
        try:
            entities = self.state.get_latest_message()["entities"]
            count = len(entities)
            if count == 0:
                # in principle should never occur given the training
                please_style = styles.get_please()
                string = f"{please_style} indicate which field you are interested to"
                return string
            slot_name_list = fn.extract_fields_names_and_values(
                entities, only_names=True)
            # we first verify if each slot_name corresponds to a field in the dorm
            correct, string = self.state.all_fields_present(slot_name_list)
            if not correct:
                return string
            good_style = styles.get_good()
            string = f"{good_style}, "
            for name in slot_name_list:
                text = fn.verify_presence(name, self.state.form_slots(), only_text=True)
                string = f'{string}, {text}'
            next_step_string = self.state.manage_next_step()
            string = f'{string}\n{next_step_string}'
            return string
        except:
            if not self.state.get_warning_present():
                print(
                    "A problem occured while a registration form bot tries to verify the presence of a label")
            raise Exception

    def explainLabel(self):
        function_name = 'explainLabel'
        if u.DEBUG:
            print(f'{class_name}: {function_name}')
        try:
            entities = self.state.get_latest_message()["entities"]
            count = len(entities)
            if count == 0:
                # the user wants to explain the current field (next slot)
                field = self.state.get_next_slot(only_name=True)   # return also if the next slot is required or not
                field_desc = self.state.get_field_description(field)
                next_step_string = self.state.manage_next_step()
                string = f'{field_desc}\n{next_step_string}'
                return string
            slot_name_list = fn.extract_fields_names_and_values(
                entities, only_names=True)
            # we first verify if each slot_name corresponds to a field in the dorm
            correct, string = self.state.all_fields_present(slot_name_list)
            if not correct:
                return string
            length = len(slot_name_list)
            string = ''
            for index in range(length):
                field_desc = self.state.get_field_description(slot_name_list[index])
                if string == '':
                    string = field_desc
                else:
                    string = f'{string}\n{field_desc}'
            next_step_string = self.state.manage_next_step()
            string = f'{string}\n{next_step_string}'
            return string
        except:
            if not self.state.get_warning_present():
                print(
                    "A problem occured while a registration form bot tries to explain a label")
            raise Exception

    def affirm(self):
        function_name = 'affirm'
        if u.DEBUG:
            print(f'{class_name}: {function_name}')
        try:
            # we have to verify the state to know what is the affirm for. the variable to check
            # is possible_next_action.
            action_name = self.state.get_possible_next_action()
            if action_name in [u.submit_action, u.reset_all_fields_action]:
                action = self.get_action(action_name)
                string = action(self)
                return string
            elif action_name is None:
                sorry_style = styles.get_sorry()
                string = f'{sorry_style} what exactly do you want to do ?'
                return string            
            string = self.state.manage_next_step()
            return string
        except:
            if not self.state.get_warning_present():
                print(
                    "A problem occured while a registration form bot tries to get an affirmation")
            raise Exception

    def deny(self):
        function_name = 'deny'
        if u.DEBUG:
            print(f'{class_name}: {function_name}')
        try:
           # we have to verify the state to know what is the deny for. the variable to check
            # is possible_next_action
            # another choice can be simply to ask the user what he wants to do.
            good_style = styles.get_good()
            string = "{}, what do you want to do now?".format(good_style)
            return string
        except:
            if not self.state.get_warning_present():
                print(
                    "A problem occured while a registration form bot tries to get a denial")
            raise Exception

    def repeatValueCamp(self):
        function_name = 'repeatValueCamp'
        if u.DEBUG:
            print(f'{class_name}: {function_name}')
        try:
            entities = self.state.get_latest_message()["entities"]
            fields = fn.extract_fields_names_and_values(
                entities, only_names=True)
            text = "{} : {}"
            string = "Here is the answer for you: "
            slots = self.state.form_slots()
            for slot in slots:
                slot_name = slot[u.slot_name]
                slot_value = slot[u.slot_value]
                if slot_name in fields:
                    if slot_value is None:
                        value = "No value"
                    else:
                        value = slot_value
                    string = f'{string}\n\t{text.format(slot_name, value)}'
            next_step_string = self.state.manage_next_step()
            string = f'{string}\n{next_step_string}'
            return string
        except:
            if not self.state.get_warning_present():
                print(
                    "A problem occured while a registration form bot tries to repeat the value of a field")
            raise Exception

    def skipCamp(self):
        function_name = 'skipCamp'
        if u.DEBUG:
            print(f'{class_name}: {function_name}')
        try:
            # we set the actual slot to campare it later with the next slot
            actual_slot_name = self.state.get_next_slot(only_name=True)    # return also if the next slot is required or not
            # we get the next slot without having filled the current slot and we verify if it is the last field
            self.state.set_next_slot_basic()
            next_slot_name, next_slot_required = self.state.get_next_slot()  # return also if the next slot is required or not
            if actual_slot_name == next_slot_name:
                sorry_style = styles.get_sorry()
                text = f"{sorry_style} this field is the last one remaining."
                opt = ""
                if not next_slot_required:
                    opt = "do you want to submit now?"
                    self.state.set_possible_next_action(u.submit_action)
                string = (f"{text} it is required to be able to submit the form.\n" +
                          f"{self.fillForm()}\n{opt}")
                return string
            # we got to the next step
            string = self.state.manage_next_step()
            return string
        except:
            if not self.state.get_warning_present():
                print(
                    "A problem occured while a registration form bot tries to skip a camp")
            raise Exception

    def repeatRequiredLabels(self):
        function_name = 'repeatRequiredLabels'
        if u.DEBUG:
            print(f'{class_name}: {function_name}')
        try:
            sure_style = styles.get_sure()
            required_fields = self.state.get_fields_list(only_required=True)
            ans = "{} the required fields are the following {}.".format(
                sure_style, required_fields)
            string = self.state.manage_next_step()
            string = f"{ans}\n{string}"
            return string
        except:
            if not self.state.get_warning_present():
                print(
                    "A problem occured while a registration form bot tries to repeat Required labels")
            raise Exception

    def repeatOptionalLabels(self):
        function_name = 'repeatOptionalLabels'
        if u.DEBUG:
            print(f'{class_name}: {function_name}')
        try:
            sure_style = styles.get_sure()
            optional_list = []
            slots = self.state.form_slots()
            for slot in slots:
                if slot[u.slot_name] != u.REQUESTED_SLOT:
                    if not slot[u.required]:
                        optional_list.append(slot[u.slot_name])
            optional_fields = fn.get_string_from_list(optional_list)
            ans = "{} the optional fields are the following {}.".format(
                sure_style, optional_fields)
            string = self.state.manage_next_step()
            string = f"{ans}\n{string}"
            return string
        except:
            if not self.state.get_warning_present():
                print(
                    "A problem occured while a registration form bot tries to repeat optional labels")
            raise Exception

    def repeatAllLabels(self):
        function_name = 'repeatAllLabels'
        if u.DEBUG:
            print(f'{class_name}: {function_name}')
        try:
            sure_style = styles.get_sure()
            all_fields = self.state.get_fields_list()
            ans = f"{sure_style} the fields present in this form are the following {all_fields}."
            next_step_string = self.state.manage_next_step()
            string = f"{ans}\n{next_step_string}"
            return string
        except:
            if not self.state.get_warning_present():
                print(
                    "A problem occured while a registration form bot tries to repeat all the labels")
            raise Exception

    def giveRemainingRequiredLabels(self):
        function_name = 'giveRemainingRequiredLabels'
        if u.DEBUG:
            print(f'{class_name}: {function_name}')
        try:
            sure_style = styles.get_sure()
            remaining_required_fields = self.state.get_fields_list(only_required=True, remaining=True)
            ans = "{} the remaining required fields are the following {}.".format(
                sure_style, remaining_required_fields)
            next_step_string = self.state.manage_next_step()
            string = f"{ans} \n{next_step_string}"
            return string
        except:
            if not self.state.get_warning_present():
                print(
                    "A problem occured while a registration form bot tries to give the remaining Required labels")
            raise Exception

    def giveRemainingOptionalLabels(self):
        function_name = 'giveRemainingOptionalLabels'
        if u.DEBUG:
            print(f'{class_name}: {function_name}')
        try:
            sure_style = styles.get_sure()
            remaining_optional_list = []
            slots = self.state.form_slots()
            for slot in slots:
                if slot[u.slot_name] != u.REQUESTED_SLOT:
                    if not slot[u.required]:
                        if slot[u.slot_value] is None:
                            # we add remaining optional fields
                            remaining_optional_list.append(slot[u.slot_name])
            optional_fields = fn.get_string_from_list(
                remaining_optional_list)
            ans = "{} the remaining optional fields are the following {}.".format(
                sure_style, optional_fields)
            next_step_string = self.state.manage_next_step()
            string = f'{ans}\n{next_step_string}'
            return string
        except:
            if not self.state.get_warning_present():
                print(
                    "A problem occured while a registration form bot tries to give the remaining optional labels")
            raise Exception

    def giveAllRemainingLabels(self):
        function_name = 'giveAllRemainingLabels'
        if u.DEBUG:
            print(f'{class_name}: {function_name}')
        try:
            sure_style = styles.get_sure()
            all_remaining_fields = self.state.get_fields_list(remaining=True)
            ans = "{} the remaining fields present in this form are the following {}.".format(
                sure_style, all_remaining_fields)
            string = self.state.manage_next_step()
            string = f'{ans}\n{string}'
            return string
        except:
            if not self.state.get_warning_present():
                print(
                    "A problem occured while a registration form bot tries to give all the remaining labels")
            raise Exception

    def verifyValueFilledCamps(self):
        function_name = 'verifyValueFilledCamps'
        if u.DEBUG:
            print(f'{class_name}: {function_name}')
        try:
            slots = self.state.form_slots()
            filled_string = fn.get_pairs(slots, only_filled=True)
            next_step_string = self.state.manage_next_step()
            if filled_string == '':
                sorry_style = styles.get_sorry()
                string = f'{sorry_style} up to now you did not complete any field\n{next_step_string}'
            else:
                string = (f"the fields you already completed are the following: \n{filled_string}\n" +
                        f"the stars indicate the required fields\n{next_step_string}")
            return string
        except:
            if not self.state.get_warning_present():
                print(
                    "A problem occured while a registration form bot tries to verify the value of the filled camps")
            raise Exception

    def repeatFormTitle(self):
        function_name = 'repeatFormTitle'
        if u.DEBUG:
            print(f'{class_name}: {function_name}')
        try:
            form_title = self.state.get_form_title()
            if form_title is None:
                string = "this form does not have a title."
            else:
                string = "the title of this form is {}.".format(form_title)
            next_step_string = self.state.manage_next_step()
            string = f'{string}\n{next_step_string}'
            return string
        except:
            if not self.state.get_warning_present():
                print(
                    "A problem occured while a registration form bot tries to repeat the form's name")
            raise Exception

    def repeatFormExplanation(self):
        function_name = 'repeatFormExplanation'
        if u.DEBUG:
            print(f'{class_name}: {function_name}')
        try:
            form_desc = self.state.get_form_description()
            if form_desc is None:
                sorry_style = styles.get_sorry()
                string = "{} this form does not have a description.".format(
                    sorry_style)
            else:
                sure_style = styles.get_sure()
                string = "{} here it is: {}.".format(sure_style, form_desc)
            next_step_string = self.state.manage_next_step()
            string = f'{string}\n{next_step_string}'
            return string
        except:
            if not self.state.get_warning_present():
                print(
                    "A problem occured while a registration form bot tries to repeat the form's explanation")
            raise Exception

    def resetAllCamps(self):
        function_name = 'resetAllCamps'
        if u.DEBUG:
            print(f'{class_name}: {function_name}')
        try:
            if not self.state.get_reset_alarm_enabled():
                string = "we are about to reset all the fields and restart the process.\n are you sure you want to continue with this action?"
                self.state.set_possible_next_action(u.reset_all_fields_action)
                # we enable the alarm
                self.state.set_reset_alarm_enabled()
                return string
            # we disable the alarm before continuing
            self.state.set_reset_alarm_enabled(False)
            # we reset the web form and then we reset the slots 
            elem = self.state.get_reset_button()
            elem.click()
            slots = self.state.form_slots()
            first_found = False
            for slot in slots:
                slot_name = slot[u.slot_name]
                required = slot[u.required]
                slot_value = None
                if not first_found:     # the first label is put as requested slot
                    self.state.set_next_slot(slot_name, required)
                    # we go to the filling procedure
                    self.state.filling_procedure(slot_name, slot_value)
                    first_found = True
                elif slot_name != u.REQUESTED_SLOT:
                    # we go to the filling procedure
                    self.state.filling_procedure(slot_name, slot_value)
            next_step_string = self.state.manage_next_step()
            string = f"All the fields have been reset, now we restart the process.\n{next_step_string}"
            return string
        except:
            if not self.state.get_warning_present():
                print(
                    "A problem occured while a registration form bot tries to reset all the camps")
            raise Exception

    def submitForm(self):
        function_name = 'submitForm'
        if u.DEBUG:
            print(f'{class_name}: {function_name}')
        try:
            # we first verify that all the required fields are filled
            if not self.state.get_all_required_filled():
                remaining_required = self.state.get_fields_list(
                    remaining=True, only_required=True)
                string = ("not all the required fields are completed.\n you still have" +
                          " to complete the following required fields {}").format(remaining_required)
                return f'{string}\n{self.state.manage_next_step()}'
            if u.DEBUG:
                print("inside submitForm")
            if not self.state.get_submit_alarm_enabled():
                string = "we are about to submit, are you sure you want to continue with this action?"
                self.state.set_possible_next_action(u.submit_action)
                # we enable the alarm
                self.state.set_submit_alarm_enabled()
                return string
            # we disable the alarm
            self.state.set_submit_alarm_enabled(False)
            elem = self.state.get_submit_button()
            elem.click()
            # we signify that the submit is done to have the title page
            self.state.set_submit_done()
            self.state.set_possible_next_action(None)
            string = 'submission done'
            return string
        except:
            if not self.state.get_warning_present():
                print(
                    "A problem occured while a registration form bot tries to submit a form")
            raise Exception