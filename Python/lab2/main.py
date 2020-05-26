from tkinter import Tk, Frame, Label, Button, Toplevel, Menu

from calculation import to_ternary_convert, to_decimal_convert


def exit_program():
    root.destroy()


def about_program():
    window = Toplevel()
    window.title("О программе")
    info = Label(window, text='''
    Программа выполняет две операции: конвертация числа из десятичной системы 
    счисления в троичную симметричную систему счисления, и наоборот.
    Для отображения отрицательной единицы в троичной семмитрияной
    системе счисления используется символ i.
    Лабораторную работу выполнил Богатырев Иван (ИУ7-22Б) 2020г.''', font=("Times New Roman", 10))
    info.pack()


def keyboard_input(input, text):
    if input == "period":
        input = "."
    if input == "to ternary":
        try:
            label_input.config(text=to_ternary_convert(text))
        except ValueError:
            label_input.config(text="Value Error")
    elif input == "to decimal":
        try:
            label_input.config(text=to_decimal_convert(text))
        except ValueError:
            label_input.config(text="Value Error")
    elif input == "del" or input == "BackSpace":
        label_input.config(text=str(text)[:-1])
    elif input == "C":
        label_input.config(text="")
    elif input == "OFF":
        exit()
    elif input == "-" or input == "minus":
        if text == "":
            label_input.config(text="-")
        elif text[0] == "-":
            label_input.config(text=text[1:])
        else:
            label_input.config(text=("-" + text))
    elif input in {"1", "2", "3", "4", "5", "6", "7", "8", "9", "0", ".", "i"}:
        new_text = text + input + ""
        label_input.config(text=new_text)
    else:
        label_input.config(text=input)


def interlayer(event):
    if event.keysym in {"1", "2", "3", "4", "5", "6", "7", "8", "9", "0", ".", "i", "BackSpace", "period", "minus"}:
        keyboard_input(event.keysym, label_input['text'])


root = Tk()
root.title("Калькулятор")
root.geometry("375x490")
root.bind('<Key>', interlayer)
frame_data_input = Frame(root, width=28, height=490)
label_input = Label(frame_data_input, text="", font=("Arial", 16, 'bold'), height=3)
label_input.grid(row=0, column=0, columnspan=100)
btn_list = [
    "7", "8", "9", "C",
    "4", "5", "6", "del",
    "1", "2", "3", "-",
    "0", "i", ".", "OFF",
    "to ternary", "to decimal", ]
r = 1
c = 0
for i in btn_list:
    Button(frame_data_input, text=i, command=lambda x=i: keyboard_input(x, label_input["text"]), width=7, height=3,
           font=("Arial", 14, 'bold')).grid(row=r, column=c)
    c += 1
    if c > 3:
        c = 0
        r += 1


def action_to_ternary():
    keyboard_input("to ternary", label_input['text'])


def action_to_decimal():
    keyboard_input("to decimal", label_input['text'])


frame_data_input.pack()

menu_main = Menu(root)
root.config(menu=menu_main)
menu = Menu(menu_main, tearoff=0)
menu.add_command(label="О программе", command=about_program)
menu.add_command(label="Выход", command=exit_program)
actions = Menu(menu_main, tearoff=0)
actions.add_command(label="Перевести в троичную систему счисления", command=action_to_ternary)
actions.add_command(label="Перевести в десятичную систему счисления", command=action_to_decimal)
menu_main.add_cascade(label="Меню", menu=menu)
menu_main.add_cascade(label="Основные действия", menu=actions)

root.mainloop()
