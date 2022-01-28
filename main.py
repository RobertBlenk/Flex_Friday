from tkinter import *

window_main = Tk()


def input_word():
    window_inp = Tk()
    t1 = Entry(window_inp)
    t1.place(x=80, y=80)
    window_inp.title("Input screen")
    window_inp.geometry("850x300+5+5")
    window_inp.resizable(False, False)
    window_inp.mainloop()


def change_language():
    pass


def change_difficulty():
    pass


def page_setup():
    pass


def esc_command():  # separate window
    window_esc = Tk()

    a1 = Button(window_esc, text="input word", command=input_word)
    b1 = Button(window_esc, text="change language", command=change_language)
    c1 = Button(window_esc, text="change difficulty", command=change_difficulty)
    d1 = Button(window_esc, text="page setup", command=page_setup)

    a1.place(x=0, y=0)
    b1.place()
    c1.place()
    d1.place()

    window_esc.title("Escape")
    window_esc.geometry("850x300+5+5")
    window_esc.resizable(False, False)
    window_esc.mainloop()


def flip():
    pass


def main():

    e1 = Button(window_main, text="Esc", command=esc_command)
    e2 = Button(window_main, text="Flip", command=flip)
    e1.place(x=0, y=0)
    e2.place(x=625, y=380)

    window_main.title("FlashCards")
    window_main.geometry("1250x405+5+5")
    window_main.resizable(False, False)
    window_main.mainloop()


if __name__ == '__main__':
    main()
