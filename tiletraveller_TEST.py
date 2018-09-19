row = 1
column = 1
#print("You can travel (N)orth")
msg = "You can travel:"
first_direct = "You can travel:"
#while column < 3:
#Find available directions

#if direction == "n" or "N":
# tiles that allow travel north
if row == 1 or (row == 2 and column == 1) or (row == 2 and column == 3)  :
    msg += "(N)orth"
    direct = "(N)orth"
    #if row < 3:
     #   row += 1                             #ef er farið norður er farið upp um 1 línu (+1)
#tiles that allow travel south
if row != 1 and not(row == 3 and column == 2):
    msg += " or (S)outh"
    direct = "(S)outh"
    #if row > 1:
     #   row -= 1                             #ef er farið suður er farið niður um 1 línu (-1)
#tiles that allow travel east
if (row == 2 and column == 1) or (row == 3 and column == 1) or (row == 3 and column == 2):
    msg += " or (E)ast"
    direct = "(E)ast"
    #if column < 3:
     #   column += 1                          #ef er farið austur er farið til hægri um 1 dálk (+1)
#tiles that allow travel west
if (row == 2 and column == 2) or (row == 3 and column == 2) or (row == 3 and column == 3):
     msg += " or (W)est"
     direct = "(W)est"
     # if column > 1:
     #   column -= 1                          #ef er farið vestur er farið til vinstri um 1 dálk (-1)

#if (row == 1 and column == 3):
#    print("Victory")

print(msg)
direction = input("Direction: ")
print(type(direction))
concatenate_directions = first_direct + direct
print(concatenate_directions)
for i in direct:
    #fjarlægja sviga utan um fyrsta staf
if direction == direct[1]:
    print("direction ok")

print("röð, dálkur fyrir breytingu: ", row, "", column)
if direction == "N" or direction == "n" and row < 3:
    row += 1
elif direction == "S" or direction == "s" and row > 1:
    row -= 1
elif direction == "E" or direction == "e" and column < 3:
    column += 1
elif direction == "W" or direction == "w" and column > 1:
    column -= 1

print("röð, dálkur eftir breytingu: ", row, "", column)