from random import randint
import os
#------------Global Variables-------------#
global_game_mode_selected = 0
global_number_of_battleships = 2
global_number_of_attacks = 5

#-----------------Classes-----------------#
class Point(object):
    def __init__(self,x,y,value):
      self.x = x
      self.y = y
      self.value = value

    def setValue(self,value):
      self.value = value    

class Ship(Point):
    
  def __init__(self,x,y,size):
    self.x = x
    self.y = y
    self.size = size
    self.state = "alive"

  def verifyAttack(self,x,y):
    if(self.x == x and self.y == y):
      self.state = "sunk"
      return True
    else:
      return False

class Board (object):

    global global_game_mode_selected
    global global_number_of_battleships
    
    def __init__(self):
      self.point = []
      self.ships = []
      self.size = 3*1#global_number_of_battleships

      #Creating player attack board
      for row in range(self.size):
        self.point.append([])
          
      for row in range(self.size):
        for col in range(self.size):
          self.point[row].append(Point(row,col,"O"))

    def addShip(self):
      self.ships.append(Ship(randint(0,self.size-1),randint(0,self.size-1),1))

    def addAttack(self,row,col):
      if (self.point[row][col].value == "x" or self.point[row][col].value == "*"):
        return -1
      for ship in self.ships:
        if(ship.verifyAttack(row,col) == True):
          self.point[row][col].setValue("*")
          return 0
      else:
        self.point[row][col].setValue("x")
        return 1      

    def getNumberOfShips(self):
      return len(self.ships)

    def printShipsLocation(self):
      for ship in self.ships:
        print("({0},{1})".format(ship.x,ship.y))
        
    def __repr__(self):
      string = ""
      for row in self.point:
        for col in row:
          string += col.value      
        string += "\n"
      else:
        return string

#--------------Initial Menu---------------#
  
def printInitialMenu():
  global global_game_mode_selected
  print("--Welcome to Battleship--\n\n")
  game_mode_menu =["Please select your game mode: \n",\
                   "1- Single player several Battelships.\n",\
                   "2- Single player several Battelships (different sizes).\n",\
                   "3- Two players several Battelships (different sizes).\n",\
                   "4- Help\n"]

  welcome_menu = " ".join(game_mode_menu)
    
  while (global_game_mode_selected <1 or global_game_mode_selected>4):
    global_game_mode_selected = int(input(welcome_menu))
    if(global_game_mode_selected <1 or global_game_mode_selected>4):
      input("Please select a valid option (from 1 to 4), Press a key and try again!\n")
    elif(global_game_mode_selected != 1):
      input("This game mode is under development. Press a key and select another option\n")
      global_game_mode_selected = 0
    os.system("cls")
  else:
    print ("You have selected the option: %s"%game_mode_menu[global_game_mode_selected])
    print ("Let's play Battleship!")
    input ("Press a key to continue!")
    os.system("cls")
    
#--------------Main Loop----------------#
printInitialMenu()

#creating player1 attack board
player1_board = Board()
#adding ships to the CPU board
for ship in range(global_number_of_battleships):
  player1_board.addShip()
  
print("\nCPU:you must sink {0} ship(s) in a {1}X{2} board "\
      .format(player1_board.getNumberOfShips(),\
              player1_board.size,\
              player1_board.size))

# printing the attack board 
print(repr(player1_board))

#Starting with the player guesses
while(global_number_of_attacks > 0):
    selected_row = int(input("\nCPU:Please, enter the number of the row: "))
    selected_column = int(input("\nCPU:Please, enter the number of the column: "))    
    if((selected_column >= 0 and selected_column <= player1_board.size) and \
       (selected_row >= 0 and selected_row <= player1_board.size)):
        attack_result = player1_board.addAttack(selected_row, selected_column)
        if(attack_result >= 0):
            if(attack_result == 0):
                print("\nCPU:OH NO!, You hit my ship")
                global_number_of_battleships -= 1
            elif(attack_result == 0):
                print("\nCPU:HA HA, you miss, not even close")
            global_number_of_attacks -= 1
        else:
            print("\nCPU: Focus man, you´ve already tried to hit me in that location")
        if(global_number_of_battleships > 0):
            print("\nCPU:you have {0} more tries and {1} more ship(s) to sink".format(global_number_of_attacks,global_number_of_battleships))
        else:
            print("\nCPU:Congrats! You've sunk all the ships, you win")
            break
    else:
        print("\nCPU:Are you crazy?, That is not even in the ocean")
    print(repr(player1_board))
else:
    print("\nCPU:YOU LOSE, I'm the best")
    print("\nCPU:my ships were at:")
    player1_board.printShipsLocation()
            
#print(repr(player1_board))
#print(player1_board.addAttack(0,0))
#print(player1_board.addAttack(0,0))
#print(repr(player1_board))
                
'''
print "-"*5*number_of_battleships
for row in self.defense_board:
print " ".join(row)
'''

#-----Single Player game global variables--#

