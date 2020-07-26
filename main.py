"""
Author - Krish Bista
Date - 23 July 2020
Purpose - Scientific Calculator
"""

# importing stuff
from tkinter import *
import tkinter.messagebox
import math

# some useful variables
font = "Verdana 19 bold"

# Some functions


def all_clear(event):
    textField.delete(0, END)
    return


def clear_last(event):
    textFieldValue.set(textFieldValue.get()[:-1])
    return


def click(event):
    global textFieldValue
    clicked_btn_text = event.widget.cget("text")

    if clicked_btn_text == "x":
        textField.insert(END, "*")
        return

    if clicked_btn_text == '÷':
        textField.insert(END, "/")
        return

    if clicked_btn_text == "=":
        try:
            answer = eval(textFieldValue.get())
            textFieldValue.set(answer)

        except Exception as e:
            tkinter.messagebox.showerror(title="Error", message=e)

        return

    else:
        textFieldValue.set(textFieldValue.get() + clicked_btn_text)


def scientific_calculation(event):
    global textFieldValue
    clicked_btn_text = event.widget.cget("text")
    try:
        if clicked_btn_text == "√":
            answer = math.sqrt(float(textFieldValue.get()))
            textFieldValue.set(answer)

        elif clicked_btn_text == "^":
            base, power = textFieldValue.get().split(',')
            answer = float(base) ** float(power)
            textFieldValue.set(answer)

        elif clicked_btn_text == "a!":
            answer = math.factorial(int(textFieldValue.get()))
            textFieldValue.set(answer)
            return

        elif clicked_btn_text == "° -> c":
            answer = math.radians(float(textFieldValue.get()))
            textFieldValue.set(f"{answer} rad")
            return

        elif clicked_btn_text == "c -> °":
            answer = math.degrees(float(textFieldValue.get()))
            textFieldValue.set(f"{answer}°")
            return

        elif clicked_btn_text == "sin":
            answer = math.sin(math.radians(float(textFieldValue.get())))
            textFieldValue.set(answer)

        elif clicked_btn_text == "cos":
            answer = math.cos(math.radians(float(textFieldValue.get())))
            textFieldValue.set(answer)

        elif clicked_btn_text == "tan":
            answer = math.tan(math.radians(float(textFieldValue.get())))
            textFieldValue.set(answer)

    except Exception as e:
        tkinter.messagebox.showerror(title="Error", message=e)


def scientific_click():
    global normalMode, normalFrame
    normalFrame.pack_forget()
    scientific_frame.pack(side=TOP)
    normalFrame.pack(side=TOP)
    window.geometry("470x700")


def normal_click():
    global scientific_frame
    scientific_frame.pack_forget()
    normalFrame.pack(side=TOP)
    window.geometry("470x600")


def click_enter(event):
    event.widget = equalBtn
    click(event)


# creating a root window
window = Tk()
window.title("Calculator")
window.wm_iconbitmap("images\\calc.png.ico")
window.geometry("470x600")

# creating menu
menuBar = Menu(window)
modeMenu = Menu(menuBar, tearoff=0)
modeMenu.add_command(label="Scientific mode", font=" 12", command=scientific_click)
modeMenu.add_command(label="Normal mode", font=" 12", command=normal_click)
menuBar.add_cascade(label="Mode", menu=modeMenu)
window.config(menu=menuBar)
normalMode = True

# picture label
pic = PhotoImage(file="images\\calc2.png")
Label(window, image=pic).pack(side=TOP, pady=10)


# heading label
Label(window, text="Calculator by Krish Bista", font="Verdana 22 bold", underline=14, fg="royalblue2").pack(side=TOP)


# text field
textFieldValue = StringVar()
textFieldValue.set("")

textField = Entry(window, textvariable=textFieldValue, font="Verdana 22 bold", justify=CENTER, bg="snow2",
                  relief="solid")
textField.pack(side=TOP, pady=9, fill=X, padx=5, ipady=7)


# creating frame
normalFrame = Frame(window, )
normalFrame.pack(side=TOP)


# adding button
temp = 0
for i in range(0, 4):
    for j in range(0, 3):
        btn = Button(normalFrame, text=str(temp), font=font, bg="white", width=5, relief="groove", activebackground="light blue",
                     activeforeground="white")
        btn.grid(row=i, column=j, padx=3, pady=3)
        btn.bind("<Button-1>", click)
        temp += 1


dotBtn = Button(normalFrame, text='.', font=font, bg="white", width=5, relief="groove", activebackground="light blue",
                activeforeground="white")
dotBtn.grid(row=3, column=1, padx=3, pady=3)
dotBtn.bind("<Button-1>", click)

equalBtn = Button(normalFrame, text='=', font=font, bg="purple", width=5, relief="groove", )
equalBtn.grid(row=3, column=3, padx=3, pady=3)
equalBtn.bind("<Button-1>", click)

plusBtn = Button(normalFrame, text='+', font=font, bg="orange red", width=5, relief="groove", )
plusBtn.grid(row=0, column=3, padx=3, pady=3)
plusBtn.bind("<Button-1>", click)

minusBtn = Button(normalFrame, text='-', font=font, bg="orange red", width=5, relief="groove", )
minusBtn.grid(row=1, column=3, padx=3, pady=3)
minusBtn.bind("<Button-1>", click)

multBtn = Button(normalFrame, text='x', font=font, bg="orange red", width=5, relief="groove", )
multBtn.grid(row=2, column=3, padx=3, pady=3)
multBtn.bind("<Button-1>", click)

divBtn = Button(normalFrame, text='÷', font=font, bg="orange red", width=5, relief="groove", )
divBtn.grid(row=3, column=2, padx=3, pady=3)
divBtn.bind("<Button-1>", click)

delBtn = Button(normalFrame, text='DEL', font=font, bg="goldenrod", width=11, relief="solid", )
delBtn.grid(row=4, column=0, padx=3, pady=3, columnspan=2)
delBtn.bind("<Button-1>", clear_last)

allClearBtn = Button(normalFrame, text='AC', font=font, bg="goldenrod", width=11, relief="solid", )
allClearBtn.grid(row=4, column=2, padx=3, pady=3, columnspan=2)
allClearBtn.bind("<Button-1>", all_clear)

window.bind("<Return>", click_enter)
#####################################################################################################
# Code for scientific calculator
scientific_frame = Frame(window)
sqRootBtn = Button(scientific_frame, text='√', font=font, bg="lime", width=5, relief="groove",)
sqRootBtn.grid(row=0, column=0, padx=3, pady=3)
sqRootBtn.bind("<Button-1>", scientific_calculation)

powerBtn = Button(scientific_frame, text='^', font=font, bg="lime", width=5, relief="groove",)
powerBtn.grid(row=0, column=1, padx=3, pady=3)
powerBtn.bind("<Button-1>", scientific_calculation)

factorialBtn = Button(scientific_frame, text='a!', font=font, bg="lime", width=5, relief="groove",)
factorialBtn.grid(row=0, column=2, padx=3, pady=3)
factorialBtn.bind("<Button-1>", scientific_calculation)

radianBtn = Button(scientific_frame, text='° -> c', font=font, bg="lime", width=5, relief="groove",)
radianBtn.grid(row=0, column=3, padx=3, pady=3)
radianBtn.bind("<Button-1>", scientific_calculation)

degreeBtn = Button(scientific_frame, text='c -> °', font=font, bg="lime", width=5, relief="groove",)
degreeBtn.grid(row=1, column=0, padx=3, pady=3)
degreeBtn.bind("<Button-1>", scientific_calculation)

sinBtn = Button(scientific_frame, text='sin', font=font, bg="lime", width=5, relief="groove",)
sinBtn.grid(row=1, column=1, padx=3, pady=3)
sinBtn.bind("<Button-1>", scientific_calculation)

cosBtn = Button(scientific_frame, text='cos', font=font, bg="lime", width=5, relief="groove",)
cosBtn.grid(row=1, column=2, padx=3, pady=3)
cosBtn.bind("<Button-1>", scientific_calculation)

tanBtn = Button(scientific_frame, text='tan', font=font, bg="lime", width=5, relief="groove",)
tanBtn.grid(row=1, column=3, padx=3, pady=3)
tanBtn.bind("<Button-1>", scientific_calculation)

window.mainloop()
