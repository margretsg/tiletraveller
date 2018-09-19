#Find what directions are available (row, column).
#Find if input from user is in accordance with available directions. 
#Change position based on chosen direction. 
#The program runs as long as the user has not reached final destination (row 1, column 3).
#The program stops when user is in row 1, column 3. 
#https://github.com/margretsg/tiletraveller
row = 1
column = 1
direct = "You can travel: "
base_length = len(direct)
#Find available directions
while True:
    direct = "You can travel: "
    # tiles that allow travel north
    if row == 1 or (row == 2 and column == 1) or (row == 2 and column == 3)  :
        direct += "(N)orth"                          
    #tiles that allow travel south
    if row != 1 and not(row == 3 and column == 2):
        if len(direct) > base_length:
            direct += " or "
        direct += "(S)outh"                         
    #tiles that allow travel east
    if (row == 2 and column == 1) or (row == 3 and column == 1) or (row == 3 and column == 2):
        if len(direct) > base_length:
            direct += " or "
        direct += "(E)ast"                           
    #tiles that allow travel west
    if (row == 2 and column == 2) or (row == 3 and column == 2) or (row == 3 and column == 3):
        if len(direct) > base_length:
            direct += " or "
        direct += "(W)est"                          
    print(direct)
    #input from user, lowercased so it does not matter if it is capitalised or not when compared to allowed directions.
    direction = input("Direction: ")
    lower_direction = direction.lower()
    #check if input is ok, i.e. is in accordance with allowed directions.
    compareString = "(" + lower_direction + ")"
    if compareString not in direct.lower() :
        print("Not a valid direction!")
    else:
        #change position based on chosen direction.
        #print("row, column before change: ", row, "", column)
        if  lower_direction == "n": 
            row += 1
        elif lower_direction == "s": 
            row -= 1
        elif lower_direction == "e": 
            column += 1
        elif lower_direction == "w": 
            column -= 1
    if row == 1 and column == 3:
        print("Victory!")
        break
    #empty the string between rounds to have only the directions that are relevant for each round
    direct = str()
    #print("row, column after change: ", row, "", column)
  