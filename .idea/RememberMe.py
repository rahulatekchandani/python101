# Author : Rahul Tekchandani
# E-mail : rahul.anil.tekchandani@gmail.com

'''Python code to track username by creating temporary files'''

import json
import os

# Create new JSON file for first time user and write username in it
# For repeat user, call wish_user()
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

# Open the JSON file and read the contents
def wish_user(full_filename):
    mode = 'r'
    with open(full_filename, mode) as file_object:
        name = json.load(file_object)
        print("Thanks for returning back : " + name)

# Starting point of program
greet_user()