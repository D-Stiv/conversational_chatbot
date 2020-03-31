# generator of data types

from random import randint
import utility as u
import simulation_constants as cts


def generate_date(months):
    # receive the data structure of the months, list of dictionaries
    try:
        min_year = 1900
        max_year = 2019
        year = randint(min_year, max_year)
        month_letter = randint(0,1)
        month_dic = get_random_value(months)
        day = randint(1, month_dic['number_days'])
        if day < 10:
            day = f'0{day}'
        if month_letter:
            # month in letters
            month = get_random_value(month_dic['month'])
            separator = ' '
        else:
            month = month_dic['month_letter']
            separator = get_random_value(['-', '/', ''])
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

def generate_time():
    try:
        # different formats
        meridians = ['am', 'pm', "o'clock", '']
        separator = randint(o,1)
        separator_types = ['.', ':', "'"]
        meridian = get_random_value(meridians)
        hour_part = give_hour(meridian)
        if separator:
            separator_type = get_random_value(separator_types)
            minute_part = get_minute
        else:
            separator_type = ''
            minute_part = ''
        time = f'{hour_part}{separator_type}{minute_part} {meridian}'
        return time
    except:
        print(f'Fail to generate a time')
        raise Exception

def give_hour(meridian):
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

def give_minute():
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

def generate_place_address(address_names):
    try:
        min_num = 10
        max_num = 50
        # we have 3 styles french, british, italian
        styles = ['french', 'british', 'italian']
        style = get_random_value(styles)
        if style == 'french':
            # format is number type name
            types = ['rue', 'place', 'avenue', 'boulevard']
        elif style == 'british':
            # the format is number name type
            types = ['street', 'road', 'avenue', 'boulevard']
        elif style == 'italian':
            # the format is type name number
            types = ['via', 'viale', 'piazza', 'pzle']
        my_type = get_random_value(types)
        my_name = get_random_value(address_namse)
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

def generate_phone_number():
    try:
        prefixes = cts.phone_prefixes
        signs = ['00', '+']
        length = u.min_length_phone_number + 5
        phone_number = f'{get_random_value(signs)}{get_random_value(prefixes)}'
        for _ in range(length):
            phone_number = f'{phone_number}{randint(0, 9)}'
        return phone_number
    except:
        print(f'Fail to generate a phone number')
        raise Exception

def generate_email(name):
    try:
        name = name.replace(' ', '.')
        # format is first_part@damain_name.extension
        domain_names = ['yahoo', 'gmail', 'hotmail', 'polimi', 'outlook']
        extensions = ['cm', 'com', 'uk', 'it', 'fr']
        min_length_first_part = 5
        max_length_first_part = 9
        # first part computation
        length = randint(min_length_first_part, max_length_first_part)
        first_part = name
        if length > len(name):            
            diff = length - len(name)
            possible_char = u.alphabet + u.number_0_9
            for _ in range(diff):
                char = get_random_value(possible_char)
                if randint(0,1):
                    first_part = f'{first_part}{char}'
                else:
                    first_part = f'{char}{first_part}'
        # domain
        domain = get_random_value(domain_names)
        # extension
        extension = get_random_value(extensions)
        email = f'{first_part}@{domain}.{extension}'
        return email
    except:
        print('Fail to generate an email')
        raise Exception

def generate_password(name):
    try:
        name = name.replace(' ', '.')
        min_length_password = 5
        max_length_password = 9
        # first part computation
        length = randint(min_length_password, max_length_password)
        password = name
        if length > len(name):            
            diff = length - len(name)
            possible_char = u.alphabet + u.number_0_9 + u.password_spec_chars
            for _ in range(diff):
                char = get_random_value(possible_char)
                if randint(0,1):
                    password = f'{password}{char}'
                else:
                    password = f'{char}{password}'
        return password
    except:
        print('Fail to generate a password')
        raise Exception

def get_random_value(my_list, number=1):
    # get a random value in a list of objects
    try:
        if number != 1:
            values = []
            for _ in range(number):
                value = my_list[randint(0, len(my_list)-1)]
                while value in values:
                    value = my_list[randint(0, len(my_list)-1)]
                values.append(value)
            return values
        else:
            index = randint(0, len(my_list)-1)
            value = my_list[index]
            return value
    except:
        print('Fail to get a random')
        raise Exception

