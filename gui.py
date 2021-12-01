import tkinter as tk
import tkinter.font as tkFont

class App:
    def __init__(self, root):
        #setting title
        root.title("undefined")
        #setting window size
        width=600
        height=500
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)

        GButton_632=tk.Button(root)
        GButton_632["activebackground"] = "#ff5722"
        GButton_632["activeforeground"] = "#000000"
        GButton_632["bg"] = "#efefef"
        ft = tkFont.Font(family='Times',size=10)
        GButton_632["font"] = ft
        GButton_632["fg"] = "#000000"
        GButton_632["justify"] = "center"
        GButton_632["text"] = "Button"
        GButton_632.place(x=500,y=450,width=70,height=25)
        GButton_632["command"] = self.GButton_632_command

        GLabel_650=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_650["font"] = ft
        GLabel_650["fg"] = "#333333"
        GLabel_650["justify"] = "center"
        GLabel_650["text"] = "label"
        GLabel_650.place(x=40,y=30,width=524,height=119)

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

        GLabel_819=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_819["font"] = ft
        GLabel_819["fg"] = "#333333"
        GLabel_819["justify"] = "center"
        GLabel_819["text"] = "label"
        GLabel_819.place(x=40,y=300,width=519,height=52)

        GLabel_676=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_676["font"] = ft
        GLabel_676["fg"] = "#333333"
        GLabel_676["justify"] = "center"
        GLabel_676["text"] = "label"
        GLabel_676.place(x=140,y=360,width=320,height=30)

        GLabel_270=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_270["font"] = ft
        GLabel_270["fg"] = "#333333"
        GLabel_270["justify"] = "center"
        GLabel_270["text"] = "label"
        GLabel_270.place(x=20,y=390,width=233,height=83)

    def GButton_632_command(self):
        print("command")


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
