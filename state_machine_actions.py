# Contains the actions of the state machine

import state_machine_data

class Actions:
    def __init__(
        self,
        user
        ):
        self.user = user

    def find_action_and_run(self, dialogue_state):
        try:
            pass
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
    
    def action_state_00(self):
        try:
            pass
        except:
            print('Fail to get an answer for the state "00"')
            raise Exception

    def action_state_01(self):
        try:
            return self.action_state_01_04()
        except:
            print('Fail to get an answer for the state "01"')
            raise Exception
        
    def action_state_02(self):
        try:
            pass
        except:
            print('Fail to get an answer for the state "02"')
            raise Exception
        
    def action_state_03(self):
        try:
            pass
        except:
            print('Fail to get an answer for the state "03"')
            raise Exception
        
    def action_state_04(self):
        try:
            return self.action_state_01_04()
        except:
            print('Fail to get an answer for the state "04"')
            raise Exception
        
    def action_state_05(self):
        try:
            return self.action_state_05_06()
        except:
            print('Fail to get an answer for the state "05"')
            raise Exception
        
    def action_state_06(self):
        try:
            return self.action_state_05_06
        except:
            print('Fail to get an answer for the state "06"')
            raise Exception
        
    def action_state_07(self):
        try:
            pass
        except:
            print('Fail to get an answer for the state "07"')
            raise Exception
        
    def action_state_08(self):
        try:
            pass
        except:
            print('Fail to get an answer for the state "08"')
            raise Exception
        
    def action_state_09(self):
        try:
            pass
        except:
            print('Fail to get an answer for the state "09"')
            raise Exception
          
    def action_state_10(self):
        try:
            pass
        except:
            print('Fail to get an answer for the state "10"')
            raise Exception
         
    def action_state_11(self):
        try:
            pass
        except:
            print('Fail to get an answer for the state "11"')
            raise Exception
         
    def action_state_12(self):
        try:
            pass
        except:
            print('Fail to get an answer for the state "12"')
            raise Exception
         
    def action_state_13(self):
        try:
            pass
        except:
            print('Fail to get an answer for the state "13"')
            raise Exception
       
    def action_state_01_04(self):
        try:
            pass
        except:
            print('Fail to get an answer for the state "01_04"')
            raise Exception
        
    def action_state_05_06(self):
        try:
            pass
        except:
            print('Fail to get an answer for the state "05_06"')
            raise Exception

    actions_list = [action_state_00, action_state_01, action_state_02, action_state_03, action_state_04,
        action_state_05, action_state_06, action_state_07, action_state_08, action_state_09, action_state_10,
        action_state_11, action_state_12, action_state_13]        