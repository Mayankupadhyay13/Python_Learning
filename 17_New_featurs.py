
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

li = [1,245,34,565]
for index, item in enumerate(li):
    print(f'item at index {index} is {item}')