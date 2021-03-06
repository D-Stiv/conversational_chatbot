"""At the very end of this file there is a module to train the model for the 
Conversational Chatbot. We only have to run this file for it to be done."""

# statistics for the thesis
compute_response_time = True

# exceptional message
EXCEPTION_MESSAGE = "Something went wrong during the handling of this message.\n what can i precisely do for you please ?"

DEBUG = False

# maximum number of dialogues
MAX_DIALOGUES = 5

# frequency control: interval for being able to manually stop the simulation in term of number of message exchanged
CONTROL_FREQUENCE = 50

# frequence to see the change in the slots in term of interactions
NOTIFICATION_FREQUENCE = 10

# coefficient used to regule the dialogue and the notifications
COEFF = 3

REQUESTED_SLOT = "requested_slot"
CANCELED = "canceled"
VOID = ''
USE_SPELLING = True  # True when we are ready to manage the spelling correctly
# when USE_SPELLING is False, fillSpellingField calls fillGenericField
tag_registration_form = "registration_form_tag"

# decides whether we have to train the model or not
train_model = False

# decides whether or not write the log and the report
write_log = True
write_report = True

# whether or not we use the simulator
simulation_enabled = True

# defines whether or not we get the URL from the user
ask_url = False

# URL of the form to fill
url_new = "http://localhost/ecobusiness/new-project-form/"
url_test = "http://localhost/ecobusiness/test-project-form/"

form_url = url_new

# URLs for the test Web Forms
url_1 = 'http://localhost/ecobusiness/test-form-1/'
url_2 = 'http://localhost/ecobusiness/test-form-2/'
url_3 = 'http://localhost/ecobusiness/test-form-3/'

test_url_list = [url_1, url_2, url_3]

urls = test_url_list + [url_new, url_test]

# browser to user to open the url, Chrome - Firefox - Edge
browsers = ['edge', 'firefox', 'chrome']

# interactive enabled to choose the browser
interactive_enabled = False

# training information

# folders' name
training_folder = 'training_files'
models_folder = 'models'
registration_form_folder = 'registration_form'
login_form_folder = 'login_form'

# files name
nlu_data_file = 'nlu_data.json'
nlu_config_file = 'nlu_config.yml'


# string to stop the session
stop = 'leave'

# minimum and maximum year acceptable for the date
min_year = 1500
max_year = 3000

# minimum and maximum month acceptable
min_month = 0
max_month = 12

# minimum and maximum day acceptable
min_day = 1
max_day = 31

# minimum and maximum hour acceptable
min_hour = 0
max_hour = 24

# minimum and maximum minute acceptable
min_minute = 0
max_minute = 60

# spelling
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
            'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
special_characters = ['space', 'exclamation', 'double quote', 'hash', 'dollar', 'percent', 'ampersand',
                      'left parenthesis', 'right parenthesis', 'asterisk', 'plus', 'comma', 'minus', 'dot',
                      'full stop', 'slash', 'colon', 'semicolon', 'less than', 'equal', 'greater than',
                      'question mark', 'at', 'left bracket', 'backslash', 'right bracket', 'caret',
                      'underscore', 'backlick', 'left brace', 'vertical bar', 'right brace', 'tilde']
spec_char_symbol = [' ', '!', '"', '#', '$', '%', '&', 
                    '(', ')', '*', '+', ',', '-', '.', 
                    '.', '/', ':', ';', '<', '=', '>', 
                    '?', '@', '[', '\\', ']', '^', 
                    '_', '`', '{', '|', '}', '~']
terminator = ['terminate', 'terminator', 'conclude',
              'end', 'close', 'finish', 'finished', 'halt']
number_0_9 = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
password_spec_chars = ['!', '@', '#', '$', '%', '^', '&', '*', '_']

# styles
again_styles = ['again', 'once more', 'another time', '']
next_styles = ['next', 'following']
insert_styles = ['insert', 'put', 'fill', 'give', 'complete']
good_styles = ['good', 'fine', 'well', 'okay', 'correct']
modify_styles = ['modify', 'change', 'update', 'adjust', 'amend', 'revise']

# value types
button = 'button'
color = 'color'
date = 'date'
datetime_local = 'datetime-local'
email = 'email'
file_type = 'file'
hidden = 'hidden'
image = 'image'
month_type = 'month'
number = 'number'
password = 'password'
range_type = 'range'
reset = 'reset'
search = 'search'
submit = 'submit'
tel = 'tel'
text = 'text'
time = 'time'
url = 'url'
week = 'week'
dropdown = 'dropdown'
radio = 'radio'
checkbox = 'checkbox'
text_area = 'text_area'
integer = 'integer'
decimal = 'decimal'

# input type list
input_type_list = [text_area, color, date, datetime_local, email, file_type, hidden, image,
                   month_type, number, integer, decimal, password, range_type, reset, search, submit, tel, text, time, url, week]

choices_type_list = [radio, checkbox, dropdown]
number_types_list = [number, integer, decimal]

# list of non supported types
non_supported_types = [month_type]

# length phone number
min_length_phone_number = 3     # this is without plus (117, 112, ...)

# length of password
min_length_password = 5

# week days
monday = 'monday'
tuesday = 'tuesday'
wednesday = 'wednesday'
thursday = 'thursday'
friday = 'friday'
saturday = 'saturday'
sunday = 'sunday'

# months of the year
january = 'january'
february = 'february'
march = 'march'
april = 'april'
may = 'may'
june = 'june'
july = 'july'
august = 'august'
september = 'september'
october = 'october'
november = 'november'
december = 'december'

# time indications
o_clock = "o_clock"
am = 'am'
pm = 'pm'

months = [january, february, march, april, may, june, july, august,
          september, october, november, december]
time_refs = [o_clock, am, pm]

# logs and reports folder's name
logs_folder = 'logs'
reports_folder = 'reports'

# user and Chatbot markers
user_marker = 'User'
chatbot_marker = 'Chatbot'

# signs for the function convert to int
normal = 'N'
month = 'M'
year = 'Y'
day = 'D'
hour = 'H'
minute = 'Min'


# keys of the slot data structure
slot_name = 'slot_name'     # given by the bot-field attribute
slot_value = 'slot_value'   # to be inserted by the user
value_name = 'value_name'   # given by the name attribute
value_type = 'value_type'   # given by the bot-type or type attribute
spelling = 'spelling'       # given by field-spelling attribute
required = 'required'       # given by required attribute
choice_list = 'choice_list'  # list of choices in case of dropdown, radio or checkbox
# description/explanation of the field. given by field-desc attribute
description = 'description'
title = 'title'             # form the form. the description also used for the form
min_value = 'min'
max_value = 'max'
precision = 'precision'

# annotations of the web_page
bot_title = 'bot-title'
bot_field = 'bot-field'
bot_button = 'bot-button'
bot_desc = 'bot-desc'
bot_tag = 'bot-tag'
field_type = 'field-type'
field_spelling = 'field-spelling'
field_desc = 'field-desc'

# keys for the spelling state structure
close_prompt_enabled = 'close_prompt_enabled'
current_spelling_input_value = 'current_spelling_input_value'
spelling_interrupted = 'spelling_interrupted'
spelling_list = 'spelling_list'
waiting_message = 'waiting_message'
after_spelling = 'after_spelling'
saved_spelling_fields = 'saved_spelling_fields'
# goes with the spelling field at the same index
saved_spelling_values = 'saved_spelling_values'

# keys for parameters of the machine (will be use for the state machine)
possible_next_action = 'possible_next_action'
all_required_filled = 'all_required_filled'
warning_message = 'warning_message'
warning_present = 'warning_present'
next_slot = 'next_slot'
next_slot_required = 'next_slot_required'
submit_alarm_enabled = 'submit_alarm_enabled'
reset_alarm_enabled = 'reset_alarm_enabled'
submit_done = 'submit_done'
filling_started = 'filling_started'
# we add a key for state of the state machine
state_name = 'state_name'

# names of actions useful
affirm_action = 'affirm'
deny_action = 'deny'
fill_form_action = 'fillForm'
fill_field_action = 'fillGenericField'
reset_all_fields_action = 'resetAllFields'
spelling_action = 'spelling'
submit_action = 'submitForm'

# keys for the constructs data structure of the state of the dialogue
text_construct = 'text'
list_construct = 'list'
form_construct = 'form'
slots = 'slots'
number_not_handled = 'number_not_handled'


# restricted actions, not self defining actions, need state to decide what to do
restricted_actions = [affirm_action, deny_action]

# funzionalities
fun_explain_field = 'ask the explanation of a field'
fun_remaining_fields = 'ask the list of remaining fields'
fun_remaining_required_fields = 'ask the list of the remaining required fields'
fun_remaining_optional_fields = 'ask the list of remaining optional fields'
fun_all_fields = 'request the list of fields present in this Web Form'
fun_required_fields = 'request the required fields of this Web Form'
fun_optional_fields = 'request the list of the optional fields ontained in the Web Form'
fun_modify_field = 'modify the value inserted for a field'
fun_recap = 'ask the recap for the fields inserted'
fun_skip = 'skip this field'
fun_reset = 'restart the process from the beginning'
fun_submit = 'submit the Web Form if all the required fields are completed'
fun_verify_value = 'verify the value of a field'
fun_complete_field = 'decide to complete a different field'
fun_form_description = 'ask the Web Form description'
fun_form_title = 'request the title of this Web Form'
fun_verify_presence_field = 'verify if there is a given field in this Web Form'
fun_resume = 'ask to resume the filling procedure and restart from where you stopped'

functionalities_list = [fun_explain_field, fun_remaining_fields, fun_remaining_required_fields, fun_remaining_optional_fields, 
    fun_all_fields, fun_required_fields, fun_optional_fields, fun_modify_field, fun_recap, fun_skip, fun_submit, fun_reset, 
    fun_verify_value, fun_complete_field, fun_form_description, fun_form_title
]