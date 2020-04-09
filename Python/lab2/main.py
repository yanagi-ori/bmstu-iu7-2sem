from tkinter import Tk, Frame, Label, Button

from calculation import to_ternary_convert, to_decimal_convert


def keyboard_input(input, text):
    if input == "to ternary":
        label_input.config(text=to_ternary_convert(text))
    elif input == "to decimal":
        label_input.config(text=to_decimal_convert(text))
    elif input == "del":
        label_input.config(text=text[:-1])
    elif input == "C":
        label_input.config(text="")
    elif input == "OFF":
        exit()
    elif input == "-":
        if text[0] == "-":
            label_input.config(text=text[1:])
        else:
            label_input.config(text=("-" + text))
    elif input in {"1", "2", "3", "4", "5", "6", "7", "8", "9", "0", ".", "i"}:
        new_text = text + input + ""
        label_input.config(text=new_text)
    else:
        label_input.config(text=input)


root = Tk()
root.title("Калькулятор")
root.geometry("375x490")
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

frame_data_input.pack()
root.mainloop()
