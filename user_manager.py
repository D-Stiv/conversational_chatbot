from random import randint, shuffle
import utility as u
import simulation_constants as cts
import json
import data_type_generator as gen
import state_machine_data as sm
import interaction_files_keys as ifk


class User:
    def __init__(
        self,
        text_fields,
        choices_lists
    ):
        # we initialize the user
        self.intents_data = cts.intents_list
        self.min_random_number = 0
        self.max_random_number = cts.inf

        self.text_fields = text_fields
        self.spelling_string = ''
        self.spelling_string_index = 0
        self.remaining_spelling_interruptions = cts.MAX_SPELLING_INTERRUPTIONS
        self.choices_lists = choices_lists  # dictionary where the keys are the value_name
        self.counter = cts.counter_trigger
        self.active_list = cts.initial_active_list
        self.dialogue_state = {}
        self.data = self.initialize_data()


    def initialize_data(self):
        try:
            # we start initializing the actions data putting the right intervals
            self.compute_intervals()
            # now we load the data
            data = {
                cts.filling: {},
                cts.interaction: {}
            }
            # we start with the filling files
            keys = cts.filling_keys
            files_names = cts.filling_files_names
            length = len(keys)
            for index in range(length):
                # we load a given json file which is a list
                path = f'./{cts.data_folder}/{cts.filling_folder}/{files_names[index]}'
                with open(path, 'r') as fp_list:
                    data_list = json.load(fp_list)
                # we shuffle the list
                shuffle(data_list)
                # we associate to the list loaded the corresponding key
                data[cts.filling][keys[index]] = data_list
            # we proceed with the interaction files
            keys = cts.interaction_keys
            files_names = cts.interaction_files_names
            length = len(keys)
            for index in range(length):
                # we load a given json file which is a list
                path = f'./{cts.data_folder}/{cts.interaction_folder}/{files_names[index]}'
                with open(path, 'r') as fp:
                    my_data = json.load(fp)
                # we associate to the list loaded the corresponding key
                data[cts.interaction][keys[index]] = my_data
            return data
        except:
            print('Fail to initialize the data')
            raise Exception

    def compute_intervals(self):
        try:
            R = randint(cts.min_R, cts.max_R)
            self.min_random_number = R + 1
            cumulative_total = R
            length = len(self.active_list)
            if self.counter > 0:
                shuffle(self.active_list)
            for index in range(length):
                intent_name = self.active_list[index]
                intent_data = self.get_intent_data(intent_name)
                intent_data[cts.min_number] = cumulative_total + 1
                intent_data[cts.max_number] = cumulative_total + intent_data[cts.cardinality_interval]
                cumulative_total += intent_data[cts.cardinality_interval]
            self.max_random_number = cumulative_total
        except:
            print('Fail to compute the interval for each intent')
            raise Exception

    def get_intent_data(self, intent_name):
        try:
            for intent_data in self.intents_data:
                if intent_data[cts.intent_name] == intent_name:
                    return intent_data
        except:
            print(f'Fail to get the data of the intent {intent_name}')
            raise Exception

    def update_active_list(self, intent_name):
        #  after the section of the intent to execute we decrease its remaining number of executions
        try:
            if intent_name in cts.interaction_keys[1:-3]:   # interaction_keys is also the list of the intents, we extract the non_essential once
                self.counter -= 1
            intent_data = self.get_intent_data(intent_name)
            intent_data[cts.max_execution] -= 1
            if intent_data[cts.max_execution] == 0:
                # we update the interval
                intent_data[cts.min_number] = 0
                intent_data[cts.max_number] = 0
                # we remove it from the active list
                self.active_list.remove(intent_name)
                # given that the active list have been modified we have to recompute the intervals
                self.compute_intervals()
        except:
            print(f'Fail to remove the intent {intent_name} in the active list')
            raise Exception
    
    def select_intent_and_execute(self, prohibited_intents=cts.fill_form):
        # randomly selects an intent in the active list to be executed
        try:
            if len(self.text_fields) == 0:
                intents_using_text_fields = [cts.explain_field, cts.modify_value_field, cts.repeat_value_field]
                prohibited_intents = prohibited_intents + intents_using_text_fields
            number = randint(self.min_random_number, self.max_random_number)
            for intent_name in self.active_list:
                intent_data = self.get_intent_data(intent_name)
                # we verify if the random number is in the range of this intent
                if number in range(intent_data[cts.min_number], intent_data[cts.max_number]+1):
                    intent_name_selected = intent_name
                    break
            if prohibited_intents is not None:
                while intent_name_selected in prohibited_intents:
                    number = randint(self.min_random_number, self.max_random_number)
                    for intent_name in self.active_list:
                        intent_data = self.get_intent_data(intent_name)
                        # we verify if the random number is in the range of this intent
                        if number in range(intent_data[cts.min_number], intent_data[cts.max_number]+1):
                            intent_name_selected = intent_name
                            break
            answer = self.construct_answer(intent_name_selected)
            return answer
        except:
            print('Fail to select the intent to be executed')
            raise Exception

    def get_choice_list(self, choice_name):
        return self.choices_lists[choice_name]

    def get_answer(self, dialogue_state):
        try:
            """we are mainly going to use the state to construct the response but 
            in some precise situtions the text coul be useful for an immediate answer"""
            # we verify if the spelling have been interrupted to decrease the counter
            if dialogue_state[u.spelling_interrupted]:
                self.remaining_spelling_interruptions -= 1
            # we set the dialogue state which will be used by the action_states and the actions
            self.dialogue_state = dialogue_state
            state_name = self.get_state_name()
            if state_name is None:
                # we will activate the initial state
                state_name = sm.state_00[u.state_name]
            action = self.get_action_state(state_name)
            answer = action(self)
            return answer
        except:
            print('Fail to get the user answer')
            # we return a contant string only to avoid interrupting the dialogue
            string = 'fill the form'
            return string
        
    def reset_spelling_data(self):
        self.spelling_string = ''
        self.spelling_string_index = 0

    def construct_answer(self, intent_name):
        # receives the name of an intent and perform the standard operation for generating a 
        # message coherent with that intent
        try:
            self.update_active_list(intent_name)
            intent_function = self.get_intent_function(intent_name)
            answer = intent_function(self)
            return answer
        except:
            print(f'Fail to construct an answer for the intent {intent_name}')
            raise Exception

    def get_interaction_message(self, file_name, key=''):
        # when key is not void, the file contains a dictionary and we should go to the corresponding 
        # key. when key is void, the file contains a list. The file_name here is without extension
        try:
            if u.DEBUG:
                print(f'file_name: {file_name}')
            if key != '':
                elements = self.data[cts.interaction][file_name][key]
            else:
                elements = self.data[cts.interaction][file_name]
            element = gen.get_random_value(elements)
            return element
        except:
            print(f'Fail to construct an interaction message')
            raise Exception

    def get_filling_message(self, file_name):
        # For the moment all the filling elements are lists
        try:
            elements = self.data[cts.filling][file_name]
            element = gen.get_random_value(elements)
            return element
        except:
            print(f'Fail to construct a filling message')
            raise Exception

    def get_state_name(self):
        # gets the name of the state in the state machine corresponding to dialogue state
        try:
            for state in sm.states_list:
                found = True
                for key in sm.keys_list:
                    if self.dialogue_state[key] != state[key]:
                        found = False
                        break
                if found:
                    state_name = state[u.state_name]
                    return state_name
            # there is no state corresponding to the dialogue state
            return None
        except:
            print('Fail to get the neme of the state')
            raise Exception

    def get_action_state(self, state_name):
        # given the name of a state of the state machine, finds the corresponding action in the list 
        # of actions state and return
        try:
            action_state_name = f'action_{state_name}'
            for action_state in self.actions_state_list:
                if action_state.__name__ == action_state_name:
                    return action_state
        except: 
            print(f'Fail to get the action with name {state_name}')
            raise Exception

    def get_intent_function(self, intent_name):
        # given the name of an intent, finds the corresponding intent in the list 
        # of intents state and return
        try:
            intent_function_name =f'intent_{intent_name}'
            for intent_function in self.intents_functions_list:
                if intent_function.__name__ == intent_function_name:
                    return intent_function
        except: 
            print(f'Fail to get the intent with name {intent_name}')
            raise Exception
    
    def action_state_00(self):
        try:
            intent_name = cts.fill_form
            return self.construct_answer(intent_name)
        except:
            print('Fail to get an answer for the state "00"')
            raise Exception

    def action_state_01(self):
        try:
            if self.counter <= 0 or len(self.active_list) <= len(cts.essential_intents):
                intent_name = cts.complete_field
                return self.construct_answer(intent_name)
            prohibited_intents = [u.spelling_action]
            return self.select_intent_and_execute(prohibited_intents)
        except:
            print('Fail to get an answer for the state "01"')
            raise Exception
        
    def action_state_02(self):
        try:
            if self.counter <= 0 or len(self.active_list) <= len(cts.essential_intents):
                intent_name = u.spelling_action
                return self.construct_answer(intent_name)
            prohibited_intents = [cts.complete_field]
            return self.select_intent_and_execute(prohibited_intents)
        except:
            print('Fail to get an answer for the state "02"')
            raise Exception
        
    def action_state_03(self):
        try:
            if self.counter <= 0 or len(self.active_list) <= len(cts.essential_intents):
                intent_name = cts.affirm
                return self.construct_answer(intent_name)
            # we have only two possibilities: 0- affirm, 1-deny.
            number = randint(0, 1)
            if number == 0:
                intent_name = cts.affirm
            else:
                intent_name = cts.deny
            return self.construct_answer(intent_name)
        except:
            print('Fail to get an answer for the state "03"')
            raise Exception
        
    def action_state_04(self):
        try:
            if self.counter <= 0 or len(self.active_list) <= len(cts.essential_intents):
                intent_name = cts.complete_field
                return self.construct_answer(intent_name)
            prohibited_intents = [u.spelling_action]
            return self.select_intent_and_execute(prohibited_intents)
        except:
            print('Fail to get an answer for the state "04"')
            raise Exception
        
    def action_state_05(self):
        try:
            if self.counter <= 0 or len(self.active_list) <= len(cts.essential_intents):
                intent_name = cts.complete_field
                return self.construct_answer(intent_name)
            prohibited_intents = [u.spelling_action]
            return self.select_intent_and_execute(prohibited_intents)
        except:
            print('Fail to get an answer for the state "05"')
            raise Exception
        
    def action_state_06(self):
        try:
            if self.counter <= 0 or len(self.active_list) <= len(cts.essential_intents):
                intent_name = cts.submit_form
                return self.construct_answer(intent_name)
            prohibited_intents = [u.spelling_action]
            return self.select_intent_and_execute(prohibited_intents)
        except:
            print('Fail to get an answer for the state "06"')
            raise Exception
        
    def action_state_07(self):
        try:
            if self.counter <= 0 or len(self.active_list) <= len(cts.essential_intents):
                intent_name = cts.affirm
                return self.construct_answer(intent_name)
            prohibited_intents = [u.spelling_action, cts.complete_field]
            return self.select_intent_and_execute(prohibited_intents)
        except:
            print('Fail to get an answer for the state "07"')
            raise Exception
        
    def action_state_08(self):
        """if the answer is '0' we close the session, otherwise we open a new dialogue. There is 
        another control outside to limit the number of dialogues in a session, so the tendency 
        is to open a new dialogue in order to have more samples."""
        try:
            number = randint(0, 10)
            if cts.use_terminal:
                text = '\n[ALERT: Would you like to start a new dialogue ?\t1- Yes\t0- No\n>>> Response: '
                answer = input(text)
            else:
                #answer = f'{number}'
                answer = '1'
            return answer
        except:
            print('Fail to get an answer for the state "08"')
            raise Exception
        
    def action_state_09(self):
        try:
            if self.counter <= 0 or len(self.active_list) <= len(cts.essential_intents):
                intent_name = cts.deny
                return self.construct_answer(intent_name)
            prohibited_intents = [u.spelling_action]
            return self.select_intent_and_execute(prohibited_intents)
        except:
            print('Fail to get an answer for the state "09"')
            raise Exception
          
    def action_state_10(self):
        try:
            if self.counter <= 0 or len(self.active_list) <= len(cts.essential_intents):
                intent_name = u.spelling_action
                return self.construct_answer(intent_name)
            prohibited_intents = [cts.complete_field]
            return self.select_intent_and_execute(prohibited_intents)
        except:
            print('Fail to get an answer for the state "10"')
            raise Exception
         
    def action_state_11(self):
        try:
            if self.counter <= 0 or self.remaining_spelling_interruptions <= 0 or len(self.active_list) <= len(cts.essential_intents):
                intent_name = u.spelling_action
                return self.construct_answer(intent_name)
            prohibited_intents = [cts.complete_field]
            return self.select_intent_and_execute(prohibited_intents)
        except:
            print('Fail to get an answer for the state "11"')
            raise Exception
         
    def action_state_12(self):
        try:
            if self.counter <= 0 or self.remaining_spelling_interruptions <= 0 or len(self.active_list) <= len(cts.essential_intents):
                intent_name = u.spelling_action
                return self.construct_answer(intent_name)
            prohibited_intents = [cts.complete_field]
            return self.select_intent_and_execute(prohibited_intents)
        except:
            print('Fail to get an answer for the state "12"')
            raise Exception
         
    def action_state_13(self):
        try:
            if self.counter <= 0 or len(self.active_list) <= len(cts.essential_intents):
                intent_name = cts.affirm
                return self.construct_answer(intent_name)
            # we have only two possibilities: 0- affirm, 1-deny.
            number = randint(0, 1)
            if number == 0:
                intent_name = cts.affirm
            else:
                intent_name = cts.deny
            return self.construct_answer(intent_name)
        except:
            print('Fail to get an answer for the state "13"')
            raise Exception

    def action_state_14(self):
        try:
            if self.counter <= 0 or len(self.active_list) <= len(cts.essential_intents):
                intent_name = cts.complete_field
                return self.construct_answer(intent_name)
            prohibited_intents = [u.spelling_action]
            return self.select_intent_and_execute(prohibited_intents)
        except:
            print('Fail to get an answer for the state "14"')
            raise Exception

    def action_state_15(self):
        try:
            if self.counter <= 0 or len(self.active_list) <= len(cts.essential_intents):
                intent_name = cts.deny
                return self.construct_answer(intent_name)
            prohibited_intents = [u.spelling_action]
            return self.select_intent_and_execute(prohibited_intents)
        except:
            print('Fail to get an answer for the state "15"')
            raise Exception

    def action_state_16(self):
        try:
            if self.counter <= 0 or len(self.active_list) <= len(cts.essential_intents):
                intent_name = cts.submit_form
                return self.construct_answer(intent_name)
            prohibited_intents = [u.spelling_action]
            return self.select_intent_and_execute(prohibited_intents)
        except:
            print('Fail to get an answer for the state "15"')
            raise Exception

    actions_state_list = [action_state_00, action_state_01, action_state_02, action_state_03, action_state_04,
        action_state_05, action_state_06, action_state_07, action_state_08, action_state_09, action_state_10,
        action_state_11, action_state_12, action_state_13, action_state_14, action_state_15, action_state_16]  


    def get_not_choice_value(self, value_type, field):
        try:
            if value_type == u.date:
                value = gen.generate_date(self.get_filling_message(cts.months))
            elif value_type == u.time:
                value = gen.generate_time()
            elif value_type == u.text_area:
                value = self.get_filling_message(cts.messages)
            elif value_type == u.tel:
                value = gen.generate_phone_number()
            elif value_type == u.email:
                name = self.get_filling_message(cts.names)
                value = gen.generate_email(name)
            elif value_type == u.password:
                name = self.get_filling_message(cts.names)
                value = gen.generate_password(name)
            elif value_type in u.number_types_list:
                min_value = self.dialogue_state[u.min_value]
                max_value = self.dialogue_state[u.max_value]
                if value_type in [u.integer, u.number]:
                    value = gen.generate_integer(min_value, max_value)
                else:
                    # decimal
                    precision = self.dialogue_state[u.precision]
                    value = gen.generate_decimal(precision, min_value, max_value)
            elif 'address' in field:
                # probably a place address
                value = gen.generate_place_address(self.get_filling_message(cts.address_names))
            elif 'city' in field:
                # probably a city
                value = self.get_filling_message(cts.cities)
            elif 'country' in field:
                # probably a country
                value = self.get_filling_message(cts.countries)
            elif 'name' in field:
                # probably a person name
                value = self.get_filling_message(cts.names)
            else:
                # can be anything but we decide to put a person name
                value = self.get_filling_message(cts.names)
            return value
        except:
            print('Fail to get a not choice value')
            raise Exception
            
    def intent_complete_field(self):
        # we have mainly two cases, when the type is choice and when the type is not a choice
        try:
            value_type = self.dialogue_state[u.value_type]
            value_name = self.dialogue_state[u.value_name]
            field = self.dialogue_state[u.slot_name].lower()
            if value_type in u.choices_type_list:
                choice_list = self.choices_lists[value_name]
                if value_type == u.checkbox:
                    """value type is checbox so we can have more than one choice, for the simulation the maximum is two
                    we have 5 cases: 0- value, 1- name_value, 2- value_name, 3- two_values, 4- name_value_value.
                    The first 3 are linked to the fact that we decide to choose only one value, so identical to radio 
                    and dropdown. the last two are related to the selection of two values"""
                    number = randint(0, 4)
                    if number in range(3, 5):
                        # 3 or 4
                        values = gen.get_random_value(choice_list, number=2)
                        if number == 3:
                            # two_values
                            file_key = ifk.two_values
                            sentence = self.get_interaction_message(cts.complete_field, file_key)
                            answer = sentence.format(values[0], values[1])
                        else:
                            # 4, name_value_value
                            file_key = ifk.name_value_value
                            sentence = self.get_interaction_message(cts.complete_field, file_key)
                            answer = sentence.format(field, values[0], values[1])
                        return answer
                # 0, 1, 2 of the checkbox + dropdown + radio
                # we have only one choice 
                value = gen.get_random_value(choice_list)
                # we select a sentence with one slot name or two slots (one name one value)
                # so in total three cases: 0 - value, 1 - value_name, 2 - name_value
                number = randint(0, 2)
                if number == 0:
                    # one value
                    file_key = ifk.one_name
                    sentence = self.get_interaction_message(cts.complete_field, file_key)
                    answer = sentence.format(value)
                elif number == 1:
                    # value_name
                    file_key = ifk.value_name
                    sentence = self.get_interaction_message(cts.complete_field, file_key)
                    answer = sentence.format(value, field)
                else:
                    # 2, name_value
                    file_key = ifk.name_value
                    sentence = self.get_interaction_message(cts.complete_field, file_key)
                    answer = sentence.format(field, value)
                return answer
            # we are not in a choice, we should look if it is date, time, address not email, name, country, city
            value = self.get_not_choice_value(value_type, field)
            # we select a sentence with one slot name or two slots (one name one value)
            # so in total three cases: 0 - value, 1 - value_name, 2 - name_value
            number = randint(0, 2)
            if number == 0:
                # one_value
                file_key = ifk.one_value
                sentence = self.get_interaction_message(cts.complete_field, file_key)
                answer = sentence.format(value)
            elif number == 1:
                # value_name
                file_key = ifk.value_name
                sentence = self.get_interaction_message(cts.complete_field, file_key)
                answer = sentence.format(value, field)
            else:
                # 2, name_value
                file_key = ifk.name_value
                sentence = self.get_interaction_message(cts.complete_field, file_key)
                answer = sentence.format(field, value)
            return answer
        except:
            print('Fail in finding a message to ask to complete a field')
            raise Exception

    def intent_spelling(self):
        # we have two cases, when the spelling did not start already and when the spelling already started
        try:
            value_type = self.dialogue_state[u.value_type]
            field = self.dialogue_state[u.slot_name].lower()
            if self.spelling_string == '':
                # we are not in a choice, we should look if it is date, time, address not email, name, country, city
                value = self.get_not_choice_value(value_type, field)
                self.spelling_string = value
                self.spelling_string_index = -1
                print(f'[User - Input to be inserted by spelling: {value}]')
            # we update first the spelling data anthen we analyze the char
            self.spelling_string_index += 1
            if self.spelling_string_index >= len(self.spelling_string):
                self.reset_spelling_data()
                char = gen.get_random_value(u.terminator)
                return char
            char = self.spelling_string[self.spelling_string_index]
            # now we analyze the char, mainly the special characters
            if char in u.spec_char_symbol:
                index = u.spec_char_symbol.index(char)
                char = u.special_characters[index]
            return char
        except:
            print('Fail in finding a message to spell a field')
            raise Exception

    def intent_submit_form(self):
        # we select an expression to ask the submit and we return 
        answer = self.get_interaction_message(cts.submit_form)
        return answer

    def intent_affirm(self):
        # we select an expression to affirm and we return
        answer = self.get_interaction_message(cts.affirm)
        return answer

    def intent_deny(self):
        # if we started the spelling we have to update the spelling data
        self.reset_spelling_data()
        # we select an expression to deny and we return
        answer = self.get_interaction_message(cts.deny)
        return answer

    def intent_explain_field(self):
        # we select a sentence from the corresponding file in the database 
        try:
            field = gen.get_random_value(self.text_fields)
            sentence = self.get_interaction_message(cts.explain_field)
            answer = sentence.format(field)
            return answer
        except:
            print('Fail to extract a sentence to ask an explanation about a field')
            raise Exception

    def intent_fill_form(self):
        # we select a sentence from the corresponding file in the database 
        answer = self.get_interaction_message(cts.fill_form)
        return answer

    def intent_give_all_remaining_fields(self):
        # we select a sentence from the corresponding file in the database 
        answer = self.get_interaction_message(cts.give_all_remaining_fields)
        return answer

    def intent_give_remaining_optional_fields(self):
        # we select a sentence from the corresponding file in the database 
        answer = self.get_interaction_message(cts.give_remaining_optional_fields)
        return answer

    def intent_give_remaining_required_fields(self):
        # we select a sentence from the corresponding file in the database 
        answer = self.get_interaction_message(cts.give_remaining_required_fields)
        return answer

    def intent_modify_value_field(self):
        """we select the number and type of slots and we select a sentence 
        from the corresponding file in the database 
        there are 4 cases: 0- zero, 1- one_name, 2- name_value, 3- two_names"""
        try:
            length = len(self.text_fields)
            if length >= 3:
                upper = 3
            else:
                upper = 2
            number = randint(0, upper)
            if number == 0:
                answer = self.get_interaction_message(cts.repeat_value_field, ifk.zero)
            elif number == 1:
                field = gen.get_random_value(self.text_fields)
                sentence = self.get_interaction_message(cts.repeat_value_field, ifk.one_name)
                answer = sentence.format(field)
            elif number == 2:
                field = gen.get_random_value(self.text_fields)
                value = self.get_filling_message(cts.possible_fields)
                sentence = self.get_interaction_message(cts.repeat_value_field, ifk.name_value)
                answer = sentence.format(field, value)
            else:
                # 3, two_names
                fields = gen.get_random_value(self.text_fields, number=2)
                sentence = self.get_interaction_message(cts.repeat_value_field, ifk.two_names)
                answer = sentence.format(fields[0], fields[1])
            return answer
        except:
            print('Fail in finding a message to ask to modify the value of a field')
            raise Exception

    def intent_repeat_all_fields(self):
        # we select a sentence from the corresponding file in the database 
        answer = self.get_interaction_message(cts.repeat_all_fields)
        return answer

    def intent_repeat_optional_fields(self):
        # we select a sentence from the corresponding file in the database 
        answer = self.get_interaction_message(cts.repeat_optional_fields)
        return answer

    def intent_repeat_required_fields(self):
        # we select a sentence from the corresponding file in the database 
        answer = self.get_interaction_message(cts.repeat_required_fields)
        return answer

    def intent_repeat_form_explanation(self):
        # we select a sentence from the corresponding file in the database 
        answer = self.get_interaction_message(cts.repeat_form_explanation)
        return answer

    def intent_repeat_value_field(self):
        """we select the number and type of slots and we select a sentence 
        from the corresponding file in the database 
        there are 3 cases: 0- zero, 1- one_name, 2- two_names"""
        try:
            length = len(self.text_fields)
            if length >= 2:
                upper = 2
            else:
                upper = 1
            number = randint(0, upper)
            if number == 0:
                answer = self.get_interaction_message(cts.repeat_value_field, ifk.zero)
            elif number == 1:
                field = gen.get_random_value(self.text_fields)
                sentence = self.get_interaction_message(cts.repeat_value_field, ifk.one_name)
                answer = sentence.format(field)
            else:
                # 2, two_names
                fields = gen.get_random_value(self.text_fields, number=2)
                sentence = self.get_interaction_message(cts.repeat_value_field, ifk.two_names)
                answer = sentence.format(fields[0], fields[1])
            return answer
        except:
            print('Fail in finding a message to ask to repeat the value of a field')
            raise Exception

    def intent_reset_all_fields(self):
        # we select a sentence from the corresponding file in the database 
        answer = self.get_interaction_message(cts.reset_all_fields)
        return answer

    def intent_skip_field(self):
        # we select a sentence from the corresponding file in the database 
        answer = self.get_interaction_message(cts.skip_field)
        return answer

    def intent_verify_presence_field(self):
        # we select the number and type of slots and we select a sentence 
        # from the corresponding file in the database 
        try:
            field = self.get_filling_message(cts.possible_fields)
            sentence = self.get_interaction_message(cts.verify_presence_field)
            answer = sentence.format(field)
            return answer
        except:
            print('Fail in finding a message to ask to verify the presence of a field')
            raise Exception

    def intent_verify_value_for_completed_fields(self):
        # we select a sentence from the corresponding file in the database 
        answer = self.get_interaction_message(cts.verify_value_for_completed_fields)
        return answer


    essential_intents_funcions = [intent_complete_field, intent_spelling,
                        intent_submit_form, intent_affirm, intent_deny]
    non_essential_intents_funcions = [intent_explain_field, intent_fill_form, intent_give_all_remaining_fields,
                            intent_give_remaining_optional_fields, intent_give_remaining_required_fields, intent_modify_value_field,
                            intent_repeat_all_fields, intent_repeat_optional_fields, intent_repeat_required_fields,
                            intent_repeat_form_explanation, intent_repeat_value_field, intent_reset_all_fields, intent_skip_field,
                            intent_verify_presence_field, intent_verify_value_for_completed_fields]

    intents_functions_list = essential_intents_funcions + non_essential_intents_funcions



class BadUser(User):
    def __init__(
        self,
        slots
    ):
        # we initialize the user
        super().__init__(slots)
