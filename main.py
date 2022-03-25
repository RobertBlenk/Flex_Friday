from tkinter import *
window_main = Tk()


def main():

    def entered():
        hangul = str(t1.get())
        print(hangul)
        t1.delete(0, 'end')
        english = t1a.get()
        print(english)
        t1a.delete(0, 'end')

    def tb():
        print("pressed tb")
        t_b.config(relief=SUNKEN)
        t_n.config(relief=RAISED)
        t_v.config(relief=RAISED)

    def tn():
        print("pressed tn")
        t_b.config(relief=RAISED)
        t_n.config(relief=SUNKEN)
        t_v.config(relief=RAISED)

    def tv():
        print("pressed tv")
        t_b.config(relief=RAISED)
        t_n.config(relief=RAISED)
        t_v.config(relief=SUNKEN)

    def input_word():
        global t_b
        global t_n
        global t_v
        global t1
        global t1a
        window_inp = Tk()
        t1 = Entry(window_inp)
        t1a = Entry(window_inp)
        t2 = Button(window_inp, text="Enter", command=entered)
        t3 = Label(window_inp, text="Enter word in Hangul here")
        t3a = Label(window_inp, text="Enter word in English here")
        t3b = Label(window_inp, text="choose a category here")
        t_b = Button(window_inp, text="Basic", command=tb)
        t_n = Button(window_inp, text="Nouns", command=tn)
        t_v = Button(window_inp, text="Verbs", command=tv)
        t1.place(x=20, y=22)
        t1a.place(x=20, y=72)
        t_b.place(x=20, y=112)
        t_n.place(x=60, y=112)
        t_v.place(x=108, y=112)
        t2.place(x=20, y=172)
        t3.place(x=20, y=0)
        t3a.place(x=20, y=45)
        t3b.place(x=20, y=90)
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
        window_esc.geometry("166x166+5+5")
        window_esc.resizable(False, False)
        window_esc.mainloop()

    def flip():
        pass

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
