### variables ###

# Data Tpyes in python #
a=10        # integer() variable with having literal value  # identifies a as class<int>
b='mayank'  # string() variabe      # identifies b as class<str>
c=10.09     # float() variable      # identifies c as class<float>
d=True      # boolean() variable    # identifies d as class<bool>
e=None      # none variable         # identifies e ad class<None>


# multiple assignement to variables
x=y=z= 100 # all have same value 
print (x,y,z)

age = 10, 20, 30 # act as tuple here 
print(age)

_age = 10
print(_age) # prints 10 change the age value at run time 

ab,bc,ad = 12,'hello',10.98
print (ab,bc,ad) # assign in single line.


####### operators #######
    # Arthmatic operators
'''Arithmetic operators: +, -, *, **, /, %, // etc '''
x=11
y=2
print(x//y)# print the whole number adjusted to left in number line after divide
print(x**y)# print 121  (11*11) makes power of right to left 

    #Assignment Operators 
'''Assignment operators: =, +=, -= ,/=,%=,//=,**='''
x+=y
x**=y
print(x)# 11+2 prints 13

    #Comparison Operators
'''Comparison operators: ==, >, >=, <, != etc'''
print(x==y)

    #Logical Operators
'''Logical operators: and, or, not'''

ref = 2<3 and 3>2 
print (ref) #true checks for both 
ef = 2<3 or 3==2
print(ef)# true checks for one only
ref = not ref
print (ref)#false

    # identity Operators 
'''(is , is not) used to check identity of two memory locations '''
print (a is b)#false
print(a is not b)# true

    # Membership Operators
'''(in, not in) used to check membership of the values in a sequence like string, list, tuple etc.'''
num =[12,23,21,32,2]
print(12 in num)#true in the num 
print(13 in num)#false not in num

    # Bitwise Operators
'''(&, |, ^, ~, >>, <<)used to perform bitwise operations means bit by bit operations '''