from typing import List, Tuple, Union
########### Advance Python Newly Added Features ############

############# walrus operator: --------- (:=)
''' introduced in python 3.8, 
    allow to assign the values of variables as that variable is part of expression '''
if(n := len([1,2,3,4,5])) > 3 :
    print(f'list is too long {n} elements , expected <= 3 in it..')
# In this example, n is assigned the value of len([1,2,3,4,5]) and then used in the compresion within the if statement.



######### Type Definition in python :---------
''' Basically defining the type of the variable in python as in java.'''
n :int = 10             # type int of the variable

name : str = 'Ramlal'

def sum(a:int , b:int, c:str) -> int: # here -> int: (means it returns the int value.)
    return a+b




############ Advance Type Hints: -----------

'''using python's typing module provides more advanced type hints such as List,Tuple,Dict,Union etc.'''
'''like -> from typing import List, Tuple,Dict, Union '''

# using this we can declare the type of thses Built-in data-Type Hints.

# list of int
num : List[int] = [1,2,3,4,5]

#tuple of int and string
numbers : Tuple[int,str] = (1,"kallu")

# union type for the variable that can hold multiple types
identifier : Union[str,int] = ''  # means it can be int or str
identifier = 1010

'''These annotation help in making the code self-documenting 
and allow devlopers to understand the data structure.'''




########### Match case :--------------
def statusMethod(stateus):
    match stateus:
        case 100:
            return True
        case 200 :
            return False
        case 300 :
            return "string"
        case 400 :
            print("400 print")
        case _:
            return "Defalut print hoga isme.."
print(statusMethod(1000))



######### how to (merge_and_update) the dictionary ########## 
dict1 = {'a' : 1, 'b' : 2}
dict2 = {1 : '100', 2 : '200'}
merged = dict1|dict2
print(merged)
print(dict1.get('a'))