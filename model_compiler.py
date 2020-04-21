# model compiler to load the new model when necessary

import asyncio
import rasa
import shutil
from os import path
import utility as u

root_folder = f'./{u.registration_form_folder}'
domain_file_path=f'{root_folder}/{u.training_folder}/{u.domain_file}'
model_folder=f'{root_folder}/{u.models_folder}'
nlu_data_file_path=f'{root_folder}/{u.training_folder}/{u.nlu_data_file}'
nlu_config_file_path=f'{root_folder}/{u.training_folder}/{u.nlu_config_file}'

# if a previous training folder exists, we remove it
previous_model = f'{model_folder}/{u.tag_registration_form}'
if path.exists(previous_model):
    shutil.rmtree(f'{previous_model}', ignore_errors=True)
# nlu training
loop = asyncio.get_event_loop()
loop.run_until_complete(rasa.nlu.train(
    nlu_config=nlu_config_file_path, data=nlu_data_file_path, path=model_folder, fixed_model_name=u.tag_registration_form))[1]
