import copy
import logging
import typing
from typing import Any, Dict, Iterator, List, Optional, Text
from selenium.webdriver.support.ui import Select
import utility as u
import functions as fn
import styles

logger = logging.getLogger(__name__)
class_name = 'State'

class State:

    def __init__(
        self,
        form_element,
        constructs={},  # Text, Form, List, ...
    ) -> None:
        """Initialize the tracker."""

        try:
            self.message_history = []
            self.constructs = constructs
            self.form_element = form_element
            self.num_total_fields, self.num_required_fields, self.num_optional_fields = fn.get_num_fields(
                constructs)
            self.num_required_remaining = self.num_required_fields
            self.spelling_state = self.initialize_spelling_sate()
            self.machine_parameters = self.initialize_machine_parameters(first_slot=constructs['form']['slots'][0])
        except:
            print("ERROR: A problem occured while initializing the state")
        
    def initialize_machine_parameters(self, first_slot):
        machine_parameters = {
            u.filling_started: False,
            u.submit_done: False,
            u.reset_alarm_enabled: False,
            u.submit_alarm_enabled: False,
            u.warning_present: False,
            u.all_required_filled: False,
            u.possible_next_action: None,
            u.warning_message: '',
            u.next_slot: first_slot[u.slot_name],   # in principle it should never be u.REQUESTED_SLOT
            u.next_slot_required: first_slot[u.required]
        }
        return machine_parameters

    def initialize_spelling_sate(self):
        spelling_state = {
            u.close_prompt_enabled: False,   # True when we are in spelling mode
            u.current_spelling_input_value: '',
            u.spelling_interrupted: False,
            u.spelling_list: [],
            u.after_spelling: False,
            u.waiting_message: None,
            u.saved_spelling_fields: [],
            u.saved_spelling_values: []
        }
        return spelling_state

    def get_slots(self):
        return self.constructs[u.form_construct][u.slots]

    def get_latest_message(self):
        return self.message_history[len(self.message_history)-1]

    def set_possible_next_action(self, action_name):
        self.machine_parameters[u.possible_next_action] = action_name

    def get_possible_next_action(self):
        return self.machine_parameters[u.possible_next_action]

    def set_reset_alarm_enabled(self, value=True):
        self.machine_parameters[u.reset_alarm_enabled] = value

    def get_reset_alarm_enabled(self):
        return self.machine_parameters[u.reset_alarm_enabled]

    def set_submit_alarm_enabled(self, value=True):
        self.machine_parameters[u.submit_alarm_enabled] = value

    def get_submit_alarm_enabled(self):
        return self.machine_parameters[u.submit_alarm_enabled]
    
    def set_submit_done(self, value=True):
        self.machine_parameters[u.submit_done] = value

    def get_submit_done(self):
        return self.machine_parameters[u.submit_done]

    def set_filling_started(self, value=True):
        self.machine_parameters[u.filling_started] = value

    def get_filling_started(self):
        return self.machine_parameters[u.filling_started]

    def add_spelling_field_to_save(self, field):
        self.spelling_state[u.saved_spelling_fields].append(field)

    def get_saved_spelling_fields(self):
        return self.spelling_state[u.saved_spelling_fields]

    def add_spelling_value_to_save(self, value):
        self.spelling_state[u.saved_spelling_values].append(value)
    
    def get_saved_spelling_values(self):
        return self.spelling_state[u.saved_spelling_values]

    def get_waiting_message(self):
        return self.spelling_state[u.waiting_message]
    
    def set_waiting_message(self, message):
        self.spelling_state[u.waiting_message] = message

    def get_spelling_interrupted(self):
        return self.spelling_state[u.spelling_interrupted]

    def set_spelling_interrupted(self, value=True):
        self.spelling_state[u.spelling_interrupted] = value

    def get_spelling_list(self):
        return self.spelling_state[u.spelling_list]

    def set_spelling_list(self, slot_name_list, slot_value_list):
        function_name = 'set_spelling_list'
        if u.DEBUG:
            print(f'{class_name}: {function_name}')
        try:
            """the idea here is to separate the spelling and non spelling fields.
            for the spelling fields, the value is not important, since we will retake it.
            we set the spelling_list and we return the non spelling data"""
            spelling_fields = self.get_spelling_fields()
            name_list = []
            value_list = []
            spelling_list = []
            num_value = len(slot_value_list)
            length = len(slot_name_list)
            for index in range(length):
                slot_name = slot_name_list[index]
                if slot_name in spelling_fields:
                    spelling_list.append(slot_name)
                else:
                    name_list.append(slot_name)
                    if index < num_value:
                        # we have to make sure thet the value is present
                        slot_value = slot_value_list[index]
                        value_list.append(slot_value)
            if len(slot_name_list) < num_value:
                length = len(slot_name_list)
                for index in range(length, num_value):
                    slot_value = slot_value_list[index]
                    value_list.append(slot_value)
            self.spelling_state[u.spelling_list] = spelling_list
            return name_list, value_list
        except:
            print('ERROR: Fail to get the spelling list')
            raise Exception

    def get_spelling_fields(self):
        function_name = 'get_spelling_fields'
        if u.DEBUG:
            print(f'{class_name}: {function_name}')
        try:
            spelling_fields = []
            slots = self.form_slots()
            for slot in slots:
                if slot[u.slot_name] != u.REQUESTED_SLOT:
                    if slot[u.spelling]:
                        spelling_fields.append(slot[u.slot_name])
            return spelling_fields
        except:
            print('ERROR: Fail to get the spelling fields')
            raise Exception

    def add_spelling_name(self, slot_name):
        if slot_name not in self.spelling_state[u.spelling_list]:
            self.spelling_state[u.spelling_list].append(slot_name)

    def get_required_fields(self):
        function_name = 'get_required_fields'
        if u.DEBUG:
            print(f'{class_name}: {function_name}')
        try:
            required_fields = []
            slots = self.form_slots()
            for slot in slots:
                if slot[u.slot_name] != u.REQUESTED_SLOT:
                    if slot[u.required]:
                        required_fields.append(slot[u.slot_name])
            return required_fields
        except:
            print('ERROR: Fail to get the spelling fields')
            raise Exception

    def set_next_slot(self, slot_name, required):
        function_name = 'set_next_slot'
        if u.DEBUG:
            print(f'{class_name}: {function_name}')
        try:
            self.machine_parameters[u.next_slot] = slot_name
            self.machine_parameters[u.next_slot_required] = required
            # we modify also the next_slot in the slots
            self.set_slot(u.REQUESTED_SLOT, slot_name)
        except:
            print(f'ERROR: Fail to set the next slot to be {slot_name}')
            raise Exception

    def update_spelling_list(self, slot_name):
        self.spelling_state[u.spelling_list].remove(slot_name)

    def reset_current_spelling_input_value(self):
        self.spelling_state[u.current_spelling_input_value] = ""

    def reset_spelling_list(self):
        self.spelling_state[u.spelling_list] = []

    def set_after_spelling(self, value=True):
        self.spelling_state[u.after_spelling] = value
    
    def get_after_spelling(self):
        return self.spelling_state[u.after_spelling]

    def set_close_prompt_enabled(self, value=True):
        self.spelling_state[u.close_prompt_enabled] = value

    def get_close_prompt_enabled(self):
        return self.spelling_state[u.close_prompt_enabled]

    # Modifies the state inserting the latest message which is the message of the last user input
    def add_latest_message(self, message):
        self.message_history.append(message)

    def set_warning_present(self, value=True):
        self.machine_parameters[u.warning_present] = value
        if value == False:
            self.machine_parameters[u.warning_message] = ''
    
    def get_warning_present(self):
        return self.machine_parameters[u.warning_present]

    # extracts and restitutes the slots present in the form with their values
    def form_slots(self):
        function_name = 'form_slots'
        if u.DEBUG:
            print(f'{class_name}: {function_name}')
        try:
            slots = self.constructs["form"]["slots"]
            return slots
        except:
            print("ERROR: A problem occured while extracting the slots")
            raise Exception

    # Gets the value of a given slot
    def get_slot(self, slot_name):
        function_name = 'get_slot'
        if u.DEBUG:
            print(f'{class_name}: {function_name}')
        try:
            slots = self.form_slots()
            for slot in slots:
                if slot[u.slot_name] == slot_name:
                    return slot
            # the field we are looking for is not in the form
            if u.DEBUG:
                print(f'The field {slot_name} is not in the form')
            sorry_style = styles.get_sorry()
            please_style = styles.get_please()
            text = f"{sorry_style} the field {slot_name} is not present in this form.{please_style} could you precise the action you want to perform?"
            self.set_warning_message(text)
            raise Exception
        except:
            if not self.get_warning_present():
                print(f"ERROR: Fail to get the field --> {slot_name} <--")
            raise Exception

    # inserts the value in a given slot
    def set_slot(self, slot_name, slot_value):
        function_name = 'set_slot'
        if u.DEBUG:
            print(f'{class_name}: {function_name}')
        try:
            exists = False
            slots = self.form_slots()
            for existing_slot in slots:
                if slot_name == existing_slot[u.slot_name]:
                    exists = True
                    existing_slot[u.slot_value] = slot_value
                    break
            if not exists:
                fields_list = self.get_fields_list()
                text = f'The name {slot_name} does not correspond to any label. the fields present are the following {fields_list}.\nwhich field do you want to modify?'
                self.set_warning_message(text)
                raise Exception
        except:
            print(f"ERROR: A problem occured while trying to put the value {slot_value} in the slot {slot_name}")
            raise Exception

    def set_warning_message(self, text):
        if text != u.VOID:
            # we also set the warning present to True since there is a message
            self.set_warning_present()
        self.machine_parameters[u.warning_message] = text
        

    def get_warning_message(self):
        return self.machine_parameters[u.warning_message]

    # return all the slots with their name and their value
    def get_slots_value(self):
        function_name = 'get_slots_value'
        if u.DEBUG:
            print(f'{class_name}: {function_name}')
        try:
            slots_value = {}
            slots = self.form_slots()
            for slot in slots:
                slot_name = slot[u.slot_name]
                slot_value = slot[u.slot_value]
                slots_value[slot_name] = slot_value
            return slots_value
        except:
            print('[ERROR: Fail to get the value of the fields')
            raise Exception

    # Restitutes the value (slot) of the required slot
    def get_requested_slot(self):
        function_name = 'get_requested_slot'
        if u.DEBUG:
            print(f'{class_name}: {function_name}')
        try:
            slots = self.form_slots()
            for slot in slots:
                if slot[u.slot_name] == u.REQUESTED_SLOT:
                    slot_name = slot[u.slot_value]
            return slot_name
        except:
            print("ERROR: A problem occured while fetching the value of required_slot")
            raise Exception

    # Restitutes the next slot's name
    def get_next_slot(self, only_name=False):
        function_name = 'get_next_slot'
        if u.DEBUG:
            print(f'{class_name}: {function_name}')
        try:
            if only_name:
                return self.machine_parameters[u.next_slot]
            else:
                return self.machine_parameters[u.next_slot], self.machine_parameters[u.next_slot_required]
        except:
            print("ERROR: A problem occured while getting the next slot")
            raise Exception

    # sets the next field (slot) according to the order of the web form
    def set_next_slot_basic(self):
        function_name = 'set_next_slot_basic'
        if u.DEBUG:
            print(f'{class_name}: {function_name}')
        try:
            slot_name = self.get_next_slot(only_name=True)
            # we try to take in sequence the first empty field after the current field
            actual_found = False
            slots = self.form_slots()
            for slot in slots:
                if slot[u.slot_name] != u.REQUESTED_SLOT and slot[u.value_type] not in u.non_supported_types:
                    if actual_found:
                        # we are after the actual field
                        if slot[u.slot_value] is None:
                            self.set_next_slot(
                                slot[u.slot_name], slot[u.required])
                            return 
                    if slot[u.slot_name] == slot_name:
                        actual_found = True
            # there is no empty field after the current field, we try to look before
            for slot in slots:
                if slot[u.slot_name] != u.REQUESTED_SLOT and slot[u.value_type] not in u.non_supported_types:
                    if slot[u.slot_value] is None:
                        self.set_next_slot(
                            slot[u.slot_name], slot[u.required])
                        return 
                    if slot[u.slot_name] == slot_name:
                        # we returned at the starting point, so two cases:
                        if slot[u.slot_value] is not None:
                            # we completed all the fields, next slot is None
                            self.set_next_slot(None, None)
                        # otherwise the user wanted to skip but the field is the last to fill
                        return 
        except:
            print('ERROR: Fail to get the next slot for skipping case')
            raise Exception

    # Transforms the choices list into text and restitutes
    def get_next_slot_text(self, slot_name, slot_required):
        function_name = 'get_next_slot_text'
        if u.DEBUG:
            print(f'{class_name}: {function_name}')
        try:
            types_with_options = u.choices_type_list
            slot = self.get_slot(slot_name)
            value_type = slot[u.value_type]
            required_string = fn.get_required_string(slot_required)
            if value_type in types_with_options:
                choice_list = slot[u.choice_list]
                option_string = fn.get_string_from_list(choice_list)
                if value_type in [u.dropdown, u.checkbox]:
                    string = f"Select the {slot_name} in the following list {option_string}. {required_string}"
                elif value_type == u.radio:
                    string = f"Choose your {slot_name} in the following list {option_string}. {required_string}"
                if u.DEBUG:
                    print("choice list")
                    print(choice_list)
            else:
                insert_style = styles.get_insert()
                please_style = styles.get_please()
                string = f"{please_style} {insert_style} the value for the field {slot_name}. {required_string}"
            return string
        except:
            print("ERROR: Fail to extract the text for the next slot")
            raise Exception

    # Inserts the value inside the web page (form) with the label corrisponding to the slot
    def fill_input(self, slot_name, slot_value):
        function_name = 'fill_input'
        if u.DEBUG:
            print(f'{class_name}: {function_name}')
        # returns the slot value eventually modified to be in the right format, and a string to 
        # eventuelly mention some incopatibilities
        try:
            string = ""
            # substitute the underscores with spaces to outpu the right message
            input_type_list = u.input_type_list
            slot = self.get_slot(slot_name)
            value_type = slot[u.value_type]
            value_name = slot[u.value_name]
            # the slot_value is not None
            if u.DEBUG:
                print(f"value_name: {value_name}, value_type: {value_type}")
            compatible, text = fn.is_compatible(slot_value, slot)
            if not compatible:
                next_step_string = self.manage_next_step()
                string = f'{text}\n{next_step_string}'
                return None, string
            # the value and the type are compatible so it is pssible that the value has been converted
            # to an appropriate form contained in text
            slot_value = text
            if value_type in input_type_list:
                elem = self.form_element.find_element_by_name(value_name)
                elem.clear()
                if slot_value is None:
                    return "", string
                elem.send_keys(slot_value)
                return slot_value, string
            # the value_type is in u.choices_list
            # the value is put in lowercase to coincide with the choice
            slot_value = slot_value.lower()
            if u.DEBUG:
                print(f"choice: {slot_value}")
            # we verify that slot_value is in the list of choices
            choice_list = slot[u.choice_list]
            length = len(choice_list)
            for index in range(length):
                choice_list[index] = choice_list[index].lower()
            if slot_value not in choice_list:
                sorry_style = styles.get_sorry()
                please_style = styles.get_please()
                string = (f"{sorry_style} the choice {slot_value} is not valid for the field {slot_name}" +
                        f"{please_style} choose one in the following list: {choice_list}")
                return None, string
            # we are sure that the choice of the user is in the list of choices
            if value_type == u.dropdown:
                self.set_choice_dropdown(
                    slot_name=slot_name, choice_value=slot_value)
            elif value_type == u.checkbox:
                self.set_choice_checkbox(
                    slot_name=slot_name, choice_value=slot_value)
            elif value_type == u.radio:
                self.set_choice_radio(
                    slot_name=slot_name, choice_value=slot_value)
            return slot_value, string
        except:
            string = f'The value {slot_value} is not valid for the field {slot_name}'
            return None, string

    # Select the choice_value of the user for the dropdown with the given name
    def set_choice_dropdown(self, slot_name, choice_value):
        function_name = 'set_choice_dropdown'
        if u.DEBUG:
            print(f'{class_name}: {function_name}')
        try:
            slot = self.get_slot(slot_name)
            choice_name = slot[u.value_name].lower()
            select = Select(self.form_element.find_element_by_name(choice_name))
            if choice_value is None:
                # the choice_value is to select the first element
                select.select_by_index(0)
            else:
                select.select_by_value(choice_value)                    
        except:
            print(f"ERROR: A problem occured while trying to set the choice_value {choice_value} in the dropdown with name {choice_name}")
            raise Exception

    # Select the choice_value of the user for the radio with the given name
    def set_choice_radio(self, slot_name, choice_value):
        function_name = 'set_choice_radio'
        if u.DEBUG:
            print(f'{class_name}: {function_name}')
        try:
            slot = self.get_slot(slot_name)
            choice_name = slot[u.value_name].lower()
            elems = self.form_element.find_elements_by_name(choice_name)
            if choice_value is None:
                # we select the first element of the list
                elems[0].click()
                return
            choice_value = choice_value.lower()
            for elem in elems:
                value = elem.get_attribute("value")
                if value == choice_value:
                    elem.click()
                    return
        except:
            if not self.get_warning_present():
                print(f"ERROR: A problem occured while trying to set the choice_value {choice_value} in the radio with name {choice_name}")
            raise Exception

    # Select the choice_value of the user for the checkbox with the given name
    def set_choice_checkbox(self, slot_name, choice_value):
        function_name = 'set_choice_checkbox'
        if u.DEBUG:
            print(f'{class_name}: {function_name}')
        try:
            slot = self.get_slot(slot_name)
            choice_name = slot[u.value_name].lower()
            elems = self.form_element.find_elements_by_name(choice_name)
            if choice_value is None:
                for elem in elems:
                    if elem.is_selected():
                        elem.click()
                        return            
            for elem in elems:
                value = elem.get_attribute("value")
                if value == choice_value:
                    if not elem.is_selected():
                        elem.click()
                    return
                else:
                    if elem.is_selected():
                        elem.click()
        except:
            if not self.get_warning_present():
                print(f"ERROR: A problem occured while trying to set the choice_value {choice_value} in the checkbox with name {choice_name}")
            raise Exception

    # Select the choices of the user for the checkbox with the given name
    def set_choices_checkbox(self, slot_name, choice_values):
        function_name = 'set_choices_checkbox'
        if u.DEBUG:
            print(f'{class_name}: {function_name}')
        try:
            slot = self.get_slot(slot_name)
            choice_name = slot[u.value_name].lower()
            choices_lower = []
            for choice_value in choice_values:
                choices_lower.append(choice_value.lower())
            elems = self.form_element.find_elements_by_name(choice_name)
            value_present = False
            for elem in elems:
                value = elem.get_attribute("value")
                if value in choices_lower:
                    if not elem.is_selected():
                        elem.click()
                        value_present = True
                else:
                    if elem.is_selected():
                        elem.click()
                        value_present = True
            if not value_present:
                choices_string = fn.get_string_from_list(choice_values)
                sorry_style = styles.get_sorry()
                please_style = styles.get_please()
                text = (f"{sorry_style} none of the choices {choices_string} you proposed is valid for the field {slot_name}" +
                        f"{please_style} choose them in the following list: {choice_list}")
                self.set_warning_message(text)
                raise Exception
        except:
            if not self.get_warning_present():
                choices_list = fn.get_string_from_list(choice_values)
                print(f"ERROR: A problem occured while trying to set the choices {choices_list} in the checkbox with name {choice_name}")
            raise Exception

    # Finds the submit button inside the form and restitutes it
    def get_submit_button(self):
        function_name = 'get_submit_button'
        if u.DEBUG:
            print(f'{class_name}: {function_name}')
        try:
            elem = self.form_element.find_element_by_xpath(
                f".//input[@{u.bot_button} = 'submit']")
            return elem
        except:
            print("ERROR: A problem occured while trying to get the submit button")
            raise Exception

    # Finds the reset button inside the form and restitutes it
    def get_reset_button(self):
        function_name = 'get_reset_button'
        if u.DEBUG:
            print(f'{class_name}: {function_name}')
        try:
            elem = self.form_element.find_element_by_xpath(
                f".//input[@{u.bot_button} = 'reset']")
            return elem
        except:
            print("ERROR: A problem occured while trying to get the reset button")
            raise Exception

    def get_num_required_remaining(self):
        return self.num_required_remaining

    def decrease_num_required_remaining(self, scale=1):
        self.num_required_remaining -= scale

    def increase_num_required_remaining(self, scale=1):
        self.num_required_remaining += scale

    def set_all_required_filled(self, value):
        self.machine_parameters[u.all_required_filled] = value

    def get_all_required_filled(self):
        return self.machine_parameters[u.all_required_filled]

    def complete_spelling_value(self, char):
        self.spelling_state[u.current_spelling_input_value] = f'{self.spelling_state[u.current_spelling_input_value]}{char}'
        if u.DEBUG:
            print(f'[Current spelling input: {self.spelling_state[u.current_spelling_input_value]} ]')

    def get_current_spelling_input_value(self):
        return self.spelling_state[u.current_spelling_input_value]
    
    def set_current_spelling_input_value(self, value):
        self.spelling_state[u.current_spelling_input_value] = value

    # returns a string containing the list of fields, we can precise if we want only the
    # remaining ones, only the required ones
    def get_fields_list(self, only_required=False, remaining=False):
        function_name = 'get_fields_list'
        if u.DEBUG:
            print(f'{class_name}: {function_name}')
        try:
            list_fields = []
            slots = self.form_slots()
            for slot in slots:
                if slot[u.slot_name] != u.REQUESTED_SLOT:
                    # we descard the slot u.REQUESTED_SLOT because it does not represent a field
                    if slot[u.required]:
                        if not remaining or slot[u.slot_value] is None:
                            # we add remaining required fields
                            list_fields.append(slot[u.slot_name])
                    if not only_required and not slot[u.required]:
                        if not remaining or slot[u.slot_value] is None:
                            # we add remaining not required fields
                            list_fields.append(slot[u.slot_name])
            string = fn.get_string_from_list(list_fields)
            return string
        except:
            print(f'ERROR: Fail to get the list of the fields')
            raise Exception

    def get_form_title(self):
        function_name = 'get_form_title'
        if u.DEBUG:
            print(f'{class_name}: {function_name}')
        try:
            requested_slot = self.get_slot(u.REQUESTED_SLOT)
            title = requested_slot[u.title]
            if title is None:
                sorry_style = styles.get_sorry()
                text = f"{sorry_style} there is no title provided for this form"
                return text
            # the title is present in the html file
            return title
        except:
            print('ERROR: Fail to get the title of the form')
            raise Exception

    def get_form_description(self):
        function_name = 'get_form_description'
        if u.DEBUG:
            print(f'{class_name}: {function_name}')
        try:
            requested_slot = self.get_slot(u.REQUESTED_SLOT)
            desc = requested_slot[u.description]
            if desc is None:
                sorry_style = styles.get_sorry()
                text = f"{sorry_style} there is no explanation provided for this form"
                return text
            # the description is present in the html file
            return desc
        except:
            print('ERROR: Fail to get the description of the form')
            raise Exception

    def get_field_description(self, field):
        function_name = 'get_field_description'
        if u.DEBUG:
            print(f'{class_name}: {function_name}')
        try:
            slot = self.get_slot(field)
            desc = slot[u.description]
            if desc is None:
                sorry_style = styles.get_sorry()
                text = f"There is no explanation provided for the field {field} {sorry_style}"
                return text
            # the description is present in the html file
            text = f'{field}: {desc}'
            return text
        except:
            print(f'ERROR: Fail to get the description of the field {field}')
            raise Exception

    def submit_string(self):
        function_name = 'submit_string'
        if u.DEBUG:
            print(f'{class_name}: {function_name}')
        try:
            first = "All the fields have been completed."
            values = fn.get_pairs(slots=self.form_slots())
            okay_style = styles.get_good()
            stringSubmit = f"Is everything {okay_style} for the submission?"
            string = f"{first} Here is the summary: \n{values} \n{stringSubmit}.\nThe stars indicate the required fields"
            return string
        except:
            print('ERROR: Fail to generate the submit string')
            raise Exception

    def manage_next_step(self):
        function_name = 'manage_next_step'
        if u.DEBUG:
            print(f'{class_name}: {function_name}')
        try:
            slot_name, next_slot_required = self.get_next_slot()
            if slot_name is not None:
                if u.DEBUG:
                    print("The next slot is: " + slot_name)
                    # to observe the modification that happened
                    print(self.get_slots_value())
                string = "{}".format(
                    self.get_next_slot_text(slot_name, next_slot_required))
                if slot_name in self.get_spelling_fields() and u.READY_FOR_SPELLING:
                    # we add the field to the spelling list
                    self.add_spelling_name(slot_name)
                    # we verify if the field has been previously saved 
                    saved_fields = self.get_saved_spelling_fields()
                    if u.DEBUG:
                        print(f'The saved fields are {saved_fields}')
                    if slot_name in saved_fields:
                        # we set the saved value and we get the next step string
                        return self.resume_spelling(slot_name)
                    else:
                        please_style = styles.get_please()
                        string = (f'{string}\nSince it is a field requiring the spelling, we are going to take' +
                                f' its value one character at a time.\n{please_style} insert the first character')
                        # possible next action is spelling
                        self.set_possible_next_action(u.spelling_action)
                        return string
                else:
                    # possible next action is fillGenericCamp
                    self.set_possible_next_action(u.fill_field_action)
                    return string
            else:
                # the submit button here is one shot so we enable the alarm
                self.set_submit_alarm_enabled()
                string = self.submit_string()
                self.set_possible_next_action(u.submit_action)
                return string
        except:
            print("ERROR: Fail to get the string for the next field")
            raise Exception

    def resume_spelling(self, slot_name):
        try:
            # we update the next fields
            slot = self.get_slot(slot_name)
            self.set_next_slot(slot_name, slot[u.required])
            
            saved_fields = self.get_saved_spelling_fields()
            saved_values = self.get_saved_spelling_values()
            # we set the saved value as current input value 
            index = saved_fields.index(slot_name)
            value = saved_values[index]
            self.set_current_spelling_input_value(value)
            if u.DEBUG:
                print(f'The current value for {slot_name} is {value}')
            # we remove the field from saved state
            saved_fields.remove(slot_name)
            saved_values.remove(value)
            next_style = styles.get_next()
            please_style = styles.get_please()
            string = (f'You started filling the field {slot_name} and the current value is {value} ' +
                    f'\n{please_style} insert the {next_style} character')
            # possible next action is spelling
            self.set_possible_next_action(u.spelling_action)
            return string
        except:
            print('ERROR: Fail to manage the resume of the spelling')
            raise Exception

    def managed_particular_case(self, slot_name_list, slot_value_list):
        function_name = 'managed_particular_case'
        if u.DEBUG:
            print(f'{class_name}: {function_name}')
        try:
            # The particular case refers to a checkbox with more than one choice_value made
            # we update the Web Form and we set the slots
            if len(slot_name_list) >= len(slot_value_list):
                return False
            if len(slot_name_list) == 0:
                slot_name = self.get_next_slot(only_name=True)
            else:
                slot_name = slot_name_list[0]
            slot = self.get_slot(slot_name)
            value_type = slot[u.value_type]
            if value_type != "checkbox":
                return False
            self.set_choices_checkbox(
                slot_name=slot_name, choice_values=slot_value_list)
            slot[u.slot_value] = slot_value_list
            self.update(slot_name)
            return True
        except:
            print("ERROR: Fail to check particular case")
            raise Exception

    def update(self, slot_name):
        function_name = 'update'
        if u.DEBUG:
            print(f'{class_name}: {function_name}')
        try:
            """the slot have been filled and now we have to update the state by modifying the
            necessary variables which are: 'num_required_remaining', 'all_required_filled'
            when the slot was required and num_required_remaining = 0 after modif"""

            if slot_name == u.REQUESTED_SLOT:
                # theoretically should never occur
                return None
            # we update the next field only if the the field that have been completed was the one supposed to be completed
            field_to_be_completed = self.get_next_slot(only_name=True)
            if slot_name == field_to_be_completed:
                self.set_next_slot_basic()
            # we update the statistics about the number of required fields remaining
            slot = self.get_slot(slot_name)
            if not slot[u.required]:
                return u.VOID
            if slot[u.slot_value] is None:
                # we cancelled the value of a field
                self.increase_num_required_remaining()
                return u.CANCELED
            # we inserted the value  in a field
            self.decrease_num_required_remaining()
            if self.get_num_required_remaining() == 0:
                self.set_all_required_filled(True)
                text = ("All the required fields have been completed, from now on you can" +
                            " submit")
                next_step_string = self.manage_next_step()
                string = f'{text}\n{next_step_string}'
                return string
            return u.VOID
        except:
            print(f'ERROR: Fail to update the the next slot and the other statistics related to it')
            raise Exception

    def fill_generic_slots(self, slot_name_list, slot_value_list):
        function_name = 'fill_generic_slots'
        if u.DEBUG:
            print(f'{class_name}: {function_name}')
        try:
            numSlot = len(slot_name_list)
            numValue = len(slot_value_list)
            if numSlot == 1 and numValue == 0:
                required_fields = self.get_required_fields()
                slot_name = slot_name_list[0]
                if slot_name in required_fields:
                    slot_required = True
                else:
                    slot_required = False
                # we prepare the slot for the next value coming
                self.set_next_slot(slot_name, slot_required)
                string = self.manage_next_step()
                return True, string
            if numValue >= numSlot:
                correct, string = self.fill_slots_more_values(
                    slot_name_list, slot_value_list)
            else:
                correct, string = self.fill_slots_more_names(
                    slot_name_list, slot_value_list)
            if correct:
                string = f'Web Form updated. {string}'
            else:
                string = f'The Web Form has not been updated, problem of validity.\n{string}'
            return correct, string
        except:
            if not self.get_warning_present():
                print("ERROR: Fail to fill the slots")
            raise Exception

    def fill_slots_more_values(self, slot_name_list, slot_value_list):
        function_name = 'fill_slots_more_values'
        if u.DEBUG:
            print(f'{class_name}: {function_name}')
        try:
            # we find the slot that refers to that entity, if there are many slots, we take the first empty
            # one, and if all are full we take the first one
            # Another hypothesis is that each slot is directly followed or directly preceeded by its value
            particular_case = self.managed_particular_case(
                slot_name_list, slot_value_list)
            if particular_case:
                return True, self.manage_next_step()
            # we are not in a checkbox with more than one choice_value made
            ready_to_submit = False
            numSlot = len(slot_name_list)
            numValue = len(slot_value_list)
            for index in range(numSlot):
                # we fill in sequence the fields with values
                slot_name = slot_name_list[index]
                slot_value = slot_value_list[index]
                if u.DEBUG:
                    print(f"field label: {slot_name}, field value: {slot_value}")
                slot_value, comment = self.fill_input(slot_name, slot_value)
                if slot_value is None:
                    # incompatibility observed, the comment contains the next_step_string
                    return False, comment
                self.set_slot(slot_name, slot_value)
                text = self.update(slot_name)
                if text != u.VOID:  # slot value is not None so text != u.CANCELED
                    ready_to_submit = True
                    string = text                
            for index in range(numSlot, numValue):
                # we want to complete in sequence the empty fields with the values not
                # explicitely associated to any field
                slots = self.form_slots()
                for slot in slots:
                    slot_name = slot[u.slot_name]
                    if slot_name != u.REQUESTED_SLOT:
                        slot_value = slot[u.slot_value]
                        spelling = slot[u.spelling]
                        if slot_value is None and not spelling:
                            slot_value, comment = self.fill_input(
                                slot_name, slot_value_list[index])
                            if slot_value is None:
                                # incompatibility observed, the comment contains the next_step_string
                                return False, comment
                            # the Web form has been updated correctly and now we update the slots
                            self.set_slot(slot_name, slot_value)
                            text = self.update(slot_name)
                            # update returns a message when we just completed the last required field
                            if text != u.VOID:
                                ready_to_submit = True
                                string = text
                            break
            next_step_string = self.manage_next_step()
            if ready_to_submit:
                next_slot_name = self.get_next_slot(only_name=True)    # return also if the next slot is required or not
                if next_slot_name is not None:
                    return True, string
            string = next_step_string
            return True, string
        except:
            if not self.get_warning_present():
                print('ERROR: Fail to fill the slots when there are more values than fields names')
            raise Exception

    def fill_slots_more_names(self, slot_name_list, slot_value_list):
        function_name = 'fill_slots_more_names'
        if u.DEBUG:
            print(f'{class_name}: {function_name}')
        try:
            empty_slots_names = []
            # there are strictly less values than fields, so it is possible to have empty fields at
            # the end
            ready_to_submit = False
            numSlot = len(slot_name_list)
            numValue = len(slot_value_list)
            for index in range(numValue):
                # we fill in sequencw the fields with values
                slot_name = slot_name_list[index]
                slot_value = slot_value_list[index]
                slot_value, comment = self.fill_input(slot_name, slot_value)
                if slot_value is None:
                    # incompatibility observed, the comment contains the next_step_string
                    return False, comment
                self.set_slot(slot_name, slot_value)
                text = self.update(slot_name)
                if text != u.VOID:
                    ready_to_submit = True
                    string = text
            for index in range(numValue, numSlot):
                slot_name = slot_name_list[index]
                empty_slots_names.append(slot_name)
            # the choie here is to reset all the fields that the user wanted to modify but did not give the
            # values. Another choice_value could be to leave them as they are
            for slot_name in empty_slots_names:
                self.fill_input(slot_name, slot_value=None)
                self.set_slot(slot_name, slot_value=None)
                text = self.update(slot_name)
                # update return u.CANCELED when we just reset the value of a required slot
                if text == u.CANCELED:
                    # one required value have been canceled
                    ready_to_submit = False
            # now we prepare the output string
            next_step_string = self.manage_next_step()
            fields = fn.get_string_from_list(empty_slots_names)
            modify_style = styles.get_modify()
            intro = (f"You wanted to {modify_style} the fields {fields} but you did not insert their values")
            if ready_to_submit:
                next_slot_name = self.get_next_slot(only_name=True)    # return also if the next slot is required or not
                if next_slot_name is not None:
                    string = f'{intro}\n{string}\n{next_step_string}'
                    return True, string
            string = f"{intro}\n{next_step_string}"
            return True, string
        except:
            if not self.get_warning_present():
                print('ERROR: Fail to fill slots when there are more names than values')
            raise Exception

    def all_fields_present(self, slot_name_list):
        function_name = 'all_fields_present'
        if u.DEBUG:
            print(f'{class_name}: {function_name}')
        try:
            # returns True if all the fields are present and False otherwise. In ca of false retruns also the next_step string
            string =''
            for slot_name in slot_name_list:
                present = fn.verify_presence(slot_name, self.form_slots(), only_presence=True)
                if not present:
                    sorry_style = styles.get_sorry()
                    text = (f"{sorry_style} the field {slot_name} is not present in this form.\nThe fields of this form are" +
                            f" the following: {self.get_fields_list()}")
                    next_step_string = self.manage_next_step()
                    string = f'{text}\n{next_step_string}'
                    return False, string
            return True, string
        except:
            if not self.get_warning_present():
                print('ERROR: Fail to verify presence of all fields')
            raise Exception

    def filling_procedure(self, slot_name, slot_value):
        function_name = 'filling_procedure'
        if u.DEBUG:
            print(f'{class_name}: {function_name}')
        try:
            if slot_value is None:
                # we take the previous value for that field
                previous_value = self.get_slot(slot_name)[u.slot_value]
                if previous_value is not None:
                    # we are resetting a field
                    self.set_slot(slot_name=slot_name, slot_value=slot_value)
                    string = self.update(slot_name)
                else:
                    string = u.VOID
                if string in [u.VOID, u.CANCELED]:
                    next_step_string = self.manage_next_step()
                    return next_step_string
                return string
            # we update the Web Form
            slot_value, comment = self.fill_input(slot_name, slot_value)
            if slot_value is None:
                # incompatibility observed, the comment contains the next_step_string
                return comment
            # Everything went fine so we update the internal structure
            self.set_slot(slot_name=slot_name, slot_value=slot_value)
            string = self.update(slot_name)
            if string in [u.VOID, u.CANCELED]:
                next_step_string = self.manage_next_step()
                return next_step_string
            return string
        except:
            if not self.get_warning_present():
                print('ERROR: Fail to complete the filling procedure')
            raise Exception
