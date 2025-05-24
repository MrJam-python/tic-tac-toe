print ("Welcome to TIC-TAC-TOE!")
board_pos = ["-", "-", "-", "-", "-", "-", "-", "-", "-",]
#             0    1    2    3   4     5    6    7   8 
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
print ("[-][-][-]")
print ("[-][-][-]")
print ("[-][-][-]")
