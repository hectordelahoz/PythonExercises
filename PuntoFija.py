#-----Import Definitions-----#
from random import randint
#-----Global Variables-------#
#---------DebugClass---------#
class Debug(object):

	def __init__(self):
		self.enabled = False
		self.level = 0
		
	def enable(self):
		self.enabled = True
		self.level = 1
	
	def setLevel(self,level):
		self.level = level
	
	def msg(self,msg,level):
		if((self.enabled == True) and (level <= self.level)):
			print(msg)

#--------DigitClass----------#
class Digit(object):
	global debug
	
	def __init__(self,digit):
		self.digit = digit
		self.state = "X"
		debug.msg("{0}, {1}".format(Digit.__name__,str(self.digit)),2)
	
	def getDigitState(self):
		return self.state
	
	def setDigitState(self,state):
		self.state = state

#--------NumbeClass----------#
class Number(object):	
	
	def __init__(self):
		self.number=[]
		
		for cpu_number_index in range(4):
			try_again = True
			if(cpu_number_index == 0):
				self.number.append(Digit(randint(0,9)))
			else:
				while(try_again == True):
					new_number = randint(0,9)
					for stored_digit_index in range(0,len(self.number)):						
						debug.msg("{0}, new_number = {1},self.number[{2}].digit={3}".format(Digit.__name__,new_number,stored_digit_index,self.number[stored_digit_index].digit),2)
						if(new_number == self.number[stored_digit_index].digit):
							debug.msg("{0}, New number is equal to some stored number".format(Digit.__name__),3)
							break
					else:
						self.number.append(Digit(new_number))
						try_again = False
		else:
			if(debug.enabled == True):
				final_number = ""
				for stored_digit in self.number:
					final_number += str(stored_digit.digit)
				else:
					debug.msg("{0}, I Have a number for you: {1}".format(Number.__name__,final_number),1)
		
	def __repr__(self):
		cpu_number = ""
		for digit in self.number:			
			cpu_number += str(digit.state)
		else:
			return(cpu_number)
					
	
	def checkGuess(self,guess_number):
		for guess_index in range(len(guess_number)):
			for real_index in range(len(self.number)):
				if int(guess_number[guess_index]) == self.number[real_index].digit:
					if guess_index == real_index:
						self.number[real_index].setDigitState("F")						
					else:
						self.number[real_index].setDigitState("P")
					break
	
	def checkWin(self):
		if(self.number[0].state == "F" and self.number[1].state == "F" and\
			 self.number[2].state == "F" and self.number[3].state == "F"):
			return "You Win"
		else:
			return "Try Again"
	
	def newTry(self):
		for digit in self.number:
			digit.setDigitState("X")
		else:
			debug.msg("{0}, The number state was cleared".format(Digit.__name__),2)
			
#----Main Loop------#
debug = Debug()
#debug.enable()
#debug.setLevel(1)
cpu_number = Number()
result =""
while(1):
	player_number = list(input("Insert a four digit number: "))
	cpu_number.checkGuess(player_number)
	print("You Have: {0}".format(repr(cpu_number)))
	result = cpu_number.checkWin()
	print(result)
	if(result == "You Win"):
		break
	else:
		cpu_number.newTry()
else:
        input("Bye!")

