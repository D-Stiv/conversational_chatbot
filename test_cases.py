# structural test cases
import utility as u

# intents
complete_field = 'fillGenericField'
affirm = 'affirm'
deny = 'deny'
submit_form = 'submitForm'
reset_all_fields = 'resetAllFields'
spelling = 'spelling'
modify_value_field = 'modifyValueGenericField'
repeat_value_field = 'repeatValueField'
repeat_all_fields = 'repeatAllFields'
repeat_required_fields = 'repeatRequiredFields'
repeat_optional_fields = 'repeatOptionalFields'
give_all_remaining_fields = 'giveAllRemainingFields'
give_remaining_required_fields = 'giveRemainingRequiredFields'
give_remaining_optional_fields = 'giveRemainingOptionalFields'
skip_field = 'skipField'
verify_presence_field = 'verifyPresenceOfField'
verify_value_fields = 'verifyValueFilledFields'
repeat_form_explanation = 'repeatFormExplanation'
repeat_form_title = 'repeatFormTitle'
explain_field = 'explainField'

# keys
message_id = "message_id"
test_form_number = "test_form_number"
initial_state = "initial_situation"
spelling_state = "spelling_state"
machine_parameters = "machine_parameters"
test_case_message = "test_case_message"
result_expected = "result_expected"

input_field = "input_field"
input_value = "input_value"

entities = "entities"
intent = "intent"
text = "text"

entity = "entity"
value = "value"
name = "name"
confidence = "confidence"

functional = "functional"
structural = "structural"

# list of fields
first_name = 'first name'
last_name = 'last name'
mark = 'mark'
password = 'password'
email_address = 'email address'
phone_number = 'phone number'
number_persons = 'number of persons'
birthday = 'birthday'
arrival_time = 'arrival time'
car = 'car'
gender = 'gender'
electronic_devices = 'electronic devices'
message = 'message'

structural_test_cases = [
    {
        message_id: "000",
        test_form_number: 1,
        initial_state: {
            u.slots: [
                {
                    u.slot_name: first_name,
                    u.slot_value: None
                },
                {
                    u.slot_name: mark,
                    u.slot_value: None
                },
                {
                    u.slot_name: password,
                    u.slot_value: None
                },
                {
                    u.slot_name: email_address,
                    u.slot_value: None
                }
            ]
        },
        test_case_message: {
            entities: [],
            intent: {
                name: repeat_form_title,
                confidence: 1
            },
            text: 'please tell me the title of the form again'
        },
        result_expected: 'The form does not have a title'
    },
    {
        message_id: "001",
        test_form_number: 3,
        initial_state: {},
        test_case_message: {
            entities: [],
            intent: {
                name: repeat_form_title,
                confidence: 1
            },
            text: 'give me the title of the form'
        },
        result_expected: 'The title of this form is test form sample number 3'
    },
    {
        message_id: "002",
        test_form_number: 1,
        initial_state: {},
        test_case_message: {
            entities: [],
            intent: {
                name: repeat_form_explanation,
                confidence: 1
            },
            text: 'what is this form about?'
        },
        result_expected: 'It does not have a description'
    },
    {
        message_id: "003",
        test_form_number: 1,
        initial_state: {},
        test_case_message: {
            entities: [],
            intent: {
                name: complete_field,
                confidence: 1
            },
            text: 'add the value of the field'
        },
        result_expected: 'Which field exactly would you like to {modify} and which value do you want to {insert} for that field?'
    },
    {
        message_id: "004",
        test_form_number: 1,
        initial_state: {
            machine_parameters: {
                u.possible_next_action: spelling
            }
        },
        test_case_message: {
            entities: [
                {
                    entity: input_field,
                    value: email_address
                },
                {
                    entity: input_value,
                    value: 'alfred@hot.it'
                },
                {
                    entity: input_value,
                    value: '28.5'
                },
                {
                    entity: input_field,
                    value: mark
                }
            ],
            intent: {
                name: complete_field,
                confidence: 1
            },
            text: 'my email address is alfred@hot.it and 28,5 is the mark'
        },
        result_expected: '{sorry} i did not understand your request, could you reformulate {please}'
    },
    {
        message_id: "005",
        test_form_number: 1,
        initial_state: {
            u.slots: [
                {
                    u.slot_name: first_name,
                    u.slot_value: None
                }
            ],
            spelling_state: {
                u.spelling_list: [last_name, first_name],
                u.after_spelling: True
            }
        },
        test_case_message: {
            entities: [],
            intent: {
                name: complete_field,
                confidence: 1
            },
            text: 'i want to complete a field'
        },
        result_expected: 'Now you are going to spell the value for the field {last name}, {please} insert the first character'
    },
    {
        message_id: "006",
        test_form_number: 1,
        initial_state: {
            u.slots: [
                {
                    u.slot_name: first_name,
                    u.slot_value: None
                }
            ],
            spelling_state: {
                u.spelling_list: [first_name],
                u.after_spelling: False
            }
        },
        test_case_message: {
            entities: [],
            intent: {
                name: complete_field,
                confidence: 1
            },
            text: 'i want to complete the field'
        },
        result_expected: 'You will have to spell the value for the field {first name}'
    },
    {
        message_id: "007",
        test_form_number: 1,
        initial_state: {
            u.slots: [
                {
                    u.slot_name: first_name,
                    u.slot_value: None
                },
                {
                    u.slot_name: last_name,
                    u.slot_value: None
                }
            ],
            spelling_state: {
                u.spelling_list: [first_name, last_name],
                u.after_spelling: False
            }
        },
        test_case_message: {
            entities: [],
            intent: {
                name: complete_field,
                confidence: 1
            },
            text: 'i want to complete a field'
        },
        result_expected: 'You will have to spell the value for the following fieldss {first name, last name}.  We start by the field {first name}'
    },
    {
        message_id: "008",
        test_form_number: 1,
        initial_state: {
            u.slots: [
                {
                    u.slot_name: first_name,
                    u.slot_value: None
                },
                {
                    u.slot_name: last_name,
                    u.slot_value: None
                }
            ],
            spelling_state: {
                u.spelling_list: [first_name, last_name],
                u.after_spelling: False
            }
        },
        test_case_message: {
            entities: [],
            intent: {
                name: complete_field,
                confidence: 1
            },
            text: 'complete a field'
        },
        result_expected: '… insert the first character, you will be able to use SPACE for spacing and TERMINATE to {conclude} the spelling'
    },
    {
        message_id: "009",
        test_form_number: 1,
        initial_state: {
            spelling_state: {
                u.close_prompt_enabled: False,
                u.current_spelling_input_value: '',
                u.spelling_list: [],
                u.waiting_message: None,
                u.saved_spelling_fields: [],
                u.saved_spelling_values: []
            },
            machine_parameters: {
                u.submit_done: False,
                u.reset_alarm_enabled: False,
                u.submit_alarm_enabled: False,
                u.possible_next_action: None,
                u.warning_message: ''
            }
        },
        test_case_message: {
            entities: [],
            intent: {
                name: spelling,
                confidence: 1
            },
            text: 'rome'
        },
        result_expected: 'Your input {input} is not valid, try to insert only the character please'
    },
    {
        message_id: "010",
        test_form_number: 1,
        initial_state: {
            u.slots: [
                {
                    u.slot_name: first_name,
                    u.slot_value: None
                },
                {
                    u.slot_name: last_name,
                    u.slot_value: None
                },
                {
                    u.slot_name: mark,
                    u.slot_value: None
                },
                {
                    u.slot_name: password,
                    u.slot_value: None
                },
                {
                    u.slot_name: email_address,
                    u.slot_value: None
                }
            ],
            spelling_state: {
                u.close_prompt_enabled: False,
                u.current_spelling_input_value: '',
                u.spelling_list: [],
                u.waiting_message: None,
                u.saved_spelling_fields: [],
                u.saved_spelling_values: []
            },
            machine_parameters: {
                u.submit_done: False,
                u.reset_alarm_enabled: False,
                u.submit_alarm_enabled: False,
                u.possible_next_action: None,
                u.warning_message: ''
            }
        },
        test_case_message: {
            entities: [
                {
                    entity: 'spelling',
                    value: 'terminator'
                }
            ],
            intent: {
                name: spelling,
                confidence: 1
            },
            text: 'terminator'
        },
        result_expected: "You should insert at least one character different from 'blank'"
    },
    {
        message_id: "011",
        test_form_number: 2,
        initial_state: {
            u.slots: [
                {
                    u.slot_name: number_persons,
                    u.slot_value: None
                },
                {
                    u.slot_name: phone_number,
                    u.slot_value: None
                },
                {
                    u.slot_name: birthday,
                    u.slot_value: None
                },
                {
                    u.slot_name: arrival_time,
                    u.slot_value: None
                }
            ],
            spelling_state: {
                u.close_prompt_enabled: False,
                u.current_spelling_input_value: '',
                u.spelling_list: [],
                u.waiting_message: None,
                u.saved_spelling_fields: [],
                u.saved_spelling_values: []
            },
            machine_parameters: {
                u.submit_done: False,
                u.reset_alarm_enabled: False,
                u.submit_alarm_enabled: False,
                u.possible_next_action: None,
                u.warning_message: ''
            }
        },
        initial_state: {
            u.slots: [
                {
                    u.slot_name: phone_number,
                    u.slot_value: "3986452734"
                },
                {
                    u.slot_name: number_persons,
                    u.slot_value: "4"
                },
                {
                    u.slot_name: birthday,
                    u.slot_value: "12/03/2010"
                }
            ]
        },
        test_case_message: {
            entities: [],
            intent: {
                name: verify_presence_field,
                confidence: 1
            },
            text: 'is the field presnt in the form?'
        },
        result_expected: '{please} indicate which field you are interested to'
    },
    {
        message_id: "012",
        test_form_number: 2,
        initial_state: {
            machine_parameters: {
                u.possible_next_action: None
            }
        },
        test_case_message: {
            entities: [],
            intent: {
                name: affirm,
                confidence: 1
            },
            text: 'yes'
        },
        result_expected: '{sorry} what exactly do you want to do?'
    },
    {
        message_id: "013",
        test_form_number: 2,
        initial_state: {
            u.slots: [
                {
                    u.slot_name: arrival_time,
                    u.slot_value: None
                }
            ]
        },
        test_case_message: {
            entities: [],
            intent: {
                name: deny,
                confidence: 1
            },
            text: 'no'
        },
        result_expected: '{well}, what do you want to do now?'
    },
    {
        message_id: "014",
        test_form_number: 2,
        initial_state: {},
        test_case_message: {
            entities: [],
            intent: {
                name: verify_value_fields,
                confidence: 1
            },
            text: 'i want the recap of what have been done so far'
        },
        result_expected: 'Here is the answer for you : …   '
    },
    {
        message_id: "015",
        test_form_number: 2,
        initial_state: {
            u.slots: [
                {
                    u.slot_name: birthday,
                    u.slot_value: None
                }
            ]
        },
        test_case_message: {
            entities: [
                {
                    entity: input_field,
                    value: birthday
                }
            ],
            intent: {
                name: repeat_value_field,
                confidence: 1
            },
            text: 'what is the value of the birthday?'
        },
        result_expected: '… No value ….'
    },
    {
        message_id: "016",
        test_form_number: 2,
        initial_state: {},
        test_case_message: {
            entities: [],
            intent: {
                name: skip_field,
                confidence: 1
            },
            text: 'skip'
        },
        result_expected: '{sorry} this field is the last one remaining'
    },
    {
        message_id: "017",
        test_form_number: 2,
        initial_state: {},
        test_case_message: {
            entities: [],
            intent: {
                name: skip_field,
                confidence: 1
            },
            text: 'skip'
        },
        result_expected: '… do you want to submit now?'
    },
    {
        message_id: "018",
        test_form_number: 1,
        initial_state: {
            u.slots: [
                {
                    u.slot_name: first_name,
                    u.slot_value: "rock"
                },
                {
                    u.slot_name: mark,
                    u.slot_value: "23,45"
                },
                {
                    u.slot_name: password,
                    u.slot_value: "empty_pass@rt"
                },
                {
                    u.slot_name: email_address,
                    u.slot_value: None
                }
            ]
        },
        test_case_message: {
            entities: [],
            intent: {
                name: skip_field,
                confidence: 1
            },
            text: 'skip'
        },
        result_expected: '… it is required to submit the form …'
    },
    {
        message_id: "019",
        test_form_number: 1,
        initial_state: {},
        test_case_message: {
            entities: [],
            intent: {
                name: repeat_required_fields,
                confidence: 1
            },
            text: 'which are the required fields?'
        },
        result_expected: '{sure} the required fields are the following {fields}'
    },
    {
        message_id: "020",
        test_form_number: 1,
        initial_state: {},
        test_case_message: {
            entities: [],
            intent: {
                name: repeat_optional_fields,
                confidence: 1
            },
            text: 'which are the optional fields of this form?'
        },
        result_expected: '{sure} the optional fields are the following {fields}'
    },
    {
        message_id: "021",
        test_form_number: 3,
        initial_state: {},
        test_case_message: {
            entities: [],
            intent: {
                name: repeat_all_fields,
                confidence: 1
            },
            text: 'which are the fields of this form?'
        },
        result_expected: '{sure} the fields present in this form are the following {fields}'
    },
    {
        message_id: "022",
        test_form_number: 3,
        initial_state: {
            u.slots: [
                {
                    u.slot_name: car,
                    u.slot_value: "bmw"
                },
                {
                    u.slot_name: gender,
                    u.slot_value: None
                },
                {
                    u.slot_name: electronic_devices,
                    u.slot_value: "smartphone"
                },
                {
                    u.slot_name: message,
                    u.slot_value: None
                }
            ]
        },
        test_case_message: {
            entities: [],
            intent: {
                name: give_remaining_required_fields,
                confidence: 1
            },
            text: 'which are the required remaining fields'
        },
        result_expected: '{sure} the remaining required fields are the following {fields}'
    },
    {
        message_id: "023",
        test_form_number: 3,
        initial_state: {},
        test_case_message: {
            entities: [],
            intent: {
                name: give_remaining_optional_fields,
                confidence: 1
            },
            text: 'which are the remaining optional fields?'
        },
        result_expected: '{sure} the remaining optional fields are the following {fields}'
    },
    {
        message_id: "024",
        test_form_number: 3,
        initial_state: {},
        test_case_message: {
            entities: [],
            intent: {
                name: give_all_remaining_fields,
                confidence: 1
            },
            text: 'which are the remaining fields'
        },
        result_expected: '{sure} the remaining fields present in this form are the following {fields}'
    },
    {
        message_id: "025",
        test_form_number: 3,
        initial_state: {
            u.slots: [
                {
                    u.slot_name: car,
                    u.slot_value: None
                },
                {
                    u.slot_name: gender,
                    u.slot_value: None
                },
                {
                    u.slot_name: electronic_devices,
                    u.slot_value: None
                },
                {
                    u.slot_name: message,
                    u.slot_value: None
                }
            ]
        },
        test_case_message: {
            entities: [],
            intent: {
                name: verify_value_fields,
                confidence: 1
            },
            text: 'i want to have the summary please'
        },
        result_expected: '{sorry} up to now you did not complete any field…'
    },
    {
        message_id: "026",
        test_form_number: 3,
        initial_state: {
            u.slots: [
                {
                    u.slot_name: gender,
                    u.slot_value: "male"
                }
            ]
        },
        test_case_message: {
            entities: [],
            intent: {
                name: verify_value_fields,
                confidence: 1
            },
            text: 'can i have the summary please?'
        },
        result_expected: 'The fields you already complete are he following {fields}. The stars represent the required fields'
    },
    {
        message_id: "027",
        test_form_number: 1,
        initial_state: {
            machine_parameters: {
                u.reset_alarm_enabled: False
            }
        },
        test_case_message: {
            entities: [],
            intent: {
                name: reset_all_fields,
                confidence: 1
            },
            text: 'reset'
        },
        result_expected: 'We are about to reset all the field. Are you sure you want to continue with this action?'
    },
    {
        message_id: "028",
        test_form_number: 2,
        initial_state: {
            u.slots: [
                {
                    u.slot_name: phone_number,
                    u.slot_value: "3549213458"
                },
                {
                    u.slot_name: number_persons,
                    u.slot_value: "1"
                },
                {
                    u.slot_name: birthday,
                    u.slot_value: "12/12/2012"
                }
            ],
            machine_parameters: {
                u.reset_alarm_enabled: True
            }
        },
        test_case_message: {
            entities: [],
            intent: {
                name: reset_all_fields,
                confidence: 1
            },
            text: 'reset'
        },
        result_expected: 'All the fields have been reset, now we restart the process'
    },
    {
        message_id: "029",
        test_form_number: 1,
        initial_state: {
            u.slots: [
                {
                    u.slot_name: first_name,
                    u.slot_value: "alfonso"
                },
                {
                    u.slot_name: mark,
                    u.slot_value: None
                },
                {
                    u.slot_name: password,
                    u.slot_value: "p!^ss_w%@rd"
                },
                {
                    u.slot_name: email_address,
                    u.slot_value: None
                }
            ]
        },
        test_case_message: {
            entities: [],
            intent: {
                name: submit_form,
                confidence: 1
            },
            text: 'submit'
        },
        result_expected: 'Not all the required fields have been completed. You still have to complete the following required fields {fields}'
    },
    {
        message_id: "030",
        test_form_number: 1,
        initial_state: {
            u.slots: [
                {
                    u.slot_name: email_address,
                    u.slot_value: "em@il.it"
                }
            ],
            machine_parameters: {
                u.submit_alarm_enabled: False
            }
        },
        test_case_message: {
            entities: [],
            intent: {
                name: submit_form,
                confidence: 1
            },
            text: 'submit the form'
        },
        result_expected: 'We are going to submit, are you sure you want to continue with this action?'
    },
    {
        message_id: "031",
        test_form_number: 2,
        initial_state: {},
        test_case_message: {
            entities: [
                {
                    entity: input_field,
                    value: birthday
                },
                {
                    entity: input_value,
                    value: '5 oct 2010'
                }
            ],
            intent: {
                name: complete_field,
                confidence: 1
            },
            text: 'the card expiration date is 5 oct 2010'
        },
        result_expected: 'It is possible that the month you inserted is not well written'
    },
    {
        message_id: "032",
        test_form_number: 1,
        initial_state: {
            spelling_state: {
                u.close_prompt_enabled: False,
                u.current_spelling_input_value: '',
                u.spelling_list: [],
                u.waiting_message: None,
                u.saved_spelling_fields: [],
                u.saved_spelling_values: []
            },
            machine_parameters: {
                u.submit_done: False,
                u.reset_alarm_enabled: False,
                u.submit_alarm_enabled: False,
                u.possible_next_action: None,
                u.warning_message: ''
            }
        },
        test_case_message: {
            entities: [
                {
                    entity: input_field,
                    value: 'name'
                },
                {
                    entity: input_value,
                    value: 'gorges'
                }
            ],
            intent: {
                name: complete_field,
                confidence: 1
            },
            text: 'my name is gorges'
        },
        result_expected: 'The name {name} does not correspond to any label. The fields present are the following {fields}. Which field do you want to modify?'
    },
    {
        message_id: "033",
        test_form_number: 1,
        initial_state: {},
        test_case_message: {
            entities: [
                {
                    entity: input_field,
                    value: 'anniversary'
                }
            ],
            intent: {
                name: repeat_value_field,
                confidence: 1
            },
            text: 'what is the value of anniversary?'
        },
        result_expected: '{sorry} the field {anniversary} is not present in this form. {please} could you precise the action you want to perfect?'
    },
    {
        message_id: "034",
        test_form_number: 3,
        initial_state: {
            u.slots: [
                {
                    u.slot_name: car,
                    u.slot_value: "honda"
                }
            ],
            spelling_state: {
                u.close_prompt_enabled: False,
                u.current_spelling_input_value: '',
                u.spelling_list: [],
                u.waiting_message: None,
                u.saved_spelling_fields: [],
                u.saved_spelling_values: []
            },
            machine_parameters: {
                u.submit_done: False,
                u.reset_alarm_enabled: False,
                u.submit_alarm_enabled: False,
                u.possible_next_action: None,
                u.warning_message: ''
            }
        },
        test_case_message: {
            entities: [
                {
                    entity: gender,
                    value: 'other'
                }
            ],
            intent: {
                name: complete_field,
                confidence: 1
            },
            text: 'gender is other'
        },
        result_expected: 'Select the {gender} in the following list {fields} …'
    },
    {
        message_id: "035",
        test_form_number: 3,
        initial_state: {
            u.slots: [
                {
                    u.slot_name: gender,
                    u.slot_value: None
                },
                {
                    u.slot_name: car,
                    u.slot_value: None
                }
            ],
            spelling_state: {
                u.close_prompt_enabled: False,
                u.current_spelling_input_value: '',
                u.spelling_list: [],
                u.waiting_message: None,
                u.saved_spelling_fields: [],
                u.saved_spelling_values: []
            },
            machine_parameters: {
                u.submit_done: False,
                u.reset_alarm_enabled: False,
                u.submit_alarm_enabled: False,
                u.possible_next_action: None,
                u.warning_message: ''
            }
        },
        test_case_message: {
            entities: [
                {
                    entity: input_field,
                    value: car
                },
                {
                    entity: input_value,
                    value: 'hyundai'
                }
            ],
            intent: {
                name: complete_field,
                confidence: 1
            },
            text: 'the car is hyundai'
        },
        result_expected: 'Choose your {car} in the following list {fields} …'
    },
    {
        message_id: "036",
        test_form_number: 2,
        initial_state: {
            u.slots: [
                {
                    u.slot_name: phone_number,
                    u.slot_value: None
                },
                {
                    u.slot_name: number_persons,
                    u.slot_value: None
                },
                {
                    u.slot_name: birthday,
                    u.slot_value: None
                }
            ],
            spelling_state: {
                u.close_prompt_enabled: False,
                u.current_spelling_input_value: '',
                u.spelling_list: [],
                u.waiting_message: None,
                u.saved_spelling_fields: [],
                u.saved_spelling_values: []
            },
            machine_parameters: {
                u.submit_done: False,
                u.reset_alarm_enabled: False,
                u.submit_alarm_enabled: False,
                u.possible_next_action: None,
                u.warning_message: ''
            }
        },
        test_case_message: {
            entities: [
                {
                    entity: input_field,
                    value: phone_number
                },
                {
                    entity: input_value,
                    value: '55483498'
                }
            ],
            intent: {
                name: complete_field,
                confidence: 1
            },
            text: 'my phone number is 55483498'
        },
        result_expected: '{please} {insert} the value for the field {phone number} …'
    },
    {
        message_id: "037",
        test_form_number: 2,
        initial_state: {},
        test_case_message: {
            entities: [
                {
                    entity: input_field,
                    value: number_persons
                },
                {
                    entity: input_value,
                    value: 'steve'
                }
            ],
            intent: {
                name: complete_field,
                confidence: 1
            },
            text: 'the number of persons is steve'
        },
        result_expected: 'Incompatibility between the value {value} and the type {type} …'
    },
    {
        message_id: "038",
        test_form_number: 3,
        initial_state: {
            spelling_state: {
                u.close_prompt_enabled: False,
                u.current_spelling_input_value: '',
                u.spelling_list: [],
                u.waiting_message: None,
                u.saved_spelling_fields: [],
                u.saved_spelling_values: []
            },
            machine_parameters: {
                u.submit_done: False,
                u.reset_alarm_enabled: False,
                u.submit_alarm_enabled: False,
                u.possible_next_action: None,
                u.warning_message: ''
            }
        },
        test_case_message: {
            entities: [
                {
                    entity: input_field,
                    value: gender
                },
                {
                    entity: input_value,
                    value: 'man'
                }
            ],
            intent: {
                name: complete_field,
                confidence: 1
            },
            text: 'my gender is man'
        },
        result_expected: '{sorry} the choice {choice} is not valid for the field {gender}. Please choose one in the following list: {values}'
    },
    {
        message_id: "039",
        test_form_number: 3,
        initial_state: {
            spelling_state: {
                u.close_prompt_enabled: False,
                u.current_spelling_input_value: '',
                u.spelling_list: [],
                u.waiting_message: None,
                u.saved_spelling_fields: [],
                u.saved_spelling_values: []
            },
            machine_parameters: {
                u.submit_done: False,
                u.reset_alarm_enabled: False,
                u.submit_alarm_enabled: False,
                u.possible_next_action: None,
                u.warning_message: ''
            }
        },
        test_case_message: {
            entities: [
                {
                    entity: input_field,
                    value: electronic_devices
                },
                {
                    entity: input_value,
                    value: 'smart'
                },
                {
                    entity: input_value,
                    value: 'phone'
                }
            ],
            intent: {
                name: complete_field,
                confidence: 1
            },
            text: 'my electronic devices are smart and phone'
        },
        result_expected: '{sorry} none of the choices {choices} you proposed is valid for the field {electronic devices}. Please choose them in the following list {values}'
    },
    {
        message_id: "040",
        test_form_number: 1,
        initial_state: {
            spelling_state: {
                u.close_prompt_enabled: False,
                u.current_spelling_input_value: '',
                u.spelling_list: [],
                u.waiting_message: None,
                u.saved_spelling_fields: [],
                u.saved_spelling_values: []
            },
            machine_parameters: {
                u.submit_done: False,
                u.reset_alarm_enabled: False,
                u.submit_alarm_enabled: False,
                u.possible_next_action: None,
                u.warning_message: ''
            }
        },
        test_case_message: {
            entities: [
                {
                    entity: input_field,
                    value: mark
                }
            ],
            intent: {
                name: explain_field,
                confidence: 1
            },
            text: 'what is mark?'
        },
        result_expected: 'There is no explanation provided for the field {mark} {sorry}'
    },
    {
        message_id: "041",
        test_form_number: 1,
        initial_state: {
            u.slots: [
                {
                    u.slot_name: first_name,
                    u.slot_value: "harry"
                },
                {
                    u.slot_name: mark,
                    u.slot_value: "23,56"
                },
                {
                    u.slot_name: password,
                    u.slot_value: "passitoword"
                }
            ],
            spelling_state: {
                u.close_prompt_enabled: False,
                u.current_spelling_input_value: '',
                u.spelling_list: [],
                u.waiting_message: None,
                u.saved_spelling_fields: [],
                u.saved_spelling_values: []
            },
            machine_parameters: {
                u.submit_done: False,
                u.reset_alarm_enabled: False,
                u.submit_alarm_enabled: False,
                u.possible_next_action: None,
                u.warning_message: ''
            }
        },
        test_case_message: {
            entities: [
                {
                    entity: input_field,
                    value: email_address
                },
                {
                    entity: input_value,
                    value: 'emai_@.mail.polimi.it'
                }
            ],
            intent: {
                name: modify_value_field,
                confidence: 1
            },
            text: 'i want to modify the field email address with the value emai_@.mail.polimi.it'
        },
        result_expected: 'All the fields have been completed. Is everything {okay} for the submission. Here is the summary {summary}. The stars indicate the required fields'
    },
    {
        message_id: "042",
        test_form_number: 1,
        initial_state: {
            u.slots: [
                {
                    u.slot_name: first_name,
                    u.slot_value: None
                }
            ],
            spelling_state: {
                u.close_prompt_enabled: False,
                u.current_spelling_input_value: '',
                u.spelling_list: [],
                u.waiting_message: None,
                u.saved_spelling_fields: [first_name],
                u.saved_spelling_values: ["alda"]
            },
            machine_parameters: {
                u.submit_done: False,
                u.reset_alarm_enabled: False,
                u.submit_alarm_enabled: False,
                u.possible_next_action: None,
                u.warning_message: ''
            }
        },
        test_case_message: {
            entities: [],
            intent: {
                name: repeat_required_fields,
                confidence: 1
            },
            text: 'which are the required fields?'
        },
        result_expected: 'You started filling the field {first name} and the current value is {alda} {please} insert the {next} character'
    },
    {
        message_id: "043",
        test_form_number: 2,
        initial_state: {
            u.slots: [
                {
                    u.slot_name: phone_number,
                    u.slot_value: None
                },
                {
                    u.slot_name: number_persons,
                    u.slot_value: "4"
                },
                {
                    u.slot_name: birthday,
                    u.slot_value: None
                }
            ],
            spelling_state: {
                u.close_prompt_enabled: False,
                u.current_spelling_input_value: '',
                u.spelling_list: [],
                u.waiting_message: None,
                u.saved_spelling_fields: [],
                u.saved_spelling_values: []
            },
            machine_parameters: {
                u.submit_done: False,
                u.reset_alarm_enabled: False,
                u.submit_alarm_enabled: False,
                u.possible_next_action: None,
                u.warning_message: ''
            }
        },
        test_case_message: {
            entities: [],
            intent: {
                name: give_all_remaining_fields,
                confidence: 1
            },
            text: 'which are the fields still to be completed?'
        },
        result_expected: '… Since it is a field requiring the spelling, we are going to take its value one character at a time …'
    },
    {
        message_id: "044",
        test_form_number: 3,
        initial_state: {
            u.slots: [
                {
                    u.slot_name: car,
                    u.slot_value: None
                },
                {
                    u.slot_name: gender,
                    u.slot_value: None
                }
            ],
            spelling_state: {
                u.close_prompt_enabled: False,
                u.current_spelling_input_value: '',
                u.spelling_list: [],
                u.waiting_message: None,
                u.saved_spelling_fields: [],
                u.saved_spelling_values: []
            },
            machine_parameters: {
                u.submit_done: False,
                u.reset_alarm_enabled: False,
                u.submit_alarm_enabled: False,
                u.possible_next_action: None,
                u.warning_message: ''
            }
        },
        test_case_message: {
            entities: [
                {
                    entity: input_field,
                    value: gender
                },
                {
                    entity: input_value,
                    value: 'male'
                }
            ],
            intent: {
                name: complete_field,
                confidence: 1
            },
            text: 'the gender is male'
        },
        result_expected: 'All the required fields have been completed, from now on you can submit'
    },
    {
        message_id: "045",
        test_form_number: 2,
        initial_state: {
            spelling_state: {
                u.close_prompt_enabled: False,
                u.current_spelling_input_value: '',
                u.spelling_list: [],
                u.waiting_message: None,
                u.saved_spelling_fields: [],
                u.saved_spelling_values: []
            },
            machine_parameters: {
                u.submit_done: False,
                u.reset_alarm_enabled: False,
                u.submit_alarm_enabled: False,
                u.possible_next_action: None,
                u.warning_message: ''
            }
        },
        test_case_message: {
            entities: [
                {
                    entity: input_field,
                    value: arrival_time
                },
                {
                    entity: input_value,
                    value: '7 pm'
                },
                {
                    entity: input_field,
                    value: birthday
                }
            ],
            intent: {
                name: modify_value_field,
                confidence: 1
            },
            text: 'i want to modify the arrival time putting 7 pm, i also want to change th birthday'
        },
        result_expected: 'You wanted to {modify} the fields {birthday} but you did not insert the values'
    },
    {
        message_id: "046",
        test_form_number: 1,
        initial_state: {
            spelling_state: {
                u.close_prompt_enabled: False,
                u.current_spelling_input_value: '',
                u.spelling_list: [],
                u.waiting_message: None,
                u.saved_spelling_fields: [],
                u.saved_spelling_values: []
            },
            machine_parameters: {
                u.submit_done: False,
                u.reset_alarm_enabled: False,
                u.submit_alarm_enabled: False,
                u.possible_next_action: None,
                u.warning_message: ''
            }
        },
        test_case_message: {
            entities: [
                {
                    entity: input_field,
                    value: 'city'
                }
            ],
            intent: {
                name: explain_field,
                confidence: 1
            },
            text: 'What is city?'
        },
        result_expected: '{sorry} the field {city} is not present in this form. The fields of this form are the following: {fields}'
    },
    {
        message_id: "047",
        test_form_number: 1,
        initial_state: {
            spelling_state: {
                u.close_prompt_enabled: False,
                u.current_spelling_input_value: '',
                u.spelling_list: [],
                u.waiting_message: None,
                u.saved_spelling_fields: [],
                u.saved_spelling_values: []
            },
            machine_parameters: {
                u.submit_done: False,
                u.reset_alarm_enabled: False,
                u.submit_alarm_enabled: False,
                u.possible_next_action: None,
                u.warning_message: ''
            }
        },
        test_case_message: {
            entities: [
                {
                    entity: input_field,
                    value: 'email'
                }
            ],
            intent: {
                name: verify_presence_field,
                confidence: 1
            },
            text: 'is email present in the form?'
        },
        result_expected: 'The field {email} is not present but you have these alternatives {email address}'
    },
    {
        message_id: "048",
        test_form_number: 1,
        initial_state: {
            u.slots: [
                {
                    u.slot_name: mark,
                    u.slot_value: None
                },
                {
                    u.slot_name: password,
                    u.slot_value: None
                }
            ],
            spelling_state: {
                u.close_prompt_enabled: False,
                u.current_spelling_input_value: '',
                u.spelling_list: [],
                u.waiting_message: None,
                u.saved_spelling_fields: [],
                u.saved_spelling_values: []
            },
            machine_parameters: {
                u.submit_done: False,
                u.reset_alarm_enabled: False,
                u.submit_alarm_enabled: False,
                u.possible_next_action: None,
                u.warning_message: ''
            }
        },
        test_case_message: {
            entities: [
                {
                    entity: input_field,
                    value: password
                }
            ],
            intent: {
                name: verify_presence_field,
                confidence: 1
            },
            text: 'is the field password present in this form?'
        },
        result_expected: 'The field {password} is present'
    },
    {
        message_id: "049",
        test_form_number: 1,
        initial_state: {},
        test_case_message: {
            entities: [
                {
                    entity: input_field,
                    value: 'suggestions'
                }
            ],
            intent: {
                name: verify_presence_field,
                confidence: 1
            },
            text: 'is there the field suggestions in the form?'
        },
        result_expected: 'The field {suggestions} is not present {sorry}'
    },
    {
        message_id: "050",
        test_form_number: 1,
        initial_state: {
            u.slots: [
                {
                    u.slot_name: first_name,
                    u.slot_value: "madiba"
                },
                {
                    u.slot_name: mark,
                    u.slot_value: "23"
                },
                {
                    u.slot_name: password,
                    u.slot_value: None
                },
                {
                    u.slot_name: email_address,
                    u.slot_value: None
                }
            ]
        },
        test_case_message: {
            entities: [
                {
                    entity: input_field,
                    value: password
                },
                {
                    entity: input_value,
                    value: 'p@s%&word'
                }
            ],
            intent: {
                name: complete_field,
                confidence: 1
            },
            text: 'the password is p@s%&word'
        },
        result_expected: 'This field is required'
    },
    {
        message_id: "051",
        test_form_number: 1,
        initial_state: {
            u.slots: [
                {
                    u.slot_name: first_name,
                    u.slot_value: "madiba"
                },
                {
                    u.slot_name: mark,
                    u.slot_value: None
                },
                {
                    u.slot_name: password,
                    u.slot_value: None
                },
                {
                    u.slot_name: email_address,
                    u.slot_value: None
                }
            ]
        },
        test_case_message: {
            entities: [
                {
                    entity: input_field,
                    value: mark
                },
                {
                    entity: input_value,
                    value: '25'
                }
            ],
            intent: {
                name: complete_field,
                confidence: 1
            },
            text: 'my mark is 25'
        },
        result_expected: 'This field is optional'
    },
    {
        message_id: "052",
        test_form_number: 1,
        initial_state: {
            spelling_state: {
                u.close_prompt_enabled: True,
                u.current_spelling_input_value: 'elis',
                u.spelling_list: [first_name],
                u.waiting_message: None,
                u.saved_spelling_fields: [],
                u.saved_spelling_values: []
            },
            machine_parameters: {
                u.submit_done: False,
                u.reset_alarm_enabled: False,
                u.submit_alarm_enabled: False,
                u.possible_next_action: spelling,
                u.warning_message: ''
            }
        },
        test_case_message: {
            entities: [
                {
                    entity: input_value,
                    value: 'a'
                }
            ],
            intent: {
                name: spelling,
                confidence: 1
            },
            text: 'a'
        },
        result_expected: '{please} {insert} the {next} character, remeber that you can use the expr SPACE for the blank and the expr TERMINATE to {conclude} the spelling'
    },
    {
        message_id: "053",
        test_form_number: 1,
        initial_state: {
            spelling_state: {
                u.close_prompt_enabled: True,
                u.current_spelling_input_value: 'elisa',
                u.spelling_list: [first_name],
                u.waiting_message: give_all_remaining_fields,
                u.spelling_interrupted: True,
                u.saved_spelling_fields: [],
                u.saved_spelling_values: []
            },
            machine_parameters: {
                u.submit_done: False,
                u.reset_alarm_enabled: False,
                u.submit_alarm_enabled: False,
                u.possible_next_action: None,
                u.warning_message: ''
            }
        },
        test_case_message: {
            entities: [],
            intent: {
                name: give_all_remaining_fields,
                confidence: 1
            },
            text: 'what are the remaining fields'
        },
        result_expected: 'Please i would like to have a clear answer. Would you like to save the state of the field that you started spelling. In case of negative response, …'
    },
    {
        message_id: "054",
        test_form_number: 1,
        initial_state: {
            spelling_state: {
                u.close_prompt_enabled: True,
                u.current_spelling_input_value: 'elisa',
                u.spelling_list: [first_name],
                u.waiting_message: None,
                u.saved_spelling_fields: [],
                u.saved_spelling_values: []
            },
            machine_parameters: {
                u.submit_done: False,
                u.reset_alarm_enabled: False,
                u.submit_alarm_enabled: False,
                u.possible_next_action: None,
                u.warning_message: ''
            }
        },
        test_case_message: {
            entities: [],
            intent: {
                name: repeat_required_fields,
                confidence: 1
            },
            text: 'which are the required fields?'
        },
        result_expected: 'Do you want to save the state of the field you started spelling? In case of negative response, that input will simply be canceled'
    },
    {
        message_id: "055",
        test_form_number: 1,
        initial_state: {},
        test_case_message: {
            entities: [
                {
                    entity: input_field,
                    value: mark
                },
                {
                    entity: input_value,
                    value: '  '
                },
                {
                    entity: input_field,
                    value: password
                },
                {
                    entity: input_value,
                    value: 'p@sswRD'
                }
            ],
            intent: {
                name: complete_field,
                confidence: 1
            },
            text: 'my mark is   and my password is p@sswRD'
        },
        result_expected: 'The value you inserted only contains the blanks, and so it is not valid. Your input should contain at least one character different from the blank'
    },
    {
        message_id: "056",
        test_form_number: 1,
        initial_state: {
            u.slots: [
                {
                    u.slot_name: first_name,
                    u.slot_value: None
                },
                {
                    u.slot_name: mark,
                    u.slot_value: None
                }
            ]
        },
        test_case_message: {
            entities: [
                {
                    entity: input_field,
                    value: email_address
                },
                {
                    entity: input_value,
                    value: 'emaddress.cm'
                }
            ],
            intent: {
                name: complete_field,
                confidence: 1
            },
            text: 'my email address is emaddress.cm'
        },
        result_expected: 'The email should contain the character <{@}>'
    },
    {
        message_id: "057",
        test_form_number: 1,
        initial_state: {},
        test_case_message: {
            entities: [
                {
                    entity: input_field,
                    value: email_address
                },
                {
                    entity: input_value,
                    value: 'emai@addres@mail.it'
                }
            ],
            intent: {
                name: complete_field,
                confidence: 1
            },
            text: 'the email address is emai@addres@mail.it'
        },
        result_expected: 'The email should contain only one character <{@}>'
    },
    {
        message_id: "058",
        test_form_number: 1,
        initial_state: {},
        test_case_message: {
            entities: [
                {
                    entity: input_field,
                    value: email_address
                },
                {
                    entity: input_value,
                    value: '@email.it'
                }
            ],
            intent: {
                name: complete_field,
                confidence: 1
            },
            text: 'my email address is @email.it'
        },
        result_expected: 'The email should not start with the character <{@}>'
    },
    {
        message_id: "059",
        test_form_number: 1,
        initial_state: {},
        test_case_message: {
            entities: [
                {
                    entity: input_field,
                    value: email_address
                },
                {
                    entity: input_value,
                    value: 'em_address@'
                }
            ],
            intent: {
                name: complete_field,
                confidence: 1
            },
            text: 'the email address is em_address@'
        },
        result_expected: 'The email should not end with the character <{@}>'
    },
    {
        message_id: "060",
        test_form_number: 2,
        initial_state: {
            u.slots: [
                {
                    u.slot_name: phone_number,
                    u.slot_value: None
                },
                {
                    u.slot_name: number_persons,
                    u.slot_value: None
                },
                {
                    u.slot_name: birthday,
                    u.slot_value: None
                },
                {
                    u.slot_name: arrival_time,
                    u.slot_value: None
                }
            ]
        },
        test_case_message: {
            entities: [
                {
                    entity: input_field,
                    value: number_persons
                },
                {
                    entity: input_value,
                    value: 'three'
                }
            ],
            intent: {
                name: complete_field,
                confidence: 1
            },
            text: 'the number of persons is three'
        },
        result_expected: '{sorry} the value {three} is not an integer, {please} {insert} a valid value.'
    },
    {
        message_id: "061",
        test_form_number: 1,
        initial_state: {},
        test_case_message: {
            entities: [
                {
                    entity: input_field,
                    value: password
                },
                {
                    entity: input_value,
                    value: 'pass'
                }
            ],
            intent: {
                name: complete_field,
                confidence: 1
            },
            text: 'the password is pass'
        },
        result_expected: 'The password you proposed is too short. The minimum number of characters accepted is {length}'
    },
    {
        message_id: "062",
        test_form_number: 1,
        initial_state: {},
        test_case_message: {
            entities: [
                {
                    entity: input_field,
                    value: password
                },
                {
                    entity: input_value,
                    value: 'pass/worf'
                }
            ],
            intent: {
                name: complete_field,
                confidence: 1
            },
            text: 'the password is pass/worf'
        },
        result_expected: 'A non acceptable character have been inserted in the passsword. The only accepted special characters are the following {characters}'
    },
    {
        message_id: "063",
        test_form_number: 2,
        initial_state: {},
        test_case_message: {
            entities: [
                {
                    entity: input_field,
                    value: phone_number
                },
                {
                    entity: input_value,
                    value: '00+3935897654'
                }
            ],
            intent: {
                name: complete_field,
                confidence: 1
            },
            text: 'the phone number is 00+3935897654'
        },
        result_expected: 'The character <{+}> could only be at the beginning of the number'
    },
    {
        message_id: "064",
        test_form_number: 2,
        initial_state: {},
        test_case_message: {
            entities: [
                {
                    entity: input_field,
                    value: phone_number
                },
                {
                    entity: input_value,
                    value: '+39+3598456790'
                }
            ],
            intent: {
                name: complete_field,
                confidence: 1
            },
            text: 'the phone number is +39+3598456790'
        },
        result_expected: 'A telephone number should not contain the character < {plus_sign} > several times'
    },
    {
        message_id: "065",
        test_form_number: 1,
        initial_state: {},
        test_case_message: {
            entities: [
                {
                    entity: input_field,
                    value: phone_number
                },
                {
                    entity: input_value,
                    value: '+1'
                }
            ],
            intent: {
                name: complete_field,
                confidence: 1
            },
            text: 'the phone number is +1'
        },
        result_expected: '{sorry} the value {+1} is not valid, {please} {insert} a valid phone number'
    },
    {
        message_id: "066",
        test_form_number: 2,
        initial_state: {},
        test_case_message: {
            entities: [
                {
                    entity: input_field,
                    value: arrival_time
                },
                {
                    entity: input_value,
                    value: 'am 7'
                }
            ],
            intent: {
                name: complete_field,
                confidence: 1
            },
            text: 'the arrival time is am 7'
        },
        result_expected: 'The time you inserted is not valid. …'
    },
    {
        message_id: "067",
        test_form_number: 2,
        initial_state: {
            u.slots: [
                {
                    u.slot_name: birthday,
                    u.slot_value: None
                }
            ]
        },
        test_case_message: {
            entities: [
                {
                    entity: input_field,
                    value: birthday
                },
                {
                    entity: input_value,
                    value: '12 apr 2010'
                }
            ],
            intent: {
                name: complete_field,
                confidence: 1
            },
            text: 'the birthday date is 12 apr 2010'
        },
        result_expected: 'The date inserted is not valid …'
    },
    {
        message_id: "068",
        test_form_number: 2,
        initial_state: {},
        test_case_message: {
            entities: [
                {
                    entity: input_field,
                    value: birthday
                },
                {
                    entity: input_value,
                    value: '32/02/2012'
                }
            ],
            intent: {
                name: complete_field,
                confidence: 1
            },
            text: 'the birthday is 32/02/2012'
        },
        result_expected: 'The day you inserted is out of range'
    },
    {
        message_id: "069",
        test_form_number: 2,
        initial_state: {
            u.slots: [
                {
                    u.slot_name: phone_number,
                    u.slot_value: None
                }
            ]
        },
        test_case_message: {
            entities: [
                {
                    entity: input_field,
                    value: birthday
                },
                {
                    entity: input_value,
                    value: '21 14 2018'
                }
            ],
            intent: {
                name: complete_field,
                confidence: 1
            },
            text: 'the birthday is 21 14 2018'
        },
        result_expected: 'The month you inserted is out of range'
    },
    {
        message_id: "070",
        test_form_number: 2,
        initial_state: {},
        test_case_message: {
            entities: [
                {
                    entity: input_field,
                    value: birthday
                },
                {
                    entity: input_value,
                    value: '20/03/0000'
                }
            ],
            intent: {
                name: complete_field,
                confidence: 1
            },
            text: 'the birthday is 20/03/0000'
        },
        result_expected: 'The year you inserted is out of range, the minimum is {min_value} and the maximum is {max_value}'
    },
    {
        message_id: "071",
        test_form_number: 2,
        initial_state: {},
        test_case_message: {
            entities: [
                {
                    entity: input_value,
                    value: '25'
                },
                {
                    entity: input_field,
                    value: arrival_time
                }
            ],
            intent: {
                name: complete_field,
                confidence: 1
            },
            text: '25 is the arrival time'
        },
        result_expected: 'The hour is out of range'
    },
    {
        message_id: "072",
        test_form_number: 2,
        initial_state: {},
        test_case_message: {
            entities: [
                {
                    entity: input_value,
                    value: '07:80'
                },
                {
                    entity: input_field,
                    value: arrival_time
                }
            ],
            intent: {
                name: complete_field,
                confidence: 1
            },
            text: '07:80 is the arrival time'
        },
        result_expected: 'The minutes are out of range'
    },
    {
        message_id: "073",
        test_form_number: 1,
        initial_state: {},
        test_case_message: {
            entities: [
                {
                    entity: input_value,
                    value: 'harry.mayson@gmailcm'
                },
                {
                    entity: input_field,
                    value: email_address
                }
            ],
            intent: {
                name: complete_field,
                confidence: 1
            },
            text: 'harry.mayson@gmailcm is the email address'
        },
        result_expected: 'There should be at least one character <{dot_sign}> after the character <{at_sign}>'
    },
    {
        message_id: "074",
        test_form_number: 1,
        initial_state: {
            u.slots: [
                {
                    u.slot_name: first_name,
                    u.slot_value: None
                }
            ],
            spelling_state: {
                u.close_prompt_enabled: False,
                u.current_spelling_input_value: '',
                u.spelling_list: [],
                u.waiting_message: None,
                u.saved_spelling_fields: [],
                u.saved_spelling_values: []
            },
            machine_parameters: {
                u.submit_done: False,
                u.reset_alarm_enabled: False,
                u.submit_alarm_enabled: False,
                u.possible_next_action: None,
                u.warning_message: ''
            }
        },
        test_case_message: {
            entities: [
                {
                    entity: input_value,
                    value: 'harry@gmailcm'
                },
                {
                    entity: input_field,
                    value: email_address
                }
            ],
            intent: {
                name: complete_field,
                confidence: 1
            },
            text: 'harry@gmailcm is my email address'
        },
        result_expected: 'The email should contain the character <{dot_sign}>'
    },

    {
        message_id: "075",
        test_form_number: 1,
        initial_state: {
            u.slots: [
                {
                    u.slot_name: first_name,
                    u.slot_value: None
                }
            ],
            spelling_state: {
                u.close_prompt_enabled: False,
                u.current_spelling_input_value: '',
                u.spelling_list: [],
                u.waiting_message: None,
                u.saved_spelling_fields: [],
                u.saved_spelling_values: []
            },
            machine_parameters: {
                u.submit_done: False,
                u.reset_alarm_enabled: False,
                u.submit_alarm_enabled: False,
                u.possible_next_action: None,
                u.warning_message: ''
            }
        },
        test_case_message: {
            entities: [
                {
                    entity: input_value,
                    value: 'harry.potter@gmailcm'
                },
                {
                    entity: input_field,
                    value: email_address
                }
            ],
            intent: {
                name: complete_field,
                confidence: 1
            },
            text: 'harry.potter@gmailcm is my email address'
        },
        result_expected: 'There should be at least one character <{dot_sign}> after the character <{at_sign}>'
    },
    {
        message_id: "076",
        test_form_number: 3,
        initial_state: {
            u.slots: [
                {
                    u.slot_name: car,
                    u.slot_value: None
                },
                {
                    u.slot_name: gender,
                    u.slot_value: None
                },
                {
                    u.slot_name: electronic_devices,
                    u.slot_value: None
                },
                {
                    u.slot_name: message,
                    u.slot_value: None
                }
            ],
            spelling_state: {
                u.close_prompt_enabled: False,
                u.current_spelling_input_value: '',
                u.spelling_list: [],
                u.waiting_message: None,
                u.saved_spelling_fields: [],
                u.saved_spelling_values: []
            },
            machine_parameters: {
                u.submit_done: False,
                u.reset_alarm_enabled: False,
                u.submit_alarm_enabled: False,
                u.possible_next_action: None,
                u.warning_message: ''
            }
        },
        test_case_message: {
            entities: [],
            intent: {
                name: complete_field,
                confidence: 1
            },
            text: 'I want the required fields'
        },
        result_expected: 'There is one required field in this form which is {gender}'
    },
    {
        message_id: "077",
        test_form_number: 2,
        initial_state: {
            u.slots: [
                {
                    u.slot_name: phone_number,
                    u.slot_value: None
                },
                {
                    u.slot_name: number_persons,
                    u.slot_value: None
                },
                {
                    u.slot_name: birthday,
                    u.slot_value: None
                },
                {
                    u.slot_name: arrival_time,
                    u.slot_value: None
                }
            ],
            spelling_state: {
                u.close_prompt_enabled: False,
                u.current_spelling_input_value: '',
                u.spelling_list: [],
                u.waiting_message: None,
                u.saved_spelling_fields: [],
                u.saved_spelling_values: []
            },
            machine_parameters: {
                u.submit_done: False,
                u.reset_alarm_enabled: False,
                u.submit_alarm_enabled: False,
                u.possible_next_action: None,
                u.warning_message: ''
            }
        },
        test_case_message: {
            entities: [],
            intent: {
                name: repeat_required_fields,
                confidence: 1
            },
            text: 'which are the required fields?'
        },
        result_expected: 'There is no required field in this form'
    },
    {
        message_id: "078",
        test_form_number: 1,
        initial_state: {
            u.slots: [
                {
                    u.slot_name: first_name,
                    u.slot_value: 'Elena'
                },
                {
                    u.slot_name: last_name,
                    u.slot_value: None
                },
                {
                    u.slot_name: mark,
                    u.slot_value: '28'
                },
                {
                    u.slot_name: password,
                    u.slot_value: None
                },
                {
                    u.slot_name: email_address,
                    u.slot_value: 'silver@stone.com'
                }
            ],
            spelling_state: {
                u.close_prompt_enabled: False,
                u.current_spelling_input_value: '',
                u.spelling_list: [],
                u.waiting_message: None,
                u.saved_spelling_fields: [],
                u.saved_spelling_values: []
            },
            machine_parameters: {
                u.submit_done: False,
                u.reset_alarm_enabled: False,
                u.submit_alarm_enabled: False,
                u.possible_next_action: None,
                u.warning_message: ''
            }
        },
        test_case_message: {
            entities: [],
            intent: {
                name: give_remaining_required_fields,
                confidence: 1
            },
            text: 'Can i have the remaining the remaining required fields?'
        },
        result_expected: 'There is no required field remaining'
    },
    {
        message_id: "079",
        test_form_number: 1,
        initial_state: {
            u.slots: [
                {
                    u.slot_name: first_name,
                    u.slot_value: None
                },
                {
                    u.slot_name: last_name,
                    u.slot_value: None
                },
                {
                    u.slot_name: mark,
                    u.slot_value: '27'
                },
                {
                    u.slot_name: password,
                    u.slot_value: 'pass04real11'
                },
                {
                    u.slot_name: email_address,
                    u.slot_value: 'em_ail@ego.it'
                }
            ],
            spelling_state: {
                u.close_prompt_enabled: False,
                u.current_spelling_input_value: '',
                u.spelling_list: [],
                u.waiting_message: None,
                u.saved_spelling_fields: [],
                u.saved_spelling_values: []
            },
            machine_parameters: {
                u.submit_done: False,
                u.reset_alarm_enabled: False,
                u.submit_alarm_enabled: False,
                u.possible_next_action: None,
                u.warning_message: ''
            }
        },
        test_case_message: {
            entities: [],
            intent: {
                name: give_remaining_required_fields,
                confidence: 1
            },
            text: 'which are the remaining required fields?'
        },
        result_expected: 'The only required field that remains is {first name}'
    },
    {
        message_id: "080",
        test_form_number: 1,
        initial_state: {
            u.slots: [
                {
                    u.slot_name: first_name,
                    u.slot_value: 'elvis'
                },
                {
                    u.slot_name: last_name,
                    u.slot_value: 'jones'
                },
                {
                    u.slot_name: mark,
                    u.slot_value: '24'
                },
                {
                    u.slot_name: password,
                    u.slot_value: 'my_pass0wr0'
                },
                {
                    u.slot_name: email_address,
                    u.slot_value: 'email@mail.it'
                }
            ],
            spelling_state: {
                u.close_prompt_enabled: False,
                u.current_spelling_input_value: '',
                u.spelling_list: [],
                u.waiting_message: None,
                u.saved_spelling_fields: [],
                u.saved_spelling_values: []
            },
            machine_parameters: {
                u.submit_done: False,
                u.reset_alarm_enabled: False,
                u.submit_alarm_enabled: False,
                u.possible_next_action: None,
                u.warning_message: ''
            }
        },
        test_case_message: {
            entities: [],
            intent: {
                name: give_all_remaining_fields,
                confidence: 1
            },
            text: 'i want the remaining fields'
        },
        result_expected: 'There is no field remaining'
    },
    {
        message_id: "081",
        test_form_number: 1,
        initial_state: {
            u.slots: [
                {
                    u.slot_name: first_name,
                    u.slot_value: 'donald'
                },
                {
                    u.slot_name: last_name,
                    u.slot_value: 'duck'
                },
                {
                    u.slot_name: mark,
                    u.slot_value: '26'
                },
                {
                    u.slot_name: password,
                    u.slot_value: 'platform_password'
                },
                {
                    u.slot_name: email_address,
                    u.slot_value: None
                }
            ],
            spelling_state: {
                u.close_prompt_enabled: False,
                u.current_spelling_input_value: '',
                u.spelling_list: [],
                u.waiting_message: None,
                u.saved_spelling_fields: [],
                u.saved_spelling_values: []
            },
            machine_parameters: {
                u.submit_done: False,
                u.reset_alarm_enabled: False,
                u.submit_alarm_enabled: False,
                u.possible_next_action: None,
                u.warning_message: ''
            }
        },
        test_case_message: {
            entities: [],
            intent: {
                name: give_all_remaining_fields,
                confidence: 1
            },
            text: 'what are the remaining fields?'
        },
        result_expected: 'There is one field remaining and it is {email address}'
    },
    {
        message_id: "082",
        test_form_number: 1,
        initial_state: {
            u.slots: [
                {
                    u.slot_name: first_name,
                    u.slot_value: 'abdel'
                },
                {
                    u.slot_name: last_name,
                    u.slot_value: None
                },
                {
                    u.slot_name: mark,
                    u.slot_value: None
                },
                {
                    u.slot_name: email_address,
                    u.slot_value: None
                }
            ],
            spelling_state: {
                u.close_prompt_enabled: False,
                u.current_spelling_input_value: '',
                u.spelling_list: [],
                u.waiting_message: None,
                u.saved_spelling_fields: [],
                u.saved_spelling_values: []
            },
            machine_parameters: {
                u.submit_done: False,
                u.reset_alarm_enabled: False,
                u.submit_alarm_enabled: False,
                u.possible_next_action: None,
                u.warning_message: ''
            }
        },
        test_case_message: {
            entities: [],
            intent: {
                name: submit_form,
                confidence: 1
            },
            text: 'submit'
        },
        result_expected: '...You should complete the field {email address}.'
    },
    {
        message_id: "083",
        test_form_number: 1,
        initial_state: {
            u.slots: [
                {
                    u.slot_name: first_name,
                    u.slot_value: None
                }
            ],
            spelling_state: {
                u.close_prompt_enabled: False,
                u.current_spelling_input_value: '',
                u.spelling_list: [],
                u.waiting_message: None,
                u.saved_spelling_fields: [],
                u.saved_spelling_values: []
            },
            machine_parameters: {
                u.submit_done: False,
                u.reset_alarm_enabled: False,
                u.submit_alarm_enabled: False,
                u.possible_next_action: None,
                u.warning_message: ''
            }
        },
        test_case_message: {
            entities: [
                {
                    entity: input_value,
                    value: '.harry@gmailcm'
                },
                {
                    entity: input_field,
                    value: email_address
                }
            ],
            intent: {
                name: complete_field,
                confidence: 1
            },
            text: '.harry@gmailcm is my email address'
        },
        result_expected: 'The email should not start with the character < {dot_sign} >'
    },
    {
        message_id: "084",
        test_form_number: 1,
        initial_state: {
            u.slots: [
                {
                    u.slot_name: first_name,
                    u.slot_value: None
                }
            ],
            spelling_state: {
                u.close_prompt_enabled: False,
                u.current_spelling_input_value: '',
                u.spelling_list: [],
                u.waiting_message: None,
                u.saved_spelling_fields: [],
                u.saved_spelling_values: []
            },
            machine_parameters: {
                u.submit_done: False,
                u.reset_alarm_enabled: False,
                u.submit_alarm_enabled: False,
                u.possible_next_action: None,
                u.warning_message: ''
            }
        },
        test_case_message: {
            entities: [
                {
                    entity: input_value,
                    value: 'harry@gmailcm.'
                },
                {
                    entity: input_field,
                    value: email_address
                }
            ],
            intent: {
                name: complete_field,
                confidence: 1
            },
            text: 'harry@gmailcm. is my email address'
        },
        result_expected: 'The email should not end with the character < {dot_sign} >'
    },
    
    {
        message_id: "085",
        test_form_number: 1,
        initial_state: {
            machine_parameters: {
                u.submit_alarm_enabled: True,
                u.possible_next_action: submit_form,
                u.submit_done: False
            }
        },
        test_case_message: {
            entities: [],
            intent: {
                name: affirm,
                confidence: 1
            },
            text: 'yes'
        },
        result_expected: '{good} you have been moved to the page with title {title}'
    },
    {
        message_id: "086",
        test_form_number: 2,
        initial_state: {
            spelling_state: {
                u.close_prompt_enabled: False,
                u.current_spelling_input_value: '',
                u.spelling_list: [],
                u.waiting_message: None,
                u.saved_spelling_fields: [],
                u.saved_spelling_values: []
            },
            machine_parameters: {
                u.submit_done: False,
                u.reset_alarm_enabled: False,
                u.submit_alarm_enabled: True,
                u.possible_next_action: None,
                u.warning_message: ''
            }
        },
        test_case_message: {
            entities: [],
            intent: {
                name: submit_form,
                confidence: 1
            },
            text: 'may i submit the form?'
        },
        result_expected: 'Submission done'
    }
]

functional_test_cases = [
    {
        message_id: "000",
        test_form_number: 1,
        initial_state: {
            u.slots: [
                {
                    u.slot_name: first_name,
                    u.slot_value: None
                },
                {
                    u.slot_name: mark,
                    u.slot_value: None
                },
                {
                    u.slot_name: password,
                    u.slot_value: None
                },
                {
                    u.slot_name: email_address,
                    u.slot_value: None
                }
            ]
        },
        test_case_message: {
            entities: [
                {
                    entity: input_field,
                    value: email_address
                },
                {
                    entity: input_value,
                    value: 'alice@mail.it'
                }
            ],
            intent: {
                name: complete_field,
                confidence: 1
            },
            text: 'the email address is alice@mail.it'
        },
        result_expected: 'The email address becomes alice@mail.it and next field is first name'
    },
    {
        message_id: "001",
        test_form_number: 1,
        initial_state: {
            u.slots: [
                {
                    u.slot_name: first_name,
                    u.slot_value: "bob"
                },
                {
                    u.slot_name: mark,
                    u.slot_value: "25,85"
                }
            ],
            machine_parameters: {
                u.reset_alarm_enabled: True,
                u.possible_next_action: reset_all_fields
            }
        },
        test_case_message: {
            entities: [],
            intent: {
                    name: affirm,
                    confidence: 1
            }   ,
            text: 'yes'
        },
        result_expected: 'all the fields are reset (value=None) and the next field is first name'
    },
    {
        message_id: "002",
        test_form_number: 1,
        initial_state: {
            u.slots: [
                {
                    u.slot_name: password,
                    u.slot_value: "p088w0r0"
                },
                {
                    u.slot_name: first_name,
                    u.slot_value: "robert"
                },
                {
                    u.slot_name: email_address,
                    u.slot_value: "alice@bob.it"
                }
            ],
            spelling_state: {
                u.close_prompt_enabled: False,
                u.current_spelling_input_value: '',
                u.spelling_list: [],
                u.waiting_message: None,
                u.saved_spelling_fields: [],
                u.saved_spelling_values: []
            },
            machine_parameters: {
                u.submit_alarm_enabled: True
            }
        },
        test_case_message: {
            entities: [],
            intent: {
                name: deny,
                confidence: 1
            },
            text: 'no'
        },
        result_expected: 'submit alarm is disabled, state 05'
    },
    {
        message_id: "003",
        test_form_number: 1,
        initial_state: {
            u.slots: [
                {
                    u.slot_name: first_name,
                    u.slot_value: "lucie"
                },
                {
                    u.slot_name: email_address,
                    u.slot_value: "dear_alice@bob.it"
                }
            ],
            spelling_state: {
                u.close_prompt_enabled: False,
                u.current_spelling_input_value: '',
                u.spelling_list: [],
                u.waiting_message: None,
                u.saved_spelling_fields: [],
                u.saved_spelling_values: []
            },
            machine_parameters: {
                u.submit_done: False,
                u.reset_alarm_enabled: False,
                u.submit_alarm_enabled: False,
                u.possible_next_action: None,
                u.warning_message: ''
            }
        },
        test_case_message: {
            entities: [],
            intent: {
                name: submit_form,
                confidence: 1
            },
            text: 'submit'
        },
        result_expected: 'The submit alarm will be enabledand we have to confirm the action'
    },
    {
        message_id: "004",
        test_form_number: 1,
        initial_state: {
            u.slots: [
                {
                    u.slot_name: password,
                    u.slot_value: "p088w0r0"
                },
                {
                    u.slot_name: email_address,
                    u.slot_value: "alice@bob.it"
                },
                {
                    u.slot_name: mark,
                    u.slot_value: "27,2"
                }
            ]
        },
        test_case_message: {
            entities: [],
            intent: {
                name: reset_all_fields,
                confidence: 1
            },
            text: 'reset'
        },
        result_expected: 'The reset alarm is enabled and we have to confirm the action'
    },
    {
        message_id: "005",
        test_form_number: 1,
        initial_state: {
            u.slots: [
                {
                    u.slot_name: first_name,
                    u.slot_value: None
                },
                {
                    u.slot_name: last_name,
                    u.slot_value: None
                },
                {
                    u.slot_name: mark,
                    u.slot_value: None
                },
                {
                    u.slot_name: email_address,
                    u.slot_value: None
                },
                {
                    u.slot_name: password,
                    u.slot_value: None
                }
            ],
            spelling_state: {
                u.close_prompt_enabled: True,
                u.current_spelling_input_value: 'adama',
                u.spelling_list: [last_name]
            },
            machine_parameters: {
                u.possible_next_action: spelling
            }
        },
        test_case_message: {
            entities: [
                {
                    entity: 'spelling',
                    value: 'terminate'
                }
            ],
            intent: {
                name: spelling,
                confidence: 1
            },
            text: 'terminate'
        },
        result_expected: 'The value adama is set for the last name, the next field is mark'
    },
    {
        message_id: "006",
        test_form_number: 1,
        initial_state: {
            u.slots: [
                {
                    u.slot_name: mark,
                    u.slot_value: "28"
                },
                {
                    u.slot_name: first_name,
                    u.slot_value: None
                }
            ],
            spelling_state: {
                u.close_prompt_enabled: False,
                u.current_spelling_input_value: '',
                u.spelling_list: [],
                u.waiting_message: None,
                u.saved_spelling_fields: [],
                u.saved_spelling_values: []
            },
            machine_parameters: {
                u.submit_done: False,
                u.reset_alarm_enabled: False,
                u.submit_alarm_enabled: False,
                u.possible_next_action: None,
                u.warning_message: ''
            }
        },
        test_case_message: {
            entities: [
                {
                    entity: input_field,
                    value: mark
                },
                {
                    entity: input_value,
                    value: '30'
                }
            ],
            intent: {
                name: modify_value_field,
                confidence: 1
            },
            text: 'I want to modify the mark putting the value 30 instead'
        },
        result_expected: 'The mark becomes 30, the next field is password'
    },
    {
        message_id: "007",
        test_form_number: 2,
        initial_state: {
            u.slots: [
                {
                    u.slot_name: number_persons,
                    u.slot_value: "6"
                }
            ]
        },
        test_case_message: {
            entities: [
                {
                    entity: input_value,
                    value: '22/02/2000'
                }
            ],
            intent: {
                name: complete_field,
                confidence: 1
            },
            text: '22/02/2000'
        },
        result_expected: 'The birthday becomes 22/02/2000, the next field is arrival time'
    },
    {
        message_id: "008",
        test_form_number: 2,
        initial_state: {
            u.slots: [
                {
                    u.slot_name: number_persons,
                    u.slot_value: "2"
                },
                {
                    u.slot_name: arrival_time,
                    u.slot_value: "07:00"
                },
                {
                    u.slot_name: phone_number,
                    u.slot_value: "00237651322430"
                },
                {
                    u.slot_name: birthday,
                    u.slot_value: None
                }
            ]
        },
        test_case_message: {
            entities: [
                {
                    entity: input_field,
                    value: arrival_time
                }
            ],
            intent: {
                name: repeat_value_field,
                confidence: 1
            },
            text: 'Could you please repeat the arrival time for me?'
        },
        result_expected: 'Gives the value 07:00 of the arrival time, the next field is birthday'
    },
    {
        message_id: "009",
        test_form_number: 2,
        initial_state: {},
        test_case_message: {
            entities: [],
            intent: {
                name: repeat_all_fields,
                confidence: 1
            },
            text: 'which are the fields of this form?'
        },
        result_expected: 'lists the five fields from phone number to card expiration date, the next field is birthday'
    },
    {
        message_id: "010",
        test_form_number: 2,
        initial_state: {},
        test_case_message: {
            entities: [],
            intent: {
                name: repeat_required_fields,
                confidence: 1
            },
            text: 'which are the required fields of this form?'
        },
        result_expected: 'lists zero field, the next field is birthday'
    },
    {
        message_id: "011",
        test_form_number: 2,
        initial_state: {},
        test_case_message: {
            entities: [],
            intent: {
                name: repeat_optional_fields,
                confidence: 1
            },
            text: 'which are the optional fields?'
        },
        result_expected: 'Gives the list of all the fields, they are all optimal. The next field is birthday'
    },
    {
        message_id: "012",
        test_form_number: 2,
        initial_state: {
            u.slots: [
                {
                    u.slot_name: phone_number,
                    u.slot_value: "+223615342345"
                },
                {
                    u.slot_name: number_persons,
                    u.slot_value: None
                },
                {
                    u.slot_name: birthday,
                    u.slot_value: "31/05/1990"
                },
                {
                    u.slot_name: arrival_time,
                    u.slot_value: None
                }
            ],
        },
        test_case_message: {
            entities: [],
            intent: {
                name: give_all_remaining_fields,
                confidence: 1
            },
            text: 'which are the fields still to be completed?'
        },
        result_expected: 'Number of persons, arrival time. The next field is number of persons'
    },
    {
        message_id: "013",
        test_form_number: 2,
        initial_state: {},
        test_case_message: {
            entities: [],
            intent: {
                name: give_remaining_required_fields,
                confidence: 1
            },
            text: 'are there required remaining fields?'
        },
        result_expected: 'No remaining required field. The next field is number of persons'
    },
    {
        message_id: "014",
        test_form_number: 2,
        initial_state: {
            u.slots: [
                {
                    u.slot_name: phone_number,
                    u.slot_value: None
                }
            ]
        },
        test_case_message: {
            entities: [],
            intent: {
                name: give_remaining_optional_fields,
                confidence: 1
            },
            text: 'which are the remaining optional fields?'
        },
        result_expected: 'Phone number, number of persons, arrival time'
    },
    {
        message_id: "015",
        test_form_number: 3,
        initial_state: {},
        test_case_message: {
            entities: [
                {
                    entity: input_value,
                    value: 'audi'
                }
            ],
            intent: {
                name: complete_field,
                confidence: 1
            },
            text: 'audi'
        },
        result_expected: 'Car has value audi. The next field is gender'
    },
    {
        message_id: "016",
        test_form_number: 3,
        initial_state: {},
        test_case_message: {
            entities: [],
            intent: {
                name: skip_field,
                confidence: 1
            },
            text: 'skip'
        },
        result_expected: 'The next field is electronic devices'
    },
    {
        message_id: "017",
        test_form_number: 3,
        initial_state: {
            u.slots: [
                {
                    u.slot_name: gender,
                    u.slot_value: "male"
                }
            ]
        },
        test_case_message: {
            entities: [
                {
                    entity: input_field,
                    value: 'family name'
                }
            ],
            intent: {
                name: verify_presence_field,
                confidence: 1
            },
            text: 'is the field family name present in this form?'
        },
        result_expected: 'The field family name is not present. The next field is electronic devices'
    },
    {
        message_id: "018",
        test_form_number: 3,
        initial_state: {
            u.slots: [
                {
                    u.slot_name: electronic_devices,
                    u.slot_value: "smartphone"
                }
            ]
        },
        test_case_message: {
            entities: [],
            intent: {
                name: verify_value_fields,
                confidence: 1
            },
            text: 'can i have a point of the situation?'
        },
        result_expected: 'Gives the paires field-value. The next field is message'
    },
    {
        message_id: "019",
        test_form_number: 3,
        initial_state: {},
        test_case_message: {
            entities: [],
            intent: {
                name: repeat_form_explanation,
                confidence: 1
            },
            text: 'can you tell me again what is this form about?'
        },
        result_expected: 'Gives the form description. The next field is message'
    },
    {
        message_id: "020",
        test_form_number: 3,
        initial_state: {},
        test_case_message: {
            entities: [
                {
                    entity: input_field,
                    value: message
                }
            ],
            intent: {
                name: explain_field,
                confidence: 1
            },
            text: 'what is message?'
        },
        result_expected: 'Explains message. The next field is message'
    },
    {
        message_id: "021",
        test_form_number: 1,
        initial_state: {
            u.slots: [
                {
                    u.slot_name: first_name,
                    u.slot_value: None
                },
                {
                    u.slot_name: mark,
                    u.slot_value: None
                },
                {
                    u.slot_name: password,
                    u.slot_value: None
                },
                {
                    u.slot_name: email_address,
                    u.slot_value: None
                }
            ],
        },
        test_case_message: {
            entities: [
                {
                    entity: input_value,
                    value: 'jack'
                }
            ],
            intent: {
                name: complete_field,
                confidence: 1
            },
            text: 'jack'
        },
        result_expected: 'First name is jack. The next field is mark'
    },
    {
        message_id: "022",
        test_form_number: 1,
        initial_state: {},
        test_case_message: {
            entities: [
                {
                    entity: input_field,
                    value: first_name
                },
                {
                    entity: input_value,
                    value: 'jack bauer'
                }
            ],
            intent: {
                name: modify_value_field,
                confidence: 1
            },
            text: 'i want to odify the first name with jack bauer'
        },
        result_expected: 'First name is jack bauer. The next field is mark'
    },
    {
        message_id: "023",
        test_form_number: 1,
        initial_state: {},
        test_case_message: {
            entities: [
                {
                    entity: input_field,
                    value: first_name
                },
                {
                    entity: input_value,
                    value: 'estelle laure harris'
                }
            ],
            intent: {
                name: complete_field,
                confidence: 1
            },
            text: 'my first name is estelle laure harris'
        },
        result_expected: 'First name is estelle laure harris. The next slot is mark'
    },
    {
        message_id: "024",
        test_form_number: 1,
        initial_state: {},
        test_case_message: {
            entities: [
                {
                    entity: input_field,
                    value: mark
                },
                {
                    entity: input_value,
                    value: '28'
                }
            ],
            intent: {
                name: complete_field,
                confidence: 1
            },
            text: 'my mark is 28'
        },
        result_expected: 'The mark is 28, the next field is password'
    },
    {
        message_id: "025",
        test_form_number: 1,
        initial_state: {},
        test_case_message: {
            entities: [
                {
                    entity: input_field,
                    value: mark
                },
                {
                    entity: input_value,
                    value: '28,1'
                }
            ],
            intent: {
                name: complete_field,
                confidence: 1
            },
            text: 'my mark is 28,1'
        },
        result_expected: 'The mark is 28,1. The next field is password'
    },
    {
        message_id: "026",
        test_form_number: 1,
        initial_state: {
            u.slots: [
                {
                    u.slot_name: first_name,
                    u.slot_value: None
                },
                {
                    u.slot_name: mark,
                    u.slot_value: None
                },
                {
                    u.slot_name: email_address,
                    u.slot_value: None
                },
                {
                    u.slot_name: password,
                    u.slot_value: None
                }
            ],
            spelling_state: {
                u.close_prompt_enabled: False,
                u.current_spelling_input_value: '',
                u.spelling_list: [],
                u.waiting_message: None,
                u.saved_spelling_fields: [],
                u.saved_spelling_values: []
            },
            machine_parameters: {
                u.submit_done: False,
                u.reset_alarm_enabled: False,
                u.submit_alarm_enabled: False,
                u.possible_next_action: None,
                u.warning_message: ''
            }
        },
        test_case_message: {
            entities: [
                {
                    entity: input_field,
                    value: mark
                },
                {
                    entity: input_value,
                    value: '28,45'
                }
            ],
            intent: {
                name: complete_field,
                confidence: 1
            },
            text: 'my mark is 28,45'
        },
        result_expected: 'The mark is 28,45. The next field is password'
    },
    {
        message_id: "027",
        test_form_number: 1,
        initial_state: {},
        test_case_message: {
            entities: [
                {
                    entity: input_field,
                    value: mark
                },
                {
                    entity: input_value,
                    value: '28,654'
                }
            ],
            intent: {
                name: complete_field,
                confidence: 1
            },
            text: 'my mark is 28,654'
        },
        result_expected: 'The mark is 28,654. The next field is password'
    },
    {
        message_id: "028",
        test_form_number: 1,
        initial_state: {
            spelling_state: {
                u.close_prompt_enabled: False,
                u.current_spelling_input_value: '',
                u.spelling_list: [],
                u.waiting_message: None,
                u.saved_spelling_fields: [],
                u.saved_spelling_values: []
            },
            machine_parameters: {
                u.submit_done: False,
                u.reset_alarm_enabled: False,
                u.submit_alarm_enabled: False,
                u.possible_next_action: None,
                u.warning_message: ''
            }
        },
        test_case_message: {
            entities: [
                {
                    entity: input_field,
                    value: mark
                },
                {
                    entity: input_value,
                    value: '280'
                }
            ],
            intent: {
                name: complete_field,
                confidence: 1
            },
            text: 'my mark is 280'
        },
        result_expected: 'The mark is above the maximum, the next field is password'
    },
    {
        message_id: "029",
        test_form_number: 1,
        initial_state: {},
        test_case_message: {
            entities: [
                {
                    entity: input_field,
                    value: mark
                },
                {
                    entity: input_value,
                    value: '24,4567'
                }
            ],
            intent: {
                name: complete_field,
                confidence: 1
            },
            text: 'mark 24,4567'
        },
        result_expected: 'The mark is 24,45'
    },
    {
        message_id: "030",
        test_form_number: 1,
        initial_state: {},
        test_case_message: {
            entities: [
                {
                    entity: input_field,
                    value: mark
                },
                {
                    entity: input_value,
                    value: '2.001.002'
                }
            ],
            intent: {
                name: complete_field,
                confidence: 1
            },
            text: 'mark 2.001.002'
        },
        result_expected: 'the mark is above the maximum'
    },
    {
        message_id: "031",
        test_form_number: 1,
        initial_state: {},
        test_case_message: {
            entities: [
                {
                    entity: input_field,
                    value: mark
                },
                {
                    entity: input_value,
                    value: '3.000,54'
                }
            ],
            intent: {
                name: complete_field,
                confidence: 1
            },
            text: 'mark 3.000,54'
        },
        result_expected: 'The mark is above the maximum'
    },
    {
        message_id: "032",
        test_form_number: 1,
        initial_state: {},
        test_case_message: {
            entities: [
                {
                    entity: input_field,
                    value: mark
                },
                {
                    entity: input_value,
                    value: '23.211'
                }
            ],
            intent: {
                name: complete_field,
                confidence: 1
            },
            text: 'mark 23.211'
        },
        result_expected: 'The mark is 23,211'
    },
    {
        message_id: "033",
        test_form_number: 1,
        initial_state: {},
        test_case_message: {
            entities: [
                {
                    entity: input_field,
                    value: mark
                },
                {
                    entity: input_value,
                    value: '17,002.988'
                }
            ],
            intent: {
                name: complete_field,
                confidence: 1
            },
            text: 'mark 17,002.98'
        },
        result_expected: 'The is above the maximum'
    },
    {
        message_id: "034",
        test_form_number: 1,
        initial_state: {},
        test_case_message: {
            entities: [
                {
                    entity: input_field,
                    value: password
                },
                {
                    entity: input_value,
                    value: 'pass'
                }
            ],
            intent: {
                name: complete_field,
                confidence: 1
            },
            text: 'the password is pass'
        },
        result_expected: 'The value is too short'
    },
    {
        message_id: "035",
        test_form_number: 1,
        initial_state: {},
        test_case_message: {
            entities: [
                {
                    entity: input_field,
                    value: password
                },
                {
                    entity: input_value,
                    value: 'pass_word'
                }
            ],
            intent: {
                name: complete_field,
                confidence: 1
            },
            text: 'pass_word is the password'
        },
        result_expected: 'The password is pass_word'
    },
    {
        message_id: "036",
        test_form_number: 1,
        initial_state: {},
        test_case_message: {
            entities: [
                {
                    entity: input_field,
                    value: password
                },
                {
                    entity: input_value,
                    value: 'p!@ss#w$%^r&d*_'
                }
            ],
            intent: {
                name: complete_field,
                confidence: 1
            },
            text: 'my password is p!@ss#w$%^r&d*_'
        },
        result_expected: 'The password is p!@ss#w$%^r&d*_'
    },
    {
        message_id: "037",
        test_form_number: 3,
        initial_state: {},
        test_case_message: {
            entities: [],
            intent: {
                name: repeat_form_title,
                confidence: 1
            },
            text: 'what is the title of this form?'
        },
        result_expected: 'Gives the form title. The next field is message'
    },
    {
        message_id: "038",
        test_form_number: 1,
        initial_state: {},
        test_case_message: {
            entities: [
                {
                    entity: input_field,
                    value: email_address
                },
                {
                    entity: input_value,
                    value: 'em@il.it'
                }
            ],
            intent: {
                name: complete_field,
                confidence: 1
            },
            text: 'email address em@il.it'
        },
        result_expected: 'Email address is em@il.it'
    },
    {
        message_id: "039",
        test_form_number: 1,
        initial_state: {},
        test_case_message: {
            entities: [
                {
                    entity: input_field,
                    value: email_address
                },
                {
                    entity: input_value,
                    value: 'em_ail'
                }
            ],
            intent: {
                name: complete_field,
                confidence: 1
            },
            text: 'the email address is em_ail'
        },
        result_expected: 'There should be the at sign'
    },
    {
        message_id: "040",
        test_form_number: 1,
        initial_state: {},
        test_case_message: {
            entities: [
                {
                    entity: input_field,
                    value: email_address
                },
                {
                    entity: input_value,
                    value: 'e@m@il.it'
                }
            ],
            intent: {
                name: complete_field,
                confidence: 1
            },
            text: 'my email address is e@m@il.it'
        },
        result_expected: 'There should be only one at sign'
    },
    {
        message_id: "041",
        test_form_number: 1,
        initial_state: {},
        test_case_message: {
            entities: [
                {
                    entity: input_field,
                    value: email_address
                },
                {
                    entity: input_value,
                    value: 'em@il.mail.it'
                }
            ],
            intent: {
                name: complete_field,
                confidence: 1
            },
            text: 'the email address is em@il.mail.it'
        },
        result_expected: 'Te email address is em@il.mail.it'
    },
    {
        message_id: "042",
        test_form_number: 1,
        initial_state: {},
        test_case_message: {
            entities: [
                {
                    entity: input_field,
                    value: email_address
                },
                {
                    entity: input_value,
                    value: 'my_em@il.mail.polimi.it'
                }
            ],
            intent: {
                name: complete_field,
                confidence: 1
            },
            text: 'my email address is my_em@il.mail.polimi.it'
        },
        result_expected: 'The email address is my_em@il.mail.polimi.it'
    },
    {
        message_id: "043",
        test_form_number: 2,
        initial_state: {},
        test_case_message: {
            entities: [
                {
                    entity: input_field,
                    value: email_address
                },
                {
                    entity: input_value,
                    value: 'em@il'
                }
            ],
            intent: {
                name: complete_field,
                confidence: 1
            },
            text: 'the email address is em@il'
        },
        result_expected: 'There should be the dot_sign'
    },
    {
        message_id: "044",
        test_form_number: 2,
        initial_state: {
            u.slots: [
                {
                    u.slot_name: phone_number,
                    u.slot_value: None
                },
                {
                    u.slot_name: number_persons,
                    u.slot_value: None
                },
                {
                    u.slot_name: birthday,
                    u.slot_value: None
                },
                {
                    u.slot_name: arrival_time,
                    u.slot_value: None
                }
            ]
        },
        test_case_message: {
            entities: [
                {
                    entity: input_field,
                    value: phone_number
                },
                {
                    entity: input_value,
                    value: '00393545345566'
                }
            ],
            intent: {
                name: complete_field,
                confidence: 1
            },
            text: 'phone number 00393545345566'
        },
        result_expected: 'The value of the phone number becomes 00393545345566'
    },
    {
        message_id: "045",
        test_form_number: 2,
        initial_state: {},
        test_case_message: {
            entities: [
                {
                    entity: input_field,
                    value: phone_number
                },
                {
                    entity: input_value,
                    value: '+393454566789'
                }
            ],
            intent: {
                name: complete_field,
                confidence: 1
            },
            text: 'the phone number is +393454566789'
        },
        result_expected: 'The value of phone number becomes +393454566789'
    },
    {
        message_id: "046",
        test_form_number: 2,
        initial_state: {},
        test_case_message: {
            entities: [
                {
                    entity: input_field,
                    value: phone_number
                },
                {
                    entity: input_value,
                    value: '+39+2376758933'
                }
            ],
            intent: {
                name: complete_field,
                confidence: 1
            },
            text: 'the phone number is +39+2376758933'
        },
        result_expected: 'There should be at most one <+>'
    },
    {
        message_id: "047",
        test_form_number: 2,
        initial_state: {
            spelling_state: {
                u.close_prompt_enabled: False,
                u.current_spelling_input_value: '',
                u.spelling_list: [],
                u.waiting_message: None,
                u.saved_spelling_fields: [],
                u.saved_spelling_values: []
            },
            machine_parameters: {
                u.submit_done: False,
                u.reset_alarm_enabled: False,
                u.submit_alarm_enabled: False,
                u.possible_next_action: None,
                u.warning_message: ''
            }
        },
        test_case_message: {
            entities: [
                {
                    entity: input_field,
                    value: phone_number
                },
                {
                    entity: input_value,
                    value: '14'
                }
            ],
            intent: {
                name: complete_field,
                confidence: 1
            },
            text: 'the phone number is 14'
        },
        result_expected: 'Too short phone number'
    },
    {
        message_id: "048",
        test_form_number: 2,
        initial_state: {
            u.slots: [
                {
                    u.slot_name: phone_number,
                    u.slot_value: None
                },
                {
                    u.slot_name: number_persons,
                    u.slot_value: None
                },
                {
                    u.slot_name: birthday,
                    u.slot_value: None
                }
            ]
        },
        test_case_message: {
            entities: [
                {
                    entity: input_field,
                    value: phone_number
                },
                {
                    entity: input_value,
                    value: '+237899755421345456'
                }
            ],
            intent: {
                name: complete_field,
                confidence: 1
            },
            text: 'the phone number is +237899755421345456'
        },
        result_expected: 'Too long phone number'
    },
    {
        message_id: "049",
        test_form_number: 2,
        initial_state: {},
        test_case_message: {
            entities: [
                {
                    entity: input_field,
                    value: number_persons
                },
                {
                    entity: input_value,
                    value: '-2'
                }
            ],
            intent: {
                name: complete_field,
                confidence: 1
            },
            text: 'the number of persons is -2'
        },
        result_expected: 'Value lower than the minimum'
    },
    {
        message_id: "050",
        test_form_number: 2,
        initial_state: {
            u.slots: [
                {
                    u.slot_name: birthday,
                    u.slot_value: None
                },
                {
                    u.slot_name: phone_number,
                    u.slot_value: None
                },
                {
                    u.slot_name: number_persons,
                    u.slot_value: None
                },
                {
                    u.slot_name: arrival_time,
                    u.slot_value: None
                }
            ],
            spelling_state: {
                u.close_prompt_enabled: False,
                u.current_spelling_input_value: '',
                u.spelling_list: [],
                u.waiting_message: None,
                u.saved_spelling_fields: [],
                u.saved_spelling_values: []
            },
            machine_parameters: {
                u.submit_done: False,
                u.reset_alarm_enabled: False,
                u.submit_alarm_enabled: False,
                u.possible_next_action: None,
                u.warning_message: ''
            }
        },
        test_case_message: {
            entities: [
                {
                    entity: input_field,
                    value: number_persons
                },
                {
                    entity: input_value,
                    value: '4'
                }
            ],
            intent: {
                name: complete_field,
                confidence: 1
            },
            text: 'the number of persons is 4'
        },
        result_expected: 'The value of number of persons is 4'
    },
    {
        message_id: "051",
        test_form_number: 2,
        initial_state: {},
        test_case_message: {
            entities: [
                {
                    entity: input_field,
                    value: number_persons
                },
                {
                    entity: input_value,
                    value: '4,5'
                }
            ],
            intent: {
                name: complete_field,
                confidence: 1
            },
            text: 'The number of persons is 4,5'
        },
        result_expected: '4,5 is not an integer number'
    },
    {
        message_id: "052",
        test_form_number: 2,
        initial_state: {},
        test_case_message: {
            entities: [
                {
                    entity: input_field,
                    value: number_persons
                },
                {
                    entity: input_value,
                    value: '2,000'
                }
            ],
            intent: {
                name: complete_field,
                confidence: 1
            },
            text: 'the number of persons is 2,000'
        },
        result_expected: 'Number above the maximum'
    },
    {
        message_id: "053",
        test_form_number: 2,
        initial_state: {},
        test_case_message: {
            entities: [
                {
                    entity: input_field,
                    value: number_persons
                },
                {
                    entity: input_value,
                    value: '1.000'
                }
            ],
            intent: {
                name: complete_field,
                confidence: 1
            },
            text: 'the number of persons is 1.000'
        },
        result_expected: 'The number is above the maximum'
    },
    {
        message_id: "054",
        test_form_number: 2,
        initial_state: {
            u.slots: [
                {
                    u.slot_name: birthday,
                    u.slot_value: None
                },
                {
                    u.slot_name: phone_number,
                    u.slot_value: None
                },
                {
                    u.slot_name: number_persons,
                    u.slot_value: None
                },
                {
                    u.slot_name: arrival_time,
                    u.slot_value: None
                }
            ],
            spelling_state: {
                u.close_prompt_enabled: False,
                u.current_spelling_input_value: '',
                u.spelling_list: [],
                u.waiting_message: None,
                u.saved_spelling_fields: [],
                u.saved_spelling_values: []
            },
            machine_parameters: {
                u.submit_done: False,
                u.reset_alarm_enabled: False,
                u.submit_alarm_enabled: False,
                u.possible_next_action: None,
                u.warning_message: ''
            }
        },
        test_case_message: {
            entities: [
                {
                    entity: input_field,
                    value: birthday
                },
                {
                    entity: input_value,
                    value: '2010-02-15'
                }
            ],
            intent: {
                name: complete_field,
                confidence: 1
            },
            text: 'the birthday is 2010-02-15'
        },
        result_expected: 'The birthday is 15/02/2010'
    },
    {
        message_id: "055",
        test_form_number: 2,
        initial_state: {},
        test_case_message: {
            entities: [
                {
                    entity: input_field,
                    value: birthday
                },
                {
                    entity: input_value,
                    value: '12-10-1995'
                }
            ],
            intent: {
                name: complete_field,
                confidence: 1
            },
            text: 'the birthday is 12-10-1995'
        },
        result_expected: 'The birthday is 12/10/1995'
    },
    {
        message_id: "056",
        test_form_number: 2,
        initial_state: {},
        test_case_message: {
            entities: [
                {
                    entity: input_field,
                    value: birthday
                },
                {
                    entity: input_value,
                    value: '08-15-2005'
                }
            ],
            intent: {
                name: complete_field,
                confidence: 1
            },
            text: 'the birthday is 08-15-2005'
        },
        result_expected: 'The birthday is 15/08/2005'
    },
    {
        message_id: "057",
        test_form_number: 2,
        initial_state: {},
        test_case_message: {
            entities: [
                {
                    entity: input_field,
                    value: birthday
                },
                {
                    entity: input_value,
                    value: '15032002'
                }
            ],
            intent: {
                name: complete_field,
                confidence: 1
            },
            text: 'the birthday is 15032002'
        },
        result_expected: 'The birthday is 15/03/2002'
    },
    {
        message_id: "058",
        test_form_number: 2,
        initial_state: {
            u.slots: [
                {
                    u.slot_name: birthday,
                    u.slot_value: None
                },
                {
                    u.slot_name: phone_number,
                    u.slot_value: None
                },
                {
                    u.slot_name: number_persons,
                    u.slot_value: None
                },
                {
                    u.slot_name: arrival_time,
                    u.slot_value: None
                }
            ],
            spelling_state: {
                u.close_prompt_enabled: False,
                u.current_spelling_input_value: '',
                u.spelling_list: [],
                u.waiting_message: None,
                u.saved_spelling_fields: [],
                u.saved_spelling_values: []
            },
            machine_parameters: {
                u.submit_done: False,
                u.reset_alarm_enabled: False,
                u.submit_alarm_enabled: False,
                u.possible_next_action: None,
                u.warning_message: ''
            }
        },
        test_case_message: {
            entities: [
                {
                    entity: input_field,
                    value: birthday
                },
                {
                    entity: input_value,
                    value: '02 january 1988'
                }
            ],
            intent: {
                name: complete_field,
                confidence: 1
            },
            text: 'the birthday is 02 january 1988'
        },
        result_expected: 'The birthday is 02/01/1988'
    },
    {
        message_id: "059",
        test_form_number: 2,
        initial_state: {},
        test_case_message: {
            entities: [
                {
                    entity: input_field,
                    value: birthday
                },
                {
                    entity: input_value,
                    value: 'February 28 2020'
                }
            ],
            intent: {
                name: complete_field,
                confidence: 1
            },
            text: 'the birthday is February 28 2020'
        },
        result_expected: 'The birthday is 28/02/2020'
    },
    {
        message_id: "060",
        test_form_number: 2,
        initial_state: {},
        test_case_message: {
            entities: [
                {
                    entity: input_field,
                    value: arrival_time
                },
                {
                    entity: input_value,
                    value: '15:10'
                }
            ],
            intent: {
                name: complete_field,
                confidence: 1
            },
            text: 'the arrival time is 15:10'
        },
        result_expected: 'The arrival time is 15:10'
    },
    {
        message_id: "061",
        test_form_number: 2,
        initial_state: {},
        test_case_message: {
            entities: [
                {
                    entity: input_field,
                    value: arrival_time
                },
                {
                    entity: input_value,
                    value: '1230'
                }
            ],
            intent: {
                name: complete_field,
                confidence: 1
            },
            text: 'the arrival time is 1230'
        },
        result_expected: 'The arrival time is 12:30'
    },
    {
        message_id: "062",
        test_form_number: 2,
        initial_state: {
            u.slots: [
                {
                    u.slot_name: birthday,
                    u.slot_value: None
                },
                {
                    u.slot_name: phone_number,
                    u.slot_value: None
                },
                {
                    u.slot_name: number_persons,
                    u.slot_value: None
                },
                {
                    u.slot_name: arrival_time,
                    u.slot_value: None
                }
            ],
            spelling_state: {
                u.close_prompt_enabled: False,
                u.current_spelling_input_value: '',
                u.spelling_list: [],
                u.waiting_message: None,
                u.saved_spelling_fields: [],
                u.saved_spelling_values: []
            },
            machine_parameters: {
                u.submit_done: False,
                u.reset_alarm_enabled: False,
                u.submit_alarm_enabled: False,
                u.possible_next_action: None,
                u.warning_message: ''
            }
        },
        test_case_message: {
            entities: [
                {
                    entity: input_field,
                    value: arrival_time
                },
                {
                    entity: input_value,
                    value: '08:05 am'
                }
            ],
            intent: {
                name: complete_field,
                confidence: 1
            },
            text: 'the arrival time is 08:05 am'
        },
        result_expected: 'The arrival time is 08:05'
    },
    {
        message_id: "063",
        test_form_number: 2,
        initial_state: {},
        test_case_message: {
            entities: [
                {
                    entity: input_field,
                    value: arrival_time
                },
                {
                    entity: input_value,
                    value: '5 pm'
                }
            ],
            intent: {
                name: complete_field,
                confidence: 1
            },
            text: 'the arrival time is 5 pm'
        },
        result_expected: 'The arrival time is 17:00'
    },
    {
        message_id: "064",
        test_form_number: 2,
        initial_state: {},
        test_case_message: {
            entities: [
                {
                    entity: input_field,
                    value: arrival_time
                },
                {
                    entity: input_value,
                    value: '4:15'
                }
            ],
            intent: {
                name: complete_field,
                confidence: 1
            },
            text: 'the arrival time is 4:15'
        },
        result_expected: 'The arrival time is 04:15'
    },
    {
        message_id: "065",
        test_form_number: 2,
        initial_state: {},
        test_case_message: {
            entities: [
                {
                    entity: input_field,
                    value: arrival_time
                },
                {
                    entity: input_value,
                    value: '2:20 pm'
                }
            ],
            intent: {
                name: complete_field,
                confidence: 1
            },
            text: 'the arrival time is 2:20 pm'
        },
        result_expected: 'The arrival time is 14:20'
    },
    {
        message_id: "066",
        test_form_number: 2,
        initial_state: {
            u.slots: [
                {
                    u.slot_name: birthday,
                    u.slot_value: None
                },
                {
                    u.slot_name: phone_number,
                    u.slot_value: None
                },
                {
                    u.slot_name: number_persons,
                    u.slot_value: None
                },
                {
                    u.slot_name: arrival_time,
                    u.slot_value: None
                }
            ],
            spelling_state: {
                u.close_prompt_enabled: False,
                u.current_spelling_input_value: '',
                u.spelling_list: [],
                u.waiting_message: None,
                u.saved_spelling_fields: [],
                u.saved_spelling_values: []
            },
            machine_parameters: {
                u.submit_done: False,
                u.reset_alarm_enabled: False,
                u.submit_alarm_enabled: False,
                u.possible_next_action: None,
                u.warning_message: ''
            }
        },
        test_case_message: {
            entities: [
                {
                    entity: input_field,
                    value: arrival_time
                },
                {
                    entity: input_value,
                    value: '7'
                }
            ],
            intent: {
                name: complete_field,
                confidence: 1
            },
            text: 'the arrival time is 7'
        },
        result_expected: 'The arrival time is 07:00'
    },
    {
        message_id: "067",
        test_form_number: 3,
        initial_state: {
            u.slots: [
                {
                    u.slot_name: message,
                    u.slot_value: None
                },
                {
                    u.slot_name: gender,
                    u.slot_value: None
                }
            ]
        },
        test_case_message: {
            entities: [
                {
                    entity: input_field,
                    value: message
                },
                {
                    entity: input_value,
                    value: "if the mountain won't come to muhammad, muhammad must go to the mountain"
                }
            ],
            intent: {
                name: complete_field,
                confidence: 1
            },
            text: "the message is if the mountain won't come to muhammad, muhammad must go to the mountain"
        },
        result_expected: "message becomes 'if the mountain won't come to muhammad, muhammad must go to the mountain'"
    },
    {
        message_id: "068",
        test_form_number: 3,
        initial_state: {
            u.slots: [
                {
                    u.slot_name: message,
                    u.slot_value: None
                },
                {
                    u.slot_name: gender,
                    u.slot_value: None
                }
            ]
        },
        test_case_message: {
            entities: [
                {
                    entity: input_field,
                    value: message
                },
                {
                    entity: input_value,
                    value: 'adversity and loss make a man wise. a journey of thousand miles begins with a single step.'
                }
            ],
            intent: {
                name: complete_field,
                confidence: 1
            },
            text: 'the message is adversity and loss make a man wise. a journey of thousand miles begins with a single step.'
        },
        result_expected: "The message becomes 'adversity and loss make a man wise. a journey of thousand miles begins with a single step.'"
    },
    {
        message_id: "069",
        test_form_number: 3,
        initial_state: {
            u.slots: [
                {
                    u.slot_name: gender,
                    u.slot_value: None
                }
            ]
        },
        test_case_message: {
            entities: [
                {
                    entity: input_field,
                    value: message
                },
                {
                    entity: input_value,
                    value: "better late than never, appearances can be deceptive, fall seven times stand up eight, good things come to those who wait."
                }
            ],
            intent: {
                name: complete_field,
                confidence: 1
            },
            text: 'the message is better late than never, appearances can be deceptive, fall seven times stand up eight, good things come to those who wait.'
        },
        result_expected: "the message becomes 'better late than never, appearances can be deceptive, fall seven times stand up eight, good things come to those who wait.'"
    },
    {
        message_id: "070",
        test_form_number: 3,
        initial_state: {
            u.slots: [
                {
                    u.slot_name: car,
                    u.slot_value: None
                },
                {
                    u.slot_name: gender,
                    u.slot_value: None
                },
                {
                    u.slot_name: electronic_devices,
                    u.slot_value: None
                },
                {
                    u.slot_name: message,
                    u.slot_value: None
                }
            ]
        },
        test_case_message: {
            entities: [
                {
                    entity: input_field,
                    value: car
                },
                {
                    entity: input_value,
                    value: 'citroen'
                }
            ],
            intent: {
                name: complete_field,
                confidence: 1
            },
            text: 'the car is citroen'
        },
        result_expected: 'The car is citroen'
    },
    {
        message_id: "071",
        test_form_number: 3,
        initial_state: {},
        test_case_message: {
            entities: [
                {
                    entity: input_field,
                    value: car
                },
                {
                    entity: input_value,
                    value: 'ford'
                },
                {
                    entity: input_value,
                    value: 'bmw'
                }
            ],
            intent: {
                name: complete_field,
                confidence: 1
            },
            text: 'the choices for car are ford and bmw'
        },
        result_expected: 'The car becomes ford, bmw is not a choice for gender.'
    },
    {
        message_id: "072",
        test_form_number: 3,
        initial_state: {},
        test_case_message: {
            entities: [
                {
                    entity: input_field,
                    value: gender
                },
                {
                    entity: input_value,
                    value: 'male'
                }
            ],
            intent: {
                name: complete_field,
                confidence: 1
            },
            text: 'the gender is male'
        },
        result_expected: 'gender is male'
    },
    {
        message_id: "073",
        test_form_number: 3,
        initial_state: {
            u.slots: [
                {
                    u.slot_name: car,
                    u.slot_value: None
                },
                {
                    u.slot_name: gender,
                    u.slot_value: None
                },
                {
                    u.slot_name: electronic_devices,
                    u.slot_value: None
                },
                {
                    u.slot_name: message,
                    u.slot_value: None
                }
            ]
        },
        test_case_message: {
            entities: [
                {
                    entity: input_field,
                    value: gender
                },
                {
                    entity: input_value,
                    value: 'female'
                },
                {
                    entity: input_value,
                    value: 'none'
                }
            ],
            intent: {
                name: complete_field,
                confidence: 1
            },
            text: 'the choices for the gender are female and male'
        },
        result_expected: 'gender becomes female, none is not a choice for electronic devices'
    },
    {
        message_id: "074",
        test_form_number: 3,
        initial_state: {},
        test_case_message: {
            entities: [
                {
                    entity: input_field,
                    value: electronic_devices
                },
                {
                    entity: input_value,
                    value: 'smartphone'
                }
            ],
            intent: {
                name: complete_field,
                confidence: 1
            },
            text: 'the electronic devices ares smartphone'
        },
        result_expected: 'electronic devices becomes smartphone'
    },
    {
        message_id: "075",
        test_form_number: 3,
        initial_state: {},
        test_case_message: {
            entities: [
                {
                    entity: input_field,
                    value: electronic_devices
                },
                {
                    entity: input_value,
                    value: 'smartphone'
                },
                {
                    entity: input_value,
                    value: 'tablet'
                }
            ],
            intent: {
                name: complete_field,
                confidence: 1
            },
            text: 'the electronic devices are sartphone and tablet'
        },
        result_expected: 'The electronic devices become [smartphone, tablets]'
    },
    {
        message_id: "076",
        test_form_number: 3,
        initial_state: {},
        test_case_message: {
            entities: [
                {
                    entity: input_field,
                    value: electronic_devices
                },
                {
                    entity: input_value,
                    value: 'computer'
                },
                {
                    entity: input_value,
                    value: 'smart watch'
                },
                {
                    entity: input_value,
                    value: 'smart tv'
                }
            ],
            intent: {
                name: complete_field,
                confidence: 1
            },
            text: 'the electronic devices are computer, smart watch, smart tv'
        },
        result_expected: 'The electronic devices become [computer, smart watch, smart tv]'
    },
    {
        message_id: "077",
        test_form_number: 3,
        initial_state: {
            u.slots: [
                {
                    u.slot_name: gender,
                    u.slot_value: None
                }
            ]
        },
        test_case_message: {
            entities: [
                {
                    entity: input_field,
                    value: message
                },
                {
                    entity: input_value,
                    value: 'if the mountain'
                }
            ],
            intent: {
                name: complete_field,
                confidence: 1
            },
            text: 'the message is if the mountain'
        },
        result_expected: 'message becomes "if the mountain"'
    },
    {
        message_id: "078",
        test_form_number: 3,
        initial_state: {
            u.slots: [
                {
                    u.slot_name: gender,
                    u.slot_value: None
                }
            ]
        },
        test_case_message: {
            entities: [
                {
                    entity: input_field,
                    value: message
                },
                {
                    entity: input_value,
                    value: "if the mountain won't come to muhammad"
                }
            ],
            intent: {
                name: complete_field,
                confidence: 1
            },
            text: "the message is if the mountain won't come to muhammad"
        },
        result_expected: "message becomes 'if the mountain won't come to muhammad'"
    },
    {
        message_id: "079",
        test_form_number: 3,
        initial_state: {
            u.slots: [
                {
                    u.slot_name: message,
                    u.slot_value: None
                },
                {
                    u.slot_name: gender,
                    u.slot_value: None
                }
            ]
        },
        test_case_message: {
            entities: [
                {
                    entity: input_field,
                    value: message
                },
                {
                    entity: input_value,
                    value: "if the mountain won't come to muhammad, muhammad must go"
                }
            ],
            intent: {
                name: complete_field,
                confidence: 1
            },
            text: "the message is if the mountain won't come to muhammad, muhammad must go"
        },
        result_expected: "message becomes 'if the mountain won't come to muhammad, muhammad must go'"
    },


    {
        message_id: "080",
        test_form_number: 1,
        initial_state: {
            u.slots: [
                {
                    u.slot_name: first_name,
                    u.slot_value: None
                },
                {
                    u.slot_name: last_name,
                    u.slot_value: None
                },
                {
                    u.slot_name: mark,
                    u.slot_value: None
                },
                {
                    u.slot_name: password,
                    u.slot_value: None
                },
                {
                    u.slot_name: email_address,
                    u.slot_value: None
                }
            ],
            spelling_state: {
                u.close_prompt_enabled: False,
                u.current_spelling_input_value: '',
                u.spelling_list: [],
                u.waiting_message: None,
                u.saved_spelling_fields: [],
                u.saved_spelling_values: []
            },
            machine_parameters: {
                u.submit_done: False,
                u.reset_alarm_enabled: False,
                u.submit_alarm_enabled: False,
                u.possible_next_action: None,
                u.warning_message: ''
            }
        },
        test_case_message: {
            entities: [],
            intent: {
                name: complete_field,
                confidence: 1
            },
            text: 'i would like to complete a field'
        },
        result_expected: 'which field do you want to complete?'
    },
    {
        message_id: "081",
        test_form_number: 1,
        initial_state: {
            u.slots: [
                {
                    u.slot_name: first_name,
                    u.slot_value: None
                },
                {
                    u.slot_name: last_name,
                    u.slot_value: None
                },
                {
                    u.slot_name: mark,
                    u.slot_value: None
                },
                {
                    u.slot_name: password,
                    u.slot_value: None
                },
                {
                    u.slot_name: email_address,
                    u.slot_value: None
                }
            ],
            spelling_state: {
                u.close_prompt_enabled: False,
                u.current_spelling_input_value: '',
                u.spelling_list: [],
                u.waiting_message: None,
                u.saved_spelling_fields: [],
                u.saved_spelling_values: []
            },
            machine_parameters: {
                u.submit_done: False,
                u.reset_alarm_enabled: False,
                u.submit_alarm_enabled: False,
                u.possible_next_action: None,
                u.warning_message: ''
            }
        },
        test_case_message: {
            entities: [
                {
                    entity: input_field,
                    value: mark
                }
            ],
            intent: {
                name: complete_field,
                confidence: 1
            },
            text: 'i would like to complete the mark'
        },
        result_expected: 'insert the value of the field mark'
    },
    {
        message_id: "082",
        test_form_number: 1,
        initial_state: {
            u.slots: [
                {
                    u.slot_name: first_name,
                    u.slot_value: None
                },
                {
                    u.slot_name: last_name,
                    u.slot_value: None
                },
                {
                    u.slot_name: mark,
                    u.slot_value: '22'
                },
                {
                    u.slot_name: password,
                    u.slot_value: None
                },
                {
                    u.slot_name: email_address,
                    u.slot_value: None
                }
            ],
            spelling_state: {
                u.close_prompt_enabled: False,
                u.current_spelling_input_value: '',
                u.spelling_list: [],
                u.waiting_message: None,
                u.saved_spelling_fields: [],
                u.saved_spelling_values: []
            },
            machine_parameters: {
                u.submit_done: False,
                u.reset_alarm_enabled: False,
                u.submit_alarm_enabled: False,
                u.possible_next_action: None,
                u.warning_message: ''
            }
        },
        test_case_message: {
            entities: [{
                    entity: input_value,
                    value: 'my_password8ere'
                }
            ],
            intent: {
                name: complete_field,
                confidence: 1
            },
            text: 'my_password8ere'
        },
        result_expected: 'The password value becomes my_password8ere'
    },
    {
        message_id: "083",
        test_form_number: 1,
        initial_state: {
            u.slots: [
                {
                    u.slot_name: first_name,
                    u.slot_value: None
                },
                {
                    u.slot_name: last_name,
                    u.slot_value: None
                },
                {
                    u.slot_name: mark,
                    u.slot_value: None
                },
                {
                    u.slot_name: password,
                    u.slot_value: None
                },
                {
                    u.slot_name: email_address,
                    u.slot_value: None
                }
            ],
            spelling_state: {
                u.close_prompt_enabled: False,
                u.current_spelling_input_value: '',
                u.spelling_list: [],
                u.waiting_message: None,
                u.saved_spelling_fields: [],
                u.saved_spelling_values: []
            },
            machine_parameters: {
                u.submit_done: False,
                u.reset_alarm_enabled: False,
                u.submit_alarm_enabled: False,
                u.possible_next_action: None,
                u.warning_message: ''
            }
        },
        test_case_message: {
            entities: [
                {
                    entity: input_field,
                    value: first_name
                },
                {
                    entity: input_field,
                    value: last_name
                }
            ],
            intent: {
                name: complete_field,
                confidence: 1
            },
            text: 'i would like to complete the first name and the last name'
        },
        result_expected: 'you are going to fill the first name and last name, we start by the first name. insert the first character... the spelling list contains first name and last name'
    },
    {
        message_id: "084",
        test_form_number: 1,
        initial_state: {
            u.slots: [
                {
                    u.slot_name: first_name,
                    u.slot_value: 'bob'
                },
                {
                    u.slot_name: last_name,
                    u.slot_value: 'alice'
                },
                {
                    u.slot_name: mark,
                    u.slot_value: None
                },
                {
                    u.slot_name: password,
                    u.slot_value: None
                },
                {
                    u.slot_name: email_address,
                    u.slot_value: None
                }
            ],
            spelling_state: {
                u.close_prompt_enabled: False,
                u.current_spelling_input_value: '',
                u.spelling_list: [],
                u.waiting_message: None,
                u.saved_spelling_fields: [],
                u.saved_spelling_values: []
            },
            machine_parameters: {
                u.submit_done: False,
                u.reset_alarm_enabled: False,
                u.submit_alarm_enabled: False,
                u.possible_next_action: None,
                u.warning_message: ''
            }
        },
        test_case_message: {
            entities: [
                {
                    entity: input_value,
                    value: 'bob'
                },
                {
                    entity: input_value,
                    value: 'alice'
                }
            ],
            intent: {
                name: complete_field,
                confidence: 1
            },
            text: '26 and alice@pass_good'
        },
        result_expected: 'the value of the mark have been inserted but alice@pass_good have not been taken into consideration since it is not associated to any field'
    },
    {
        message_id: "085",
        test_form_number: 1,
        initial_state: {
            u.slots: [
                {
                    u.slot_name: first_name,
                    u.slot_value: None
                },
                {
                    u.slot_name: last_name,
                    u.slot_value: None
                },
                {
                    u.slot_name: mark,
                    u.slot_value: None
                },
                {
                    u.slot_name: password,
                    u.slot_value: None
                },
                {
                    u.slot_name: email_address,
                    u.slot_value: None
                }
            ],
            spelling_state: {
                u.close_prompt_enabled: False,
                u.current_spelling_input_value: '',
                u.spelling_list: [],
                u.waiting_message: None,
                u.saved_spelling_fields: [],
                u.saved_spelling_values: []
            },
            machine_parameters: {
                u.submit_done: False,
                u.reset_alarm_enabled: False,
                u.submit_alarm_enabled: False,
                u.possible_next_action: None,
                u.warning_message: ''
            }
        },
        test_case_message: {
            entities: [
                {
                    entity: input_field,
                    value: email_address
                },
                {
                    entity: input_value,
                    value: 'bob@alice.polimi.it'
                }
            ],
            intent: {
                name: complete_field,
                confidence: 1
            },
            text: 'the email address is bob@alice.polimi.it'
        },
        result_expected: 'The email address becomes bob@alice.polimi.it'
    },
    {
        message_id: "086",
        test_form_number: 1,
        initial_state: {
            u.slots: [
                {
                    u.slot_name: first_name,
                    u.slot_value: None
                },
                {
                    u.slot_name: last_name,
                    u.slot_value: None
                },
                {
                    u.slot_name: mark,
                    u.slot_value: None
                },
                {
                    u.slot_name: password,
                    u.slot_value: None
                },
                {
                    u.slot_name: email_address,
                    u.slot_value: None
                }
            ],
            spelling_state: {
                u.close_prompt_enabled: False,
                u.current_spelling_input_value: '',
                u.spelling_list: [],
                u.waiting_message: None,
                u.saved_spelling_fields: [],
                u.saved_spelling_values: []
            },
            machine_parameters: {
                u.submit_done: False,
                u.reset_alarm_enabled: False,
                u.submit_alarm_enabled: False,
                u.possible_next_action: None,
                u.warning_message: ''
            }
        },
        test_case_message: {
            entities: [
                {
                    entity: input_field,
                    value: mark
                },
                {
                    entity: input_value,
                    value: '24'
                },
                {
                    entity: input_field,
                    value: password
                }
            ],
            intent: {
                name: complete_field,
                confidence: 1
            },
            text: 'the mark is 24, i want to complete the password'
        },
        result_expected: 'the password have not been taken into consideration because it is not associated to any value. The mark becomes 24'
    },
    {
        message_id: "087",
        test_form_number: 1,
        initial_state: {
            u.slots: [
                {
                    u.slot_name: first_name,
                    u.slot_value: None
                },
                {
                    u.slot_name: last_name,
                    u.slot_value: None
                },
                {
                    u.slot_name: mark,
                    u.slot_value: '22'
                },
                {
                    u.slot_name: password,
                    u.slot_value: None
                },
                {
                    u.slot_name: email_address,
                    u.slot_value: None
                }
            ],
            spelling_state: {
                u.close_prompt_enabled: False,
                u.current_spelling_input_value: '',
                u.spelling_list: [],
                u.waiting_message: None,
                u.saved_spelling_fields: [],
                u.saved_spelling_values: []
            },
            machine_parameters: {
                u.submit_done: False,
                u.reset_alarm_enabled: False,
                u.submit_alarm_enabled: False,
                u.possible_next_action: None,
                u.warning_message: ''
            }
        },
        test_case_message: {
            entities: [
                {
                    entity: input_field,
                    value: mark
                },
                {
                    entity: input_value,
                    value: '28'
                },
                {
                    entity: input_value,
                    value: 'alicebob@polimi.it'
                }
            ],
            intent: {
                name: complete_field,
                confidence: 1
            },
            text: 'the mark is 28, continue inserting alicebob@polimi.it'
        },
        result_expected: 'The mark becomes 28. the value alicebob@polimi.it has not been taken into consideration because it was not associated to any field'
    },
    {
        message_id: "088",
        test_form_number: 1,
        initial_state: {
            u.slots: [
                {
                    u.slot_name: first_name,
                    u.slot_value: None
                },
                {
                    u.slot_name: last_name,
                    u.slot_value: None
                },
                {
                    u.slot_name: mark,
                    u.slot_value: None
                },
                {
                    u.slot_name: password,
                    u.slot_value: None
                },
                {
                    u.slot_name: email_address,
                    u.slot_value: None
                }
            ],
            spelling_state: {
                u.close_prompt_enabled: False,
                u.current_spelling_input_value: '',
                u.spelling_list: [],
                u.waiting_message: None,
                u.saved_spelling_fields: [],
                u.saved_spelling_values: []
            },
            machine_parameters: {
                u.submit_done: False,
                u.reset_alarm_enabled: False,
                u.submit_alarm_enabled: False,
                u.possible_next_action: None,
                u.warning_message: ''
            }
        },
        test_case_message: {
            entities: [
                {
                    entity: input_field,
                    value: password
                },
                {
                    entity: input_value,
                    value: 'the#pa@ssw0r0'
                },
                {
                    entity: input_field,
                    value: email_address
                },
                {
                    entity: input_value,
                    value: 'my_email@address.pop'
                }
            ],
            intent: {
                name: complete_field,
                confidence: 1
            },
            text: 'the password is the#pa@ssw0r0 and the email address is my_email@address.pop'
        },
        result_expected: 'The password and email address are modified. insert the value of the first name'
    },
    {
        message_id: "089",
        test_form_number: 1,
        initial_state: {
            u.slots: [
                {
                    u.slot_name: first_name,
                    u.slot_value: None
                },
                {
                    u.slot_name: last_name,
                    u.slot_value: None
                },
                {
                    u.slot_name: mark,
                    u.slot_value: None
                },
                {
                    u.slot_name: password,
                    u.slot_value: None
                },
                {
                    u.slot_name: email_address,
                    u.slot_value: None
                }
            ],
            spelling_state: {
                u.close_prompt_enabled: False,
                u.current_spelling_input_value: '',
                u.spelling_list: [],
                u.waiting_message: None,
                u.saved_spelling_fields: [],
                u.saved_spelling_values: []
            },
            machine_parameters: {
                u.submit_done: False,
                u.reset_alarm_enabled: False,
                u.submit_alarm_enabled: False,
                u.possible_next_action: None,
                u.warning_message: ''
            }
        },
        test_case_message: {
            entities: [
                {
                    entity: input_field,
                    value: password
                },
                {
                    entity: input_value,
                    value: 'pq88W0r9'
                },
                {
                    entity: input_field,
                    value: email_address
                },
                {
                    entity: input_field,
                    value: mark
                }
            ],
            intent: {
                name: complete_field,
                confidence: 1
            },
            text: 'the password is pq88W0r9, i would like to complete the email address and the mark too'
        },
        result_expected: 'The password is updated, email address and mark have not been taken into consideration. insert the value of the emmail address'
    },
    {
        message_id: "090",
        test_form_number: 1,
        initial_state: {
            u.slots: [
                {
                    u.slot_name: first_name,
                    u.slot_value: None
                },
                {
                    u.slot_name: last_name,
                    u.slot_value: None
                },
                {
                    u.slot_name: mark,
                    u.slot_value: None
                },
                {
                    u.slot_name: password,
                    u.slot_value: None
                },
                {
                    u.slot_name: email_address,
                    u.slot_value: None
                }
            ],
            spelling_state: {
                u.close_prompt_enabled: False,
                u.current_spelling_input_value: '',
                u.spelling_list: [],
                u.waiting_message: None,
                u.saved_spelling_fields: [],
                u.saved_spelling_values: []
            },
            machine_parameters: {
                u.submit_done: False,
                u.reset_alarm_enabled: False,
                u.submit_alarm_enabled: False,
                u.possible_next_action: None,
                u.warning_message: ''
            }
        },
        test_case_message: {
            entities: [
                {
                    entity: input_field,
                    value: mark
                },
                {
                    entity: input_value,
                    value: "18"
                },
                {
                    entity: input_value,
                    value: 'pass_w0r8'
                },
                {
                    entity: input_value,
                    value: 'email_address@mail.com'
                }
            ],
            intent: {
                name: complete_field,
                confidence: 1
            },
            text: 'the mark is 18, insert the values pass_w0r8 and email_address@mail.com'
        },
        result_expected: 'The mark is updated, pass_w0r8 and email_address@mail.com ot taken into consideration. the next field is password'
    },
    {
        message_id: "091",
        test_form_number: 1,
        initial_state: {
            u.slots: [
                {
                    u.slot_name: first_name,
                    u.slot_value: 'alexander'
                },
                {
                    u.slot_name: last_name,
                    u.slot_value: 'brown'
                },
                {
                    u.slot_name: mark,
                    u.slot_value: None
                },
                {
                    u.slot_name: password,
                    u.slot_value: None
                },
                {
                    u.slot_name: email_address,
                    u.slot_value: None
                }
            ],
            spelling_state: {
                u.close_prompt_enabled: False,
                u.current_spelling_input_value: '',
                u.spelling_list: [],
                u.waiting_message: None,
                u.saved_spelling_fields: [],
                u.saved_spelling_values: []
            },
            machine_parameters: {
                u.submit_done: False,
                u.reset_alarm_enabled: False,
                u.submit_alarm_enabled: False,
                u.possible_next_action: complete_field,
                u.warning_message: ''
            }
        },
        test_case_message: {
            entities: [],
            intent: {
                name: deny,
                confidence: 1
            },
            text: "no i don't"
        },
        result_expected: 'Could you precise the action you would like to perform?'
    },
    {
        message_id: "092",
        test_form_number: 1,
        initial_state: {
            u.slots: [
                {
                    u.slot_name: first_name,
                    u.slot_value: None
                },
                {
                    u.slot_name: last_name,
                    u.slot_value: None
                },
                {
                    u.slot_name: mark,
                    u.slot_value: None
                },
                {
                    u.slot_name: password,
                    u.slot_value: None
                },
                {
                    u.slot_name: email_address,
                    u.slot_value: None
                }
            ],
            spelling_state: {
                u.close_prompt_enabled: False,
                u.current_spelling_input_value: '',
                u.spelling_list: [first_name],
                u.waiting_message: None,
                u.saved_spelling_fields: [],
                u.saved_spelling_values: []
            },
            machine_parameters: {
                u.submit_done: False,
                u.reset_alarm_enabled: False,
                u.submit_alarm_enabled: False,
                u.possible_next_action: spelling,
                u.warning_message: ''
            }
        },
        test_case_message: {
            entities: [],
            intent: {
                name: deny,
                confidence: 1
            },
            text: 'no'
        },
        result_expected: 'could you precise the action that you would like to perform?'
    },
    {
        message_id: "093",
        test_form_number: 1,
        initial_state: {
            u.slots: [
                {
                    u.slot_name: first_name,
                    u.slot_value: None
                },
                {
                    u.slot_name: last_name,
                    u.slot_value: None
                },
                {
                    u.slot_name: mark,
                    u.slot_value: None
                },
                {
                    u.slot_name: password,
                    u.slot_value: None
                },
                {
                    u.slot_name: email_address,
                    u.slot_value: None
                }
            ],
            spelling_state: {
                u.close_prompt_enabled: True,
                u.current_spelling_input_value: 'adam',
                u.spelling_list: [first_name],
                u.waiting_message: None,
                u.saved_spelling_fields: [],
                u.saved_spelling_values: []
            },
            machine_parameters: {
                u.submit_done: False,
                u.reset_alarm_enabled: False,
                u.submit_alarm_enabled: False,
                u.possible_next_action: None,
                u.warning_message: ''
            }
        },
        test_case_message: {
            entities: [],
            intent: {
                name: deny,
                confidence: 1
            },
            text: 'no'
        },
        result_expected: 'Would you like to save the spelling data?'
    },
    {
        message_id: "094",
        test_form_number: 1,
        initial_state: {
            u.slots: [
                {
                    u.slot_name: first_name,
                    u.slot_value: 'rob'
                },
                {
                    u.slot_name: last_name,
                    u.slot_value: 'sunday'
                },
                {
                    u.slot_name: mark,
                    u.slot_value: '27'
                },
                {
                    u.slot_name: password,
                    u.slot_value: None
                },
                {
                    u.slot_name: email_address,
                    u.slot_value: None
                }
            ],
            spelling_state: {
                u.close_prompt_enabled: False,
                u.spelling_interrupted: False,
                u.current_spelling_input_value: '',
                u.spelling_list: [],
                u.waiting_message: None,
                u.saved_spelling_fields: [],
                u.saved_spelling_values: []
            },
            machine_parameters: {
                u.submit_done: False,
                u.reset_alarm_enabled: True,
                u.submit_alarm_enabled: False,
                u.possible_next_action: None,
                u.warning_message: ''
            }
        },
        test_case_message: {
            entities: [],
            intent: {
                name: deny,
                confidence: 1
            },
            text: 'no'
        },
        result_expected: 'next field is password, no modification of the actual fields, alarm disabled'
    },
    {
        message_id: "095",
        test_form_number: 1,
        initial_state: {
            u.slots: [
                {
                    u.slot_name: first_name,
                    u.slot_value: 'mody'
                },
                {
                    u.slot_name: last_name,
                    u.slot_value: 'friz'
                },
                {
                    u.slot_name: mark,
                    u.slot_value: '22'
                },
                {
                    u.slot_name: password,
                    u.slot_value: None
                },
                {
                    u.slot_name: email_address,
                    u.slot_value: 'johm@ala.net'
                }
            ],
            spelling_state: {
                u.close_prompt_enabled: False,
                u.current_spelling_input_value: '',
                u.spelling_list: [],
                u.waiting_message: None,
                u.saved_spelling_fields: [],
                u.saved_spelling_values: []
            },
            machine_parameters: {
                u.submit_done: False,
                u.reset_alarm_enabled: False,
                u.submit_alarm_enabled: False,
                u.possible_next_action: submit_form,
                u.warning_message: ''
            }
        },
        test_case_message: {
            entities: [],
            intent: {
                name: deny,
                confidence: 1
            },
            text: 'no, i prefer not'
        },
        result_expected: 'The next field is password, alarm desabled'
    },
    {
        message_id: "096",
        test_form_number: 1,
        initial_state: {
            u.slots: [
                {
                    u.slot_name: first_name,
                    u.slot_value: None
                },
                {
                    u.slot_name: last_name,
                    u.slot_value: None
                },
                {
                    u.slot_name: mark,
                    u.slot_value: None
                },
                {
                    u.slot_name: password,
                    u.slot_value: None
                }
            ],
            spelling_state: {
                u.close_prompt_enabled: False,
                u.current_spelling_input_value: '',
                u.spelling_list: [],
                u.waiting_message: None,
                u.saved_spelling_fields: [],
                u.saved_spelling_values: []
            },
            machine_parameters: {
                u.submit_done: False,
                u.reset_alarm_enabled: False,
                u.submit_alarm_enabled: False,
                u.possible_next_action: None,
                u.warning_message: ''
            }
        },
        test_case_message: {
            entities: [
                {
                    entity: input_field,
                    value: arrival_time
                },
                {
                    entity: input_value,
                    value: '08:05 am'
                }
            ],
            intent: {
                name: complete_field,
                confidence: 1
            },
            text: 'What is this form about?'
        },
        result_expected: 'This form does not have any explanation'
    },
    {
        message_id: "097",
        test_form_number: 1,
        initial_state: {
            u.slots: [
                {
                    u.slot_name: first_name,
                    u.slot_value: 'roman'
                },
                {
                    u.slot_name: last_name,
                    u.slot_value: 'mathiew'
                },
                {
                    u.slot_name: mark,
                    u.slot_value: None
                },
                {
                    u.slot_name: password,
                    u.slot_value: None
                },
                {
                    u.slot_name: email_address,
                    u.slot_value: 'mathiew@kenyan.uk'
                }
            ],
            spelling_state: {
                u.close_prompt_enabled: False,
                u.current_spelling_input_value: '',
                u.spelling_list: [],
                u.waiting_message: None,
                u.saved_spelling_fields: [],
                u.saved_spelling_values: []
            },
            machine_parameters: {
                u.submit_done: False,
                u.reset_alarm_enabled: False,
                u.submit_alarm_enabled: False,
                u.possible_next_action: None,
                u.warning_message: ''
            }
        },
        test_case_message: {
            entities: [],
            intent: {
                name: submit_form,
                confidence: 1
            },
            text: 'may i submit?'
        },
        result_expected: 'we are about to submit, do you confirm?'
    },
    {
        message_id: "098",
        test_form_number: 1,
        initial_state: {
            u.slots: [
                {
                    u.slot_name: first_name,
                    u.slot_value: 'beta'
                },
                {
                    u.slot_name: last_name,
                    u.slot_value: 'free'
                },
                {
                    u.slot_name: mark,
                    u.slot_value: None
                },
                {
                    u.slot_name: password,
                    u.slot_value: None
                },
                {
                    u.slot_name: email_address,
                    u.slot_value: None
                }
            ],
            spelling_state: {
                u.close_prompt_enabled: False,
                u.current_spelling_input_value: '',
                u.spelling_list: [],
                u.waiting_message: None,
                u.saved_spelling_fields: [],
                u.saved_spelling_values: []
            },
            machine_parameters: {
                u.submit_done: False,
                u.reset_alarm_enabled: False,
                u.submit_alarm_enabled: False,
                u.possible_next_action: None,
                u.warning_message: ''
            }
        },
        test_case_message: {
            entities: [],
            intent: {
                name: submit_form,
                confidence: 1
            },
            text: 'i want to submit'
        },
        result_expected: 'Not all the required fields are completed, you still have to fill the email address'
    },
    {
        message_id: "099",
        test_form_number: 1,
        initial_state: {
            u.slots: [
                {
                    u.slot_name: first_name,
                    u.slot_value: 'berty'
                },
                {
                    u.slot_name: last_name,
                    u.slot_value: 'ngono'
                },
                {
                    u.slot_name: mark,
                    u.slot_value: '21'
                },
                {
                    u.slot_name: password,
                    u.slot_value: None
                },
                {
                    u.slot_name: email_address,
                    u.slot_value: None
                }
            ],
            spelling_state: {
                u.close_prompt_enabled: False,
                u.current_spelling_input_value: '',
                u.spelling_list: [],
                u.waiting_message: None,
                u.saved_spelling_fields: [],
                u.saved_spelling_values: []
            },
            machine_parameters: {
                u.submit_done: False,
                u.reset_alarm_enabled: False,
                u.submit_alarm_enabled: False,
                u.possible_next_action: None,
                u.warning_message: ''
            }
        },
        test_case_message: {
            entities: [],
            intent: {
                name: reset_all_fields,
                confidence: 1
            },
            text: 'i want to restart from the beginning'
        },
        result_expected: 'reset alarm is enabled. We are going to reset, do you confirm the action?'
    },
    {
        message_id: "100",
        test_form_number: 1,
        initial_state: {
            u.slots: [
                {
                    u.slot_name: first_name,
                    u.slot_value: 'edgar'
                },
                {
                    u.slot_name: last_name,
                    u.slot_value: 'bolsonaro'
                },
                {
                    u.slot_name: mark,
                    u.slot_value: None
                },
                {
                    u.slot_name: password,
                    u.slot_value: 'hinhan+wer'
                },
                {
                    u.slot_name: email_address,
                    u.slot_value: None
                }
            ],
            spelling_state: {
                u.close_prompt_enabled: False,
                u.current_spelling_input_value: '',
                u.spelling_list: [],
                u.waiting_message: None,
                u.saved_spelling_fields: [],
                u.saved_spelling_values: []
            },
            machine_parameters: {
                u.submit_done: False,
                u.reset_alarm_enabled: True,
                u.submit_alarm_enabled: False,
                u.possible_next_action: None,
                u.warning_message: ''
            }
        },
        test_case_message: {
            entities: [],
            intent: {
                name: reset_all_fields,
                confidence: 1
            },
            text: 'I want to reset all the fields'
        },
        result_expected: 'All the fields reset'
    },
    {
        message_id: "101",
        test_form_number: 1,
        initial_state: {
            u.slots: [
                {
                    u.slot_name: first_name,
                    u.slot_value: None
                },
                {
                    u.slot_name: last_name,
                    u.slot_value: None
                },
                {
                    u.slot_name: mark,
                    u.slot_value: None
                },
                {
                    u.slot_name: password,
                    u.slot_value: None
                },
                {
                    u.slot_name: email_address,
                    u.slot_value: None
                }
            ],
            spelling_state: {
                u.close_prompt_enabled: True,
                u.current_spelling_input_value: 'ad',
                u.spelling_list: [first_name],
                u.waiting_message: None,
                u.saved_spelling_fields: [],
                u.saved_spelling_values: []
            },
            machine_parameters: {
                u.submit_done: False,
                u.reset_alarm_enabled: False,
                u.submit_alarm_enabled: False,
                u.possible_next_action: spelling,
                u.warning_message: ''
            }
        },
        test_case_message: {
            entities: [
                {
                    entity: spelling,
                    value: 'a'
                }
            ],
            intent: {
                name: spelling,
                confidence: 1
            },
            text: 'a'
        },
        result_expected: 'current spelling string: ada. Insert the next character'
    },
    {
        message_id: "102",
        test_form_number: 1,
        initial_state: {
            u.slots: [
                {
                    u.slot_name: first_name,
                    u.slot_value: 'anna'
                },
                {
                    u.slot_name: last_name,
                    u.slot_value: 'richards'
                },
                {
                    u.slot_name: mark,
                    u.slot_value: '20'
                },
                {
                    u.slot_name: password,
                    u.slot_value: 'ombrella'
                },
                {
                    u.slot_name: email_address,
                    u.slot_value: None
                }
            ],
            spelling_state: {
                u.close_prompt_enabled: True,
                u.current_spelling_input_value: 'en',
                u.spelling_list: [email_address],
                u.waiting_message: None,
                u.saved_spelling_fields: [],
                u.saved_spelling_values: []
            },
            machine_parameters: {
                u.submit_done: False,
                u.reset_alarm_enabled: False,
                u.submit_alarm_enabled: False,
                u.possible_next_action: None,
                u.warning_message: ''
            }
        },
        test_case_message: {
            entities: [
                {
                    entity: input_value,
                    value: 1
                }
            ],
            intent: {
                name: spelling,
                confidence: 1
            },
            text: '1'
        },
        result_expected: 'the current spelling value: en1. Insert the next character'
    },
    {
        message_id: "103",
        test_form_number: 1,
        initial_state: {
            u.slots: [
                {
                    u.slot_name: first_name,
                    u.slot_value: 'anna'
                },
                {
                    u.slot_name: last_name,
                    u.slot_value: 'richards'
                },
                {
                    u.slot_name: mark,
                    u.slot_value: '20'
                },
                {
                    u.slot_name: password,
                    u.slot_value: 'ombrella'
                },
                {
                    u.slot_name: email_address,
                    u.slot_value: None
                }
            ],
            spelling_state: {
                u.close_prompt_enabled: True,
                u.current_spelling_input_value: 'en',
                u.spelling_list: [email_address],
                u.waiting_message: None,
                u.saved_spelling_fields: [],
                u.saved_spelling_values: []
            },
            machine_parameters: {
                u.submit_done: False,
                u.reset_alarm_enabled: False,
                u.submit_alarm_enabled: False,
                u.possible_next_action: None,
                u.warning_message: ''
            }
        },
        test_case_message: {
            entities: [
                {
                    entity: input_value,
                    value: 98
                }
            ],
            intent: {
                name: spelling,
                confidence: 1
            },
            text: '98'
        },
        result_expected: 'the current spelling value: en98. Insert the next character'
    },
    {
        message_id: "104",
        test_form_number: 1,
        initial_state: {
            u.slots: [
                {
                    u.slot_name: first_name,
                    u.slot_value: 'anna'
                },
                {
                    u.slot_name: last_name,
                    u.slot_value: 'richards'
                },
                {
                    u.slot_name: mark,
                    u.slot_value: '20'
                },
                {
                    u.slot_name: password,
                    u.slot_value: 'ombrella'
                },
                {
                    u.slot_name: email_address,
                    u.slot_value: None
                }
            ],
            spelling_state: {
                u.close_prompt_enabled: True,
                u.current_spelling_input_value: 'en',
                u.spelling_list: [email_address],
                u.waiting_message: None,
                u.saved_spelling_fields: [],
                u.saved_spelling_values: []
            },
            machine_parameters: {
                u.submit_done: False,
                u.reset_alarm_enabled: False,
                u.submit_alarm_enabled: False,
                u.possible_next_action: None,
                u.warning_message: ''
            }
        },
        test_case_message: {
            entities: [
                {
                    entity: input_value,
                    value: 348
                }
            ],
            intent: {
                name: spelling,
                confidence: 1
            },
            text: '348'
        },
        result_expected: 'the current spelling value: en348. Insert the next character'
    },
    {
        message_id: "105",
        test_form_number: 1,
        initial_state: {
            u.slots: [
                {
                    u.slot_name: first_name,
                    u.slot_value: 'anna'
                },
                {
                    u.slot_name: last_name,
                    u.slot_value: 'richards'
                },
                {
                    u.slot_name: mark,
                    u.slot_value: '20'
                },
                {
                    u.slot_name: password,
                    u.slot_value: 'ombrella'
                },
                {
                    u.slot_name: email_address,
                    u.slot_value: None
                }
            ],
            spelling_state: {
                u.close_prompt_enabled: True,
                u.current_spelling_input_value: 'en',
                u.spelling_list: [email_address],
                u.waiting_message: None,
                u.saved_spelling_fields: [],
                u.saved_spelling_values: []
            },
            machine_parameters: {
                u.submit_done: False,
                u.reset_alarm_enabled: False,
                u.submit_alarm_enabled: False,
                u.possible_next_action: None,
                u.warning_message: ''
            }
        },
        test_case_message: {
            entities: [
                {
                    entity: spelling,
                    value: 'at'
                }
            ],
            intent: {
                name: spelling,
                confidence: 1
            },
            text: 'at'
        },
        result_expected: 'the current spelling value: en@. Insert the next character'
    },
    {
        message_id: "106",
        test_form_number: 1,
        initial_state: {
            u.slots: [
                {
                    u.slot_name: first_name,
                    u.slot_value: 'anna'
                },
                {
                    u.slot_name: last_name,
                    u.slot_value: 'richards'
                },
                {
                    u.slot_name: mark,
                    u.slot_value: '20'
                },
                {
                    u.slot_name: password,
                    u.slot_value: 'ombrella'
                },
                {
                    u.slot_name: email_address,
                    u.slot_value: None
                }
            ],
            spelling_state: {
                u.close_prompt_enabled: True,
                u.current_spelling_input_value: 'en',
                u.spelling_list: [email_address],
                u.waiting_message: None,
                u.saved_spelling_fields: [],
                u.saved_spelling_values: []
            },
            machine_parameters: {
                u.submit_done: False,
                u.reset_alarm_enabled: False,
                u.submit_alarm_enabled: False,
                u.possible_next_action: None,
                u.warning_message: ''
            }
        },
        test_case_message: {
            entities: [
                {
                    entity: spelling,
                    value: '@'
                }
            ],
            intent: {
                name: spelling,
                confidence: 1
            },
            text: '@'
        },
        result_expected: 'the current spelling value: en@. Insert the next character'
    },
    {
        message_id: "107",
        test_form_number: 1,
        initial_state: {
            u.slots: [
                {
                    u.slot_name: first_name,
                    u.slot_value: 'anna'
                },
                {
                    u.slot_name: last_name,
                    u.slot_value: 'richards'
                },
                {
                    u.slot_name: mark,
                    u.slot_value: '20'
                },
                {
                    u.slot_name: password,
                    u.slot_value: 'ombrella'
                },
                {
                    u.slot_name: email_address,
                    u.slot_value: None
                }
            ],
            spelling_state: {
                u.close_prompt_enabled: True,
                u.current_spelling_input_value: 'en',
                u.spelling_list: [email_address],
                u.waiting_message: None,
                u.saved_spelling_fields: [],
                u.saved_spelling_values: []
            },
            machine_parameters: {
                u.submit_done: False,
                u.reset_alarm_enabled: False,
                u.submit_alarm_enabled: False,
                u.possible_next_action: None,
                u.warning_message: ''
            }
        },
        test_case_message: {
            entities: [
                {
                    entity: spelling,
                    value: '('
                }
            ],
            intent: {
                name: spelling,
                confidence: 1
            },
            text: '('
        },
        result_expected: 'the current spelling value: en. Character not accepted. Insert the next character'
    },
    {
        message_id: "108",
        test_form_number: 1,
        initial_state: {
            u.slots: [
                {
                    u.slot_name: first_name,
                    u.slot_value: 'alan'
                },
                {
                    u.slot_name: last_name,
                    u.slot_value: 'demur'
                },
                {
                    u.slot_name: mark,
                    u.slot_value: '18'
                },
                {
                    u.slot_name: password,
                    u.slot_value: None
                },
                {
                    u.slot_name: email_address,
                    u.slot_value: None
                }
            ],
            spelling_state: {
                u.close_prompt_enabled: False,
                u.current_spelling_input_value: '',
                u.spelling_list: [],
                u.waiting_message: None,
                u.saved_spelling_fields: [],
                u.saved_spelling_values: []
            },
            machine_parameters: {
                u.submit_done: False,
                u.reset_alarm_enabled: False,
                u.submit_alarm_enabled: False,
                u.possible_next_action: None,
                u.warning_message: ''
            }
        },
        test_case_message: {
            entities: [],
            intent: {
                name: modify_value_field,
                confidence: 1
            },
            text: 'i want to modify a field'
        },
        result_expected: 'which field do you want to modify and which value for it?'
    },
    {
        message_id: "109",
        test_form_number: 1,
        initial_state: {
            u.slots: [
                {
                    u.slot_name: first_name,
                    u.slot_value: 'vincent'
                },
                {
                    u.slot_name: last_name,
                    u.slot_value: 'eliot'
                },
                {
                    u.slot_name: mark,
                    u.slot_value: None
                },
                {
                    u.slot_name: password,
                    u.slot_value: None
                },
                {
                    u.slot_name: email_address,
                    u.slot_value: None
                }
            ],
            spelling_state: {
                u.close_prompt_enabled: False,
                u.current_spelling_input_value: '',
                u.spelling_list: [],
                u.waiting_message: None,
                u.saved_spelling_fields: [],
                u.saved_spelling_values: []
            },
            machine_parameters: {
                u.submit_done: False,
                u.reset_alarm_enabled: False,
                u.submit_alarm_enabled: False,
                u.possible_next_action: None,
                u.warning_message: ''
            }
        },
        test_case_message: {
            entities: [
                {
                    entity: input_field,
                    value: first_name
                }
            ],
            intent: {
                name: modify_value_field,
                confidence: 1
            },
            text: 'i want to change the first name'
        },
        result_expected: 'Insert the value of the first name'
    },
    {
        message_id: "110",
        test_form_number: 1,
        initial_state: {
            u.slots: [
                {
                    u.slot_name: first_name,
                    u.slot_value: 'henry'
                },
                {
                    u.slot_name: last_name,
                    u.slot_value: 'gomez'
                },
                {
                    u.slot_name: mark,
                    u.slot_value: '22'
                },
                {
                    u.slot_name: password,
                    u.slot_value: None
                },
                {
                    u.slot_name: email_address,
                    u.slot_value: None
                }
            ],
            spelling_state: {
                u.close_prompt_enabled: False,
                u.current_spelling_input_value: '',
                u.spelling_list: [],
                u.waiting_message: None,
                u.saved_spelling_fields: [],
                u.saved_spelling_values: []
            },
            machine_parameters: {
                u.submit_done: False,
                u.reset_alarm_enabled: False,
                u.submit_alarm_enabled: False,
                u.possible_next_action: None,
                u.warning_message: ''
            }
        },
        test_case_message: {
            entities: [
                {
                    entity: input_field,
                    value: first_name
                },
                {
                    entity: input_field,
                    value: mark
                }
            ],
            intent: {
                name: modify_value_field,
                confidence: 1
            },
            text: 'modify the first name and the mark'
        },
        result_expected: 'Insert the value of the first name'
    },
    {
        message_id: "111",
        test_form_number: 1,
        initial_state: {
            u.slots: [
                {
                    u.slot_name: first_name,
                    u.slot_value: 'alfred'
                },
                {
                    u.slot_name: last_name,
                    u.slot_value: 'sacker'
                },
                {
                    u.slot_name: mark,
                    u.slot_value: '27'
                },
                {
                    u.slot_name: password,
                    u.slot_value: None
                },
                {
                    u.slot_name: email_address,
                    u.slot_value: None
                }
            ],
            spelling_state: {
                u.close_prompt_enabled: False,
                u.current_spelling_input_value: '',
                u.spelling_list: [],
                u.waiting_message: None,
                u.saved_spelling_fields: [],
                u.saved_spelling_values: []
            },
            machine_parameters: {
                u.submit_done: False,
                u.reset_alarm_enabled: False,
                u.submit_alarm_enabled: False,
                u.possible_next_action: None,
                u.warning_message: ''
            }
        },
        test_case_message: {
            entities: [
                {
                    entity: input_field,
                    value: mark
                },
                {
                    entity: input_value,
                    value: '30'
                }
            ],
            intent: {
                name: modify_value_field,
                confidence: 1
            },
            text: 'i want to modify the mark, inserting 30'
        },
        result_expected: 'The mark becomes 30, The next field is password.'
    },
    {
        message_id: "112",
        test_form_number: 1,
        initial_state: {
            u.slots: [
                {
                    u.slot_name: first_name,
                    u.slot_value: 'dummy'
                },
                {
                    u.slot_name: last_name,
                    u.slot_value: 'season'
                },
                {
                    u.slot_name: mark,
                    u.slot_value: None
                },
                {
                    u.slot_name: password,
                    u.slot_value: 'pwd98star'
                },
                {
                    u.slot_name: email_address,
                    u.slot_value: None
                }
            ],
            spelling_state: {
                u.close_prompt_enabled: False,
                u.current_spelling_input_value: '',
                u.spelling_list: [],
                u.waiting_message: None,
                u.saved_spelling_fields: [],
                u.saved_spelling_values: []
            },
            machine_parameters: {
                u.submit_done: False,
                u.reset_alarm_enabled: False,
                u.submit_alarm_enabled: False,
                u.possible_next_action: None,
                u.warning_message: ''
            }
        },
        test_case_message: {
            entities: [
                {
                    entity: input_field,
                    value: password
                },
                {
                    entity: input_value,
                    value: 'my_pwd98stra'
                },
                {
                    entity: input_field,
                    value: mark
                },
                {
                    entity: input_field,
                    value: email_address
                }
            ],
            intent: {
                name: modify_value_field,
                confidence: 1
            },
            text: 'modify the password and insert my_pwd98stra, modify also the mark and the email address'
        },
        result_expected: 'password modified, the next field is mark'
    },
    {
        message_id: "113",
        test_form_number: 1,
        initial_state: {
            u.slots: [
                {
                    u.slot_name: first_name,
                    u.slot_value: None
                },
                {
                    u.slot_name: last_name,
                    u.slot_value: None
                },
                {
                    u.slot_name: mark,
                    u.slot_value: '19'
                },
                {
                    u.slot_name: password,
                    u.slot_value: 'pourtine'
                },
                {
                    u.slot_name: email_address,
                    u.slot_value: None
                }
            ],
            spelling_state: {
                u.close_prompt_enabled: False,
                u.current_spelling_input_value: '',
                u.spelling_list: [],
                u.waiting_message: None,
                u.saved_spelling_fields: [],
                u.saved_spelling_values: []
            },
            machine_parameters: {
                u.submit_done: False,
                u.reset_alarm_enabled: False,
                u.submit_alarm_enabled: False,
                u.possible_next_action: None,
                u.warning_message: ''
            }
        },
        test_case_message: {
            entities: [
                {
                    entity: input_field,
                    value: mark
                },
                {
                    entity: input_value,
                    value: '25'
                },
                {
                    entity: input_field,
                    value: password
                },
                {
                    entity: input_value,
                    value: 'new_passw'
                }
            ],
            intent: {
                name: modify_value_field,
                confidence: 1
            },
            text: 'modify the mark with 25 and modify the password with new_passw'
        },
        result_expected: 'The mark and he password are modified. the next field is email address'
    },
    {
        message_id: "114",
        test_form_number: 1,
        initial_state: {
            u.slots: [
                {
                    u.slot_name: first_name,
                    u.slot_value: None
                },
                {
                    u.slot_name: last_name,
                    u.slot_value: 'bradley'
                },
                {
                    u.slot_name: mark,
                    u.slot_value: '30'
                },
                {
                    u.slot_name: password,
                    u.slot_value: None
                },
                {
                    u.slot_name: email_address,
                    u.slot_value: None
                }
            ],
            spelling_state: {
                u.close_prompt_enabled: False,
                u.current_spelling_input_value: '',
                u.spelling_list: [],
                u.waiting_message: None,
                u.saved_spelling_fields: [],
                u.saved_spelling_values: []
            },
            machine_parameters: {
                u.submit_done: False,
                u.reset_alarm_enabled: False,
                u.submit_alarm_enabled: False,
                u.possible_next_action: None,
                u.warning_message: ''
            }
        },
        test_case_message: {
            entities: [],
            intent: {
                name: give_remaining_required_fields,
                confidence: 1
            },
            text: 'which are the remaining required fields?'
        },
        result_expected: 'The remaining required fields are first name and email address. The next field is password'
    },
    {
        message_id: "115",
        test_form_number: 1,
        initial_state: {
            u.slots: [
                {
                    u.slot_name: first_name,
                    u.slot_value: 'ronald'
                },
                {
                    u.slot_name: last_name,
                    u.slot_value: None
                },
                {
                    u.slot_name: mark,
                    u.slot_value: None
                },
                {
                    u.slot_name: password,
                    u.slot_value: None
                },
                {
                    u.slot_name: email_address,
                    u.slot_value: None
                }
            ],
            spelling_state: {
                u.close_prompt_enabled: False,
                u.current_spelling_input_value: '',
                u.spelling_list: [],
                u.waiting_message: None,
                u.saved_spelling_fields: [],
                u.saved_spelling_values: []
            },
            machine_parameters: {
                u.submit_done: False,
                u.reset_alarm_enabled: False,
                u.submit_alarm_enabled: False,
                u.possible_next_action: None,
                u.warning_message: ''
            }
        },
        test_case_message: {
            entities: [],
            intent: {
                name: give_remaining_required_fields,
                confidence: 1
            },
            text: 'which are the required fields that remain to fill?'
        },
        result_expected: 'there is one remaining required fieldand it is email address. The next field is last name'
    },
    {
        message_id: "116",
        test_form_number: 1,
        initial_state: {
            u.slots: [
                {
                    u.slot_name: first_name,
                    u.slot_value: 'wonder'
                },
                {
                    u.slot_name: last_name,
                    u.slot_value: None
                },
                {
                    u.slot_name: mark,
                    u.slot_value: None
                },
                {
                    u.slot_name: password,
                    u.slot_value: None
                },
                {
                    u.slot_name: email_address,
                    u.slot_value: 'won@der.com'
                }
            ],
            spelling_state: {
                u.close_prompt_enabled: False,
                u.current_spelling_input_value: '',
                u.spelling_list: [],
                u.waiting_message: None,
                u.saved_spelling_fields: [],
                u.saved_spelling_values: []
            },
            machine_parameters: {
                u.submit_done: False,
                u.reset_alarm_enabled: False,
                u.submit_alarm_enabled: False,
                u.possible_next_action: None,
                u.warning_message: ''
            }
        },
        test_case_message: {
            entities: [],
            intent: {
                name: give_remaining_required_fields,
                confidence: 1
            },
            text: 'please i would like to know the remaining requiered fields'
        },
        result_expected: 'There is no requiered field remaining. The next field is last name'
    },
    {
        message_id: "117",
        test_form_number: 1,
        initial_state: {
            u.slots: [
                {
                    u.slot_name: first_name,
                    u.slot_value: None
                },
                {
                    u.slot_name: last_name,
                    u.slot_value: None
                },
                {
                    u.slot_name: mark,
                    u.slot_value: None
                },
                {
                    u.slot_name: password,
                    u.slot_value: None
                },
                {
                    u.slot_name: email_address,
                    u.slot_value: None
                }
            ],
            spelling_state: {
                u.close_prompt_enabled: False,
                u.current_spelling_input_value: '',
                u.spelling_list: [],
                u.waiting_message: None,
                u.saved_spelling_fields: [],
                u.saved_spelling_values: []
            },
            machine_parameters: {
                u.submit_done: False,
                u.reset_alarm_enabled: False,
                u.submit_alarm_enabled: False,
                u.possible_next_action: None,
                u.warning_message: ''
            }
        },
        test_case_message: {
            entities: [],
            intent: {
                name: repeat_required_fields,
                confidence: 1
            },
            text: 'could you please repeat the required fields?'
        },
        result_expected: 'The required fields are first name and email address. The next field is first name'
    },
    {
        message_id: "118",
        test_form_number: 2,
        initial_state: {
            u.slots: [
                {
                    u.slot_name: birthday,
                    u.slot_value: '12-04-1992'
                },
                {
                    u.slot_name: phone_number,
                    u.slot_value: '1040059566'
                },
                {
                    u.slot_name: number_persons,
                    u.slot_value: '3'
                },
                {
                    u.slot_name: arrival_time,
                    u.slot_value: None
                }
            ],
            spelling_state: {
                u.close_prompt_enabled: False,
                u.current_spelling_input_value: '',
                u.spelling_list: [],
                u.waiting_message: None,
                u.saved_spelling_fields: [],
                u.saved_spelling_values: []
            },
            machine_parameters: {
                u.submit_done: False,
                u.reset_alarm_enabled: False,
                u.submit_alarm_enabled: False,
                u.possible_next_action: None,
                u.warning_message: ''
            }
        },
        test_case_message: {
            entities: [],
            intent: {
                name: repeat_value_field,
                confidence: 1
            },
            text: 'What is the value of the field?'
        },
        result_expected: 'Which field are interested into?'
    },
    {
        message_id: "119",
        test_form_number: 2,
        initial_state: {
            u.slots: [
                {
                    u.slot_name: birthday,
                    u.slot_value: '10-09-1988'
                },
                {
                    u.slot_name: phone_number,
                    u.slot_value: '9838743844422'
                },
                {
                    u.slot_name: number_persons,
                    u.slot_value: '2'
                },
                {
                    u.slot_name: arrival_time,
                    u.slot_value: None
                }
            ],
            spelling_state: {
                u.close_prompt_enabled: False,
                u.current_spelling_input_value: '',
                u.spelling_list: [],
                u.waiting_message: None,
                u.saved_spelling_fields: [],
                u.saved_spelling_values: []
            },
            machine_parameters: {
                u.submit_done: False,
                u.reset_alarm_enabled: False,
                u.submit_alarm_enabled: False,
                u.possible_next_action: None,
                u.warning_message: ''
            }
        },
        test_case_message: {
            entities: [
                {
                    entity: input_field,
                    value: phone_number
                }
            ],
            intent: {
                name: repeat_value_field,
                confidence: 1
            },
            text: 'what is the value of the field phone number?'
        },
        result_expected: 'phone number: 9838743844422. The next field is arrvival time'
    },
    {
        message_id: "120",
        test_form_number: 2,
        initial_state: {
            u.slots: [
                {
                    u.slot_name: birthday,
                    u.slot_value: None
                },
                {
                    u.slot_name: phone_number,
                    u.slot_value: None
                },
                {
                    u.slot_name: number_persons,
                    u.slot_value: '2'
                },
                {
                    u.slot_name: arrival_time,
                    u.slot_value: None
                }
            ],
            spelling_state: {
                u.close_prompt_enabled: False,
                u.current_spelling_input_value: '',
                u.spelling_list: [],
                u.waiting_message: None,
                u.saved_spelling_fields: [],
                u.saved_spelling_values: []
            },
            machine_parameters: {
                u.submit_done: False,
                u.reset_alarm_enabled: False,
                u.submit_alarm_enabled: False,
                u.possible_next_action: None,
                u.warning_message: ''
            }
        },
        test_case_message: {
            entities: [
                {
                    entity: input_field,
                    value: number_persons
                },
                {
                    entity: input_field,
                    value: arrival_time
                }
            ],
            intent: {
                name: complete_field,
                confidence: 1
            },
            text: 'What are the values of the fields number of persons and arrival time'
        },
        result_expected: 'nunmber of persons: 2, arrival time: no value. The next field is arrival time'
    },
    {
        message_id: "121",
        test_form_number: 2,
        initial_state: {
            u.slots: [
                {
                    u.slot_name: birthday,
                    u.slot_value: None
                },
                {
                    u.slot_name: phone_number,
                    u.slot_value: None
                },
                {
                    u.slot_name: number_persons,
                    u.slot_value: None
                },
                {
                    u.slot_name: arrival_time,
                    u.slot_value: None
                }
            ],
            spelling_state: {
                u.close_prompt_enabled: False,
                u.current_spelling_input_value: '',
                u.spelling_list: [],
                u.waiting_message: None,
                u.saved_spelling_fields: [],
                u.saved_spelling_values: []
            },
            machine_parameters: {
                u.submit_done: False,
                u.reset_alarm_enabled: False,
                u.submit_alarm_enabled: False,
                u.possible_next_action: None,
                u.warning_message: ''
            }
        },
        test_case_message: {
            entities: [],
            intent: {
                name: repeat_all_fields,
                confidence: 1
            },
            text: 'could you repeat the fields please'
        },
        result_expected: 'The fields are birthday, phone number, number of persons, arrival time. The next field is birthday'
    },
    {
        message_id: "122",
        test_form_number: 2,
        initial_state: {
            u.slots: [
                {
                    u.slot_name: birthday,
                    u.slot_value: None
                },
                {
                    u.slot_name: phone_number,
                    u.slot_value: None
                },
                {
                    u.slot_name: number_persons,
                    u.slot_value: None
                },
                {
                    u.slot_name: arrival_time,
                    u.slot_value: None
                }
            ],
            spelling_state: {
                u.close_prompt_enabled: False,
                u.current_spelling_input_value: '',
                u.spelling_list: [],
                u.waiting_message: None,
                u.saved_spelling_fields: [],
                u.saved_spelling_values: []
            },
            machine_parameters: {
                u.submit_done: False,
                u.reset_alarm_enabled: False,
                u.submit_alarm_enabled: False,
                u.possible_next_action: None,
                u.warning_message: ''
            }
        },
        test_case_message: {
            entities: [],
            intent: {
                name: repeat_required_fields,
                confidence: 1
            },
            text: 'which are the required fields please?'
        },
        result_expected: 'There is no required field in this form. The next field is birthday'
    },
    {
        message_id: "123",
        test_form_number: 2,
        initial_state: {
            u.slots: [
                {
                    u.slot_name: birthday,
                    u.slot_value: None
                },
                {
                    u.slot_name: phone_number,
                    u.slot_value: None
                },
                {
                    u.slot_name: number_persons,
                    u.slot_value: None
                },
                {
                    u.slot_name: arrival_time,
                    u.slot_value: None
                }
            ],
            spelling_state: {
                u.close_prompt_enabled: False,
                u.current_spelling_input_value: '',
                u.spelling_list: [],
                u.waiting_message: None,
                u.saved_spelling_fields: [],
                u.saved_spelling_values: []
            },
            machine_parameters: {
                u.submit_done: False,
                u.reset_alarm_enabled: False,
                u.submit_alarm_enabled: False,
                u.possible_next_action: None,
                u.warning_message: ''
            }
        },
        test_case_message: {
            entities: [],
            intent: {
                name: repeat_optional_fields,
                confidence: 1
            },
            text: 'Which are the optional fields?'
        },
        result_expected: 'The optional fields are birthday, phone number, number of persons, arrival time. The next field is birthday'
    },
    {
        message_id: "124",
        test_form_number: 2,
        initial_state: {
            u.slots: [
                {
                    u.slot_name: birthday,
                    u.slot_value: '02-02-2001'
                },
                {
                    u.slot_name: phone_number,
                    u.slot_value: '5653792873'
                },
                {
                    u.slot_name: number_persons,
                    u.slot_value: '2'
                },
                {
                    u.slot_name: arrival_time,
                    u.slot_value: '05:00'
                }
            ],
            spelling_state: {
                u.close_prompt_enabled: False,
                u.current_spelling_input_value: '',
                u.spelling_list: [],
                u.waiting_message: None,
                u.saved_spelling_fields: [],
                u.saved_spelling_values: []
            },
            machine_parameters: {
                u.submit_done: False,
                u.reset_alarm_enabled: False,
                u.submit_alarm_enabled: False,
                u.possible_next_action: None,
                u.warning_message: ''
            }
        },
        test_case_message: {
            entities: [],
            intent: {
                name: give_all_remaining_fields,
                confidence: 1
            },
            text: 'which are the remaining fields?'
        },
        result_expected: 'There is no remaining field. Here is the recap, do you want to submit?'
    },
    {
        message_id: "125",
        test_form_number: 2,
        initial_state: {
            u.slots: [
                {
                    u.slot_name: birthday,
                    u.slot_value: '03-05-1992'
                },
                {
                    u.slot_name: phone_number,
                    u.slot_value: '1235364321'
                },
                {
                    u.slot_name: number_persons,
                    u.slot_value: None
                },
                {
                    u.slot_name: arrival_time,
                    u.slot_value: '20:28'
                }
            ],
            spelling_state: {
                u.close_prompt_enabled: False,
                u.current_spelling_input_value: '',
                u.spelling_list: [],
                u.waiting_message: None,
                u.saved_spelling_fields: [],
                u.saved_spelling_values: []
            },
            machine_parameters: {
                u.submit_done: False,
                u.reset_alarm_enabled: False,
                u.submit_alarm_enabled: False,
                u.possible_next_action: None,
                u.warning_message: ''
            }
        },
        test_case_message: {
            entities: [],
            intent: {
                name: give_all_remaining_fields,
                confidence: 1
            },
            text: 'Please which re the remaining fields?'
        },
        result_expected: 'There is one remaining field and it is number of persons. The next field is number of persons'
    },
    {
        message_id: "126",
        test_form_number: 2,
        initial_state: {
            u.slots: [
                {
                    u.slot_name: birthday,
                    u.slot_value: None
                },
                {
                    u.slot_name: phone_number,
                    u.slot_value: None
                },
                {
                    u.slot_name: number_persons,
                    u.slot_value: '4'
                },
                {
                    u.slot_name: arrival_time,
                    u.slot_value: '15:46'
                }
            ],
            spelling_state: {
                u.close_prompt_enabled: False,
                u.current_spelling_input_value: '',
                u.spelling_list: [],
                u.waiting_message: None,
                u.saved_spelling_fields: [],
                u.saved_spelling_values: []
            },
            machine_parameters: {
                u.submit_done: False,
                u.reset_alarm_enabled: False,
                u.submit_alarm_enabled: False,
                u.possible_next_action: None,
                u.warning_message: ''
            }
        },
        test_case_message: {
            entities: [],
            intent: {
                name: give_all_remaining_fields,
                confidence: 1
            },
            text: 'please could you give me the remaining fields?'
        },
        result_expected: 'the remaining fields are birthday and phone number. The next field is birthday'
    },
    {
        message_id: "127",
        test_form_number: 2,
        initial_state: {
            u.slots: [
                {
                    u.slot_name: birthday,
                    u.slot_value: '06-07-1999'
                },
                {
                    u.slot_name: phone_number,
                    u.slot_value: None
                },
                {
                    u.slot_name: number_persons,
                    u.slot_value: '3'
                },
                {
                    u.slot_name: arrival_time,
                    u.slot_value: None
                }
            ],
            spelling_state: {
                u.close_prompt_enabled: False,
                u.current_spelling_input_value: '',
                u.spelling_list: [],
                u.waiting_message: None,
                u.saved_spelling_fields: [],
                u.saved_spelling_values: []
            },
            machine_parameters: {
                u.submit_done: False,
                u.reset_alarm_enabled: False,
                u.submit_alarm_enabled: False,
                u.possible_next_action: None,
                u.warning_message: ''
            }
        },
        test_case_message: {
            entities: [],
            intent: {
                name: give_remaining_optional_fields,
                confidence: 1
            },
            text: 'what are the remaining optional fields'
        },
        result_expected: 'The remaining optional fields are phone number and arrival time'
    },
    {
        message_id: "128",
        test_form_number: 2,
        initial_state: {
            u.slots: [
                {
                    u.slot_name: birthday,
                    u.slot_value: None
                },
                {
                    u.slot_name: phone_number,
                    u.slot_value: '983789234180'
                },
                {
                    u.slot_name: number_persons,
                    u.slot_value: '3'
                },
                {
                    u.slot_name: arrival_time,
                    u.slot_value: '13:33'
                }
            ],
            spelling_state: {
                u.close_prompt_enabled: False,
                u.current_spelling_input_value: '',
                u.spelling_list: [],
                u.waiting_message: None,
                u.saved_spelling_fields: [],
                u.saved_spelling_values: []
            },
            machine_parameters: {
                u.submit_done: False,
                u.reset_alarm_enabled: False,
                u.submit_alarm_enabled: False,
                u.possible_next_action: None,
                u.warning_message: ''
            }
        },
        test_case_message: {
            entities: [],
            intent: {
                name: give_remaining_optional_fields,
                confidence: 1
            },
            text: 'which are the remaining fields that are optional'
        },
        result_expected: 'There is one remaining optional field ant it is the birthday. The next field is birthday'
    },
    {
        message_id: "129",
        test_form_number: 2,
        initial_state: {
            u.slots: [
                {
                    u.slot_name: birthday,
                    u.slot_value: '12-07-2010'
                },
                {
                    u.slot_name: phone_number,
                    u.slot_value: '85759849202'
                },
                {
                    u.slot_name: number_persons,
                    u.slot_value: '3'
                },
                {
                    u.slot_name: arrival_time,
                    u.slot_value: '18:30'
                }
            ],
            spelling_state: {
                u.close_prompt_enabled: False,
                u.current_spelling_input_value: '',
                u.spelling_list: [],
                u.waiting_message: None,
                u.saved_spelling_fields: [],
                u.saved_spelling_values: []
            },
            machine_parameters: {
                u.submit_done: False,
                u.reset_alarm_enabled: False,
                u.submit_alarm_enabled: False,
                u.possible_next_action: None,
                u.warning_message: ''
            }
        },
        test_case_message: {
            entities: [],
            intent: {
                name: give_remaining_optional_fields,
                confidence: 1
            },
            text: 'Which are the remaining optional fields?'
        },
        result_expected: 'There is no optional field. Here is the recap, do you want to submit?'
    },
    {
        message_id: "130",
        test_form_number: 2,
        initial_state: {
            u.slots: [
                {
                    u.slot_name: birthday,
                    u.slot_value: '25-07-2003'
                },
                {
                    u.slot_name: phone_number,
                    u.slot_value: None
                },
                {
                    u.slot_name: number_persons,
                    u.slot_value: '3'
                },
                {
                    u.slot_name: arrival_time,
                    u.slot_value: None
                }
            ],
            spelling_state: {
                u.close_prompt_enabled: False,
                u.current_spelling_input_value: '',
                u.spelling_list: [],
                u.waiting_message: None,
                u.saved_spelling_fields: [],
                u.saved_spelling_values: []
            },
            machine_parameters: {
                u.submit_done: False,
                u.reset_alarm_enabled: False,
                u.submit_alarm_enabled: True,
                u.possible_next_action: submit_form,
                u.warning_message: ''
            }
        },
        test_case_message: {
            entities: [],
            intent: {
                name: affirm,
                confidence: 1
            },
            text: 'yes'
        },
        result_expected: 'submit done'
    },
    {
        message_id: "131",
        test_form_number: 3,
        initial_state: {
            u.slots: [
                {
                    u.slot_name: car,
                    u.slot_value: 'volvo'
                },
                {
                    u.slot_name: gender,
                    u.slot_value: 'male'
                },
                {
                    u.slot_name: electronic_devices,
                    u.slot_value: 'smartphone'
                },
                {
                    u.slot_name: message,
                    u.slot_value: None
                }
            ],
            spelling_state: {
                u.close_prompt_enabled: False,
                u.current_spelling_input_value: '',
                u.spelling_list: [],
                u.waiting_message: None,
                u.saved_spelling_fields: [],
                u.saved_spelling_values: []
            },
            machine_parameters: {
                u.submit_done: False,
                u.reset_alarm_enabled: True,
                u.submit_alarm_enabled: False,
                u.possible_next_action: reset_all_fields,
                u.warning_message: ''
            }
        },
        test_case_message: {
            entities: [],
            intent: {
                name: affirm,
                confidence: 1
            },
            text: 'yes'
        },
        result_expected: 'The fields have been reset'
    },
    {
        message_id: "132",
        test_form_number: 3,
        initial_state: {
            u.slots: [
                {
                    u.slot_name: car,
                    u.slot_value: 'kia'
                },
                {
                    u.slot_name: gender,
                    u.slot_value: 'female'
                },
                {
                    u.slot_name: electronic_devices,
                    u.slot_value: None
                },
                {
                    u.slot_name: message,
                    u.slot_value: None
                }
            ],
            spelling_state: {
                u.close_prompt_enabled: False,
                u.current_spelling_input_value: '',
                u.spelling_list: [],
                u.waiting_message: None,
                u.saved_spelling_fields: [],
                u.saved_spelling_values: []
            },
            machine_parameters: {
                u.submit_done: False,
                u.reset_alarm_enabled: False,
                u.submit_alarm_enabled: False,
                u.possible_next_action: None,
                u.warning_message: ''
            }
        },
        test_case_message: {
            entities: [],
            intent: {
                name: repeat_required_fields,
                confidence: 1
            },
            text: 'Could you repeat de required felds please?'
        },
        result_expected: 'There is one required field and it is gender'
    },
    {
        message_id: "133",
        test_form_number: 3,
        initial_state: {
            u.slots: [
                {
                    u.slot_name: car,
                    u.slot_value: 'lexus'
                },
                {
                    u.slot_name: gender,
                    u.slot_value: 'other'
                },
                {
                    u.slot_name: electronic_devices,
                    u.slot_value: None
                },
                {
                    u.slot_name: message,
                    u.slot_value: None
                }
            ],
            spelling_state: {
                u.close_prompt_enabled: False,
                u.current_spelling_input_value: '',
                u.spelling_list: [],
                u.waiting_message: None,
                u.saved_spelling_fields: [],
                u.saved_spelling_values: []
            },
            machine_parameters: {
                u.submit_done: False,
                u.reset_alarm_enabled: False,
                u.submit_alarm_enabled: False,
                u.possible_next_action: None,
                u.warning_message: ''
            }
        },
        test_case_message: {
            entities: [],
            intent: {
                name: skip_field,
                confidence: 1
            },
            text: 'next field please'
        },
        result_expected: 'The next field is message'
    },
    {
        message_id: "134",
        test_form_number: 3,
        initial_state: {
            u.slots: [
                {
                    u.slot_name: car,
                    u.slot_value: None
                },
                {
                    u.slot_name: gender,
                    u.slot_value: None
                },
                {
                    u.slot_name: electronic_devices,
                    u.slot_value: None
                },
                {
                    u.slot_name: message,
                    u.slot_value: None
                }
            ],
            spelling_state: {
                u.close_prompt_enabled: False,
                u.current_spelling_input_value: '',
                u.spelling_list: [],
                u.waiting_message: None,
                u.saved_spelling_fields: [],
                u.saved_spelling_values: []
            },
            machine_parameters: {
                u.submit_done: False,
                u.reset_alarm_enabled: False,
                u.submit_alarm_enabled: False,
                u.possible_next_action: None,
                u.warning_message: ''
            }
        },
        test_case_message: {
            entities: [],
            intent: {
                name: verify_presence_field,
                confidence: 1
            },
            text: 'Is the field universtity present?'
        },
        result_expected: 'The field university is not present . The next field is car'
    },
    {
        message_id: "135",
        test_form_number: 3,
        initial_state: {
            u.slots: [
                {
                    u.slot_name: car,
                    u.slot_value: None
                },
                {
                    u.slot_name: gender,
                    u.slot_value: None
                },
                {
                    u.slot_name: electronic_devices,
                    u.slot_value: None
                },
                {
                    u.slot_name: message,
                    u.slot_value: None
                }
            ],
            spelling_state: {
                u.close_prompt_enabled: False,
                u.current_spelling_input_value: '',
                u.spelling_list: [],
                u.waiting_message: None,
                u.saved_spelling_fields: [],
                u.saved_spelling_values: []
            },
            machine_parameters: {
                u.submit_done: False,
                u.reset_alarm_enabled: False,
                u.submit_alarm_enabled: False,
                u.possible_next_action: None,
                u.warning_message: ''
            }
        },
        test_case_message: {
            entities: [],
            intent: {
                name: verify_presence_field,
                confidence: 1
            },
            text: 'are the fields car and gender present in this form?'
        },
        result_expected: 'Car is present, gender is present. The next field is car'
    },
    {
        message_id: "136",
        test_form_number: 3,
        initial_state: {
            u.slots: [
                {
                    u.slot_name: car,
                    u.slot_value: 'ford'
                },
                {
                    u.slot_name: gender,
                    u.slot_value: 'female'
                },
                {
                    u.slot_name: electronic_devices,
                    u.slot_value: 'computer'
                },
                {
                    u.slot_name: message,
                    u.slot_value: None
                }
            ],
            spelling_state: {
                u.close_prompt_enabled: False,
                u.current_spelling_input_value: '',
                u.spelling_list: [],
                u.waiting_message: None,
                u.saved_spelling_fields: [],
                u.saved_spelling_values: []
            },
            machine_parameters: {
                u.submit_done: False,
                u.reset_alarm_enabled: False,
                u.submit_alarm_enabled: False,
                u.possible_next_action: None,
                u.warning_message: ''
            }
        },
        test_case_message: {
            entities: [
                {
                    entity: input_field,
                    value: car
                }
            ],
            intent: {
                name: verify_value_fields,
                confidence: 1
            },
            text: 'what is the value of the field car'
        },
        result_expected: 'car: ford. The next field is message'
    },
    {
        message_id: "137",
        test_form_number: 3,
        initial_state: {
            u.slots: [
                {
                    u.slot_name: car,
                    u.slot_value: 'fiat'
                },
                {
                    u.slot_name: gender,
                    u.slot_value: 'male'
                },
                {
                    u.slot_name: electronic_devices,
                    u.slot_value: 'computer'
                },
                {
                    u.slot_name: message,
                    u.slot_value: None
                }
            ],
            spelling_state: {
                u.close_prompt_enabled: False,
                u.current_spelling_input_value: '',
                u.spelling_list: [],
                u.waiting_message: None,
                u.saved_spelling_fields: [],
                u.saved_spelling_values: []
            },
            machine_parameters: {
                u.submit_done: False,
                u.reset_alarm_enabled: False,
                u.submit_alarm_enabled: False,
                u.possible_next_action: None,
                u.warning_message: ''
            }
        },
        test_case_message: {
            entities: [],
            intent: {
                name: verify_value_fields,
                confidence: 1
            },
            text: 'What is the value of the field?'
        },
        result_expected: 'To which field are you interested to?'
    },
    {
        message_id: "138",
        test_form_number: 3,
        initial_state: {
            u.slots: [
                {
                    u.slot_name: car,
                    u.slot_value: 'honda'
                },
                {
                    u.slot_name: gender,
                    u.slot_value: 'female'
                },
                {
                    u.slot_name: electronic_devices,
                    u.slot_value: 'smart watch'
                },
                {
                    u.slot_name: message,
                    u.slot_value: None
                }
            ],
            spelling_state: {
                u.close_prompt_enabled: False,
                u.current_spelling_input_value: '',
                u.spelling_list: [],
                u.waiting_message: None,
                u.saved_spelling_fields: [],
                u.saved_spelling_values: []
            },
            machine_parameters: {
                u.submit_done: False,
                u.reset_alarm_enabled: False,
                u.submit_alarm_enabled: False,
                u.possible_next_action: None,
                u.warning_message: ''
            }
        },
        test_case_message: {
            entities: [
                {
                    entity: input_field,
                    value: car
                },
                {
                    entity: input_field,
                    value: gender
                }
            ],
            intent: {
                name: verify_value_fields,
                confidence: 1
            },
            text: 'What is the value of the fields car and gender'
        },
        result_expected: 'Car: honda, gender: female. The next field is message'
    },
    {
        message_id: "139",
        test_form_number: 3,
        initial_state: {
            u.slots: [
                {
                    u.slot_name: car,
                    u.slot_value: 'bmw'
                },
                {
                    u.slot_name: gender,
                    u.slot_value: 'other'
                },
                {
                    u.slot_name: electronic_devices,
                    u.slot_value: None
                },
                {
                    u.slot_name: message,
                    u.slot_value: 'i am happy to be here'
                }
            ],
            spelling_state: {
                u.close_prompt_enabled: False,
                u.current_spelling_input_value: '',
                u.spelling_list: [],
                u.waiting_message: None,
                u.saved_spelling_fields: [],
                u.saved_spelling_values: []
            },
            machine_parameters: {
                u.submit_done: False,
                u.reset_alarm_enabled: False,
                u.submit_alarm_enabled: False,
                u.possible_next_action: None,
                u.warning_message: ''
            }
        },
        test_case_message: {
            entities: [],
            intent: {
                name: repeat_form_title,
                confidence: 1
            },
            text: 'what is the title of this form?'
        },
        result_expected: 'The title is test form sample number 3. The next field is electronic devices'
    },
    {
        message_id: "140",
        test_form_number: 1,
        initial_state: {
            u.slots: [
                {
                    u.slot_name: first_name,
                    u.slot_value: None
                },
                {
                    u.slot_name: last_name,
                    u.slot_value: None
                },
                {
                    u.slot_name: mark,
                    u.slot_value: None
                },
                {
                    u.slot_name: password,
                    u.slot_value: None
                }
            ],
            spelling_state: {
                u.close_prompt_enabled: False,
                u.current_spelling_input_value: '',
                u.spelling_list: [],
                u.waiting_message: None,
                u.saved_spelling_fields: [],
                u.saved_spelling_values: []
            },
            machine_parameters: {
                u.submit_done: False,
                u.reset_alarm_enabled: False,
                u.submit_alarm_enabled: False,
                u.possible_next_action: None,
                u.warning_message: ''
            }
        },
        test_case_message: {
            entities: [],
            intent: {
                name: repeat_form_title,
                confidence: 1
            },
            text: 'Please give me the title of the form'
        },
        result_expected: 'This form does not have a title. The next field is first name.'
    },
    {
        message_id: "141",
        test_form_number: 3,
        initial_state: {
            u.slots: [
                {
                    u.slot_name: car,
                    u.slot_value: None
                },
                {
                    u.slot_name: gender,
                    u.slot_value: None
                },
                {
                    u.slot_name: electronic_devices,
                    u.slot_value: None
                },
                {
                    u.slot_name: message,
                    u.slot_value: None
                }
            ],
            spelling_state: {
                u.close_prompt_enabled: False,
                u.current_spelling_input_value: '',
                u.spelling_list: [],
                u.waiting_message: None,
                u.saved_spelling_fields: [],
                u.saved_spelling_values: []
            },
            machine_parameters: {
                u.submit_done: False,
                u.reset_alarm_enabled: False,
                u.submit_alarm_enabled: False,
                u.possible_next_action: None,
                u.warning_message: ''
            }
        },
        test_case_message: {
            entities: [],
            intent: {
                name: repeat_form_explanation,
                confidence: 1
            },
            text: 'What is this form about?'
        },
        result_expected: 'This form presents various fields ... The next field is car'
    },
    {
        message_id: "142",
        test_form_number: 3,
        initial_state: {
            u.slots: [
                {
                    u.slot_name: car,
                    u.slot_value: None
                },
                {
                    u.slot_name: gender,
                    u.slot_value: None
                },
                {
                    u.slot_name: electronic_devices,
                    u.slot_value: None
                },
                {
                    u.slot_name: message,
                    u.slot_value: None
                }
            ],
            spelling_state: {
                u.close_prompt_enabled: False,
                u.current_spelling_input_value: '',
                u.spelling_list: [],
                u.waiting_message: None,
                u.saved_spelling_fields: [],
                u.saved_spelling_values: []
            },
            machine_parameters: {
                u.submit_done: False,
                u.reset_alarm_enabled: False,
                u.submit_alarm_enabled: False,
                u.possible_next_action: None,
                u.warning_message: ''
            }
        },
        test_case_message: {
            entities: [],
            intent: {
                name: explain_field,
                confidence: 1
            },
            text: 'What is it?'
        },
        result_expected: 'The car brand that you prefer. The next field is car'
    },
    {
        message_id: "143",
        test_form_number: 3,
        initial_state: {
            u.slots: [
                {
                    u.slot_name: car,
                    u.slot_value: None
                },
                {
                    u.slot_name: gender,
                    u.slot_value: None
                },
                {
                    u.slot_name: electronic_devices,
                    u.slot_value: None
                },
                {
                    u.slot_name: message,
                    u.slot_value: None
                }
            ],
            spelling_state: {
                u.close_prompt_enabled: False,
                u.current_spelling_input_value: '',
                u.spelling_list: [],
                u.waiting_message: None,
                u.saved_spelling_fields: [],
                u.saved_spelling_values: []
            },
            machine_parameters: {
                u.submit_done: False,
                u.reset_alarm_enabled: False,
                u.submit_alarm_enabled: False,
                u.possible_next_action: None,
                u.warning_message: ''
            }
        },
        test_case_message: {
            entities: [
                {
                    entity: input_field,
                    value: electronic_devices
                }
            ],
            intent: {
                name: complete_field,
                confidence: 1
            },
            text: 'What is electronic devices?'
        },
        result_expected: 'The electronic devices you own. The next field is car'
    },
    {
        message_id: "144",
        test_form_number: 3,
        initial_state: {
            u.slots: [
                {
                    u.slot_name: car,
                    u.slot_value: None
                },
                {
                    u.slot_name: gender,
                    u.slot_value: None
                },
                {
                    u.slot_name: electronic_devices,
                    u.slot_value: None
                },
                {
                    u.slot_name: message,
                    u.slot_value: None
                }
            ],
            spelling_state: {
                u.close_prompt_enabled: False,
                u.current_spelling_input_value: '',
                u.spelling_list: [],
                u.waiting_message: None,
                u.saved_spelling_fields: [],
                u.saved_spelling_values: []
            },
            machine_parameters: {
                u.submit_done: False,
                u.reset_alarm_enabled: False,
                u.submit_alarm_enabled: False,
                u.possible_next_action: complete_field,
                u.warning_message: ''
            }
        },
        test_case_message: {
            entities: [],
            intent: {
                name: affirm,
                confidence: 1
            },
            text: 'yes'
        },
        result_expected: 'could you precise the action that you want to perform? The next field is car'
    },
    {
        message_id: "145",
        test_form_number: 2,
        initial_state: {
            u.slots: [
                {
                    u.slot_name: phone_number,
                    u.slot_value: None
                },
                {
                    u.slot_name: number_persons,
                    u.slot_value: None
                },
                {
                    u.slot_name: birthday,
                    u.slot_value: None
                },
                {
                    u.slot_name: arrival_time,
                    u.slot_value: None
                }
            ],
            spelling_state: {
                u.close_prompt_enabled: True,
                u.current_spelling_input_value: '354252',
                u.spelling_list: [phone_number],
                u.waiting_message: None,
                u.saved_spelling_fields: [],
                u.saved_spelling_values: []
            },
            machine_parameters: {
                u.submit_done: False,
                u.reset_alarm_enabled: False,
                u.submit_alarm_enabled: False,
                u.possible_next_action: spelling,
                u.warning_message: ''
            }
        },
        test_case_message: {
            entities: [
                {
                    entity: input_value,
                    value: 4
                }
            ],
            intent: {
                name: affirm,
                confidence: 1
            },
            text: 'yes'
        },
        result_expected: 'Do you want to save the spelling information?'
    },
    {
        message_id: "146",
        test_form_number: 2,
        initial_state: {
            u.slots: [
                {
                    u.slot_name: phone_number,
                    u.slot_value: None
                },
                {
                    u.slot_name: number_persons,
                    u.slot_value: None
                },
                {
                    u.slot_name: birthday,
                    u.slot_value: None
                },
                {
                    u.slot_name: arrival_time,
                    u.slot_value: None
                }
            ],
            spelling_state: {
                u.close_prompt_enabled: False,
                u.spelling_interrupted: False,
                u.current_spelling_input_value: '',
                u.spelling_list: [],
                u.waiting_message: None,
                u.saved_spelling_fields: [],
                u.saved_spelling_values: []
            },
            machine_parameters: {
                u.submit_done: False,
                u.reset_alarm_enabled: False,
                u.submit_alarm_enabled: False,
                u.possible_next_action: spelling,
                u.warning_message: ''
            }
        },
        test_case_message: {
            entities: [],
            intent: {
                name: affirm,
                confidence: 1
            },
            text: 'sure i want'
        },
        result_expected: 'Which action exactly do you want to perform?'
    }
]