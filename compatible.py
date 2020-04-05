# module to verify the compatibility of value types
import functions as fn
import styles
import utility as u

months = u.months
time_refs = u.time_refs


def verify_compatibility_generic(value):
    # returns false when the value only contains blanks
    text = value
    value = value.replace(' ', '')
    if value == '':
        text = 'the value you inserted only contains the blanks, and so it is not valid.\n your input should contain at least one charater different from the blank'
        return False, text
    return True, text


def verify_compatibility_email(value):
    try:
        text = value
        at_sign = '@'
        if at_sign not in value:
            text = 'the email should contain the character < {} >'.format(
                at_sign)
            return False, text
        elif at_sign == value[0]:
            text = 'the email should not start with the character < {} >'.format(
                at_sign)
            return False, text
        elif at_sign == value[len(value)-1]:
            text = 'the email should not end with the character < {} >'.format(
                at_sign)
            return False, text
        return True, text
    except:
        print(
            f'Fail faile to verify the compatibility of the value {value} for the type email')
        raise Exception


def verify_compatibility_number(value):
    try:
        text = value
        text = fn.convert_to_int(value)
        if text is None:
            sorry_style = styles.get_sorry()
            insert_style = styles.get_insert()
            please_style = styles.get_please()
            text = '{} the value {} is not a number, {} {} a valid value.'.format(
                sorry_style, value, please_style, insert_style)
            return False, text
        return True, text
    except:
        print(
            f'Fail faile to verify the compatibility of the value {value} for the type number')
        raise Exception


def verify_compatibility_password(value):
    try:
        if len(value) < u.min_length_password:
            text = ('the password you proposed is too short. The minimum number ' +
                    'of characters accepted is {}').format(u.min_length_password)
            return False, text
        lower_value = value.lower()
        all_pwd_chars = u.alphabet + u.number_0_9 + u.password_spec_chars
        for char in lower_value:
            if char not in all_pwd_chars:
                if u.DEBUG:
                    print(f'Character not accepted: {char}')
                text = ('a non acceptable character have been inserted in the passsword.\n' +
                        'the only accepted special characters are the following {}').format(u.password_spec_chars)
                return False, text
        return True, value
    except:
        print(
            f'Fail to verify the compatibility of the value {value} for the type password')
        raise Exception


def verify_compatibility_tel(value):
    try:
        text = value
        plus_sign = "+"
        num_occur = value.count(plus_sign)
        if num_occur == 1:
            if value[0] != plus_sign:
                text = 'the character < {} > could only be at the beginning of the number'.format(
                    plus_sign)
                return False, text
        elif num_occur > 1:
            text = 'a telephone number should not contain the character < {} > several times'.format(
                plus_sign)
            return False, text
        # we remove the eventual plus sign at the beginning
        number = value.replace(plus_sign, '')
        # we verify if the remaining string only contains digits from 0 to 9
        number = fn.convert_to_int(number)
        if number is None or len(value) < u.min_length_phone_number:
            sorry_style = styles.get_sorry()
            insert_style = styles.get_insert()
            please_style = styles.get_please()
            text = '{} the value {} is not valid, {} {} a valid phone number'.format(
                sorry_style, value, please_style, insert_style)
            return False, text
        return True, text
    except:
        print(
            f'Fail to verify the compatibility of {value} for the type phone number')
        raise Exception


def verify_compatibility_time(value):
    try:
        # the format is HH:MM
        format_string = ('the acceptable formats are the following: <HH:MM>, <HHMM>, <HH:MM am>, ' +
                         '<H>, <H am>, <H:MM>, <H:MM am>')
        # the maximum length is for hh:mm o_clock
        if len(value) > len('hh:mm o_clock'):
            return False, ''
        # we accept <HH:MM> and <HHMM>
        hh = value[:2]
        mm = value[-2:]
        hh = fn.convert_to_int(hh, u.hour)
        mm = fn.convert_to_int(mm, u.minute)
        if hh is not None and mm is not None:
            text = '{}:{}'.format(get_hour_from_integer(
                int(hh)), get_minute_from_integer(int(mm)))
            return True, text

        # we accept <HH:MM am>
        hh = value[:2]
        mm = value[3:5]
        meridian = value[5:].lower()    # we consider the space
        meridian = meridian.replace(' ', '')    # we remove the space
        hh = fn.convert_to_int(hh, u.hour)
        mm = fn.convert_to_int(mm, u.minute)
        if hh is not None and mm is not None and meridian in time_refs:
            text = '{}:{}'.format(get_hour_from_integer(
                int(hh), meridian), get_minute_from_integer(int(mm)))
            return True, text

        # we accept <H>
        hh = value
        hh = fn.convert_to_int(hh, u.hour)
        if hh is not None:
            text = '{}:00'.format(get_hour_from_integer(int(hh)))
            return True, text

        # we accept <H am>
        hh = value[:2]
        meridian = value[1:].lower()
        meridian = meridian.replace(' ', '')
        hh = fn.convert_to_int(hh, u.hour)
        if hh is not None and meridian in time_refs:
            text = '{}:00'.format(get_hour_from_integer(int(hh), meridian))
            return True, text

        # we accept <H:MM>
        hh = value[0]
        mm = value[-2:]
        hh = fn.convert_to_int(hh, u.hour)
        mm = fn.convert_to_int(mm, u.minute)
        if hh is not None and mm is not None:
            text = '{}:{}'.format(get_hour_from_integer(
                int(hh)), get_minute_from_integer(int(mm)))
            return True, text

        # we accept <H:MM am>
        hh = value[0]
        mm = value[2:4]
        meridian = value[4:].lower()    # we consider the space
        meridian = meridian.replace(' ', '')    # we remove the space
        hh = fn.convert_to_int(hh, u.hour)
        mm = fn.convert_to_int(mm, u.minute)
        if hh is not None and mm is not None and meridian in time_refs:
            text = '{}:{}'.format(get_hour_from_integer(
                int(hh), meridian), get_minute_from_integer(int(mm)))
            return True, text

        # we discar all the rest
        text = f"the time you inserted is not valid.\n{format_string}"
        return False, text
    except:
        print(
            f'Fail faile to verify the compatibility of the value {value} for the type time')
        raise Exception


def verify_compatibility_date(value):
    try:
        # the format is DD-MM-YYYY
        format_string = ('the acceptable formats are the following: <YYYY-MM-DD>, <DD-MM-YYYY>, <MM-DD-YYYY>, ' +
                         '<DDMMYYYY>, <DD month YYYY>, <month DD YYYY>')
        
        if len(value) == len('YYYY-MM-DD'):
            # we accept <YYYY-MM-DD>
            year = value[:4]
            mm = value[5:7]
            dd = value[-2:]
            year = fn.convert_to_int(year, u.year)
            mm = fn.convert_to_int(mm, u.month)
            dd = fn.convert_to_int(dd, u.day)
            if year is not None and mm is not None and dd is not None:
                text = '{}-{}-{}'.format(get_dd_from_integer(int(dd)),
                                        get_mm_from_integer(int(mm)),get_yyyy_from_integer(int(year)) )
                return True, text

            # we accept <DD-MM-YYYY>
            year = value[-4:]
            mm = value[3:5]
            dd = value[:2]
            year = fn.convert_to_int(year, u.year)
            mm = fn.convert_to_int(mm, u.month)
            dd = fn.convert_to_int(dd, u.day)
            if year is not None and mm is not None and dd is not None:
                text = '{}-{}-{}'.format(get_dd_from_integer(int(dd)),
                                        get_mm_from_integer(int(mm)),get_yyyy_from_integer(int(year)) )
                return True, text

            # we accept <MM-DD-YYYY>
            year = value[-4:]
            mm = value[:2]
            dd = value[3:5]
            year = fn.convert_to_int(year, u.year)
            mm = fn.convert_to_int(mm, u.month)
            dd = fn.convert_to_int(dd, u.day)
            if year is not None and mm is not None and dd is not None:
                text = '{}-{}-{}'.format(get_dd_from_integer(int(dd)),
                                        get_mm_from_integer(int(mm)),get_yyyy_from_integer(int(year)) )
                return True, text

        if len(value) == len('DDMMYYYY'):
            # we accept <DDMMYYYY>
            year = value[-4:]
            mm = value[2:4]
            dd = value[:2]
            year = fn.convert_to_int(year, u.year)
            mm = fn.convert_to_int(mm, u.month)
            dd = fn.convert_to_int(dd, u.day)
            if year is not None and mm is not None and dd is not None:
                text = '{}-{}-{}'.format(get_dd_from_integer(int(dd)),
                                        get_mm_from_integer(int(mm)),get_yyyy_from_integer(int(year)) )
                return True, text

        if len(value) >= len('DD may YYYY'):
            # we accept <DD month YYYY>
            year = value[-4:]
            month = value[3:-5].lower()
            dd = value[:2]
            if month in months:
                year = fn.convert_to_int(year, u.year)
                mm_index = months.index(month)
                dd = fn.convert_to_int(dd, u.day)
                if year is not None and dd is not None:
                    text = '{}-{}-{}'.format(get_dd_from_integer(int(dd)),
                                            get_mm_from_index(mm_index), get_yyyy_from_integer(int(year)))
                    return True, text

            # we accept <month DD YYYY>
            year = value[-4:]
            month = value[:-8].lower()
            dd = value[-7:-5]
            if month in months:
                year = fn.convert_to_int(year, u.year)
                mm_index = months.index(month)
                dd = fn.convert_to_int(dd, u.day)
                if year is not None and dd is not None:
                    text = '{}-{}-{}'.format(get_dd_from_integer(int(dd)),
                                            get_mm_from_index(mm_index), get_yyyy_from_integer(int(year)))
                    return True, text

        # we exclude all the rest
        text = 'the date inserted is not valid\n{}'.format(format_string)
        return False, text
    except:
        print(
            f'Fail faile to verify the compatibility of the value {value} for the type date')
        raise Exception


def verify_compatibility_month(value):
    try:
        # defines a month and a year, the format is YYYY-MM
        format_string = 'the acceptable formats are the following: <YYYY-MM>, <month YYYY>, <YYYY month>'
        # we first validate the right format, with any character in place of < - >
        # we accept <YYYY-MM>
        month = value[-2:]
        year = value[:4]
        month = fn.convert_to_int(month, u.month)
        year = fn.convert_to_int(year, u.year)
        if month is not None:
            month_index = int(month)
            if month_index in range(1, 12+1):
                if year is not None:
                    text = '{}-{}'.format(get_yyyy_from_integer(int(year)),
                                          get_mm_from_index(month_index))
                    return True, text
                else:
                    text = "the year you inserted is not valid, \n{}".format(
                        format_string)
                    return False, text
            text = "the month insert is not valid, \n{}".format(format_string)
            return False, text

        # we accept < month YYYY > month only in english and any character in between
        year = value[-4:]
        month = value[:-5]  # 4 digit for the year and 1 separatoe
        month = month.lower()
        if month in months:
            year = fn.convert_to_int(year, u.year)
            if year is not None:
                month = get_mm_from_index(months.index(month))
                # we create a string with the mont and year in the right format
                text = '{}-{}'.format(get_yyyy_from_integer(int(year)), month)
                return True, text
            else:
                text = 'the year is not valid. {}'.format(format_string)
                return False, text
        # Now we accept < YYYY month > in english with any character in between
        year = value[:4]
        month = value[5:]  # 4 digit for the year and 1 separatoe
        month = month.lower()
        if month in months:
            year = fn.convert_to_int(year, u.year)
            if year is not None:
                month = get_mm_from_index(months.index(month))
                # we create a string with the mont and year in the right format
                text = '{}-{}'.format(get_yyyy_from_integer(int(year)), month)
                return True, text
            else:
                text = 'the year is not valid. \n{}'.format(format_string)
                return False, text
        text = 'it is possible that the month you inserted is not well written. \n{}'.format(
            format_string)
        return False, text
    except:
        print(
            f'Fail faile to verify the compatibility of the value {value} for the type month')
        raise Exception


def get_mm_from_index(index):
    try:
        if index in range(0, 9):
            val = '0{}'.format(index + 1)
        elif index in range(9, 12):
            val = '{}'.format(index + 1)
        else:
            raise Exception('month out of range')
        return val
    except:
        print(f'Fail to get the MM from the index {index}')
        raise Exception


def get_yyyy_from_integer(value):
    try:
        if value in range(0, 10):
            val = '000{}'.format(value)
        elif value in range(10, 100):
            val = '00{}'.format(value)
        elif value in range(100, 1000):
            val = '0{}'.format(value)
        elif value in range(1000, 10000):
            val = '{}'.format(value)
        else:
            raise Exception('year out of range')
        return val
    except:
        print(f'Fail to get YYYY from value {value}')
        raise Exception


def get_mm_from_integer(value):
    try:
        if value in range(1, 10):
            val = '0{}'.format(value)
        elif value in range(10, 12+1):
            val = '{}'.format(value)
        else:
            raise Exception('month out of range')
        return val
    except:
        print(f'Fail to get the MM for the value {value}')
        raise Exception


def get_dd_from_integer(value):
    try:
        if value in range(0, 10):
            val = '0{}'.format(value)
        elif value in range(10, 31+1):
            val = '{}'.format(value)
        else:
            raise Exception('day out of range')
        return val
    except:
        print(f'Fail to get the DD for the value {value}')
        raise Exception


def get_minute_from_integer(value):
    try:
        if value in range(0, 10):
            val = '0{}'.format(value)
        elif value in range(10, 60+1):
            val = '{}'.format(value)
        else:
            raise Exception('minutes out of range')
        return val
    except:
        print(f'Fail get the minutes for the value {value}')
        raise Exception


def get_hour_from_integer(value, meridian=u.o_clock):
    try:
        if meridian == u.o_clock:
            if value in range(0, 10):
                val = '0{}'.format(value)
            elif value in range(10, 24+1):
                val = '{}'.format(value)
            else:
                raise Exception('hour out of range')
            return val
        if meridian == u.am:
            if value in range(0, 10):
                val = '0{}'.format(value)
            elif value in range(10, 12+1):
                val = '{}'.format(value)
            else:
                raise Exception('hour out of range')
            return val
        if meridian == u.pm:
            if value in range(1, 12+1):
                val = '{}'.format(value + 12)
            else:
                raise Exception('hour out of range')
            return val
    except:
        print(f'Fail to get the hour form the value {value}')
        raise Exception