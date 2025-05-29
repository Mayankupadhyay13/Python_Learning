'''solving  the problems by creating objects is one of the most popular concept in programming. 
this is called object-oriented programming.
    This concept focuses on using reusable code called (DRY principles).
'''
############# classes ############:----------

'''A blue_print for creating the objects'''
class Employee:
    language = 'py'
    age = 21
    salary = 10000


########## objects ########### :--------------
harry = Employee()
harry.name = 'harry'
print(harry.name,harry.language,harry.age,f'thank you {harry.name}')

ramlal = Employee()
ramlal.name = 'Ramlal'
# instance attribute: \\\\
ramlal.salary = 10000000            # instance attribute more preference. checks this first if not then go to class level
print(ramlal.name,ramlal.language,ramlal.age,ramlal.salary,f"thank u {ramlal.name}")

# Note : here (name) is (object/instance) arttibute and (language & age) are (class attribute).
#Note : Instance attribute, take preference over the class attribute during assignment and retrival. 


########## self parameter : ##########\\\\\
'''self refers to the attribute of class. Automatically passed with a function call from object.  
Note : IMP: 
            As in java, we can make methods without any arguments inside class but, 
            in python we can't, its complsury to have at least one argument which is (self). in the particular method becaz

            as above 
            harry = Employee()
            harry.anyMethod() coverted internaly like -> Employee.anyMethod(harry) means method have one argument cause an error
            that's why methos should have at least one arg, as self(which refers to instances of that class only)  

            if any cases you want use -> @staticmethod(), or @classmethod() in_side the class

            (Java's this -> python's self to refer current object )
            In Python, you cannot define an instance method without at least one parameter usually named (self)because 
            Python uses explicit self to refer to the instance. This is different from Java, where the this reference is implicit.
        exapmle:---
'''
# class Example:
#     id = 1
#     S_No = 1010
#     def anyMethod():                          shows an error
#         print('class method') 
# example = Example()
# example.anyMethod()

class Example:
    id = 1
    S_No = 1010
    def anyMethod(self):
        print('Exapmle class method..')              # prints class method..
        print(self.id,self.S_No)

    @staticmethod
    def greetings():
        print("RAM RAM JII")

example = Example()
example.anyMethod()
example.greetings()

######### Constructor the __init()__ ##########

# The (DUNDER) methods starting from __init_, __annotation_, etc.

class Example2:
    id = 1
    S_No = 1010

    def __init__(self,name,id,sno):
        print('Object initializing ....')
        self.name = name
        self.S_No = sno
        self.id = id

    def anyMethod(self):
        print('Exapmle2 class method..')              # prints class method..
        print(self.name,self.id,self.S_No)

    @staticmethod
    def greetings():
        print("Good Morning")

example = Example2('Ramulal',170,2020)
example.anyMethod()
example.greetings()