from tkinter import*
import math
import parser
import tkinter.messagebox

root = Tk()
root.title("Scientific Calculator")
root.configure(background="powder blue")
root.resizable(width =False, height=False)
root.geometry("594x510+0+0")

calc = Frame(root)
calc.grid()

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
        
        def display(self, value):
                txtDisplay.delete(0, END)
                txtDisplay.insert(0, value)

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
                if self.op == "Mod":
                        self.total %= self.current
                self.input_value = True
                self.check_sum = False
                self.display(self.total)
                return

        def operation(self, op):
                self.current = float(self.current)
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

        def pi(self):
                self.result = False
                self.current = math.pi
                self.display(self.current)

        def tau(self):
                self.result = False
                self.current = math.tau
                self.display(self.current)

        def e(self):
                self.result = False
                self.current = math.e
                self.display(self.current)

        def cos(self):
                self.result = False
                self.current = math.cos(math.radians(float(txtDisplay.get())))
                self.display(self.current)

        def cosh(self):
                self.result = False
                self.current = math.cosh(math.radians(float(txtDisplay.get())))
                self.display(self.current)

        def tan(self):
                self.result = False
                self.current = math.tan(math.radians(float(txtDisplay.get())))
                self.display(self.current)
        
        def tanh(self):
                self.result = False
                self.current = math.tanh(math.radians(float(txtDisplay.get())))
                self.display(self.current)

        def sin(self):
                self.result = False
                self.current = math.sin(math.radians(float(txtDisplay.get())))
                self.display(self.current)

        def sinh(self):
                self.result = False
                self.current = math.sinh(math.radians(float(txtDisplay.get())))
                self.display(self.current)

        def log(self):
                self.result = False
                self.current = math.log(float(txtDisplay.get()))
                self.display(self.current)

        def exp(self):
                self.result = False
                self.current = math.exp(float(txtDisplay.get()))
                self.display(self.current)

        def acosh(self):
                self.result = False
                self.current = math.acosh(float(txtDisplay.get()))
                self.display(self.current)

        def asinh(self):
                self.result = False
                self.current = math.asinh(float(txtDisplay.get()))
                self.display(self.current)

        def expm1(self):
                self.result = False
                self.current = math.expm1(float(txtDisplay.get()))
                self.display(self.current)

        def lgamma(self):
                self.result = False
                self.current = math.lgamma(float(txtDisplay.get()))
                self.display(self.current)

        def deg(self):
                self.result = False
                self.current = math.degrees(float(txtDisplay.get()))
                self.display(self.current)

        def log2(self):
                self.result = False
                self.current = math.log2(float(txtDisplay.get()))
                self.display(self.current)

        def log10(self):
                self.result = False
                self.current = math.log10(float(txtDisplay.get()))
                self.display(self.current)

        def log1p(self):
                self.result = False
                self.current = math.log1p(float(txtDisplay.get()))
                self.display(self.current)

        

added_value = Calc()

#*****************************************************Row 0(Display)******************************************************************

txtDisplay = Entry(calc, font=('ariel',20,'bold'), bg="powder blue", bd=30, width=28, justify=RIGHT)
txtDisplay.grid(row=0, column=0, columnspan=4,pady=1)
txtDisplay.insert(0, "0")

#*****************************************************numpad algorithm******************************************************************

numberpad = "123456789"
i = 0
btn = []
for j in range(2,5):
    for k in range(3):
        btn.append(Button(calc, width=6, height=2, font=('ariel',20,'bold'), bd =4, text = numberpad[i]))
        btn[i].grid(row = j, column =k, pady=1)
        btn[i]["command"] = lambda x = numberpad[i]: added_value.numberEnter(x)
        i += 1

#***************************************************************Operators**************************************************************************

btnClearEntry = Button(calc, pady=1, bg= "powder blue", bd=4, fg="black", font=('ariel', 20, 'bold'), width = 6, height = 2,
            text="CE", command = added_value.all_Clear_Entry).grid(row = 1, column = 0)
btnClear = Button(calc, pady=1, bg= "powder blue", bd=4, fg="black", font=('ariel', 20, 'bold'), width = 6, height = 2,
            text="C", command = added_value.Clear_Entry).grid(row = 1, column = 1, pady=1)
btnSqRoot = Button(calc, pady=1, bg= "powder blue", bd=4, fg="black", font=('ariel', 20, 'bold'), width = 6, height = 2,
            text="√", command = added_value.squared).grid(row = 1, column = 2)
btnAdd = Button(calc, pady=1, bg= "powder blue", bd=4, fg="black", font=('ariel', 20, 'bold'), width = 6, height = 2,
            text=chr(43), command = lambda: added_value.operation("add")).grid(row = 1, column = 3)
btnSub = Button(calc, pady=1, bg= "powder blue", bd=4, fg="black", font=('ariel', 20, 'bold'), width = 6, height = 2,
            text=chr(45), command = lambda: added_value.operation("sub")).grid(row = 2, column = 3)
btnMult = Button(calc, pady=1, bg= "powder blue", bd=4, fg="black", font=('ariel', 20, 'bold'), width = 6, height = 2,
            text="x", command = lambda: added_value.operation("multi")).grid(row = 3, column = 3)
btnDiv = Button(calc, pady=1, bg= "powder blue", bd=4, fg="black", font=('ariel', 20, 'bold'), width = 6, height = 2,
            text="÷", command = lambda: added_value.operation("divide")).grid(row = 4, column = 3)

#**********************************************Row5********************************************************************
btn0 = Button(calc, pady=1, bg= "powder blue", bd=4, fg="black", font=('ariel', 20, 'bold'), width = 6, height = 2,
            text="0", command = lambda: added_value.numberEnter(0)).grid(row = 5, column = 0)
btnDot = Button(calc, pady=1, bg= "powder blue", bd=4, fg="black", font=('ariel', 20, 'bold'), width = 6, height = 2,
            text=".", command = lambda: added_value.numberEnter('.')).grid(row = 5, column = 1)
btnPM = Button(calc, pady=1, bg= "powder blue", bd=4, fg="black", font=('ariel', 20, 'bold'), width = 6, height = 2,
            text=chr(177), command = added_value.opPM).grid(row = 5, column = 2)
btnEquals = Button(calc, pady=1, bg= "powder blue", bd=4, fg="black", font=('ariel', 20, 'bold'), width = 6, height = 2,
            text="=", command = added_value.sum_of_total).grid(row = 5, column = 3)


#**********************************************Scientific Calculator*************************************************************************
#*****************************************************************************************************************************
btnPi = Button(calc, pady=1, bg= "powder blue", bd=4, fg="black", font=('ariel', 20, 'bold'), width = 6, height = 2,
            text="π", command = added_value.pi).grid(row = 1, column = 4)
btnCos = Button(calc, pady=1, bg= "powder blue", bd=4, fg="black", font=('ariel', 20, 'bold'), width = 6, height = 2,
            text="cos", command = added_value.cos).grid(row = 1, column = 5, pady=1)
btntan = Button(calc, pady=1, bg= "powder blue", bd=4, fg="black", font=('ariel', 20, 'bold'), width = 6, height = 2,
            text="tan", command = added_value.tan).grid(row = 1, column = 6)
btnsin = Button(calc, pady=1, bg= "powder blue", bd=4, fg="black", font=('ariel', 20, 'bold'), width = 6, height = 2,
            text="sin", command = added_value.sin).grid(row = 1, column = 7)

#****************************************************************************************************************************
btn2Pi = Button(calc, pady=1, bg= "powder blue", bd=4, fg="black", font=('ariel', 20, 'bold'), width = 6, height = 2,
            text="2π", command = added_value.tau).grid(row = 2, column = 4)
btnCosh = Button(calc, pady=1, bd=4, fg="black", font=('ariel', 20, 'bold'), width = 6, height = 2,
            text="cosh", command = added_value.cosh).grid(row = 2, column = 5, pady=1)
btntanh = Button(calc, pady=1, fg="black", font=('ariel', 20, 'bold'), width = 6, height = 2,
            text="tanh", command = added_value.tanh).grid(row = 2, column = 6)
btnsinh = Button(calc, pady=1, bd=4, fg="black", font=('ariel', 20, 'bold'), width = 6, height = 2,
            text="sinh", command = added_value.sinh).grid(row = 2, column = 7)

#****************************************************************************************************************************
btnlog = Button(calc, pady=1, bg= "powder blue", bd=4, fg="black", font=('ariel', 20, 'bold'), width = 6, height = 2,
            text="log", command = added_value.log).grid(row = 3, column = 4)
btnExp = Button(calc, pady=1, bd=4, fg="black", font=('ariel', 20, 'bold'), width = 6, height = 2,
            text="Exp", command = added_value.exp).grid(row = 3, column = 5, pady=1)
btnMod = Button(calc, pady=1, bd=4, fg="black", font=('ariel', 20, 'bold'), width = 6, height = 2,
            text="Mod", command = lambda: added_value.operation("Mod")).grid(row = 3, column = 6)
btnE = Button(calc, pady=1, bd=4, fg="black", font=('ariel', 20, 'bold'), width = 6, height = 2,
            text="e", command = added_value.e).grid(row = 3, column = 7)

#*************************************************************************************************************************
btnlog2 = Button(calc, pady=1, bg= "powder blue", bd=4, fg="black", font=('ariel', 20, 'bold'), width = 6, height = 2,
            text="log2", command = added_value.log2).grid(row = 4, column = 4)
btndeg = Button(calc, pady=1, bd=4, fg="black", font=('ariel', 20, 'bold'), width = 6, height = 2,
            text="deg", command = added_value.deg).grid(row = 4, column = 5, pady=1)
btnacosh = Button(calc, pady=1, bd=4, fg="black", font=('ariel', 20, 'bold'), width = 6, height = 2,
            text="acosh", command = added_value.acosh).grid(row = 4, column = 6)
btnasinh = Button(calc, pady=1, bd=4, fg="black", font=('ariel', 20, 'bold'), width = 6, height = 2,
            text="asinh", command = added_value.asinh).grid(row = 4, column = 7)


#****************************************************************************************************************************
btnlog10 = Button(calc, pady=1, bg= "powder blue", bd=4, fg="black", font=('ariel', 20, 'bold'), width = 6, height = 2,
            text="log10", command = added_value.log10).grid(row = 5, column = 4)
btnlog1p = Button(calc, pady=1, bg= "powder blue", bd=4, fg="black", font=('ariel', 20, 'bold'), width = 6, height = 2,
            text="log1p", command = added_value.log1p).grid(row = 5, column = 5, pady=1)
btnexpm1 = Button(calc, pady=1, bg= "powder blue", bd=4, fg="black", font=('ariel', 20, 'bold'), width = 6, height = 2,
            text="expm1", command = added_value.expm1).grid(row = 5, column = 6)
btnlgamma = Button(calc, pady=1, bg= "powder blue", bd=4, fg="black", font=('ariel', 20, 'bold'), width = 6, height = 2,
            text="lgamma", command = added_value.lgamma).grid(row = 5, column = 7)


lblDisplay= Label(calc, text="Scientific Calculator", font=('ariel', 30, 'bold'), justify=CENTER)
lblDisplay.grid(row=0, column=4, columnspan=4)

#*****************************************************Menu and function******************************************************************

def iExit():
    iExit = tkinter.messagebox.askyesno("Scientific Calculator", "Confirm if you want to exit")
    if iExit > 0:
        root.destroy()
        return

def Scientific():
    root.resizable(width =False, height=False)
    root.geometry("1190x510+0+0")

def Standard():
    root.resizable(width =False, height=False)
    root.geometry("594x510+0+0")

menubar = Menu(calc)

filemenu = Menu(menubar, tearoff = 0)
menubar.add_cascade(label = "File", menu =filemenu)
filemenu.add_command(label = "Standard", command = Standard)
filemenu.add_command(label = "Scientific", command = Scientific)
filemenu.add_separator()
filemenu.add_command(label = "Exit", command = iExit)

editmenu = Menu(menubar, tearoff = 0)
menubar.add_cascade(label = "Edit", menu =editmenu)
editmenu.add_command(label = "Cut")
editmenu.add_command(label = "Copy")
editmenu.add_separator()
editmenu.add_command(label = "Exit")

helpmenu = Menu(menubar, tearoff = 0)
menubar.add_cascade(label = "Help", menu =helpmenu)
helpmenu.add_command(label = "View Help")

root.config(menu=menubar)
root.mainloop()