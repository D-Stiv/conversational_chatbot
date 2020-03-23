# functions self contained and others used to restitute formated strings
import styles
import utility as u
import compatible as c


def extract_fields_names_and_values(entities):
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
                return c.verify_compatibility_time
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


def get_pairs(slots):
    try:
        string = ""
        text = "{} : {}"
        for slot in slots:
            slot_name = slot[u.slot_name]
            if slot_name != u.REQUESTED_SLOT:
                if slot[u.required]:
                    slot_name = slot_name + ' **'
                slot_value = slot[u.slot_value]
                string = "{}\t{}\n".format(
                    string, text.format(slot_name, slot_value))

        return string
    except:
        print("Fail to get the pairs")
        raise Exception


def verify_presence(name, slots):
    try:
        possible_names = []
        for slot in slots:
            slot_name = slot[u.slot_name]
            possible_names.append(slot_name)
        if name in possible_names:
            text = "the field {} is present.".format(name)
            return text, True
        alternatives = []
        for pos in possible_names:
            if name in pos:
                alternatives.append(pos)
        if len(alternatives) > 0:
            string_alt = get_string_from_list(alternatives)
            text = "the field {} is not present but you have these alternatives {}.".format(
                name, string_alt)
            return text, False
        sorry_style = styles.get_sorry()
        text = "the field {} is not present {}".format(name, sorry_style)
        return text, False
    except:
        print(f'Fail to verify the presence of {name}')
        raise Exception


def get_value_name(elem):
    try:
        simple_type_list = [u.button, u.color, u.date, u.datetime_local, u.email, u.file_type, u.hidden, u.image,
                            u.month, u.number, u.password, u.range_type, u.reset, u.search, u.submit, u.tel, u.text, u.time, u.url, u.week]
        multiple_choice_type_list = [u.checkbox, u.radio]
        el = elem.find_element_by_xpath(
            ".//div[@bot-entity = 'input_value']")
        value_type = el.get_attribute("entity-type")
        required = is_required(el)
        value_name = ""
        if value_type in simple_type_list:
            value_name = elem.find_element_by_xpath(
                ".//div[@bot-entity = 'input_value']/input").get_attribute("name")
        elif value_type == u.dropdowm:
            value_name = elem.find_element_by_xpath(
                ".//div[@bot-entity = 'input_value']/select").get_attribute("name")
        elif value_type == u.text_area:
            value_name = elem.find_element_by_xpath(
                ".//div[@bot-entity = 'input_value']/textarea").get_attribute("name")
        elif value_type in multiple_choice_type_list:
            value_name = elem.find_element_by_xpath(
                ".//div[@bot-entity = 'input_value']/div[1]/input").get_attribute("name")
        return value_name, value_type, required
    except:
        print("Fail to extract the values' name and the values' type")
        raise Exception


def get_input_fields(form_element):
    # return the list of slots containing matching of input_field name with input_value name
    # also returns the number of required camps and the total number of camps
    try:
        if u.NEW_ANNOTATION:
            return get_input_fields_new(form_element)
        slots = []
        elems = form_element.find_elements_by_xpath(
            ".//div[@bot-block='input_section']")
        first_found = False
        for elem in elems:
            Field = elem.find_element_by_xpath(
                ".//div[@bot-entity = 'input_field']").text
            # We use lower case to have a uniforme case such that the field_name = entity_value of the intent
            field = Field.lower()
            if not first_found:
                first = field
                first_found = True
            value_name, value_type, required = get_value_name(elem)
            slot = {
                "slot_value": None,         # value corresponding to a label
                "slot_name": field,         # label
                "value_name": value_name,   # name_id of the value camp for a label
                "value_type": value_type,   # type tha the value should have
                "required": required        # is the filling of a label required or not
            }
            slots.append(slot)
        slot_requested = {
            "slot_name": u.REQUESTED_SLOT,
            "slot_value": first
        }
        slots.append(slot_requested)
        return slots
    except:
        print("Fail to extract the form's input fields labels")
        raise Exception


def get_field_description_new(field, driver):
    try:
        elems_input = driver.find_elements_by_xpath("//input")   
        elems_dropdown = driver.find_elements_by_xpath("//select")
        elems_textarea = driver.find_elements_by_xpath("//textarea")
        elems = elems_input + elems_dropdown + elems_textarea
        for elem in elems:
            if elem.get_attribute(u.bot_field) == field:
                desc = elem.get_attribute('bot-desc')
                return desc
        # description not present
        return None
    except:
        print(f'Fail to get the description of the field {field}')
        raise Exception


def get_input_fields_new(form_element):
    try:
        elems_input = form_element.find_elements_by_xpath(".//input")   
        elems_dropdown = form_element.find_elements_by_xpath(".//select")
        elems_textarea = form_element.find_elements_by_xpath(".//textarea")
        elems = elems_input + elems_dropdown + elems_textarea
        slots = []
        first_field = ""
        for elem in elems:
            field = elem.get_attribute(u.bot_field)
            if field is not None:
                if first_field == "":
                    first_field = field.lower()
                value_name = elem.get_attribute('name')
                value_type = elem.get_attribute(u.field_type)
                if not value_type:
                    # the bot-type would be the same as the input type, so we avoid putting it
                    value_type = elem.get_attribute('type')
                if elem.get_attribute(u.required) is not None:
                    required = True
                else:
                    required = False
                if elem.get_attribute('field-spelling') is not None:
                    spelling = True
                else:
                    spelling = False
                slot = {
                    u.slot_value: None,         # value corresponding to a label
                    u.slot_name: field.lower(), # label
                    u.value_name: value_name,   # name_id of the value camp for a label
                    u.value_type: value_type,   # type tha the value should have
                    u.required: required,       # is the filling of a label required or not
                    u.spelling: spelling
                }
                slots.append(slot)
        requested_slot = {
            "slot_value": first_field,
            "slot_name": u.REQUESTED_SLOT
        }
        slots.append(requested_slot)
        return slots
    except:
        print('Fail to get the input field name')
        raise Exception


def get_required_string(required):
    if required:
        req = "this field is required"
    else:
        req = "this field is optional"
    return req


def is_required(element):
    # verifies if a driver element (corresponds to an input in our case) is required or not
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
