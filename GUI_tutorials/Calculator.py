from tkinter import*
import math

class Calc():
    def __init__(self):
        self.total = 0
        self.current = ""
        self.input_value = True
        self.check_sum = False
        self.op = ""
        self.result = False
        return

    def numberEnter(self, num):
        self.result = False
        firstnum = txtDisplay.get()
        secondnum =str(num)
        if self.input_value:
            self.current = secondnum
            self.input_value = False
        else:
            if secondnum== '.':
                if secondnum in firstnum:
                    return
            self.current = firstnum + secondnum
        self.display(self.current)
        return

    def sum_of_total(self):
        self.result = True
        self.current = float(self.current)
        if self.check_sum == True:
            self.valid_function()
        else:
            self.total = float(txtDisplay.get())
        return

    def valid_function(self):
        if self.op == "add":
            self.total += self.current
        if self.op == "sub":
            self.total -= self.current
        if self.op == "multi":
            self.total *= self.current
        if self.op == "divide":
            self.total /= self.current
        self.input_value = True
        self.check_sum = False
        self.display(self.total)
        return

    def operation(self, op):
        self.current =   float(self.current)
        if self.check_sum:
            self.valid_function()
        elif not self.result:
            self.total = self.current
            self.input_value = True
        self.check_sum = True
        self.op = op
        self.result = False
        return

    def Clear_Entry(self):
            self.result = False
            self.current = "0"
            self.display(0)
            self.input_value = True
            return

    def all_Clear_Entry(self):
            self.Clear_Entry()
            self.total = 0
            return

    def display(self, value):
        txtDisplay.delete(0, END)
        txtDisplay.insert(0, value)
        return

    def opPM(self):
            self.result = False
            self.current = -(float(txtDisplay.get()))
            self.display(self.current)
            return

    def squared(self):
            self.result = False
            self.current = math.sqrt(float(txtDisplay.get()))
            self.display(self.current)
            return


added_value = Calc()
root = Tk()
root.title("Calculator")
root.resizable(width = False, height = False)
calc = Frame(root)
calc.grid()

#**********************************************Row0***************************************************************************************
txtDisplay = Entry(calc, font=('ariel', 20, 'bold'), bg = "powder blue", bd = 30, width = 28, justify = RIGHT)
txtDisplay.grid(row = 0, column = 0, columnspan = 4, pady = 1)
txtDisplay.insert(0, "0")


#**********************************************Row1***************************************************************************************
btnClearEntry = Button(calc, pady=1, bd=4, fg="black", font=('ariel', 20, 'bold'), width = 6, height = 2,
            text="CE", command = added_value.all_Clear_Entry).grid(row = 1, column = 0)
btnClear = Button(calc, pady=1, bd=4, fg="black", font=('ariel', 20, 'bold'), width = 6, height = 2,
            text="C", command = added_value.Clear_Entry).grid(row = 1, column = 1)
btnSqRoot = Button(calc, pady=1, bd=4, fg="black", font=('ariel', 20, 'bold'), width = 6, height = 2,
            text="√", command = added_value.squared).grid(row = 1, column = 2)
btnAdd = Button(calc, pady=1, bd=4, fg="black", font=('ariel', 20, 'bold'), width = 6, height = 2,
            text=chr(43), command = lambda: added_value.operation("add")).grid(row = 1, column = 3)

#**********************************************Row2***************************************************************************************
btn1 = Button(calc, pady=1, bd=4, fg="black", font=('ariel', 20, 'bold'), width = 6, height = 2,
            text="1", bg="powder blue", command = lambda: added_value.numberEnter(1)).grid(row = 2, column = 0)
btn2 = Button(calc, pady=1, bd=4, fg="black", font=('ariel', 20, 'bold'), width = 6, height = 2,
            text="2", bg="powder blue", command = lambda: added_value.numberEnter(2)).grid(row = 2, column = 1)
btn3 = Button(calc, pady=1, bd=4, fg="black", font=('ariel', 20, 'bold'), width = 6, height = 2,
            text="3", bg="powder blue", command = lambda: added_value.numberEnter(3)).grid(row = 2, column = 2)
btnSub = Button(calc, pady=1, bd=4, fg="black", font=('ariel', 20, 'bold'), width = 6, height = 2,
            text=chr(45), command = lambda: added_value.operation("sub")).grid(row = 2, column = 3)

#**********************************************Row3***************************************************************************************
btn4 = Button(calc, pady=1, bd=4, fg="black", font=('ariel', 20, 'bold'), width = 6, height = 2,
            text="4", bg="powder blue", command = lambda: added_value.numberEnter(4)).grid(row = 3, column = 0)
btn5 = Button(calc, pady=1, bd=4, fg="black", font=('ariel', 20, 'bold'), width = 6, height = 2,
            text="5", bg="powder blue", command = lambda: added_value.numberEnter(5)).grid(row = 3, column = 1)
btn6 = Button(calc, pady=1, bd=4, fg="black", font=('ariel', 20, 'bold'), width = 6, height = 2,
            text="6", bg="powder blue", command = lambda: added_value.numberEnter(6)).grid(row = 3, column = 2)
btnMult = Button(calc, pady=1, bd=4, fg="black", font=('ariel', 20, 'bold'), width = 6, height = 2,
            text="x", command = lambda: added_value.operation("multi")).grid(row = 3, column = 3)

#**********************************************Row4***************************************************************************************
btn7 = Button(calc, pady=1, bd=4, fg="black", font=('ariel', 20, 'bold'), width = 6, height = 2,
            text="7", bg="powder blue", command = lambda: added_value.numberEnter(7)).grid(row = 4, column = 0)
btn8 = Button(calc, pady=1, bd=4, fg="black", font=('ariel', 20, 'bold'), width = 6, height = 2,
            text="8", bg="powder blue", command = lambda: added_value.numberEnter(8)).grid(row = 4, column = 1)
btn9 = Button(calc, pady=1, bd=4, fg="black", font=('ariel', 20, 'bold'), width = 6, height = 2,
            text="9", bg="powder blue", command = lambda: added_value.numberEnter(9)).grid(row = 4, column = 2)
btnDiv = Button(calc, pady=1, bd=4, fg="black", font=('ariel', 20, 'bold'), width = 6, height = 2,
            text="÷", command = lambda: added_value.operation("divide")).grid(row = 4, column = 3)

#**********************************************Row5***************************************************************************************
btn0 = Button(calc, pady=1, bd=4, fg="black", font=('ariel', 20, 'bold'), width = 6, height = 2,
            text="0", command = lambda: added_value.numberEnter(0)).grid(row = 5, column = 0)
btnDot = Button(calc, pady=1, bd=4, fg="black", font=('ariel', 20, 'bold'), width = 6, height = 2,
            text=".").grid(row = 5, column = 1)
btnPM = Button(calc, pady=1, bd=4, fg="black", font=('ariel', 20, 'bold'), width = 6, height = 2,
            text=chr(177), command = added_value.opPM).grid(row = 5, column = 2)
btnEquals = Button(calc, pady=1, bd=4, fg="black", font=('ariel', 20, 'bold'), width = 6, height = 2,
            text="=", command = added_value.sum_of_total).grid(row = 5, column = 3)


root.mainloop()
