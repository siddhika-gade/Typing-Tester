from tkinter import *
import tkinter.font as font
import random

score = 0
time = 0
count = 0
missed = 0

def timeFunc():
    global time, score, missed, count
    if count <= 10:
        time += 1
        timer.configure(text=time)
        timer.after(1000, timeFunc)
    else:
        result_label = Label(wn2, text='', font=('arial', 25, 'italic bold'), fg='grey')
        result_label.place(x=230, y=250)
        result_label.configure(text='Time taken = {} \nScore = {} \nMissed = {}'.format(time, score, count - score - 1))
        missed = 0
        score = 0
        time = 0
        count = 0
        next_word_label.destroy()
        user_input.destroy()
        scoreboard_label.destroy()
        timer_label.destroy()
        timer.destroy()

def main_game_score():
    global score, count
    count += 1
    if user_input.get() == next_word_label['text']:
        score += 1
        scoreboard_label.configure(text=score)

    if count < 10:
        random.shuffle(words)
        next_word_label.configure(text=words[0])
        user_input.delete(0, END)
    else:
        timeFunc()

def start_game():
    global wn2, user_input, next_word_label, scoreboard_label, timer_label, timer

    wn2 = Tk()
    wn2.geometry('700x600')
    wn2.title('Typing Test')
    wn2.config(bg='honeydew2')

    next_word_label = Label(wn2, text='Type here', font=('arial', 20, 'italic bold'), fg='black')
    next_word_label.place(x=30, y=240)

    scoreboard_label = Label(wn2, text=score, font=('arial', 25, 'italic bold'), fg='blue')
    scoreboard_label.place(x=100, y=180)

    timer_label = Label(wn2, text=time, font=('arial', 25, 'italic bold'), fg='blue')
    timer_label.place(x=560, y=180)

    user_input = Entry(wn2, font=('arial', 25, 'italic bold'), bd=10, justify='center')
    user_input.place(x=150, y=330)
    user_input.focus_set()

    timer = Label(wn2, text=time, font=('arial', 25, 'italic bold'), fg='blue')
    timer.place(x=560, y=180)

    wn2.bind('<Return>', lambda event: main_game_score())
    wn2.after(1000, timeFunc)
    wn2.mainloop()

# Creating the main window
wn = Tk()
wn.geometry('600x600')
wn.title("Python Typing Test")
wn.config(bg='LightBlue')

heading_frame = Frame(wn, bg="snow3", bd=5)
heading_frame.place(relx=0.2, rely=0.2, relwidth=0.6, relheight=0.16)

heading_label = Label(heading_frame, text="Welcome to Typing Test", bg='azure2', fg='black', font=('Courier', 15, 'bold'))
heading_label.place(relx=0, rely=0, relwidth=1, relheight=1)

btn = Button(wn, text="Start", bg='old lace', fg='black', width=20, height=2, command=start_game)
btn['font'] = font.Font(size=12)
btn.place(x=200, y=300)

words = ["programming", "challenge", "keyboard", "learning", "practice", "developer", "python", "technology", "typing", "interface"]

wn.mainloop()
