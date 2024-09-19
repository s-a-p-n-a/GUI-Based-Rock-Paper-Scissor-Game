from tkinter import *
from PIL import Image, ImageTk
from random import randint

window = Tk()           #variable for tk window screen
window.title("Rock Paper and Scissor")
window.configure(background="SkyBlue")


image_rock1 = ImageTk.PhotoImage(Image.open("computer-stone.png"))
image_paper1 = ImageTk.PhotoImage(Image.open("computer-paper.png"))
image_scissor1 = ImageTk.PhotoImage(Image.open("computer-scissor.png"))
image_rock2 = ImageTk.PhotoImage(Image.open("rock.png"))
image_paper2 = ImageTk.PhotoImage(Image.open("paper.png"))
image_scissor2 = ImageTk.PhotoImage(Image.open("scissor.png"))



label_player = Label(window, image=image_scissor2)   #label is a function, for label  Added default images as scissor can add any
label_computer = Label(window, image=image_scissor1)
label_computer.grid(row=1, column=0)
label_player.grid(row=1, column=4)

computer_score = Label(window, text=0,font=("arial",60,"bold"),fg="red", bg="SkyBlue")
player_score =Label(window, text=0, font=("arial",60,"bold"),fg="red", bg="SkyBlue")
computer_score.grid(row=1, column=1)         #alignment
player_score.grid(row=1, column=3)

player_indicator = Label(window,font=('arial',40,"bold"),text=" PLAYER",    #labeling 
                         bg="orange", fg="black")
computer_indicator = Label(window, font=("arial",40,"bold"),text="COMPUTER",
                           bg="orange", fg="black")
computer_indicator.grid(row=0, column=1)
player_indicator.grid(row=0, column=3)

def updateMessage(a):                         #function for final msg
    final_message['text'] = a

def Computer_update():                          # fun for computer score count
    final = int(computer_score['text'])  
    final += 1
    computer_score['text'] = str(final) 

def player_update():                           #for player score count
    final = int(player_score['text'])
    final += 1
    player_score['text'] = str(final)


#main function
def winner_check(p,c):
    if p == c:
        updateMessage("It's a tie")

    elif p == "rock":

        if c =="paper":
            updateMessage("Computer Wins!")
            Computer_update()
        else:
            updateMessage("Player wins!")   
            player_update()
    elif p == "paper":

        if c == "scissor":
            updateMessage("Computer Wins!") 
            Computer_update()
        else:
            updateMessage("Player Wins!")
            player_update()
    elif p == "scissor":

        if c == "rock":
            updateMessage("Compter Wins!")
            Computer_update()
        else:
            updateMessage("Player Win!")
            player_update()   
    else:
        pass         

# we need to update through the images as we used images
to_select = ["rock", "paper", "scissor"]

def choice_update(a):          #from msg_updation a     

    choice_computer = to_select[randint(0,2)]     # rock = 0, p=1, s=2
    if choice_computer == "rock":                    #image assignment
        label_computer.configure(image=image_rock1)
    elif choice_computer == "paper":
        label_computer.configure(image=image_paper1) 
    else:
        label_computer.configure(image=image_scissor1)

    if a == "rock":
        label_player.configure(image=image_rock2)
    elif a == "paper":
        label_player.configure(image=image_paper2) 
    else:
        label_player.configure(image=image_scissor2)                


    winner_check(a, choice_computer)





final_message = Label(window, font=("arial",40,"bold"),bg="red", fg="white")
final_message.grid(row=4, column=2)




button_rock = Button(window, width=16, height=3, text="ROCK",font=("arial",20,"bold"),
                     bg="yellow", fg="red", command=lambda:choice_update("rock")).grid(row=2, column=1)

button_paper = Button(window, width=16, height=3, text="PAPER",font=("arial",20,"bold"),
                      bg="yellow",fg="red", command=lambda:choice_update("paper")).grid(row=2, column=2)

button_scissor = Button(window, width=16, height=3, text="SCISSOR",font=("arial",20,"bold"),
                        bg="yellow",fg="red", command=lambda:choice_update("scissor")).grid(row=2, column=3)

window.mainloop()