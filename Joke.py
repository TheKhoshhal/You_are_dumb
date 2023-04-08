import tkinter as tk
import random


def change_position():
    btn_no.place_forget()
    
    no_y = random.randint(60, 250)
    no_x = random.randint(125, 300)
    btn_no.place(x=no_x, y=no_y)

def i_knew_it():
    lbl_question.place_forget()
    btn_no.place_forget()
    btn_yes.place_forget()
    
    lbl_joke.place(x=115, y=60)

win = tk.Tk()
win.resizable(0, 0)
win.title(":)))")

Frm_question = tk.Frame(master=win, width=350, height=300)
Frm_question.pack()

lbl_question = tk.Label(master=Frm_question, text="Are you Dumb?", font=("Gadugi", 15), fg="black")
lbl_question.place(x=110, y=50)

btn_yes = tk.Button(master=Frm_question, text="yes", font=("Gadugi", 10), fg="#3B2F2F", cursor="hand2", height=1, width=4, command=lambda:i_knew_it())
btn_no = tk.Button(master=Frm_question, text="no", font=("Gadugi", 10), fg="#3B2F2F", cursor="hand2", height=1, width=4, command=lambda:change_position())

btn_yes.place(x=115, y=200)
btn_no.place(x=195, y=200)

lbl_joke = tk.Label(master=Frm_question, text="I knew it :3", font=("Gadugi", 16), fg="#2C3539")

win.mainloop()
