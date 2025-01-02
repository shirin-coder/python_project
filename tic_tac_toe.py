import tkinter

def set_tile(row,column):
    global curr_player

    if board[row][column]["text"] != "":
        return
    
    board[row][column]["text"] = curr_player  #mark the board
    
    if curr_player == playerO: #switch player
        curr_player = playerX
    else:
        curr_player = playerO

    label["text"] = curr_player+" s turn"


# check winner
def check_winner()
def new_game():
    pass


# game setup
playerX = "X"
playerO = "O"
curr_player = playerX
board = [[0,0,0],
         [0,0,0],
         [0,0,0]]

color_blue = "#4584b6"
color_yellow = "#ffde57"
color_gray = "#343434"
color_light_gray = "#646464"

turns = 0
game_over = False
# window setup
window = tkinter.Tk()
window.title("Tic Tac Toe")
window.resizable(False,False)


frame = tkinter.Frame(window) #placing frame inside the window
label = tkinter.Label(frame,text=curr_player+" 's turn",font=("Consolas",20),background=color_gray,
                      foreground="white")


label.grid(row=0,column=0,columnspan=3,sticky="we")

for row in range(3):
    for column in range(3):
        board[row][column] = tkinter.Button(frame,text="",font=("Consolas",50,"bold"),
                                            background=color_gray,foreground=color_blue,width = 4,height = 1,
                                            command=lambda row=row,column=column:set_tile(row,column))
        board[row][column].grid(row=row+1,column=column)




button = tkinter.Button(frame,text="restart",font=("Consolas",20),background=color_gray,
                        foreground="white",command = new_game)
button.grid(row=4,column=0,columnspan=3,sticky="we")
frame.pack()


window.mainloop() #This loop keeps your application running and responsive
