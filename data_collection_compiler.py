# data collection compiler

import data_collection_parameters as d_c_p
import utility as u
import xlsxwriter as xw

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
        while True or counter < u.MAX_DIALOGUES:
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
        while True or counter < u.MAX_DIALOGUES:
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
            counter += 1
        index += 1
    except:
        print('Fail to extract report parameters')
        report_correct = False
    

data = [log_data, report_data]
d_c_p.create_json_file('recap.json', data)

  
try:
    file_path = f'{d_c_p.root_folder}/{d_c_p.excel_file}'
    wb = xw.Workbook(file_path) 
    ws = wb.add_worksheet() 
except:
    print('Fail to open the excel file')

if log_correct and report_correct:
    # we insert the log values
    try:
        for col_index in range(len(d_c_p.columns)):
            col = col_index*d_c_p.number_parameters + col_index
            delta = -1
            for row_index in range(len(log_data[0][d_c_p.e_t_list])):
                old_delta = delta
                delta = int(row_index/d_c_p.number_forms)
                row = d_c_p.first_row_number + row_index + d_c_p.interval_tables*delta  # between 2 successive tables there are 'interval_tables' free cells
                try:
                    r_t_value = log_data[col_index][d_c_p.r_t_list][row_index]
                    e_t_value = log_data[col_index][d_c_p.e_t_list][row_index]
                    c_value = report_data[col_index][d_c_p.c_list][row_index]
                    f_value = report_data[col_index][d_c_p.f_list][row_index]
                except:
                    break
                if old_delta != delta:
                    # we insert the dialogue number
                    value = f'DIALOGUE {delta+1}'
                    ws.write(row-1, col, value)
                    value = f'S = {d_c_p.s_values[col_index]}'
                    ws.write(row-1, col+2, value)
                # we insert the values in the excel file
                ws.write(row, col, r_t_value)
                ws.write(row, col+1, e_t_value)
                ws.write(row, col+2, c_value)
                ws.write(row, col+3, f_value)
    except:
        print(f'Problem to update all the col_index = {col_index}')
        raise Exception
 
wb.close()
print('values inserted successfully')