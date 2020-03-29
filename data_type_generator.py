# generator of data types

from random import randint


def generate_choice(choice_name):
    try:
        choice_value = get_random_value(choices_lists[choice_name])
        return choice_value
    except:
        print(f'Fail to generate the choice for {choice_name}')
        raise Exception

def generate_choices(choice_name):
    try:
        # useful when you have a checkbox and you can select many values
        total_choices = choices_lists[choice_name]
        number = len(total_choices)
        num_choices = randint(1, min(2, number))
        if num_choices == number:
            return total_choices
        partial_choices = []
        for _ in range(num_choices):
            choice = get_random_value(total_choices)
            partial_choices.append(choice)
            total_choices.remove(choice)
        return partial_choices
    except:
        print(f'Fail to generate the choice for {choice_name}')
        raise Exception

def generate_date():
    try:
        min_year = 1900
        max_year = 2019
        year = randint(min_year, max_year)
        month_letter = randint(0,1)
        month_dic = data[cts.months]
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

def generate_name():
    try:
        name = get_random_value(data[cts.names])
        return name
    except:
        print(f'Fail to generate a name')
        raise Exception

def generate_country():
    try:
        country = get_random_value(data[cts.countries])
        return country
    except:
        print(f'Fail to generate a country')
        raise Exception

def generate_city():
    try:
        city = get_random_value(data[cts.cities])
        return city
    except:
        print(f'Fail to generate a city')
        raise Exception

def generate_place_address():
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
        my_name = get_random_value(data[cts.address_namse])
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

def get_random_value(my_list):
        index = randint(0, len(my_list))
        return my_list[index]

