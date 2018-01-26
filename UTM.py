import numpy as nn

def right():
	global pointer
	if tape[pointer+1]=tape[]:

	return 0

def left():
	return 0

def write():
	return 0

def statecommit(tstate):
	return tstate



print "\033[1m--Zev Pogrebin UTM v1.0 --\033[0m"
tapein = raw_input("Enter tape conents: ") #Obtain tape contents
#prog = input("Enter program path: ") #Obtain program file

#file = open(prog, "r") 

print "\n\033[1m___________________________\033[0m"
print "Evaluating ",  tapein
#print "With instruction set ", prog

#print read(file) #testing

pointer=0
state=0

instset = nn.empty((2,5)) # Initialize instruction set
# instate | input | output | outstate | move 
tape = nn.empty((len(tapein))) #Initialize other

for i in range (0,len(tapein)):
	tape[i]=tapein[i]
	i += 1

print instset
print tape
