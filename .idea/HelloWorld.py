

eow = "----------------------"
print eow
# Simple print
print "Hello World"

# Print with string
name = "rahul"
print "Hi " + name + ", how are you?"

# Print with integer
age = 29
print "You are " + str(age) + " years old"

print eow
# Simple string functions
print name.upper()
print name.lstrip()

print eow
# Working with lists
cars = ['honda','ford',' toyota','mazda ']
print cars
print cars[0].title(),cars[2].title().strip()
print cars[-1].upper()

print cars

cars.append("kia") # add to end of list
print cars

cars.insert(1,"nissan") # add to certain point in list
print cars

del cars[1] # remove element using index no
print cars

print eow
dishes = {'eggs': 2, 'sausage': 1, 'bacon': 1, 'spam': 500}
dkeys = dishes.keys()
dvalues = dishes.values()
print dkeys
print dvalues