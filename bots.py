from rasa.nlu.model import Interpreter
import styles
import json
import os
from os import path
import utility as u
from form_interface import Form
import functions as fn
import asyncio
import rasa
import shutil
import time


class LoginForm(Form):
    root_folder = f'./{u.login_form_folder}'

    def __init__(
        self,
        state,
        bot_tag,
        model_folder=f'{root_folder}/{u.models_folder}',
        nlu_data_file_path=f'{root_folder}/{u.training_folder}/{u.nlu_data_file}',
        nlu_config_file_path=f'{root_folder}/{u.training_folder}/{u.nlu_config_file}'
    ):
        super().__init__(state, bot_tag, model_folder,
                         nlu_data_file_path, nlu_config_file_path)
        self.restricted_actions = u.restricted_actions
        self.model_path = None
        self.model_path_found = False

class RegistrationForm(Form):
    root_folder = f'./{u.registration_form_folder}'

    def __init__(
        self,
        state,
        bot_tag,
        model_folder=f'{root_folder}/{u.models_folder}',
        nlu_data_file_path=f'{root_folder}/{u.training_folder}/{u.nlu_data_file}',
        nlu_config_file_path=f'{root_folder}/{u.training_folder}/{u.nlu_config_file}'
    ):
        super().__init__(state, bot_tag, model_folder,
                         nlu_data_file_path, nlu_config_file_path)
        self.restricted_actions = u.restricted_actions
        self.model_path = None
        self.model_path_found = False

    def train_model(self):
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

    def interpret_message(self, user_input):
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
            latest_message = interpreter.parse(user_input)
            if u.DEBUG:
                print(f"interpret_message - message: \n{latest_message['intent']}")
            return latest_message
        except:
            print("A problem occured while a registration form bot tries to interprete the input <<{}>>".format(
                user_input))
            raise Exception

    def fillForm(self):
        try:
            # if the filling did not start, we give the form info to the user, otherwise we continue
            # with the next input_field.state variables to observe are num_camps, num_remaining, ...

            # we start by checking if the filling already started or not
            if self.state.get_filling_started():
                if self.state.get_close_prompt_enabled():
                    # we set the message to be returned to the user
                    string = fn.next_char_string()
                    self.state.set_possible_next_action(u.spelling_action)
                else:
                    string = self.state.manage_next_step()
                    _, required = self.state.get_next_slot()
                    if not required:
                        string = f'{string} otherwise, you can {u.fun_all_fields}, {u.fun_remaining_required_fields} or {u.fun_skip} '
                    else:
                        string = f'{string} otherwise, you can {u.fun_modify_field}'
                    already_filled = fn.get_pairs(self.state.form_slots(), only_filled=True)
                    fields_to_complete = self.state.get_fields_list(remaining=True)
                    if len(fields_to_complete) > 0:
                        if already_filled != '':
                            string = f'You are filling a Web Form and you still have to complete the following fields {fields_to_complete}.\nHere are the fields that you already completed:\n{already_filled}.\n{string}'
                        else:
                            string = f'You are filling a Web Form and you still have to complete the following fields {fields_to_complete}.\n{string}'                        
                return string
            # the filling did not start
            self.state.set_filling_started()
            form_title = self.state.get_form_title()
            if form_title is None:
                form_intro = "This form does not have a title."
            else:
                form_intro = f"The title of this form is {form_title}."
            form_desc = self.state.get_form_description()
            if form_desc is None:
                desc_intro = "it does not have a description."
            else:
                desc_intro = f"{form_desc}."
            # we format the string to retrieve
            first_string = self.state.manage_next_step()
            list_fields = self.state.get_fields_list()
            string_fields = fn.get_string_from_list(list_fields)
            string = (f"{form_intro} {desc_intro} this form contains the following fields: {string_fields}, from which {self.state.num_required_fields} are required" +
                      f" and {self.state.num_optional_fields} are optional.\nhere we go:\n{first_string}")
            return string
        except:
            if not self.state.get_warning_present():
                print(
                    "A problem occured while a registration form bot tries to start filling the form")
            raise Exception

    def fillGenericField(self):
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
                self.state.set_possible_next_action(u.fill_field_action)
                return string
            slot_name_list, slot_value_list = fn.extract_fields_names_and_values(
                entities)
            # we first verify if each slot_name corresponds to a field in the dorm
            correct, string = self.state.all_fields_present(slot_name_list)
            if not correct:
                return string
            """we extract now the spelling field and we insert them in the spelling list
            after that we fill the generic fields before passing the floor to 
            fillSpellingField to complete the fields in spelling list."""
            slot_name_list, slot_value_list = self.state.set_spelling_list(
                slot_name_list, slot_value_list)
            # the spelling list have been set and we can continue
            if len(slot_value_list) + len(slot_name_list) == 0:
                string = self.fillSpellingField()
                return string
            if len(slot_value_list) + len(slot_name_list) >= 1:
                # there is at least one generic info
                # the use of possible_next_action here is to mitigate training error. with a perfect training they are not necessary
                if len(slot_value_list) == 1 and len(slot_name_list) == 0 and (self.state.get_possible_next_action() == u.fill_field_action or intent == u.fill_field_action):
                    # we are inserting a value for the current field
                    slot_name = self.state.get_next_slot(only_name=True)   # return also if the next slot is required or not
                    # We make verify if the current field is spelling
                    spelling_fields = self.state.get_spelling_fields()
                    if slot_name in spelling_fields:
                        string = self.fillSpellingField()
                        return string
                    slot_value = slot_value_list[0]
                    # the slot value can change, being put in the right format
                    # we go to the filling procedure insuring that the field is not spelling
                    string = self.state.filling_procedure(slot_name, slot_value)
                elif self.state.get_possible_next_action() != u.fill_field_action and intent != u.fill_field_action:
                    # probably bad destination due to misinterpretation
                    sorry_style = styles.get_sorry()
                    please_style = styles.get_please()
                    text = f'{sorry_style} i do not understand your request, could you reformulate {please_style}?'
                    _, required = self.state.get_next_slot()
                    if not required:
                        text = f'{text} otherwise, you can {u.fun_skip} or {u.fun_submit}'
                    else:
                        text = f'{text} otherwise, you can {u.fun_explain_field} or {u.fun_complete_field}'
                    self.state.set_warning_message(text)
                    raise Exception
                else:
                    # we have a list of fields with their values
                    string = self.state.fill_generic_slots(slot_name_list=slot_name_list,
                                                     slot_value_list=slot_value_list)
            next_field_before = self.state.get_next_slot(only_name=True)
            # we verify if the spelling_list is empty or not
            if len(self.state.get_spelling_list()) != 0:
                string_spelling = self.fillSpellingField()
                next_field_after = self.state.get_next_slot(only_name=True)
                if next_field_before == next_field_after:
                    # the spelling did not modified the Web page, we return the string from the non spelling fields
                    return string
                # the spelling mofified the Web Form, so we use its string
                return string_spelling
            return string
        except:
            if not self.state.get_warning_present():
                print(
                    "A problem occured while a registration form bot tries to fill a camp")
            raise Exception

    def fillSpellingField(self):
        try:
            if len(self.state.get_spelling_list()) == 0:
                # misinterpretation
                text = 'I did not get you well, could you precise your action please?'
                _, required = self.state.get_next_slot()
                if not required:
                    text = f'{text} otherwise, you can {u.fun_skip}, {u.fun_reset} or {u.fun_submit}'
                else:
                    text = f'{text} otherwise, you can {u.fun_remaining_fields} or {u.fun_modify_field}'
                self.state.set_warning_message(text)
                raise Exception
            # we have to verify if we just finished the spelling of a field
            if self.state.get_after_spelling():
                # after spelling is desabled since we are going to insert the vale for a field
                self.state.set_after_spelling(False)
                slot_name = self.state.get_next_slot(only_name=True)
                slot_value = self.state.get_current_spelling_input_value()
                # we go to the filling procedure. The spelling list can be modified in this phase
                string = self.state.filling_procedure(slot_name, slot_value)
                if 'inserted!' in string.lower() and 'not' in string.lower():
                    self.state.reset_current_spelling_input_value()
                    return string
                # verify if all the fields in spelling list have been completed
                if len(self.state.get_spelling_list()) - 1 == 0:
                    self.state.reset_spelling_list()
                else:
                    # there are still fields to spell
                    self.state.update_spelling_list(slot_name)
                    next_field = self.state.get_spelling_list()[0]
                    please_style = styles.get_please()
                    string = (f"Web Form updated. Now you are going to spell the value for the field {next_field}.\n" +
                            f"{please_style} insert the first character")
                # after the spelling we insert the value for the given field and we reset the string
                self.state.reset_current_spelling_input_value()
                return string
            """we are not after spelling so the fillGenericField directly called this function(at the
            previous step it was triggered by the spelling function) or it is triggered by
            the mofifySpellingField function"""

            # we look if one of the fields in spelling fields has been saved to resume it. In case of many fields saved we take the first
            slot_name_list = self.state.get_spelling_list()
            saved_fields = self.state.get_saved_spelling_fields()
            if len(saved_fields) > 0:
                # there is at least one saved field
                for field in slot_name_list:
                    if field in saved_fields:
                        string = self.state.resume_spelling(field)
                        return string
            # we set the first spelling field of the list as the next field
            slot_name = slot_name_list[0]
            self.state.set_next_slot(slot_name)
            # we add styles to the output
            please_style = styles.get_please()
            end_style = styles.get_end()
            fields_string = fn.get_string_from_list(slot_name_list)
            if len(slot_name_list) == 1:
                intro = f"You will have to spell the value of the field {slot_name_list[0]}."
            else:
                intro = (f"You will have to spell the values of the following fields {fields_string}.\n" +
                         f"We start by the field {slot_name_list[0]}.")
            # we set the message to be returned to the user
            string = (f'{intro}\n{please_style} insert the first character, you will be able to use SPACE for spacing' +
                      f'and TERMINATE to {end_style} the spelling')
            self.state.set_possible_next_action(u.spelling_action)
            return string
        except:
            if not self.state.get_warning_present():
                print(
                    "A problem occured while a registration form bot tries to fill a spelling camp")
            raise Exception

    def spelling(self):
        try:
            if len(self.state.get_spelling_list()) == 0 or self.state.get_possible_next_action() != u.spelling_action:
                # misinterpretation
                latest_message = self.state.get_latest_message()
                latest_message['intent']['name'] = u.fill_field_action
                string = self.fillGenericField()
                return string
            all_types = u.alphabet + u.special_characters + u.terminator + u.spec_char_symbol
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
                self.state.set_possible_next_action(u.spelling_action)
                return string
            # verify if the input is for termination of the spelling
            for term in u.terminator:
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
                    string = self.fillSpellingField()
                    return string
            # we manage the case of special character which needs a translation
            if text.lower() in u.special_characters:
                index = u.special_characters.index(text)
                text = u.spec_char_symbol[index]
            # we are sure that the character inserted by the user is valid
            if self.state.get_current_spelling_input_value() == '':
                # we enable the close prompt because we receive the first character
                self.state.set_close_prompt_enabled()
            # we proceed by completting the current spelling input value
            self.state.complete_spelling_value(text)
            # we set the message to be returned to the user
            string = fn.next_char_string()
            self.state.set_possible_next_action(u.spelling_action)
            return string
        except:
            if not self.state.get_warning_present():
                print(
                    "A problem occured while a registration form bot tries to get a spelling")
            raise Exception

    def verifyPresenceOfField(self):
        try:
            entities = self.state.get_latest_message()["entities"]
            count = len(entities)
            if count == 0:
                # in principle should never occur given the training
                please_style = styles.get_please()
                text = f"{please_style} indicate which field you are interested to,"
                _, required = self.state.get_next_slot()
                if not required:
                    text = f'{text} otherwise, you can {u.fun_submit}, {u.fun_verify_presence_field} or {u.fun_skip}'
                else:
                    text = f'{text} otherwise, you can {u.fun_verify_value} or {u.fun_form_description}'
                self.state.set_warning_message(text)
                raise Exception
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

    def explainField(self):
        try:
            entities = self.state.get_latest_message()["entities"]
            count = len(entities)
            slot_name_list = fn.extract_fields_names_and_values(
                entities, only_names=True)
            if count == 0 or len(slot_name_list) == 0:
                # the user wants to explain the current field (next slot)
                field = self.state.get_next_slot(only_name=True)   # return also if the next slot is required or not
                field_desc = self.state.get_field_description(field)
                next_step_string = self.state.manage_next_step()
                string = f'{field_desc}\n{next_step_string}'
                return string
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
                text = f'{sorry_style} what exactly do you want to do? If you want, you can:\n{fn.get_functionalities_list()}'
                self.state.set_warning_message(text)
                raise Exception            
            string = self.state.manage_next_step()
            _, required = self.state.get_next_slot()
            if not required:
                string = f'{string} otherwise, you can {u.fun_all_fields}, {u.fun_remaining_required_fields} or {u.fun_skip} '
            else:
                string = f'{string} otherwise, you can {u.fun_remaining_required_fields} or {u.fun_form_title}'
            return string
        except:
            if not self.state.get_warning_present():
                print(
                    "A problem occured while a registration form bot tries to get an affirmation")
            raise Exception

    def deny(self):
        try:
           # we have to verify the state to know what is the deny for. the variable to check
            # is possible_next_action
            # another choice can be simply to ask the user what he wants to do.
            if self.state.get_next_slot(only_name=True) is not None:
                string = self.state.manage_next_step()
                _, required = self.state.get_next_slot()
                if not required:
                    string = f'{string} otherwise, you can {u.fun_remaining_required_fields}'
                else:
                    string = f'{string} otherwise, you can {u.fun_recap} or {u.fun_verify_value}'
                return string
            good_style = styles.get_good()
            string = f"{good_style}, what do you want to do now? you can:\n{fn.get_fuunctionalities_list()}"
            return string
        except:
            if not self.state.get_warning_present():
                print(
                    "A problem occured while a registration form bot tries to get a denial")
            raise Exception

    def repeatValueField(self):
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
            self.state.set_possible_next_action(u.fill_field_action)
            string = f'{string}\nDo you want to modify this value? if not you can {u.fun_resume}'
            return string
        except:
            if not self.state.get_warning_present():
                print(
                    "A problem occured while a registration form bot tries to repeat the value of a field")
            raise Exception

    def skipField(self):
        try:
            # we set the actual slot to campare it later with the next slot
            actual_slot_name = self.state.get_next_slot(only_name=True)    # return also if the next slot is required or not
            # we get the next slot without having filled the current slot and we verify if it is the last field
            self.state.set_next_slot_basic()
            next_slot_name, next_slot_required = self.state.get_next_slot()  # return also if the next slot is required or not
            if actual_slot_name == next_slot_name:
                sorry_style = styles.get_sorry()
                text = f"{sorry_style} this field is the last one remaining."
                if not next_slot_required:
                    opt = "Do you want to submit now?"
                    self.state.set_possible_next_action(u.submit_action)
                    string = f'{text}{opt} If yes, give an affirmative response otherwise {self.state.manage_next_step()}'
                else:
                    string = (f"{text} it is required to be able to submit the Web Form.\n" +
                            f"{self.fillForm()}")
                return string
            # we got to the next step
            string = self.state.manage_next_step()
            fields_remaining = self.state.get_fields_list(remaining=True)
            if self.state.get_all_required_filled() and len(fields_remaining) <= 2:
                string = f'If you want, you can {u.fun_submit}, otherwise {string}'
            else:
                string = f'The {actual_slot_name} has been skipped.\n{string}'
            return string
        except:
            if not self.state.get_warning_present():
                print(
                    "A problem occured while a registration form bot tries to skip a camp")
            raise Exception

    def repeatRequiredFields(self):
        try:
            sure_style = styles.get_sure()
            required_fields = self.state.get_fields_list(only_required=True)
            if len(required_fields) == 0:
                ans = 'There is no required field in this form'
            elif len(required_fields) == 1:
                ans = f'There is one required field in this form which is {required_fields[0]}'
            else:
                string_fields = fn.get_string_from_list(required_fields)
                ans = f"{sure_style} the required fields are the following: {string_fields}."
            string = self.state.manage_next_step()
            string = f"{ans}\n{string}"
            return string
        except:
            if not self.state.get_warning_present():
                print(
                    "A problem occured while a registration form bot tries to repeat Required labels")
            raise Exception

    def repeatOptionalFields(self):
        try:
            sure_style = styles.get_sure()
            optional_list = []
            slots = self.state.form_slots()
            for slot in slots:
                if slot[u.slot_name] != u.REQUESTED_SLOT:
                    if not slot[u.required]:
                        optional_list.append(slot[u.slot_name])
            optional_fields = fn.get_string_from_list(optional_list)
            ans = f"{sure_style} the optional fields are the following {optional_fields}."
            string = self.state.manage_next_step()
            string = f"{ans}\n{string}"
            return string
        except:
            if not self.state.get_warning_present():
                print(
                    "A problem occured while a registration form bot tries to repeat optional labels")
            raise Exception

    def repeatAllFields(self):
        try:
            all_fields = self.state.get_fields_list()
            string_fields = fn.get_string_from_list(all_fields)
            ans = f"The fields present in this form are the following: {string_fields}."
            next_step_string = self.state.manage_next_step()
            string = f"{ans}\n{next_step_string}"
            return string
        except:
            if not self.state.get_warning_present():
                print(
                    "A problem occured while a registration form bot tries to repeat all the labels")
            raise Exception

    def giveRemainingRequiredFields(self):
        try:
            sure_style = styles.get_sure()
            remaining_required_fields = self.state.get_fields_list(only_required=True, remaining=True)
            if len(remaining_required_fields) == 0:
                ans = 'There is no required field remaining'
            elif len(remaining_required_fields) == 1:
                ans = f'The only required field that remains is {remaining_required_fields[0]}'
            else:
                string_fields = fn.get_string_from_list(remaining_required_fields)
                ans = f"{sure_style} the remaining required fields are the following: {string_fields}."
            next_step_string = self.state.manage_next_step()
            string = f"{ans} \n{next_step_string}"
            return string
        except:
            if not self.state.get_warning_present():
                print(
                    "A problem occured while a registration form bot tries to give the remaining Required labels")
            raise Exception

    def giveRemainingOptionalFields(self):
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
            ans = f"{sure_style} the remaining optional fields are the following {optional_fields}."
            next_step_string = self.state.manage_next_step()
            string = f'{ans}\n{next_step_string}'
            return string
        except:
            if not self.state.get_warning_present():
                print(
                    "A problem occured while a registration form bot tries to give the remaining optional labels")
            raise Exception

    def giveAllRemainingFields(self):
        try:
            sure_style = styles.get_sure()
            all_remaining_fields = self.state.get_fields_list(remaining=True)
            if len(all_remaining_fields) == 0:
                ans = 'There is no field remaining'
            elif len(all_remaining_fields) == 1:
                ans = f'There is one field remaining and it is {all_remaining_fields[0]}'
            else:
                string_fields = fn.get_string_from_list(all_remaining_fields)
                ans = f"{sure_style} the remaining fields present in this form are the following: {string_fields}."
            string = self.state.manage_next_step()
            string = f'{ans}\n{string}'
            return string
        except:
            if not self.state.get_warning_present():
                print(
                    "A problem occured while a registration form bot tries to give all the remaining labels")
            raise Exception

    def verifyValueFilledFields(self):
        try:
            slots = self.state.form_slots()
            filled_string = fn.get_pairs(slots, only_filled=True)
            next_step_string = self.state.manage_next_step()
            if filled_string == '':
                sorry_style = styles.get_sorry()
                string = f'{sorry_style} up to now you did not complete any field\n{next_step_string}'
            else:
                string = (f"The fields you already completed are the following: \n{filled_string}\n" +
                        f"If you see some stars, they indicate the required fields.\n{next_step_string}")
            return string
        except:
            if not self.state.get_warning_present():
                print(
                    "A problem occured while a registration form bot tries to verify the value of the filled camps")
            raise Exception

    def repeatFormTitle(self):
        try:
            form_title = self.state.get_form_title()
            if form_title is None:
                string = "This form does not have a title."
            else:
                string = f"The title of this form is {form_title}."
            next_step_string = self.state.manage_next_step()
            string = f'{string}\n{next_step_string}'
            return string
        except:
            if not self.state.get_warning_present():
                print(
                    "A problem occured while a registration form bot tries to repeat the form's name")
            raise Exception

    def repeatFormExplanation(self):
        try:
            form_desc = self.state.get_form_description()
            next_step_string = self.state.manage_next_step()
            if form_desc is None:
                sorry_style = styles.get_sorry()
                string = f"{sorry_style} this form does not have a description.\n{next_step_string}"
                _, required = self.state.get_next_slot()
                if not required:
                    string = f'{string} otherwise, you can {u.fun_skip}'
                else:
                    string = f'{string} otherwise, you can {u.fun_recap} or {u.fun_verify_value}. In any case you will have to complete this field in order to submit'
            else:
                sure_style = styles.get_sure()
                string = f"{sure_style} here it is: {form_desc}."
                string = f'{string}\n{next_step_string}'
            return string
        except:
            if not self.state.get_warning_present():
                print(
                    "A problem occured while a registration form bot tries to repeat the form's explanation")
            raise Exception

    def resetAllFields(self):
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
                if slot_name != u.REQUESTED_SLOT:
                    required = slot[u.required]
                    slot_value = None
                    if not first_found:     # the first label is put as requested slot
                        self.state.set_next_slot(slot_name, required)
                        # we go to the filling procedure
                        self.state.filling_procedure(slot_name, slot_value)
                        first_found = True
                    else:
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
        try:
            remaining_required = self.state.get_fields_list(remaining=True, only_required=True)
            # we first verify if all the required fields are filled
            if len(remaining_required) > 0:
                # at least one required field is still empty
                initial_string = 'Not all the required fields are completed.'
                next_step_string = self.state.manage_next_step()
                if len(remaining_required) == 1:
                    string = f'{initial_string}\nYou should complete the field {remaining_required[0]}.\n{next_step_string}'
                elif len(remaining_required) > 1:
                    string_fields = fn.get_string_from_list(remaining_required)
                    string = f"{initial_string}\nYou still have to complete the following required fields {string_fields}.\n{next_step_string}"
                return string
            if u.DEBUG or not self.state.get_all_required_filled(): 
                print("inside submitForm")
            if not self.state.get_submit_alarm_enabled():
                recap = fn.get_pairs(self.state.form_slots())
                string = f"\n{recap}\nIf you would like to change something, let me know, otherwise confirm that you really want to continue with the submission?"
                self.state.set_possible_next_action(u.submit_action)
                # we enable the alarm
                self.state.set_submit_alarm_enabled()
                return string
            # we disable the alarm
            self.state.set_submit_alarm_enabled(False)
            elem = self.state.get_submit_button()
            elem.click()
            # we verify if the submission effectively occured
            try:
                # The point here is to avoid the Web Form to be submitted in the internal structure 
                # without being effectively submitted. It could be a matter of seconds so we put a sleep.
                elem = self.state.get_submit_button(verification=True)
                time.sleep(10)
                self.state.get_submit_button(verification=True).click()
                string = 'verification'
                if u.DEBUG:
                    print(string)
            except:
                # submission effective
                # we signify that the submit is done to have the title page
                self.state.set_submit_done()
                self.state.set_possible_next_action(None)
                string = 'Submission done'
                return string
            # submission not effective
            string = ('The submission is not effective due to a not valid value for a field. We advice you to restart the process from the beginning' +
                    '\nDo you accept to restart the process from the beginning?')
            self.state.set_reset_alarm_enabled()
            self.state.set_possible_next_action(u.reset_all_fields_action)
            return string
        except:
            if not self.state.get_warning_present():
                print(
                    "A problem occured while a registration form bot tries to submit a form")
            raise Exception