def to_decimal_convert(num):
    array = num.split(".")
    if len(array) == 1:
        array = list(array[0])
        replace(array)
        asym_process(array)
        return left_post_process(array)
    elif len(array) == 2:
        left = list(array[0])
        right = list(array[1])
        replace(left)
        asym_process(left)
        replace(right)
        right.reverse()
        asym_process(right)
        right.reverse()
        if right[-1] == "-1": right[-1] = "3"
        return left_post_process(left) + right_post_process(right)


def left_post_process(array):
    sum = 0
    for i in range(len(array)):
        sum += int(array[-i - 1]) * 3 ** i
    return sum


def right_post_process(array):
    sum = 0
    for i in range(len(array)):
        sum += int(array[i]) * 3 ** (-i - 1)
    return sum - 1


def replace(array):
    for i in range(len(array)):
        if array[i] == "i":
            array[i] = "-1"


def to_ternary_convert(num):
    if "i" in str(num):
        return "error"
    num = float(num)
    negative = False
    if list(str(num))[0] == '-':
        num = float("".join(list(str(num))[1:]))
        negative = True
    left = []
    temp = int(num)
    while temp > 0:
        left = [temp % 3] + left
        temp = temp // 3
    temp = num % 1
    i = 0
    right = []
    while temp != 0 and i < 7:
        temp = temp * 3
        right += [int(temp)]
        temp = float(temp) - int(temp)
        i += 1
    if negative:
        right = invert(right)
        left = invert(left)
    left, right = to_sym(left, right)
    temp = left + ["."] + right
    return "".join([str(elem) for elem in temp]).replace("-1", "i")


def to_sym(left, right):
    array = [0] + left
    sym_process(array)
    if array[0] == 0:
        array.pop(0)
    left = array

    array = right + [0]
    array.reverse()
    sym_process(array)
    array.reverse()
    right = array
    return list(left), list(right)


def sym_process(array):
    for i in range(len(array) - 1, -1, -1):
        if array[i] == 2:
            array[i] = -1
            array[i - 1] += 1
        elif array[i] == 3:
            array[i] = 0
            array[i - 1] += 1
        elif array[i] == -2:
            array[i] = 1
            array[i - 1] -= 1
        elif array[i] == -3:
            array[i] = 0
            array[i - 1] -= 1


def asym_process(array):
    for i in range(1, len(array)):
        if int(array[i]) == -1:
            array[i] = "2"
            array[i - 1] = str(int(array[i - 1]) - 1)
        elif int(array[i]) == 0:
            array[i] = "3"
            array[i - 1] = str(int(array[i - 1]) - 1)
        elif int(array[i]) == -2:
            array[i] = "1"
            array[i - 1] = str(int(array[i - 1]) + 1)
        elif int(array[i]) == -3:
            array[i] = "0"
            array[i - 1] = str(int(array[i - 1]) + 1)


def invert(array):
    for i in range(len(array)):
        array[i] *= -1
    return array
