import Utility.Utilities1 as Util

file_status = Util.check_file('/Users/rahul/PycharmProjects/Introductions/text_files/')
print("File status: " + str(file_status))

directory_status = Util.check_directory('/Users/rahul/PycharmProjects/Introductions/text_files/')
print("Directory status: " + str(directory_status))

fformat = Util.check_fileformat('/Users/rahul/PycharmProjects/Introductions/text_files/sample.txt')
print("File format: " + str(fformat))

file_list = Util.readfile_list('/Users/rahul/PycharmProjects/Introductions/text_files/SampleText1.txt')
print(file_list)

