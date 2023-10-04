# Dice Rolling Simulator, 22-July-22

from tkinter import *
import random

# Root Settings
root = Tk()
root.title("Dice Rolling Simulator")
root.geometry("220x175")


# list to store numbers rolled.
rolled = [0]


# __Functionality__
def rolling():
    roll = random.randint(1, 6)

    rolled.append(roll)

    display.delete(0, END)
    display.insert(0, str(roll))

    Label(root, text=rolled[-2], font='Tahoma 10 bold').grid(row=4, column=0, sticky=W+E, padx=10)

# __Layout__


# Title for D.R.S:
title = Label(root, text="Dice Rolling Simulator", font=('Tahoma', 15))
title.grid(row=0, column=0, sticky=W+E, padx=10, pady=10)

# Display for D.R.S:
display = Entry(root, font=('Tahoma', 10), justify=CENTER)
display.grid(row=1, column=0, sticky=W+E, padx=10, pady=5)

# Button for D.R.S (to roll):
roll_button = Button(root, text="Roll", font=('Tahoma', 10), command=rolling)
roll_button.grid(row=2, column=0, sticky=W+E, padx=10, pady=5)

# Last Number Rolled, Title:
last_number_rolled = Label(root, text="Last Number Rolled", font='Tahoma 10 underline')
last_number_rolled.grid(row=3, column=0, sticky=W+E, padx=10, pady=(5, 0))

root.mainloop()
