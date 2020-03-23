# This file manages all the views, has the role to get the necessary simulation parameters and output them in an appropriate format in order to keep track of the evolving of the simulation

from view import View
import utility as u


class ViewChatPannel(View):

    def __init__(
        self,
        writer,
        marker = ""
    ):
        super().__init__(writer, marker)

    # shows the end of the simulation
    def show_end_of_conversation(self, counter):
        text = f"{counter}. END OF THE CONVERSATION !!!"
        self.writer.add_line(text)
        print(text)

    # shows the complition of the requested maximum number of iterations when it occurs
    def show_completed_iterations(self, counter):
        text = f"{counter}. We Stop here because the maximum number of iterations is reached"
        self.writer.add_line(text)
        print(text)
