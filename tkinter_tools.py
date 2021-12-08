# Tkinter Tools by JamesJoynsonEllis

import tkinter

username = ""
password = ""


def blank_lines_horizontal(row, length, root):
    for i in range(length):
        _ = tkinter.Label(root, text=" ")
        _.grid(row=row, column=i)


def blank_lines_vertical(column, length, root):
    for i in range(length):
        _ = tkinter.Label(root, text=" ")
        _.grid(row=i, column=column)


def get_login_submit_login(username_entry, password_entry):
    global username
    global password
    username = username_entry.get()
    password = password_entry.get()


def quit_button_command(root):
    return 0, 0


def get_login():
    global username
    global password

    root = tkinter.Tk()
    root.title("Login")

    # Assets #
    blank_lines_horizontal(0, 10, root=root)

    username_label = tkinter.Label(root, text="Username: ")
    password_label = tkinter.Label(root, text="Password: ")
    username_entry = tkinter.Entry(root)
    password_entry = tkinter.Entry(root, show="*")
    submit_button = tkinter.Button(root, text="Submit", command=lambda:get_login_submit_login(username_entry, password_entry))
    quit_button = tkinter.Button(root, text="Quit", command=lambda:quit_button_command(root))

    username_label.grid(row=1, column=1)
    password_label.grid(row=2, column=1)
    username_entry.grid(row=1, column=2, columnspan=2)
    password_entry.grid(row=2, column=2, columnspan=2)
    submit_button.grid(row=3, column=3)
    quit_button.grid(row=3, column=1)

    tkinter.mainloop()
    return username.replace(" ", ""), password.replace(" ", "")


# This code is not to be directly used without crediting the author
