# makes all the preprocessing tasks and launches the interaction

import dialogue_manager
import utility as u
import writers as w
import functions as fn
import simulation_constants as cts


def manage_current_form(bot_tag, s=None):
    manager.start(bot_tag, s=s)

def initial_parsing(url, browser, s=None):
    manager = dialogue_manager.DialogueManager(url=url, browser=browser)
    if s is not None:
        manager.initialize_views(s)
    else:
        manager.initialize_views(cts.counter_trigger)
    manager.create_form_bots()
    return manager

s_values = [32, 32]
for s in s_values:
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

    # Interaction Level with direct access by the user
    if u.ask_url:
        url = input('Please insert the URL of the Web Form that you would like to fill.\nURL: ')
    else:
        url = u.form_url

    # The Access level calls the Interaction level for the initialization of the bots
    # for all the Forms present in thee Web page
    manager = initial_parsing(url=url, browser=browser, s=s)

    # In the Access level, we move the focus in a specific Form and the access Level
    # extracts the value of the attribute bot-tag of that Web Form
    current_form_tag = u.tag_registration_form

    # The Access Level calls the Interaction Level to manage the current Form
    manage_current_form(current_form_tag, s=s)

    try:
        final_string = 'End of the session.'
        if u.write_log:
            manager.write_log()
            final_string = f'{final_string} The log is present in the folder <logs>.'
        if u.write_report:
            # we write the report now if we have at least one state
            states_list = manager.states_list
            if len(states_list) > 0:
               # report_writer = w.ReportWriter(states_list, cts.counter_trigger)
                report_writer = w.ReportWriter(states_list, s)
                report_writer.start()
                final_string = f'{final_string} The report is in the folder <reoprts>.'
        print(final_string)
    except:
        raise Exception