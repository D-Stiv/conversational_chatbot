# module to give different styles to words
from random import randint
import utility


def get_please():
    please_present = randint(0, 1)
    if please_present:
        please_style = 'please'
    else:
        please_style = ''
    return please_style

def get_sorry():
    sorry_present = randint(0, 1)
    if sorry_present:
        sorry_style = 'sorry'
    else:
        sorry_style = ''
    return sorry_style

def get_sure():
    sure_present = randint(0, 1)
    if sure_present:
        sure_style = 'sure'
    else:
        sure_style = ''
    return sure_style

def get_thanks():
    thanks_present = randint(0, 1)
    if thanks_present:
        thanks_style = 'thank you'
    else:
        thanks_style = ''
    return thanks_style

def get_next():
    next_styles = utility.next_styles
    next_index = randint(0, len(next_styles) - 1)
    next_style = next_styles[next_index]
    return next_style


def get_again():
    again_styles = utility.again_styles
    again_index = randint(0, len(again_styles) - 1)
    again_style = again_styles[again_index]
    return again_style


def get_end():
    terminator = utility.terminator
    end_index = randint(0, len(terminator) - 1)
    if terminator[end_index] in ['terminator', 'finished']:
        end_style = 'end'
    else:
        end_style = terminator[end_index]
    return end_style

def get_good():
    good_styles = utility.good_styles
    limit = len(good_styles)
    index = randint(0, limit-1)
    good_style = good_styles[index]
    return good_style

def get_insert():
    insert_styles = utility.insert_styles
    insert_index = randint(0, len(insert_styles) - 1)
    insert_style = insert_styles[insert_index]
    return insert_style

def get_modify():
    modify_styles = utility.modify_styles
    modify_index = randint(0, len(modify_styles) - 1)
    modify_style = modify_styles[modify_index]
    return modify_style