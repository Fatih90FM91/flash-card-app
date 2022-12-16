from tkinter import *
import pandas
import random
BACKGROUND_COLOR = "#B1DDC6"

current_card = {}
to_learn = {}
try:
    data = pandas.read_csv('data/french_words.csv')
except FileNotFoundError:
    original_data = pandas.read_csv('data/french_words.csv')
    to_learn = original_data.to_dict(orient='records')
else:

    to_learn = data.to_dict(orient='records')

print(to_learn)


def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    canvas.itemconfig(lang_title, text='French')
    canvas.itemconfig(lang_word, text=current_card['French'])
    flip_timer = window.after(3000, func=flip_card)


def flip_card():
    global current_card

    new_img = PhotoImage(file='images/card_back.png')
    canvas.itemconfig(canvas_img, image=new_img)
    canvas.itemconfig(lang_title, text='English', fill='white')
    canvas.itemconfig(lang_word, text=current_card['English'], fill='white')


def is_known():
    global current_card
    to_learn.remove(current_card)
    data = pandas.DataFrame(to_learn)
    data.to_csv('data/words_to_learn.csv', index=False)
    next_card()


window = Tk()
window.title('Flash Card App')
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_timer = window.after(3000, func=flip_card)
#


canvas = Canvas(width=800, height=526)
card_image = PhotoImage(file='images/card_front.png')
canvas_img = canvas.create_image(400, 263, image=card_image,)
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
lang_title = canvas.create_text(400, 150, text='title', font=('Ariel', 40, 'italic'))
lang_word = canvas.create_text(400, 263, text='word', font=('Ariel', 40, 'italic'))
canvas.grid(row=0, column=0, columnspan=2)

cross_image = PhotoImage(file='images/wrong.png')
unknown_Btn = Button(image=cross_image, highlightthickness=0, command=next_card)
unknown_Btn.grid(row=1, column=0)

check_image = PhotoImage(file='images/right.png')
right_Btn = Button(image=check_image, highlightthickness=0, command=is_known)
right_Btn.grid(row=1, column=1)


next_card()
window.mainloop()

