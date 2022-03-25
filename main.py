from tkinter import *
import sqlite3
window_main = Tk()
conn = sqlite3.connect(database='database.db')
c = conn.cursor()
# this was me making the table for korean, I only had to do this once but, I wanted to keep it there.
#  c.execute("""CREATE TABLE korean(
            #hangul text,
            #romaja text,
            #english text,
            #category text
            #)""")

#  conn.commit()
#  conn.close()
#c.execute("SELECT * FROM korean WHERE english='hello'")
#print(c.fetchone())


def main():

    class Input_word:

        def __init__(self, han, rom, eng, cat):
            self.hangul = han
            self.romaja = rom
            self.english = eng
            self.category = cat

    def entered():
        var_hangul = str(t1.get())
        t1.delete(0, 'end')

        var_english = t1a.get()
        t1a.delete(0, 'end')

        var_romaja = t1b.get()
        t1b.delete(0, 'end')

        Word = Input_word(var_hangul, var_romaja, var_english, var_category)

        c.execute("INSERT INTO korean VALUES (?, ?, ?, ?)", (Word.hangul, Word.romaja, Word.english, Word.category))
        conn.commit()
        conn.close()

    def tb():
        global var_category
        var_category = "Basic"
        t_b.config(relief=SUNKEN)
        t_n.config(relief=RAISED)
        t_v.config(relief=RAISED)

    def tn():
        global var_category
        var_category = "Noun"
        t_b.config(relief=RAISED)
        t_n.config(relief=SUNKEN)
        t_v.config(relief=RAISED)

    def tv():
        global var_category
        var_category = "Verb"
        t_b.config(relief=RAISED)
        t_n.config(relief=RAISED)
        t_v.config(relief=SUNKEN)

    def input_word():
        global t_b
        global t_n
        global t_v
        global t1
        global t1a
        global t1b
        window_inp = Tk()
        t1 = Entry(window_inp)
        t1a = Entry(window_inp)
        t1b = Entry(window_inp)
        t2 = Button(window_inp, text="Enter", command=entered)
        t3 = Label(window_inp, text="Enter word in Hangul here:")
        t3a = Label(window_inp, text="Enter word in English here:")
        t3b = Label(window_inp, text="Enter the word in Romaja here:")
        t3c = Label(window_inp, text="choose a category here")
        t_b = Button(window_inp, text="Basic", command=tb)
        t_n = Button(window_inp, text="Noun", command=tn)
        t_v = Button(window_inp, text="Verb", command=tv)
        t1.place(x=20, y=22)
        t1a.place(x=20, y=72)
        t1b.place(x=20, y=112)
        t_b.place(x=20, y=162)
        t_n.place(x=63, y=162)
        t_v.place(x=108, y=162)
        t2.place(x=20, y=212)
        t3.place(x=20, y=0)
        t3a.place(x=20, y=45)
        t3b.place(x=20, y=90)
        t3c.place(x=20, y=140)
        window_inp.title("Input screen")
        window_inp.geometry("450x300+5+5")
        window_inp.resizable(False, False)
        window_inp.mainloop()

    def change_language():
        pass

    def mode_basic():
        c.execute("SELECT * FROM korean WHERE category='Basic'")
        xlist = list(c.fetchall())
        conn.commit()
        c.close()
        return xlist

    def mode_noun():
        c.execute("SELECT * FROM korean WHERE category='Nouns'")
        xlist = list(c.fetchall())
        conn.commit()
        c.close()
        return xlist

    def mode_verb():
        c.execute("SELECT * FROM korean WHERE category='Verbs'")
        xlist = list(c.fetchall())
        conn.commit()
        c.close()
        return xlist

    def change_mode():
        window_mode = Tk()
        c2 = Button(window_mode, text="Basic", command=mode_basic)
        c3 = Button(window_mode, text="Noun", command=mode_noun)
        c4 = Button(window_mode, text="Verb", command=mode_verb)

        c2.place(x=0, y=0)
        c3.place(x=100, y=0)
        c4.place(x=200, y=0)
        window_mode.title("Mode change")
        window_mode.geometry("400x405+5+5")
        window_mode.resizable(False, False)
        window_mode.mainloop()

    def page_setup():
        pass

    def esc_command():  # separate window
        window_esc = Tk()

        a1 = Button(window_esc, text="input word", command=input_word)
        b1 = Button(window_esc, text="change language", command=change_language)
        c1 = Button(window_esc, text="change mode", command=change_mode)
        d1 = Button(window_esc, text="page setup", command=page_setup)

        a1.place(x=0, y=0)
        b1.place()
        c1.place(x=81.5, y=0)
        d1.place()

        window_esc.title("Escape")
        window_esc.geometry("166x166+5+5")
        window_esc.resizable(False, False)
        window_esc.mainloop()

    def flip():
        print("flipped")
    # main starts

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
