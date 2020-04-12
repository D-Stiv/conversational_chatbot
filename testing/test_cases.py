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
        result_expected: 'submit alarm is disabled, state '
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
                name: submit_form,
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
                name: reset_all_fields,
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
                name: spelling,
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
                name: modify_value_field,
                confidence: 1
            },
            text: ''
        },
        result_expected: ''
    },
    {
        message_id: "007",
        test_form_number: 2,
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
                name: complete_field,
                confidence: 1
            },
            text: ''
        },
        result_expected: ''
    },
    {
        message_id: "008",
        test_form_number: 2,
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
                name: repeat_value_field,
                confidence: 1
            },
            text: ''
        },
        result_expected: ''
    },
    {
        message_id: "009",
        test_form_number: 2,
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
                name: repeat_all_fields,
                confidence: 1
            },
            text: ''
        },
        result_expected: ''
    },
    {
        message_id: "010",
        test_form_number: 2,
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
                name: repeat_required_fields,
                confidence: 1
            },
            text: ''
        },
        result_expected: ''
    },
    {
        message_id: "011",
        test_form_number: 2,
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
                name: repeat_optional_fields,
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
                name: give_remaining_fields,
                confidence: 1
            },
            text: ''
        },
        result_expected: ''
    },
    {
        message_id: "013",
        test_form_number: 2,
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
                name: give_remaining_required_fields,
                confidence: 1
            },
            text: ''
        },
        result_expected: ''
    },
    {
        message_id: "014",
        test_form_number: 2,
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
                name: give_remaining_optional_fields,
                confidence: 1
            },
            text: ''
        },
        result_expected: ''
    },
    {
        message_id: "015",
        test_form_number: 3,
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
                name: complete_field,
                confidence: 1
            },
            text: ''
        },
        result_expected: ''
    },
    {
        message_id: "016",
        test_form_number: 3,
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
                name: skip_field,
                confidence: 1
            },
            text: ''
        },
        result_expected: ''
    },
    {
        message_id: "017",
        test_form_number: 3,
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
                name: verify_presence_field,
                confidence: 1
            },
            text: ''
        },
        result_expected: ''
    },
    {
        message_id: "018",
        test_form_number: 3,
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
                name: verify_value_fields,
                confidence: 1
            },
            text: ''
        },
        result_expected: ''
    },
    {
        message_id: "019",
        test_form_number: 3,
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
                name: repeat_form_explanation,
                confidence: 1
            },
            text: ''
        },
        result_expected: ''
    },
    {
        message_id: "020",
        test_form_number: 3,
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
                name: explain_field,
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
        test_form_number: 2,
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
        test_form_number: 2,
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
        test_form_number: 2,
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
        test_form_number: 2,
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
        test_form_number: 2,
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
        test_form_number: 2,
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
        test_form_number: 2,
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
        test_form_number: 2,
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
        test_form_number: 2,
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
        test_form_number: 2,
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
        test_form_number: 2,
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
        test_form_number: 2,
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
        test_form_number: 2,
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
        test_form_number: 2,
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
        test_form_number: 2,
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
        test_form_number: 2,
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
        test_form_number: 2,
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
        test_form_number: 2,
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
        test_form_number: 2,
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
        test_form_number: 2,
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
        test_form_number: 2,
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
        test_form_number: 2,
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
        test_form_number: 2,
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
        test_form_number: 2,
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
        test_form_number: 2,
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
        test_form_number: 2,
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
        test_form_number: 2,
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
        test_form_number: 3,
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
        test_form_number: 3,
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
        test_form_number: 3,
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
        test_form_number: 3,
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
        test_form_number: 3,
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
        test_form_number: 3,
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
        test_form_number: 3,
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
        test_form_number: 3,
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
        test_form_number: 3,
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
        test_form_number: 3,
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
        test_form_number: 3,
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
        test_form_number: 3,
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
        test_form_number: 3,
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
        test_form_number: 3,
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
        test_form_number: 3,
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
        test_form_number: 3,
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
        test_form_number: 3,
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
        test_form_number: 3,
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