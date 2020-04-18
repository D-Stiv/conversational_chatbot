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
        text = 'The value you inserted only contains the blanks, and so it is not valid.\nYour input should contain at least one character different from the blank'
        return False, text
    return True, text


def verify_compatibility_email(value):
    try:
        text = value
        # we should not have the space in the value
        if ' ' in value:
            text = "The character SPACE should not be present in this value type"
            return False, text
        
        at_sign = '@'
        dot_sign = '.'
        number_at_sign = value.count('@')
        if dot_sign not in value:
            text = f'The email should contain the character < {dot_sign} >'
            return False, text
        if number_at_sign == 0:
            text = f'The email should contain the character < {at_sign} >'
            return False, text
        elif number_at_sign > 1:
            text = f'The email should contain only one character < {at_sign} >'
            return False, text
        if at_sign == value[0]:
            text = f'The email should not start with the character < {at_sign} >'
            return False, text
        elif at_sign == value[len(value)-1]:
            text = f'The email should not end with the character < {at_sign} >'
            return False, text
        pos_at = value.index(at_sign)
        if dot_sign not in value[pos_at :]:
            text = f'There should be at least one character <{dot_sign}> after the character <{at_sign}>'
            return False, text
        return True, text
    except:
        print(
            f'Fail to verify the compatibility of the value {value} for the type email')
        raise Exception


def verify_compatibility_number(value, min_value=-float('inf'), max_value=float('inf')):
    try:
        value = value.replace(' ', '')
        int_value = get_integer(value)
        if int_value is None:
            sorry_style = styles.get_sorry()
            insert_style = styles.get_insert()
            please_style = styles.get_please()
            text = f'{sorry_style} the value {value} is not a number, {please_style} {insert_style} a valid value.'
            return False, text
        return True, value
    except:
        print(f'Fail to verify the compatibility of the value {value} for the type number')
        raise Exception


def verify_compatibility_integer(value, min_value=-float('inf'), max_value=float('inf')):
    try:
        value = value.replace(' ', '')
        int_value = get_integer(value)
        sorry_style = styles.get_sorry()
        insert_style = styles.get_insert()
        please_style = styles.get_please()
        if int_value is None:
            text = f'{sorry_style} the value {value} is not an integer, {please_style} {insert_style} a valid value.'
            return False, text
        number = int(int_value)
        if number < min_value or number > max_value:
            if number < min_value:
                text = f'{sorry_style} the value inserted is less than the minimum value acceptable {min_value}'
            else:
                text = f'{sorry_style} the value inserted is more than the maximum value acceptable {max_value}'
            return False, text
        return True, int_value
    except:
        print(
            f'Fail to verify the compatibility of the value {value} for the type integer')
        raise Exception


def verify_compatibility_decimal(value, precision=2, min_value=-float('inf'), max_value=float('inf')):
    try:
        value = value.replace(' ', '')
        dec_value = get_decimal(value)
        sorry_style = styles.get_sorry()
        insert_style = styles.get_insert()
        please_style = styles.get_please()
        if dec_value is None:
            text = f'{sorry_style} the value {value} is not a decimal, {please_style} {insert_style} a valid value.'
            return False, text
        # float takes the 'dot' as separator, so we should transform it before getting the float
        number = float(dec_value.replace(',', '.'))
        if number < min_value or number > max_value:
            if number < min_value:
                text = f'{sorry_style} the value inserted is less than the minimum value acceptable {min_value}'
            else:
                text = f'{sorry_style} the value inserted is more than the maximum value acceptable {max_value}'
            return False, text
        if ',' not in dec_value:
            return True, dec_value
        # the value has a decimal part
        if precision == float('inf'):
            return True, dec_value
        dec_part = dec_value[dec_value.index(',')+1 :]
        if len(dec_part) <= 2:
            # the precision is respected
            return True, dec_value
        # the precision is more accurate then what required, we decide to troncate, no rounding
        dec_value = dec_value[: dec_value.index(',')+precision+1]
        return True, dec_value
    except:
        print(
            f'Fail to verify the compatibility of the value {value} for the type decimal with precision {precision}')
        raise Exception


def verify_compatibility_password(value):
    try:
        if len(value) < u.min_length_password:
            text = ('The password you proposed is too short. The minimum number ' +
                    f'of characters accepted is {u.min_length_password}')
            return False, text
        lower_value = value.lower()
        all_pwd_chars = u.alphabet + u.number_0_9 + u.password_spec_chars
        for char in lower_value:
            if char not in all_pwd_chars:
                if u.DEBUG:
                    print(f'Character not accepted: {char}')
                text = ('A non acceptable character have been inserted in the passsword.\n' +
                        f'The only accepted special characters are the following {u.password_spec_chars}')
                return False, text
        return True, value
    except:
        print(
            f'Fail to verify the compatibility of the value {value} for the type password')
        raise Exception


def verify_compatibility_tel(value):
    try:
        # we should not have the space in the value
        if ' ' in value:
            text = "The character SPACE should not be present in this value type"
            return False, text
        text = value
        plus_sign = "+"
        num_occur = value.count(plus_sign)
        if num_occur == 1:
            if value[0] != plus_sign:
                text = f'The character < {plus_sign} > could only be at the beginning of the number'
                return False, text
        elif num_occur > 1:
            text = f'A telephone number should not contain the character < {plus_sign} > several times'
            return False, text
        # we remove the eventual plus sign at the beginning
        number = value.replace(plus_sign, '')
        # we verify if the remaining string only contains digits from 0 to 9
        number = fn.convert_to_int(number)
        if number is None or len(value) < u.min_length_phone_number:
            sorry_style = styles.get_sorry()
            insert_style = styles.get_insert()
            please_style = styles.get_please()
            text = f'{sorry_style} the value {value} is not valid, {please_style} {insert_style} a valid phone number'
            return False, text
        return True, text
    except:
        print(
            f'Fail to verify the compatibility of {value} for the type phone number')
        raise Exception


def verify_compatibility_time(value):
    try:
        # the format is HH:MM
        format_string = ('The acceptable formats are the following: <HH:MM>, <HHMM>, <HH:MM am>, ' +
                         '<H>, <H am>, <H:MM>, <H:MM am>')
        # the maximum length is for hh:mm o_clock
        if len(value) > len('hh:mm o_clock'):
            return False, ''
        # we accept <HH:MM> and <HHMM>
        hh = value[:2]
        mm = value[-2:]
        hh = fn.convert_to_int(hh, u.hour)
        mm = fn.convert_to_int(mm, u.minute)
        if hh is not None and mm is not None and len(value) in [4, 5]:
            answer, text = get_time(hh=hh, mm=mm)            
            return answer, text

        # we accept <HH:MM am>
        hh = value[:2]
        mm = value[3:5]
        meridian = value[5:].lower()    # we consider the space
        meridian = meridian.replace(' ', '')    # we remove the space
        hh = fn.convert_to_int(hh, u.hour)
        mm = fn.convert_to_int(mm, u.minute)
        if hh is not None and mm is not None and meridian in time_refs and len(value) >= len('HH:MM am'):
            answer, text = get_time(hh=hh, meridian=meridian, mm=mm)            
            return answer, text

        # we accept <H am>
        hh = value[:2]
        meridian = value[1:].lower()
        meridian = meridian.replace(' ', '')
        hh = fn.convert_to_int(hh, u.hour)
        if hh is not None and meridian in time_refs and len(value) >= len('H am'):
            answer, text = get_time(hh=hh, meridian=meridian)
            return answer, text

        # we accept <H:MM>
        hh = value[0]
        mm = value[-2:]
        hh = fn.convert_to_int(hh, u.hour)
        mm = fn.convert_to_int(mm, u.minute)
        if hh is not None and mm is not None and len(value) == len('H:MM'):
            answer, text = get_time(hh=hh, mm=mm)            
            return answer, text

        # we accept <H:MM am>
        hh = value[0]
        mm = value[2:4]
        meridian = value[4:].lower()    # we consider the space
        meridian = meridian.replace(' ', '')    # we remove the space
        hh = fn.convert_to_int(hh, u.hour)
        mm = fn.convert_to_int(mm, u.minute)
        if hh is not None and mm is not None and meridian in time_refs and len(value) >= len('H:MM am'):
            answer, text = get_time(hh=hh, meridian=meridian, mm=mm)            
            return answer, text

        # we accept <H>
        hh = value
        hh = fn.convert_to_int(hh, u.hour)
        if hh is not None and len(value) == len('H'):
            answer, text = get_time(hh=hh)
            return answer, text

        # we discar all the rest
        text = f"The time you inserted is not valid.\n{format_string}"
        return False, text
    except:
        print(
            f'Fail to verify the compatibility of the value {value} for the type time')
        raise Exception


def verify_compatibility_date(value):
    try:
        # the format is DD-MM-YYYY
        format_string = ('The acceptable formats are the following: <YYYY-MM-DD>, <DD-MM-YYYY>, <MM-DD-YYYY>, ' +
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
                answer, text = get_date(dd=dd, mm=mm, year=year)            
                return answer, text
               
            # we accept <DD-MM-YYYY>
            year = value[-4:]
            mm = value[3:5]
            dd = value[:2]
            year = fn.convert_to_int(year, u.year)
            mm = fn.convert_to_int(mm, u.month)
            dd = fn.convert_to_int(dd, u.day)
            if year is not None and mm is not None and dd is not None:
                answer, text = get_date(dd=dd, mm=mm, year=year)            
                return answer, text

            # we accept <MM-DD-YYYY>
            year = value[-4:]
            mm = value[:2]
            dd = value[3:5]
            year = fn.convert_to_int(year, u.year)
            mm = fn.convert_to_int(mm, u.month)
            dd = fn.convert_to_int(dd, u.day)
            if year is not None and mm is not None and dd is not None:
                answer, text = get_date(dd=dd, mm=mm, year=year)            
                return answer, text

        if len(value) == len('DDMMYYYY'):
            # we accept <DDMMYYYY>
            year = value[-4:]
            mm = value[2:4]
            dd = value[:2]
            year = fn.convert_to_int(year, u.year)
            mm = fn.convert_to_int(mm, u.month)
            dd = fn.convert_to_int(dd, u.day)
            if year is not None and mm is not None and dd is not None:
                answer, text = get_date(dd=dd, mm=mm, year=year)            
                return answer, text

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
                    answer, text = get_date(dd=dd, mm_index=mm_index, year=year)            
                    return answer, text
                   
            # we accept <month DD YYYY>
            year = value[-4:]
            month = value[:-8].lower()
            dd = value[-7:-5]
            if month in months:
                year = fn.convert_to_int(year, u.year)
                mm_index = months.index(month)
                dd = fn.convert_to_int(dd, u.day)
                if year is not None and dd is not None:
                    answer, text = get_date(dd=dd, mm_index=mm_index, year=year)            
                    return answer, text

        # we exclude all the rest
        text = f'The date inserted is not valid\n{format_string}'
        return False, text
    except:
        print(
            f'Fail to verify the compatibility of the value {value} for the type date')
        raise Exception


def verify_compatibility_month(value):
    try:
        # defines a month and a year, the format is YYYY-MM
        format_string = 'The acceptable formats are the following: <YYYY-MM>, <month YYYY>, <YYYY month>'
        # we first validate the right format, with any character in place of < - >
        # we accept <YYYY-MM>
        month = value[-2:]
        year = value[:4]
        month = fn.convert_to_int(month, u.month)
        year = fn.convert_to_int(year, u.year)
        if month is not None:
            month_index = int(month) - 1
            if month_index in range(0, 11+1):
                if year is not None:
                    answer, text = get_date(mm_index=month_index, year=year)            
                    return answer, text
                else:
                    text = f"The year you inserted is not valid for <YYYY-MM>, \n{format_string}"
                    return False, text
            text = f"The month inserted is not valid for <YYYY-MM>, \n{format_string}"
            return False, text

        # we accept < month YYYY > month only in english and any character in between
        year = value[-4:]
        month = value[:-5]  # 4 digit for the year and 1 separatoe
        month = month.lower()
        if month in months:
            year = fn.convert_to_int(year, u.year)
            if year is not None:
                month_index = months.index(month)
                # we create a string with the mont and year in the right format
                answer, text = get_date(mm_index=month_index, year=year)            
                return answer, text
            else:
                text = f'The year is not valid for < month YYYY >. {format_string}'
                return False, text
        # Now we accept < YYYY month > in english with any character in between
        year = value[:4]
        month = value[5:]  # 4 digit for the year and 1 separatoe
        month = month.lower()
        if month in months:
            year = fn.convert_to_int(year, u.year)
            if year is not None:
                month_index = months.index(month)
                # we create a string with the mont and year in the right format
                answer, text = get_date(mm_index=month_index, year=year)            
                return answer, text
            else:
                text = f'The year is not valid for < YYYY month >. \n{format_string}'
                return False, text
        text = f'It is possible that the month you inserted is not well written. \n{format_string}'
        return False, text
    except:
        print(
            f'Fail to verify the compatibility of the value {value} for the type month')
        raise Exception


def get_mm_from_index(index):
    try:
        if index in range(0, 9):
            val = f'0{index + 1}'
        elif index in range(9, 12):
            val = f'{index + 1}'
        else:
            return None
        return val
    except:
        print(f'Fail to get the MM from the index {index}')
        raise Exception


def get_yyyy_from_integer(value):
    try:
        if value in range(0, 10):
            val = f'000{value}'
        elif value in range(10, 100):
            val = f'00{value}'
        elif value in range(100, 1000):
            val = f'0{value}'
        elif value in range(1000, 10000):
            val = f'{value}'
        else:
            return None
        return val
    except:
        print(f'Fail to get YYYY from value {value}')
        raise Exception


def get_mm_from_integer(value):
    try:
        if value in range(1, 10):
            val = f'0{value}'
        elif value in range(10, 12+1):
            val = f'{value}'
        else:
            return None
        return val
    except:
        print(f'Fail to get the MM for the value {value}')
        raise Exception


def get_dd_from_integer(value):
    try:
        if value in range(0, 10):
            val = f'0{value}'
        elif value in range(10, 31+1):
            val = f'{value}'
        else:
            return None
        return val
    except:
        print(f'Fail to get the DD for the value {value}')
        raise Exception


def get_minute_from_integer(value):
    try:
        if value in range(0, 10):
            val = f'0{value}'
        elif value in range(10, 60+1):
            val = f'{value}'
        else:
            return None
        return val
    except:
        print(f'Fail get the minutes for the value {value}')
        raise Exception


def get_hour_from_integer(value, meridian=u.o_clock):
    try:
        if meridian == u.o_clock:
            if value in range(0, 10):
                val = f'0{value}'
            elif value in range(10, 24+1):
                val = f'{value}'
            else:
                return None
            return val
        if meridian == u.am:
            if value in range(0, 10):
                val = f'0{value}'
            elif value in range(10, 12+1):
                val = f'{value}'
            else:
                return None
            return val
        if meridian == u.pm:
            if value in range(1, 12+1):
                val = f'{value + 12}'
            else:
                return None
            return val
    except:
        print(f'Fail to get the hour form the value {value}')
        raise Exception


def get_date(dd=u.VOID, mm=u.VOID, mm_index=u.VOID, year=u.VOID):
    try:
        day = dd
        month = mm
        if dd != u.VOID:
            day = get_dd_from_integer(int(dd))
        if mm != u.VOID and mm_index == u.VOID:
            month = get_mm_from_integer(int(mm))
        elif mm == u.VOID and mm_index != u.VOID:
            month = get_mm_from_index(mm_index)
        year = get_yyyy_from_integer(int(year))
        if None not in [day, month, year]:
            if day != u.VOID:
                text = f'{day}-{month}-{year}'
            else:
                text = f'{month}-{year}'
            return True, text
        text = u.VOID
        if day is None:
            text = 'The day you inserted is out of range'
        if month is None:
            month_text = 'The month you inserted is out of range'
            if text == u.VOID:
                text = month_text
            else:
                text = f'{text}. {month_text}'
        if year is None:
            year_text = f'The year you inserted is out of range, the minimum is {u.min_year} and the maximum is {u.max_year}'
            if text == u.VOID:
                text = year_text
            else:
                text = f'{text}. {year_text}'
        return False, text
    except:
        print('Fail to return the date in the right format')
        raise Exception


def get_time(hh=u.VOID, meridian=u.VOID, mm=u.VOID):
    try:
        if meridian == u.VOID:
            hour = get_hour_from_integer(int(hh))
        else:
            hour = get_hour_from_integer(int(hh), meridian)
        if mm != u.VOID:
            minutes = get_minute_from_integer(int(mm))
        else:
            minutes = '00'
        if None not in [hour, minutes]:
            text = f'{hour}:{minutes}'
            return True, text
        text = u.VOID
        if hour is None:
            text = f'The hour is out of range'
        if minutes is None:
            minute_text = f'The minutes are out of range'
            if text == u.VOID:
                text = minute_text
            else:
                text = f'{text}, {minute_text}'
        return False, text
    except:
        print('Fail to return the time in the right format')
        raise Exception


def get_decimal(value):
    try:
        # returns a string in format ID* or ID*,D* with I in [1,9] and D in [0,9]
        # accepts ID* or ID*,D* or ID?(.DDD)* or ID?(.DDD)*,D* or ID?(,DDD)* or ID?(,DDD)*.D*
        num_comma = value.count(',')
        num_dot = value.count('.')
        # an integer value is decimal
        if (num_comma == 0 and num_dot == 0) or (num_comma == 0 and num_dot > 1) or (num_comma > 1 and num_dot == 0):
            return get_integer(value)
        if num_comma > 1 and num_dot > 1:
            return None
        # format of type ID?D?.D* or ID?D?,D*
        if num_comma + num_dot == 1:
            if num_comma == 1:
                separator = ','
            else:
                separator = '.'
            before = value[:value.index(separator)]
            after = value[value.index(separator)+1:]
            try:
                before = int(before)
                # we only verify whether or not after can be cast in integer
                int(after)
            except:
                return None
            value = f'{before},{after}'
            return value
        # format of type ID?D?,DDD.D* or ID?D?.DDD,D*
        if num_comma == 1 and num_dot == 1:
            pos_comma = value.index(',')
            pos_dot = value.index('.')
            if pos_comma < pos_dot:
                pos = pos_dot
            else:
                pos = pos_comma
            before = get_integer(value[:pos])
            if before is None:
                return None
            after = value[pos+1:]
            try:
                int(after)
            except:
                return None
            value = f'{before},{after}'
            return value
        # format of type ID?D?,DDD(,DDD)+.D* or ID?D?.DDD(.DDD)+,D*
        if (num_comma == 1 and num_dot > 1) or (num_dot == 1 and num_comma > 1):
            if num_comma == 1:
                pos = value.index(',')
            else:
                pos = value.index('.')
            before = get_integer(value[:pos])
            if before is None:
                return None
            after = value[pos+1:]
            try:
                int(after)
            except:
                return None
            value = f'{before},{after}'
            return value
        # all the other cases are discarded
        return None
    except:
        print('Fail to get the decimal number')
        raise Exception


def get_integer(value):
    try:
        # returns a string in format ID* with I in [1,9] and D in [0,9]
        # accepts ID* or ID?(.DDD)* or ID?(,DDD)* 
        if '.' not in value and ',' not in value:
            value = value.replace(' ', '')
            try:
                value = int(value)
            except:
                if u.DEBUG:
                    print('The value contains a non acceptable character')
                return None
            return f'{value}'
        if '.' in value and ',' in value:
            # the integer cannot have both comma and dot
            return None
        if '.' in value:
            separator = '.'
        else:
            separator = ','
        string_value = ''
        while len(value) > 3:
            try:
                # we verify whether or not the last three characters can be cast in integer
                int(value[-3:])
            except:
                return None
            string_value = f'{value[-3:]}{string_value}'
            if value[-4:-3] != separator:
                return None
            value = value[:-4]
        try:
            first = int(value)
        except:
            return None
        string_value = f'{first}{string_value}'
        return string_value
    except:
        print('Fail to get the integer number')
        raise Exception