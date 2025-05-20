############### Dictionary's and Sets ################

'''Dictionary is same as HashMap in java Stores key_value pairs in it.
    str,int,float can be key/values  '''
empty_dic = {}
print(type(empty_dic)) #<class 'dict'>
dic = {
    'Harry':90,
    'ramu':67,
    'kamu':89,
    'jhaplu':78
}; print(dic,type(dic))

'''Properties of Dictionary ----------
    -> unorderd 
    -> mutable
    -> indexed
    -> can't conatin duplicate key's

'''
print(dic.items())# return dict key_value pairs in tuple form
print(dic.keys) # prints object refference 
print(dic.keys()) # prints keys

dic.update({'kamu':99, 'champu':87})
print(dic) # mutability achived here

print(dic.get('champu11')) #returns value of the key if exist else return None
#print(dic['champu11']) # return error 


########### Sets #########

'''collection of with no duplicacy , unordered elements
PROPERTIES of Sets -------
1. Sets are unordered => Element’s order doesn’t matter
2. Sets are unindexed => Cannot access elements by index
3. There is no way to change items in sets.
4. Sets cannot contain duplicate values.
'''


#Empty Set ------
s = set()           # dont create like this (s = {} it's dictionary)
print(type(s))     #<class 'set'>

_set = {2,2,1,1}                    # no duplicate 
_s_et = {2, 20.0, 'harry',200}      # allowed
#print(type(_set))
print (_set)
print (_s_et)

## Set methods() ------------
# 1. add()
_s_et.add(1020)
_s_et.discard(10)     #don't raise error while member or not                                    both work same
#_s_et.remove(1020)      #KeyError: 1020 if the set don't have that mamber it raise (KeyError)
print(_s_et,type(_s_et))

# 2. clear(), len(), remove(), discard(),
# union() -> (combine the both sets), intersection() -> (comman values in both sets)
#difference(), issubset(), issuperset(),

set1 = {1,2,4,6,7}
set2 = {23,1,3,4}
set3 = {1,2}
set4 = {100, 200 ,300}
print(set1.difference(set2)) #returns this in set1 {2, 6, 7} (eleminate the comman from set1)

print(set1.union(set2))         #{1, 2, 3, 4, 6, 7, 23} add both sets union

print(set1.intersection(set2))  #return {1, 4}

print(set3.issubset(set1))      # return true

print(set1.issuperset(set3))    # return true

print(set1.isdisjoint(set4))    # return true dont have similar values (disjoint) 

#Note: -------
print(20==20.0)                 #return true
sett = { 20,20.0,'20'} # cal the len() it return 2here but its 3 why?
print(len(sett))        # return 2 , bcz python ckecks for values 

# IMp: 
'''Can you change the values inside a list which is contained in set's ?????????
Ans : No, you can not have list as element in set bcz , set's elements in python canbe immutable and hashable.
while list's are mutable and not hashable.
'''

