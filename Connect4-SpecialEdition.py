
import time
#intro
print("\nWelcome to Connect 4!\nThe goal of this game is to connect 4 of your assigned symbols in a row the following ways:\nvertically, horizontally, or diagonally.\n")
print("BUT - THERE IS A TWIST! THE LAWS OF GRAVITY HAVE BEEN VOIDED!\nYOU WILL NOW GET TO EXPERIENCE A NEW WAY OF PLAYING CONNECT 4!\n")
time.sleep(3)
print(3)
time.sleep(1)
print(2)
time.sleep(1)
print(1)
time.sleep(1)
print("\nWELCOME TO A NEW ERA OF CONNECT 4!\n")
#connect 4 board
columns = ["Column >","|1|","|2|","|3|","|4|","|5|","|6|","|7|","|8|"]
r8 = ["Row 8 ->","|_|","|_|","|_|","|_|","|_|","|_|","|_|","|_|"]
r7 = ["Row 7 ->","|_|","|_|","|_|","|_|","|_|","|_|","|_|","|_|"]
r6 = ["Row 6 ->","|_|","|_|","|_|","|_|","|_|","|_|","|_|","|_|"]
r5 = ["Row 5 ->","|_|","|_|","|_|","|_|","|_|","|_|","|_|","|_|"]
r4 = ["Row 4 ->","|_|","|_|","|_|","|_|","|_|","|_|","|_|","|_|"]
r3 = ["Row 3 ->","|_|","|_|","|_|","|_|","|_|","|_|","|_|","|_|"]
r2 = ["Row 2 ->","|_|","|_|","|_|","|_|","|_|","|_|","|_|","|_|"]
r1 = ["Row 1 ->","|_|","|_|","|_|","|_|","|_|","|_|","|_|","|_|"]
#grid function will print out the grid every time called

#prints out grid

#setup
player1 = input("Enter Player #1's name: ")
player2 = input("Enter Player #2's name: ")
print()
print("\n\n\n\n\n\n\n\n\n\n\n\nPlayer 1 - " + player1 + "'s symbol is: ☂\nPlayer 2 - " + player2 + "'s symbol is: ☀︎\n\nGRID: \n")
columns_final = ""
one = ""
two = ""
three = ""
four = ""
five = ""
six = ""
seven = ""
eight = ""
    

for i in r1:
    one += i
    one += " "
for i in r2:
     two += i
     two += " "
for i in r3:
    three += i
    three += " "
for i in r4:
    four += i
    four += " "
for i in r5:
    five += i
    five += " "
for i in r6:
    six += i
    six += " "
for i in r7:
    seven += i
    seven += " "
for i in r8:
    eight += i
    eight += " "
for i in columns:
    columns_final += i
    columns_final += " "
    
print(columns_final)
print(one)
print(two)
print(three)
print(four)
print(five)
print(six)
print(seven)
print(eight)

#setting def for grid for future use cases
def grid():
    print("\n\n\n\n\n\n\n\n\n\n\n\nPlayer 1 - " + player1 + "'s symbol is: ☂\nPlayer 2 - " + player2 + "'s symbol is: ☀︎\n\nGRID: \n")
    columns_final = ""
    one = ""
    two = ""
    three = ""
    four = ""
    five = ""
    six = ""
    seven = ""
    eight = ""
    

    for i in r1:
        one += i
        one += " "
    for i in r2:
        two += i
        two += " "
    for i in r3:
        three += i
        three += " "
    for i in r4:
        four += i
        four += " "
    for i in r5:
        five += i
        five += " "
    for i in r6:
        six += i
        six += " "
    for i in r7:
        seven += i
        seven += " "
    for i in r8:
        eight += i
        eight += " "
    for i in columns:
        columns_final += i
        columns_final += " "
    
    print(columns_final)
    print(one)
    print(two)
    print(three)
    print(four)
    print(five)
    print(six)
    print(seven)
    print(eight)
    

#variables used later for identification
row = 0
row_num = 0
term_num = 0
column_num = str()
end_or_not = False
#player 1's turn
def p1():
    global row
    global row_num
    global column_num
    print("\nIt's " + player1 + "'s turn!")
    column_num = int(input("Enter a column number to place ☂︎: "))
    if column_num > 8 or column_num < 1:
        print("That column doesn't exist! Try again.")
        p1()
    elif r1[column_num] == "|_|":
        r1[column_num] = "|☂︎|"
        row = r1
        row_num = 1
        grid()
    elif r2[column_num] == "|_|":
        r2[column_num] = "|☂︎|"
        row = r2
        row_num = 2
        grid()  
    elif r3[column_num] == "|_|":
        r3[column_num] = "|☂︎|"
        row = r3
        row_num = 3
        grid()  
    elif r4[column_num] == "|_|":
        r4[column_num] = "|☂︎|"
        row = r4
        row_num = 4
        grid()  
    elif r5[column_num] == "|_|":
        r5[column_num] = "|☂︎|"
        row = r5
        row_num = 5
        grid()  
    elif r6[column_num] == "|_|":
        r6[column_num] = "|☂︎|"
        row = r6
        row_num = 6
        grid()  
    elif r7[column_num] == "|_|":
        r7[column_num] = "|☂︎|"
        row = r7
        row_num = 7
        grid()  
    elif r8[column_num] == "|_|":
        r8[column_num] = "|☂︎|"
        row = r8
        row_num = 8
        grid() 
    else: 
        print("There are no more spaces left in column number " + str(column_num))
        p1()
#player 2's turn 
def p2():
    global row
    global row_num
    global column_num
    print("\nIt's "+player2 + "'s turn!")
    column_num = int(input("Enter a column number to place ☀︎: "))
    if column_num > 8 or column_num < 1:
        print("That column does not exist! Try again.")
        p2()
    elif r1[column_num] == "|_|":
        r1[column_num] = "|☀︎|"
        row = r1
        row_num = 1
        grid()
    elif r2[column_num] == "|_|":
        r2[column_num] = "|☀︎|"
        row = r2
        row_num = 2
        grid()  
    elif r3[column_num] == "|_|":
        r3[column_num] = "|☀︎|"
        row = r3
        row_num = 3
        grid()  
    elif r4[column_num] == "|_|":
        r4[column_num] = "|☀︎|"
        row = r4
        row_num = 4
        grid()  
    elif r5[column_num] == "|_|":
        r5[column_num] = "|☀︎|"
        row = r5
        row_num = 5
        grid()  
    elif r6[column_num] == "|_|":
        r6[column_num] = "|☀︎|"
        row = r6
        row_num = 6
        grid()  
    elif r7[column_num] == "|_|":
        r7[column_num] = "|☀︎|"
        row = r7
        row_num = 7
        grid()  
    elif r8[column_num] == "|_|":
        r8[column_num] = "|☀︎|"
        row = r8
        row_num = 8
        grid() 
    else: 
        print("There are no more spaces left in column number " + str(column_num)) 
        p2()


while True:
    #player 1's move
    p1()
    #assigns vertical columns to variables
    c1 = [r1[1],r2[1],r3[1],r4[1],r5[1],r6[1],r7[1],r8[1]]
    c2 = [r1[2],r2[2],r3[2],r4[2],r5[2],r6[2],r7[2],r8[2]]
    c3 = [r1[3],r2[3],r3[3],r4[3],r5[3],r6[3],r7[3],r8[3]]
    c4 = [r1[4],r2[4],r3[4],r4[4],r5[4],r6[4],r7[4],r8[4]]
    c5 = [r1[5],r2[5],r3[5],r4[5],r5[5],r6[5],r7[5],r8[5]]
    c6 = [r1[6],r2[6],r3[6],r4[6],r5[6],r6[6],r7[6],r8[6]]
    c7 = [r1[7],r2[7],r3[7],r4[7],r5[7],r6[7],r7[7],r8[7]] 
    c8 = [r1[8],r2[8],r3[8],r4[8],r5[8],r6[8],r7[8],r8[8]]   
    connect4 = 0
    #checks for horizontal connect 4
    for term in r1:
        if term == "|☂︎|":
            connect4 += 1
            if connect4 == 4:
                print(player1 + " wins ☺︎")
                exit()
        else:
            connect4 = 0
    for term in r2:
        if term == "|☂︎|":
            connect4 += 1
            if connect4 == 4:
                print(player1 + " wins ☺︎")
                exit()
        else:
            connect4 = 0
        
    for term in r3:
        if term == "|☂︎|":
            connect4 += 1
            if connect4 == 4:
                print(player1 + " wins ☺︎")
                exit()
        else:
            connect4 = 0
    for term in r4:
        if term == "|☂︎|":
            connect4 += 1
            if connect4 == 4:
                print(player1 + " wins ☺︎")
                exit()
        else:
            connect4 = 0
    for term in r5:
        if term == "|☂︎|":
            connect4 += 1
            if connect4 == 4:
                print(player1 + " wins ☺︎")
                exit()
        else:
            connect4 = 0
    for term in r6:
        if term == "|☂︎|":
            connect4 += 1
            if connect4 == 4:
                print(player1 + " wins ☺︎")
                exit()
        else:
            connect4 = 0
    for term in r7:
        if term == "|☂︎|":
            connect4 += 1
            if connect4 == 4:
                print(player1 + " wins ☺︎")
                exit()
        else:
            connect4 = 0
    for term in r8:
        if term == "|☂︎|":
            connect4 += 1
            if connect4 == 4:
                print(player1 + " wins ☺︎")
                exit()
        else:
            connect4 = 0
    #checks for vertical connect 4
    for term in c1:
        if term == "|☂︎|":
            connect4 += 1
            if connect4 == 4:
                print(player1  + " wins ☺︎")
                exit()
        else:
            connect4 = 0
    for term in c2:
        if term == "|☂︎|":
            connect4 += 1
            if connect4 == 4:
                print(player1  + " wins ☺︎")
                exit()
        else:
            connect4 = 0
    for term in c3:
        if term == "|☂︎|":
            connect4 += 1
            if connect4 == 4:
                print(player1  + " wins ☺︎")
                exit()
        else:
            connect4 = 0
    for term in c4:
        if term == "|☂︎|":
            connect4 += 1
            if connect4 == 4:
                print(player1  + " wins ☺︎")
                exit()
        else:
            connect4 = 0
    for term in c5:
        if term == "|☂︎|":
            connect4 += 1
            if connect4 == 4:
                print(player1  + " wins ☺︎")
                exit()
        else:
            connect4 = 0
    for term in c6:
        if term == "|☂︎|":
            connect4 += 1
            if connect4 == 4:
                print(player1  + " wins ☺︎")
                exit()
        else:
            connect4 = 0
    for term in c7:
        if term == "|☂︎|":
            connect4 += 1
            if connect4 == 4:
                print(player1  + " wins ☺︎")
                exit()
        else:
            connect4 = 0
    for term in c8:
        if term == "|☂︎|":
            connect4 += 1
            if connect4 == 4:
                print(player1  + " wins ☺︎")
                exit()
        else:
            connect4 = 0
    #check for horizontal connect 4
    term_num=0
    for term in c1:
        term_num += 1
        if term == "|☂︎|":
            try:
                if c2[term_num] == "|☂︎|":
                    if c3[term_num + 1] == "|☂︎|":
                        if c4[term_num + 2] == "|☂︎|":
                            print(player1 + " wins ☺︎")
                            end_or_not = True
                            break
            except:
                pass
    term_num=0        
    for term in c2:
        term_num += 1
        if term == "|☂︎|":
            try:
                if c3[term_num] == "|☂︎|":
                    if c4[term_num + 1] == "|☂︎|":
                        if c5[term_num + 2] == "|☂︎|":
                            print(player1+" wins ☺︎")
                            end_or_not = True
                            break
            except:
                pass
    term_num=0     
    for term in c3:
        term_num += 1
        if term == "|☂︎|":
            try:
                if c4[term_num] == "|☂︎|":
                    if c5[term_num + 1] == "|☂︎|":
                        if c6[term_num + 2] == "|☂︎|":
                            print(player1+" wins ☺︎")
                            end_or_not = True
                            break
            except:
                pass
    term_num=0    
    for term in c4:
        term_num += 1
        if term == "|☂︎|":
            try:
                if c5[term_num] == "|☂︎|":
                    if c6[term_num + 1] == "|☂︎|":
                        if c7[term_num + 2] == "|☂︎|":
                            print(player1+" wins ☺︎")
                            end_or_not = True
                            break
            except:
                pass
    term_num=0
    for term in c5:
        term_num += 1
        if term == "|☂︎|":
            try:
                if c6[term_num] == "|☂︎|":
                    if c7[term_num + 1] == "|☂︎|":
                        if c8[term_num + 2] == "|☂︎|":
                            print(player1+" wins ☺︎")
                            end_or_not = True
                            break
            except:
                pass
    term_num=0
    for term in c8:
        term_num += 1
        if term == "|☂︎|":
            try:
                if c7[term_num] == "|☂︎|":
                    if c6[term_num + 1] == "|☂︎|":
                        if c5[term_num + 2] == "|☂︎|":
                            print(player1+" wins ☺︎")
                            end_or_not = True
                            break
            except:
                pass  
    term_num=0
    for term in c7:
        term_num += 1
        if term == "|☂︎|":
            try:
                if c6[term_num] == "|☂︎|":
                    if c5[term_num + 1] == "|☂︎|":
                        if c4[term_num + 2] == "|☂︎|":
                            print(player1+" wins ☺︎")
                            end_or_not = True
                            break
            except:
                pass
    term_num=0 
    for term in c6:
        term_num += 1
        if term == "|☂︎|":
            try:
                if c5[term_num] == "|☂︎|":
                    if c4[term_num + 1] == "|☂︎|":
                        if c3[term_num + 2] == "|☂︎|":
                            print(player1+" wins ☺︎")
                            end_or_not = True
                            break
            except:
                pass  
    term_num=0  
    for term in c5:
        term_num += 1
        if term == "|☂︎|":
            try:
                if c4[term_num] == "|☂︎|":
                    if c3[term_num + 1] == "|☂︎|":
                        if c2[term_num + 2] == "|☂︎|":
                            print(player1+" wins ☺︎")
                            end_or_not = True
                            break
            except:
                pass  
    term_num=0   
    for term in c4:
        term_num += 1
        if term == "|☂︎|":
            try:
                if c3[term_num] == "|☂︎|":
                    if c2[term_num + 1] == "|☂︎|":
                        if c1[term_num + 2] == "|☂︎|":
                            print(player1+" wins ☺︎")
                            end_or_not = True
                            break
            except:
                pass  
    term_num=0   
    if end_or_not == True:
        exit()
    #player two's move
    p2()
    #assigns vertical columns to variables
    c1 = [r1[1],r2[1],r3[1],r4[1],r5[1],r6[1],r7[1],r8[1]]
    c2 = [r1[2],r2[2],r3[2],r4[2],r5[2],r6[2],r7[2],r8[2]]
    c3 = [r1[3],r2[3],r3[3],r4[3],r5[3],r6[3],r7[3],r8[3]]
    c4 = [r1[4],r2[4],r3[4],r4[4],r5[4],r6[4],r7[4],r8[4]]
    c5 = [r1[5],r2[5],r3[5],r4[5],r5[5],r6[5],r7[5],r8[5]]
    c6 = [r1[6],r2[6],r3[6],r4[6],r5[6],r6[6],r7[6],r8[6]]
    c7 = [r1[7],r2[7],r3[7],r4[7],r5[7],r6[7],r7[7],r8[7]] 
    c8 = [r1[8],r2[8],r3[8],r4[8],r5[8],r6[8],r7[8],r8[8]]
    #loops through each row to see if there is a horizontal connect 4
    for term in r1:
        if term == "|☀︎|":
            connect4 += 1
            if connect4 == 4:
                print(player2 + " wins ☺︎")
                exit()
        else:
            connect4 = 0
    for term in r2:
        if term == "|☀︎|":
            connect4 += 1
            if connect4 == 4:
                print(player2 + " wins ☺︎")
                exit()
        else:
            connect4 = 0
    for term in r3:
        if term == "|☀︎|":
            connect4 += 1
            if connect4 == 4:
                print(player2 + " wins ☺︎")
                exit()
        else:
            connect4 = 0
    for term in r4:
        if term == "|☀︎|":
            connect4 += 1
            if connect4 == 4:
                print(player2 + " wins ☺︎")
                exit()
        else:
            connect4 = 0
    for term in r5:
        if term == "|☀︎|":
            connect4 += 1
            if connect4 == 4:
                print(player2 + " wins ☺︎")
                exit()
        else:
            connect4 = 0
    for term in r6:
        if term == "|☀︎|":
            connect4 += 1
            if connect4 == 4:
                print(player2 + " wins ☺︎")
                exit()
        else:
            connect4 = 0
    for term in r7:
        if term == "|☀︎|":
            connect4 += 1
            if connect4 == 4:
                print(player2 + " wins ☺︎")
                exit()
        else:
            connect4 = 0
    for term in r8:
        if term == "|☀︎|":
            connect4 += 1
            if connect4 == 4:
                print(player2 + " wins ☺︎")
                exit()
        else:
            connect4 = 0
    #checks for vertical connect 4
    for term in c1:
        if term == "|☀︎|":
            connect4 += 1
            if connect4 == 4:
                print(player2 + " wins ☺︎")
                exit()
        else:
            connect4 = 0
    for term in c2:
        if term == "|☀︎|":
            connect4 += 1
            if connect4 == 4:
                print(player2 + " wins ☺︎")
                exit()
        else:
            connect4 = 0
    for term in c3:
        if term == "|☀︎|":
            connect4 += 1
            if connect4 == 4:
                print(player2 + " wins ☺︎")
                exit()
        else:
            connect4 = 0
    for term in c4:
        if term == "|☀︎|":
            connect4 += 1
            if connect4 == 4:
                print(player2 + " wins ☺︎")
                exit()
        else:
            connect4 = 0
    for term in c5:
        if term == "|☀︎|":
            connect4 += 1
            if connect4 == 4:
                print(player2 + " wins ☺︎")
                exit()
        else:
            connect4 = 0
    for term in c6:
        if term == "|☀︎|":
            connect4 += 1
            if connect4 == 4:
                print(player2 + " wins ☺︎")
                exit()
        else:
            connect4 = 0
    for term in c7:
        if term == "|☀︎|":
            connect4 += 1
            if connect4 == 4:
                print(player2 + " wins ☺︎")
                exit()
        else:
            connect4 = 0
    for term in c8:
        if term == "|☀︎|":
            connect4 += 1
            if connect4 == 4:
                print(player2 + " wins ☺︎")
                exit()
        else:
            connect4 = 0
    #check for horizontal connect 4
    term_num=0
    for term in c1:
        term_num += 1
        if term == "|☀︎|":
            try:
                if c2[term_num] == "|☀︎|":
                    if c3[term_num + 1] == "|☀︎|":
                        if c4[term_num + 2] == "|☀︎|":
                            print(player1+" wins ☺︎")
                            end_or_not = True
                            break
            except:
                pass
    term_num=0        
    for term in c2:
        term_num += 1
        if term == "|☀︎|":
            try:
                if c3[term_num] == "|☀︎|":
                    if c4[term_num + 1] == "|☀︎|":
                        if c5[term_num + 2] == "|☀︎|":
                            print(player1+" wins ☺︎")
                            end_or_not = True
                            break
            except:
                pass
    term_num=0     
    for term in c3:
        term_num += 1
        if term == "|☀︎|":
            try:
                if c4[term_num] == "|☀︎|":
                    if c5[term_num + 1] == "|☀︎|":
                        if c6[term_num + 2] == "|☀︎|":
                            print(player1+" wins ☺︎")
                            end_or_not = True
                            break
            except:
                pass
    term_num=0    
    for term in c4:
        term_num += 1
        if term == "|☀︎|":
            try:
                if c5[term_num] == "|☀︎|":
                    if c6[term_num + 1] == "|☀︎|":
                        if c7[term_num + 2] == "|☀︎|":
                            print(player1+" wins ☺︎")
                            end_or_not = True
                            break
            except:
                pass
    term_num=0
    for term in c5:
        term_num += 1
        if term == "|☀︎|":
            try:
                if c6[term_num] == "|☀︎|":
                    if c7[term_num + 1] == "|☀︎|":
                        if c8[term_num + 2] == "|☀︎|":
                            print(player1+" wins ☺︎")
                            end_or_not = True
                            break
            except:
                pass
    term_num=0
    for term in c8:
        term_num += 1
        if term == "|☀︎|":
            try:
                if c7[term_num] == "|☀︎|":
                    if c6[term_num + 1] == "|☀︎|":
                        if c5[term_num + 2] == "|☀︎|":
                            print(player1+" wins ☺︎")
                            end_or_not = True
                            break
            except:
                pass  
    term_num=0
    for term in c7:
        term_num += 1
        if term == "|☀︎|":
            try:
                if c6[term_num] == "|☀︎|":
                    if c5[term_num + 1] == "|☀︎|":
                        if c4[term_num + 2] == "|☀︎|":
                            print(player1+" wins ☺︎")
                            end_or_not = True
                            break
            except:
                pass
    term_num=0 
    for term in c6:
        term_num += 1
        if term == "|☀︎|":
            try:
                if c5[term_num] == "|☀︎|":
                    if c4[term_num + 1] == "|☀︎|":
                        if c3[term_num + 2] == "|☀︎|":
                            print(player1+" wins ☺︎")
                            end_or_not = True
                            break
            except:
                pass  
    term_num=0  
    for term in c5:
        term_num += 1
        if term == "|☀︎|":
            try:
                if c4[term_num] == "|☀︎|":
                    if c3[term_num + 1] == "|☀︎|":
                        if c2[term_num + 2] == "|☀︎|":
                            print(player1+" wins ☺︎")
                            end_or_not = True
                            break
            except:
                pass  
    term_num=0   
    for term in c4:
        term_num += 1
        if term == "|☀︎|":
            try:
                if c3[term_num] == "|☀︎|":
                    if c2[term_num + 1] == "|☀︎|":
                        if c1[term_num + 2] == "|☀︎|":
                            print(player1+" wins ☺︎")
                            end_or_not = True
                            break
            except:
                pass  
    term_num=0   
    if end_or_not == True:
        exit()