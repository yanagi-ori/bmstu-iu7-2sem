# Исследуемая функция
from math import fabs, sin


# Богатырев Иван ИУ7-22Б 2019


class CheckerException(Exception):
    pass


NO_ERRORS = True  # Корень найден без огибок
ERROR_CODE_1 = 1  # Превышено максимальное количество итераций


def function(x):
    return sin(x)
    # return x ** 2 + 1


def half_divide_method(start_point, end_point, accuracy, max_iteration, current_iteration=0):
    while current_iteration <= max_iteration:
        mid_point = (start_point + end_point) / 2
        if current_iteration >= max_iteration:
            return ['', '', '', ERROR_CODE_1]
        if (abs(function(mid_point))) < accuracy:
            return [mid_point, function(mid_point), current_iteration, False]
        elif function(mid_point) > 0:
            end_point = mid_point
            current_iteration += 1
        elif function(mid_point) < 0:
            start_point = mid_point
            current_iteration += 1


"""def half_divide_method(start_point, end_point, accuracy, max_iteration, current_iteration=0):
    mid_point = (start_point + end_point) / 2
    if current_iteration >= max_iteration:
        return ['', '', '', ERROR_CODE_1]
    if abs(function(mid_point)) < accuracy:
        return [mid_point, function(mid_point), current_iteration, False]
    elif function(mid_point) > 0:
        return half_divide_method(start_point, mid_point, accuracy, max_iteration, current_iteration + 1)
    elif function(mid_point) < 0:
        return half_divide_method(mid_point, end_point, accuracy, max_iteration, current_iteration + 1)"""


def find_roots(start_point, end_point, step, eps, max_iteration):
    array_of_roots = []
    x_cur = start_point
    x_next = round(x_cur + step, 10)
    if x_next > end_point:
        x_next = end_point
    while x_next <= end_point:
        if abs(function(x_cur)) < eps:
            array_of_roots.append(0)
            array_of_roots[-1] = [len(array_of_roots),
                                  '{:g}..{:g}'.format(x_cur, x_next),
                                  x_cur, function(x_cur), 1, False]
        elif function(x_cur) * function(x_next) < 0:
            array_of_roots.append(0)
            array_of_roots[-1] = ([len(array_of_roots), '{:g}..{:g}'.format(x_cur, x_next)] +
                                  half_divide_method(x_cur, x_next, eps, max_iteration))

        x_cur = x_next
        x_next = round(x_cur + step, 10)
        if x_next > end_point and end_point - x_cur > eps:
            x_next = end_point

    if abs(x_cur - end_point) < eps and abs(function(x_cur)) < eps:
        array_of_roots.append(0)
        array_of_roots[-1] = [len(array_of_roots),
                              '{:g}..{:g}'.format(x_cur, end_point),
                              end_point, function(end_point), 0, 0]
    return array_of_roots


# Проверка входных данных
def checker(start_point, end_point, step, eps, max_iteration):
    error_code = 0
    try:
        if start_point == "" or end_point == "" or \
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
    return float(start_point), float(end_point), float(step), float(eps), float(max_iteration), float(error_code)
