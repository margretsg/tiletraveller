 # 1.Which implementation was easier and why? 
# The second is easier because then it is possible to break the problem down into smaller pieces.
 # 2. Which implementation is more readable and why? 
# The second is more readable because the code calls the necessary functions, that are outside of the 
# main program, that do the necessary work and return the solution to the program so it can continue. The code is thus shorter 
# making it easier to read.
 # 3. Which problems in the first implementations were you able to solve with the latter implementation? 
# The problem of having too long code that was difficult to read.
 
#Find what directions are available (row, column).
#Find if input from user is in accordance with available directions. Loops until correct input is received.
#Change position based on chosen direction. 
#Program runs as long as the user has not reached final destination (row 1, column 3).
#Program stops when user is in row 1, column 3. 
#https://github.com/margretsg/tiletraveller

#Function that finds out which directions are possible. Takes in the position, i.e. number of row and column
#and returns the row and column combinations that are possible for each direction (north, east, south, west).
def may_move_north(row, column):
#Function that finds out if user can move north   
    return row == 1 or (row == 2 and column == 1) or (row == 2 and column == 3)
def may_move_east(row, column):
#Function that finds out if user can move east      
    return (row == 2 and column == 1) or (row == 3 and column == 1) or (row == 3 and column == 2)
def may_move_south(row, column): 
#Function that finds out if user can move south        
    return row != 1 and not(row == 3 and column == 2)
def may_move_west(row, column):
#Function that finds out if user can move west       
    return (row == 2 and column == 2) or (row == 3 and column == 2) or (row == 3 and column == 3)

def choose_direction():
#Function that takes in input from user (the direction), if it is not valid it loops until is valid.
#Input from user, lowercased so it does not matter if it is capitalised or not when compared to allowed directions.
#Returns the direction.
    direction = input("Direction: ")
    lower_direction = direction.lower()
    #check if input is ok, i.e. is in accordance with allowed directions.
    compareString = "(" + lower_direction + ")"
    if compareString not in direct.lower() :
        print("Not a valid direction!")
        while compareString not in direct.lower():
            direction = input("Direction: ")
            lower_direction = direction.lower()
            compareString = "(" + lower_direction + ")"
    return lower_direction 

def move(lower_direction, row, column):
#Function that takes in the direction from user and moves the user by row or column according to that direction. 
# Returns number of row and column.
    if  lower_direction == "n": 
        row += 1
    elif lower_direction == "s": 
        row -= 1
    elif lower_direction == "e": 
        column += 1
    elif lower_direction == "w": 
        column -= 1
    return row, column

row = 1
column = 1
direct = "You can travel: "
base_length = len(direct)
while True:
    #Find available directions
    direct = "You can travel: "
    if may_move_north(row, column) :
        direct += "(N)orth"                          
    if may_move_east(row, column):
        if len(direct) > base_length:
            direct += " or "
        direct += "(E)ast"                
    if may_move_south(row, column):
        if len(direct) > base_length:
            direct += " or "
        direct += "(S)outh"                                   
    if may_move_west(row, column):
        if len(direct) > base_length:
            direct += " or "
        direct += "(W)est"                          
    print(direct + ".")
    #Function call, returns direction chosen by user.
    lower_direction = choose_direction()
    #Function call, returns the moves (row, column) in accordance to the chosen direction.
    row, column = move(lower_direction, row, column)
    #If final destination is reached, the program prints Victory and ends.
    if row == 1 and column == 3:
        print("Victory!")
        break
  