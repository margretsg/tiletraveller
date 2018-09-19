

def move(direction, row, column):
    lower_direction = direction.lower()
    #check if input is ok, i.e. is the same as the direction the user could go.
    compareString = "(" + lower_direction + ")"
    if compareString not in direct.lower() :
        print("Not a valid direction!")
    else:
        #change position according to chosen direction. 
        #print("rowð, column before change: ", row, "", column)
        if  lower_direction == "n": 
            row += 1
        elif lower_direction == "s": 
            row -= 1
        elif lower_direction == "e": 
            column += 1
        elif lower_direction == "w": 
            column -= 1
    return row, column    

def may_move_north(row, column):   
#Decides if a user can move north
    return row == 1 or (row == 2 and column == 1) or (row == 2 and column == 3)
def may_move_south(row, column): 
#Decides if a user can move south   
    return row != 1 and not(row == 3 and column == 2)
def may_move_east(row, column):
#Decides if a user can move east
    return (row == 2 and column == 1) or (row == 3 and column == 1) or (row == 3 and column == 2)
def may_move_west(row, column):
#Decides if a user can move west
    return (row == 2 and column == 2) or (row == 3 and column == 2) or (row == 3 and column == 3)

row = 1
column = 1
direct = "You can travel: "
base_length = len(direct)    
#Find available directions
while True:
    direct = "You can travel: "
    # tiles that allow travel north
    if may_move_north(row, column) :
        direct += "(N)orth"                          
    #tiles that allow travel south
    if may_move_south(row, column):
        if len(direct) > base_length:
            direct += " or "
        direct += "(S)outh"                         
    #tiles that allow travel east
    if may_move_east(row, column):
        if len(direct) > base_length:
            direct += " or "
        direct += "(E)ast"                           
    #tiles that allow travel west
    if may_move_west(row, column):
        if len(direct) > base_length:
            direct += " or "
        direct += "(W)est"                          
    print(direct)
    #input from user
    direction = input("Direction: ")

    row, column = move(direction, row, column)

    if row == 1 and column == 3:
        print("Victory!")
        break
    #empty the string between rounds to have only the directions that are relevant for each round
    direct = str()
    #print("row, column after change: ", row, "", column)
  