# Multiplication Table, 17-July-22

from tkinter import *

root = Tk()
root.title("Multiplication Table")
root.geometry("240x300")


answers = []


# __Functionality__
def generator(number, till):

    current_limit = 0

    for limit in range(int(till)):
        current_limit += 1

        number_table = int(number) * current_limit

        the_table = Label(root, text=f'{current_limit}) {number} x {current_limit} = {number_table}')
        the_table.grid(row=5 + current_limit, sticky=W + E, columnspan=2)

        answers.append(the_table)


def clear_content(answers):
    for label in answers.copy():
        label.destroy()
        answers.remove(label)

    number_table_get.delete(0, END)
    number_table_till_get.delete(0, END)


# __Layout__


# Heading:
heading = Label(root, text="Number Table Generator", font=("Tahoma", 15))
heading.grid(row=0, column=0, columnspan=2, sticky=W, padx=(5, 0))

# Number Table:
number_table = Label(root, text="Number: ", font=("Tahoma", 10))
number_table.grid(row=1, column=0, sticky=W, padx=(5, 0))

number_table_get = Entry(root, font=("Tahoma", 10), width=20, borderwidth=2)
number_table_get.grid(row=1, column=1, sticky=W)

# Number Table (till):
number_table_till = Label(root, text="Till: ", font=("Tahoma", 10))
number_table_till.grid(row=2, column=0, sticky=W, padx=(5, 0))

number_table_till_get = Entry(root, font=("Tahoma", 10), width=20, borderwidth=2)
number_table_till_get.grid(row=2, column=1, sticky=W)

# Generate Table (Button):
generate_table = Button(root, text="Generate Table", font=("Tahoma", 10),
                        command=lambda: generator(number_table_get.get(), number_table_till_get.get()))
generate_table.grid(row=3, column=0, columnspan=2, sticky=W + E, padx=(5, 0))

# Clear Contents (Button):
generate_table = Button(root, text="Clear", font=("Tahoma", 10), command=lambda: clear_content(answers))
generate_table.grid(row=4, column=0, columnspan=2, sticky=W + E, padx=(5, 0))

root.mainloop()
