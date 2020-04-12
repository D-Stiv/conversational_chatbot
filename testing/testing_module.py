# testing module

import test_cases as t_c
import utility as u
from writers import LogWriter
from choice_bot import BotsManager
from selenium import webdriver
import functions as fn

class Testing:
    bots_list = []
    functional_testing_writer = LogWriter(destination_folder='testing/testing_logs/functional')
    structural_testing_writer = LogWriter(destination_folder='testing/testing_logs/structural')
    counter = 0

    def start(self):
        self.create_bots()
        self.testing(t_c.functional)
        # we reset the counter of lines
        self.counter = 0
        self.testing(t_c.structural)

    def create_bots(self):
        try:
            for index in range(3):
                if index == 0:
                    driver = webdriver.Edge()
                elif index == 1:
                    driver = webdriver.Chrome()
                else:
                    driver = webdriver.Firefox()
                driver.get(u.test_url_list[index])
                form_element = driver.find_elements_by_tag_name('form')
                bot_manager = BotsManager()
                bot_manager.parse_web_form(form_element)
                self.bots_list.append(bot_manager.botList[0])
        except:
            print('Fail to create the bots')
            raise Exception

    def testing(self, testing_type):
        try:
            if testing_type == t_c.functional:
                test_cases = t_c.functional_test_cases
            else:
                test_cases = t_c.structural_test_cases
            for test_case in test_cases:
                index = test_case[t_c.test_form_number] - 1
                bot = self.bots_list[index]
                self.state_preparation(bot.state, test_case)
                state_before = self.get_state_summary(bot.state)
                intent = test_case[t_c.test_case_message][t_c.intent][t_c.name]
                response = bot.findActionAndRun(intent)
                state_after = self.get_state_summary(bot_state)
                difference = {
                    u.slots: self.get_difference(state_before[u.slots], state_after[u.slots]),
                    t_c.spelling_state: self.get_difference(state_before[t_c.spelling_state], state_after[t_c.spelling_state]),
                    t_c.machine_parameters: self.get_difference(state_before[t_c.machine_parameters], state_after[t_c.machine_parameters])
                }
                self.write_test_case(testing_type=testing_type, initial_situation=state_before, test_case=test_case, effects=difference, response=response)
            if testing_type == t_c.structural:
                self.structural_testing_writer.start(display_summary=False)
            else:
                self.functional_testing_writer.start(display_summary=False)        
        except:
            print('Fail to complete the testing')
            if testing_type == t_c.structural:
                self.structural_testing_writer.start(display_summary=False)
            else:
                self.functional_testing_writer.start(display_summary=False)

    def state_preparation(self, state, test_case):
        try:
            general_keys = test_case.keys()
            for general_key in general_keys:
                if general_key == u.slots:
                    # we set the slots
                    for slot in test_case[u.slots]:
                        state.filling_procedure(slot[u.slot_name], slot[u.slot_value])
                elif general_key == t_c.spelling_state:
                    # we start by the spelling state
                    spelling_state = test_case[t_c.spelling_state]
                    keys = spelling_state.keys()
                    for key in keys:
                        if key == u.close_prompt_enabled:
                            state.set_close_prompt_enabled(spelling_state[u.close_prompt_enabled])
                        elif key == u.current_spelling_input_value:
                            state.set_current_spelling_input_value(spelling_state[u.current_spelling_input_value])
                        elif key == u.spelling_list:
                            state.spelling_state[u.spelling_list] = spelling_state[u.spelling_list]
                        elif key == u.waiting_intent:
                            state.set_waiting_intent(spelling_state[u.waiting_intent])
                        elif key == u.saved_spelling_fields:
                            state.add_spelling_field_to_save(spelling_state[u.saved_spelling_fields])
                            state.add_spelling_value_to_save(spelling_state[u.saved_spelling_values])
                elif general_key == t_c.machine_parameters:
                    # we continue with machine parameters
                    machine_parameters = test_case[t_c.machine_parameters]
                    keys = machine_parameters.keys()
                    for key in keys:
                        if key == u.submit_done:
                            state.set_submit_done(machine_parameters[u.submit_done])
                        elif key == u.reset_alarm_enabled:
                            state.set_reset_alarm_enabled(machine_parameters[u.reset_alarm_enabled])
                        elif key == u.submit_alarm_enabled:
                            state.set_submit_alarm_enabled(machine_parameters[u.submit_alarm_enabled])
                        elif key == u.possible_next_action:
                            state.set_possible_next_action(machine_parameters[u.possible_next_action])
                        elif key == u.warning_message:
                            state.set_warning_message(machine_parameters[u.warning_message])
        except:
            print('Fail to initialize the initial state for the test case')
            raise Exception

    def get_state_summary(self, state):
        # returns a dictionary of essential parameters that may change during the interaction
        try:
            summary = {
                u.slots: state.constructs[u.form_construct][u.slots],
                t_c.spelling_state: state.spelling_state,
                t_c.machine_parameters: state.machine_parameters
            }
            return summary
        except:
            print('Fail to get the state summary')
            raise Exception

    def get_difference(self, before, after):
        # receives two elements and returns only the parameters which chaged from before to after
        if type(before) == type([]):
            difference = []
            length = len(before)
            for index in range(length):
                if before[index][u.slot_value] != after[index][u.slot_value]:
                    difference.append(after[index])
            return difference
        # type(before) == type({})
        difference = {}
        keys = after.keys()
        for key in keys:
            if after[key] != before[key]:
                difference[key] = after[key]
        return difference

    def write_test_case(self, testing_type, initial_situation, test_case, effects, response):
        try:
            escape = '\n\t'

            fields_line = fn.get_pairs(initial_situation.form_slots()).replace('\n', ' ').replace('\t', ' ')
            spelling_line = self.get_string_from_dic(initial_situation[t_c.spelling_state])
            machine_line = self.get_string_from_dic(initial_situation[t_c.machine_parameters])
            init_line = f'Fields - {fields_line}{escape}\tSpelling state - {spelling_line}{escape}\tMachine parameters - {machine_line}'
            
            test_case_line = test_case[t_c.test_case_message][t_c.text]
            expected_line = test_case[t_c.result_expected]
            response_line = response.replace('\n', ' ').replace('\t', ' ')

            effects_fields = fn.get_pairs(effect[u.slots]).replace('\n', ' ').replace('\t', ' ')
            effects_spelling = self.get_string_from_dic(effects[t_c.spelling_state])
            effects_machine = self.get_string_from_dic(effects[t_c.machine_parameters])
            effects_line = f'Modified fields - {effects_fields}{escape}\tModified spelling attributes - {effects_spelling}{escape}\tModified machine parameters - {effects_machine}'

            line = f'Test case - {self.counter}{escape}[Initial situation: {init_line}] {escape}[Test case meaage: {test_case_line}] {escape}[Result expected: {expected_line}] {escape}[Result obtained: (effects: {effects_line}) (response:{response_line})]'
            self.counter += 1
            if testing_type == t_c.functional:
                self.functional_testing_writer.add_line(line)
            else:
                self.structural_testing_writer.add_line(line)
        except:
            print('Fail to generate and summary of the test case')
            raise Exception

    def get_string_from_dic(self, dic):
        try:
            string = ''
            for key in dic.keys():
                if string == '':
                    string = f'{key}: {dic[key]}'
                else:
                    string = f'{string}, {key}: {dic[key]}'
            return string
        except:
            print('Fail to get the string from the dictionary')
            raise Exception