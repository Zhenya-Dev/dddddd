from tkinter import *

root = Tk()
root.geometry('1280x720')
root.title('Sudoku')
root.resizable(False, False)
root['bg'] = '#FAFAFA'

# Difficulty Label
difficulty_selection_label = Label(root, text='Difficulty', font=('IBM Plex Mono', 48, 'bold'), background='#FAFAFA', foreground='#060606')
difficulty_selection_label.place(x=390, y=40, width=500)

# Functions
# Function to handle button clicks
def button_click(difficulty):
    global last_clicked_button
    score_dict={'easy': 2000, 'medium': 5000, 'hard': 8000}
    last_clicked_button = score_dict[difficulty]

def test():
    print(f'Score: {last_clicked_button}')

# Buttons
# Easy
easy_button = Button(root, text='Easy', font=('IBM Plex Mono', 20, 'bold'), background='#FAFAFA', foreground='#0D0C0C',
                     relief='solid', width='18', cursor='target', command=lambda: button_click('easy'))
easy_button.place(x=480, y=250)

# Medium
medium_button = Button(root, text='Medium', font=('IBM Plex Mono', 20, 'bold'), background='#FAFAFA', foreground='#0D0C0C',
                       relief='solid', width='18', cursor='target', command=lambda: button_click('medium'))
medium_button.place(x=480, y=330)

# Hard
hard_button = Button(root, text='Hard', font=('IBM Plex Mono', 20, 'bold'), background='#FAFAFA', foreground='#0D0C0C',
                     relief='solid', width='18', cursor='target', command=lambda: button_click('hard'))
hard_button.place(x=480, y=410)

hard_button = Button(root, text='Test Button', font=('IBM Plex Mono', 20, 'bold'), background='#FAFAFA', foreground='#0D0C0C',
                     relief='solid', width='18', cursor='target', command=test)
hard_button.place(x=480, y=490)

root.mainloop()
