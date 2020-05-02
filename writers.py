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
        counter_trigger=None,
        destination_folder = u.logs_folder,
        file_type = 'log'
    ):
        super().__init__(counter_trigger, destination_folder, file_type)
        self.summary_string = ''
        self.conversation_string = ''
        self.number_turns_chatbot = 0
        self.number_turns_user = 0
        self.session_string = ''

    def start(self, display_summary=None):
        try:
            if self.session_string == '':
                text = self.write_dialogue(display_summary)
            else:
                text = self.session_string
            self.create_file(text)
            print('The log has been created successfully')
        except:
            print('Problem while creating the session log')
            raise Exception

    def write_dialogue(self, display_summary=None):
        try:
            header = self.construct_header()
            if display_summary is not None:
                summary = display_summary
            else:
                summary = self.construct_summary()
            conv_log = self.construct_conv_log()
            text = f'{header}\n\n{summary}\n\n{conv_log}\n\n'
            return text
        except:
            print('Fail to write the dialogue')
            raise Exception

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
        counter_trigger = None,
        destination_folder = u.reports_folder,
        file_type = 'report'
    ):
        super().__init__(counter_trigger, destination_folder, file_type)
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
                if number == 1:
                    summary = f'SUMMARY\n\n\tThere is {number} completed dialogue'
                else:
                    summary = f'SUMMARY\n\n\tThere are {number} completed dialogues'
            report_log = self.construct_report_log()
            text = f'{header}\n\n{summary}\n\n{report_log}\n\n'
            self.create_file(text)
            print('The report has been created successfully')
            self.close_windows()
        except:
            print('Fail to construct the report')
            raise Exception

    def close_windows(self):
        for state in self.states_list:
            try:
                driver = state.form_element.parent
                driver.close()
            except:
                pass

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
            try:
                url_tot = fe.parent.current_url
                # we troncate the url just before the question mark
                if '?' in url_tot:
                    url = url_tot[:url_tot.index('?')]
                else:
                    url = url_tot
    #            url_resp =url_tot[1 + url_tot.index('?'):]
                line = f'[browser_name: {fe.parent.name} - page_title: {fe.parent.title} - URL: {url}]'
            except:
                line = 'The window have been closed, so we cannot give you the form elements, sorry'
            if u.DEBUG:
                print(line)
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
            flexibility_coefficient_content = self.get_flexibility_coefficient(state, tab)
            statistics_content = f'{convergence_rate_content}\n{flexibility_coefficient_content}'
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

    def get_cummulative_values(self, slots, required=False):
        try:
            sum_length = 0
            for slot in slots:
                if slot[u.slot_value] is not None and required:
                    if slot[u.required]:
                        sum_length += 1 + len(slot[u.slot_value])
                elif slot[u.slot_value] is not None:
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
            user_turns = total_fields - total_spelling + m_k_factor

            total_required_fields = len(self.get_required_slots(slots))
            total_required_spelling = len(self.get_required_slots(spelling_slots, spelling=True))
            cummulative_required_spelling_values = self.get_cummulative_values(spelling_slots, required=True)
            m_k_required_factor = cummulative_required_spelling_values
            required_user_turns = total_required_fields - total_required_spelling + m_k_required_factor

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
            line_text = f'convergence rate: c = {round(Decimal(2*user_turns + 1)/Decimal(total_turns), 2)}'
            convergence_rate_content = f'{convergence_rate_content}\n{self.add_line(line_text, tab=tabb)}'
            k = 2   # minimum number of user turns in spelling
            conv_adj_num = 2*(user_turns - m_k_factor + total_spelling*k) + 1
            conv_adj_denom = total_turns - 2*(m_k_factor - total_spelling*k)
            line_text = f'adjustded convergence rate: c_adj = {round(Decimal(conv_adj_num)/Decimal(conv_adj_denom), 2)}'
            convergence_rate_content = f'{convergence_rate_content}\n{self.add_line(line_text, tab=tabb)}'
            
            line_text = 'Normalized Convergence Rate:'
            convergence_rate_content = f'{convergence_rate_content}\n{self.add_line(line_text, tab=tab)}'
            line_text = f'total number of required fields: n_2 = {total_required_fields}'
            convergence_rate_content = f'{convergence_rate_content}\n{self.add_line(line_text, tab=tabb)}'
            line_text = f'total number of spelling fields: m_2 = {total_required_spelling}'
            convergence_rate_content = f'{convergence_rate_content}\n{self.add_line(line_text, tab=tabb)}'
            line_text = f'total number of required spelling turns: m_k_2 factor = {m_k_required_factor}'
            convergence_rate_content = f'{convergence_rate_content}\n{self.add_line(line_text, tab=tabb)}'
            line_text = f'normalized convergence rate: c_2 = {round(Decimal(2*required_user_turns + 1)/Decimal(total_turns), 2)}'
            
            convergence_rate_content = f'{convergence_rate_content}\n{self.add_line(line_text, tab=tabb)}'
            return convergence_rate_content
        except:
            print('Fail to get the convergence rate content')
            raise Exception
    
    def get_flexibility_coefficient(self, state, tab):
        try:
            self.increase_counter()
            tabb = f'{tab}\t'
            number_not_handled = state.constructs[u.form_construct][u.number_not_handled]
            slots = state.constructs["form"]["slots"]
            total_slots = len(slots) # we do not remove one because we count the submit request          
            spelling_slots = self.get_spelling_slots(slots)
            total_spelling = len(spelling_slots)
            cummulative_spelling_values = self.get_cummulative_values(spelling_slots)
            m_k_factor = max(self.spelling_length, cummulative_spelling_values)
            flexibility_num = total_slots - total_spelling + m_k_factor - number_not_handled
            flexibility_denom = len(state.message_history)
            k = 2   # minimum number of user turns in case of spelling
            flexibility_num_adj = len(state.message_history) - m_k_factor + total_spelling*(k - 1) - number_not_handled
            flexibility_denom_adj = len(state.message_history) - m_k_factor + total_spelling*(k - 1)
            line_text = 'Natural Language Flexibility Coefficient:'
            flexibility_coefficient_content = self.add_line(line_text, tab=tab)
            line_text = f"number of required turns: v = {flexibility_num} turns"
            flexibility_coefficient_content = f'{flexibility_coefficient_content}\n{self.add_line(line_text, tab=tabb)}'
            line_text = f"number of user's turns: w = {flexibility_denom} turns"
            flexibility_coefficient_content = f'{flexibility_coefficient_content}\n{self.add_line(line_text, tab=tabb)}'
            line_text = f"natural language flexibility coefficient: f = {round(Decimal(flexibility_num)/Decimal(flexibility_denom), 4)}"
            flexibility_coefficient_content = f'{flexibility_coefficient_content}\n{self.add_line(line_text, tab=tabb)}'
            line_text = f"adjusted flexibility coefficient: f_adj = {round(Decimal(flexibility_num_adj)/Decimal(flexibility_denom_adj), 4)}"
            flexibility_coefficient_content = f'{flexibility_coefficient_content}\n{self.add_line(line_text, tab=tabb)}'
            return flexibility_coefficient_content
        except:
            print('Fail to get the flexibility factor content')
            raise Exception

    def get_required_slots(self, slots, spelling=False):
        try:
            required_slots = []
            for slot in slots:
                if slot[u.slot_name] == u.REQUESTED_SLOT:
                    pass
                elif slot[u.required] and spelling:
                    if slot[u.spelling]:
                        required_slots.append(slot)
                elif slot[u.required]:
                    required_slots.append(slot)
            return required_slots
        except:
            print('Fail to get the required slots')
            raise Exception