# calculator.py 
# written by: Matthew Chute
# last updated: October, 2019

from tkinter import *

class calculator:

    # getInput()
    def getInput(self):
        """
        Takes all values from Entry and stores them into userInput.
        """
        self.userInput = self.entry.get()


    # clearInput()
    def clearInput(self):
        """
        Clears the Entry.
        """
        self.entry.delete(0, END)


    # buttonPress()
    def buttonPress(self, argv):
        """
        Inserts the argument of the button into Entry.
        """
        self.entry.insert(END, argv)


    # evaluate()
    def evaluate(self):
        """
        Uses eval() to evaluate the input.
        Two exceptions:
            1. ZeroDivisionError:   displays "Not a number" to user
            2. SyntaxError:         displays "Input error"
        If eval() is successful, then displays result in Entry.
        """
        self.getInput()
        try:
            self.result = eval(self.userInput)
        except ZeroDivisionError:
            self.entry.delete(0, END)
            self.entry.insert(0, "Not a number")
        except SyntaxError:
            self.entry.delete(0, END)
            self.entry.insert(0, "Input error")
        else:
            self.entry.delete(0, END)
            self.entry.insert(0, self.result)


    # constructor()
    def __init__(self, gui):

        # gui
        gui.title("")
        gui.geometry()

        # entry
        self.entry = Entry(gui, fg = "blue")
        self.entry.grid(row = 0, column = 0, columnspan = 4)

        # buttons:
        # first row 
        buttonAC = Button(gui, text = "AC", width = 17, height = 3, fg = "blue", command = lambda: self.clearInput())
        buttonAC.grid(row = 1, column = 0, columnspan = 3)

        buttonDiv = Button(gui, text = "/", width = 5, height = 3, fg = "blue", command = lambda: self.buttonPress("/"))
        buttonDiv.grid(row = 1, column = 3)

        # second row
        button7 = Button(gui, text = "7", width = 5, height = 3, fg = "blue", command = lambda: self.buttonPress("7"))
        button7.grid(row = 2, column = 0)

        button8 = Button(gui, text = "8", width = 5, height = 3, fg = "blue", command = lambda: self.buttonPress("8"))
        button8.grid(row = 2, column = 1)

        button9 = Button(gui, text = "9", width = 5, height = 3, fg = "blue", command = lambda: self.buttonPress("9"))
        button9.grid(row = 2, column = 2)

        buttonMult = Button(gui, text = "*", width = 5, height = 3, fg = "blue", command = lambda: self.buttonPress("*"))
        buttonMult.grid(row = 2, column = 3)

        # third row
        button4 = Button(gui, text = "4", width = 5, height = 3, fg = "blue", command = lambda: self.buttonPress("4"))
        button4.grid(row = 3, column = 0)

        button5 = Button(gui, text = "5", width = 5, height = 3, fg = "blue", command = lambda: self.buttonPress("5"))
        button5.grid(row = 3, column = 1)

        button6 = Button(gui, text = "6", width = 5, height = 3, fg = "blue", command = lambda: self.buttonPress("6"))
        button6.grid(row = 3, column = 2)

        buttonSub = Button(gui, text = "-", width = 5, height = 3, fg = "blue", command = lambda: self.buttonPress("-"))
        buttonSub.grid(row = 3, column = 3)

        # fourth row
        button1 = Button(gui, text = "1", width = 5, height = 3, fg = "blue", command = lambda: self.buttonPress("1"))
        button1.grid(row = 4, column = 0)

        button2 = Button(gui, text = "2", width = 5, height = 3, fg = "blue", command = lambda: self.buttonPress("2"))
        button2.grid(row = 4, column = 1)

        button3 = Button(gui, text = "3", width = 5, height = 3, fg = "blue", command = lambda: self.buttonPress("3"))
        button3.grid(row = 4, column = 2)

        buttonAdd = Button(gui, text = "+", width = 5, height = 3, fg = "blue", command = lambda: self.buttonPress("+"))
        buttonAdd.grid(row = 4, column = 3)

        # fifth row
        button0 = Button(gui, text = "0", width = 11, height = 3, fg = "blue", command = lambda: self.buttonPress("0"))
        button0.grid(row = 5, column = 0, columnspan = 2)

        buttonDot = Button(gui, text = ".", width = 5, height = 3, fg = "blue", command = lambda: self.buttonPress("."))
        buttonDot.grid(row = 5, column = 2)

        buttonEquals = Button(gui, text = "=", width = 5, height = 3, fg = "blue", command = lambda: self.evaluate())
        buttonEquals.grid(row = 5, column = 3)


# driver
root = Tk()
calculator(root)
root.mainloop()
