ifilename = '/Users/rahul/PycharmProjects/Introductions/text_files/SampleText1.txt'
ofilename = '/Users/rahul/PycharmProjects/Introductions/text_files/SampleText2.txt'

''' read() functions -  reads the entire file and returns content as single string '''

try:
    with open(ifilename) as file_object :
        contents = file_object.read()
        print(contents.upper())

    if "rahul" in contents :
        print("exists")

    with open(ofilename,'w') as file_object :
        file_object.write(contents.upper())

    file_object.close()

except Exception:
    print ("File not found")

