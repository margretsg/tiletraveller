row = 1
column = 1
direct = "You can travel: "
base_length = len(direct)
#Find available directions
count = 1
while True:
    direct = "You can travel: "
    # tiles that allow travel north
    if row == 1 or (row == 2 and column == 1) or (row == 2 and column == 3)  :
        direct += "(N)orth"                          #ef er farið norður er farið upp um 1 línu (+1)
    #tiles that allow travel south
    if row != 1 and not(row == 3 and column == 2):
        if len(direct) > base_length:
            direct += " or "
        direct += "(S)outh"                          #ef er farið suður er farið niður um 1 línu (-1)
    #tiles that allow travel east
    if (row == 2 and column == 1) or (row == 3 and column == 1) or (row == 3 and column == 2):
        if len(direct) > base_length:
            direct += " or "
        direct += "(E)ast"                           #ef er farið austur er farið til hægri um 1 dálk (+1)
    #tiles that allow travel west
    if (row == 2 and column == 2) or (row == 3 and column == 2) or (row == 3 and column == 3):
        if len(direct) > base_length:
            direct += " or "
        direct += "(W)est"                          #ef er farið vestur er farið til vinstri um 1 dálk (-1)
    print(direct)
    
    #concatenate_directions = first_direct + direct
    #print(concatenate_directions)
    direction = input("Direction: ")
    lower_direction = direction.lower()
    #kanna hvort innslegin stafur(átt) sé í lagi, þ.e. strengur nr 1 í direct (þ.e. stafur nr. 2 sem er þá N, S, W, eða E)
    #stemmi við innslegin staf. Breyti báðum strengjum í lower svo séu samanburðarhæfir.
    compareString = "(" + lower_direction + ")"
    print("CompareString is: ", compareString)
    if compareString not in direct.lower() :
        print("Not a valid direction!")
    else:
        print("röð, dálkur fyrir breytingu: ", row, "", column)
        if  lower_direction == "n": #and row < 3:
            row += 1
        elif lower_direction == "s": #and row > 1:
            row -= 1
        elif lower_direction == "e": #and column < 3:
            column += 1
        elif lower_direction == "w": #and column > 1:
            column -= 1

    if row == 1 and column == 3:
        print("Victory!")
        break

    #tæma strenginn svo safnist ekki upp í hverri umferð þær áttir sem notandi má slá inn
    direct = str()
    print("röð, dálkur eftir breytingu: ", row, "", column)
    count += 1