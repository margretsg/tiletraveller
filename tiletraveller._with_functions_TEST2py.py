#Find what directions are available (row, column).
#Find if input from user is in accordance with available directions. 
#Change position based on chosen direction. 
#The program runs as long as the user has not reached final destination (row 1, column 3).
#The program stops when user is in row 1, column 3. 
#https://github.com/margretsg/tiletraveller

##Function that finds out which directions are possible.
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
#input from user, lowercased so it does not matter if it is capitalised or not when compared to allowed directions.
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
#Function that moves the user according to the direction chosen by the user
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
#Find available directions
while True:
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
    ##Function calls, return moves
    #if  lower_direction == "n": 
    #    row += 1
    #elif lower_direction == "s": 
    #    row -= 1
    #elif lower_direction == "e": 
    #    column += 1
    #elif lower_direction == "w": 
    #    column -= 1
    if row == 1 and column == 3:
        print("Victory!")
        break
  