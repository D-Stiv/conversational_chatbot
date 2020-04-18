import asyncio
from rasa.nlu.model import Interpreter
from os import path
import rasa
from rasa.nlu.convert import convert_training_data
import utility as u
from state import State
import simulation_constants as cts
import interaction_files_keys as ifk
import json
from random import randint
from datetime import datetime
from selenium import webdriver


form_element = webdriver.Edge()
# webPath = "http://www.polimi.it"
webPath = u.form_url
form_element.get(webPath)
form_element.minimize_window()

form_element = form_element.find_element_by_tag_name('form')
fe = form_element
url_tot = fe.parent.current_url
# we troncate the url just before the question mark
if '?' in url_tot:
    url = url_tot[:url_tot.index('?')]
else:
    url = url_tot
line = f'[browser_name: {fe.parent.name} - page_title: {fe.parent.title} - URL: {url}]'
print(line)
print('yes')

"""
form_elements = form_element.find_elements_by_tag_name('form')
for form_element in form_elements:

    inputs = form_element.find_elements_by_xpath(".//input")

    elems = inputs

    for elem in elems:
        field = elem.get_attribute('bot-field')
        if field:
            print(f'found {field}')
        else:
            print(f'Passing field {field}')
    print('not found')
    bot_tag = form_element.get_attribute('bot-tag')
    print(bot_tag)

slots = []
constructs = {
                "text": None,
                "list": None,
                "form": {
                    "slots": slots
                }
            }
my_state = State(form_element=form_element, constructs=constructs)
my_list = [1, 2, 3, 4, 5]
print(my_list)
my_list.remove(3)
print(my_list)
my_list = [15] + my_list
print(my_list)
print(my_list[1:])

path = f'./{cts.data_folder}/{cts.filling_folder}/{cts.address_names_file}'
with open(path, 'r') as fp_list:
    data_list = json.load(fp_list)
sentence = data_list[0]
answer = sentence
print(6%4)

now = datetime.now()
zero = now - now
print(f'zero is: {zero}')
try:
    days = 0
    try:
        days = zero.days
    except:
        print('level 2')
    print('level 1')
except:
    print('Fail')
"""
