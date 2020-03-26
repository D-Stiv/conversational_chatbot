import copy
import logging
import typing
from typing import Any, Dict, Iterator, List, Optional, Text
from selenium.webdriver.support.ui import Select
import utility as u
import functions as fn
import styles

logger = logging.getLogger(__name__)


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
            print("A problem occured while initializing the state")
        
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
            u.waiting_intent: None,
            u.saved_spelling_fields: [],
            u.saved_spelling_values: []
        }
        return spelling_state

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

    def get_waiting_intent(self):
        return self.spelling_state[u.waiting_intent]
    
    def set_waiting_intent(self, intent):
        self.spelling_state[u.waiting_intent] = intent

    def get_spelling_interrupted(self):
        return self.spelling_state[u.spelling_interrupted]

    def set_spelling_interrupted(self, value=True):
        self.spelling_state[u.spelling_interrupted] = value

    def get_spelling_list(self):
        return self.spelling_state[u.spelling_list]

    def set_spelling_list(self, slot_name_list, slot_value_list):
        try:
            """the idea here is to separate the spelling and non spelling fields.
            for the spelling fields, the value is not important, since we will retake it.
            we set the spelling_list and we return the non spelling data"""
            spelling_fields = self.get_spelling_fields()
            name_list = []
            value_list = []
            spelling_list = []
            num_value = len(slot_value_list)
            for index in range(len(slot_name_list)):
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
                for index in range(len(slot_name_list), num_value):
                    slot_value = slot_value_list[index]
                    value_list.append(slot_value)
            self.spelling_state[u.spelling_list] = spelling_list
            return name_list, value_list
        except:
            print('Fail to get the spelling list')
            raise Exception

    def get_spelling_fields(self):
        try:
            spelling_fields = []
            for slot in self.form_slots():
                if slot[u.slot_name] != u.REQUESTED_SLOT:
                    if slot[u.spelling]:
                        spelling_fields.append(slot[u.slot_name])
            return spelling_fields
        except:
            print('Fail to get the spelling fields')
            raise Exception

    def add_spelling_name(self, slot_name):
        if slot_name not in self.spelling_state[u.spelling_list]:
            self.spelling_state[u.spelling_list].append(slot_name)

    def get_required_fields(self):
        try:
            required_fields = []
            for slot in self.form_slots():
                if slot[u.slot_name] != u.REQUESTED_SLOT:
                    if slot[u.required]:
                        required_fields.append(slot[u.slot_name])
            return required_fields
        except:
            print('Fail to get the spelling fields')
            raise Exception

    def set_next_slot(self, slot_name, required):
        try:
            self.machine_parameters[u.next_slot] = slot_name
            self.machine_parameters[u.next_slot_required] = required
        except:
            print(f'Fail to set the next slot to be {slot_name}')
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

    # Modifies the state inserting the latest message which is the intent of the last user input
    def add_latest_message(self, message):
        self.message_history.append(message)

    def set_warning_present(self, value=True):
        self.machine_parameters[u.warning_present] = value
    
    def get_warning_present(self):
        return self.machine_parameters[u.warning_present]

    # extracts and restitutes the slots present in the form with their values
    def form_slots(self):
        try:
            slots = self.constructs["form"]["slots"]
            return slots
        except:
            print("A problem occured while extracting the slots")
            raise Exception

    # Gets the value of a given slot
    def get_slot(self, slot_name):
        try:
            for slot in self.form_slots():
                if slot[u.slot_name] == slot_name:
                    return slot
            text = "Trying to access a non existing slot {}".format(slot_name)
            self.set_warning_message(text)
            raise Exception
        except:
            print("Fail to get the slot --> {} <--".format(slot_name))
            raise Exception

    # inserts the value in a given slot
    def set_slot(self, slot_name, slot_value):
        try:
            exists = False
            slots = self.form_slots()
            for existing_slot in slots:
                if slot_name == existing_slot[u.slot_name]:
                    exists = True
                    existing_slot[u.slot_value] = slot_value
                    break
            if not exists:
                text = 'The name {} does not correspond to any label, please verify the spelling and try again'.format(
                    slot_name)
                self.set_warning_message(text)
                raise Exception
        except:
            print("A problem occured while trying to put the value {} in the slot {}".format(
                slot_value, slot_name))
            raise Exception

    def set_warning_message(self, text):
        next_slot_string = self.manage_next_step()
        text = f'{text}\n{next_slot_string}'
        self.machine_parameters[u.warning_message] = text
        # we also set the warning present to True since there is a message
        self.set_warning_present()

    def get_warning_message(self):
        return self.machine_parameters[u.warning_message]

    # return all the slots with their name and their value
    def get_slots_value(self):
        slots_value = {}
        for slot in self.form_slots():
            slot_name = slot[u.slot_name]
            slot_value = slot[u.slot_value]
            slots_value[slot_name] = slot_value
        return slots_value

    # Puts a given slot as the required slot
    def set_requested_slot(self, slot_name):
        try:
            exists = False
            for existing_slot in self.form_slots():
                if slot_name == existing_slot[u.slot_name]:
                    exists = True
                    break
            if exists:
                for slot in self.form_slots():
                    if slot[u.slot_name] == slot_name:
                        slot[u.slot_value] == u.REQUESTED_SLOT
            else:
                text = 'The name {} does not correspond to any label, please verify the spelling and try again'.format(
                    slot_name)
                self.set_warning_message(text)
                raise Exception
        except:
            print(
                "A problem occured while trying to set required_slot with the slot {}".format(slot))
            raise Exception

    # Restitutes the value (slot) of the required slot
    def get_requested_slot(self):
        try:
            for slot in self.form_slots():
                if slot[u.slot_name] == u.REQUESTED_SLOT:
                    slot_name = slot[u.slot_value]
            return slot_name
        except:
            print("A problem occured while fetching the value of required_slot")
            raise Exception

    # Restitutes the next slot's name
    def get_next_slot(self):
        try:
            return self.machine_parameters[u.next_slot], self.machine_parameters[u.next_slot_required]
        except:
            print("A problem occured while getting the next slot")
            raise Exception

    # sets the next field (slot) according to the order of the web form
    def set_next_slot_basic(self):
        try:
            slot_name = self.get_next_slot()
            # we try to take in sequence the first empty field after the current field
            actual_found = False
            for slot in self.form_slots():
                if slot[u.slot_name] != u.REQUESTED_SLOT:
                    if actual_found:
                        # we are after the actual field
                        if slot[u.slot_value] is None:
                            self.set_next_slot(
                                slot[u.slot_name], slot[u.required])
                            return 
                    if slot[u.slot_name] == slot_name:
                        actual_found = True
            # there is no empty field after the current field, we try to look before
            for slot in self.form_slots():
                if slot[u.slot_name] != u.REQUESTED_SLOT:
                    if slot[u.slot_value] is None:
                        self.set_next_slot(
                            slot[u.slot_name], slot[u.required])
                        return 
                    if slot[u.slot_name] == slot_name:
                        # we returned at the starting point, so we don't have to set the next slot
                        return 
        except:
            print('Fail to get the next slot for skipping case')
            raise Exception

    # Transforms the choices list into text and restitutes
    def get_next_slot_text(self, slot_name, slot_required):
        try:
            types_with_options = [u.dropdowm, u.checkbox, u.radio]
            slot = self.get_slot(slot_name)
            value_type = slot[u.value_type]
            required_string = fn.get_required_string(slot_required)
            if value_type in types_with_options:
                choice_list = slot[u.choice_list]
                option_string = fn.get_string_from_list(choice_list)
                if value_type == u.dropdowm:
                    string = f"Select the {slot_name} in the following list {option_string}. {required_string}"
                else:
                    if value_type == u.checkbox:
                        string = f"Select your {slot_name} in the following list {option_string}. {required_string}"
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
            print("Fail to extract the text for the next slot")
            raise Exception

    # Inserts the value inside the web page (form) with the label corrisponding to the slot
    def fill_input(self, slot_name, slot_value):
        try:
            is_none = False
            if slot_value is None:
                is_none = True
            # substitute the underscores with spaces to outpu the right message
            input_type_list = u.input_type_list
            slot = self.get_slot(slot_name)
            value_type = slot[u.value_type]
            value_name = slot[u.value_name]
            if not is_none:
                if u.DEBUG:
                    print("value_name: {}, value_type: {}".format(
                        value_name, value_type))
                compatible, text = fn.is_compatible(slot_value, value_type)
                if not compatible:
                    text = "Incompatibility between the value {} and the type {}.\n{}".format(
                        slot_value, value_type, text)
                    self.set_warning_message(text)
                    raise Exception
                # the value and the type are compatible so it is pssible that the value has been converted
                # to an appropriate form contained in text
                slot_value = text
            if value_type in input_type_list:
                elem = self.form_element.find_element_by_name(value_name)
                elem.clear()
                if slot_value is None:
                    return ""
                elem.send_keys(slot_value)
                return slot_value
            # the value is put in lowercase to coincide with the choice
            if not is_none:
                slot_value = slot_value.lower()
            if value_type == u.dropdowm:
                self.set_choice_dropdown(
                    slot_name=slot_name, choice_value=slot_value)
            elif value_type == u.checkbox:
                self.set_choice_checkbox(
                    slot_name=slot_name, choice_value=slot_value)
            elif value_type == u.radio:
                self.set_choice_radio(
                    slot_name=slot_name, choice_value=slot_value)
            if is_none:
                return ""
            return slot_value
        except:
            if not self.get_warning_present():
                print("A problem occured while trying to insert in the web page the value {} for the label {}".format(
                    slot_value, slot_name))
            raise Exception

    # Select the choice_value of the user for the dropdown with the given name
    def set_choice_dropdown(self, slot_name, choice_value):
        try:
            slot = self.get_slot(slot_name)
            choice_name = slot[u.slot_value].lower()
            select = Select(self.form_element.find_element_by_name(choice_name))
            if choice_value is None:
                # the choice_value is to select the first element
                select.select_by_index(0)
            else:
                choice_value = choice_value.lower()
                # verify if the choice_value is in the dropdown list
                # if not warning for no match with choice
                choice_list = slot[u.choice_list]
                # we transform the choice_list in lowercase
                for index in range(len(choice_list)):
                    choice_list[index] = choice_list[index].lower()
                if choice_value in choice_list:
                    select.select_by_value(choice)
                else:
                    sorry_style = styles.get_sorry()
                    please_style = styles.get_please()
                    text = (f"{sorry_style} the choice_value {choice} is not valid for the field {self.next_slot}" +
                            f"{please_style} choose one in the following list: {choice_list}")
                    self.set_warning_message(text)
                    raise Exception
        except:
            print("A problem occured while trying to set the choice_value {} in the dropdown with name {}".format(
                choice_value, choice_name))
            raise Exception

    # Select the choice_value of the user for the radio with the given name
    def set_choice_radio(self, slot_name, choice_value):
        try:
            slot = self.get_slot(slot_name)
            choice_name = slot[u.slot_value].lower()
            elems = self.form_element.find_elements_by_name(choice_name)
            if choice_value is None:
                # we select the first element of the list
                elems[0].click()
                return
            choice_value = choice.lower()
            choice_list = slot[u.choice_list]
            # we transform the choice_list in lowercase
            for index in range(len(choice_list)):
                choice_list[index] = choice_list[index].lower()
            if choice_value in choice_list:
                for elem in elems:
                    value = elem.get_attribute("value")
                    if value == choice:
                        elem.click()
                        return
            # no match to be implement modifying warning
            sorry_style = styles.get_sorry()
            please_style = styles.get_please()
            text = (f"{sorry_style} the choice_value {choice} is not valid for the field {name}" +
                    f"{please_style} choose one in the following list: {choice_list}")
            self.set_warning_message(text)
            raise Exception
        except:
            if not self.get_warning_present():
                print("A problem occured while trying to set the choice_value {} in the radio with name {}".format(
                    choice_value, choice_name))
            raise Exception

    # Select the choice_value of the user for the checkbox with the given name
    def set_choice_checkbox(self, slot_name, choice_value):
        try:
            slot = self.get_slot(slot_name)
            choice_name = slot[u.slot_value].lower()
            elems = self.form_element.find_elements_by_name(choice_name)
            choice_list = slot[u.choice_list]
            if choice_value is None:
                for elem in elems:
                    if elem.is_selected():
                        elem.click()
                        return
            choice_value = choice.lower()
            if u.DEBUG:
                print("choice: {}".format(choice))
            for elem in elems:
                value = elem.get_attribute("value")
                if value == choice:
                    if not elem.is_selected():
                        elem.click()
                    return
                else:
                    if elem.is_selected():
                        elem.click()
            # no match to be implement modifying warning
            sorry_style = styles.get_sorry()
            please_style = styles.get_please()
            text = ("{} the choice_value {} is not valid for the field {}" +
                    "{} choose one in the following list: {}").format(sorry_style,
                                                                      choice, please_style, choice_list)
            self.set_warning_message(text)
            raise Exception
        except:
            if not self.get_warning_present():
                print("A problem occured while trying to set the choice_value {} in the checkbox with name {}".format(
                    choice_value, choice_name))
            raise Exception

    # Select the choices of the user for the checkbox with the given name
    def set_choices_checkbox(self, slot_name, choice_values):
        try:
            slot = self.get_slot(slot_name)
            choice_name = slot[u.slot_value].lower()
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
                text = ("{} none of the choices {} you proposed is valid for the field {}" +
                        "{} choose them in the following list: {}").format(sorry_style,
                                                                           choices_string, please_style, choice_list)
                self.set_warning_message(text)
                raise Exception
        except:
            if not self.get_warning_present():
                choices_list = fn.get_string_from_list(choice_values)
                print("A problem occured while trying to set the choices {} in the checkbox with name {}".format(
                    choices_list, choice_name))
            raise Exception

    # Finds the submit button inside the form and restitutes it
    def get_submit_button(self):
        try:
            elem = self.form_element.find_element_by_xpath(
                f".//input[@{u.bot_button} = 'submit']")
            return elem
        except:
            print("A problem occured while trying to get the submit button")
            raise Exception

    # Finds the reset button inside the form and restitutes it
    def get_reset_button(self):
        try:
            elem = self.form_element.find_element_by_xpath(
                f".//input[@{u.bot_button} = 'reset']")
            return elem
        except:
            print("A problem occured while trying to get the reset button")
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
        try:
            list_fields = []
            for slot in self.form_slots():
                if slot[u.slot_name] != u.REQUESTED_SLOT:
                    # we descard the slot u.REQUESTED_SLOT because it does not represent a field
                    if slot[u.required]:
                        if not remaining or slot[u.slot_value] is None:
                            # we add remaining required fields
                            list_fields.append(slot[u.slot_name])
                    if not only_required:
                        if not remaining or slot[u.slot_value] is None:
                            # we add remaining not required fields
                            list_fields.append(slot[u.slot_name])
            string = fn.get_string_from_list(list_fields)
            return string
        except:
            print(f'Fail to get the list of the fields')
            raise Exception

    def get_form_title(self):
        try:
            title = self.form_element.get_attribute('bot-title')
            return title
        except:
            print('Fail to get the title of the form')
            raise Exception

    def get_form_description(self):
        desc = self.form_element.get_attribute('bot-desc')
        return desc

    def get_field_description(self, field):
        try:
            _, is_present = fn.verify_presence(field, self.form_slots())
            if not is_present:
                raise Exception(
                    "You are trying to get a description of a not existing field {}".format(field))
            desc = fn.get_field_description(field, self.form_element)
            if desc is None:
                sorry_style = styles.get_sorry()
                text = "there is no explanation provided for the field {} {}".format(
                    field, sorry_style)
                return text
            # the description is present in the html file
            return desc
        except:
            print(f'Fail to get the description of the field {field}')
            raise Exception

    def submit_string(self):
        try:
            first = "all the fields have been completed\n"
            values = fn.get_pairs(slots=self.form_slots())
            okay_style = styles.get_good()
            stringSubmit = "Is everything {} for the submission ?".format(
                okay_style)
            string = "{} here is the summary: \n{} \n{}.\n the stars indicate the required fields".format(
                first, values, stringSubmit)
            return string
        except:
            print('Fail to generate the submit string')
            raise Exception

    def manage_next_step(self):
        try:
            slot_name, next_slot_required = self.get_next_slot()
            if slot_name is not None:
                if u.DEBUG:
                    print("the next slot is: " + slot_name)
                    # to observe the modification that happened
                    print(self.get_slots_value())
                string = "{}".format(
                    self.get_next_slot_text(slot_name, next_slot_required))
                if slot_name in self.get_spelling_fields() and u.READY_FOR_SPELLING:
                    self.add_spelling_name(slot_name)
                    # we enable the close prompt. It will be disabled when the user will insert the terminator
                    self.set_close_prompt_enabled()
                    please_style = styles.get_please()
                    # we verify if the field has been previously saved 
                    saved_fields = self.get_saved_spelling_fields()
                    if slot_name in saved_fields:
                        saved_values = self.get_saved_spelling_values()
                        # we set the saved value as current input value 
                        index = saved_fields.index(slot_name)
                        value = saved_value[index]
                        self.set_current_spelling_input_value(value)
                        # we remove the field from saved state
                        saved_fields.remove(slot_name)
                        saved_values.remove(value)
                        next_style = styles.get_next()
                        string = (f'You started filling this field and the current value is {value} ' +
                            f'\n{please_style} insert the {next_style} character')
                    else:
                        string = (f'{string}\nSince it is a field requiring the spelling, we are going to take' +
                                f' its value one character at a time.\n{please_style} insert the first character')
                    # possible next action is spelling
                    self.set_possible_next_action(u.spelling_action)
                    return string
                else:
                    # possible nest action is fillGenericCamp
                    self.set_possible_next_action(u.fill_field_action)
                    return string
            else:
                string = self.submit_string()
                self.set_possible_next_action(u.submit_action)
                return string
        except:
            print("Fail to manage the next step")
            raise Exception

    def managed_particular_case(self, slot_name_list, slot_value_list):
        try:
            # The particular case refers to a checkbox with more than one choice_value made
            if len(slot_name_list) != 1:
                return False
            if len(slot_name_list) >= len(slot_value_list):
                return False
            slot_name = slot_name_list[0]
            slot = self.get_slot(slot_name)
            value_type = slot[u.value_type]
            if value_type != "checkbox":
                return False
            self.set_choices_checkbox(
                slot_name=slot_name, choice_values=slot_value_list)
            return True
        except:
            print("Fail to check particular case")
            raise Exception

    def update(self, slot_name, slot_value):
        try:
            """the slot have been filled and now we have to update the state by modifying the
            necessary variables which are: 'num_required_remaining', 'all_required_filled'
            when the slot was required and num_required_remaining = 0 after modif"""

            if slot_name == u.REQUESTED_SLOT:
                # theoretically should never occur
                return
            # we update the next field
            self.set_next_slot_basic()
            slots = self.form_slots()
            for sl in slots:
                if sl[u.slot_name] == slot_name:
                    slot = sl
                    break
            text = ""
            if slot[u.required]:
                if slot[u.slot_value] is None:
                    # we cancel the value of a field
                    self.increase_num_required_remaining()
                    return u.CANCELED
                # we insert the value  of a field
                self.decrease_num_required_remaining()
                if self.get_num_required_remaining() == 0:
                    self.set_all_required_filled(True)
                    next_slot_name = self.next_slot
                    if next_slot_name is not None:
                        text = (" all the required fields have been completed, from now on you can" +
                                " submit")
            return text
        except:
            print(
                f'Fail to update the slot {slot_name} with the value {slot_value}')
            raise Exception

    def fill_generic_slots(self, slot_name_list, slot_value_list):
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
                return string
            if numValue >= numSlot:
                string = self.fill_slots_more_values(
                    slot_name_list, slot_value_list)
            else:
                string = self.fill_slots_more_names(
                    slot_name_list, slot_value_list)
            return string
        except:
            if not self.get_warning_present():
                print("Fail to fill the slots")
            raise Exception

    def fill_slots_more_values(self, slot_name_list, slot_value_list):
        try:
            # we find the slot that refers to that entity, if there are many slots, we take the first empty
            # one, and if all are full we take the first one
            # Another hypothesis is that each slot is directly followed or directly preceeded by its value
            particular_case = self.managed_particular_case(
                slot_name_list, slot_value_list)
            if particular_case:
                return self.manage_next_step()
            # we are not in a checkbox with more than one choice_value made
            ready_to_submit = False
            numSlot = len(slot_name_list)
            numValue = len(slot_value_list)
            for index in range(numSlot):
                # we fill in sequence the fields with values
                slot_name = slot_name_list[index]
                slot_value = slot_value_list[index]
                if u.DEBUG:
                    print("field label: {}, field value: {}".format(
                        slot_name, slot_value))
                slot_value = self.fill_input(slot_name, slot_value)
                self.set_slot(slot_name, slot_value)
                text = self.update(slot_name, slot_value)
                if text != "":
                    ready_to_submit = True
            for index in range(numSlot, numValue):
                # we want to complete in sequence the empty fields with the values not
                # explicitely associated to any field
                for slot in self.form_slots():
                    slot_name = slot[u.slot_name]
                    if self.get_slot(slot_name) is None:
                        slot_value = self.fill_input(
                            slot_name, slot_value_list[index])
                        self.set_slot(slot_name, slot_value)
                        text = self.update(
                            slot_name, slot_value)
                        if text != "":
                            ready_to_submit = True
            string = ""
            if ready_to_submit:
                next_slot_name, _ = self.get_next_slot()
                if next_slot_name is not None:
                    string = (" all the required fields have been completed form now on you can" +
                              " submit")
            return string
        except:
            if not self.get_warning_present():
                print(
                    'Fail to fill the slots when there are more values than field names')
            raise Exception

    def fill_slots_more_names(self, slot_name_list, slot_value_list):
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
                slot_value = self.fill_input(slot_name, slot_value)
                self.set_slot(slot_name, slot_value)
                text = self.update(
                    slot_name, slot_value)
                if text != "":
                    ready_to_submit = True
            for index in range(numValue, numSlot):
                slot_name = slot_name_list[index]
                empty_slots_names.append(slot_name)
            # the choie here is to reset all the fields that the user wanted to modify but did not give the
            # values. Another choice_value could be to leave them as they are
            for slot_name in empty_slots_names:
                self.fill_input(slot_name, slot_value=None)
                self.set_slot(slot_name, slot_value=None)
                text = self.update(
                    slot_name, slot_value=None)
                if text == u.CANCELED:
                    # one required value have been canceled
                    ready_to_submit = False
            # now we prepare the output string
            ready_string = ""
            if ready_to_submit:
                next_slot_name, _ = self.get_next_slot()
                if next_slot_name is not None:
                    ready_string = (" all the required fields have been completed form now on you can" +
                                    " submit")
            empty_slots_names = self.fill_generic_slots(
                slot_name_list=slot_name_list, slot_value_list=slot_value_list)
            fields = fn.get_string_from_list(empty_slots_names)
            modify_style = styles.get_modify()
            intro = ("You wanted to {} the fields {} but you did not insert their" +
                     "values\n").format(modify_style, fields)
            string = "{}\n{}".format(intro, ready_string)

            return string
        except:
            if not self.get_warning_present():
                print('Fail to fill slots when there are more names than values')
            raise Exception

    def all_fields_present(self, slot_name_list):
        try:
            for slot_name in slot_name_list:
                _, present = fn.verify_presence(slot_name, self.form_slots())
                if not present:
                    sorry_style = styles.get_sorry()
                    please_style = styles.get_please()
                    thanks_style = styles.get_thanks()
                    text = ("{} the field {} is not present in this form. \nthe fields of this form are" +
                            " the following: {}\n{} precise the action you want to perform {}").format(sorry_style,
                                                                                                       slot_name, self.get_fields_list(), please_style, thanks_style)
                    self.set_warning_message(text)
                    raise Exception
        except:
            if not self.get_warning_present():
                print('Fail to verify presence of all fields')
            raise Exception

    def filling_procedure(self, slot_name, slot_value):
        try:
            # we update the Web Form
            slot_value = self.fill_input(slot_name, slot_value)
            # Everything went fine so we update the internal structure
            self.set_slot(slot_name=slot_name, slot_value=slot_value)
            string = self.update(slot_name, slot_value)
            return string
        except:
            if not self.get_warning_present():
                print('Fail to complete the filling procedure')
            raise Exception
