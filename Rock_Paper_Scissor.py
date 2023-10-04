# Rock Paper Scissors, 25-July-22

from tkinter import *
import random

root = Tk()
root.title("Rock Paper Scissors")
root.geometry("395x395")
root.configure(bg="#FFD300")


round_number = 0
rounds_to_win = 5

play_score_count = 0
comp_score_count = 0

choice_dict = {"R": "ROCK", "P": "PAPER", "S": "SCISSOR"}


# Functionality:
def brain(player_choices):
    global round_number
    global play_score_count
    global comp_score_count
    global choice_dict

    computer_choices = ["R", "P", "S"]
    computer_choice = random.choice(computer_choices)

    comp_entry.delete(0, END)
    comp_entry.insert(0, choice_dict.get(computer_choice))
    comp_entry.configure(justify=CENTER)
    comp_entry.grid(row=4, column=2, padx=(0, 10), pady=(0, 5), sticky=W + E)

    player_choice = player_choices

    play_entry.delete(0, END)
    play_entry.insert(0, choice_dict.get(player_choice))
    play_entry.configure(justify=CENTER)
    play_entry.grid(row=4, column=0, padx=(10, 0), pady=(0, 5), sticky=W + E)

    round_number += 1
    round_numb = Label(root, text=f"Round: {round_number}", font="Tahoma 10 bold", bg="#FFD300", borderwidth=1, relief=SUNKEN,
                       justify=CENTER)
    round_numb.grid(row=2, column=0, columnspan=3, padx=10, pady=5, sticky=W + E)

    # Player (WIN) Conditions:
    if player_choice == "R" and computer_choice == "S":

        round_rslt.configure(state=NORMAL, justify=CENTER)
        round_rslt.delete(0, END)
        round_rslt.insert(0, "Player Wins")
        round_rslt.grid(row=5, column=0, columnspan=3, padx=10, pady=5, sticky=W + E)
        round_rslt.configure(state=DISABLED)

        play_score_count += 1

        play_track = Entry(root, font="Tahoma 10", bg="#FFD300", justify=CENTER)
        play_track.grid(row=7, column=0, padx=(10, 0), pady=(5, 0), sticky=W + E)
        play_track.insert(0, str(play_score_count))

    elif player_choice == "P" and computer_choice == "R":

        round_rslt.configure(state=NORMAL, justify=CENTER)
        round_rslt.delete(0, END)
        round_rslt.insert(0, "Player Wins")
        round_rslt.grid(row=5, column=0, columnspan=3, padx=10, pady=5, sticky=W + E)
        round_rslt.configure(state=DISABLED)

        play_score_count += 1

        play_track = Entry(root, font="Tahoma 10", bg="#FFD300", justify=CENTER)
        play_track.grid(row=7, column=0, padx=(10, 0), pady=(5, 0), sticky=W + E)
        play_track.insert(0, str(play_score_count))

    elif player_choice == "S" and computer_choice == "P":

        round_rslt.configure(state=NORMAL, justify=CENTER)
        round_rslt.delete(0, END)
        round_rslt.insert(0, "Player Wins")
        round_rslt.grid(row=5, column=0, columnspan=3, padx=10, pady=5, sticky=W + E)
        round_rslt.configure(state=DISABLED)

        play_score_count += 1

        play_track = Entry(root, font="Tahoma 10", bg="#FFD300", justify=CENTER)
        play_track.grid(row=7, column=0, padx=(10, 0), pady=(5, 0), sticky=W + E)
        play_track.insert(0, str(play_score_count))

    elif (player_choice == "R" and computer_choice == "R") or (player_choice == "P" and computer_choice == "P") or (player_choice == "S" and computer_choice == "S"):

        round_rslt.configure(state=NORMAL, justify=CENTER)
        round_rslt.delete(0, END)
        round_rslt.insert(0, "TIE")
        round_rslt.grid(row=5, column=0, columnspan=3, padx=10, pady=5, sticky=W + E)
        round_rslt.configure(state=DISABLED)

    else:

        round_rslt.configure(state=NORMAL, justify=CENTER)
        round_rslt.delete(0, END)
        round_rslt.insert(0, "Computer Wins")
        round_rslt.grid(row=5, column=0, columnspan=3, padx=10, pady=5, sticky=W + E)
        round_rslt.configure(state=DISABLED)

        comp_score_count += 1

        comp_track = Entry(root, font="Tahoma 10", bg="#FFD300", justify=CENTER)
        comp_track.grid(row=7, column=2, padx=(0, 10), pady=(5, 0), sticky=W + E)
        comp_track.insert(0, str(comp_score_count))

    if comp_score_count == rounds_to_win:
        rock_button = Button(root, text="ROCK", font="Tahoma 10 bold", bg="#FFD300", height=2, justify=CENTER,
                             state=DISABLED)
        papr_button = Button(root, text="PAPER", font="Tahoma 10 bold", bg="#FFD300", height=2, justify=CENTER,
                             state=DISABLED)
        scir_button = Button(root, text="SCISSOR", font="Tahoma 10 bold", bg="#FFD300", height=2, justify=CENTER,
                             state=DISABLED)
        rock_button.grid(row=8, column=0, rowspan=2, pady=10, padx=(10, 5), ipadx=12)
        papr_button.grid(row=8, column=1, rowspan=2, pady=10, padx=5, ipadx=9)
        scir_button.grid(row=8, column=2, rowspan=2, pady=10, padx=(5, 10))

        round_rslt.configure(state=NORMAL, justify=CENTER, bg="#FF3131")
        round_rslt.delete(0, END)
        round_rslt.insert(0, "Computer Wins The Game")
        round_rslt.grid(row=5, column=0, columnspan=3, padx=10, pady=5, sticky=W + E)

        start_game = Button(root, text="Rematch", font="Tahoma 10 bold", bg="#FFD300", borderwidth=1, relief=SUNKEN,
                            justify=CENTER, command=start)
        start_game.grid(row=10, column=0, columnspan=3, padx=5, pady=(20, 5), ipadx=10)

    elif play_score_count == rounds_to_win:
        rock_button = Button(root, text="ROCK", font="Tahoma 10 bold", bg="#FFD300", height=2, justify=CENTER,
                             state=DISABLED)
        papr_button = Button(root, text="PAPER", font="Tahoma 10 bold", bg="#FFD300", height=2, justify=CENTER,
                             state=DISABLED)
        scir_button = Button(root, text="SCISSOR", font="Tahoma 10 bold", bg="#FFD300", height=2, justify=CENTER,
                             state=DISABLED)
        rock_button.grid(row=8, column=0, rowspan=2, pady=10, padx=(10, 5), ipadx=12)
        papr_button.grid(row=8, column=1, rowspan=2, pady=10, padx=5, ipadx=9)
        scir_button.grid(row=8, column=2, rowspan=2, pady=10, padx=(5, 10))

        round_rslt.configure(state=NORMAL, justify=CENTER, bg="#39FF14")
        round_rslt.delete(0, END)
        round_rslt.insert(0, "Player Wins The Game")
        round_rslt.grid(row=5, column=0, columnspan=3, padx=10, pady=5, sticky=W + E)

        start_game = Button(root, text="Rematch", font="Tahoma 10 bold", bg="#FFD300", borderwidth=1, relief=SUNKEN,
                            justify=CENTER, command=start)
        start_game.grid(row=10, column=0, columnspan=3, padx=5, pady=(20, 5), ipadx=10)


def start():
    global round_number
    global play_score_count
    global comp_score_count

    round_number = 0
    play_score_count = 0
    comp_score_count = 0

    rock_button = Button(root, text="ROCK", font="Tahoma 10 bold", bg="#FFD300", height=2, justify=CENTER, command=lambda: brain("R"))
    papr_button = Button(root, text="PAPER", font="Tahoma 10 bold", bg="#FFD300", height=2, justify=CENTER, command=lambda: brain("P"))
    scir_button = Button(root, text="SCISSOR", font="Tahoma 10 bold", bg="#FFD300", height=2, justify=CENTER, command=lambda: brain("S"))
    rock_button.grid(row=8, column=0, rowspan=2, pady=10, padx=(10, 5), ipadx=12)
    papr_button.grid(row=8, column=1, rowspan=2, pady=10, padx=5, ipadx=9)
    scir_button.grid(row=8, column=2, rowspan=2, pady=10, padx=(5, 10))

    play_track = Entry(root, font="Tahoma 10", bg="#FFD300", justify=CENTER)
    play_track.insert(0, "0")
    comp_track = Entry(root, font="Tahoma 10", bg="#FFD300", justify=CENTER)
    comp_track.insert(0, "0")
    play_track.grid(row=7, column=0, padx=(10, 0), pady=(5, 0), sticky=W + E)
    comp_track.grid(row=7, column=2, padx=(0, 10), pady=(5, 0), sticky=W + E)

    round_numb = Label(root, text=f"Round: {round_number}", font="Tahoma 10 bold", bg="#FFD300", borderwidth=1,
                       relief=SUNKEN,
                       justify=CENTER)
    round_numb.grid(row=2, column=0, columnspan=3, padx=10, pady=5, sticky=W + E)

    play_entry.delete(0, END)
    comp_entry.delete(0, END)

    play_entry.grid(row=4, column=0, padx=(10, 0), pady=(0, 5), sticky=W + E)
    comp_entry.grid(row=4, column=2, padx=(0, 10), pady=(0, 5), sticky=W + E)

    round_rslt.delete(0, END)
    round_rslt.configure(bg="#FFD300")
    round_rslt.grid(row=5, column=0, columnspan=3, padx=10, pady=5, sticky=W + E)

    start_game = Button(root, text="Start Game ", font="Tahoma 10 bold", bg="#FFD300", borderwidth=1, relief=SUNKEN,
                        justify=CENTER, state=DISABLED)
    start_game.grid(row=10, column=0, columnspan=3, padx=5, pady=(20, 5))


def quit():
    root.quit()


# Layout:

# A. Title:
main_title = Label(root, text="Rock Paper Scissors Game", font="Tahoma 15 bold", bg="#FFD300", fg="#33135C")

# B. Sub-Title:
subb_title = Label(root, text="VS Computer", font="Tahoma 10 underline", bg="#FFD300", fg="#652EC7")

# C. Player:
play_label = Label(root, text="Player", font="Tahoma 10 bold", bg="#FFD300", borderwidth=1, relief=SUNKEN)
play_entry = Entry(root, font="Tahoma 10")

# D. Computer:
comp_label = Label(root, text="Computer", font="Tahoma 10 bold", bg="#FFD300", borderwidth=1, relief=SUNKEN)
comp_entry = Entry(root, font="Tahoma 10")

# E. Score:
play_score = Label(root, text="Player Score", font="Tahoma 10 underline", bg="#FFD300")
comp_score = Label(root, text="Computer Score", font="Tahoma 10 underline", bg="#FFD300")

play_track = Entry(root, font="Tahoma 10", bg="#FFD300", justify=CENTER, state=DISABLED)
comp_track = Entry(root, font="Tahoma 10", bg="#FFD300", justify=CENTER, state=DISABLED)

# F. Buttons:
rock_button = Button(root, text="ROCK", font="Tahoma 10 bold", bg="#FFD300", height=2, justify=CENTER, state=DISABLED)
papr_button = Button(root, text="PAPER", font="Tahoma 10 bold", bg="#FFD300", height=2, justify=CENTER, state=DISABLED)
scir_button = Button(root, text="SCISSOR", font="Tahoma 10 bold", bg="#FFD300", height=2, justify=CENTER, state=DISABLED)

# G. Miscellaneous
versus_lbl = Label(root, text="VS", font="Tahoma 10 bold", bg="#FFD300", borderwidth=1, relief=SUNKEN, justify=CENTER)

to_win_lbl = Label(root, text="To Win", font="Tahoma 10 bold", bg="#FFD300", borderwidth=1, relief=SUNKEN, justify=CENTER)
to_win_set = Label(root, text=f"{rounds_to_win}", font="Tahoma 10", bg="#FFD300", borderwidth=1, relief=SUNKEN, justify=CENTER)

round_numb = Label(root, text="Round: 0", font="Tahoma 10 bold", bg="#FFD300", borderwidth=1, relief=SUNKEN, justify=CENTER)
round_rslt = Entry(root, font="Tahoma 10", bg="#FFD300", borderwidth=1, relief=SUNKEN, state=DISABLED)

start_game = Button(root, text="Start Game ", font="Tahoma 10 bold", bg="#FFD300", borderwidth=1, relief=SUNKEN, justify=CENTER, command=start)
quits_game = Button(root, text=" Quit Game ", font="Tahoma 10 bold", bg="#FFD300", borderwidth=1, relief=SUNKEN, justify=CENTER, command=quit)

# Z. Placing Widgets:
main_title.grid(row=0, column=0, columnspan=3, padx=10, pady=(5, 0), sticky=W+E)
subb_title.grid(row=1, column=0, columnspan=3, padx=60, pady=(0, 5), sticky=W)

round_numb.grid(row=2, column=0, columnspan=3, padx=10, pady=5, sticky=W+E)

play_label.grid(row=3, column=0, padx=(10, 0), pady=(10, 0), sticky=W + E)
play_entry.grid(row=4, column=0, padx=(10, 0), pady=(0, 5), sticky=W + E)

versus_lbl.grid(row=3, column=1, rowspan=2, padx=5, sticky=W+E)

comp_label.grid(row=3, column=2, padx=(0, 10), pady=(10, 0), sticky=W+E)
comp_entry.grid(row=4, column=2, padx=(0, 10), pady=(0, 5), sticky=W+E)

round_rslt.grid(row=5, column=0, columnspan=3, padx=10, pady=5, sticky=W+E)

to_win_lbl.grid(row=6, column=1, padx=5, pady=(5, 0), sticky=W+E)
to_win_set.grid(row=7, column=1, padx=5, pady=(5, 0), sticky=W+E)

play_score.grid(row=6, column=0, padx=(10, 0), pady=(5, 0), sticky=W+E)
comp_score.grid(row=6, column=2, padx=(0, 10), pady=(5, 0), sticky=W+E)

play_track.grid(row=7, column=0, padx=(10, 0), pady=(5, 0), sticky=W+E)
comp_track.grid(row=7, column=2, padx=(0, 10), pady=(5, 0), sticky=W+E)

rock_button.grid(row=8, column=0, rowspan=2, pady=10, padx=(10, 5), ipadx=12)
papr_button.grid(row=8, column=1, rowspan=2, pady=10, padx=5, ipadx=9)
scir_button.grid(row=8, column=2, rowspan=2, pady=10, padx=(5, 10))

start_game.grid(row=10, column=0, columnspan=3, padx=5, pady=(20, 5))
quits_game.grid(row=11, column=0, columnspan=3, padx=5, pady=(5, 5), ipadx=3)

root.mainloop()
