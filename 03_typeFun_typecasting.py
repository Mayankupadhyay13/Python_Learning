########### Type Casting #########
a = "10"
b = int(a) # typecasting here with fun int(),str(),float()
c = type(b)# type() function returns type of that variable
print(c)

x=10
y=str(x) # int -> str
z = type(y)
print(z)

######### How to take User input #########

input1 = input('Enter num1 here ')
input2 = input('Enter the num2 here ')

print(input1+input2)# if input 1 & 2 here it takes as string and print 12 concatinate the strings 

input3 = int(input('Enter num3 :'))
input4 = int(input('Enter num4 :'))
print(input3+input4)# return 3 here for same input 1 & 2

input5 = float(input('Enter float1 here: '))
input6 = float(input('Enter float2 here: '))
print(input5+input6)# return  1.20 + 2.20 -> 3.4000000000000004
