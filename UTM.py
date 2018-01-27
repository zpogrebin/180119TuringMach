import numpy as nn
cont=True
#-----Instruction search based on criteria state and inp
def instsearch(st, iv):
	for i in range(0, len(instset)):
		templine = instset[i]
		ststr = templine[0]
		if int(ststr[1])==st and templine[1]==iv:
			return i
	return -1

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

	def gethead(self):
		return self.tapearray[self.pointer]

	def writehead(self, digit):
		if digit == "0" or digit == "1" or digit == char:
			self.tapearray[self.pointer] = digit
		else:
			"[A '"+ digit + "' was in the instruction write. It was converted to '" + char + "']"
			self.tapearray[self.pointer] = char
	
	def move(self, direction):
		print self.pointer
		if direction == "R":
			if self.pointer == len(self.tapearray)-1:
				self.tapearray.append(char)
			self.pointer = self.pointer + 1
		if direction == "L":
			if self.pointer == 0:
				self.tapearray.insert(0, char)
			else:
				self.pointer = self.pointer - 1
		print self.pointer
		return self.pointer

#-----Obtaining Information
print "\n\033[1m--Zev Pogrebin UTM v0.0 --\033[0m"
progin = "sub.txt"
diagnostic = False
tapein = raw_input("Enter tape conents: ") #Obtain tape contents
#progin = raw_input("Enter program path: ") #Obtain program file
#diagnostic = input("Diagnostic prints?: ") #Diagnostic information
print "\n\033[1m__________________________\033[0m"
print "Evaluating\033[1m",  tapein, "\033[0m"
print "With instruction set\033[1m", progin, "\033[0m:"


#-----Initializing the instruction set and tape
instset = [] # Initialize instruction set
#Column Values instate | input | outstate | output | move 
with open(progin) as prog:
	state = int(prog.readline().rstrip()[1])
	char = prog.readline().rstrip()
	inst = prog.readline().rstrip()
	while inst:
		instset.append(inst.split(","))
		inst = prog.readline().rstrip()
tape = Tape(tapein)

#-----Logic
while cont==True:
	instline = instsearch(state, tape.gethead())
	if instline == -1:
		break
	tape.writehead(instset[instline][3])
	print instset[instline]
	tape.pointer = tape.move(instset[instline][4])
	print tape.pointer,
	state = int(instset[instline][2][1])
	print state, "".join(tape.tapearray)

#-----Ending
print "Initd tape:", tapein
print "Final tape:", "".join(tape.tapearray)
