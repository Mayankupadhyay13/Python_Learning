########### List in python #############
import inspect
''' it's a simple container that holds any type of data_type values in it '''

a = ['apple',10,'mango',20,'oranges',10.00,True]
print(a)

a[0] = 'Apple'    # here Unlike String that are not mutable , but list can 
print(a)          # changes apple to Apple

# List methods:----
'''
1. List.sort():                     sort the list
2. List.reverse():                  return reverse of the given list
3. List.append():                   add at end
4. List.insert(index, element):     add at specific index in list 
5. List.pop():                      pop out the element at particulr index and return that
6. List.remove():                   remove the value from list but, not return 
'''
a.append(100)
#a.sort()

print(a.remove(20))
print(a)


############ Tuples in python #############
'''Just as list but not mutable, It's another collection_data_type in python 
stores multiple data_type_values in it and not mmutable means immutable'''

'''NOTE IMP : 
                [Blue cube] means:  
                purple cube means: 
                wrinch(key) means: 
'''

tp = ("changu",10,"mangu",20,"tulli",30,"bulli",40,True,10.09)
print(tp)
print(type(tp))                 # return -> <class 'tuple'>
print(tp.count('mangu'))        # returns 1 becz occurs only once in it
print(tp.index(20))
print(tp.__contains__(10))

    # tuple operations: --------- 

# 1. concationation ++++
tp1 = (1,3,2)
tp2 = (2,6,7)
print(tp1+tp2)

# 2. repetition +++++
print(tp1 * 2)               # repete the tuple
 
# 3. membership ++++++
print(2 in tp1)             #true
print(2000 in tp1)          # false
# 4. unpacking +++++
a,b,c = tp1
print(a,b,c)