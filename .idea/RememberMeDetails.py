# Author : Rahul Tekchandani
# E-mail : rahul.anil.tekchandani@gmail.com

'''Python code to track user details by maintaining files, creates new file for new user
and retrieves information for returning user'''

import json
import os
from datetime import datetime

# Create new JSON file for first time user and write username in it
# Capture details and return list
def first_time_user(username):

    fname = raw_input("What is your first name")
    lname = raw_input("What is your last name")
    ssnno = raw_input("What is your SSN")
    addr = raw_input("What is your address")
    ts = str(str(datetime.now()).split(" ")[0])

    # concatenate input into string and split to list
    temp = username + "|" + fname + "|" + lname + "|" + ssnno + "|" + addr + "|" + ts
    print temp
    templist = temp.split("|")
    print templist

    # return list
    return templist


# Read details for returning user
# Open the JSON file and read the contents
def wish_user(full_filename):
    mode = 'r'
    with open(full_filename, mode) as file_object:
        content = json.load(file_object)
        print("Thanks for returning back : " + content[1] + " " + content[2])


def greet_user():
    # take inputs from user
    username = raw_input("What is your username")

    # check for file in path
    filename = str(username) + '.json'
    full_filename = '/Users/rahul/PycharmProjects/Introductions/text_files/' + filename

    if os.path.exists(full_filename):
        wish_user(full_filename)

    else:
        print("This was your first time with us : " + username)
        templist = first_time_user(username)
        mode = 'w'

    try:
        with open(full_filename,mode) as file_object:
            json.dump(templist,file_object)
    except Exception:
        pass


# Starting point of program
greet_user()