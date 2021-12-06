import tkinter


def blank_lines_horizontal(row, length, root):
    for i in range(length):
        _ = tkinter.Label(root, text=" ")
        _.grid(row=row, column=i)


def blank_lines_vertical(column, length, root):
    for i in range(length):
        _ = tkinter.Label(root, text=" ")
        _.grid(row=i, column=column)
