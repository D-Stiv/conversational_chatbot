# CLASS
# to write the logs 
# the log_writer writes the summary of the interaction (from the beginning till the end) 
# with some needed statistics

import utility as u
from writer_interface import Writer
from decimal import Decimal

class LogWriter(Writer):
    def __init__(
        self,
        destination_folder = u.logs_folder,
        file_type = 'log'
    ):
        super().__init__(destination_folder, file_type)
        self.summary_string = ''
        self.conversation_string = ''
        self.number_turns_chatbot = 0
        self.number_turns_user = 0

    def start(self, display_summary=True):
        header = self.construct_header()
        summary = self.construct_summary()
        conv_log = self.construct_conv_log()
        if display_summary:
            text = f'{header}\n\n{summary}\n\n{conv_log}\n\n'
        else:
            text = f'{header}\n\n{conv_log}\n\n'
        self.create_file(text)

    def add_chatbot_line(self, line):
        self.conversation_string = f'{self.conversation_string}\n{line}'
        self.number_turns_chatbot += 1

    def add_user_line(self, line):
        self.conversation_string = f'{self.conversation_string}\n{line}'
        self.number_turns_user += 1

    def add_line(self, line):
        self.conversation_string = f'{self.conversation_string}\n{line}'

    def construct_summary(self):
        total = self.number_turns_chatbot + self.number_turns_user
        perc_chatbot = round(100*(Decimal(self.number_turns_chatbot)/Decimal(total)), 2)
        perc_user = round(100*(Decimal(self.number_turns_user)/Decimal(total)), 2)
        summary_content = (f'The dialogue counts a total of {total} interactions from which {perc_chatbot}% ({self.number_turns_chatbot} turns) ' + 
                f' made by the chatbot and {perc_user}% ({self.number_turns_user} turns) made by the user.')
        summary = f'SUMMARY\n\n{summary_content}'
        return summary

    def construct_conv_log(self):
        conv_log = f'CONVERSATION LOG\n{self.conversation_string}'
        return conv_log


class ReportWriter(Writer):
    
    def __init__(
        self,
        states_list,
        destination_folder = u.reports_folder,
        file_type = 'report'
    ):
        super().__init__(destination_folder, file_type)
        self.counter = 0
        self.states_list = states_list
        self.text = '{}.\t' # form elements, constructs, messages
        self.spelling_length = 0


    def start(self):
        try:
            header = self.construct_header()
            number = len(self.states_list)
            if number == 0:
                summary = 'SUMMARY\n\n\tThe is no completed session'
            else:
                summary = f'SUMMARY\n\n\tThere are {number} completed sessions'
            report_log = self.construct_report_log()
            text = f'{header}\n\n{summary}\n\n{report_log}\n\n'
            self.create_file(text)
        except:
            print('Fail to construct the report')
            raise Exception

    def add_line(self, line, string='', tab=''):
        try:
            if string == '':
                string = f'{self.text.format(self.counter)}{tab}{line}'
            else:
                string = f'{string}\n{self.text.format(self.counter)}{tab}{line}'
            self.increase_counter()
            return string
        except:
            print('Fail to add line')
            raise Exception
    
    def increase_counter(self, step=1):
        self.counter += step

    def construct_report_log(self):
        try:
            report_log = f'REPORT LOG{self.get_report_log()}'        
            return report_log
        except:
            print('Fail to construct the report log')
            raise Exception

    def get_report_log(self):
        try:
            tab = '\t'
            report_log =''
            for index in range(len(self.states_list)):
                state = self.states_list[index]
                dialogue = f'\n{self.text.format(self.counter)}--- DIALOGUE {index + 1} ---\n'
                self.increase_counter()
                form_element_content = f'{self.text.format(self.counter)}I- Form element\n{self.get_form_element(state.form_element, tab)}'
                slots_content = f'{self.text.format(self.counter)}II- Slots\n{self.get_slots(state.constructs["form"]["slots"], tab)}'
                messages_content = f'{self.text.format(self.counter)}III-Messages{self.get_messages(state.message_history, tab)}'
                statistics_content = f'{self.text.format(self.counter)}IV-Statistics\n{self.get_statistics(state, tab)}'
                dialogue = f'{dialogue}\n{form_element_content}\n{slots_content}\n{messages_content}\n{statistics_content}'
                report_log = f'{report_log}\n{dialogue}'
            report_log = f'\n{report_log}\n'
            return report_log
        except:
            print('Fail to get the report log')
            raise Exception

    def get_form_element(self, form_element, tab):
        try:
            self.increase_counter()
            fe = form_element
            url_tot = fe.parent.current_url
            # we troncate the url just before the question mark
            if '?' in url_tot:
                url = url_tot[:url_tot.index('?')]
            else:
                url = url_tot
#            url_resp =url_tot[1 + url_tot.index('?'):]
            line = f'[browser_name: {fe.parent.name} - page_title: {fe.parent.title} - URL: {url}]'
            form_element_content = self.add_line(line, tab=tab)
            form_element_content = f'\n{form_element_content}\n'
            return form_element_content
        except:
            print('Fail to get the form element')
            raise Exception

    def get_slots(self, slots, tab):
        try:
            self.increase_counter()
            slots_content = ''
            for slot in slots:
                if slot[u.slot_name] != u.REQUESTED_SLOT:
                    if slot[u.value_type] in u.choices_type_list:
                        line_slot = f'[{u.slot_name}: {slot[u.slot_name]} - {u.slot_value}: {slot[u.slot_value]} - {u.required}: {slot[u.required]} - {u.spelling}: {slot[u.spelling]} - {u.description}: {slot[u.description]} - {u.choice_list}: {slot[u.choice_list]}]'
                    else:
                        line_slot = f'[{u.slot_name}: {slot[u.slot_name]} - {u.slot_value}: {slot[u.slot_value]} - {u.required}: {slot[u.required]} - {u.spelling}: {slot[u.spelling]} - {u.description}: {slot[u.description]}]'
                else:
                    line_slot = f'[Web Form info -- {u.title}: {slot[u.title]} - {u.description}: {slot[u.description]}]'
                slots_content = self.add_line(line_slot, slots_content, tab)
            slots_content = f'\n{slots_content}\n'
            return slots_content
        except:
            print('Fail to get the slots')
            raise Exception 

    def get_messages(self, messages, tab):
        try:
            self.increase_counter()
            tabb = f'{tab}\t'
            messages_content = ''
            for index in range(len(messages)):
                message = messages[index]
                self.manage_spelling(message)
                line_message = f'Message_{index}'
                line_message = self.add_line(line_message, tab=tab)
                line_text = self.add_line(f'Text: {message["text"]}', tab=tabb)
                line_intent = self.add_line(f'Intent: [name: {message["intent"]["name"]} - confidence: {round(Decimal(message["intent"]["confidence"]), 4)}]', tab=tabb)
                line_entities = self.add_line(f'Entities: {self.get_entities(message["entities"])}', tab=tabb)
                message_content = f'{line_message}\n{line_text}\n{line_intent}\n{line_entities}'
                messages_content = f'{messages_content}\n{message_content}'
            messages_content = f'\n{messages_content}\n'
            return messages_content
        except:
            print('Fail to get the messages')
            raise Exception

    def get_entities(self, entities):
        try:
            text = '[entity: {}, value: {}]'
            line = ''
            for entity in entities:
                if line == '':
                    line = text.format(entity["entity"], entity["value"])
                else:
                    line = f'{line}, {text.format(entity["entity"], entity["value"])}'
            return line
        except:
            print('Fail to get the entities')
            raise Exception

    def get_statistics(self, state, tab):
        try:
            convergence_rate_content = self.get_convergence_rate(state, tab)
            clarity_factor_content = self.get_clarity_factor(state, tab)
            statistics_content = f'{convergence_rate_content}\n{clarity_factor_content}'
            self.spelling_length = 0
            return statistics_content
        except:
            print('Fail to get the statistics')
            raise Exception

    def manage_spelling(self, message):
        try:
            intent = message["intent"]["name"]
            if intent == u.spelling:
                self.spelling_length += 1
        except:
            print('Fail to update the spelling length')
            raise Exception

    def get_spelling_slots(self, slots):
        try:
            spelling_slots = []
            for slot in slots:
                if slot[u.slot_name] != u.REQUESTED_SLOT and slot[u.spelling]:
                    spelling_slots.append(slot)
            return spelling_slots
        except:
            print('Fail to get the spelling slots')
            raise Exception

    def get_cummulative_values(self, slots):
        try:
            sum_length = 0
            for slot in slots:
                sum_length += 1 + len(slot[u.slot_value])
            return sum_length
        except:
            print('Fail to compute cummulative values')
            raise Exception

    def get_convergence_rate(self, state,tab):
        try:
            self.increase_counter()
            tabb = f'{tab}\t'
            total_turns = len(state.message_history) * 2 + 1
            slots = state.constructs["form"]["slots"]
            total_fields = len(slots) - 1
            spelling_slots = self.get_spelling_slots(slots)
            total_spelling = len(spelling_slots)
            cummulative_spelling_values = self.get_cummulative_values(spelling_slots)
            m_k_factor = max(self.spelling_length, cummulative_spelling_values)
            line_text = 'Convergence Rate:'
            convergence_rate_content = self.add_line(line_text, tab=tab)
            line_text = f'total number of turns: t = {total_turns}'
            convergence_rate_content = f'{convergence_rate_content}\n{self.add_line(line_text, tab=tabb)}'
            line_text = f'total number of fields: n = {total_fields}'
            convergence_rate_content = f'{convergence_rate_content}\n{self.add_line(line_text, tab=tabb)}'
            line_text = f'total number of spelling fields: m = {total_spelling}'
            convergence_rate_content = f'{convergence_rate_content}\n{self.add_line(line_text, tab=tabb)}'
            line_text = f'total number of spelling turns: m_k factor = {m_k_factor}'
            convergence_rate_content = f'{convergence_rate_content}\n{self.add_line(line_text, tab=tabb)}'
            line_text = f'convergence rate: c = {round(Decimal(2*(total_fields - total_spelling + m_k_factor))/Decimal(total_turns), 2)}'
            convergence_rate_content = f'{convergence_rate_content}\n{self.add_line(line_text, tab=tabb)}'
            return convergence_rate_content
        except:
            print('Fail to get the convergence rate content')
            raise Exception
    
    def get_clarity_factor(self, state, tab):
        try:
            self.increase_counter()
            tabb = f'{tab}\t'
            clarity_denom = len(state.message_history)
            slots = state.constructs["form"]["slots"]
            total_slots = len(slots) # we do not remove one because we count the submit request          
            spelling_slots = self.get_spelling_slots(slots)
            total_spelling = len(spelling_slots)
            cummulative_spelling_values = self.get_cummulative_values(spelling_slots)
            m_k_factor = max(self.spelling_length, cummulative_spelling_values)
            clarity_num = (total_slots) - total_spelling + m_k_factor
            line_text = 'Response Clarity Factor:'
            clarity_factor_content = self.add_line(line_text, tab=tab)
            line_text = f"Number of required turns: {clarity_num} turns"
            clarity_factor_content = f'{clarity_factor_content}\n{self.add_line(line_text, tab=tabb)}'
            line_text = f"Number of user's turns: {clarity_denom} turns"
            clarity_factor_content = f'{clarity_factor_content}\n{self.add_line(line_text, tab=tabb)}'
            line_text = f"Clarity factor: {round(Decimal(clarity_num)/Decimal(clarity_denom), 4)}"
            clarity_factor_content = f'{clarity_factor_content}\n{self.add_line(line_text, tab=tabb)}'
            return clarity_factor_content
        except:
            print('Fail to get the clarity factor content')
            raise Exception