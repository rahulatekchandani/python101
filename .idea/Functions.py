# Understanding functions

def print_student(salutation,fname,lname):
    print(salutation + ' ' + fname + ' ' + lname)

def default_print_student(fname,lname,salutation='Mr.'):
    """Non-default parameter preceed default parameters"""
    print(salutation + ' ' + fname + ' ' + lname)

#Positional arguements
print_student('Mr','Rahul','Tekchandani')

#Keyword arguements
print_student(salutation='Mr',fname='Rahul',lname='Tekchandani')
print_student(salutation='Mr',lname='Tekchandani',fname='Rahul')

#Default arguements
default_print_student(fname='Rahul',lname='Tekchandani')
default_print_student(fname='Rahul',lname='Tekchandani',salutation='Dr.')

# Understanding functions with return values

def get_formatted_student(salutation,fname,lname,middle=''):
    if middle:
        fullname = salutation + ' ' + fname + ' ' + middle + ' ' + lname
    else:
        fullname = salutation + ' ' + fname + ' ' + lname
    return fullname.upper()

studentname = get_formatted_student('Mr','Rahul','Tekchandani')
print(studentname)

studentname = get_formatted_student('Mr','Rahul','Tekchandani',middle='Anil')
print(studentname)

def build_addressbk(fname,lname,city=''):
    person={'firstname':fname,'lastname':lname}
    if city:
        person['city'] = city
    return person

person = build_addressbk('neha','valeja','charlotte')
print(person)

person = build_addressbk('natasha','tekchandani','charlotte')
print(person)
