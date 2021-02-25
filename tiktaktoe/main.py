import boardbuilder

# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    # register some variables
    boarddata = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
    player = 2
    p1score = 0
    p2score = 0

    # Start message - This Part is protected by Apache License 2.0   DO NOT EDIT
    print("------------------< tiktaktoe >------------------")
    print("\u001b[32m tiktaktoe startet with no error\u001b[0m")
    print(" for exit enter \u001b[31mexit\u001b[0m")
    print(" ")
    print("©Timur Stegmann")
    print("------------------< tiktaktoe >------------------")
    ###########################################################################


    #  running tik tak toe
    while ( True ):

        # toggle
        if (player == 1):
            player = 2
        else:
            player = 1

        # showing tiktaktoe board
        boardbuilder.Show_board(boarddata, player, p1score, p2score )

        # asking input
        boarddata = boardbuilder.Set_board(input(""), boarddata, player)


        if ( boardbuilder != False ):
            # Checking if there is a tiktaktoe
            if (boardbuilder.Check_board(boarddata) != False):
                # updating boarddata to let the player see where the tiktaktoe is
                boarddata = boardbuilder.Check_board(boarddata);

                # Setting player score after round
                if (player == 1):
                    p1score = p1score + 1
                else:
                    p2score = p2score + 1

                # Sending win message
                print("Session ended. \u001b[33mPlayer " + str(player) + " won!\u001b[0m RESULT:")
                # show the board
                boardbuilder.Show_board( boarddata, player, p1score, p2score )

                # wait for input
                input("press any key to continue")

                # reset the board
                boarddata = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
