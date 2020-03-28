# Conversational Chatbot

Chatbot for the filling of Web Forms without know the content of the Web Form.. it needs in input the URL of the Web Form which should have the annotation that we are going to explain. The Web form can be open on Chorme browser, Firefox browser or Edge browser and this information can be given together with the URL.

## Annotation of the Web Form code

The annotation maily consists in adding some specific attributes to Web elements. Those attributes allow us to determine the kind of information contained in a Web element. Here the Web elements interesting for us are the ones directly related to the **fields** since our objective is to complete the fields and submit. We are also interested on any **button** present in the Web Form like submit, register, reset buttons since the allow us to perform some useful actions. The attribute that we use for the annotation are the following:
* **bot-title**: it is refered to the _form tag web element_ and precise the title of the Form we are about to fill.
* **bot-tag**: it indicates the the tag of the bot that should handle the input of the user related to that form, it is based on this that the discrimination among bots is done. It should be present on the _form tag web element_. Examples of values for this attribute are *registration_form_tag*, *login_form_tag*, etc, they are only indications.
* **bot-desc**: also refered to the _form tag web element_ and specifies some useful information about the Form. It can be seen as an  explanation or a description of the Form.
* **bot-field**: present to specified that the Web element indicates a field of the form. It value should be _identical_ to the label present on the Form for the corresponding field.
* **field-type**: indicates the value type expected for that field. Sometimes this type could coincide with the input type and in those case this attribute can be ommitted.
* **field-desc**: it i an explanation that we can put on a field toeventually help the user if the label is non clear or it coul be confusing. It can consist in putting appropriate synonyms of the label taking into account the contex of the Web Form and the purpose.
* **field-spelling**: it specifies if a field requires to be spelt out by the user, for instance the personal data of user (first name, phone number, etc) because usually there are many homonyms and it is important to get the exact user's data.
* **bot-button**: its presence specifies that a web element is a button. In a web Form there is for sure at least one button which is the submit/Register button, the button that permits to conclude the filling process. Its value indicates the type of action it carries out (_submit_ for concluding the preocess, _reset_ to reset all the fields and restart)

## The structure of the project

The project is made of **three** main parts. One part completely related to the **Chatbot** with the following _modules_: **launcher, dialogue_manager, choice_bot, formInterface, bots, states, utility, styles, functions, compatible** and the _folders_ **chatito** and **x_form**. Another part consists in the **recording of the dialogues** between the Chatbot and the user, it is constituted by the _modules_ **view, views; writer_interface, writers** and the _folders_ **reports** and **logs**. The last part is for the **simulation of the user** in order to make the dialogue automatic. This part has the modules **user_manager, simulation_constants, interaction_files_keys** and the folder **simulation_data**.

### The Chatbot part

Having only this part, we should have a user physically present for the dialogue to take place. We descibe here its elements.

#### The Laucher (launcher.py)

Since the idea is to have the Conversational Chatbot connected to an **Access Level**. The Access Level is a kind of global controller, if we imagine a scenario in which the Form is inside a Web page and so it is a construct among others, the Access Level is the component of the global structure which receives the message/input of the user and decides which construct should handle it. The Access Level is connected to a Virtual Assistant in order to have the speech enabled, the launcher is the linker between the chatbot and the Access Level. It initializes the Chatbot infrastructure (URL, browser, fields, etc).

#### The Dialogue Manager (dialogue_manager.py)

At the beginning of the interaction it crates the Form bots of the Web page (for each Form present on the Web page there is a bot). During the interaction (When the focus is put on the specific bot), it receives a *bot_tag* and makes a kind of **preprocessing** consisting of getting the corresponding bot from the Bots Manager, eventually training the conversational model for that bot and by preparing the **conversation prologue** (some information about the Form like the title, the list of fields and some statistics about required and optional fields). After the preprocessing phase it starts the **dialogue** alternating from the chatbot and the user until the user writes **stop** to conclude the interaction or the user completes the filling and submission of the Web Form.

#### The Bots Manager (choice_bot.py)

It is in charge of constituting and saving the bots list of the Web page at the beginning of the interaction. Each bot has a _tag_ and a _state_. While creating the bot, it parses the Web Form code to extract the **slots** which are going to constitute the internal representation of the fields present on the Web Form. The slots are taken with all there characteristics which are *name, value, type*, if they are *required* and if they are *spelling fields* (they need to be spelt character by character). The information about the _form Web element_ (*title* and *description*) are stored in a special slot called **requested_slot** (its principal role is to save the next field to be completed).
During the interaction (when the focus is placed on a specfic form) it find the appropriate bot for that form given the corresponding *tag*. During the dialogue, it *interprets* the message of the user that it receives, extracts the *intent*. From the intent of the user input and the state, it gets the *utterance* (response) of the chatbot to be delivered to the user.

#### The Form Bots Interface (formInterface.py)

It defines the actions that the Chatbot can perform on the Web Form, but those actions have to be implemented by the real bots it is only an interface. Each action in our implementation corresponds to an intent and the different possible intents are the following:
* *affirm*: when the user gives a positive answer
* *deny*: when the user gives a negative answer
* *explainLabel*: when the user asks more information about a field
* *fillForm*: when the user ask to continue the filling of the form in case of an interruption
* *fillGenericCamp*: when the user wants to insert the value of some fields.
* *giveAllRemainingLabels*: when the user wants to know the fields that he/she did not yet completed
* *giveRemainingOptionalLabels*: when the user wants to know which the **non required** field that he/she still has to fill
* *giveRemainingRequiredLabels*: when the user wants to know which the **required** field that he/she still has to fill
* *modifyValueGenericCamp*:when the user wants to modify the value of a field. in fact this intent is similar to the fillGenericCamp intent but we distinguished to have more flexibility on the use of natural language during the greneration of training data.
* *repeatAllLabels*: if the the user asks the list of all the fields contained in the Web Form.
* *repeatFormExplanation*: if the user asks some details about the Web Form
* *repeatFormTitle*: if the user needs the title of the Web Form
* *repeatOptionalLabels*: if the user wants the list of the not mandatory fields present in the Web Form
* *repeatRequiredLabels*: if the user wants the list of the required fields of the Web Form
* *repeatValueCamp*: if the user wants to have the value of a given field of the Web Form
* *resetAllCamp*: if the user wants to reset all the fields and restart
* *skipCamp*: if the user wants to skip a field 
* *spelling*: each time the user inserts a value during the spelling mode (close prompt)
* *submitForm*: if the user wants to submit the form
* *verifyPresenceOfLabel*: if the user wants to know if a given field is present in yhe Web Form
* *verifyValueFilledCamps*: when the user wants to have a recap about the fields completed up to that moment

#### The Form Bots (bots.py)

Contains all the Form bots that we can find in a Web Form. Here we only implemented the **Registration Form Bot**. The Registration Form Bot implement some of the functions contained in the Form Bot Interface. While implementing the actions it has to update the **State** of the Dialogue ana at the same time the Web Form. The idea is to modify the Web Form in real time and modifying the fields of the Web Form in real time, it also have to modify the slots to keep the two entities coherent since the reprent the same thing.

#### The State of the Dialogue (state.py)

It represents the snapshot of the dialogue at each instant. The main components of the State are the **messages history**, the **constructs**, the **spalling state** and the **machine parameters**.

##### The messages history

Contains the list of _messages_ (data structure resulting from the interpretation of the user input) during an entire dialogue. A message is made of the *intent*, the *text* and the *entities* contained in the text.

###### The Contructs

Contains the constructs for which we emplement the bots and in our case the construct is the **form**, and inside the form the main element is the **slots**. Each slot represents a field and in addition there is a particular slot to store the next field to be completed.

###### The spelling state

Contains some variables to control the spelling process to know at each moment we know what to do about the spelling. Those variables are the *spelling fields and values saved* in case the the spelling of a field have been interrupted, the *waiting intent* to temporary save the intent in case of the interruption of the spelling and to allow the user to decide whether he/she wants to save the current spelling value or not, the *spelling list* containing the list of spelling fields that the user wants to complete, fields present in a single user input ad the *current spelling value* keeping the partial value of the field in spelling mode. 
There are also some **flags** useful to indicate some transitions like *close prompt enabled* which becomes True when we enter in spelling mode and False when we terminate the spelling of a given field. *spelling interrupted* becomes True when we interrupt a spelling and the user has to decide to save the inserted value or not, as soon as the user makes the choice, it returns to be False. *after spelling* is used to indicate that we just finished to spell the value of a field and so we have to insert that value in the Web Form, as soon as the value is inserted in the Web Form and the slots are updated, it returns to be False.

###### The machine parameters

Contains some parameters important for the dynamic of the dialogue (eventually useful to represent the dialogue flow as a state machine). The main parameters are boolean and they are the following:
* *filling started*: to indicate that the we already started the filling process (the prologue of the dialogue have been done)
* *submit done*: we have submit the form and eventually the user should decide if he/she wants to start a new dialogue or he/she prefers to end the session
* *reset alarm enabled*: to indicate that the user want to reset all the fields and he/she has to confirm the intention to make sure that it was no done by mistake
* *submit alarm enabled*: to indicate that the user want to submit the Web Form and he/she has to confirm the intention to make sure that it was no done by mistake
* *all required filled*: to indicate that all the required fields of the Web Form have been filled, and so at any moment the user can ask to submit the Web Form
* *warning present*: indicates that the message we inserted was not understood by the bot and so we have to precise the action we need to do

#### Auxiliary chatbot python files

* **utility.py**: CONSTANT file containing useful constants for the development of the bot like *file names*, *dictionary keys*, *names*, *value types constants*
* **styles.py**: API file containing functions to change the style of the sentences we return to the user
* **functions.py**: API file containing functions used by the state, the bots and other files. It is a kind of helper for everyone and the functions are independent
* **compatibility.py**: API file containing only the function used for the validation of the input types (date, time, email, password, etc)

#### Chatito folder

Contains the chatito files to generate the training data. In fact **chatito** is the instrument we use to generate the training data, it is open-source and free. Each intent has an associated file and moreover we have differents files for the *alias*(specifying similar expressions that can be used in place of a given expression), the *slot values* (samples of values for a given slot value. eg. slot: name, samples:bob, alice) and the *slots names* (synonyms for a give field name. eg. slot: name, samples: first name, last name).


### The Dialogue recording part

It is mainly constituted by the view to format the messages denpending on whether they come from the user or form the Chatbot in order to make clearer what is going on, and the writer to save what happend during the interaction in term of dialogue (logs) or in term of messages exchanged during different dialogues constituting a **session** (reports). They are activated through parameters present in the *utility.py* file (write logs, write reports).

#### The view (view.py and views.py)

* **view.py**: view interface containing the functions to be implemented by the ChatbotView and the UserView
* **views.py**: contains the implementation of the functions contained in the View Class when necessary and eventually other fuctions specific to each View type (ChatbotView, UserView)

#### The writer (writer_interface.py and writers.py)

* **writer_interface.py**: writer interface containing some functions to be used by the LogWriter and the ReportWriter
* **writers**: each writer implements the functions necessary to generate the text file.


### The Simulation part

Useful to automate the dialogue, it is used both as a Tester for the developed functions and as an instrument to assess the performance of our software prototype. It is based on data base containing user input and templates for different situation. The principles is thet for each given situation, it picks a random value among the set of values available for that situation and returns.
To know in which situation we are to know which value file use, we nodeled the dialogue as a **finite state machine** where each state is defined by a set of parameters which are the following: *close_prompt_enabled*, *spelling_interrupted*, *warning_present*, *all_required_filled*, *submit_alarm_enabled*, *reset_alarm_enabled*, *submit_done*, *possible_next_action*.

#### The User Manager (user_manager.py)

Simulates a user by providing answers to the request of the Chatbot and by asking specific things during the dialogue. It implements the necessary APIs to constitute a coherent sentence give a specific states.
There are two types of data which are the **filling data** and the **interaction data**. In addition to those two types of data we use the **choices list** (checkbox, radio, dropdown lists) contained in the Web Form to contitute the database for generating the sentences of the user.
For *date, password, time* kind of data, the User Manager user contant data present in some CONSTANTS files and randomize them inorder to test as nuch as possible the Conversational Chatbot.
* The *interaction data* are json files containing templates of sentences for the actions provided by the Conversational Chatbot. For each *complex* action there is a file.
* The *filling data* contains the values to fill the slots contained in the templates and they are organized in category(corresponding to *slot names*). The different files are atoms and so they are going to be combined to form the final values to be inserted in the slots.
The simulation is controlled by the parameter *simulation_enabled* in utility.py and for the simulation to happen, that variable should be True.

#### Database components

* **interaction_file_keys.py**: CONSTANT file containing the keys used in the json interaction files.
* **simulation_constants.py**: CONSTANT file containing the simulation files names and the keys of the data structures used by the user manager.
* **simulation data folder**: folder where the simulation files have been inserted. it counts two sub-folders, *filling* folder for the files related to the filling data and *interaction* for the files related to the interaction data.
