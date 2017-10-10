def count_word(input_path):
    try:
        with open(input_path) as file_object:
            contents = file_object.read()
    except Exception:
        pass
    else:
        filelist = contents.split()
        filename = input_path.split("/")
        print("\nInput file : " + str(filename[-1]) + "\nFile size " + str(len(filelist)))

def count_the(input_path):
    try:
        with open(input_path) as file_object:
            contents = file_object.read()
    except Exception:
        print "File Not Found"

    else:
        the_counter = 0
        filelist = contents.split()
        for word in filelist:
            if 'the' in str(word):
                the_counter = the_counter + 1
        filename = input_path.split("/")
        print("\nInput file : " + str(filename[-1]) + "\n'The' counter " + str(the_counter))

input_filename = ['WikipediaIndia.txt','Wikipedia.txt']
for file in input_filename:
    filepath = '/Users/rahul/PycharmProjects/Introductions/text_files/' + str(file)
    count_word(filepath)