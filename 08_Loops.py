############ Loops ###########

for i in range(1,6):
    print(i)

'''Types of loops in python 
-> For loop()
-> While loop()
'''
i = 0
while(i<6):
    print(i)
    i=i+1

# While loop on List ----------
list = [1,2,20,'harry','ramPAL','beerPAL']
i=0
while(i<len(list)):
    print(list[i])  
    i+=1

# For loop -----------
'''can iterate through a sequence like on list, tuple, str'''

a = [1,2,3,4,5,6,7,8,9]
i=0
for i in range(0,len(a),3): # range fun has three attributes here (start, stop, step_size)
    print(a[i])# prints (1,4,7)
    i+=1


# for loop with else: -------------

l=[1,5,9]
for item in l:
    print(item)

else:
    print('DOne Loop exits!')


# Break keyword --------
a = [3,4,10,90,7,86,67,23,12,32]
i=0
for i in range(0,len(a),3):  # return 3 90 67 32 here
    print(a[i])# 
    i+=1
    if(i==7):               # prints 3,90,67 not 32 here
        break
# COntinue keyword -------

'''continue -> is used to stop the current iteration of the loop and continue with the next one. 
                It instructs the Program to “skip this iteration.
'''
a = [1,2,3,4,5,6,7,8,9]
i=0
for i in range(0,len(a),3): # range fun has three attributes here (start, stop, step_size)
    print(a[i])# prints (1,4,7)
    i+=1
    if(i==5):
        continue
# Pass keyword -----------

'''pass is a null statement in python. It instructs to “do nothing”. '''
li = [2,3,1,4]
for item in range(len(li)):
    pass
print('Out side of loop bcz of pass keyword')