
# if( __name__ = "__main__") meaning of this is python 

''' __name__ means that, when i run the code of particluar module form that particular module only gives __main__
shows that this code is run from same module where it written '''

def fun1 ():
    print('run the code')

# mean if any one import this file and we don't want to execute this code to some other file, and want to to run in this particular file only.

if(__name__=="__main__"): # means if run in this file only execute this code 
    fun1()
    print(__name__) # prints __main__ means that the code run from own file, where it written already.
                    # else: prints that file name : exapmle -> rammode from rammode.py

                    # for ex: made a module.py file and import the code written in this as 
                    # (from module import fun1) -> print's that file name. from mathod __name__ .


# Global Keyword :----------
'''makes the local variable at global level to access'''
a = 10
def fun2():
    global a 
    a = 8989
    print(a)
print(a) # 10
fun2()  # 8989
print(a)#8989

# enumerate() function :-------

# enumerate () function adds counter to an iterable and retruns it.
li = [1,245,34,565]                                     # item at index 0 is 1
for index, item in enumerate(li):                       # item at index 1 is 245
    print(f'item at index {index} is {item}')           # item at index 2 is 34
                                                        # item at index 3 is 565

# List Comprehension :-----
# elegent way to create lists based on existing lists. 

# example : lets i want to create list from existing list of squared elements..in fomal way like this
mylist = [1,2,3,4,5]
#squaredlist = []
# for item in mylist:
#     squaredlist.append(item*item)  instead this we cn make it with list comprehension

squaredlist = [i*i for i in mylist]
print(squaredlist)
