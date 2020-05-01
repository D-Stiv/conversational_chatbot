# data collection parameters and functions

normal_root_folder = './data_collection/normal'
adjusted_root_folder = './data_collection/adjusted'
excel_file = 'recap.xlsx'
sheet = 'data_collection'
columns = ['AD', 'AI', 'AN', 'AS', 'AX', 'BC']
number_parameters = 4   # r_t, e_t, c, f
number_forms = 5    # url_1, url_2, url_3, url_new, url_test
interval_tables = 3 # from param at dialogue i to param at dialogue i+1
first_row_number = 5    # first row containing value in the first table for a given S
json_file = 'recap.json'

# file name structure: prefix_s_value
s_values = ['0', '2', '4', '8', '16', '32']
log_prefix = 'log'
report_prefix = 'report'
adjusted = 'adjusted'
indicator = 'DIALOGUE'  # helps to cut the dialogues

# parameters keyword
r_t_key = 'rage response time:'  # average response time
cummul_r_t_key = 'tive response time:' # cummulative response time
cummul_z_t_key = 'tive thinking time:'   # cummulative thinking time
c_key = 'c =' # convergence rate
c_adj_key = 'c_adj =' # adjusted convergence rate
f_key = 'f =' # natural language flexibility
f_adj_key = 'f_ad =' # adjusted natural language flexibility
total_turns = ': t ='
m_k_factor = ': m_k factor ='

r_t_list = 'r_t_list'
e_t_list = 'e_t_list'
c_list = 'c_list'
f_list = 'f_list'
s_value = 's_value'

# excel columns

excel_cols = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 
            'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X,' 'Y', 'Z', 'AA', 'AB', 'AC', 'AD', 'AE', 'AF', 
            'AG', 'AH', 'AI', 'AJ', 'AK', 'AL', 'AM', 'AN', 'AO', 'AP', 'AQ', 'AR', 'AS', 'AT', 
            'AU', 'AV', 'AW', 'AX,' 'AY', 'AZ', 'BA', 'BB', 'BC', 'BD', 'BE', 'BF', 'BG', 'Bh', 
            'BI', 'BJ', 'BK', 'BL', 'BM', 'BN', 'BO', 'BP', 'BQ', 'BR', 'BS', 'BT', 'BU', 'BV', 
            'BW', 'BX,' 'BY', 'BZ', 'CA', 'CB', 'CC', 'CD', 'CE', 'CF', 'CG', 'CH', 'CI', 'CJ', 
            'CK', 'CL', 'CM', 'CN', 'CO', 'CP', 'CQ', 'CR', 'CS', 'CT', 'CU', 'CV', 'CW', 'CX', 
            'CY', 'CZ']










import utility as u
import json
from copy import copy, deepcopy


def initialize_structures():
    try:
        log_data = []
        report_data = []

        log_data_struct = {
            s_value: '',
            r_t_list: [],
            e_t_list: []
        }

        report_data_struct = {
            s_value: '',
            c_list: [],
            f_list: []
        }
        for value in s_values:
            log_elem = deepcopy(log_data_struct)
            log_elem[s_value] = value
            log_data.append(log_elem)
            report_elem = deepcopy(report_data_struct)
            report_elem[s_value] = value
            report_data.append(report_elem)

        return log_data, report_data
    except:
        print('Fail to initialize the structure')
        raise Exception


def extract_value(string, key):
    try:
        delta = 8
        begin = string.index(key)
        end = begin + len(key)
        value = string[end:end+delta]
        value = format_value(value)
        
        return value
    except:
        print('Fail to extract the value')
        raise Exception

def format_value(value):
    new_value = ''
    for char in value:
        if char in ['\n','\t']:
            break
        elif char not in u.number_0_9 + [',', '.']:
            char = ''
        new_value = f'{new_value}{char}'
    float_value = float(new_value)
    return float_value

def get_column(base_col, delta=0):
    try:
        if delta == 0:
            return base_col.upper()
        try:
            position = excel_cols.index(base_col.upper())
            col = excel_cols[position + delta]
            return col
        except:
            # value not found
            return None
    except:
        print(f'Fail to get the column with base: {base_col} and delta: {delta}')
        raise Exception

def create_json_file(file_path, data):
    # to create a json file having the file name and the content of the json file to be created
    try:
        with open(file_path, 'w') as fp:
            json.dump(data, fp, sort_keys=True, indent=2)
        print("Json file <<<{}>>> created successfully".format(file_path))
    except:
        print("Fail to create the json file with path <<<{}>>>".format(file_path))
        raise Exception

def get_dict(data, value):
    for elem in data:
        if elem[s_value] == value:
            return elem