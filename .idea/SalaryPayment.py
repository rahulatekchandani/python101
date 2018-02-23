#Developer : Rahul Tekchandani
#Usecase : Employee roster is reviewed in function open_roster and each person identified is moved to paid employee

#This program illustrates uses of functions and returning lists between them

def open_roster(unpaid_employees,paid_employee=[]):
    """"""
    while unpaid_employees:
        person = unpaid_employees.pop()
        print(person + ' has been identified in roster')
        paid_employee.append(person)
        print(paid_employee)
    return paid_employee

def print_paid_employee(paidemployee):
    for emp in paidemployee:
        print(emp.title() + ' has been paid')

roster = ['rahul', 'neha', 'natasha']

paidemp = []
paidemp = open_roster(roster)

print_paid_employee(paidemp)