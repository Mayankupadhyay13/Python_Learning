n = int(input("ENter the number : "))
for i in range(1,n+1):
    print(" "*(n-i), end="")
    print("*"*(2*i-1),end="") #     here end="" is stops to enter the new line by the print()method by default...
    print("")
# it will print this pyramid
''' 
    *
   ***
  *****
 *******
*********
'''
############# function definition ###########
def fun1():
    print("function called ..")
fun1()

# types of function -> 
    # build-in function, user-defined function

# function with aruguments:-----------
def f2 (name,age):
    print(f"Good Day, {name}, age :{age}")
    print("Good DAy " + name,age)
    return "Thank you"
a = f2("mayank",24)
print(a)

# default arguments in function
# if the value is not assign then holds own value within function

def f3(name,age="18+"):
    print("Hello "+ name,age)
f3("Babu_Ram")
f3("Lalu_Ram",24)

# factorial Question using recursion--------
def factroial(n):
    if(n==1 or n==0):
        return 1
    return n * factroial(n-1)
fac = factroial(int(input("Enter number : ")))
print(fac)

#question :
#WAP to find greatest of three numbers______
def find(a,b,c):
    if(a > b and a > c):
        return a
    elif(b>a and b>c):
        return b
    else:
        return c
findd = find(10,21,22)
print(findd)

# Question print the sum of n natural numbers using recurssion____

def recursiveFindSum(n):
    if(n==1):
        return 1
    return n + (recursiveFindSum(n-1))
   
n= int(input("Enter the number : "))
print(recursiveFindSum(n))

# Question print pattern *** ** *

def pattern(n):
    if(n==0):
        return 
    print("*" * n)
    return pattern(n-1)
pattern(int(input("Enter the Patter number : ")))