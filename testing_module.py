# testing module

import test_cases as t_c
import utility as u
from writers import LogWriter
from choice_bot import BotsManager
from selenium import webdriver
import functions as fn
import copy

structural_summary = '\tTesting log for *structural* test cases'
functional_summary = '\tTesting log for *functional* test cases'

class Testing:
    bots_list = []
    functional_testing_writer = LogWriter(destination_folder='testing_logs/functional')
    structural_testing_writer = LogWriter(destination_folder='testing_logs/structural')
    counter = 0

    def start(self):
        self.create_bots()
        self.testing(t_c.functional)
        # we reset the whole environement
        self.reset()
        self.testing(t_c.structural)
    
    def reset(self):
        self.counter = 0
        for bot in self.bots_list:
            webdriver = bot.state.form_element.parent
            webdriver.close()
        self.bots_list = []
        self.create_bots()

    def create_bots(self):
        try:
            for index in range(3):
                if index == 0:
                    driver = webdriver.Edge()
                elif index == 1:
                    driver = webdriver.Chrome()
                else:
                    driver = webdriver.Edge()
                driver.get(u.test_url_list[index])
                driver.minimize_window()
                form_element = driver.find_element_by_tag_name('form')
                bot_manager = BotsManager()
                bot_manager.parse_web_form(form_element)
                self.bots_list.append(bot_manager.botList[0])
        except:
            print('Fail to create the bots')
            raise Exception

    def testing(self, testing_type):
        try:
            # we select the type of test cases: functional vs structural
            if testing_type == t_c.functional:
                test_cases = t_c.functional_test_cases
            else:
                test_cases = t_c.structural_test_cases
            # we analyze each test case
            for test_case in test_cases:
                if u.DEBUG:
                    print(f'>>>>> testing_type: {testing_type} - test_case_id: {test_case[t_c.message_id]} <<<<<<<')
                # we select the rigth browser
                index = test_case[t_c.test_form_number] - 1
                bot = self.bots_list[index]
                try:
                    # we initialize the state of the bot
                    self.state_preparation(bot.state, test_case)
                    # we add the test case message
                    bot.state.message_history.append(test_case[t_c.test_case_message])
                    # we perform the testing and we right the corresponding info in the file
                    state_before = self.get_state_summary(bot.state)
                    state_before = copy.deepcopy(state_before)
                    intent = test_case[t_c.test_case_message][t_c.intent][t_c.name]
                    response = bot.findActionAndRun(intent)
                    state_after = self.get_state_summary(bot.state)
                    difference = {
                        u.slots: self.get_difference(state_before[u.slots], state_after[u.slots]),
                        t_c.spelling_state: self.get_difference(state_before[t_c.spelling_state], state_after[t_c.spelling_state]),
                        t_c.machine_parameters: self.get_difference(state_before[t_c.machine_parameters], state_after[t_c.machine_parameters])
                    }
                    self.write_test_case(testing_type=testing_type, initial_situation=state_before, test_case=test_case, effects=difference, response=response)
                except:
                    pass
            # we write the testing log
            if testing_type == t_c.structural:
                self.structural_testing_writer.start(display_summary=structural_summary)
            else:
                self.functional_testing_writer.start(display_summary=functional_summary)        
        except:
            print('Fail to complete the testing')
            if testing_type == t_c.structural:
                self.structural_testing_writer.start(display_summary=structural_summary)
            else:
                self.functional_testing_writer.start(display_summary=functional_summary)

    def state_preparation(self, state, test_case):
        try:
            # test_case has keys message_id, test_form_number, initial_state, test_case_message, result_expected
            test_cases_keys = test_case.keys()
            if t_c.initial_state in test_cases_keys:
                initial_state = test_case[t_c.initial_state]
            else:
                return
            general_keys = initial_state.keys()
            for general_key in general_keys:
                if general_key == u.slots:
                    # we set the slots
                    for slot in initial_state[u.slots]:
                        state.filling_procedure(slot[u.slot_name], slot[u.slot_value])
                elif general_key == t_c.spelling_state:
                    # we start by the spelling state
                    spelling_state = initial_state[t_c.spelling_state]
                    keys = spelling_state.keys()
                    for key in keys:
                        if key == u.close_prompt_enabled:
                            state.set_close_prompt_enabled(spelling_state[u.close_prompt_enabled])
                        elif key == u.after_spelling:
                            state.set_after_spelling(spelling_state[u.after_spelling])
                        elif key == u.current_spelling_input_value:
                            state.set_current_spelling_input_value(spelling_state[u.current_spelling_input_value])
                        elif key == u.spelling_interrupted:
                            state.set_spelling_interrupted(spelling_state[u.spelling_interrupted])
                        elif key == u.spelling_list:
                            state.spelling_state[u.spelling_list] = spelling_state[u.spelling_list]
                        elif key == u.waiting_intent:
                            state.set_waiting_intent(spelling_state[u.waiting_intent])
                        elif key == u.saved_spelling_fields:
                            state.add_spelling_field_to_save(spelling_state[u.saved_spelling_fields])
                            state.add_spelling_value_to_save(spelling_state[u.saved_spelling_values])
                elif general_key == t_c.machine_parameters:
                    # we continue with machine parameters
                    machine_parameters = initial_state[t_c.machine_parameters]
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
            return
        except:
            print('Fail to initialize the initial state for the test case')
            

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
            

    def get_difference(self, before, after):
        # receives two elements and returns only the parameters which chaged from before to after
        try:
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
        except:
            print('Fail to get the difference')
            

    def write_test_case(self, testing_type, initial_situation, test_case, effects, response):
        try:
            escape = '\n\t'

            fields_line = fn.get_pairs(initial_situation[u.slots]).replace('\n', '; ').replace('\t', ' ')
            spelling_line = self.get_string_from_dic(initial_situation[t_c.spelling_state])
            machine_line = self.get_string_from_dic(initial_situation[t_c.machine_parameters])
            init_line = f'Fields - {fields_line}{escape}\tSpelling state - {spelling_line}{escape}\tMachine parameters - {machine_line}'
            
            test_case_line = test_case[t_c.test_case_message][t_c.text]
            expected_line = test_case[t_c.result_expected]
            response_line = response.replace('\n', ' ').replace('\t', ' ')
            effects_keys = effects.keys()
            effects_line = ''
            for effects_key in effects_keys:
                if effects_key == u.slots and effects[u.slots] != []:
                    effects_fields = fn.get_pairs(effects[u.slots]).replace('\n', '; ').replace('\t', ' ')
                    effects_line = f'Modified fields - {effects_fields}'
                elif effects_key == t_c.spelling_state and effects[t_c.spelling_state] != {}:
                    effects_spelling = self.get_string_from_dic(effects[t_c.spelling_state])
                    effects_line = f'{effects_line}{escape}\tModified spelling attributes - {effects_spelling}'
                elif effects_key == t_c.machine_parameters and effects[t_c.machine_parameters] != {}:
                    effects_machine = self.get_string_from_dic(effects[t_c.machine_parameters])
                    effects_line = f'{effects_line}{escape}\tModified machine parameters - {effects_machine}'
            if effects_line == '':
                line = f'<{test_case[t_c.message_id]}> {testing_type} test case - {self.counter}{escape}[Initial situation: {init_line}] {escape}[Test case meaage: {test_case_line}] {escape}[Result expected: {expected_line}] {escape}[Result obtained: (response:{response_line})]'
            else:
                line = f'<{test_case[t_c.message_id]}> {testing_type} test case - {self.counter}{escape}[Initial situation: {init_line}] {escape}[Test case meaage: {test_case_line}] {escape}[Result expected: {expected_line}] {escape}[Result obtained: (effects: {effects_line}) (response:{response_line})]'
            self.counter += 1
            if testing_type == t_c.functional:
                self.functional_testing_writer.add_line(line)
            else:
                self.structural_testing_writer.add_line(line)
        except:
            print(f'Fail to generate and summary of the test case with id {test_case[t_c.message_id]}')

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
            