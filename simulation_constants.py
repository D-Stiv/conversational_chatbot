# the constants concerning the simulation

# data folder
data_folder = 'simulation_data'
filling_folder = 'filling'  # containing the data for completing slot_value
interaction_folder = 'interaction'  # containing the templates to form the sentences

# data keys in the user
filling = 'filling'
interaction = 'interaction'

# simulation filling json files
messages_file = 'messages.json'
countries_file = 'countries.json'
cities_file = 'cities.json'
names_file = 'names.json'
address_names_file = 'address_names.json'
months_file = 'months.json'
possible_fields_file = 'possible_fields.json'

# keys for the filling files
messages = 'messages'
countries = 'countries'
cities = 'cities'
names = 'names'
address_namse = 'address_names'
months = 'months'
possible_fields = 'possible_fields'

# list of filling names and corresponding list of keys
filling_files_names = [messages_file, countries_file, cities_file, names_file, 
    address_names_file, months_file, possible_fields_file]
filling_keys = [messages, countries, cities, names, 
    address_namse, months, possible_fields]

# simulation interaction json files
complete_field_file = 'complete_field.json'
explain_field_file = 'explain_field.json'
fill_form_file = 'fill_form.json'
give_all_remaining_fields_file = 'give_all_remaining_fields.json'
give_remaining_optional_fields_file = 'give_remaining_optional_fields.json'
give_remaining_required_fields_file = 'give_remaining_required_fields.json'
modify_value_field_file = 'modify_value_field.json'
repeat_all_fields_file = 'repeat_all_fields.json'
repeat_optional_fields_file = 'repeat_optional_fields.json'
repeat_required_fields_file = 'repeat_required_fields.json'
repeat_form_explanation_file = 'repeat_form_explanation.json'
repeat_value_field_file = 'repeat_value_field.json'
reset_all_fields_file = 'reset_all_fields.json'
skip_field_file = 'skip_field.json'
verify_presence_field_file = 'verify_presence_field.json'
verify_value_for_completed_fields_file = 'verify_value_for_completed_fields.json'

# keys for the interaction files
complete_field = 'complete_field'
explain_field = 'explain_field'
fill_form = 'fill_form'
give_all_remaining_fields = 'give_all_remaining_fields'
give_remaining_optional_fields = 'give_remaining_optional_fields'
give_remaining_required_fields = 'give_remaining_required_fields'
modify_value_field = 'modify_value_field'
repeat_all_fields = 'repeat_all_fields'
repeat_optional_fields = 'repeat_optional_fields'
repeat_required_fields = 'repeat_required_fields'
repeat_form_explanation = 'repeat_form_explanation'
repeat_value_field = 'repeat_value_field'
reset_all_fields = 'reset_all_fields'
skip_field = 'skip_field'
verify_presence_field = 'verify_presence_field'
verify_value_for_completed_fields = 'verify_value_for_completed_fields'

# list of training json files with corresponding keys
interaction_files_names = [complete_field_file, explain_field_file, fill_form_file, give_all_remaining_fields_file,
    give_remaining_optional_fields_file, give_remaining_required_fields_file, modify_value_field_file, repeat_all_fields_file,
    repeat_optional_fields_file, repeat_required_fields_file, repeat_form_explanation_file, repeat_value_field_file,
    reset_all_fields_file, skip_field_file, verify_presence_field_file, verify_value_for_completed_fields_file]
interaction_keys = [complete_field, explain_field, fill_form, give_all_remaining_fields, 
    give_remaining_optional_fields, give_remaining_required_fields, modify_value_field, repeat_all_fields, 
    repeat_optional_fields, repeat_required_fields, repeat_form_explanation, repeat_value_field,
    reset_all_fields, skip_field, verify_presence_field, verify_value_for_completed_fields]

# phone number prefixes
phone_prefixes = [1, 7, 20, 27, 30, 31, 32, 33, 34, 36, 39, 40, 41, 43, 44, 45, 46, 47, 48, 49, 51, 52, 53, 
    54, 55, 56, 57, 58, 60, 61, 62, 63, 64, 65, 66, 81, 82, 84, 86, 90, 91, 92, 93, 94, 95, 98, 211, 212, 
    213, 216, 218, 220, 221, 222, 223, 224, 225, 226, 227, 228, 229, 230, 231, 232, 233, 234, 235, 236, 237, 
    238, 239, 240, 241, 243, 244, 245, 246, 247, 248, 249, 250, 251, 252, 254, 255, 256, 257, 258, 260, 261, 
    262, 263, 264, 265, 266, 267, 268, 269, 290, 291, 297, 298, 299, 346, 350, 351, 352, 353, 354, 355, 356, 
    357, 358, 359, 370, 371, 372, 373, 374, 375, 376, 377, 378, 380, 381, 382, 383, 385, 386, 387, 420, 421, 
    423, 500, 501, 503, 504, 505, 506, 507, 508, 509, 587, 590, 591, 592, 594, 595, 598, 599, 670, 672, 673, 
    674, 675, 676, 677, 678, 679, 680, 681, 682, 683, 685, 686, 687, 688, 689, 690, 691, 692, 850, 852, 853, 
    855, 856, 880, 886, 960, 961, 962, 963, 964, 965, 966, 967, 968, 970, 971, 972, 973, 974, 975, 976, 977, 
    992, 993, 994, 995, 996, 998]