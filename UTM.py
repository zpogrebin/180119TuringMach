import numpy as nn

#-----Tape object
class Tape():
	def __init__(self, tapestring):
		self.pointer = 0
		self.tapearray = []
		for i in range (0,len(tapestring)):
			if tapestring[i] == "0" or tapestring[i] == "1" or tapestring[i] == char:
				self.tapearray.append(str(tapestring[i]))
			else: 
				self.tapearray.append(str(char))
				print "[A '"+ tapestring[i] + "' character was found. It was converted to '" + char + "']"

	def gethead():
		return self.tapearray[self.pointer]

	def write():
		return 0
	
	def move(direction):
		if direction == "R":
			if pointer == len:
				tapearray.append(char)


#-----Obtaining Information
print "\n\033[1m--Zev Pogrebin UTM v0.0 --\033[0m"
tapein = "1010100101" ###Temp
progin = "sub.txt"
diagnostic = True
#tapein = raw_input("Enter tape conents: ") #Obtain tape contents
#progin = raw_input("Enter program path: ") #Obtain program file
#diagnostic = input("Diagnostic prints?: ") #Diagnostic information
print "\n\033[1m__________________________\033[0m"
print "Evaluating\033[1m",  tapein, "\033[0m"
print "With instruction set\033[1m", progin, "\033[0m:"

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

tape = Tape(tapein)
#logic
if diagnostic==True:
	print "\033[1m__________________________\nDiagnostic Information\033[0m"
	print state
	print char
	print instset
	print tape.pointer
