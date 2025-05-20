########### Conditionals ##########
# if-else: -----
a = int(input("enter your age: "))

if(a>=18):
    print("Adult")
else:
    print('under age')

# if_elif_else : -------------
b = int(input("Enter the age : "))
if(b>=18):
    print(" Adult ")
elif(b<0):
    print("Dont enter the negative age")
elif(b==0):
    print ("Zero in not age")
else:
    print("Below the age")