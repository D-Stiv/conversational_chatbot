# interface that defines the APIs necessary for the views

import utility as u


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
            if self.marker == u.chatbot_marker:
                self.writer.add_chatbot_line(text)
                print(text)
            elif self.marker == u.user_marker:
                self.writer.add_user_line(text)
                if u.simulation_enabled:
                    print(text)
        except:
            print(f'Fail to show the text {text}')
            raise Exception
