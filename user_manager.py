from random import randint, shuffle
import utility as u
import simulation_constants as cts
import json


class User:
    def __init__(
        self,
        dialogue_state
    ):
        # we initialize the user
        self.dialogue_state = dialogue_state
        self.spelling_mode = False
        self.spelling_string = ''
        self.spelling_string_index = 0
        self.choices_lists = self.initialize_choices_state()
        self.data = self.initialize_data()

    def initialize_choices_state(self):
        try:
            slots = self.dialogue_state.construct['fom']['slots']
            choices_lists = {}
            for slot in slots:
                if u.choice_list in slot.keys():
                    choices_lists[slot[u.value_name]] = slot[u.choice_list]
            return choices_state
        except:
            print('Fail to initialize the choices state')
            raise Exception
    
    def initialize_data(self):
        try:
            data = {
                cts.filling: {},
                cts.interaction: {}
            }
            # we start with the filling files
            keys = cts.filling_keys
            files_names = cts.filling_files_names
            for index in range(len(keys)):
                # we load a given json file which is a list
                path = f'./{cts.data_folder}/{cts.filling_folder}/{files_names[index]}'
                with open(path, 'r') as fp_list:
                    data_list = json.load(fp_list)
                # we shuffle the list
                shuffle(data_list)
                # we associate to the list loaded the corresponding key
                data[cts.filling][keys[index]] = data_list
            # we proceed with the interaction files
            keys = cts.interaction_keys
            files_names = cts.interaction_files_names
            for index in range(len(keys)):
                # we load a given json file which is a list
                path = f'./{cts.data_folder}/{cts.interaction_folder}/{files_names[index]}'
                with open(path, 'r') as fp:
                    data = json.load(fp)
                # we associate to the list loaded the corresponding key
                data[cts.interaction][keys[index]] = data
            return data
        except:
            print('Fail to initialize the data')
            raise Exception

    def get_answer(self, text=''):
        try:
            """we are mainly going to use the state to construct the response but 
            in some precise situtions the text coul be useful for an immediate answer"""
            return ''
        except:
            print('Fail to get the user answer')
            raise Exception

    def construct_interaction_message(self):
        try:
            pass
        except:
            print(f'Fail to construct an interaction message')
            raise Exception

    def cunstruct_filling_message(self):
        try:
            pass
        except:
            print(f'Fail to construct a filling message')
            raise Exception

    def generate_choice(self, choice_name):
        try:
            choice_value = self.get_random_value(self.choices_lists[choice_name])
            return choice_value
        except:
            print(f'Fail to generate the choice for {choice_name}')
            raise Exception

    def generate_choices(self, choice_name):
        try:
            # useful when you have a checkbox and you can select many values
            total_choices = self.choices_lists[choice_name]
            number = len(total_choices)
            num_choices = randint(1, min(2, number))
            if num_choices == number:
                return total_choices
            partial_choices = []
            for _ in range(num_choices):
                choice = self.get_random_value(total_choices)
                partial_choices.append(choice)
                total_choices.remove(choice)
            return partial_choices
        except:
            print(f'Fail to generate the choice for {choice_name}')
            raise Exception

    def generate_date(self):
        try:
            min_year = 1900
            max_year = 2019
            year = randint(min_year, max_year)
            month_letter = randint(0,1)
            month_dic = self.data[cts.months]
            day = randint(1, month_dic['number_days'])
            if day < 10:
                day = f'0{day}'
            if month_letter:
                # month in letters
                month = self.get_random_value(month_dic['month'])
                separator = ' '
            else:
                month = month_dic['month_letter']
                separator = self.get_random_value(['-', '/', ''])
            # there are two main styles, day before month and month before day
            style_one = randint(0,1)
            if style_one:
                # day before month
                date = f'{day}{separator}{month}{separator}{year}'
            else:
                # month before day
                date = f'{month}{separator}{day}{separator}{year}'
            return date
        except:
            print(f'Fail to generate a data')
            raise Exception

    def generate_time(self):
        try:
            # different formats
            meridians = ['am', 'pm', "o'clock", '']
            separator = randint(o,1)
            separator_types = ['.', ':', "'"]
            meridian = self.get_random_value(meridians)
            hour_part = self.give_hour(meridian)
            if separator:
                separator_type = self.get_random_value(separator_types)
                minute_part = self.get_minute
            else:
                separator_type = ''
                minute_part = ''
            time = f'{hour_part}{separator_type}{minute_part} {meridian}'
            return time
        except:
            print(f'Fail to generate a time')
            raise Exception

    def give_hour(self, meridian):
        try:
            # returns a string representing the hour part of the time
            min_hour = 0
            if meridian in ['am', 'pm']:
                max_hour = 12
            else:
                max_hour = 24
            double_digit = randint(0,1)
            if double_digit:
                hour = randint(min_hour, max_hour)
                if hour < 10:
                    hour = f'0{hour}'
            else:
                hour = randint(min_hour, 9)
            hour_part = f'{hour}'
            return hour_part
        except:
            print('Fail to give an hour')
            raise Exception

    def give_minute(self):
        try:
            min_mm = 0
            max_mm = 59
            double_digit = randint(0,1)
            if double_digit:
                minute = randint(min_mm, max_mm)
                if minute < 10:
                    minute = f'0{minute}'
            else:
                minute = randint(min_mm, 9)
            minute_part = f'{minute}'
            return minute_part
        except:
            print('Fail to give minutes')
            raise Exception

    def generate_name(self):
        try:
            name = self.get_random_value(self.data[cts.names])
            return name
        except:
            print(f'Fail to generate a name')
            raise Exception

    def generate_country(self):
        try:
            country = self.get_random_value(self.data[cts.countries])
            return country
        except:
            print(f'Fail to generate a country')
            raise Exception

    def generate_city(self):
        try:
            city = self.get_random_value(self.data[cts.cities])
            return city
        except:
            print(f'Fail to generate a city')
            raise Exception

    def generate_place_address(self):
        try:
            min_num = 10
            max_num = 50
            # we have 3 styles french, british, italian
            styles = ['french', 'british', 'italian']
            style = self.get_random_value(styles)
            if style == 'french':
                # format is number type name
                types = ['rue', 'place', 'avenue', 'boulevard']
            elif style == 'british':
                # the format is number name type
                types = ['street', 'road', 'avenue', 'boulevard']
            elif style == 'italian':
                # the format is type name number
                types = ['via', 'viale', 'piazza', 'pzle']
            my_type = self.get_random_value(types)
            my_name = self.get_random_value(self.data[cts.address_namse])
            my_number = randint(min_num, max_num)
            text = '{} {} {}'
            if style == 'french':
                # format is number type name
                place_address = text.format(my_number, my_type, my_name)
            elif style == 'british':
                # the format is number name type
                place_address = text.format(my_number, my_name, my_type)
            elif style == 'italian':
                # the format is type name number
                place_address = text.format(my_type, my_name, my_number)
            return place_address
        except:
            print(f'Fail to generate a place address')
            raise Exception

    def generate_phone_number(self):
        try:
            prefixes = cts.phone_prefixes
            signs = ['00', '+']
            length = u.min_length_phone_number + 5
            phone_number = f'{self.get_random_value(signs)}{self.get_random_value(prefixes)}'
            for _ in range(length):
                phone_number = f'{phone_number}{randint(0, 9)}'
            return phone_number
        except:
            print(f'Fail to generate a phone number')
            raise Exception

    def get_random_value(self, my_list):
        index = randint(0, len(my_list))
        return my_list[index]


class BadUser(User):
    def __init__(
        self,
        slots
    ):
        # we initialize the user
        super().__init__(slots)
