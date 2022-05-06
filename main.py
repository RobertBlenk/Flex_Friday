import tkinter
from tkinter import *
import sqlite3
import random

score = 0
window_main = Tk()
conn = sqlite3.connect(database='database.db')
c = conn.cursor()
donn = sqlite3.connect(database='score.db')
d = donn.cursor()
d.execute("DELETE FROM current")
d.execute("INSERT INTO current VALUES (0, 0, 0)")
#  d.execute("INSERT INTO High VALUES (0)")
#  d.execute("DELETE FROM High")
donn.commit()

# This is how I made the tables in SQL, just wanted to keep them here for reference.
#  d.execute("""CREATE TABLE current(
            #score integer,
            #correct integer,
            #incorrect integer
            #)""")
#  donn.commit()
#  d.close()
#  d.execute("""CREATE TABLE High(
            #score integer
            #)""")
#  donn.commit()
#  d.close()

#  c.execute("""CREATE TABLE korean(
            #hangul text,
            #romaja text,
            #english text,
            #category text
            #)""")

#  conn.commit()
#  conn.close()
#  c.execute("SELECT * FROM korean WHERE english='hello'")
#  c.execute("SELECT * FROM korean WHERE category='Basic'")
#  print(c.fetchall())


def main():

    class Input_word:

        def __init__(self, han, rom, eng, cat):
            self.hangul = han
            self.romaja = rom
            self.english = eng
            self.category = cat

    class input_score:

        def __init__(self, score, corr, incorr):
            self.score = score
            self.correct = corr
            self.incorrect = incorr

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

    def main_function():
        global ans
        global y1
        global y2
        global y3
        global y4
        c.execute("SELECT * FROM korean ")
        x_list = list(c.fetchall())
        x_set = set()
        f = True

        while f is True:
            x = random.randint(0, (len(x_list) - 1))
            x_set.add(x_list[x])

            if len(x_set) >= 4:
                f = False

        x_list2 = list(x_set)
        list2 = list("")

        for r in range(0, 4):
            l = list(x_list2[r])
            list2.append(l[2])

        w = x_list2[0]
        w2 = Input_word(w[0], w[1], w[2], w[3])
        c.execute("SELECT * FROM korean WHERE english= (:eng)", {'eng': w2.english})
        w3 = c.fetchone()
        ans = w3[2]

        y1 = random.choice(list2)
        list2.remove(y1)
        y2 = random.choice(list2)
        list2.remove(y2)
        y3 = random.choice(list2)
        list2.remove(y3)
        y4 = random.choice(list2)
        list2.remove(y4)

        et1.set(y1)
        et2.set(y2)
        et3.set(y3)
        et4.set(y4)
        w3_0.set(w3[0])
        w3_1.set(w3[1])

        d.execute("SELECT * FROM High")
        dd = d.fetchone()
        hh.set(dd)
        d.execute("SELECT * FROM current")
        jj = d.fetchone()
        hh2.set(jj[0])
        window_main.update()

    # main starts
    global et1
    global et2
    global et3
    global et4
    global hh
    global hh2
    et1 = tkinter.StringVar()
    et2 = tkinter.StringVar()
    et3 = tkinter.StringVar()
    et4 = tkinter.StringVar()
    w3_0 = tkinter.StringVar()
    w3_1 = tkinter.StringVar()
    hh = tkinter.IntVar()
    hh2 = tkinter.IntVar()
    main_function()

    def cor():
        d.execute("SELECT * FROM current")
        x_ = d.fetchone()
        d.execute("DELETE FROM current")

        c_ = int(x_[0])
        d_ = int(x_[1])
        d_ += 1
        e_ = int(x_[2])
        c_ += 100
        z = input_score(c_, d_, e_)

        d.execute("INSERT INTO current VALUES (?, ?, ?)", (z.score, z.correct, z.incorrect))
        d.execute("SELECT * FROM current")
        xd = d.fetchone()
        s = xd[1] + xd[2]
        s2 = 100 / s
        xd1 = round(xd[1] * s2, 1)
        xd2 = round(xd[2] * s2, 1)
        print(str(xd1) + "% Correct")
        print(str(xd2) + "% Incorrect")

        #  this is the high score portion of the code
        d.execute("SELECT * FROM High")
        ok = d.fetchone()

        if int(z.score) > int(ok[0]):
            print("Beat High score")
            d.execute("DELETE FROM High")
            d.execute("INSERT INTO High VALUES (:scr)", {'scr': z.score})
            db1 = Label(window_main, text="                             ")
            db2 = Label(window_main, text=str(z.score))
            db1.place(x=55, y=10)
            db2.place(x=110, y=10)
            donn.commit()

        #  this is just "resetting" the buttons by just "coloring" over them with spaces
        main_function()

    def incor():
        d.execute("SELECT * FROM current")
        x_ = d.fetchone()
        d.execute("DELETE FROM current")

        c_ = int(x_[0])
        d_ = int(x_[1])
        e_ = int(x_[2])
        e_ += 1
        c_ -= 50
        z = input_score(c_, d_, e_)

        d.execute("INSERT INTO current VALUES (?, ?, ?)", (z.score, z.correct, z.incorrect))
        d.execute("SELECT * FROM current")
        xd = d.fetchone()
        s = xd[1] + xd[2]
        s2 = 100 / s
        xd1 = round(xd[1] * s2, 1)
        xd2 = round(xd[2] * s2, 1)
        print(str(xd1) + "% Correct")
        print(str(xd2) + "% Incorrect")

        #  print("incorrect")
        main_function()

    def f_et1():
        if y1 == ans:
            cor()
        else:
            incor()

    def f_et2():
        if y2 == ans:
            cor()
        else:
            incor()

    def f_et3():
        if y3 == ans:
            cor()
        else:
            incor()

    def f_et4():
        if y4 == ans:
            cor()
        else:
            incor()

    e1 = Button(window_main, text="Esc", command=esc_command)
    e2 = Button(window_main, textvariable=et1, command=f_et1)
    e3 = Button(window_main, textvariable=et2, command=f_et2)
    e4 = Button(window_main, textvariable=et3, command=f_et3)
    e5 = Button(window_main, textvariable=et4, command=f_et4)
    e6 = Label(window_main, textvariable=w3_0, font=("", 70))
    e7 = Label(window_main, textvariable=w3_1, font=("", 20))
    e8 = Label(window_main, text="Score:", font=("", 15))
    e9 = Label(window_main, text="High score:")
    e10 = Label(window_main, textvariable=hh)
    e11 = Label(window_main, textvariable=hh2, font=("", 15))

    e1.place(x=0, y=0)
    e2.place(x=1000, y=20)
    e3.place(x=1000, y=60)
    e4.place(x=1000, y=100)
    e5.place(x=1000, y=140)
    e6.place(x=360, y=20)
    e7.place(x=460, y=200)
    e8.place(x=35, y=35)
    e9.place(x=35, y=10)
    e10.place(x=110, y=10)
    e11.place(x=100, y=35)

    window_main.title("FlashCards")
    window_main.geometry("1250x405+5+5")
    window_main.resizable(False, False)
    window_main.mainloop()
    conn.close()


if __name__ == '__main__':
    main()
