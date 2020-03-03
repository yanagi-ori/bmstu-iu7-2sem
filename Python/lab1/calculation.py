# Исследуемая функция
from math import *
from tkinter.messagebox import showerror


# Богатырев Иван ИУ7-22Б 2019


class CheckerException(Exception):
    pass


NO_ERRORS = True  # Корень найден без огибок
ERROR_CODE_1 = 1  # Превышено максимальное количество итераций


def function(func_str, x):
    result = eval(func_str)
    return result


def half_divide_method(func_str, start_point, end_point, accuracy, max_iteration, current_iteration=0):
    mid_point = (start_point + end_point) / 2
    if current_iteration >= max_iteration:
        return ['', '', '', ERROR_CODE_1]
    if abs(function(func_str, mid_point)) < accuracy:
        return [mid_point, function(func_str, mid_point), current_iteration, False]
    elif function(func_str, mid_point) * function(func_str, start_point) < 0:
        return half_divide_method(func_str, start_point, mid_point, accuracy, max_iteration, current_iteration + 1)
    else:
        return half_divide_method(func_str, mid_point, end_point, accuracy, max_iteration, current_iteration + 1)


def find_roots(func_str, start_point, end_point, step, eps, max_iteration):
    array_of_roots = []
    x_cur = start_point
    x_next = round(x_cur + step, 10)
    if x_next > end_point:
        x_next = end_point
    while x_next <= end_point:
        if abs(function(func_str, x_cur)) < eps:
            array_of_roots.append(0)
            array_of_roots[-1] = [len(array_of_roots), '{:g}..{:g}'.format(x_cur, x_next),
                                  x_cur, function(func_str, x_cur), 1, False]
        elif function(func_str, x_cur) * function(func_str, x_next) < 0:
            array_of_roots.append(0)
            array_of_roots[-1] = ([len(array_of_roots), '{:g}..{:g}'.format(x_cur, x_next)] +
                                  half_divide_method(func_str, x_cur, x_next, eps, max_iteration))
        x_cur = x_next
        x_next = round(x_cur + step, 10)
        if x_next > end_point and end_point - x_cur > eps:
            x_next = end_point

        if abs(x_cur - end_point) < eps and abs(function(func_str, x_cur)) < eps:
            array_of_roots.append(0)
            array_of_roots[-1] = [len(array_of_roots),
                                  '{:g}..{:g}'.format(x_cur, end_point),
                                  end_point, function(func_str, end_point), 0, 0]
    return array_of_roots


# Проверка входных данных
def checker(function_str, start_point, end_point, step, eps, max_iteration):
    error_code = 0
    try:
        if function_str == "" or start_point == "" or end_point == "" or \
                step == "" or eps == "" or max_iteration == "":
            raise CheckerException
        start = float(start_point)
        end = float(end_point)
        if end <= start:
            raise CheckerException
    except CheckerException:
        error_code = 1
    if not error_code:
        try:
            step = float(step)
            if step <= 0:
                raise CheckerException
        except CheckerException:
            error_code = 2
    if not error_code:
        try:
            eps = float(eps)
            if eps <= 0:
                raise CheckerException
        except CheckerException:
            error_code = 3
    if not error_code:
        try:
            max_iteration = int(max_iteration)
            if 920 < max_iteration <= 0:
                raise CheckerException
        except CheckerException:
            error_code = 4
    if function_str == "" or start_point == "" or end_point == "" or step == "" or eps == "" or max_iteration == "" and not error_code:
        error_code = 5
    if step <= eps and not error_code:
        error_code = 6
    if not error_code:
        try:
            abs(function(function_str, 0))
        except (TypeError, SyntaxError, ValueError, NameError):
            error_code = 7
    return float(start_point), float(end_point), float(step), float(eps), float(max_iteration), float(error_code)
