DEBUG = True

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

REQUESTED_SLOT = "requested_slot"
CANCELED = "canceled"
READY_FOR_SPELLING = True  # True when we are ready to manage the spelling correctly
# when READY_FOR_SPELLING is False, fillSpellingCamp calls fillGenericCamp
tag_registration_form = "registration_form_tag"

# decides whether we have to train the model or not
train_model = False

# decides whether or not write the log and the report
write_log = True
write_report = True

# URL of the form to fill
form_url = "http://localhost/ecobusiness/new-project-form/"

# browser to user to open the url, Chrome - Firefox - Edge
browsers = ['chrome', 'firefox', 'edge']

# interactive enabled to choose the browser
interactive_enabled = False

# training information

## folders' name
training_folder = 'training_files'
models_folder = 'models'
registration_form_folder = 'registration_form'
login_form_folder = 'login_form'

## files name
domain_file = 'domain_file.yml'
nlu_data_file = 'nlu_data.json'
nlu_config_file = 'nlu_config.yml'


# restricted actions, not self defining actions, need state to decide what to do
restricted_actions = ['affirm', 'deny']

# spelling
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
            'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
special_characters = ['space', 'exclamation', 'double quote', 'hash', 'dollar', 'percent', 'ampersand',
                      'left parenthesis', 'right parenthesis', 'asterisk', 'plus', 'comma', 'minus', 'dot',
                      'full stop', 'slash', 'Colon', 'semicolon', 'less than', 'equal', 'greater than',
                      'question mark', 'at', 'left bracket', 'backslash', 'right bracket', 'caret',
                      'underscore', 'backlick', 'left brace', 'vertical bar', 'right brace', 'tilde']
spec_char_symbol = [' ', '!', '"', '#', '$', '%', '&', '(', ')', '*', '+', '-', '.', '.', '/', ':', ';', '<',
                    '=', '>', '?', '@', '[', '\\', ']', '^', '_', '`', '{', '|', '}', '~']
terminator = ['terminate', 'terminator', 'conclude',
              'end', 'stop', 'close', 'finish', 'finished', 'halt']
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
month = 'month'
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
dropdowm = 'dropdown'
radio = 'radio'
checkbox = 'checkbox'
text_area = 'text_area'

# input type list 
input_type_list = [text_area, color, date, datetime_local, email, file_type, hidden, image,
    month, number, password, range_type, reset, search, submit, tel, text, time, url, week]


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
o_clock = "o'clock"
am = 'am'
pm = 'pm'


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

# annotations of the web_page
bot_title = 'bot-title'
bot_field = 'bot-field'
bot_button = 'bot-button'
bot_desc = 'bot-desc'
field_type = 'field-type'
field_spelling = 'field-spelling'
field_desc = 'field-desc'