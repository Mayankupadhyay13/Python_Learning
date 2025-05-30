########### Decorator methods in python #################


# class method :---------
# @classmethod decorators :----
'''A class methods is a method which is bound to the class and not the object of the class '''      
class Employee:
    a = 1
    @classmethod                # decorator used create the class method
    def show(cls):              # shows class attribute here which is 1 bcz, of @classmethod (decorator), else show 45
        print(f'class attribute of a is {cls.a}')
e = Employee()
e.a = 45
e.show()

# @property decorators:----------
# @.setter decorator

class Employeee:
    a =10                   
    @property          # GETTER      # property decorator -> This makes name act like an attribute, but behind the scenes it calls a method.
    def name(self):
        return f"{self.fname} {self.lname}"
    
    @name.setter        # setter    # decorator setter This allows you to assign to emp.name like an attribute.
                            #Behind the scenes, it splits the input string and sets two instance variables: self.fname and self.lname.
    def name(self, value):
        self.fname = value.split(" ")[0]
        self.lname = value.split(" ")[1]

emp = Employeee()
emp.name = "Kallu Bhai"
print(emp.name)
''' Yes, @property and @<property>.setter work together as a coordinated pair 
for the same attribute name—just like getter and setter methods work together in Java.'''

# Encaplulation :---

''' encapsulate the multiple working components as In this class hass.. '''

# Abstraction:----
''' hidding the implimentation from the user by providing the functionality..'''

# Operator Overloading in python :------

''' Operators in python can be overloaded using dunder methods. __add__(),__str__(),etc.
These methods are called when a given operator is used on the objects. 
Operators can be overloaded using the following methods:---

    p1+p2 ->   p1.__add__(p2)
    p1-p2 ->   p1.__sub__(p2)
    p1*p2 ->   p1.__mul__(p2)
    p1/p1 ->   p1.__truediv__(p2)
    p1//p2 ->  p1.__floordiv__(p2)

    __add__(self, other): For the + operator.
    __sub__(self, other): For the - operator.
    __mul__(self, other): For the * operator.
    __div__(self, other): For the / operator.
    __eq__(self, other): For the == operator.
    __lt__(self, other): For the < operator.
    __getitem__(self, key): For the [] operator (indexing).
    
    __str__() -> used to set what should be displayed upon calling or when is convert object to str().
    __len__() -> used to set what upon calculating the length on object.
'''
class NUmbber:
    def __init__(self,n):       # __add__ is a magic method that tells Python how to handle the (+) operator for your objects.
        self.n = n              # When you write n + m, Python internally calls:  n.__add__(m)

    def __add__(self,other):    #Inside that method: -> self refers to the object on the left (n)
        return self.n + other.n                  #  -> other refers to the object on the right (m) 
    
                                # So it returns n.n + m.n, which is 10 + 20
n = NUmbber(10)
m = NUmbber(20)
print(n+m)   


               #shows error bcz, here we add the two different objects of class NUmbber()
#                            ''' In python Everithing is class here it says what + ? 
#                         so, here in python we using add operator overloading '''  