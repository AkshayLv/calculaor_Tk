from tkinter import *
import webbrowser

root = Tk()
root.title("Calculator")
root.geometry("270x440+600+200")
root.resizable(False, False)

operands = [None,None]
op = [None]
textb = Text(root, bd=5, width=19, height=2)
textb_fnt = ("Arial", 17)
textb.configure(font = textb_fnt)
textb.tag_configure("right_align", justify="right")
textb.grid(row=0, column=0, padx=5, pady=10, columnspan=30)

def num_clk(num):
    textb.insert(END,num, "right_align")

def clk_op(n):
    operands.clear()
    operands.append(float(textb.get("1.0",END)))
    textb.delete("1.0",END)
    op.clear()
    op.append(n)

def clk_eq():
    operands.append(float(textb.get("1.0",END)))
    textb.delete("1.0",END)
    if op[0]==1:
        result = operands[0] + operands[1]
    elif op[0]==2:
        result = operands[0] - operands[1]
    elif op[0]==3:
        result = operands[0] * operands[1]
    elif op[0]==4:
        if operands[1]==0:
            result = "Not Defined"
        else:
            result = operands[0] / operands[1]
    else:
        result = 0

    try:
        if result-int(result)!=0:
            textb.insert("1.0",result, "right_align")
        else:
            textb.insert("1.0",int(result), "right_align")

    except ValueError:
        textb.insert("1.0", result, "right_align")
    
def clk_clr():
    textb.delete("1.0",END)
    operands.clear()
    op.clear()

def cred():
    webbrowser.open("https://github.com/AkshayLv", new=2)



b7 = Button(root, text="7", width=10, height = 3, command=lambda: num_clk(7))
b8 = Button(root, text="8", width=10, height = 3, command=lambda: num_clk(8))
b9 = Button(root, text="9", width=10, height = 3, command=lambda: num_clk(9))
b4 = Button(root, text="4", width=10, height = 3, command=lambda: num_clk(4))
b5 = Button(root, text="5", width=10, height = 3, command=lambda: num_clk(5))
b6 = Button(root, text="6", width=10, height = 3, command=lambda: num_clk(6))
b1 = Button(root, text="1", width=10, height = 3, command=lambda: num_clk(1))
b2 = Button(root, text="2", width=10, height = 3, command=lambda: num_clk(2))
b3 = Button(root, text="3", width=10, height = 3, command=lambda: num_clk(3))
b0 = Button(root, text="0", width=10, height = 3, command=lambda: num_clk(0))


b7.grid(row=1, column=0, pady=5, padx=5)
b8.grid(row=1, column=1, pady=5, padx=5)
b9.grid(row=1, column=2, pady=5, padx=5)
b4.grid(row=2, column=0, pady=5, padx=5)
b5.grid(row=2, column=1, pady=5, padx=5)
b6.grid(row=2, column=2, pady=5, padx=5)
b1.grid(row=3, column=0, pady=5, padx=5)
b2.grid(row=3, column=1, pady=5, padx=5)
b3.grid(row=3, column=2, pady=5, padx=5)


b_add = Button(root, text="+", width=4, height = 1, bg = "black", fg = "white", command=lambda:clk_op(1))
b_sub = Button(root, text="-", width=4, height = 1, bg = "black", fg = "white", command=lambda:clk_op(2))
b_mul = Button(root, text="X", width=4, height = 1, bg = "black", fg = "white", command=lambda:clk_op(3))
b_div = Button(root, text="/", width=4, height = 1, bg = "black", fg = "white", command=lambda:clk_op(4))
b_eq = Button(root, text="=", width=10, height = 3, bg = "black", fg = "white", command=lambda:clk_eq())
b_dot = Button(root, text=".", width=10, height = 3, bg = "black", fg = "white", command=lambda:num_clk("."))
b_clr = Button(root, text="CLR", width=10, height = 3, bg = "black", fg = "white", command=lambda:clk_clr())
b_cred = Button(root, text="GIT", width=10, height = 3, bg = "blue", fg = "white", bd=2, command=lambda:cred())


b_add.grid(row=4, column=0, pady=5, padx=5, ipadx=0, ipady=0, sticky=NW)
b0.grid(row=4, column=1, pady=5, padx=5)
b_mul.grid(row=4, column=0, pady=5, padx=5,  ipadx=0, ipady=0, sticky=NE)
b_sub.grid(row=4, column=0, pady=5, padx=5, ipadx=0, ipady=0, sticky=SW)
b_eq.grid(row=5, column=1, pady=5, padx=5)
b_div.grid(row=4, column=0, pady=5, padx=5, ipadx=0, ipady=0, sticky=SE)
b_dot.grid(row=4, column=2, pady=5, padx=5)
b_clr.grid(row=5, column=0, pady=5, padx=5)
b_cred.grid(row=5, column=2, pady=5, padx=5)


root.mainloop()