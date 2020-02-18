from tkinter import Toplevel, Label, LEFT, Button, Entry, Tk, Frame, Menu, W, NW, E

import matplotlib.pyplot as plt
import numpy as np
from tkinter.messagebox import showerror

import calculation

# Богатырев Иван ИУ7-22Б 2019
FONT_ARIAL = ("Arial", 14)
FONT_TNR = ("Times New Roman", 12)


def exit_program():
    root.destroy()


def about_programm():
    window = Toplevel()
    window.title("О программе")
    info = Label(window, text='''
    Программа предназанчена для нахождения корней функции методом половинного деления.
    В выполнения вычислений в программу нежно ввести начальное и конечное значение х,
    шаг, точность и макисмально допустимое количество итераций уточнения корня.
    Шаг должен задаваться с тем рассчетом, чтобы на каждом отдельном интервале
    находилось не более одного корня, так как метод половинного деления работает 
    только в таком случае. 
    Важно! Максимальное количество итераций ограничено. Стоит указывать не более 992 итераций, 
    иначе произойдет переполнение стека.
    После выполнения вычилений выводится таблица и график. 
    В таблице содержатся данные об интервале, в котором был найден корень функции,
    значение корня, значение функции, количество потребовавшихся итераций и код ошибки.
    В отдельном окне отображается графическое представление функции. Красными точками
    обозначены корни функции, зелеными - макимум/минимум функции.
    Лабораторную работу выполнил Богатырев Иван (ИУ7-22Б) 2019г.''', justify=LEFT, font=("Times New Roman", 10))
    info.pack()


# Описание кодов ошибок
def list_of_errors():
    window = Toplevel()
    window.title("Список кодов ошибок")
    info = Label(window, text='''
    0 - корень найден без ошибок
    1 - превышено максимальное количество итераций
    Наличие ошибки означает, что в результате некорректно заданного шага
    обрабатывался интервал, на котором одна из производных функции непостоянна.
    ''', justify=LEFT, font=("Times New Roman", 10))
    info.pack()


# Очистка таблицы
def clean_table():
    for i in array_of_root_labels:
        for j in i:
            j.destroy()
    array_of_root_labels.clear()


# Отрисовка таблицы
def output_process(event):
    clean_table()
    # Считывание данных с полей ввода
    start = field_from.get()
    end = field_to.get()
    step = field_step.get()
    eps = field_accuracy.get()
    max_iteration = field_max_iteration.get()

    error_dict = {1: 'Некорректные границы интервала',
                  2: 'Некорректный шаг',
                  3: 'Некорректная точность',
                  4: 'Некорректное максималное количество итераций',
                  5: 'Пустые значения'}
    if start == "" or end == "" or step == "" or eps == "" or max_iteration == "":
        error = 5
    else:
        x_start, x_end, step, eps, max_iteration, error = calculation.checker(start, end, step, eps, max_iteration)
    if error:
        showerror('Ошибка', error_dict[error])
    else:
        try:
            array_of_roots = calculation.find_roots(x_start, x_end, step, eps, max_iteration)
        except RecursionError:
            showerror("Ошибка", "Произошло переполнение стека")
        else:
            if not len(array_of_roots):
                no_root = Label(frame_roots_table, text="Корней не найдено",
                                font=FONT_TNR)
                array_of_root_labels.append([no_root])
                no_root.grid(row=1, column=0)
            elif len(array_of_roots) <= 25:
                for index, item in enumerate(array_of_roots):
                    if item[5] != 0:
                        num, interval, root_x, root_y, iterations, error_code = ('{:d}'.format(item[0]), item[1],
                                                                                 '', '', '',
                                                                                 '{:g}'.format(item[5]))

                    else:
                        num, interval, root_x, root_y, iterations, error_code = ('{:d}'.format(item[0]), item[1],
                                                                                 '{:g}'.format(item[2]),
                                                                                 '{:.1g}'.format(item[3]),
                                                                                 '{:g}'.format(item[4]),
                                                                                 '{:g}'.format(item[5]))
                    num_col = Label(frame_roots_table, text=num, font=FONT_TNR)
                    interval_col = Label(frame_roots_table, text=interval, font=FONT_TNR)
                    root_x_col = Label(frame_roots_table, text=root_x, font=FONT_TNR)
                    root_y_col = Label(frame_roots_table, text=root_y, font=FONT_TNR)
                    iterations_col = Label(frame_roots_table, text=iterations, font=FONT_TNR)
                    error_code_col = Label(frame_roots_table, text=error_code, font=FONT_TNR)
                    num_col.grid(row=index + 1, column=0)
                    interval_col.grid(row=index + 1, column=1)
                    root_x_col.grid(row=index + 1, column=2)
                    root_y_col.grid(row=index + 1, column=3)
                    iterations_col.grid(row=index + 1, column=4)
                    error_code_col.grid(row=index + 1, column=5)

                    array_of_root_labels.append([num_col, interval_col, root_x_col,
                                                 root_y_col, iterations_col, error_code_col])
            else:
                too_much_roots = Label(frame_roots_table,
                                       text="Найдено слишком много корней",
                                       font=FONT_TNR)
                too_much_roots.grid(row=1, column=0)
                array_of_root_labels.append([too_much_roots])
            draw_chart(x_start, x_end, array_of_roots)


# Рисование графика
def draw_chart(x_start, x_end, array_of_roots):
    plt.clf()
    plt.figure(1)
    arr_x = np.linspace(x_start, x_end, 100000)
    arr_y = [calculation.function(i) for i in arr_x]
    plt.plot(arr_x, arr_y, '-')
    max_y = 0
    min_y = 0
    last_root = -100000
    for i in range(len(arr_y)):
        if arr_y[i] > arr_y[max_y]:
            max_y = i
        if arr_y[i] < arr_y[min_y]:
            min_y = i
        if abs(arr_x[i] - last_root) > 1e-2 and abs(arr_y[i]) < 1e-3:
            plt.scatter(arr_x[i], arr_y[i], color='r')
            last_root = arr_x[i]
    plt.scatter(arr_x[max_y], arr_y[max_y], color='g')
    plt.scatter(arr_x[min_y], arr_y[min_y], color='g')
    plt.grid(True)
    plt.show()


# Богатырев Иван ИУ7-22Б 2019
root = Tk()
root.title("Уточнение корней методом половинного деления")
root.geometry("720x720")

# Панель ввода данных
frame_data_input = Frame(root, width=1280, height=250)
label_input = Label(frame_data_input, text="Введите параметры:", font=FONT_ARIAL)
label_input.grid(row=0, column=0, columnspan=5, sticky=NW, ipady=3)
label_interval = Label(frame_data_input, text="Интервал", font=FONT_ARIAL)
label_interval.grid(row=1, column=0, sticky=W, pady=1)
label_from = Label(frame_data_input, text="от", font=FONT_ARIAL)
label_from.grid(row=1, column=1, sticky=W)
field_from = Entry(frame_data_input, font=FONT_ARIAL, width=7)
field_from.grid(row=1, column=2)
label_to = Label(frame_data_input, text="до", font=FONT_ARIAL)
label_to.grid(row=1, column=3, sticky=W)
field_to = Entry(frame_data_input, font=FONT_ARIAL, width=7)
field_to.grid(row=1, column=4)
label_step = Label(frame_data_input, text="Шаг", font=FONT_ARIAL)
label_step.grid(row=2, column=0, sticky=W, pady=1)
field_step = Entry(frame_data_input, font=FONT_ARIAL, width=7)
field_step.grid(row=2, column=4)
label_accuracy = Label(frame_data_input, text="Точность", font=FONT_ARIAL)
label_accuracy.grid(row=3, column=0, sticky=W, pady=1)
field_accuracy = Entry(frame_data_input, font=FONT_ARIAL, width=7)
field_accuracy.grid(row=3, column=4)
label_max_iteration = Label(frame_data_input, text="Максимальное кол-во итераций", font=FONT_ARIAL)
label_max_iteration.grid(row=4, column=0, columnspan=4, sticky=W, pady=1)
field_max_iteration = Entry(frame_data_input, font=FONT_ARIAL, width=7)
field_max_iteration.grid(row=4, column=4)
button_go = Button(frame_data_input, text="Найти корни", font=FONT_ARIAL)
button_go.grid(row=5, column=1, columnspan=5, sticky=E, pady=5)
frame_data_input.grid(row=0)

button_go.bind("<Button-1>", output_process)
button_go.bind('<Return>', output_process)
field_max_iteration.bind('<Return>', output_process)
field_accuracy.bind('<Return>', output_process)
field_step.bind('<Return>', output_process)
field_to.bind('<Return>', output_process)
field_from.bind('<Return>', output_process)

array_of_root_labels = []
frame_roots_table = Frame(root, width=1280, height=430)
number = Label(frame_roots_table, text="№", font=FONT_ARIAL)
interval = Label(frame_roots_table, text='Интервал', font=FONT_ARIAL)
root_x = Label(frame_roots_table, text='x', font=FONT_ARIAL)
root_y = Label(frame_roots_table, text='f(x)', font=FONT_ARIAL)
iterations = Label(frame_roots_table, text='Количество итераций',
                   font=FONT_ARIAL)
error_code = Label(frame_roots_table, text='Код ошибки',
                   font=FONT_ARIAL)
number.grid(row=0, column=0, ipadx=20)
interval.grid(row=0, column=1, ipadx=20)
root_x.grid(row=0, column=2, ipadx=20)
root_y.grid(row=0, column=3, ipadx=20)
iterations.grid(row=0, column=4, ipadx=20)
error_code.grid(row=0, column=5, ipadx=20)
frame_roots_table.grid(row=1)
menu_main = Menu(root)
root.config(menu=menu_main)
menu = Menu(menu_main, tearoff=0)
menu.add_command(label="О программе", command=about_programm)
menu.add_command(label="Описание ошибок", command=list_of_errors)
menu.add_command(label="Выход", command=exit_program)
menu_main.add_cascade(label="Меню", menu=menu)

root.mainloop()
