# interface that defines the APIs necessary for the views

import utility as u
from datetime import datetime

class View:

    def __init__(
        self,
        writer,
        marker=""
    ) -> None:
        """Initializing of the View"""
        self.marker = marker
        self.writer = writer

    # displays a text in an appropriate way
    def show_text(self, counter, text):
        try:
            text = f"{counter}. {self.marker} - {text}"
            if counter == 0:
                # it is the chatbot
                # we initialize the cumulative response time 
                self.initialize_cumulative_times()
                self.set_starting_time(datetime.now())               
            if self.marker == u.chatbot_marker:
                # we compute the interval between the request and the response
                if counter != 0:
                    self.update_response_time()
                # we put the time at which the user sends the request to compute the thinking time
                self.update_current_time()
                self.writer.add_chatbot_line(text)
                print(text)
            elif self.marker == u.user_marker:
                self.update_thinking_time()
                # we put the time at which the user sends the request to compute the response time
                self.update_current_time()
                self.writer.add_user_line(text)
                if u.simulation_enabled:
                    print(text)
        except:
            print(f'Fail to show the text {text}')
            raise Exception
