# structural test cases
import utility as u

# intents
complete_field = 'fillGenericCamp'
affirm = 'affirm'
deny = 'deny'
submit_form = 'submitForm'
reset_all_fields = 'resetAllCamps'
spelling = 'spelling'
modify_value_field = 'modifyValueGenericCamp'
repeat_value_field = 'repeatValueCamp'
repeat_all_fields = 'repeatAllLabels'
repeat_required_fields = 'repeatRequiredLabels'
repeat_optional_fields = 'repeatOptionalLabels'
give_remaining_fields = 'giveAllRemainingLabels'
give_remaining_required_fields = 'giveRemainingRequiredLabels'
give_remaining_optional_fields = 'giveRemainingOptionalLabels'
skip_field = 'skipCamp'
verify_presence_field = 'verifyPresenceOfLabel'
verify_value_fields = 'verifyValueFilledCamps'
repeat_form_explanation = 'repeatFormExplanation'
explain_field = 'explainLabel'

# keys
message_id = "001"
test_form_number = "test_form_number"
initial_state = "initial_situation"
spelling_state = "spelling_state"
machine_parameters = "machine_parameters"
test_case_message = "test_case_message"
result_expected = "result_expected"

entities = "entities"
intent = "intent"
text = "text"

entity = "entity"
value = "value"
name = "name"
confidence = "confidence"

functional = "functional"
structural = "structural"

structural_test_cases = [
    {
        message_id: "000",
        test_form_number: 1,
        initial_state: {
            u.slots: [
                {
                    u.slot_name: "",
                    u.slot_value: ""
                }
            ],
            spelling_state: {
                u.close_prompt_enabled: False,
                u.current_spelling_input_value: '',
                u.spelling_list: [],
                u.waiting_intent: None,
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
                    entity: '',
                    value: ''
                }
            ],
            intent: {
                name: '',
                confidence: 1
            },
            text: ''
        },
        result_expected: ''
    },
    {
        message_id: "001",
        test_form_number: 1,
        initial_state: {
            u.slots: [
                {
                    u.slot_name: "",
                    u.slot_value: ""
                }
            ],
            spelling_state: {
                u.close_prompt_enabled: False,
                u.current_spelling_input_value: '',
                u.spelling_list: [],
                u.waiting_intent: None,
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
                    entity: '',
                    value: ''
                }
            ],
            intent: {
                name: '',
                confidence: 1
            },
            text: ''
        },
        result_expected: ''
    },
    {
        message_id: "002",
        test_form_number: 1,
        initial_state: {
            u.slots: [
                {
                    u.slot_name: "",
                    u.slot_value: ""
                }
            ],
            spelling_state: {
                u.close_prompt_enabled: False,
                u.current_spelling_input_value: '',
                u.spelling_list: [],
                u.waiting_intent: None,
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
                    entity: '',
                    value: ''
                }
            ],
            intent: {
                name: '',
                confidence: 1
            },
            text: ''
        },
        result_expected: ''
    },
    {
        message_id: "003",
        test_form_number: 1,
        initial_state: {
            u.slots: [
                {
                    u.slot_name: "",
                    u.slot_value: ""
                }
            ],
            spelling_state: {
                u.close_prompt_enabled: False,
                u.current_spelling_input_value: '',
                u.spelling_list: [],
                u.waiting_intent: None,
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
                    entity: '',
                    value: ''
                }
            ],
            intent: {
                name: '',
                confidence: 1
            },
            text: ''
        },
        result_expected: ''
    },
    {
        message_id: "004",
        test_form_number: 1,
        initial_state: {
            u.slots: [
                {
                    u.slot_name: "",
                    u.slot_value: ""
                }
            ],
            spelling_state: {
                u.close_prompt_enabled: False,
                u.current_spelling_input_value: '',
                u.spelling_list: [],
                u.waiting_intent: None,
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
                    entity: '',
                    value: ''
                }
            ],
            intent: {
                name: '',
                confidence: 1
            },
            text: ''
        },
        result_expected: ''
    },
    {
        message_id: "005",
        test_form_number: 1,
        initial_state: {
            u.slots: [
                {
                    u.slot_name: "",
                    u.slot_value: ""
                }
            ],
            spelling_state: {
                u.close_prompt_enabled: False,
                u.current_spelling_input_value: '',
                u.spelling_list: [],
                u.waiting_intent: None,
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
                    entity: '',
                    value: ''
                }
            ],
            intent: {
                name: '',
                confidence: 1
            },
            text: ''
        },
        result_expected: ''
    },
    {
        message_id: "006",
        test_form_number: 1,
        initial_state: {
            u.slots: [
                {
                    u.slot_name: "",
                    u.slot_value: ""
                }
            ],
            spelling_state: {
                u.close_prompt_enabled: False,
                u.current_spelling_input_value: '',
                u.spelling_list: [],
                u.waiting_intent: None,
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
                    entity: '',
                    value: ''
                }
            ],
            intent: {
                name: '',
                confidence: 1
            },
            text: ''
        },
        result_expected: ''
    },
    {
        message_id: "007",
        test_form_number: 1,
        initial_state: {
            u.slots: [
                {
                    u.slot_name: "",
                    u.slot_value: ""
                }
            ],
            spelling_state: {
                u.close_prompt_enabled: False,
                u.current_spelling_input_value: '',
                u.spelling_list: [],
                u.waiting_intent: None,
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
                    entity: '',
                    value: ''
                }
            ],
            intent: {
                name: '',
                confidence: 1
            },
            text: ''
        },
        result_expected: ''
    },
    {
        message_id: "008",
        test_form_number: 1,
        initial_state: {
            u.slots: [
                {
                    u.slot_name: "",
                    u.slot_value: ""
                }
            ],
            spelling_state: {
                u.close_prompt_enabled: False,
                u.current_spelling_input_value: '',
                u.spelling_list: [],
                u.waiting_intent: None,
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
                    entity: '',
                    value: ''
                }
            ],
            intent: {
                name: '',
                confidence: 1
            },
            text: ''
        },
        result_expected: ''
    },
    {
        message_id: "009",
        test_form_number: 1,
        initial_state: {
            u.slots: [
                {
                    u.slot_name: "",
                    u.slot_value: ""
                }
            ],
            spelling_state: {
                u.close_prompt_enabled: False,
                u.current_spelling_input_value: '',
                u.spelling_list: [],
                u.waiting_intent: None,
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
                    entity: '',
                    value: ''
                }
            ],
            intent: {
                name: '',
                confidence: 1
            },
            text: ''
        },
        result_expected: ''
    },
    {
        message_id: "010",
        test_form_number: 1,
        initial_state: {
            u.slots: [
                {
                    u.slot_name: "",
                    u.slot_value: ""
                }
            ],
            spelling_state: {
                u.close_prompt_enabled: False,
                u.current_spelling_input_value: '',
                u.spelling_list: [],
                u.waiting_intent: None,
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
                    entity: '',
                    value: ''
                }
            ],
            intent: {
                name: '',
                confidence: 1
            },
            text: ''
        },
        result_expected: ''
    },
    {
        message_id: "011",
        test_form_number: 1,
        initial_state: {
            u.slots: [
                {
                    u.slot_name: "",
                    u.slot_value: ""
                }
            ],
            spelling_state: {
                u.close_prompt_enabled: False,
                u.current_spelling_input_value: '',
                u.spelling_list: [],
                u.waiting_intent: None,
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
                    entity: '',
                    value: ''
                }
            ],
            intent: {
                name: '',
                confidence: 1
            },
            text: ''
        },
        result_expected: ''
    },
    {
        message_id: "012",
        test_form_number: 1,
        initial_state: {
            u.slots: [
                {
                    u.slot_name: "",
                    u.slot_value: ""
                }
            ],
            spelling_state: {
                u.close_prompt_enabled: False,
                u.current_spelling_input_value: '',
                u.spelling_list: [],
                u.waiting_intent: None,
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
                    entity: '',
                    value: ''
                }
            ],
            intent: {
                name: '',
                confidence: 1
            },
            text: ''
        },
        result_expected: ''
    },
    {
        message_id: "013",
        test_form_number: 1,
        initial_state: {
            u.slots: [
                {
                    u.slot_name: "",
                    u.slot_value: ""
                }
            ],
            spelling_state: {
                u.close_prompt_enabled: False,
                u.current_spelling_input_value: '',
                u.spelling_list: [],
                u.waiting_intent: None,
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
                    entity: '',
                    value: ''
                }
            ],
            intent: {
                name: '',
                confidence: 1
            },
            text: ''
        },
        result_expected: ''
    },
    {
        message_id: "014",
        test_form_number: 1,
        initial_state: {
            u.slots: [
                {
                    u.slot_name: "",
                    u.slot_value: ""
                }
            ],
            spelling_state: {
                u.close_prompt_enabled: False,
                u.current_spelling_input_value: '',
                u.spelling_list: [],
                u.waiting_intent: None,
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
                    entity: '',
                    value: ''
                }
            ],
            intent: {
                name: '',
                confidence: 1
            },
            text: ''
        },
        result_expected: ''
    },
    {
        message_id: "015",
        test_form_number: 1,
        initial_state: {
            u.slots: [
                {
                    u.slot_name: "",
                    u.slot_value: ""
                }
            ],
            spelling_state: {
                u.close_prompt_enabled: False,
                u.current_spelling_input_value: '',
                u.spelling_list: [],
                u.waiting_intent: None,
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
                    entity: '',
                    value: ''
                }
            ],
            intent: {
                name: '',
                confidence: 1
            },
            text: ''
        },
        result_expected: ''
    },
    {
        message_id: "016",
        test_form_number: 1,
        initial_state: {
            u.slots: [
                {
                    u.slot_name: "",
                    u.slot_value: ""
                }
            ],
            spelling_state: {
                u.close_prompt_enabled: False,
                u.current_spelling_input_value: '',
                u.spelling_list: [],
                u.waiting_intent: None,
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
                    entity: '',
                    value: ''
                }
            ],
            intent: {
                name: '',
                confidence: 1
            },
            text: ''
        },
        result_expected: ''
    },
    {
        message_id: "017",
        test_form_number: 1,
        initial_state: {
            u.slots: [
                {
                    u.slot_name: "",
                    u.slot_value: ""
                }
            ],
            spelling_state: {
                u.close_prompt_enabled: False,
                u.current_spelling_input_value: '',
                u.spelling_list: [],
                u.waiting_intent: None,
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
                    entity: '',
                    value: ''
                }
            ],
            intent: {
                name: '',
                confidence: 1
            },
            text: ''
        },
        result_expected: ''
    },
    {
        message_id: "018",
        test_form_number: 1,
        initial_state: {
            u.slots: [
                {
                    u.slot_name: "",
                    u.slot_value: ""
                }
            ],
            spelling_state: {
                u.close_prompt_enabled: False,
                u.current_spelling_input_value: '',
                u.spelling_list: [],
                u.waiting_intent: None,
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
                    entity: '',
                    value: ''
                }
            ],
            intent: {
                name: '',
                confidence: 1
            },
            text: ''
        },
        result_expected: ''
    },
    {
        message_id: "019",
        test_form_number: 1,
        initial_state: {
            u.slots: [
                {
                    u.slot_name: "",
                    u.slot_value: ""
                }
            ],
            spelling_state: {
                u.close_prompt_enabled: False,
                u.current_spelling_input_value: '',
                u.spelling_list: [],
                u.waiting_intent: None,
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
                    entity: '',
                    value: ''
                }
            ],
            intent: {
                name: '',
                confidence: 1
            },
            text: ''
        },
        result_expected: ''
    },
    {
        message_id: "020",
        test_form_number: 1,
        initial_state: {
            u.slots: [
                {
                    u.slot_name: "",
                    u.slot_value: ""
                }
            ],
            spelling_state: {
                u.close_prompt_enabled: False,
                u.current_spelling_input_value: '',
                u.spelling_list: [],
                u.waiting_intent: None,
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
                    entity: '',
                    value: ''
                }
            ],
            intent: {
                name: '',
                confidence: 1
            },
            text: ''
        },
        result_expected: ''
    },
    {
        message_id: "021",
        test_form_number: 1,
        initial_state: {
            u.slots: [
                {
                    u.slot_name: "",
                    u.slot_value: ""
                }
            ],
            spelling_state: {
                u.close_prompt_enabled: False,
                u.current_spelling_input_value: '',
                u.spelling_list: [],
                u.waiting_intent: None,
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
                    entity: '',
                    value: ''
                }
            ],
            intent: {
                name: '',
                confidence: 1
            },
            text: ''
        },
        result_expected: ''
    },
    {
        message_id: "022",
        test_form_number: 1,
        initial_state: {
            u.slots: [
                {
                    u.slot_name: "",
                    u.slot_value: ""
                }
            ],
            spelling_state: {
                u.close_prompt_enabled: False,
                u.current_spelling_input_value: '',
                u.spelling_list: [],
                u.waiting_intent: None,
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
                    entity: '',
                    value: ''
                }
            ],
            intent: {
                name: '',
                confidence: 1
            },
            text: ''
        },
        result_expected: ''
    },
    {
        message_id: "023",
        test_form_number: 1,
        initial_state: {
            u.slots: [
                {
                    u.slot_name: "",
                    u.slot_value: ""
                }
            ],
            spelling_state: {
                u.close_prompt_enabled: False,
                u.current_spelling_input_value: '',
                u.spelling_list: [],
                u.waiting_intent: None,
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
                    entity: '',
                    value: ''
                }
            ],
            intent: {
                name: '',
                confidence: 1
            },
            text: ''
        },
        result_expected: ''
    },
    {
        message_id: "024",
        test_form_number: 1,
        initial_state: {
            u.slots: [
                {
                    u.slot_name: "",
                    u.slot_value: ""
                }
            ],
            spelling_state: {
                u.close_prompt_enabled: False,
                u.current_spelling_input_value: '',
                u.spelling_list: [],
                u.waiting_intent: None,
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
                    entity: '',
                    value: ''
                }
            ],
            intent: {
                name: '',
                confidence: 1
            },
            text: ''
        },
        result_expected: ''
    },
    {
        message_id: "025",
        test_form_number: 1,
        initial_state: {
            u.slots: [
                {
                    u.slot_name: "",
                    u.slot_value: ""
                }
            ],
            spelling_state: {
                u.close_prompt_enabled: False,
                u.current_spelling_input_value: '',
                u.spelling_list: [],
                u.waiting_intent: None,
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
                    entity: '',
                    value: ''
                }
            ],
            intent: {
                name: '',
                confidence: 1
            },
            text: ''
        },
        result_expected: ''
    },
    {
        message_id: "026",
        test_form_number: 1,
        initial_state: {
            u.slots: [
                {
                    u.slot_name: "",
                    u.slot_value: ""
                }
            ],
            spelling_state: {
                u.close_prompt_enabled: False,
                u.current_spelling_input_value: '',
                u.spelling_list: [],
                u.waiting_intent: None,
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
                    entity: '',
                    value: ''
                }
            ],
            intent: {
                name: '',
                confidence: 1
            },
            text: ''
        },
        result_expected: ''
    },
    {
        message_id: "027",
        test_form_number: 1,
        initial_state: {
            u.slots: [
                {
                    u.slot_name: "",
                    u.slot_value: ""
                }
            ],
            spelling_state: {
                u.close_prompt_enabled: False,
                u.current_spelling_input_value: '',
                u.spelling_list: [],
                u.waiting_intent: None,
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
                    entity: '',
                    value: ''
                }
            ],
            intent: {
                name: '',
                confidence: 1
            },
            text: ''
        },
        result_expected: ''
    },
    {
        message_id: "028",
        test_form_number: 1,
        initial_state: {
            u.slots: [
                {
                    u.slot_name: "",
                    u.slot_value: ""
                }
            ],
            spelling_state: {
                u.close_prompt_enabled: False,
                u.current_spelling_input_value: '',
                u.spelling_list: [],
                u.waiting_intent: None,
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
                    entity: '',
                    value: ''
                }
            ],
            intent: {
                name: '',
                confidence: 1
            },
            text: ''
        },
        result_expected: ''
    },
    {
        message_id: "029",
        test_form_number: 1,
        initial_state: {
            u.slots: [
                {
                    u.slot_name: "",
                    u.slot_value: ""
                }
            ],
            spelling_state: {
                u.close_prompt_enabled: False,
                u.current_spelling_input_value: '',
                u.spelling_list: [],
                u.waiting_intent: None,
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
                    entity: '',
                    value: ''
                }
            ],
            intent: {
                name: '',
                confidence: 1
            },
            text: ''
        },
        result_expected: ''
    },
    {
        message_id: "030",
        test_form_number: 1,
        initial_state: {
            u.slots: [
                {
                    u.slot_name: "",
                    u.slot_value: ""
                }
            ],
            spelling_state: {
                u.close_prompt_enabled: False,
                u.current_spelling_input_value: '',
                u.spelling_list: [],
                u.waiting_intent: None,
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
                    entity: '',
                    value: ''
                }
            ],
            intent: {
                name: '',
                confidence: 1
            },
            text: ''
        },
        result_expected: ''
    },
    {
        message_id: "031",
        test_form_number: 1,
        initial_state: {
            u.slots: [
                {
                    u.slot_name: "",
                    u.slot_value: ""
                }
            ],
            spelling_state: {
                u.close_prompt_enabled: False,
                u.current_spelling_input_value: '',
                u.spelling_list: [],
                u.waiting_intent: None,
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
                    entity: '',
                    value: ''
                }
            ],
            intent: {
                name: '',
                confidence: 1
            },
            text: ''
        },
        result_expected: ''
    },
    {
        message_id: "032",
        test_form_number: 1,
        initial_state: {
            u.slots: [
                {
                    u.slot_name: "",
                    u.slot_value: ""
                }
            ],
            spelling_state: {
                u.close_prompt_enabled: False,
                u.current_spelling_input_value: '',
                u.spelling_list: [],
                u.waiting_intent: None,
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
                    entity: '',
                    value: ''
                }
            ],
            intent: {
                name: '',
                confidence: 1
            },
            text: ''
        },
        result_expected: ''
    },
    {
        message_id: "033",
        test_form_number: 1,
        initial_state: {
            u.slots: [
                {
                    u.slot_name: "",
                    u.slot_value: ""
                }
            ],
            spelling_state: {
                u.close_prompt_enabled: False,
                u.current_spelling_input_value: '',
                u.spelling_list: [],
                u.waiting_intent: None,
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
                    entity: '',
                    value: ''
                }
            ],
            intent: {
                name: '',
                confidence: 1
            },
            text: ''
        },
        result_expected: ''
    },
    {
        message_id: "034",
        test_form_number: 1,
        initial_state: {
            u.slots: [
                {
                    u.slot_name: "",
                    u.slot_value: ""
                }
            ],
            spelling_state: {
                u.close_prompt_enabled: False,
                u.current_spelling_input_value: '',
                u.spelling_list: [],
                u.waiting_intent: None,
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
                    entity: '',
                    value: ''
                }
            ],
            intent: {
                name: '',
                confidence: 1
            },
            text: ''
        },
        result_expected: ''
    },
    {
        message_id: "035",
        test_form_number: 1,
        initial_state: {
            u.slots: [
                {
                    u.slot_name: "",
                    u.slot_value: ""
                }
            ],
            spelling_state: {
                u.close_prompt_enabled: False,
                u.current_spelling_input_value: '',
                u.spelling_list: [],
                u.waiting_intent: None,
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
                    entity: '',
                    value: ''
                }
            ],
            intent: {
                name: '',
                confidence: 1
            },
            text: ''
        },
        result_expected: ''
    },
    {
        message_id: "036",
        test_form_number: 1,
        initial_state: {
            u.slots: [
                {
                    u.slot_name: "",
                    u.slot_value: ""
                }
            ],
            spelling_state: {
                u.close_prompt_enabled: False,
                u.current_spelling_input_value: '',
                u.spelling_list: [],
                u.waiting_intent: None,
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
                    entity: '',
                    value: ''
                }
            ],
            intent: {
                name: '',
                confidence: 1
            },
            text: ''
        },
        result_expected: ''
    },
    {
        message_id: "037",
        test_form_number: 1,
        initial_state: {
            u.slots: [
                {
                    u.slot_name: "",
                    u.slot_value: ""
                }
            ],
            spelling_state: {
                u.close_prompt_enabled: False,
                u.current_spelling_input_value: '',
                u.spelling_list: [],
                u.waiting_intent: None,
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
                    entity: '',
                    value: ''
                }
            ],
            intent: {
                name: '',
                confidence: 1
            },
            text: ''
        },
        result_expected: ''
    },
    {
        message_id: "038",
        test_form_number: 1,
        initial_state: {
            u.slots: [
                {
                    u.slot_name: "",
                    u.slot_value: ""
                }
            ],
            spelling_state: {
                u.close_prompt_enabled: False,
                u.current_spelling_input_value: '',
                u.spelling_list: [],
                u.waiting_intent: None,
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
                    entity: '',
                    value: ''
                }
            ],
            intent: {
                name: '',
                confidence: 1
            },
            text: ''
        },
        result_expected: ''
    },
    {
        message_id: "039",
        test_form_number: 1,
        initial_state: {
            u.slots: [
                {
                    u.slot_name: "",
                    u.slot_value: ""
                }
            ],
            spelling_state: {
                u.close_prompt_enabled: False,
                u.current_spelling_input_value: '',
                u.spelling_list: [],
                u.waiting_intent: None,
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
                    entity: '',
                    value: ''
                }
            ],
            intent: {
                name: '',
                confidence: 1
            },
            text: ''
        },
        result_expected: ''
    },
    {
        message_id: "040",
        test_form_number: 1,
        initial_state: {
            u.slots: [
                {
                    u.slot_name: "",
                    u.slot_value: ""
                }
            ],
            spelling_state: {
                u.close_prompt_enabled: False,
                u.current_spelling_input_value: '',
                u.spelling_list: [],
                u.waiting_intent: None,
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
                    entity: '',
                    value: ''
                }
            ],
            intent: {
                name: '',
                confidence: 1
            },
            text: ''
        },
        result_expected: ''
    },
    {
        message_id: "041",
        test_form_number: 1,
        initial_state: {
            u.slots: [
                {
                    u.slot_name: "",
                    u.slot_value: ""
                }
            ],
            spelling_state: {
                u.close_prompt_enabled: False,
                u.current_spelling_input_value: '',
                u.spelling_list: [],
                u.waiting_intent: None,
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
                    entity: '',
                    value: ''
                }
            ],
            intent: {
                name: '',
                confidence: 1
            },
            text: ''
        },
        result_expected: ''
    },
    {
        message_id: "042",
        test_form_number: 1,
        initial_state: {
            u.slots: [
                {
                    u.slot_name: "",
                    u.slot_value: ""
                }
            ],
            spelling_state: {
                u.close_prompt_enabled: False,
                u.current_spelling_input_value: '',
                u.spelling_list: [],
                u.waiting_intent: None,
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
                    entity: '',
                    value: ''
                }
            ],
            intent: {
                name: '',
                confidence: 1
            },
            text: ''
        },
        result_expected: ''
    },
    {
        message_id: "043",
        test_form_number: 1,
        initial_state: {
            u.slots: [
                {
                    u.slot_name: "",
                    u.slot_value: ""
                }
            ],
            spelling_state: {
                u.close_prompt_enabled: False,
                u.current_spelling_input_value: '',
                u.spelling_list: [],
                u.waiting_intent: None,
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
                    entity: '',
                    value: ''
                }
            ],
            intent: {
                name: '',
                confidence: 1
            },
            text: ''
        },
        result_expected: ''
    },
    {
        message_id: "044",
        test_form_number: 1,
        initial_state: {
            u.slots: [
                {
                    u.slot_name: "",
                    u.slot_value: ""
                }
            ],
            spelling_state: {
                u.close_prompt_enabled: False,
                u.current_spelling_input_value: '',
                u.spelling_list: [],
                u.waiting_intent: None,
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
                    entity: '',
                    value: ''
                }
            ],
            intent: {
                name: '',
                confidence: 1
            },
            text: ''
        },
        result_expected: ''
    },
    {
        message_id: "045",
        test_form_number: 1,
        initial_state: {
            u.slots: [
                {
                    u.slot_name: "",
                    u.slot_value: ""
                }
            ],
            spelling_state: {
                u.close_prompt_enabled: False,
                u.current_spelling_input_value: '',
                u.spelling_list: [],
                u.waiting_intent: None,
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
                    entity: '',
                    value: ''
                }
            ],
            intent: {
                name: '',
                confidence: 1
            },
            text: ''
        },
        result_expected: ''
    },
    {
        message_id: "046",
        test_form_number: 1,
        initial_state: {
            u.slots: [
                {
                    u.slot_name: "",
                    u.slot_value: ""
                }
            ],
            spelling_state: {
                u.close_prompt_enabled: False,
                u.current_spelling_input_value: '',
                u.spelling_list: [],
                u.waiting_intent: None,
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
                    entity: '',
                    value: ''
                }
            ],
            intent: {
                name: '',
                confidence: 1
            },
            text: ''
        },
        result_expected: ''
    },
    {
        message_id: "047",
        test_form_number: 1,
        initial_state: {
            u.slots: [
                {
                    u.slot_name: "",
                    u.slot_value: ""
                }
            ],
            spelling_state: {
                u.close_prompt_enabled: False,
                u.current_spelling_input_value: '',
                u.spelling_list: [],
                u.waiting_intent: None,
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
                    entity: '',
                    value: ''
                }
            ],
            intent: {
                name: '',
                confidence: 1
            },
            text: ''
        },
        result_expected: ''
    },
    {
        message_id: "048",
        test_form_number: 1,
        initial_state: {
            u.slots: [
                {
                    u.slot_name: "",
                    u.slot_value: ""
                }
            ],
            spelling_state: {
                u.close_prompt_enabled: False,
                u.current_spelling_input_value: '',
                u.spelling_list: [],
                u.waiting_intent: None,
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
                    entity: '',
                    value: ''
                }
            ],
            intent: {
                name: '',
                confidence: 1
            },
            text: ''
        },
        result_expected: ''
    },
    {
        message_id: "049",
        test_form_number: 1,
        initial_state: {
            u.slots: [
                {
                    u.slot_name: "",
                    u.slot_value: ""
                }
            ],
            spelling_state: {
                u.close_prompt_enabled: False,
                u.current_spelling_input_value: '',
                u.spelling_list: [],
                u.waiting_intent: None,
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
                    entity: '',
                    value: ''
                }
            ],
            intent: {
                name: '',
                confidence: 1
            },
            text: ''
        },
        result_expected: ''
    },
    {
        message_id: "050",
        test_form_number: 1,
        initial_state: {
            u.slots: [
                {
                    u.slot_name: "",
                    u.slot_value: ""
                }
            ],
            spelling_state: {
                u.close_prompt_enabled: False,
                u.current_spelling_input_value: '',
                u.spelling_list: [],
                u.waiting_intent: None,
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
                    entity: '',
                    value: ''
                }
            ],
            intent: {
                name: '',
                confidence: 1
            },
            text: ''
        },
        result_expected: ''
    },
    {
        message_id: "051",
        test_form_number: 1,
        initial_state: {
            u.slots: [
                {
                    u.slot_name: "",
                    u.slot_value: ""
                }
            ],
            spelling_state: {
                u.close_prompt_enabled: False,
                u.current_spelling_input_value: '',
                u.spelling_list: [],
                u.waiting_intent: None,
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
                    entity: '',
                    value: ''
                }
            ],
            intent: {
                name: '',
                confidence: 1
            },
            text: ''
        },
        result_expected: ''
    },
    {
        message_id: "052",
        test_form_number: 1,
        initial_state: {
            u.slots: [
                {
                    u.slot_name: "",
                    u.slot_value: ""
                }
            ],
            spelling_state: {
                u.close_prompt_enabled: False,
                u.current_spelling_input_value: '',
                u.spelling_list: [],
                u.waiting_intent: None,
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
                    entity: '',
                    value: ''
                }
            ],
            intent: {
                name: '',
                confidence: 1
            },
            text: ''
        },
        result_expected: ''
    },
    {
        message_id: "053",
        test_form_number: 1,
        initial_state: {
            u.slots: [
                {
                    u.slot_name: "",
                    u.slot_value: ""
                }
            ],
            spelling_state: {
                u.close_prompt_enabled: False,
                u.current_spelling_input_value: '',
                u.spelling_list: [],
                u.waiting_intent: None,
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
                    entity: '',
                    value: ''
                }
            ],
            intent: {
                name: '',
                confidence: 1
            },
            text: ''
        },
        result_expected: ''
    },
    {
        message_id: "054",
        test_form_number: 1,
        initial_state: {
            u.slots: [
                {
                    u.slot_name: "",
                    u.slot_value: ""
                }
            ],
            spelling_state: {
                u.close_prompt_enabled: False,
                u.current_spelling_input_value: '',
                u.spelling_list: [],
                u.waiting_intent: None,
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
                    entity: '',
                    value: ''
                }
            ],
            intent: {
                name: '',
                confidence: 1
            },
            text: ''
        },
        result_expected: ''
    },
    {
        message_id: "055",
        test_form_number: 1,
        initial_state: {
            u.slots: [
                {
                    u.slot_name: "",
                    u.slot_value: ""
                }
            ],
            spelling_state: {
                u.close_prompt_enabled: False,
                u.current_spelling_input_value: '',
                u.spelling_list: [],
                u.waiting_intent: None,
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
                    entity: '',
                    value: ''
                }
            ],
            intent: {
                name: '',
                confidence: 1
            },
            text: ''
        },
        result_expected: ''
    },
    {
        message_id: "056",
        test_form_number: 1,
        initial_state: {
            u.slots: [
                {
                    u.slot_name: "",
                    u.slot_value: ""
                }
            ],
            spelling_state: {
                u.close_prompt_enabled: False,
                u.current_spelling_input_value: '',
                u.spelling_list: [],
                u.waiting_intent: None,
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
                    entity: '',
                    value: ''
                }
            ],
            intent: {
                name: '',
                confidence: 1
            },
            text: ''
        },
        result_expected: ''
    },
    {
        message_id: "057",
        test_form_number: 1,
        initial_state: {
            u.slots: [
                {
                    u.slot_name: "",
                    u.slot_value: ""
                }
            ],
            spelling_state: {
                u.close_prompt_enabled: False,
                u.current_spelling_input_value: '',
                u.spelling_list: [],
                u.waiting_intent: None,
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
                    entity: '',
                    value: ''
                }
            ],
            intent: {
                name: '',
                confidence: 1
            },
            text: ''
        },
        result_expected: ''
    },
    {
        message_id: "058",
        test_form_number: 1,
        initial_state: {
            u.slots: [
                {
                    u.slot_name: "",
                    u.slot_value: ""
                }
            ],
            spelling_state: {
                u.close_prompt_enabled: False,
                u.current_spelling_input_value: '',
                u.spelling_list: [],
                u.waiting_intent: None,
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
                    entity: '',
                    value: ''
                }
            ],
            intent: {
                name: '',
                confidence: 1
            },
            text: ''
        },
        result_expected: ''
    },
    {
        message_id: "059",
        test_form_number: 1,
        initial_state: {
            u.slots: [
                {
                    u.slot_name: "",
                    u.slot_value: ""
                }
            ],
            spelling_state: {
                u.close_prompt_enabled: False,
                u.current_spelling_input_value: '',
                u.spelling_list: [],
                u.waiting_intent: None,
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
                    entity: '',
                    value: ''
                }
            ],
            intent: {
                name: '',
                confidence: 1
            },
            text: ''
        },
        result_expected: ''
    },
    {
        message_id: "060",
        test_form_number: 1,
        initial_state: {
            u.slots: [
                {
                    u.slot_name: "",
                    u.slot_value: ""
                }
            ],
            spelling_state: {
                u.close_prompt_enabled: False,
                u.current_spelling_input_value: '',
                u.spelling_list: [],
                u.waiting_intent: None,
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
                    entity: '',
                    value: ''
                }
            ],
            intent: {
                name: '',
                confidence: 1
            },
            text: ''
        },
        result_expected: ''
    },
    {
        message_id: "061",
        test_form_number: 1,
        initial_state: {
            u.slots: [
                {
                    u.slot_name: "",
                    u.slot_value: ""
                }
            ],
            spelling_state: {
                u.close_prompt_enabled: False,
                u.current_spelling_input_value: '',
                u.spelling_list: [],
                u.waiting_intent: None,
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
                    entity: '',
                    value: ''
                }
            ],
            intent: {
                name: '',
                confidence: 1
            },
            text: ''
        },
        result_expected: ''
    },
    {
        message_id: "062",
        test_form_number: 1,
        initial_state: {
            u.slots: [
                {
                    u.slot_name: "",
                    u.slot_value: ""
                }
            ],
            spelling_state: {
                u.close_prompt_enabled: False,
                u.current_spelling_input_value: '',
                u.spelling_list: [],
                u.waiting_intent: None,
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
                    entity: '',
                    value: ''
                }
            ],
            intent: {
                name: '',
                confidence: 1
            },
            text: ''
        },
        result_expected: ''
    },
    {
        message_id: "063",
        test_form_number: 1,
        initial_state: {
            u.slots: [
                {
                    u.slot_name: "",
                    u.slot_value: ""
                }
            ],
            spelling_state: {
                u.close_prompt_enabled: False,
                u.current_spelling_input_value: '',
                u.spelling_list: [],
                u.waiting_intent: None,
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
                    entity: '',
                    value: ''
                }
            ],
            intent: {
                name: '',
                confidence: 1
            },
            text: ''
        },
        result_expected: ''
    },
    {
        message_id: "064",
        test_form_number: 1,
        initial_state: {
            u.slots: [
                {
                    u.slot_name: "",
                    u.slot_value: ""
                }
            ],
            spelling_state: {
                u.close_prompt_enabled: False,
                u.current_spelling_input_value: '',
                u.spelling_list: [],
                u.waiting_intent: None,
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
                    entity: '',
                    value: ''
                }
            ],
            intent: {
                name: '',
                confidence: 1
            },
            text: ''
        },
        result_expected: ''
    },
    {
        message_id: "065",
        test_form_number: 1,
        initial_state: {
            u.slots: [
                {
                    u.slot_name: "",
                    u.slot_value: ""
                }
            ],
            spelling_state: {
                u.close_prompt_enabled: False,
                u.current_spelling_input_value: '',
                u.spelling_list: [],
                u.waiting_intent: None,
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
                    entity: '',
                    value: ''
                }
            ],
            intent: {
                name: '',
                confidence: 1
            },
            text: ''
        },
        result_expected: ''
    },
    {
        message_id: "066",
        test_form_number: 1,
        initial_state: {
            u.slots: [
                {
                    u.slot_name: "",
                    u.slot_value: ""
                }
            ],
            spelling_state: {
                u.close_prompt_enabled: False,
                u.current_spelling_input_value: '',
                u.spelling_list: [],
                u.waiting_intent: None,
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
                    entity: '',
                    value: ''
                }
            ],
            intent: {
                name: '',
                confidence: 1
            },
            text: ''
        },
        result_expected: ''
    },
    {
        message_id: "067",
        test_form_number: 1,
        initial_state: {
            u.slots: [
                {
                    u.slot_name: "",
                    u.slot_value: ""
                }
            ],
            spelling_state: {
                u.close_prompt_enabled: False,
                u.current_spelling_input_value: '',
                u.spelling_list: [],
                u.waiting_intent: None,
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
                    entity: '',
                    value: ''
                }
            ],
            intent: {
                name: '',
                confidence: 1
            },
            text: ''
        },
        result_expected: ''
    },
    {
        message_id: "068",
        test_form_number: 1,
        initial_state: {
            u.slots: [
                {
                    u.slot_name: "",
                    u.slot_value: ""
                }
            ],
            spelling_state: {
                u.close_prompt_enabled: False,
                u.current_spelling_input_value: '',
                u.spelling_list: [],
                u.waiting_intent: None,
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
                    entity: '',
                    value: ''
                }
            ],
            intent: {
                name: '',
                confidence: 1
            },
            text: ''
        },
        result_expected: ''
    },
    {
        message_id: "069",
        test_form_number: 1,
        initial_state: {
            u.slots: [
                {
                    u.slot_name: "",
                    u.slot_value: ""
                }
            ],
            spelling_state: {
                u.close_prompt_enabled: False,
                u.current_spelling_input_value: '',
                u.spelling_list: [],
                u.waiting_intent: None,
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
                    entity: '',
                    value: ''
                }
            ],
            intent: {
                name: '',
                confidence: 1
            },
            text: ''
        },
        result_expected: ''
    },
    {
        message_id: "070",
        test_form_number: 1,
        initial_state: {
            u.slots: [
                {
                    u.slot_name: "",
                    u.slot_value: ""
                }
            ],
            spelling_state: {
                u.close_prompt_enabled: False,
                u.current_spelling_input_value: '',
                u.spelling_list: [],
                u.waiting_intent: None,
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
                    entity: '',
                    value: ''
                }
            ],
            intent: {
                name: '',
                confidence: 1
            },
            text: ''
        },
        result_expected: ''
    },
    {
        message_id: "071",
        test_form_number: 1,
        initial_state: {
            u.slots: [
                {
                    u.slot_name: "",
                    u.slot_value: ""
                }
            ],
            spelling_state: {
                u.close_prompt_enabled: False,
                u.current_spelling_input_value: '',
                u.spelling_list: [],
                u.waiting_intent: None,
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
                    entity: '',
                    value: ''
                }
            ],
            intent: {
                name: '',
                confidence: 1
            },
            text: ''
        },
        result_expected: ''
    },
    {
        message_id: "072",
        test_form_number: 1,
        initial_state: {
            u.slots: [
                {
                    u.slot_name: "",
                    u.slot_value: ""
                }
            ],
            spelling_state: {
                u.close_prompt_enabled: False,
                u.current_spelling_input_value: '',
                u.spelling_list: [],
                u.waiting_intent: None,
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
                    entity: '',
                    value: ''
                }
            ],
            intent: {
                name: '',
                confidence: 1
            },
            text: ''
        },
        result_expected: ''
    },
    {
        message_id: "073",
        test_form_number: 1,
        initial_state: {
            u.slots: [
                {
                    u.slot_name: "",
                    u.slot_value: ""
                }
            ],
            spelling_state: {
                u.close_prompt_enabled: False,
                u.current_spelling_input_value: '',
                u.spelling_list: [],
                u.waiting_intent: None,
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
                    entity: '',
                    value: ''
                }
            ],
            intent: {
                name: '',
                confidence: 1
            },
            text: ''
        },
        result_expected: ''
    },
    {
        message_id: "074",
        test_form_number: 1,
        initial_state: {
            u.slots: [
                {
                    u.slot_name: "",
                    u.slot_value: ""
                }
            ],
            spelling_state: {
                u.close_prompt_enabled: False,
                u.current_spelling_input_value: '',
                u.spelling_list: [],
                u.waiting_intent: None,
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
                    entity: '',
                    value: ''
                }
            ],
            intent: {
                name: '',
                confidence: 1
            },
            text: ''
        },
        result_expected: ''
    },
    {
        message_id: "075",
        test_form_number: 1,
        initial_state: {
            u.slots: [
                {
                    u.slot_name: "",
                    u.slot_value: ""
                }
            ],
            spelling_state: {
                u.close_prompt_enabled: False,
                u.current_spelling_input_value: '',
                u.spelling_list: [],
                u.waiting_intent: None,
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
                    entity: '',
                    value: ''
                }
            ],
            intent: {
                name: '',
                confidence: 1
            },
            text: ''
        },
        result_expected: ''
    },
    {
        message_id: "076",
        test_form_number: 1,
        initial_state: {
            u.slots: [
                {
                    u.slot_name: "",
                    u.slot_value: ""
                }
            ],
            spelling_state: {
                u.close_prompt_enabled: False,
                u.current_spelling_input_value: '',
                u.spelling_list: [],
                u.waiting_intent: None,
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
                    entity: '',
                    value: ''
                }
            ],
            intent: {
                name: '',
                confidence: 1
            },
            text: ''
        },
        result_expected: ''
    },
    {
        message_id: "077",
        test_form_number: 1,
        initial_state: {
            u.slots: [
                {
                    u.slot_name: "",
                    u.slot_value: ""
                }
            ],
            spelling_state: {
                u.close_prompt_enabled: False,
                u.current_spelling_input_value: '',
                u.spelling_list: [],
                u.waiting_intent: None,
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
                    entity: '',
                    value: ''
                }
            ],
            intent: {
                name: '',
                confidence: 1
            },
            text: ''
        },
        result_expected: ''
    },
    {
        message_id: "078",
        test_form_number: 1,
        initial_state: {
            u.slots: [
                {
                    u.slot_name: "",
                    u.slot_value: ""
                }
            ],
            spelling_state: {
                u.close_prompt_enabled: False,
                u.current_spelling_input_value: '',
                u.spelling_list: [],
                u.waiting_intent: None,
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
                    entity: '',
                    value: ''
                }
            ],
            intent: {
                name: '',
                confidence: 1
            },
            text: ''
        },
        result_expected: ''
    },
    {
        message_id: "079",
        test_form_number: 1,
        initial_state: {
            u.slots: [
                {
                    u.slot_name: "",
                    u.slot_value: ""
                }
            ],
            spelling_state: {
                u.close_prompt_enabled: False,
                u.current_spelling_input_value: '',
                u.spelling_list: [],
                u.waiting_intent: None,
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
                    entity: '',
                    value: ''
                }
            ],
            intent: {
                name: '',
                confidence: 1
            },
            text: ''
        },
        result_expected: ''
    },
    {
        message_id: "080",
        test_form_number: 1,
        initial_state: {
            u.slots: [
                {
                    u.slot_name: "",
                    u.slot_value: ""
                }
            ],
            spelling_state: {
                u.close_prompt_enabled: False,
                u.current_spelling_input_value: '',
                u.spelling_list: [],
                u.waiting_intent: None,
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
                    entity: '',
                    value: ''
                }
            ],
            intent: {
                name: '',
                confidence: 1
            },
            text: ''
        },
        result_expected: ''
    },
    {
        message_id: "081",
        test_form_number: 1,
        initial_state: {
            u.slots: [
                {
                    u.slot_name: "",
                    u.slot_value: ""
                }
            ],
            spelling_state: {
                u.close_prompt_enabled: False,
                u.current_spelling_input_value: '',
                u.spelling_list: [],
                u.waiting_intent: None,
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
                    entity: '',
                    value: ''
                }
            ],
            intent: {
                name: '',
                confidence: 1
            },
            text: ''
        },
        result_expected: ''
    },
    {
        message_id: "082",
        test_form_number: 1,
        initial_state: {
            u.slots: [
                {
                    u.slot_name: "",
                    u.slot_value: ""
                }
            ],
            spelling_state: {
                u.close_prompt_enabled: False,
                u.current_spelling_input_value: '',
                u.spelling_list: [],
                u.waiting_intent: None,
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
                    entity: '',
                    value: ''
                }
            ],
            intent: {
                name: '',
                confidence: 1
            },
            text: ''
        },
        result_expected: ''
    },
    {
        message_id: "083",
        test_form_number: 1,
        initial_state: {
            u.slots: [
                {
                    u.slot_name: "",
                    u.slot_value: ""
                }
            ],
            spelling_state: {
                u.close_prompt_enabled: False,
                u.current_spelling_input_value: '',
                u.spelling_list: [],
                u.waiting_intent: None,
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
                    entity: '',
                    value: ''
                }
            ],
            intent: {
                name: '',
                confidence: 1
            },
            text: ''
        },
        result_expected: ''
    },
    {
        message_id: "084",
        test_form_number: 1,
        initial_state: {
            u.slots: [
                {
                    u.slot_name: "",
                    u.slot_value: ""
                }
            ],
            spelling_state: {
                u.close_prompt_enabled: False,
                u.current_spelling_input_value: '',
                u.spelling_list: [],
                u.waiting_intent: None,
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
                    entity: '',
                    value: ''
                }
            ],
            intent: {
                name: '',
                confidence: 1
            },
            text: ''
        },
        result_expected: ''
    },
    {
        message_id: "085",
        test_form_number: 1,
        initial_state: {
            u.slots: [
                {
                    u.slot_name: "",
                    u.slot_value: ""
                }
            ],
            spelling_state: {
                u.close_prompt_enabled: False,
                u.current_spelling_input_value: '',
                u.spelling_list: [],
                u.waiting_intent: None,
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
                    entity: '',
                    value: ''
                }
            ],
            intent: {
                name: '',
                confidence: 1
            },
            text: ''
        },
        result_expected: ''
    },
    {
        message_id: "086",
        test_form_number: 1,
        initial_state: {
            u.slots: [
                {
                    u.slot_name: "",
                    u.slot_value: ""
                }
            ],
            spelling_state: {
                u.close_prompt_enabled: False,
                u.current_spelling_input_value: '',
                u.spelling_list: [],
                u.waiting_intent: None,
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
                    entity: '',
                    value: ''
                }
            ],
            intent: {
                name: '',
                confidence: 1
            },
            text: ''
        },
        result_expected: ''
    },
    {
        message_id: "087",
        test_form_number: 1,
        initial_state: {
            u.slots: [
                {
                    u.slot_name: "",
                    u.slot_value: ""
                }
            ],
            spelling_state: {
                u.close_prompt_enabled: False,
                u.current_spelling_input_value: '',
                u.spelling_list: [],
                u.waiting_intent: None,
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
                    entity: '',
                    value: ''
                }
            ],
            intent: {
                name: '',
                confidence: 1
            },
            text: ''
        },
        result_expected: ''
    }
]

functional_test_cases = [
    {
        message_id: "000",
        test_form_number: 1,
        test_case_message: {
            entities: [
                {
                    entity: 'input_field',
                    value: 'first name'
                },
                {
                    entity: 'input_value',
                    value: 'alice'
                }
            ],
            intent: {
                name: complete_field,
                confidence: 1
            },
            text: 'the first name is alice'
        },
        result_expected: 'first name becomes alice and next field is mark'
    },
    {
        message_id: "001",
        test_form_number: 1,
        initial_state: {
            u.slots: [
                {
                    u.slot_name: "first name",
                    u.slot_value: "bob"
                },
                {
                    u.slot_name: "mark",
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
                    u.slot_name: "password",
                    u.slot_value: "p088w0r0"
                },
                {
                    u.slot_name: "first name",
                    u.slot_value: "robert"
                },
                {
                    u.slot_name: "email address",
                    u.slot_value: "alice@bob.it"
                }
            ],
            spelling_state: {
                u.close_prompt_enabled: False,
                u.current_spelling_input_value: '',
                u.spelling_list: [],
                u.waiting_intent: None,
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
                    u.slot_name: "first name",
                    u.slot_value: "lucie"
                },
                {
                    u.slot_name: "email address",
                    u.slot_value: "dear_alice@bob.it"
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
        result_expected: 'The submit alarm will be enabledand we have to confirm the action'
    },
    {
        message_id: "004",
        test_form_number: 1,
        initial_state: {
            u.slots: [
                {
                    u.slot_name: "password",
                    u.slot_value: "p088w0r0"
                },
                {
                    u.slot_name: "email address",
                    u.slot_value: "alice@bob.it"
                },
                {
                    u.slot_name: "mark",
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
                    u.slot_name: "",
                    u.slot_value: ""
                }
            ],
            spelling_state: {
                u.close_prompt_enabled: True,
                u.current_spelling_input_value: 'adama',
                u.spelling_list: ['first name']
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
        result_expected: 'The value adama is set for the first name, the next field is mark'
    },
    {
        message_id: "006",
        test_form_number: 1,
        initial_state: {
            u.slots: [
                {
                    u.slot_name: "mark",
                    u.slot_value: "28"
                }
            ]
        },
        test_case_message: {
            entities: [
                {
                    entity: 'input_field',
                    value: 'mark'
                },
                {
                    entity: 'input_value',
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
                    u.slot_name: "number of persons",
                    u.slot_value: "6"
                }
            ]
        },
        test_case_message: {
            entities: [
                {
                    entity: 'input_value',
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
                    u.slot_name: "number of persons",
                    u.slot_value: "2"
                },
                {
                    u.slot_name: "arrival time",
                    u.slot_value: "07:00"
                },
                {
                    u.slot_name: "phone number",
                    u.slot_value: "00237651322430"
                },
                {
                    u.slot_name: "birthday",
                    u.slot_value: None
                }
            ]
        },
        test_case_message: {
            entities: [
                {
                    entity: 'input_field',
                    value: 'arrival time'
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
        test_form_number: 1,
        initial_state: {
            u.slots: [
                {
                    u.slot_name: "phone number",
                    u.slot_value: "+223615342345"
                },
                {
                    u.slot_name: "number of persons",
                    u.slot_value: None
                },
                {
                    u.slot_name: "birthday",
                    u.slot_value: "31/05/1990"
                },
                {
                    u.slot_name: "arrival time",
                    u.slot_value: None
                },
                {
                    u.slot_name: "card expiration date",
                    u.slot_value: "04/2020"
                }
            ],
        },
        test_case_message: {
            entities: [],
            intent: {
                name: give_remaining_fields,
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
                    u.slot_name: "phone number",
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
                    entity: 'input_value',
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
                    u.slot_name: "gender",
                    u.slot_value: "male"
                }
            ]
        },
        test_case_message: {
            entities: [
                {
                    entity: 'input_field',
                    value: 'last name'
                }
            ],
            intent: {
                name: verify_presence_field,
                confidence: 1
            },
            text: 'is the field last name present in this form?'
        },
        result_expected: 'The field last name is not present. The next field is electronic devices'
    },
    {
        message_id: "018",
        test_form_number: 3,
        initial_state: {
            u.slots: [
                {
                    u.slot_name: "electronic devices",
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
                    entity: 'input_field',
                    value: 'message'
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
                    u.slot_name: "first name",
                    u.slot_value: None
                },
                {
                    u.slot_name: "mark",
                    u.slot_value: None
                },
                {
                    u.slot_name: "password",
                    u.slot_value: None
                },
                {
                    u.slot_name: "email address",
                    u.slot_value: None
                }
            ],
        },
        test_case_message: {
            entities: [
                {
                    entity: 'input_value',
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
                    entity: 'input_field',
                    value: 'first name'
                },
                {
                    entity: 'input_value',
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
                    entity: 'input_field',
                    value: 'first name'
                },
                {
                    entity: 'input_value',
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
                    entity: 'input_field',
                    value: 'mark'
                },
                {
                    entity: 'input_value',
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
                    entity: 'input_field',
                    value: 'mark'
                },
                {
                    entity: 'input_value',
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
        initial_state: {},
        test_case_message: {
            entities: [
                {
                    entity: 'input_field',
                    value: 'mark'
                },
                {
                    entity: 'input_value',
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
                    entity: 'input_field',
                    value: 'mark'
                },
                {
                    entity: 'input_value',
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
        initial_state: {},
        test_case_message: {
            entities: [
                {
                    entity: 'input_field',
                    value: 'mark'
                },
                {
                    entity: 'input_value',
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
                    entity: 'input_field',
                    value: 'mark'
                },
                {
                    entity: 'input_value',
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
                    entity: 'input_field',
                    value: 'mark'
                },
                {
                    entity: 'input_value',
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
                    entity: 'input_field',
                    value: 'mark'
                },
                {
                    entity: 'input_value',
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
                    entity: 'input_field',
                    value: 'mark'
                },
                {
                    entity: 'input_value',
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
                    entity: 'input_field',
                    value: 'mark'
                },
                {
                    entity: 'input_value',
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
                    entity: 'input_field',
                    value: 'password'
                },
                {
                    entity: 'input_value',
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
                    entity: 'input_field',
                    value: 'password'
                },
                {
                    entity: 'input_value',
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
                    entity: 'input_field',
                    value: 'password'
                },
                {
                    entity: 'input_value',
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
        message_id: "038",
        test_form_number: 1,
        initial_state: {},
        test_case_message: {
            entities: [
                {
                    entity: 'input_field',
                    value: 'email address'
                },
                {
                    entity: 'input_value',
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
                    entity: 'input_field',
                    value: 'email address'
                },
                {
                    entity: 'input_value',
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
                    entity: 'input_field',
                    value: 'email address'
                },
                {
                    entity: 'input_value',
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
                    entity: 'input_field',
                    value: 'email address'
                },
                {
                    entity: 'input_value',
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
                    entity: 'input_field',
                    value: 'email address'
                },
                {
                    entity: 'input_value',
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
                    entity: 'input_field',
                    value: 'email address'
                },
                {
                    entity: 'input_value',
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
                    u.slot_name: "phone number",
                    u.slot_value: None
                },
                {
                    u.slot_name: "number of persons",
                    u.slot_value: None
                },
                {
                    u.slot_name: "birthday",
                    u.slot_value: None
                },
                {
                    u.slot_name: "arrival time",
                    u.slot_value: None
                },
                {
                    u.slot_name: "card expiration date",
                    u.slot_value: None
                }
            ]
        },
        test_case_message: {
            entities: [
                {
                    entity: 'input_field',
                    value: 'phone number'
                },
                {
                    entity: 'input_value',
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
                    entity: 'input_field',
                    value: 'phone number'
                },
                {
                    entity: 'input_value',
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
                    entity: 'input_field',
                    value: 'phone number'
                },
                {
                    entity: 'input_value',
                    value: '+39+2376758933'
                }
            ],
            intent: {
                name: complete_field,
                confidence: 1
            },
            text: 'the phone number is +39+2376758933'
        },
        result_expected: 'The should be at most one <plus_sign>'
    },
    {
        message_id: "047",
        test_form_number: 2,
        initial_state: {},
        test_case_message: {
            entities: [
                {
                    entity: 'input_field',
                    value: 'phone number'
                },
                {
                    entity: 'input_value',
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
        initial_state: {},
        test_case_message: {
            entities: [
                {
                    entity: 'input_field',
                    value: 'phone number'
                },
                {
                    entity: 'input_value',
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
                    entity: 'input_field',
                    value: 'number of persons'
                },
                {
                    entity: 'input_value',
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
        initial_state: {},
        test_case_message: {
            entities: [
                {
                    entity: 'input_field',
                    value: 'number of persons'
                },
                {
                    entity: 'input_value',
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
                    entity: 'input_field',
                    value: 'number of persons'
                },
                {
                    entity: 'input_value',
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
                    entity: 'input_field',
                    value: 'number of persons'
                },
                {
                    entity: 'input_value',
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
                    entity: 'input_field',
                    value: 'number of persons'
                },
                {
                    entity: 'input_value',
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
        initial_state: {},
        test_case_message: {
            entities: [
                {
                    entity: 'input_field',
                    value: 'birthday'
                },
                {
                    entity: 'input_value',
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
                    entity: 'input_field',
                    value: 'birthday'
                },
                {
                    entity: 'input_value',
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
                    entity: 'input_field',
                    value: 'birthday'
                },
                {
                    entity: 'input_value',
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
                    entity: 'input_field',
                    value: 'birthday'
                },
                {
                    entity: 'input_value',
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
        initial_state: {},
        test_case_message: {
            entities: [
                {
                    entity: 'input_field',
                    value: 'birthday'
                },
                {
                    entity: 'input_value',
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
                    entity: 'input_field',
                    value: 'birthday'
                },
                {
                    entity: 'input_value',
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
                    entity: 'input_field',
                    value: 'arrival time'
                },
                {
                    entity: 'input_value',
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
                    entity: 'input_field',
                    value: 'arrival time'
                },
                {
                    entity: 'input_value',
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
        initial_state: {},
        test_case_message: {
            entities: [
                {
                    entity: 'input_field',
                    value: 'arrival time'
                },
                {
                    entity: 'input_value',
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
                    entity: 'input_field',
                    value: 'arrival time'
                },
                {
                    entity: 'input_value',
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
                    entity: 'input_field',
                    value: 'arrival time'
                },
                {
                    entity: 'input_value',
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
                    entity: 'input_field',
                    value: 'arrival time'
                },
                {
                    entity: 'input_value',
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
        initial_state: {},
        test_case_message: {
            entities: [
                {
                    entity: 'input_field',
                    value: 'arrival time'
                },
                {
                    entity: 'input_value',
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
        test_form_number: 2,
        initial_state: {},
        test_case_message: {
            entities: [
                {
                    entity: 'input_field',
                    value: 'card expiration date'
                },
                {
                    entity: 'input_value',
                    value: '2010-02'
                }
            ],
            intent: {
                name: complete_field,
                confidence: 1
            },
            text: 'the card expiration date is 2010-02'
        },
        result_expected: 'The card expiration date is february 2010'
    },
    {
        message_id: "068",
        test_form_number: 2,
        initial_state: {},
        test_case_message: {
            entities: [
                {
                    entity: 'input_field',
                    value: 'card expiration date'
                },
                {
                    entity: 'input_value',
                    value: 'January 2015'
                }
            ],
            intent: {
                name: complete_field,
                confidence: 1
            },
            text: 'the card expiration date is January 2015'
        },
        result_expected: 'The card expiration date is january 2015'
    },
    {
        message_id: "069",
        test_form_number: 2,
        initial_state: {},
        test_case_message: {
            entities: [
                {
                    entity: 'input_field',
                    value: 'card expiration date'
                },
                {
                    entity: 'input_value',
                    value: '2003 march'
                }
            ],
            intent: {
                name: complete_field,
                confidence: 1
            },
            text: 'the card expiration date is 2003 march'
        },
        result_expected: 'The card expiration date is march 2003'
    },
    {
        message_id: "070",
        test_form_number: 3,
        initial_state: {
            u.slots: [
                {
                    u.slot_name: "car",
                    u.slot_value: None
                },
                {
                    u.slot_name: "gender",
                    u.slot_value: None
                },
                {
                    u.slot_name: "electronic devices",
                    u.slot_value: None
                },
                {
                    u.slot_name: "message",
                    u.slot_value: None
                }
            ]
        },
        test_case_message: {
            entities: [
                {
                    entity: 'input_field',
                    value: 'car'
                },
                {
                    entity: 'input_value',
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
                    entity: 'input_field',
                    value: 'car'
                },
                {
                    entity: 'input_value',
                    value: 'ford'
                },
                {
                    entity: 'input_value',
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
                    entity: 'input_field',
                    value: 'gender'
                },
                {
                    entity: 'input_value',
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
        initial_state: {},
        test_case_message: {
            entities: [
                {
                    entity: 'input_field',
                    value: 'gender'
                },
                {
                    entity: 'input_value',
                    value: 'female'
                },
                {
                    entity: 'input_value',
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
                    entity: 'input_field',
                    value: 'electronic devices'
                },
                {
                    entity: 'input_value',
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
                    entity: 'input_field',
                    value: 'electronic devices'
                },
                {
                    entity: 'input_value',
                    value: 'smartphone'
                },
                {
                    entity: 'input_value',
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
                    entity: 'input_field',
                    value: 'electronic devices'
                },
                {
                    entity: 'input_value',
                    value: 'computer'
                },
                {
                    entity: 'input_value',
                    value: 'smart watch'
                },
                {
                    entity: 'input_value',
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
                    u.slot_name: "gender",
                    u.slot_value: None
                }
            ]
        },
        test_case_message: {
            entities: [
                {
                    entity: 'input_field',
                    value: 'message'
                },
                {
                    entity: 'input_value',
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
                    u.slot_name: "gender",
                    u.slot_value: None
                }
            ]
        },
        test_case_message: {
            entities: [
                {
                    entity: 'input_field',
                    value: 'message'
                },
                {
                    entity: 'input_value',
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
                    u.slot_name: "message",
                    u.slot_value: None
                },
                {
                    u.slot_name: "gender",
                    u.slot_value: None
                }
            ]
        },
        test_case_message: {
            entities: [
                {
                    entity: 'input_field',
                    value: 'message'
                },
                {
                    entity: 'input_value',
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
        test_form_number: 3,
        initial_state: {
            u.slots: [
                {
                    u.slot_name: "message",
                    u.slot_value: None
                },
                {
                    u.slot_name: "gender",
                    u.slot_value: None
                }
            ]
        },
        test_case_message: {
            entities: [
                {
                    entity: 'input_field',
                    value: 'message'
                },
                {
                    entity: 'input_value',
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
        message_id: "081",
        test_form_number: 3,
        initial_state: {
            u.slots: [
                {
                    u.slot_name: "message",
                    u.slot_value: None
                },
                {
                    u.slot_name: "gender",
                    u.slot_value: None
                }
            ]
        },
        test_case_message: {
            entities: [
                {
                    entity: 'input_field',
                    value: 'message'
                },
                {
                    entity: 'input_value',
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
        message_id: "082",
        test_form_number: 3,
        initial_state: {
            u.slots: [
                {
                    u.slot_name: "gender",
                    u.slot_value: None
                }
            ]
        },
        test_case_message: {
            entities: [
                {
                    entity: 'input_field',
                    value: 'message'
                },
                {
                    entity: 'input_value',
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
    }
]