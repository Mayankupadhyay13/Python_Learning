########## Exception Handling in python ##########
try:
    a = int(input("ENter the value : "))
    print(a)

# if we want to through the particular exception exapmle input int ke liye string enter hone prr valueError ata hai
# Work as Throws in java That is can be throgh particular type of error like this
        # Throws in java

except ValueError as ve:
    print(ve)
except Exception as e:
    print(e)

print("After the code completion says Thank you!!")


######## raise keyword :----------
## Raising the custom exception in  python..

a1 = int(input("enter the value 1: "))
a2 = int(input("enter the value 2: "))

if(a2 == 0):
    raise ZeroDivisionError("Yee nai ho paega")
else:
    print(f'division is {a1/a2}')


#### Try with else :-------------

'''After the executing the try block it enters only in else: block
Tells that try block is succesfull then only else execute '''

#### Try with Finally :-------------

'''executes all times finally (), but major use case of it in function 
when i return from any block either its try/except finally executes always '''
def fun():
    try:
        inp = int(input('enter number : '))
        print(inp)
        return ""           # here even if return is there finally always executes 
    except Exception as e:
        print(e)
        return ""
    finally:
        print('chalgya')

fun()

