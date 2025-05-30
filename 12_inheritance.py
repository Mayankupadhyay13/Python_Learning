############ Inheritance #########
'''way of creating a new class from existing class '''

''' 
Note :
    We can use the method and attribute of employee in programmer object. 
    Also, we can overwrite or add new attributes and methods in programmer
'''
class Employee:
    def show(self):
        print("emp class!!")
class Programmer(Employee):
    def doSomeWork(self):
        print('programmer class!!')

a = Programmer()
print(a.show(),a.doSomeWork())

class Abc():
    name = "ramlal"

''' types of inhertance 
1. single inheritance           -> when child class inherits only one single parent class.
2. Multiple inheritance         -> child class can inherite multiple classes (company -> programmer and Abc)
3. Multilevel inheritance       -> company -> programmer->employee

'''
# Multiple and multilevel inheritance
class Company(Programmer,Abc):
    def anywork(self):
        print("printing from company!!")
b= Company()
b.anywork(),b.doSomeWork(),b.show()
print(b.name)

# Super keyword ;----

class superKeyword(Company):
    def __init__(self):
        super().anywork()
        print('Super works ')
c = superKeyword()