# Calculator 1.0, 16-July-22

from tkinter import *

root = Tk()
root.title("Calculator")
root.geometry("235x280")
root.configure(bg="#D3D3D3")


# Functionality


# Display Numbers on Display
def display_calculator(number):
    first = display.get()
    display.delete(0, END)
    display.insert(0, first + str(number))


# Clear our Display
def clear_display_calculator():
    global number_02
    global number_01
    number_01 = 0
    number_02 = 0
    display.delete(0, END)


# Add Button - Functionality
def add():
    global number_01
    global math
    math = "add"
    number_01 = int(display.get())
    display.delete(0, END)


# Subtract Button - Functionality
def subtract():
    global number_01
    global math
    math = "subtract"
    number_01 = int(display.get())
    display.delete(0, END)


# Multiplication Button - Functionality
def multiply():
    global number_01
    global math
    math = "multiply"
    number_01 = int(display.get())
    display.delete(0, END)


# Division Button - Functionality
def divide():
    global number_01
    global math
    math = "divide"
    number_01 = int(display.get())
    display.delete(0, END)


# Equal Button - Functionality
def equal_to():
    global number_01
    global math

    number_02 = int(display.get())
    display.delete(0, END)

    if math == "add":
        display.insert(0, number_01 + number_02)
    if math == "subtract":
        display.insert(0, number_01 - number_02)
    if math == "multiply":
        display.insert(0, number_01 * number_02)
    if math == "divide":
        display.insert(0, number_01 / number_02)


# Layout for our Calculator.


# Calling / Implementation of Buttons:
display = Entry(root, width=30, borderwidth=5)
display.grid(row=0, column=0, columnspan=5, padx=10, pady=(10, 0))

equal = Button(root, text="=", padx=77, pady=10, command=equal_to)
equal.grid(row=5, column=0, columnspan=3, padx=(5, 1), pady=1)

addition = Button(root, text="+", padx=17, pady=34, font=("Arial", 10), command=add)
addition.grid(row=4, column=4, rowspan=2, padx=1, pady=1)

subtract = Button(root, text="-", padx=19, pady=10, font=("Arial", 10), command=subtract)
subtract.grid(row=3, column=4, padx=1, pady=1)

multiply = Button(root, text="*", padx=19, pady=10, font=("Arial", 10), command=multiply)
multiply.grid(row=2, column=4, padx=1, pady=1)

divide = Button(root, text="/", padx=19, pady=10, font=("Arial", 10), command=divide)
divide.grid(row=1, column=4, padx=1, pady=1)

clear = Button(root, text="Reset", padx=38, pady=10, command=clear_display_calculator)
clear.grid(row=4, column=1, columnspan=2, padx=2, pady=2)

number_0 = Button(root, text="0", padx=20, pady=10, command=lambda: display_calculator(0))
number_0.grid(row=4, column=0, padx=(5, 1), pady=1)
number_1 = Button(root, text="1", padx=20, pady=10, command=lambda: display_calculator(1))
number_1.grid(row=3, column=0, padx=(5, 1), pady=1)
number_2 = Button(root, text="2", padx=20, pady=10, command=lambda: display_calculator(2))
number_2.grid(row=3, column=1, padx=1, pady=1)
number_3 = Button(root, text="3", padx=20, pady=10, command=lambda: display_calculator(3))
number_3.grid(row=3, column=2, padx=1, pady=1)
number_4 = Button(root, text="4", padx=20, pady=10, command=lambda: display_calculator(4))
number_4.grid(row=2, column=0, padx=(5, 1), pady=1)
number_5 = Button(root, text="5", padx=20, pady=10, command=lambda: display_calculator(5))
number_5.grid(row=2, column=1, padx=1, pady=1)
number_6 = Button(root, text="6", padx=20, pady=10, command=lambda: display_calculator(6))
number_6.grid(row=2, column=2, padx=1, pady=1)
number_7 = Button(root, text="7", padx=20, pady=10, command=lambda: display_calculator(7))
number_7.grid(row=1, column=0, padx=(5, 1), pady=1)
number_8 = Button(root, text="8", padx=20, pady=10, command=lambda: display_calculator(8))
number_8.grid(row=1, column=1, padx=1, pady=1)
number_9 = Button(root, text="9", padx=20, pady=10, command=lambda: display_calculator(9))
number_9.grid(row=1, column=2, padx=1, pady=1)

root.mainloop()
