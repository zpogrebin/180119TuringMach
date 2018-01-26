import numpy 

def right():
	return 0
def left():
	return 0
def write():
	return 0

def statecommit(tstate):
	open(prog,r)
	return tstate

print  "\033[1m Zev Pogrebin UTM v1.0 \033[0m"
tape = raw_input("Enter tape conents: ") #Obtain tape contents
prog = raw_input("Enter Program Path: ") #Obtain program file

file = open(prog, "r") 

print   "Evaluating ",  tape, " with instruciton set", prog
print "Tape Initial State:"
print(open(prog, "r"))

pointer=0
state=0

instset np.zeroes(4,2)

print instset
print "Tape Final   State:"
print(open(tape, "r"))
