from textblob import TextBlob
from tkinter import *

def correct_spelling():
    get_data = enter1.get()
    corr = TextBlob(get_data)
    data = corr.correct()
    enter2.delete(0, END)
    enter2.insert(0, data)

def main_window():
    global enter1, enter2
    win = Tk()
    win.geometry("500x370")
    win.resizable(False, False)
    win.config(bg="blue")
    win.title("Wscube Tech")

    label1 = Label(win, text="Incorrect Spelling", font=("Times New Roman", 25, "bold"), bg="black", fg="white")
    label1.place(x=100, y=20, height=50, width=300)

    enter1 = Entry(win, font=("Times New Roman", 25))
    enter1.place(x=50, y=80, height=50, width=400)

    label2 = Label(win, text="Correct Spelling", font=("Times New Roman", 25, "bold"), bg="black", fg="white")
    label2.place(x=100, y=140, height=50, width=300)

    enter2 = Entry(win, font=("Times New Roman", 25))
    enter2.place(x=50, y=200, height=50, width=400)

    done_button = Button(win, text="Done", font=("Times New Roman", 25, "bold"), bg="yellow", command=correct_spelling)
    done_button.place(x=150, y=280, height=50, width=200)  # Changed Button to done_button

    win.mainloop()

main_window()

