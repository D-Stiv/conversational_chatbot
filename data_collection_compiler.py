# data collection compiler

import data_collection_parameters as dcp
import utility as u
import xlsxwriter as xw


def start_compilation(root_folder, excel_file, prefix=''):
    # we open excel file
    try:
        file_path = f'{root_folder}/{prefix}{excel_file}'
        wb = xw.Workbook(file_path) 
        ws = wb.add_worksheet() 
    except:
        print('Fail to open the excel file')

    log_data, report_data = dcp.initialize_structures()
    # we set the first row and column
    col = 0
    row = dcp.first_row_number
    index = 0
    for ind in range(len(dcp.s_values)):
        try:
            suffix = dcp.s_values[ind]
            # we start a new column
            col = ind*dcp.number_parameters + ind

            current_dict = dcp.get_dict(data=log_data, value=suffix)
            log_correct = True
            report_correct = True
            # extraction of log elements
            log_path = f'{root_folder}/{prefix}{dcp.log_prefix}_{suffix}.txt'
            f_log = open(log_path, 'r')
            string_log = f_log.read()
            # extract report elements
            report_path = f'{root_folder}/{prefix}{dcp.report_prefix}_{suffix}.txt'
            f_report = open(report_path, 'r')
            string_report = f_report.read()
            counter = 0
            delta = -1  # excel
            while True or counter < u.MAX_DIALOGUES:
                # we are in a new row
                r_t_value = dcp.extract_value(string_log, dcp.r_t_key)
                cumul_r_t_value = dcp.extract_value(string_log, dcp.cumul_r_t_key)
                cumul_z_t_value = dcp.extract_value(string_log, dcp.cumul_z_t_key)
                e_t_value = int(cumul_r_t_value) + int(cumul_z_t_value)
                if prefix == '':
                    c_key = dcp.c_key
                    f_key = dcp.f_key
                else:
                    c_key = dcp.c_adj_key
                    f_key = dcp.f_adj_key
                    f_key = dcp.total_turns
                    f_value = dcp.extract_value(string_report, f_key) - dcp.extract_value(string_report, dcp.m_k_factor)
                c_value = dcp.extract_value(string_report, c_key)
                f_value = dcp.extract_value(string_report, f_key)
                # we add the values in the excel file
                old_delta = delta
                delta = int(counter/dcp.number_forms)
                row = dcp.first_row_number + counter + dcp.interval_tables*delta  # between 2 successive tables there are 'interval_tables' free cells
                if old_delta != delta:
                    # we insert the dialogue number
                    value = f'DIALOGUE {delta+1}'
                    ws.write(row-1, col, value)
                    value = f'S = {suffix}'
                    ws.write(row-1, col+2, value)
                # we insert the values in the excel file
                ws.write(row, col, r_t_value)
                ws.write(row, col+1, e_t_value)
                ws.write(row, col+2, c_value)
                ws.write(row, col+3, f_value)
                
                # add the values to the dict
                current_dict[dcp.r_t_list].append(r_t_value)
                current_dict[dcp.e_t_list].append(e_t_value)
                report_data[index][dcp.c_list].append(c_value)
                report_data[index][dcp.f_list].append(f_value)
                # we go to the next dialogue
                epsilon = 5
                string_adjusted_log = string_log[string_log.index(dcp.indicator)+epsilon:]
                string_adjusted_report = string_report[string_report.index(dcp.indicator)+epsilon:]
                if dcp.indicator not in string_adjusted_log or dcp.indicator not in string_adjusted_report:
                    break
                string_log = string_adjusted_log[string_adjusted_log.index(dcp.indicator):]
                string_report = string_adjusted_report[string_adjusted_report.index(dcp.indicator):]
                counter += 1
            index += 1
        except:
            print('Fail to extract parameters')
            log_correct = False
            report_correct = False
    data = []
    if log_correct:
        data.append(log_data)
    if report_correct:
        data.append(report_data)
    if len(data) > 0:
        file_path = f'{root_folder}/{prefix}{dcp.json_file}'
        print(file_path)
        dcp.create_json_file(file_path, data)

    wb.close()
    print('values inserted successfully')

# we load data for normal parameters
start_compilation(dcp.normal_root_folder, dcp.excel_file)

# we load data for adjusted parameters
prefix = f'{dcp.adjusted}_'
#start_compilation(dcp.adjusted_root_folder, dcp.excel_file, prefix)