# functions self contained and others used to restitute formated strings
import styles
import utility as u
import compatible as c


def extract_fields_names_and_values(entities, only_names=False):
    try:
        count = len(entities)
        slot_name_list = []
        slot_value_list = []
        for index in range(count):
            newDict = {
                "value": entities[index]["value"],
                "entity": entities[index]["entity"]
            }
            if "input_field" in newDict["entity"]:
                # it means that the entity is a field's name, a slot name
                slot_name_list.append(newDict['value'])
            else:
                # it means that the entity is field's value, a slot value
                slot_value_list.append(newDict['value'])
        if only_names:
            return slot_name_list
        else:
            return slot_name_list, slot_value_list
    except:
        print('Fail to extract the names and values for an entity')
        raise Exception


def get_string_from_list(my_list):
    # Formats a list into a string and restitutes it
    try:
        string = ""
        for e in my_list:
            if string == "":
                string = e
            else:
                string = f'{string}, {e}'
        return string
    except:
        print("Fail to get the string from a list")
        raise Exception


def is_compatible(slot_value, value_type):
    # Verifies the compatibility between the user input and the value type that it should have
    try:
        # if no modification is done we retun the slot_value
        text = slot_value
        # list of types that we are handling
        types_list = [u.date, u.password, u.email, u.number, u.tel, u.time]
        if value_type in types_list:
            if value_type == u.email:
                return c.verify_compatibility_email(slot_value)
            if value_type == u.password:
                return c.verify_compatibility_password(slot_value)
            if value_type == u.tel:
                return c.verify_compatibility_tel(slot_value)
            if value_type == u.date:
                return c.verify_compatibility_date(slot_value)
            if value_type == u.number:
                return c.verify_compatibility_number(slot_value)
            if value_type == u.time:
                return c.verify_compatibility_time(slot_value)
        else:
            return c.verify_compatibility_generic(slot_value)
        return True, text
    except:
        print("A problem occured while verifying the compatibility of the value {} for the type {}".format(
            slot_value, value_type))
        raise Exception


def convert_to_int(string, tag=u.normal):
    try:
        # return a string that can be casted to int but not an int
        num_list = u.number_0_9
        special = [' ', '.', ',']
        new_string = string
        for char in string:
            if char in special:
                new_string = string.replace(char, '')
            elif char not in num_list:
                return None
        try:
            value = int(string)
        except:
            print(f'the string {string} cannot be transformed in integer')
            return None
        if tag == u.year:
            if value not in range(u.min_year, u.max_year+1):
                return None
        elif tag == u.month:
            if value not in range(u.min_month, u.max_month+1):
                return None
        elif tag == u.day:
            if value not in range(u.min_day, u.max_day+1):
                return None
        elif tag == u.hour:
            if value not in range(u.min_hour, u.max_hour+1):
                return None
        elif tag == u.minute:
            if value not in range(u.min_minute, u.max_minute+1):
                return None
        return new_string
    except:
        print(f'Fail to convert the value {string} into an integer form')
        raise Exception


def get_pairs(slots, only_filled=False):
    try:
        string = ""
        text = "{} : {}"
        for slot in slots:
            slot_name = slot[u.slot_name]
            if slot_name != u.REQUESTED_SLOT:
                if slot[u.required]:
                    slot_name = slot_name + ' **'
                slot_value = slot[u.slot_value]
                if slot_value is not None or not only_filled:
                    # we do not enter when we find only filled and the value is None
                    string = "{}\t{}\n".format(
                        string, text.format(slot_name, slot_value))
        return string
    except:
        print("Fail to get the pairs")
        raise Exception


def verify_presence(name, slots, only_presence=False, only_text=False):
    try:
        possible_names = []
        for slot in slots:
            slot_name = slot[u.slot_name]
            possible_names.append(slot_name)
        if name in possible_names:
            text = "the field {} is present.".format(name)
            if only_presence:
                return True
            elif only_text:
                return text
            else:
                return text, True
        alternatives = []
        for pos in possible_names:
            if name in pos:
                alternatives.append(pos)
        if len(alternatives) > 0:
            string_alt = get_string_from_list(alternatives)
            text = "the field {} is not present but you have these alternatives {}.".format(
                name, string_alt)
            if only_presence:
                return False
            elif only_text:
                return text
            else:
                return text, False
        sorry_style = styles.get_sorry()
        text = "the field {} is not present {}".format(name, sorry_style)
        if only_presence:
            return False
        elif only_text:
            return text
        else:
            return text, False
    except:
        print(f'Fail to verify the presence of {name}')
        raise Exception


def get_input_fields(form_element):
    # return the list of slots containing matching of input_field name with input_value name
    # also returns the number of required camps and the total number of camps
    try:
        elems_input = form_element.find_elements_by_xpath(".//input")
        elems_dropdown = form_element.find_elements_by_xpath(".//select")
        elems_textarea = form_element.find_elements_by_xpath(".//textarea")
        elems = elems_input + elems_dropdown + elems_textarea
        slots = []
        for elem in elems:
            field = elem.get_attribute(u.bot_field)
            if field is not None:
                value_name = elem.get_attribute('name')
                value_type = elem.get_attribute(u.field_type)
                description = elem.get_attribute(u.field_desc)
                if not value_type:
                    # the bot-type would be the same as the input type, so we avoid putting it
                    value_type = elem.get_attribute('type')
                if elem.get_attribute(u.required) is not None:
                    required = True
                else:
                    required = False
                if elem.get_attribute(u.field_spelling) is not None:
                    spelling = True
                else:
                    spelling = False
                slot = {
                    u.slot_value: None,         # value corresponding to a label
                    u.slot_name: field.lower(),  # label
                    u.value_name: value_name,   # name_id of the value camp for a label
                    u.value_type: value_type,   # type tha the value should have
                    u.required: required,       # is the filling of a label required or not
                    u.description: description,  # description/explanation of a field
                    u.spelling: spelling
                }
                # in case of field with choices, we insert the list of choices
                if value_type in u.choices_type_list:
                    choice_list = get_choice_list(
                        value_name, value_type, form_element)
                    slot[u.choice_list] = choice_list
                slots.append(slot)
                #slots = [slot] + slots
        # we save the form description and title inside the requested slot
        description = form_element.get_attribute(u.bot_desc)
        title = form_element.get_attribute(u.bot_title)
        requested_slot = {
            u.slot_value: slots[0][u.slot_name],
            u.slot_name: u.REQUESTED_SLOT,
            u.description: description,
            u.title: title
        }
        slots.append(requested_slot)
        return slots
    except:
        print("Fail to extract the names of the form's input fields")
        raise Exception


def get_choice_list(choice_name, choice_type, web_elem):
    try:
        if choice_type == u.dropdown:
            name = choice_name.lower()
            elem = web_elem.find_element_by_name(name)
            choice_list = []
            options = elem.find_elements_by_xpath(".//option")
            for option in options:
                choice_list.append(option.text)
        elif choice_type in [u.radio, u.checkbox]:
            name = choice_name.lower()
            elems = web_elem.find_elements_by_name(name)
            choice_list = []
            for elem in elems:
                value = elem.get_attribute("value")
                choice_list.append(value)
        return choice_list
    except:
        print(f'Fail to get the list for the slot {name}')
        raise Exception


def get_required_string(required):
    if required:
        req = "this field is required"
    else:
        req = "this field is optional"
    return req


def is_required(element):
    # verifies if a form_element element (corresponds to an input in our case) is required or not
    value = element.get_attribute(u.required)
    if value != None:
        return True
    else:
        return False


def get_proposals(values):
    try:
        text = '{} - {}'
        string = ''
        first = True
        for index in range(len(values)):
            if first:
                string = text.format(index, values[index])
                first = False
            else:
                string = f'{string}\t{text.format(index. values[index])}'
        return string
    except:
        print(f'Fail to get the proposals')
        raise Exception


def get_num_fields(constructs):
    try:
        slots = constructs["form"]["slots"]
        total = 0
        required = 0
        optional = 0
        for slot in slots:
            if slot[u.slot_name] != u.REQUESTED_SLOT:
                total = total + 1
                if slot[u.required]:
                    required = required + 1
                else:
                    optional = optional + 1
        return total, required, optional
    except:
        print(f'Fail to get the number of fields')
        raise Exception


def next_char_string():
    try:
        # we add styles to the output
        next_style = styles.get_next()
        please_style = styles.get_please()
        end_style = styles.get_end()
        # we set the message to be returned to the user
        string = (f'{please_style} insert the {next_style} character, remember that you can use the expression SPACE for the blank' +
                  f' and the expression TERMINATE to {end_style} the spelling')
        return string
    except:
        print('Fail to get the string for asking the next character')
        raise Exception
