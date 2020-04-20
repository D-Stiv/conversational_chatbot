# makes all the preprocessing tasks and launches the interaction

import dialogue_manager
import utility as u
import writers as w
import functions as fn


def manage_current_form(bot_tag):
    manager.start(bot_tag)

def initial_parsing(url, browser):
    manager = dialogue_manager.DialogueManager(url=url, browser=browser)
    manager.initialize_views()
    manager.create_form_bots()
    return manager


# At the beginning of the parsing of the whole Web paage
# Access Level
if u.interactive_enabled:
    number = len(u.browsers)
    index = -1
    while index not in range(number):
        index = input(f'which browser do you want to user among the following ?\n{fn.get_proposals(u.browsers)}')
        if index not in range(number):
            print(f'your input is not valid, your should insert a number between 0 and {number-1}')
    browser = u.browsers[index]    
else:
    browser = u.browsers[0]

url = u.form_url

# The Access level calls the Interaction level for the initialization of the bots
# for all the Forms present in thee Web page
manager = initial_parsing(url=url, browser=browser)

# In the Access level, we move the focus in a specific Form and the access Level
# extracts the value of the attribute bot-tag of that Form
current_form_tag = u.tag_registration_form

# The Access Level calls the Interaction Level to manage the current Form
manage_current_form(current_form_tag)

final_string = 'End of the session.'
manager.write_log()
if u.write_log:
    final_string = f'{final_string} The log is present in the folder <logs>.'
if u.write_report:
    # we write the report now if we have at least one state
    states_list = manager.states_list
    if len(states_list) > 0:
        report_writer = w.ReportWriter(states_list)
        report_writer.start()
        final_string = f'{final_string} The report is in the folder <reoprts>.'
print(final_string)