#################### Strings ###################
'''Strings are sequence of characters. we can write string these three ways'''
a = 'string'
b = "String"
c = '''String'''

input1 = input('Enter the input here:') # to use varibale name in string make it like this using f in start
print(f'good morning ,{input1}')

### String slicing: --------- 
'''A string in pyton can be sliced for getting part of that string'''
name = 'Pythontutorial'
sliced_string = name[0:4] # prints pyth
character1 = name[2]    #note : indexing starts from 0, but if start with last satrt with -1 ref to last value of the index

print(sliced_string)
print(character1) # print t


# Negative slicing; -----------
char2 = name[-1]# print l
print(char2)

print(name[-4:-1])#ria
print(name[:-1])#Pythontutoria (empty means start from last in negative basis)
print(name[-6:])#torial (empty means index.length )


# slicing with skip value: -------

name2 = 'abcdefghijkL'
print(name2[1:-1:2])# prints bdfhj skip value by 2 here



###### String Functions ####
'''used to do smomething or get something on string'''
__name__ = 'mayank Upadhyay'
#print(__name__.__len__) don't konw about this

'''  1. len() method '''
print(len(__name__))# return int 14
'''  2. endswith('') method '''
print(__name__.endswith('dhyay'))# true 
'''  3. startswith('') method '''
print(__name__.startswith('Mayan'))# true // for mayan return false
'''  4. captilize () method '''
print(__name__.capitalize()) # mayankUpadhyay for this it make this Mayankupadhyay
print(__name__.title()) # mayankUpadhyay for this it make this Mayank Upadhyay first char of each word
print(__name__.find('Upad'))# 7 count space also
print(__name__.replace('Upadhyay', 'sharma')) 



###### Escape Sequence characters ######

''' \n, \t, \', \\ '''
a = 'ramu is a good boy\nbut \tnot a bad \'boy\''
print(a)
