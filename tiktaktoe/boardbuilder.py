#--------------- Board builder for tiktaktoe ------------------
# Var format:
#  boarddata = [ [0, 0, 0], [0, 0, 0], [0, 0, 0] ]
#  player = 1 or 2
#  p1score = must be a integer
#  p2score = must be a integer
#  input = String the script catch a null or restart/exit
#
# Functions:
#   Show_board( boarddata, player, p1score, p2score ):
#     description: a function to show the current board player and the score of the player;
#
#   Get_boardGet_board( row, line, borddata ):
#     description: return a number
#     var format: 0 == not set; 1 == X; 2 == O; over 2 == / (means error)
#
#   Set_board( input, boarddata, player ):
#     description: set the input on the board
#     info: input should look like a1 or something like that (the script catches other formats)
#
#   Check_board( boarddata ):
#     description: check for a tiktaktoe
#     info: if there is a tiktaktoe it returns the boarddata with the marked tiktaktoe
#           else it will be return false
#--------------- Board builder for tiktaktoe ------------------

from sys import platform

# Translate Number into Character
def translate( value ):
    if ( value == 0 ):
        return "-"
    elif ( value == 1):
        return "X"
    elif ( value == 2):
        return "O"
    else:
        return "\u001b[31m/\u001b[0m"

# Print current board
def Show_board( boarddata, player, p1score, p2score ):

    # new vars for a better overview
    a = boarddata[0]
    b = boarddata[1]
    c = boarddata[2]

    # print board title and line
    print(" +-< Board >--+--< " + cc("32m") +"Player " + str(player) + "\u001b[0m >-+\n |   1  2  3  |               |")

    # print board status
    print(" | A " + translate(a[0]) + "  " + translate(a[1]) + "  " + translate(a[2]) + "  |   \u001b[33mP1: " + str(p1score) + "\u001b[0m       |")
    print(" | B " + translate(b[0]) + "  " + translate(b[1]) + "  " + translate(b[2]) + "  |   \u001b[33mP2: " + str(p2score) + " \u001b[0m      |")
    print(" | C " + translate(c[0]) + "  " + translate(c[1]) + "  " + translate(c[2]) + "  |               |")

    # print footer
    print(" +-< Board >------------------+")

# Returning the board value on the coordinates row and line
def Get_board( row, line, borddata ):

    # Returning Board data
    if (row == "a"):
        return borddata[0][line]
    elif (row == "b"):
        return borddata[1][line]
    elif (row == "c"):
        return borddata[2][line]

# Set a mark on the board
def Set_board( input, boarddata, player ):

    ############# COMMANDS AND INPUT CHECK ################################################################
    # Check if input is False
    if not input:  print("\u001b[31mplease enter something\u001b[0m"); borddata = False; return boarddata;

    # restart board
    if input == "restart": print("\u001b[31mboard restarted!\u001b[0m"); boarddata = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]; return boarddata;

    # exit board
    if input == "exit": print("\u001b[31mexit tiktaktoe\u001b[0m"); return exit()
    ############# COMMANDS AND INPUT CHECK ################################################################


    # some vars for a better overview
    line = int( input[1] ) - 1
    row = input[0]

    # check if the vertical line is over the limit
    if row != "a" and row != "b" and row != "c":
        print("\u001b[31mCan´t set this input! [Switched Player] \u001b[0m")

    # check if the horizontal line is over the limit
    elif ( line > 3 or line < 0):
        print("\u001b[31mCan´t set this input! [Switched Player] \u001b[0m")

    # check if the spot is marked
    elif ( Get_board(row, line, boarddata) != 0 ):
        print("\u001b[31mThis position is marked by another Player! [Switched Player] \u001b[0m")

    # let the player mark
    else:
        if (row == "a"):
            boarddata[0][line] = player
        elif (row == "b"):
            boarddata[1][line] = player
        elif (row == "c"):
            boarddata[2][line] = player

    # returning new board with the mark
    return boarddata

# Checking if a player won
def Check_board( boarddata ):

    # some vars for a better overview
    a = boarddata[0]
    b = boarddata[1]
    c = boarddata[2]

    # check tiktaktoe
    if a[0] + a[1] + a[2] != 0 and a[0] == a[1] == a[2]:
        a[0] = 9
        a[1] = 9
        a[2] = 9
        return boarddata
    if b[0] + b[1] + b[2] != 0 and b[0] == b[1] ==[2]:
        b[0] = 9
        b[1] = 9
        b[2] = 9
        return boarddata
    if c[0] == c[1] == b[2] and c[0] + c[1] + c[2] != 0:
        c[0] = 9
        c[1] = 9
        c[2] = 9
        return boarddata
    if a[0] == b[0] == c[0] and a[0] + b[0] + c[0] != 0:
        a[0] = 9
        b[0] = 9
        c[0] = 9
        return boarddata
    if a[1] == b[1] == c[1] and a[1] + b[1] + c[1] != 0:
        a[1] = 9
        b[1] = 9
        c[1] = 9
        return boarddata
    if a[2] == b[2] == c[2] and a[2] + b[2] + c[2] != 0:
        a[2] = 9
        b[2] = 9
        c[2] = 9
        return boarddata
    if a[0] == b[1] == c[2] and a[0] + b[1] + c[2] != 0:
        a[0] = 9
        b[1] = 9
        c[2] = 9
        return boarddata
    if a[2] == b[1] == c[0] and a[2] + b[1] + c[0] != 0:
        a[2] = 9
        b[1] = 9
        c[0] = 9
        return boarddata

    # else:
    return False

def cc( color ):
    if platform == "darwin":
        return "\u001b[" + color
    elif platform == "win32" or platform == "win64":
        return "^<ESC^>[" + color
