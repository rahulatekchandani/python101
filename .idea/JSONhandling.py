'''Python code to dump and load working data in json format for future consumption'''

import json

numbers = [2,3,4,5]

filename = '/Users/rahul/PycharmProjects/Introductions/text_files/numbers.json'
with open(filename, 'w') as file_object:
    json.dump(numbers, file_object)

with open(filename) as file_object:
    lnum = json.load(file_object)

print lnum