import asyncio
from rasa.nlu.model import Interpreter
from os import path
import rasa
from rasa.nlu.convert import convert_training_data
import utility as u
from state import State

from selenium import webdriver
"""
driver = webdriver.Edge()
driver.minimize_window()
#webPath = "http://www.polimi.it"
webPath = u.new_url
driver.get(webPath)
form_elements = driver.find_elements_by_tag_name('form')
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

root_folder = f'./{u.global_folder}/{u.registration_form_folder}'
model_path=f'{root_folder}/{u.models_folder}/{u.tag_registration_form}/{u.tag_registration_form}'
interpreter = Interpreter.load(model_path)
print('ok')