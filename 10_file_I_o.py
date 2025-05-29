############# File_i/o ###############

''' The RAM is volatile memory, and all its content are lost at once the program terminates 
    in order to persist the data forever, we use files.

    A file is stored in storage device. A  python program can talk to the file by reading and writing the contet from it..
'''

# read mode
file = open("files.txt")  # this open() function here takes two parameter file_name and mode(read or write), by defualt read is there 
data = file.read() #, readlines()returns a list, readline()
print(data)


line = file.readline()
while(line != ""):
    print(line)             # read lines while not empty("") .
    line = file.readline()
file.close()

# append mode n file add string at end of the file.

st = "mamamma"
f = open("files.txt",'a')
print(bool(f.write(st)))
f.close()

# with statement :____________________ opens the file in read mode using 'with' which automaticaly closes the file.
with open("files.txt") as f:
    print(f.read())

# question :-----
#with open('poeam.txt') as file:
with open('poeam.txt') as f:
    file = f.read()
    if('twinkle' in file):
        print("The word twinkle is present")
    else:
        print("The word twinkle is not present")