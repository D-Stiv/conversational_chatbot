# data collection compiler

import data_collection_parameters as d_c_p
import utility as u

log_data, report_data = d_c_p.initialize_structures()
index = 0
for suffix in d_c_p.s_values:
    try:
        current_dict = d_c_p.get_dict(data=log_data, value=suffix)
        log_correct = True
        # extraction of log elements
        log_path = f'{d_c_p.root_folder}/{d_c_p.log_prefix}_{suffix}.txt'
        f = open(log_path, 'r')
        string = f.read()
        counter = 0
        while counter < u.MAX_DIALOGUES:
            r_t_value = d_c_p.extract_value(string, d_c_p.r_t_key)
            cummul_r_t_value = d_c_p.extract_value(string, d_c_p.cummul_r_t_key)
            cummul_z_t_value = d_c_p.extract_value(string, d_c_p.cummul_z_t_key)
            e_t_value = int(cummul_r_t_value) + int(cummul_z_t_value)
            # add the value to the dict
            current_dict[d_c_p.r_t_list].append(r_t_value)
            current_dict[d_c_p.e_t_list].append(e_t_value)
            # we go to the next dialogue
            epsilon = 5
            string_adjusted = string[string.index(d_c_p.indicator)+epsilon:]
            if d_c_p.indicator not in string_adjusted:
                break
            string = string[string_adjusted.index(d_c_p.indicator):]
            counter += 1
        index += 1
    except:
        print('Fail to extract log parameters')
        log_correct = False

index = 0    
for suffix in d_c_p.s_values:
    try:
        report_correct = True
        # extract report elements
        report_path = f'{d_c_p.root_folder}/{d_c_p.report_prefix}_{suffix}.txt'
        f = open(report_path, 'r')
        string = f.read()
        counter = 0
        while counter < u.MAX_DIALOGUES:
            c_value = d_c_p.extract_value(string, d_c_p.c_key)
            f_value = d_c_p.extract_value(string, d_c_p.f_key)
            # add the value to the dict
            report_data[index][d_c_p.c_list].append(c_value)
            report_data[index][d_c_p.f_list].append(f_value)
            # we go to the next dialogue
            arbitrary = 10
            string_adjusted = string[string.index(d_c_p.indicator)+arbitrary:]
            if d_c_p.indicator not in string_adjusted:
                break            
            string = string[string_adjusted.index(d_c_p.indicator):]
        index += 1
    except:
        print('Fail to extract report parameters')
        report_correct = False
    

data = [log_data, report_data]
d_c_p.create_json_file('recap.json', data)

"""    
try:
    file_path = f'{d_c_p.root_folder}/{d_c_p.excel_file}'
    wb = openpyxl.load_workbook(file_path)
    print(wb)
except:
    print('Fail to open the excel file')

if log_correct:
    # we insert the log values
    try:
        row_index = 0
        for col_index in range(len(d_c_p.columns)):
            r_t_col = d_c_p.columns[col_index]
            e_t_col = d_c_p.get_column(base_col=r_t_col, delta=1)   # 1 because e_t directly follows r_t
            row = d_c_p.first_row_number + row_index*d_c_p.interval_same_parameter
            r_t_value = log_data[col_index][d_c_p.r_t_list][row_index]
            e_t_value = log_data[col_index][d_c_p.e_t_list][row_index]
            # we insert the values in the excel file
            cell = f'{r_t_col}{row}'
            xw.Range(cell).value = r_t_value
            cell = f'{e_t_col}{row}'
            xw.Range(cell).value = e_t_value
            row_index += 1
        print('r_t and e_t values inserted successfully')
    except:
        print(f'Problem to update all the r_t and e_t. col_index = {col_index}')
    

if report_correct:
    # we insert the report values
    try:
        row_index = 0
        for col_index in range(len(d_c_p.columns)):
            c_col = d_c_p.get_column(base_col=d_c_p.columns[col_index], delta=2)
            f_col = d_c_p.get_column(base_col=c_col, delta=1)   # 1 because f directly follows c
            row = d_c_p.first_row_number + row_index*d_c_p.interval_same_parameter
            c_value = log_data[col_index][d_c_p.c_list][row_index]
            f_value = log_data[col_index][d_c_p.f_list][row_index]
            # we insert the values in the excel file
            cell = f'{c_col}{row}'
            xw.Range(cell).value = c_value
            cell = f'{f_col}{row}'
            xw.Range(cell).value = f_value
            row_index += 1
        print('c and f values inserted successfully')
    except:
        print(f'Problem to update all the c and f. col_index = {col_index}')

"""