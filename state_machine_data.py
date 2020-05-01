# contains all the states of the state machine

import utility as u


state_00 = {
    u.state_name: 'state_00',
    u.close_prompt_enabled: False,
    u.spelling_interrupted: False,
    u.warning_present: False,
    u.all_required_filled: False,
    u.submit_alarm_enabled: False,
    u.reset_alarm_enabled: False,
    u.submit_done: False,
    u.possible_next_action: None
}

state_01 = {
    u.state_name: 'state_01',
    u.close_prompt_enabled: False,
    u.spelling_interrupted: False,
    u.warning_present: False,
    u.all_required_filled: False,
    u.submit_alarm_enabled: False,
    u.reset_alarm_enabled: False,
    u.submit_done: False,
    u.possible_next_action: u.fill_field_action
}

state_02 = {
    u.state_name: 'state_02',
    u.close_prompt_enabled: False,
    u.spelling_interrupted: False,
    u.warning_present: False,
    u.all_required_filled: False,
    u.submit_alarm_enabled: False,
    u.reset_alarm_enabled: False,
    u.submit_done: False,
    u.possible_next_action: u.spelling_action
}

state_03 = {
    u.state_name: 'state_03',
    u.close_prompt_enabled: True,
    u.spelling_interrupted: True,
    u.warning_present: True,
    u.all_required_filled: False,
    u.submit_alarm_enabled: False,
    u.reset_alarm_enabled: False,
    u.submit_done: False,
    u.possible_next_action: None
}

state_04 = {
    u.state_name: 'state_04',
    u.close_prompt_enabled: False,
    u.spelling_interrupted: False,
    u.warning_present: True,
    u.all_required_filled: False,
    u.submit_alarm_enabled: False,
    u.reset_alarm_enabled: False,
    u.submit_done: False,
    u.possible_next_action: None
}

state_05 = {
    u.state_name: 'state_05',
    u.close_prompt_enabled: False,
    u.spelling_interrupted: False,
    u.warning_present: False,
    u.all_required_filled: True,
    u.submit_alarm_enabled: False,
    u.reset_alarm_enabled: False,
    u.submit_done: False,
    u.possible_next_action: u.fill_field_action
}

state_06 = {
    u.state_name: 'state_06',
    u.close_prompt_enabled: False,
    u.spelling_interrupted: False,
    u.warning_present: False,
    u.all_required_filled: True,
    u.submit_alarm_enabled: False,
    u.reset_alarm_enabled: False,
    u.submit_done: False,
    u.possible_next_action: u.submit_action
}

state_07 = {
    u.state_name: 'state_07',
    u.close_prompt_enabled: False,
    u.spelling_interrupted: False,
    u.warning_present: False,
    u.all_required_filled: True,
    u.submit_alarm_enabled: True,
    u.reset_alarm_enabled: False,
    u.submit_done: False,
    u.possible_next_action: u.submit_action
}

state_08 = {
    u.state_name: 'state_08',
    u.close_prompt_enabled: False,
    u.spelling_interrupted: False,
    u.warning_present: False,
    u.all_required_filled: True,
    u.submit_alarm_enabled: False,
    u.reset_alarm_enabled: False,
    u.submit_done: True,
    u.possible_next_action: None
}

state_09 = {
    u.state_name: 'state_09',
    u.close_prompt_enabled: False,
    u.spelling_interrupted: False,
    u.warning_present: False,
    u.all_required_filled: True,
    u.submit_alarm_enabled: False,
    u.reset_alarm_enabled: True,
    u.submit_done: False,
    u.possible_next_action: u.reset_all_fields_action
}

state_10 = {
    u.state_name: 'state_10',
    u.close_prompt_enabled: False,
    u.spelling_interrupted: False,
    u.warning_present: False,
    u.all_required_filled: True,
    u.submit_alarm_enabled: False,
    u.reset_alarm_enabled: False,
    u.submit_done: False,
    u.possible_next_action: u.spelling_action
}

state_11 = {
    u.state_name: 'state_11',
    u.close_prompt_enabled: True,
    u.spelling_interrupted: False,
    u.warning_present: False,
    u.all_required_filled: True,
    u.submit_alarm_enabled: False,
    u.reset_alarm_enabled: False,
    u.submit_done: False,
    u.possible_next_action: u.spelling_action
}

state_12 = {
    u.state_name: 'state_12',
    u.close_prompt_enabled: True,
    u.spelling_interrupted: False,
    u.warning_present: False,
    u.all_required_filled: False,
    u.submit_alarm_enabled: False,
    u.reset_alarm_enabled: False,
    u.submit_done: False,
    u.possible_next_action: u.spelling_action
}

state_13 = {
    u.state_name: 'state_13',
    u.close_prompt_enabled: True,
    u.spelling_interrupted: True,
    u.warning_present: True,
    u.all_required_filled: True,
    u.submit_alarm_enabled: False,
    u.reset_alarm_enabled: False,
    u.submit_done: False,
    u.possible_next_action: None
}

state_14 = {
    u.state_name: 'state_14',
    u.close_prompt_enabled: False,
    u.spelling_interrupted: False,
    u.warning_present: True,
    u.all_required_filled: True,
    u.submit_alarm_enabled: False,
    u.reset_alarm_enabled: False,
    u.submit_done: False,
    u.possible_next_action: None
}

state_15 = {
    u.state_name: 'state_15',
    u.close_prompt_enabled: False,
    u.spelling_interrupted: False,
    u.warning_present: False,
    u.all_required_filled: False,
    u.submit_alarm_enabled: False,
    u.reset_alarm_enabled: True,
    u.submit_done: False,
    u.possible_next_action: u.reset_all_fields_action
}

state_16 = {
    u.state_name: 'state_16',
    u.close_prompt_enabled: False,
    u.spelling_interrupted: False,
    u.warning_present: True,
    u.all_required_filled: True,
    u.submit_alarm_enabled: False,
    u.reset_alarm_enabled: False,
    u.submit_done: False,
    u.possible_next_action: None
}

states_list = [state_00, state_01, state_02, state_03, state_04, state_05, state_06, state_07, 
    state_08, state_09, state_10, state_11, state_12, state_13, state_14, state_15, state_16]

# list of important keys for the verification of the state
keys_list = [u.close_prompt_enabled, u.spelling_interrupted, u.warning_present, u.all_required_filled,
    u.submit_alarm_enabled, u.reset_alarm_enabled, u.submit_done, u.possible_next_action]
