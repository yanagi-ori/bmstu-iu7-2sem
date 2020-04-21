"""метод простого выбора"""
import random
from datetime import datetime
from tkinter import Tk, Button, Frame, Label
import matplotlib.pyplot as plt
import numpy as np


def clear():
    for i in expired_elements:
        i.destroy()


def simple_sort(array):
    for shift in range(len(array) - 1):
        least = shift
        for i in range(shift + 1, len(array)):
            if array[i] < array[least]:
                least = i
        array[shift], array[least] = array[least], array[shift]
    return array


def array_generator(length):
    array = []
    for i in range(length):
        array.append(random.randint(-1000, 1000))
    return array


def measurements(i, test_array):
    time_delta = delta_time(test_array)
    time_array[i] = time_delta.seconds + time_delta.microseconds / 1000000


def chart_measurements(test_array):
    time_delta = delta_time(test_array)
    return time_delta.seconds + time_delta.microseconds / 1000000


def delta_time(test_array):
    start_time = datetime.now()
    simple_sort(test_array)
    return datetime.now() - start_time


def button_click():
    clear()
    go_button.config(text='Retry')
    go_button.place(anchor='s', relx=0.5, rely=1, relwidth=1, height=40)
    label = Label(root,
                  text='Пример отсортированного массива: \n{}'.format(simple_sort(array_generator(10))),
                  font='6', bg='#cfcfcf')
    label.place(relx=0.5, anchor='n', rely=0.01)
    expired_elements.append(label)

    for i in range(9):
        for j, length in enumerate([1000, 1500, 2000]):
            test_array = array_generator(length)
            test_array.sort()
            measurements(j, test_array)
        for j, length in enumerate([1000, 1500, 2000]):
            measurements(j + 3, array_generator(length))
        for j, length in enumerate([1000, 1500, 2000]):
            test_array = array_generator(length)
            test_array.sort()
            test_array.reverse()
            measurements(j + 6, test_array)
    Label(frame_table, text='1000 (сек)', font=6, bg='#9e9e9e').grid(row=0, column=1, padx=3, pady=2)
    Label(frame_table, text='1500 (сек)', font=6, bg='#9e9e9e').grid(row=0, column=2, padx=3, pady=2)
    Label(frame_table, text='2000 (сек)', font=6, bg='#9e9e9e').grid(row=0, column=3, padx=3, pady=2)
    Label(frame_table, text='Упорядоченный\nмассив', font=6, bg='#9e9e9e').grid(row=1, column=0, padx=3, pady=2)
    Label(frame_table, text='Случайный\nмассив', font=6, bg='#9e9e9e').grid(row=2, column=0, padx=3, pady=2)
    Label(frame_table, text='Упорядоченный\nв обратном\nпорядке', font=6, bg='#9e9e9e').grid(row=3, column=0, padx=3, pady=2)
    for i in range(3):
        shift = 0
        col = 0
        for j in range(shift, shift + 3):
            Label(frame_table, text=time_array[j + i * 3], font=6, bg='#9e9e9e').grid(row=i + 1, column=col + 1, padx=3, pady=2)
            col += 1
    frame_table.place(anchor='center', relx=0.5, rely=0.5)
    draw_chart()


def draw_chart():
    plt.clf()
    plt.figure(1)
    arr_x = np.linspace(1000, 5500, 10)
    arr_y = [chart_measurements(array_generator(i)) for i in range(1000, 5501, 500)]
    plt.plot(arr_x, arr_y)
    plt.grid(True)
    plt.show()


root = Tk()
root.title("Исследования методов сортировки")
root.geometry("500x500")
root.config(bg='#cfcfcf')
go_button = Button(root, text="Go",
                   bg='#9e9e9e', activebackground='#707070',
                   font='16',
                   command=button_click)
go_button.place(anchor="center", relx=0.5,
                rely=0.5, width=60,
                height=40)
expired_elements = []
frame_table = Frame(root, bg='#9e9e9e')
time_array = [0, 0, 0,
              0, 0, 0,
              0, 0, 0]

root.mainloop()

# 1000 1500 2000 2500 3000 3500 4000 4500 5000 5500
