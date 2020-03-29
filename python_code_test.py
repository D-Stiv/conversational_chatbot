import asyncio
from rasa.nlu.model import Interpreter
from os import path
import rasa
from rasa.nlu.convert import convert_training_data
import utility as u
from state import State
import simulation_constants as cts

from selenium import webdriver
"""
form_element = webdriver.Edge()
form_element.minimize_window()
# webPath = "http://www.polimi.it"
webPath = u.form_url
form_element.get(webPath)
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
my_state = State(form_element=form_element, constructs=constructs)"""

my_list = [1,2,3,4,5]
print(my_list)
my_list.remove(3)
print(my_list)
my_list = [15] + my_list
print(my_list)
print(my_list[1:])

print('TTTT'.lower())