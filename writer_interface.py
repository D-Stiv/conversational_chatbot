# CLASS
# APIs to write a text file in a given dirctory

from datetime import datetime
import utility as u

class Writer:
    def __init__(
        self,
        counter_trigger,
        destination_folder,
        file_type
    ):
        # initialize the writer
        self.counter_trigger = counter_trigger
        self.destination_folder = destination_folder
        self.file_type = file_type
    
    def construct_header(self):
        try:
            if self.counter_trigger is None:
                trigger_string = 'The value of S have not been specified.'
            else:
                trigger_string = f'S = {self.counter_trigger}.'
            header_content = f'\tDate and Hour: {datetime.now()}'
            header = f'HEADER\t{trigger_string}\n\n{header_content}'
            return header
        except:
            print('Fail to construct the header')
            raise Exception

    def create_file(self, text):
        try:
            file_path = self.get_file_path()
            new_file = open(file_path, 'w')
            new_file.writelines(text)
            new_file.close()
        except:
            print('Fail to create the file')
            raise Exception

    def get_file_path(self):
        try:
            temp = f'{datetime.now()}'
            format_timestamp = temp.replace('-', '').replace(' ', '_').replace(':', '').replace('.', '_')
            file_path = f'./{self.destination_folder}/{self.file_type}_{format_timestamp}.txt'
            return file_path
        except:
            print('Fail to get the file path')
            raise Exception

