import numpy as nn

#-----tape object
class Tape():
	def __init__(self, tapestring):
		self.pointer = 0
		self.tapearray = []
		for i in range (0,len(tapestring)):
			if tapestring[i] == "0" or tapestring == "1" or tapestring == char:
				self.tapearray.append(str(tapestring[i]))
			else: 
				self.tapearray.append(str(char))
				print "[Additional characters were found, they were converted to '" + char + "']"
	
	def right():
		print pointer
		if tape[pointer+1]==tape[-0]:
			nn.append(char)
		return 0

	def left():
		return 0

	def write():
		return 0

	def statecommit(tstate):
		return tstate

#-----Obtaining Information
print "\n\033[1m--Zev Pogrebin UTM v0.0 --\033[0m"
tapein = "1010100101" ###Temp
progin = "sub.txt"
diagnostic = True
#tapein = raw_input("Enter tape conents: ") #Obtain tape contents
#progin = raw_input("Enter program path: ") #Obtain program file
#diagnostic = input("Diagnostic prints?: ") #
print "\n\033[1m__________________________\033[0m"
print "Evaluating\033[1m",  tapein, "\033[0m"
print "With instruction set\033[1m", progin, "\033[0m:\n"

#-----Initializing the instruction set
instset = [] # Initialize instruction set
#Column Values instate | input | outstate | output | move 
with open(progin) as prog:
	state = prog.readline().rstrip()
	char = prog.readline().rstrip()
	inst = prog.readline().rstrip()
	while inst:
		instset.append(inst.split(","))
		inst = prog.readline().rstrip()


#logic

if diagnostic==True:
	print state
	print char
	print instset
	print "tape placeholder" ## fix
