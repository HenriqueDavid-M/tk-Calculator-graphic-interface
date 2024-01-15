from tkinter import *
from tkinter import ttk
from tkinter import font
from tkinter.font import BOLD

# CALCULATOR COLORS
color_bg = '#000000'
color_display = '#F0F8FF'
color_keyboard = '#4169E1'
color_numbers = '#000000'
color_number_display = '#000000'

# WINDOW CONFIGURATION
window = Tk()
window.title('Calculadora')
window.geometry('235x310')
window.config(bg=color_bg)

# SCREEN
frame_screen = Frame(window, width=235, height=50, bg=color_display)
frame_screen.grid(row=0, column=0)

# KEYBOARD
frame_keyboard = Frame(window, width=235, height=268, bg=color_bg)
frame_keyboard.grid(row=1, column=0)

text_value = StringVar()
all_values = ''

# FUNCTIONALITY
def enter_values(event):

    global all_values

    all_values=all_values+str(event)
    
    text_value.set(all_values) #passing the value to the screen

# CALCULATE FUNCTION
def calculate():
    result = eval(all_values)
    
    text_value.set(str(result))

# FUNCTION TO CLEAN SCREEN
def clean_screen():
    global all_values
    all_values =''
    text_value.set('')

# LABEL
app_label = Label(frame_screen, textvariable=text_value, width=16, height=2, padx=7, relief=FLAT, anchor='e', justify=RIGHT, font=('Ivy 18'), bg=color_display, fg=color_number_display)
app_label.place(x=0, y=0)

# BUTTONS
b1 = Button(frame_keyboard,command=clean_screen, text='C', width=11, height=2, font=('Ivy 13 bold'), relief=(RAISED), overrelief=RIDGE)
b1.place(x=0, y=0)
b2 = Button(frame_keyboard, command= lambda: enter_values('%'), text='%', width=5, height=2, font=('Ivy 13 bold'), relief=(RAISED), overrelief=RIDGE)
b2.place(x=119, y=0)
b3 = Button(frame_keyboard, command= lambda: enter_values('/'), text='/', width=5, height=2, bg=color_keyboard, fg=color_numbers, font=('Ivy 13 bold'), relief=(RAISED), overrelief=RIDGE)
b3.place(x=177, y=0)
b4 = Button(frame_keyboard, command= lambda: enter_values('7'), text='7', width=5, height=2, font=('Ivy 13 bold'), relief=(RAISED), overrelief=RIDGE)
b4.place(x=0, y=52)
b5 = Button(frame_keyboard, command= lambda: enter_values('8'), text='8', width=5, height=2, font=('Ivy 13 bold'), relief=(RAISED), overrelief=RIDGE)
b5.place(x=60, y=52)
b6 = Button(frame_keyboard, command= lambda: enter_values('9'), text='9', width=5, height=2, font=('Ivy 13 bold'), relief=(RAISED), overrelief=RIDGE)
b6.place(x=119, y=52)
b7 = Button(frame_keyboard, command= lambda: enter_values('*'), text='*', width=5, height=2, bg=color_keyboard, fg=color_numbers, font=('Ivy 13 bold'), relief=(RAISED), overrelief=RIDGE)
b7.place(x=177, y=52)
b8 = Button(frame_keyboard, command= lambda: enter_values('4'), text='4', width=5, height=2, font=('Ivy 13 bold'), relief=(RAISED), overrelief=RIDGE)
b8.place(x=0, y=104)
b9 = Button(frame_keyboard, command= lambda: enter_values('5'), text='5', width=5, height=2, font=('Ivy 13 bold'), relief=(RAISED), overrelief=RIDGE)
b9.place(x=60, y=104)
b10 = Button(frame_keyboard, command= lambda: enter_values('6'), text='6', width=5, height=2, font=('Ivy 13 bold'), relief=(RAISED), overrelief=RIDGE)
b10.place(x=119, y=104)
b11 = Button(frame_keyboard, command= lambda: enter_values('-'), text='-', width=5, height=2, bg=color_keyboard, fg=color_numbers, font=('Ivy 13 bold'), relief=(RAISED), overrelief=RIDGE)
b11.place(x=177, y=104)
b12 = Button(frame_keyboard, command= lambda: enter_values('1'), text='1', width=5, height=2, font=('Ivy 13 bold'), relief=(RAISED), overrelief=RIDGE)
b12.place(x=0, y=156)
b13 = Button(frame_keyboard, command= lambda: enter_values('2'), text='2', width=5, height=2, font=('Ivy 13 bold'), relief=(RAISED), overrelief=RIDGE)
b13.place(x=60, y=156)
b14 = Button(frame_keyboard, command= lambda: enter_values('3'), text='3', width=5, height=2, font=('Ivy 13 bold'), relief=(RAISED), overrelief=RIDGE)
b14.place(x=119, y=156)
b15 = Button(frame_keyboard, command= lambda: enter_values('+'), text='+', width=5, height=2, bg=color_keyboard, fg=color_numbers, font=('Ivy 13 bold'), relief=(RAISED), overrelief=RIDGE)
b15.place(x=177, y=156)
b16 = Button(frame_keyboard, command= lambda: enter_values('0'), text='0', width=5, height=2, font=('Ivy 13 bold'), relief=(RAISED), overrelief=RIDGE)
b16.place(x=0, y=208)
b17 = Button(frame_keyboard, command= lambda: enter_values('.'), text='.', width=5, height=2, font=('Ivy 13 bold'), relief=(RAISED), overrelief=RIDGE)
b17.place(x=60, y=208)
b18 = Button(frame_keyboard, command= calculate, text='=', width=11, height=2, font=('Ivy 13 bold'), relief=(RAISED), overrelief=RIDGE)
b18.place(x=119, y=208)

# VIEW THE CALCULATOR
window.mainloop()