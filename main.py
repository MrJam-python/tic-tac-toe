import random

print ("Welcome to TIC-TAC-TOE!")
board_pos = ["-", "-", "-", "-", "-", "-", "-", "-", "-",]
#            0    1    2    3   4     5    6    7   8 
cpu_xo = 0
x_or_o = input ("Would you like to play as an O or an X?")
while x_or_o != "X" and x_or_o != "O":
    print ("INVALID INPUT, please re-enter your input.")
    x_or_o = input("Choose X or O.")
print ("Your selected letter was " + x_or_o + ".")
if x_or_o == "X":
    cpu_xo = "O"
else:
    cpu_xo = "X"
print ("The cpu has chosen " + cpu_xo + ".")
print (f"[{board_pos[0]}][{board_pos[1]}][{board_pos[2]}]")
print (f"[{board_pos[3]}][{board_pos[4]}][{board_pos[5]}]")
print (f"[{board_pos[6]}][{board_pos[7]}][{board_pos[8]}]")
mddle_man = input ("Pick a position 1-9.")
while True:
    if str(type(mddle_man)) == "<class 'str'>" and int(choice) not in range(0,9):
        mddle_man = input("INVALID INPUT, please re-enter your input.")    
    else:
        break
board_pos[int(mddle_man)-1] = x_or_o
print (board_pos)