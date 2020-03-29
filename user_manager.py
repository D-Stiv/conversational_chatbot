from random import randint, shuffle
import utility as u
import simulation_constants as cts
import json
import data_type_generator as gen


class User:
    def __init__(
        self,
        fields,
        choices_lists
    ):
        # we initialize the user
        self.fields = fields
        self.spelling_string = ''
        self.spelling_string_index = 0
        self.choices_lists = choices_lists
        self.data = self.initialize_data()
        self.counter = cts.Counter_trigger

    def initialize_data(self):
        try:
            data = {
                cts.filling: {},
                cts.interaction: {}
            }
            # we start with the filling files
            keys = cts.filling_keys
            files_names = cts.filling_files_names
            for index in range(len(keys)):
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
            for index in range(len(keys)):
                # we load a given json file which is a list
                path = f'./{cts.data_folder}/{cts.interaction_folder}/{files_names[index]}'
                with open(path, 'r') as fp:
                    data = json.load(fp)
                # we associate to the list loaded the corresponding key
                data[cts.interaction][keys[index]] = data
            return data
        except:
            print('Fail to initialize the data')
            raise Exception

    def get_choice_list(self, choice_name):
        try:
            return self.choices_lists[choice_name]
        except:
            print(f'Fail to get the list for the choice {choice_name}')
            raise Exception

    def get_filling_data(self, key):
        try:
            return self.data[cts.filling][key]
        except:
            print(f'Fail to get the filling data {key}')
            raise Exception

    def get_interaction_data(self, key):
        try:
            return self.data[cts.interaction][key]
        except:
            print(f'Fail to get the interaction data {key}')
            raise Exception

    def get_answer(self, dialogue_state):
        try:
            """we are mainly going to use the state to construct the response but 
            in some precise situtions the text coul be useful for an immediate answer"""
            return self.find_action_and_run(dialogue_state)
        except:
            print('Fail to get the user answer')
            raise Exception

    def construct_interaction_message(self):
        try:
            pass
        except:
            print(f'Fail to construct an interaction message')
            raise Exception

    def cunstruct_filling_message(self):
        try:
            pass
        except:
            print(f'Fail to construct a filling message')
            raise Exception


    def find_action_and_run(self, dialogue_state):
        try:
            state_name = self.get_state_name(dialogue_state)
            action_name = f'action_{state_name}'
            action = self.get_action(action_name)
            answer = action(dialogue_state[u.value_name], dialogue_state[u.value_type], dialogue_state[u.spelling])
            return answer
        except:
            print('Fail to find the action and run')

    def get_action(self, action_name):
        try:
            for action in self.actions:
                if action.__name__ == action_name:
                    return action
        except: 
            print(f'Fail to get the action {action_name}')
            raise Exception
    
    def action_state_00(self, value_name, value_type, spelling):
        try:
            pass
        except:
            print('Fail to get an answer for the state "00"')
            raise Exception

    def action_state_01(self, value_name, value_type, spelling):
        try:
            return self.action_state_01_04(value_name, value_type, spelling)
        except:
            print('Fail to get an answer for the state "01"')
            raise Exception
        
    def action_state_02(self, value_name, value_type, spelling):
        try:
            pass
        except:
            print('Fail to get an answer for the state "02"')
            raise Exception
        
    def action_state_03(self, value_name, value_type, spelling):
        try:
            pass
        except:
            print('Fail to get an answer for the state "03"')
            raise Exception
        
    def action_state_04(self, value_name, value_type, spelling):
        try:
            return self.action_state_01_04(value_name, value_type, spelling)
        except:
            print('Fail to get an answer for the state "04"')
            raise Exception
        
    def action_state_05(self, value_name, value_type, spelling):
        try:
            return self.action_state_05_06(value_name, value_type, spelling)
        except:
            print('Fail to get an answer for the state "05"')
            raise Exception
        
    def action_state_06(self, value_name, value_type, spelling):
        try:
            return self.action_state_05_06(value_name, value_type, spelling)
        except:
            print('Fail to get an answer for the state "06"')
            raise Exception
        
    def action_state_07(self, value_name, value_type, spelling):
        try:
            pass
        except:
            print('Fail to get an answer for the state "07"')
            raise Exception
        
    def action_state_08(self, value_name, value_type, spelling):
        try:
            pass
        except:
            print('Fail to get an answer for the state "08"')
            raise Exception
        
    def action_state_09(self, value_name, value_type, spelling):
        try:
            pass
        except:
            print('Fail to get an answer for the state "09"')
            raise Exception
          
    def action_state_10(self, value_name, value_type, spelling):
        try:
            pass
        except:
            print('Fail to get an answer for the state "10"')
            raise Exception
         
    def action_state_11(self, value_name, value_type, spelling):
        try:
            pass
        except:
            print('Fail to get an answer for the state "11"')
            raise Exception
         
    def action_state_12(self, value_name, value_type, spelling):
        try:
            pass
        except:
            print('Fail to get an answer for the state "12"')
            raise Exception
         
    def action_state_13(self, value_name, value_type, spelling):
        try:
            pass
        except:
            print('Fail to get an answer for the state "13"')
            raise Exception
       
    def action_state_01_04(self, value_name, value_type, spelling):
        try:
            pass
        except:
            print('Fail to get an answer for the state "01_04"')
            raise Exception
        
    def action_state_05_06(self, value_name, value_type, spelling):
        try:
            pass
        except:
            print('Fail to get an answer for the state "05_06"')
            raise Exception

    actions_list = [action_state_00, action_state_01, action_state_02, action_state_03, action_state_04,
        action_state_05, action_state_06, action_state_07, action_state_08, action_state_09, action_state_10,
        action_state_11, action_state_12, action_state_13]   


class BadUser(User):
    def __init__(
        self,
        slots
    ):
        # we initialize the user
        super().__init__(slots)
