#-----Instruction search based on criteria state and inp
def instsearch(st, iv):
	for i in range(0, len(instset)):
		if int(instset[i][0][1])==st and instset[i][1]==iv: #####PROBLEM
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
		if direction == "R":
			if self.pointer == len(self.tapearray)-1:
				self.tapearray.append(initchar)
			self.pointer = self.pointer + 1
		if direction == "L":
			if self.pointer == 0:
				self.tapearray.insert(0, initchar)
		return self.pointer

#-----Obtaining Information
print "\n\033[1m---Zev Pogrebin UTM v0.0---\033[0m"
headline = "\n\033[1m___________________________\033[0m"
tapein = raw_input("Enter tape conents: ") #Obtain tape contents
progin = raw_input("Enter program path: ") #Obtain program file
if "y" in raw_input("Diagnostic prints?: "):
	diagnostic=True
else: 
	diagnostic=False
print headline
print "Evaluating\033[1m",  tapein, "\033[0m"
print "With instruction set\033[1m", progin, "\033[0m:"


#-----Initializing the instruction set and tape
instset = [] # Initialize instruction set
#Column Values instate | input | outstate | output | move 
with open(progin) as prog:
	state = int(prog.readline().rstrip()[1])
	char = prog.readline().rstrip()
	initchar = prog.readline().rstrip()
	inst = prog.readline().rstrip()
	while inst:
		instset.append(inst.split(","))
		inst = prog.readline().rstrip() #load program into instset
tape = Tape(tapein) #init tape

#-----diag output
if diagnostic==True:
	print "Initial state:", state
	print "Set break chr:", char
	print "tape contents:", initchar
	print "initd pointer:", tape.pointer
	print "instructions :"
	for n in instset:
		print n
	print headline

#-----Logic
while True:
	instline = instsearch(state, tape.gethead())
	if instline == -1:
		break
	tape.writehead(instset[instline][3])
	tape.pointer = tape.move(instset[instline][4])
	state = int(instset[instline][2][1])
	if diagnostic==True:
		print instset[instline]
		print tape.pointer,
		print state, "".join(tape.tapearray)
#-----Ending
print headline
print "Initd tape:", tapein
print "Final tape:", "".join(tape.tapearray)
