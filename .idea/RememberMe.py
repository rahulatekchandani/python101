'''Python code to track username by creating temporary files'''

import json
import os

def greet_user():
    username = raw_input("What is your username")

    filename = str(username) + '.json'
    full_filename = '/Users/rahul/PycharmProjects/Introductions/text_files/' + filename

    if os.path.exists(full_filename):
        wish_user(full_filename)
    else:
        mode = 'w'

    try:
        with open(full_filename,mode) as file_object:
            json.dump(username,file_object)
            print("This was your first time with us : " + username)
    except Exception:
        pass

def wish_user(full_filename):
    mode = 'r'
    with open(full_filename, mode) as file_object:
        name = json.load(file_object)
        print("Thanks for returning back : " + name)

greet_user()

