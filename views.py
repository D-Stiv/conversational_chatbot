# This file manages all the views, has the role to get the necessary simulation parameters and output them in an appropriate format in order to keep track of the evolving of the simulation

from view import View
import utility as u
from datetime import datetime
from decimal import Decimal

cumulative_thinking_time = 0
cumulative_response_time = 0
current_time = 0
number_requests = 0
sec = 'seconds'
req = 'requests'
starting_time = datetime.now()
class ViewChatPannel(View):

    def __init__(
        self,
        writer,
        marker = ""
    ):
        super().__init__(writer, marker)
        

    # shows the end of the simulation
    def show_end_of_conversation(self, counter):
        average = self.average_response_time()
        total_response = self.get_time_in_seconds(cumulative_response_time)
        total_thinking = self.get_time_in_seconds(cumulative_thinking_time)
        stats = (f'Starting time: {starting_time}\nEnding time: {datetime.now()}' +
            f'\nCumulative response time: {total_response} {sec}\nNumber of user requests: {number_requests} {req}\nAverage response time: {average} sec/req' +
            f'\nCumulative thinking time: {total_thinking} {sec}')
        text = f"{counter}. END OF THE CONVERSATION !!!\n\n{stats}"

        self.writer.add_line(text)
        print(text)

    # shows the complition of the requested maximum number of iterations when it occurs
    def show_notifications(self, text):
        text = f'[Situation of fields]\n{text}'
        self.writer.add_line(text)
        print(text)

    def show_new_dialogue(self, counter):
        try:
            text = f'\n--- DIALOGUE {counter} ---\n'
            log = self.writer.write_dialogue()
            text = f'{text}\n{log}'
            if self.writer.session_string == '':
                self.writer.session_string = text
            else:
                self.writer.session_string = f'{self.writer.session_string}\n\n{text}'
            # we reset the parameters of the writer for the next dialogue
            self.writer.summary_string = ''
            self.writer.conversation_string = ''
            self.writer.number_turns_chatbot = 0
            self.writer.number_turns_user = 0
        except:
            print('Fail to insert the new dialogue in the session string')
            raise Exception

    def update_response_time(self):
        try:
            global cumulative_response_time
            global number_requests

            now = datetime.now()
            delta = now - current_time
            cumulative_response_time += delta
            number_requests += 1
        except:
            print('Fail to update the cumulative response time')
            raise Exception

    def update_thinking_time(self):
        try:
            global cumulative_thinking_time

            now = datetime.now()
            delta = now - current_time
            cumulative_thinking_time += delta
        except:
            print('Fail to update the cumulative response time')
            raise Exception    

    def average_response_time(self):
        try:
            cumulative_value = self.get_time_in_seconds(cumulative_response_time)
            result = round(Decimal(cumulative_value)/Decimal(number_requests), 2)
            return result
        except:
            print('Fail to compute the average response time')

    def update_current_time(self):
        global current_time
        current_time = datetime.now()

    def initialize_cumulative_times(self):
        global cumulative_response_time
        global cumulative_thinking_time
        global number_requests

        now = datetime.now()
        cumulative_response_time = now - now
        cumulative_thinking_time = cumulative_response_time
        number_requests = 0

    def get_time_in_seconds(self, date_time):
        try:
            # first extract the day, hour, minute, second and then we sum
            days = 0
            hours = 0
            minutes = 0
            seconds = 0
            try:
                days = date_time.days
            except:
                days = 0
            try:
                hours = date_time.hours
            except:
                hours = 0
            try:
                minutes = date_time.minutes
            except:
                minutes = 0
            seconds = date_time.seconds
            time = days*(24*3600) + hours*3600 + minutes*60 + seconds
            return time
        except:
            print(f'Fail to get the time {date_time} in {sec}')
        
    def set_starting_time(self, time):
        global starting_time

        starting_time = time