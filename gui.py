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
        topLabel["text"] = "label"
        topLabel.place(x=40,y=30,width=524,height=119)

        GButton_30=tk.Button(root)
        GButton_30["bg"] = "#efefef"
        ft = tkFont.Font(family='Times',size=10)
        GButton_30["font"] = ft
        GButton_30["fg"] = "#000000"
        GButton_30["justify"] = "center"
        GButton_30["text"] = "Button"
        GButton_30.place(x=40,y=160,width=142,height=128)
        GButton_30["command"] = self.GButton_30_command

        GButton_235=tk.Button(root)
        GButton_235["bg"] = "#efefef"
        ft = tkFont.Font(family='Times',size=10)
        GButton_235["font"] = ft
        GButton_235["fg"] = "#000000"
        GButton_235["justify"] = "center"
        GButton_235["text"] = "Button"
        GButton_235.place(x=230,y=160,width=143,height=127)
        GButton_235["command"] = self.GButton_235_command

        GButton_519=tk.Button(root)
        GButton_519["bg"] = "#efefef"
        ft = tkFont.Font(family='Times',size=10)
        GButton_519["font"] = ft
        GButton_519["fg"] = "#000000"
        GButton_519["justify"] = "center"
        GButton_519["text"] = "Button"
        GButton_519.place(x=420,y=160,width=140,height=126)
        GButton_519["command"] = self.GButton_519_command

        lastGameLabel=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        lastGameLabel["font"] = ft
        lastGameLabel["fg"] = "#333333"
        lastGameLabel["justify"] = "center"
        lastGameLabel["text"] = "label"
        lastGameLabel.place(x=40,y=300,width=519,height=52)

        lastGameMessage=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        lastGameMessage["font"] = ft
        lastGameMessage["fg"] = "#333333"
        lastGameMessage["justify"] = "center"
        lastGameMessage["text"] = "label"
        lastGameMessage.place(x=140,y=360,width=320,height=30)

        currentResult=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        currentResult["font"] = ft
        currentResult["fg"] = "#333333"
        currentResult["justify"] = "center"
        currentResult["text"] = "label"
        currentResult.place(x=20,y=390,width=233,height=83)

    def exitButton_command(self):
        return sys.exit()


    def GButton_30_command(self):
        print("command")


    def GButton_235_command(self):
        print("command")


    def GButton_519_command(self):
        print("command")

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
