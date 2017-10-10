ifilename = '/Users/rahul/PycharmProjects/Introductions/text_files/SampleText1.txt'
ofilename = '/Users/rahul/PycharmProjects/Introductions/text_files/SampleText4.txt'

''' readline() functions -  reads the entire file and returns each line as list '''

contents = ['Empty list']

try:
    with open(ifilename) as file_object :
        contents = file_object.readlines()
        print "\n1.0 "
        print(contents)
except FileNotFoundError:
    print "File not found"

print "\n2.0 convert list to string"
ListToString = str(contents[0])
print(ListToString.strip())

ConvToList = ListToString.split(",")
print "\n3.0 split function converts string to list"
print(ConvToList)

print "\n4.0 "
grosssalary = int(ConvToList[2])
netsalary = 0.77 * grosssalary
line = str(ConvToList[0]) + "," + str(ConvToList[1]) + ","+ str(netsalary)