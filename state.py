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
            self.spelling_list = []
            self.after_spelling = False
            self.current_action = 'fillForm'
            self.possible_next_action = 'submitForm'
            self.close_prompt_enabled = False   # True when we are in spelling mode
            self.all_required_filled = False
            self.num_total_fields, self.num_required_fields, self.num_optional_fields = fn.get_num_fields(
                constructs)
            self.num_required_remaining = self.num_required_fields
            self.current_spelling_input_value = ""
            self.warning_message = ""
            self.warning_present = False
            self.skip_enabled = False
            self.next_slot = ''
            self.next_slot_required = False
            self.submit_alarm_enabled = False
            self.submit_done = False
            self.filling_started = False
        except:
            print("A problem occured while initializing the state")

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
            self.spelling_list = spelling_list
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
        if slot_name not in self.spelling_list:
            self.spelling_list.append(slot_name)

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
            self.next_slot = slot_name
            self.next_slot_required = required
        except:
            print(f'Fail to set the next slot to be {slot_name}')
            raise Exception

    def update_spelling_list(self, slot_name):
        spelling_list = []
        for name in self.spelling_list:
            if name != slot_name:
                spelling_list.append(name)
        self.spelling_list = spelling_list

    def reset_current_spelling_input_value(self):
        self.current_input_value = ""

    def reset_spelling_list(self):
        self.spelling_list = []

    def set_after_spelling(self, value=True):
        self.after_spelling = value

    def set_skip_enabled(self, value=True):
        self.skip_enabled = value

    def set_close_prompt_enabled(self, value=True):
        self.close_prompt_enabled = value

    # Modifies the state inserting the latest message which is the intent of the last user input
    def add_latest_message(self, message):
        self.message_history.append(message)

    def set_warning_present(self, value=True):
        self.warning_present = value

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
        self.warning_message = text
        # we also set the warning present to True since there is a message
        self.set_warning_present()

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
            if self.skip_enabled:
                return self.get_next_slot_skipping()
            # this function updates the state modifying the required slot each time
            for slot in self.form_slots():
                if slot[u.slot_name] != u.REQUESTED_SLOT:
                    if slot[u.slot_value] == None:
                        slot_name = slot[u.slot_name]
                        required = slot[u.required]
                        self.set_slot(slot_name=u.REQUESTED_SLOT,
                                      slot_value=slot_name)
                        self.set_next_slot(slot_name, required)
                        return slot_name, required
            # arriving here means that all the camps have been filled, so there is no next slot
            self.set_slot(slot_name=u.REQUESTED_SLOT, slot_value=None)
            self.set_next_slot(slot_name=None, required=None)
            return None, None
        except:
            print("A problem occured while getting the next slot")
            raise Exception

    # gets the next slot when the user skips fields
    def get_next_slot_skipping(self):
        try:
            slot_name = self.next_slot
            # we try to take in sequence the first empty field after the current field
            actual_found = False
            for slot in self.form_slots():
                if slot[u.slot_name] != u.REQUESTED_SLOT:
                    if actual_found:
                        # we are after the actual field
                        if slot[u.slot_value] is None:
                            self.set_next_slot(
                                slot[u.slot_name], slot[u.required])
                            return slot[u.slot_name], slot[u.required]
                    if slot[u.slot_name] == slot_name:
                        actual_found = True
            # there is no empty field after the current field, we try to look before
            for slot in self.form_slots():
                if slot[u.slot_name] != u.REQUESTED_SLOT:
                    if slot[u.slot_value] is None:
                        self.set_next_slot(
                            slot[u.slot_name], slot[u.required])
                        return slot[u.slot_name], slot[u.required]
                    if slot[u.slot_name] == slot_name:
                        # we returned at the starting point
                        return slot[u.slot_name], slot[u.required]
        except:
            print('Fail to get the next slot for skipping case')
            raise Exception

    # Transforms the choices list into text and restitutes
    def get_next_slot_text(self, slot_name, slot_required):
        try:
            types_with_options = [u.dropdowm, u.checkbox, u.radio]
            for slot in self.form_slots():
                if slot[u.slot_name].lower() == slot_name.lower():
                    value_name = slot[u.value_name]
                    value_type = slot[u.value_type]
                    break
            required_string = fn.get_required_string(slot_required)
            if value_type in types_with_options:
                if value_type == u.dropdowm:
                    option_string = self.get_dropdown_list(value_name)
                    string = f"Select the {slot_name} in the following list {option_string}. {required_string}"
                else:
                    if value_type == u.checkbox:
                        option_string = self.get_checkbox_list(value_name)
                        string = f"Select your {slot_name} in the following list {option_string}. {required_string}"
                    elif value_type == u.radio:
                        option_string = self.get_radio_list(value_name)
                        string = f"Choose your {slot_name} in the following list {option_string}. {required_string}"
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
            value_name = ""
            value_type = ""
            for slot in self.form_slots():
                if slot[u.slot_name] != u.REQUESTED_SLOT:
                    if slot[u.slot_name].lower() == slot_name.lower():
                        value_name = slot[u.value_name]
                        value_type = slot[u.value_type]
                        break
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
                    name=value_name, choice=slot_value)
            elif value_type == u.checkbox:
                self.set_choice_checkbox(
                    name=value_name, choice=slot_value)
            elif value_type == u.radio:
                self.set_choice_radio(
                    name=value_name, choice=slot_value)
            if is_none:
                return ""
            return slot_value
        except:
            if not self.warning_present:
                print("A problem occured while trying to insert in the web page the value {} for the label {}".format(
                    slot_value, slot_name))
            raise Exception

    # Restitutes the choices list inside the dropdown with the given name
    def get_dropdown_list(self, name, tag='str'):
        try:
            name = name.lower()
            elem = self.form_element.find_element_by_name(name)
            dropdowm_list = []
            options = elem.find_elements_by_xpath(".//option")
            for option in options:
                dropdowm_list.append(option.text)
            if u.DEBUG:
                print("dropdown list")
                print(dropdowm_list)
            if tag != 'str':
                return dropdowm_list
            string = fn.get_string_from_list(dropdowm_list)
            return string
        except:
            print(
                "A problem occured while fetching the dropdown list with the name {}".format(name))
            raise Exception

    # Restitutes the choices list inside the checkbox with the given name
    def get_checkbox_list(self, name, tag='str'):
        try:
            name = name.lower()
            elems = self.form_element.find_elements_by_name(name)
            checkbox_list = []
            for elem in elems:
                value = elem.get_attribute("value")
                checkbox_list.append(value)
            if u.DEBUG:
                print("checkbox list")
                print(checkbox_list)
            if tag != 'str':
                return checkbox_list
            string = fn.get_string_from_list(checkbox_list)
            return string
        except:
            print(
                "A problem occured while fetching the checkbox list with the name {}".format(name))
            raise Exception

    # Restitutes the choices list inside the radio with the given name
    def get_radio_list(self, name, tag='str'):
        try:
            name = name.lower()
            elems = self.form_element.find_elements_by_name(name)
            radio_list = []
            for elem in elems:
                value = elem.get_attribute("value")
                radio_list.append(value)
            if u.DEBUG:
                print("radio list")
                print(radio_list)
            if tag != 'str':
                return radio_list
            string = fn.get_string_from_list(radio_list)
            return string
        except:
            print(
                "A problem occured while fetching the radio list with the name {}".format(name))
            raise Exception

    # Select the choice of the user for the dropdown with the given name
    def set_choice_dropdown(self, name, choice):
        try:
            name = name.lower()
            select = Select(self.form_element.find_element_by_name(name))
            if choice is None:
                # the choice is to select the first element
                select.select_by_index(0)
            else:
                choice = choice.lower()
                # verify if the choice is in the dropdown list
                # if not warning for no match with choice
                choice_list = self.get_dropdown_list(name, 'list')
                # we transform the choice_list in lowercase
                for index in range(len(choice_list)):
                    choice_list[index] = choice_list[index].lower()
                if choice in choice_list:
                    select.select_by_value(choice)
                else:
                    sorry_style = styles.get_sorry()
                    please_style = styles.get_please()
                    text = (f"{sorry_style} the choice {choice} is not valid for the field {self.next_slot}" +
                            f"{please_style} choose one in the following list: {choice_list}")
                    self.set_warning_message(text)
                    raise Exception
        except:
            print("A problem occured while trying to set the choice {} in the dropdown with name {}".format(
                choice, name))
            raise Exception

    # Select the choice of the user for the radio with the given name
    def set_choice_radio(self, name, choice):
        try:
            name = name.lower()
            elems = self.form_element.find_elements_by_name(name)
            if choice is None:
                # we select the first element of the list
                elems[0].click()
                return
            choice = choice.lower()
            choice_list = self.get_radio_list(name, 'list')
            # we transform the choice_list in lowercase
            for index in range(len(choice_list)):
                choice_list[index] = choice_list[index].lower()
            if choice in choice_list:
                for elem in elems:
                    value = elem.get_attribute("value")
                    if value == choice:
                        elem.click()
                        return
            # no match to be implement modifying warning
            sorry_style = styles.get_sorry()
            please_style = styles.get_please()
            text = (f"{sorry_style} the choice {choice} is not valid for the field {name}" +
                    f"{please_style} choose one in the following list: {choice_list}")
            self.set_warning_message(text)
            raise Exception
        except:
            if not self.warning_present:
                print("A problem occured while trying to set the choice {} in the radio with name {}".format(
                    choice, name))
            raise Exception

    # Select the choice of the user for the checkbox with the given name
    def set_choice_checkbox(self, name, choice):
        try:
            name = name.lower()
            elems = self.form_element.find_elements_by_name(name)
            choice_list = self.get_checkbox_list(name)
            if choice is None:
                for elem in elems:
                    if elem.is_selected():
                        elem.click()
                        return
            choice = choice.lower()
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
            text = ("{} the choice {} is not valid for the field {}" +
                    "{} choose one in the following list: {}").format(sorry_style,
                                                                      choice, please_style, choice_list)
            self.set_warning_message(text)
            raise Exception
        except:
            if not self.warning_present:
                print("A problem occured while trying to set the choice {} in the checkbox with name {}".format(
                    choice, name))
            raise Exception

    # Select the choices of the user for the checkbox with the given name
    def set_choices_checkbox(self, name, choices):
        try:
            name = name.lower()
            choices_lower = []
            for choice in choices:
                choices_lower.append(choice.lower())
            elems = self.form_element.find_elements_by_name(name)
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
                choices_string = fn.get_string_from_list(choices)
                sorry_style = styles.get_sorry()
                please_style = styles.get_please()
                text = ("{} none of the choices {} you proposed is valid for the field {}" +
                        "{} choose them in the following list: {}").format(sorry_style,
                                                                           choices_string, please_style, choice_list)
                self.set_warning_message(text)
                raise Exception
        except:
            if not self.warning_present:
                choices_list = fn.get_string_from_list(choices)
                print("A problem occured while trying to set the choices {} in the checkbox with name {}".format(
                    choices_list, name))
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
        self.all_required_filled = value

    def complete_spelling_value(self, string):
        self.current_spelling_input_value = self.current_spelling_input_value + string

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

    def set_possible_next_action(self, action):
        self.possible_next_action = action

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
            slot_name = self.next_slot
            next_slot_required = self.next_slot_required
            if slot_name is not None:
                if u.DEBUG:
                    print("the next slot is: " + slot_name)
                    # to observe the modification that happened
                    print(self.get_slots_value())
                string = "{}".format(
                    self.get_next_slot_text(slot_name, next_slot_required))
                if slot_name in self.get_spelling_fields() and u.READY_FOR_SPELLING:
                    self.add_spelling_name(slot_name)
                    please_style = styles.get_please()
                    string = (f'{string}\nSince it is a field requiring the spelling, we are going to take' +
                              f' its value one character at a time.\n{please_style} insert the first character')
            else:
                string = self.submit_string()
                self.set_possible_next_action('submitForm')
            return string
        except:
            print("Fail to manage the next step")
            raise Exception

    def managed_particular_case(self, slot_name_list, slot_value_list):
        try:
            # The particular case refers to a checkbox with more than one choice made
            if len(slot_name_list) != 1:
                return False
            if len(slot_name_list) >= len(slot_value_list):
                return False
            slot = slot_name_list[0]
            for slot in self.form_slots():
                if slot[u.slot_name].lower() == slot.lower():
                    value_name = slot[u.value_name]
                    value_type = slot[u.value_type]
                    break
            if value_type != "checkbox":
                return False
            self.set_choices_checkbox(
                name=value_name, choices=slot_value_list)
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
            self.get_next_slot()
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
            if not self.warning_present:
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
            # we are not in a checkbox with more than one choice made
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
                next_slot_name = self.get_next_slot()
                if next_slot_name is not None:
                    string = (" all the required fields have been completed form now on you can" +
                              " submit")
            return string
        except:
            if not self.warning_present:
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
            # values. Another choice could be to leave them as they are
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
                next_slot_name = self.get_next_slot()
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
            if not self.warning_present:
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
            if not self.warning_present:
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
            if not self.warning_present:
                print('Fail to complete the filling procedure')
            raise Exception
