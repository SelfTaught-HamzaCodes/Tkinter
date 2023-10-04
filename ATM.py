# ATM (Fast Cash Method), 22-July-22

# Passcode: 1234
# Cash: $100

from tkinter import *

root = Tk()
root.title("Welcome to the ATM")
root.geometry("205x270")
root.configure(bg="#989EA1")

global display_cash
global number_bs_cash

digits_root = []
digits_cash = []


# Functionality to Validate Transaction:
def validation_of_cash():
    global display_cash


    if int(display_cash.get()) == 0:
        display_cash.delete(0, END)
        display_cash.insert(0, "Enter a valid amount.")
    else:
        pass

    if int(display_cash.get()) >= 100:
        display_cash.delete(0, END)
        display_cash.insert(0, "Not Enough Balance")
    else:
        pass

    if 0 < (int(display_cash.get())) <= 100:
        balance = 100 - int(display_cash.get())
        withdrawn = int(display_cash.get())
        display_cash.delete(0, END)
        display_cash.insert(0,
                            f'Transaction Successful, withdrawn: ${withdrawn}, '
                            f'remaining balance: ${balance}')


# Functionality to Cancel Transaction:
def cancel():
    root.quit()


# Functionality for $5, $25, $50
def display_fc_cash(digit):
    global digits_cash
    global display_cash
    global number_bs_cash

    if len(digits_cash) < 1:
        digits_cash.append(digit)
        first = display_cash.get()
        display_cash.delete(0, END)
        display_cash.insert(0, first + str(digit))
    pass

    number_bs_cash = Button(cash, text="<", padx=19, pady=10, bg='#F01E2C', font=('Gotham Light', 10)
                            , command=clear_digit_fc)
    number_bs_cash.grid(row=8, column=0, padx=(5, 1), pady=1)


# Functionality for Fast Cash:
def display_fc(digit):
    global digits_cash
    global display_cash
    global number_bs_cash

    if len(digits_cash) < 2:
        digits_cash.append(digit)
        first = display_cash.get()
        display_cash.delete(0, END)
        display_cash.insert(0, first + str(digit))
    pass

    number_bs_cash = Button(cash, text="<", padx=19, pady=10, bg='#F01E2C', font=('Gotham Light', 10)
                            , command=clear_digit_fc)
    number_bs_cash.grid(row=8, column=0, padx=(5, 1), pady=1)


def clear_digit_fc():
    global digits_cash
    global number_bs_cash
    global display_cash

    digits_cash.pop()
    display_cash.delete(0, END)

    for digit in digits_cash:
        first = display_cash.get()
        display_cash.delete(0, END)
        display_cash.insert(0, first + str(digit))

    if len(digits_cash) == 0:
        number_bs_cash = Button(cash, text="<", padx=19, pady=10, bg='#F01E2C', font=('Gotham Light', 10),
                                state=DISABLED)
        number_bs_cash.grid(row=8, column=0, padx=(5, 1), pady=1)
    else:
        number_bs_cash = Button(cash, text="<", padx=19, pady=10, bg='#F01E2C', font=('Gotham Light', 10)
                                , command=clear_digit_fc)
        number_bs_cash.grid(row=8, column=0, padx=(5, 1), pady=1)


# Functionality for Numbers:
def display_atm(digit):
    global digits_root

    if display.get() == "Invalid, Try Again!":
        digits_root.clear()
        display.delete(0, END)

    if len(digits_root) < 4:
        digits_root.append(digit)
        first = display.get()
        display.delete(0, END)
        display.insert(0, first + str(digit))
    pass

    number_bs = Button(root, text="<", padx=19, pady=10, bg='#F01E2C', font=('Gotham Light', 10)
                       , command=remove_digit)
    number_bs.grid(row=6, column=0, padx=(5, 1), pady=1)


# Functionality for Removing Numbers:
def remove_digit():
    global digits_root

    digits_root.pop()
    display.delete(0, END)

    for digit in digits_root:
        first = display.get()
        display.delete(0, END)
        display.insert(0, first + str(digit))

    if len(digits_root) == 0:
        number_bs = Button(root, text="<", padx=19, pady=10, bg='#F01E2C', font=('Gotham Light', 10), state=DISABLED)
        number_bs.grid(row=6, column=0, padx=(5, 1), pady=1)
    else:
        number_bs = Button(root, text="<", padx=19, pady=10, bg='#F01E2C', font=('Gotham Light', 10)
                           , command=remove_digit)
        number_bs.grid(row=6, column=0, padx=(5, 1), pady=1)


# Functionality for Validating:
def validation_of_passcode():
    global cash
    global display_cash

    if display.get() == "1234":

        root.withdraw()

        cash = Toplevel()
        cash.title("Fast Cash")
        cash.geometry("205x380")
        cash.configure(bg="#989EA1")

        # Label for Title:
        title_cash = Label(cash, text="Fast Cash", font=('Gotham', 12), bg="#989EA1")
        title_cash.grid(row=0, column=0, columnspan=3, padx=5, pady=5)

        # Label for Pincode:
        pincode_cash = Label(cash, text="Enter the amount $:", font=('Gotham Light', 10), bg="#989EA1")
        pincode_cash.grid(row=1, column=0, columnspan=3, padx=10, pady=(5, 0), sticky=W)

        # Entry for Display:
        display_cash = Entry(cash, font=('Gotham', 10), xscrollcommand=INSERT)
        display_cash.grid(row=2, column=0, columnspan=3, padx=10, pady=(0, 5), sticky=W)

        # Buttons for Fast Cash (5, 25, 50):
        cash_05 = Button(cash, text="$05", font=('Gotham', 10), padx=10, pady=20, command=lambda: display_fc_cash(5))
        cash_25 = Button(cash, text="$25", font=('Gotham', 10), padx=10, pady=20, command=lambda: display_fc_cash(25))
        cash_50 = Button(cash, text="$50", font=('Gotham', 10), padx=10, pady=20, command=lambda: display_fc_cash(50))

        cash_05.grid(row=3, column=0, rowspan=2, padx=(7, 4), pady=1)
        cash_25.grid(row=3, column=1, rowspan=2, padx=(5, 5), pady=1)
        cash_50.grid(row=3, column=2, rowspan=2, padx=(5, 5), pady=1)

        # Buttons for Numbers (Passcode Window):
        number_0_cash = Button(cash, text="0", padx=20, pady=10, font=('Gotham Light', 10),
                               command=lambda: display_fc(0))
        number_0_cash.grid(row=8, column=1, padx=(5, 5), pady=1)
        number_1_cash = Button(cash, text="1", padx=22, pady=10, font=('Gotham Light', 10),
                               command=lambda: display_fc(1))
        number_1_cash.grid(row=5, column=0, padx=(5, 1), pady=1)
        number_2_cash = Button(cash, text="2", padx=20, pady=10, font=('Gotham Light', 10),
                               command=lambda: display_fc(2))
        number_2_cash.grid(row=5, column=1, padx=1, pady=1)
        number_3_cash = Button(cash, text="3", padx=20, pady=10, font=('Gotham Light', 10),
                               command=lambda: display_fc(3))
        number_3_cash.grid(row=5, column=2, padx=1, pady=1)
        number_4_cash = Button(cash, text="4", padx=20, pady=10, font=('Gotham Light', 10),
                               command=lambda: display_fc(4))
        number_4_cash.grid(row=6, column=0, padx=(5, 1), pady=1)
        number_5_cash = Button(cash, text="5", padx=20, pady=10, font=('Gotham Light', 10),
                               command=lambda: display_fc(5))
        number_5_cash.grid(row=6, column=1, padx=1, pady=1)
        number_6_cash = Button(cash, text="6", padx=20, pady=10, font=('Gotham Light', 10),
                               command=lambda: display_fc(6))
        number_6_cash.grid(row=6, column=2, padx=1, pady=1)
        number_7_cash = Button(cash, text="7", padx=20, pady=10, font=('Gotham Light', 10),
                               command=lambda: display_fc(7))
        number_7_cash.grid(row=7, column=0, padx=(5, 1), pady=1)
        number_8_cash = Button(cash, text="8", padx=20, pady=10, font=('Gotham Light', 10),
                               command=lambda: display_fc(8))
        number_8_cash.grid(row=7, column=1, padx=1, pady=1)
        number_9_cash = Button(cash, text="9", padx=20, pady=10, font=('Gotham Light', 10),
                               command=lambda: display_fc(9))
        number_9_cash.grid(row=7, column=2, padx=1, pady=1)

        # Button for Backspace / Enter:
        number_bs_cash = Button(cash, text="<", padx=19, pady=10, bg='#F01E2C', font=('Gotham Light', 10),
                                state=DISABLED)
        number_bs_cash.grid(row=8, column=0, padx=(5, 1), pady=1)

        number_e_cash = Button(cash, text="O", padx=19, pady=10, bg='#5DBB63', font=('Gotham Light', 10),
                               command=validation_of_cash)
        number_e_cash.grid(row=8, column=2, padx=(4, 5), pady=1)

        # Button to Cancel Transaction:
        number_c_cash = Button(cash, text="Cancel", padx=69, pady=10, bg='#E0E722', font=('Gotham Light', 10),
                               command=cancel)
        number_c_cash.grid(row=9, column=0, columnspan=3, padx=6, pady=5)

    else:
        display.delete(0, END)
        display.insert(0, "Invalid, Try Again!")


# Label for Title:
title = Label(root, text="Welcome to the ATM", font=('Gotham', 12), bg="#989EA1")
title.grid(row=0, column=0, columnspan=3, padx=5, pady=5)

# Label for Pincode:
pincode = Label(root, text="Enter your pincode:", font=('Gotham Light', 10), bg="#989EA1")
pincode.grid(row=1, column=0, columnspan=3, padx=10, pady=(5, 0), sticky=W)

# Entry for Display:
display = Entry(root, font=('Gotham', 10))
display.grid(row=2, column=0, columnspan=3, padx=10, pady=(0, 5), sticky=W)

# Buttons for Numbers (Passcode Window):
number_0 = Button(root, text="0", padx=20, pady=10, font=('Gotham Light', 10), command=lambda: display_atm(0))
number_0.grid(row=6, column=1, padx=(5, 5), pady=1)
number_1 = Button(root, text="1", padx=22, pady=10, font=('Gotham Light', 10), command=lambda: display_atm(1))
number_1.grid(row=3, column=0, padx=(5, 1), pady=1)
number_2 = Button(root, text="2", padx=20, pady=10, font=('Gotham Light', 10), command=lambda: display_atm(2))
number_2.grid(row=3, column=1, padx=1, pady=1)
number_3 = Button(root, text="3", padx=20, pady=10, font=('Gotham Light', 10), command=lambda: display_atm(3))
number_3.grid(row=3, column=2, padx=1, pady=1)
number_4 = Button(root, text="4", padx=20, pady=10, font=('Gotham Light', 10), command=lambda: display_atm(4))
number_4.grid(row=4, column=0, padx=(5, 1), pady=1)
number_5 = Button(root, text="5", padx=20, pady=10, font=('Gotham Light', 10), command=lambda: display_atm(5))
number_5.grid(row=4, column=1, padx=1, pady=1)
number_6 = Button(root, text="6", padx=20, pady=10, font=('Gotham Light', 10), command=lambda: display_atm(6))
number_6.grid(row=4, column=2, padx=1, pady=1)
number_7 = Button(root, text="7", padx=20, pady=10, font=('Gotham Light', 10), command=lambda: display_atm(7))
number_7.grid(row=5, column=0, padx=(5, 1), pady=1)
number_8 = Button(root, text="8", padx=20, pady=10, font=('Gotham Light', 10), command=lambda: display_atm(8))
number_8.grid(row=5, column=1, padx=1, pady=1)
number_9 = Button(root, text="9", padx=20, pady=10, font=('Gotham Light', 10), command=lambda: display_atm(9))
number_9.grid(row=5, column=2, padx=1, pady=1)

# Button for Backspace / Enter:
number_bs = Button(root, text="<", padx=19, pady=10, bg='#F01E2C', font=('Gotham Light', 10), state=DISABLED)
number_bs.grid(row=6, column=0, padx=(5, 1), pady=1)

number_e = Button(root, text="O", padx=19, pady=10, bg='#5DBB63', font=('Gotham Light', 10),
                  command=validation_of_passcode)
number_e.grid(row=6, column=2, padx=(4, 5), pady=1)

root.mainloop()



