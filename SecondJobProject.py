import tkinter as tk
from tkinter import messagebox
#bind - привязать

def add_digit(digit):
    value = calc.get()
    if value[0] == '0' and len(value) == 1:
        value = value[1:]
    calc.delete(0, 'end')
    calc.insert(0, value + digit)


def clear():
    calc.delete(0, 'end')
    calc.insert(0, '0')


def calculate():
    value = calc.get()
    if value[-1] in '-+/*':
        value = value + value[:-1]
    calc.delete(0, 'end')
    try:
        calc.insert(0, eval(value))
    except (NameError, SyntaxError):
        messagebox.showinfo('Attention', 'You only need to enter numbers!!!')
        calc.insert(0,'0')
    except ZeroDivisionError:
        messagebox.showinfo('Attention', 'Cant divide by zero')


def MakeDigitButton(digit):
    return tk.Button(text=f'{digit}', font=('Arial', 13, 'bold'), relief=tk.RAISED, bd=5,
                     command=lambda: add_digit(digit))


def MakeOperationButton(operation):
    return tk.Button(text=f'{operation}', font=('Arial', 13, 'bold'), relief=tk.RAISED, bd=5, fg='#FF0000',
                     command=lambda: add_operation(operation))


def makeClacButton(operation):
    return tk.Button(text=f'{operation}', font=('Arial', 13, 'bold'), relief=tk.RAISED, bd=5, fg='#FF0000',
                     command=calculate)


def add_operation(operation):
    value = calc.get()
    if value[-1] in '-+/*':
        value = value[:-1]
    elif '+' in value or '-' in value or '*' in value or '/' in value:
        calculate()
        value = calc.get()
    calc.delete(0, 'end')
    calc.insert(0, value + operation)


def makeClearButton(operation):
    return tk.Button(text=f'{operation}', font=('Arial', 13, 'bold'), relief=tk.RAISED, bd=5, fg='#FF0000',
                     command=clear)

def press_key(event):
    #print(repr(event.char))
    if event.char.isdigit():
        add_digit(event.char)
    elif event.char in '+-*/.':
        add_operation(event.char)
    elif event.char == '\r':
        calculate()
    elif event.char == '\x08':
        calc.delete(0,tk.END)
        calc.insert(0,'0')

win = tk.Tk()
win.title('Calculator')
win.resizable(False,False)
photo = tk.PhotoImage(file='images.png')
win.geometry('300x300+740+280')
win.iconphoto(False, photo)
win.config(bg='#7ED2FC')
win.bind('<Key>', press_key)
calc = tk.Entry(win, justify=tk.RIGHT, relief=tk.RAISED, bd=5, font=('Arial', 15), fg='black', width=15)
calc.insert(0, '0')
calc.grid(row=0, column=0, columnspan=6, stick='we', padx=5)
MakeDigitButton('1').grid(row=1, column=0, stick='wens', padx=5, pady=5)
MakeDigitButton('2').grid(row=1, column=1, stick='wens', padx=5, pady=5)
MakeDigitButton('3').grid(row=1, column=2, stick='wens', padx=5, pady=5)
MakeDigitButton('4').grid(row=2, column=0, stick='wens', padx=5, pady=5)
MakeDigitButton('5').grid(row=2, column=1, stick='wens', padx=5, pady=5)
MakeDigitButton('6').grid(row=2, column=2, stick='wens', padx=5, pady=5)
MakeDigitButton('7').grid(row=3, column=0, stick='wens', padx=5, pady=5)
MakeDigitButton('8').grid(row=3, column=1, stick='wens', padx=5, pady=5)
MakeDigitButton('9').grid(row=3, column=2, stick='wens', padx=5, pady=5)
MakeDigitButton('0').grid(row=4, column=0, columnspan=2, stick='wens', padx=5, pady=5)
MakeOperationButton('+').grid(row=1, column=3, stick='wens', padx=5, pady=5)
MakeOperationButton('-').grid(row=2, column=3, stick='wens', padx=5, pady=5)
MakeOperationButton('*').grid(row=3, column=3, stick='wens', padx=5, pady=5)
MakeOperationButton('/').grid(row=4, column=3, stick='wens', padx=5, pady=5)
makeClacButton('=').grid(row=4, column=2, stick='wens', padx=5, pady=5)
makeClearButton('c').grid(row=1, column=5, stick='wens', rowspan=4, padx=5, pady=5)
win.grid_columnconfigure(0, minsize=70)
win.grid_columnconfigure(1, minsize=70)
win.grid_columnconfigure(2, minsize=70)
win.grid_columnconfigure(3, minsize=70)
win.rowconfigure(1, minsize=70)
win.grid_rowconfigure(2, minsize=70)
win.grid_rowconfigure(3, minsize=70)
win.mainloop()
