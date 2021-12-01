import tkinter as tk
import tkinter.font as tkFont
import sys


class App:
    def __init__(self, root):
        #setting title
        root.title("Game of Rock, Paper, Scissors")
        #setting window size
        width=600
        height=500
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)

        exitButton=tk.Button(root)
        exitButton["activebackground"] = "#ff5722"
        exitButton["activeforeground"] = "#000000"
        exitButton["bg"] = "red"
        ft = tkFont.Font(family='Times',size=10)
        exitButton["font"] = ft
        exitButton["fg"] = "#000000"
        exitButton["justify"] = "center"
        exitButton["text"] = "Exit"
        exitButton.place(x=500,y=450,width=70,height=25)
        exitButton["command"] = self.exitButton_command

        topLabel=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        topLabel["font"] = ft
        topLabel["fg"] = "#333333"
        topLabel["justify"] = "center"
        topLabel["text"] = "Compete against the machines and do not allow them to take over the world!\nThe humanity is counting on you soldier!"
        topLabel.place(x=40,y=30,width=524,height=119)

        rockButton=tk.Button(root)
        rockButton["bg"] = "#efefef"
        ft = tkFont.Font(family='Times',size=10)
        rockButton["font"] = ft
        rockButton["fg"] = "#000000"
        rockButton["justify"] = "center"
        rockButton["text"] = "Try hit them with a rock!"
        rockButton.place(x=40,y=160,width=142,height=128)
        rockButton["command"] = self.rockButton_command

        paperButton=tk.Button(root)
        paperButton["bg"] = "#efefef"
        ft = tkFont.Font(family='Times',size=10)
        paperButton["font"] = ft
        paperButton["fg"] = "#000000"
        paperButton["justify"] = "center"
        paperButton["text"] = "Who said the pen is\nmightier than the sword?!"
        paperButton.place(x=230,y=160,width=143,height=127)
        paperButton["command"] = self.paperButton_command

        scissorsButton=tk.Button(root)
        scissorsButton["bg"] = "#efefef"
        ft = tkFont.Font(family='Times',size=10)
        scissorsButton["font"] = ft
        scissorsButton["fg"] = "#000000"
        scissorsButton["justify"] = "center"
        scissorsButton["text"] = "Ok, time to\ncut some cabels."
        scissorsButton.place(x=420,y=160,width=140,height=126)
        scissorsButton["command"] = self.scissorsButton_command

        lastGameLabel=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        lastGameLabel["font"] = ft
        lastGameLabel["fg"] = "#333333"
        lastGameLabel["justify"] = "center"
        lastGameLabel["text"] = "Print the result"
        lastGameLabel.place(x=40,y=300,width=519,height=52)

        lastGameMessage=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        lastGameMessage["font"] = ft
        lastGameMessage["fg"] = "#333333"
        lastGameMessage["justify"] = "center"
        lastGameMessage["text"] = "Here the player will get a message as result from the last round."
        lastGameMessage.place(x=100,y=360,width=400,height=30)

        currentResult=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        currentResult["font"] = ft
        currentResult["bg"] = 'white'
        currentResult["fg"] = "#333333"
        currentResult["justify"] = "center"
        currentResult["text"] = "Current result"
        currentResult.place(x=10,y=390,width=150,height=83)

    def exitButton_command(self):
        return sys.exit()


    def rockButton_command(self):
        print("command")


    def paperButton_command(self):
        print("command")


    def scissorsButton_command(self):
        print("command")

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
