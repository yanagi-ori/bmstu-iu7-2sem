from tkinter import *

root = Tk()
root.title("Решение геометрической задачи")
M = []
X = []


def dot_draw(event):
    x11, y11 = int(event.x), int(event.y)
    c.create_oval(str(x11), str(y11), str(x11), str(y11), tag='k')
    X.append([x11, y11])
    print(X)
    c.unbind("<Button-1>")


def oval_draw_step_1(event1):
    c.create_text(450, 50, text="Для создания окружности кликните в точку\n"
                                "желаемого центра,а затем на любую точку плоскости,\n"
                                "отстоящую от центра на расстоянии желаемого\nрадиуса", tag='j')
    c.create_oval(event1.x, event1.y, event1.x, event1.y, tag='j')
    c.bind("<Button-1>", lambda event, x=event1.x, y=event1.y: oval_draw_step_2(event, x, y))


def oval_draw_step_2(event2, x1, y1):
    r = ((abs(x1 - event2.x)) ** 2 + (abs(y1 - event2.y)) ** 2) ** (1 / 2)
    c.create_oval(x1 - r, y1 + r, x1 + r, y1 - r, tag='k')
    M.append([x1, y1, r])
    c.delete('j')
    c.unbind("<Button-1>")


def solve(M1, X1):
    global M, X
    z = len(X1)
    m = len(M1)
    vn = [0] * m
    sn = [0] * m
    print(M1)
    print(X1)
    for i in range(m):
        p = M1[i]
        for j in range(z):
            t = X1[j]
            if ((p[0] - t[0]) ** 2 + (p[1] - t[1]) ** 2) <= (p[2]) ** 2:
                vn[i] += 1
            else:
                sn[i] += 1
            print(vn[i], sn[i])
        vn[i] = abs(vn[i] - sn[i])
        print(vn[i])
    minn = vn[0]
    for i in range(m):
        if vn[i] < minn:
            minn = vn[i]
    for i in range(m):
        if vn[i] == minn:
            c.create_oval(M1[i][0] - M1[i][2], M1[i][1] + M1[i][2], M1[i][0] + M1[i][2], M1[i][1] - M1[i][2],
                          outline="red", tag='k')
            c.create_text(450, 50, text="Выделенные окружности являются решением", tag='k')
    M = []
    X = []


def add_window():
    def paint1():
        xx1 = int(x1.get())
        yy1 = int(y1.get())
        c.create_oval(str(290 + xx1), str(290 - yy1), str(290 + xx1), str(290 - yy1), tag='k')
        X.append([290 + xx1, 290 - yy1])

    def paint2():
        xx2 = int(x2.get())
        yy2 = int(y2.get())
        rr = int(r.get())
        c.create_oval(str(290 + xx2 - rr), str(290 - (yy2 + rr)), str(290 + xx2 + rr), str(290 - (yy2 - rr)), tag='k')
        M.append([290 + xx2, 290 - yy2, rr])

    b = Toplevel()
    b.title("Действия")
    b.resizable(False, False)
    Label(b, text=" Точка ").grid(row=1, column=0, columnspan=4)
    Label(b, text=" x ").grid(row=2, column=0)
    Label(b, text=" y ").grid(row=2, column=2)
    Button(b, text="Нарисовать", command=paint1).grid(row=3, columnspan=4)
    Label(b, text=" Окружность ").grid(row=5, column=0, columnspan=4)
    Label(b, text=" x ").grid(row=6, column=0)
    Label(b, text=" y ").grid(row=6, column=2)
    Label(b, text=" R ").grid(row=7, column=0)
    Button(b, text="Нарисовать", command=paint2).grid(row=8, columnspan=4)
    x1 = Entry(b, width=5)
    x1.grid(row=2, column=1, sticky=E)
    y1 = Entry(b, width=5)
    y1.grid(row=2, column=3, sticky=E)
    x2 = Entry(b, width=5)
    x2.grid(row=6, column=1, sticky=W)
    y2 = Entry(b, width=5)
    y2.grid(row=6, column=3, sticky=W)
    r = Entry(b, width=5)
    r.grid(row=7, column=1, sticky=W)


c = Canvas(root, width=600, height=580, bg="white")
c.place(x=0, y=20)

c.create_line(0, 290, 595, 290, arrow=LAST)
c.create_line(290, 600, 290, 5, arrow=LAST)
c.create_line(300, 285, 300, 295)
c.create_line(285, 280, 295, 280)

c.create_text(275, 280, text="10")
c.create_text(300, 305, text="10")
c.create_text(285, 300, text="0")
c.create_text(275, 10, text="y")
c.create_text(575, 305, text="x")

Button(root, text="Добавить фигуру", width=20, command=add_window).place(x=0, y=0)
Button(root, text="Нарисовать точку", width=20, command=lambda: c.bind("<Button-1>", dot_draw)).place(x=150, y=0)
Button(root, text="Нарисовать окружность",
       width=20, command=lambda: c.bind('<Button-1>', oval_draw_step_1)).place(x=300, y=0)
Button(root, text="Решить задачу", width=20, command=lambda: solve(M, X)).place(x=450, y=0)
Button(root, text="Очистить поле  ", width=90, command=lambda: c.delete('k')).place(x=0, y=575)
root.geometry("600x600")
root.mainloop()
