from tkinter import *
from tkinter import messagebox
import sqlite3
import math, random
import requests



def finction():
    root1 = Tk()
    root1.title("GROCEMART")
    root1.geometry("1199x600+35+52")
    root1.resizable(False, False)

    frame1 = Frame(root1, bg="#f6ead4", bd=9, relief=GROOVE)
    frame1.place(x=0, y=115, height=391, width=1200)

    bill_title = Label(root1, bg="#f6ead4", font=("times new roman", 60, "bold"), relief=GROOVE, bd=12, fg="#51361a",
                       text="GROCEMART").pack(fill=X)

    bill_frame = Frame(frame1, bg="#f6ead4", relief=GROOVE, bd=10, borderwidth=9)
    bill_frame.place(x=508, y=1, width=360, height=370)

    option_frame = Frame(frame1, bg="#f6ead4", relief=GROOVE, bd=10, borderwidth=9)
    option_frame.place(x=210, y=1, width=295, height=370)

    last_frame = Frame(root1, bg="#f6ead4", relief=GROOVE, bd=10, borderwidth=9)
    last_frame.place(x=0, y=506, width=1200, height=94)

    global q_turmeric_powder
    global q_sugar
    global q_jaggery
    global q_old_rice
    global q_new_rice
    global q_sona_masoori
    global q_basmati
    global q_wheat_flour
    global q_maida
    global q_multi_grain
    global q_rice_flour
    global q_besan_flour
    global q_rava
    global q_rice_rava
    global q_corn_flour
    global q_vermicelli
    global q_tamarind
    global q_red_chilli
    q_turmeric_powder = 0
    q_sugar = 0
    q_jaggery = 0
    q_old_rice = 0
    q_new_rice = 0
    q_sona_masoori = 0
    q_basmati = 0
    q_wheat_flour = 0
    q_maida = 0
    q_multi_grain = 0
    q_rice_flour = 0
    q_besan_flour = 0
    q_rava = 0
    q_rice_rava = 0
    q_corn_flour = 0
    q_vermicelli = 0
    q_tamarind = 0
    q_red_chilli = 0

    global q_toor_dal
    global q_urad_dal
    global q_moong_dal
    global q_chana_dal
    global q_rajma
    global q_white_chana
    q_toor_dal = 0
    q_urad_dal = 0
    q_moong_dal = 0
    q_chana_dal = 0
    q_rajma = 0
    q_white_chana = 0

    global q_crystal_salt
    global q_powder_salt
    global q_redchilli_powder
    global q_dhania_powder
    global q_garammasala_powder
    global q_chatmasala_powder
    global q_pepper_powder
    global q_sambar_powder
    global q_biryani_powder
    global q_coffee_powder
    global q_tea_powder
    q_crystal_salt = 0
    q_powder_salt = 0
    q_redchilli_powder = 0
    q_dhania_powder = 0
    q_garammasala_powder = 0
    q_chatmasala_powder = 0
    q_pepper_powder = 0
    q_sambar_powder = 0
    q_biryani_powder = 0
    q_coffee_powder = 0
    q_tea_powder = 0

    global q_cooking_oil
    global q_seasame_oil
    global q_coconut_oil
    global q_ghee
    global q_olive_oil
    q_cooking_oil = 0
    q_seasame_oil = 0
    q_coconut_oil = 0
    q_ghee = 0
    q_olive_oil = 0

    global q_mustard_seed
    global q_pepper
    global q_jeera
    global q_khus_khus
    global q_dhania
    global q_black_seasame_seeds
    global q_white_seasame_seeds
    global q_cashew_nuts
    global q_raisins
    global q_badam
    global q_peanuts
    global q_dates
    q_mustard_seed = 0
    q_pepper = 0
    q_jeera = 0
    q_khus_khus = 0
    q_dhania = 0
    q_black_seasame_seeds = 0
    q_white_seasame_seeds = 0
    q_cashew_nuts = 0
    q_raisins = 0
    q_badam = 0
    q_peanuts = 0
    q_dates = 0

    global q_cheese_block
    global q_butter
    global q_yoghurt
    global q_fresh_cream
    global q_paneer
    q_cheese_block = 0
    q_butter = 0
    q_yoghurt = 0
    q_fresh_cream = 0
    q_paneer = 0

    global q_tooth_paste
    global q_tooth_brush
    global q_bathing_soap
    global q_shampoo
    global q_face_powder
    global q_hand_sanitizer
    global q_deodarant
    global q_shaving_cream
    global q_hair_gel
    global q_razer_blade
    q_tooth_paste = 0
    q_tooth_brush = 0
    q_bathing_soap = 0
    q_shampoo = 0
    q_face_powder = 0
    q_hand_sanitizer = 0
    q_deodarant = 0
    q_shaving_cream = 0
    q_hair_gel = 0
    q_razer_blade = 0

    global q_dish_washing_soap
    global q_dish_washing_liquid
    global q_washing_powder
    global q_washing_soaps
    global q_bleaching_powder
    global q_sanitary_pad
    global q_toilet_paper
    global q_garbage_bag
    global q_dettol
    global q_mosquito_liquid
    q_dish_washing_soap = 0
    q_dish_washing_liquid = 0
    q_washing_powder = 0
    q_washing_soaps = 0
    q_bleaching_powder = 0
    q_sanitary_pad = 0
    q_toilet_paper = 0
    q_garbage_bag = 0
    q_dettol = 0
    q_mosquito_liquid = 0

    global q_bandages
    global q_light_bulbs
    global q_batteries
    global q_candles
    q_bandages = 0
    q_light_bulbs = 0
    q_batteries = 0
    q_candles = 0

    global q_papad
    global q_horlicks
    global q_complan
    global q_noodles
    global q_pasta
    global q_ketchup
    global q_jam
    global q_bread_delux
    global q_bread_britania
    q_papad = 0
    q_horlicks = 0
    q_complan = 0
    q_noodles = 0
    q_pasta = 0
    q_ketchup = 0
    q_jam = 0
    q_bread_delux = 0
    q_bread_britania = 0

    global change_rice
    global change_pulses
    global change_spice
    global change_oils
    global change_snuts
    global change_dairy
    global change_toi
    global change_clean
    global change_mis
    global change_other

    change_rice = 0
    change_pulses = 0
    change_spice = 0
    change_oils = 0
    change_snuts = 0
    change_dairy = 0
    change_toi = 0
    change_clean = 0
    change_mis = 0
    change_other = 0

    def nine():
        if 'error' in result.get() or '=' in result.get():
            result.delete(0, "end")
            result.insert("end", "9")
        else:
            result.insert("end", "9")

    def eight():
        if 'error' in result.get() or '=' in result.get():
            result.delete(0, "end")
            result.insert("end", "8")
        else:
            result.insert("end", "8")

    def seven():
        if 'error' in result.get() or '=' in result.get():
            result.delete(0, "end")
            result.insert("end", "7")
        else:
            result.insert("end", "7")

    def six():
        if 'error' in result.get() or '=' in result.get():
            result.delete(0, "end")
            result.insert("end", "6")
        else:
            result.insert("end", "6")

    def five():
        if 'error' in result.get() or '=' in result.get():
            result.delete(0, "end")
            result.insert("end", "5")
        else:
            result.insert("end", "5")

    def four():
        if 'error' in result.get() or '=' in result.get():
            result.delete(0, "end")
            result.insert("end", "4")
        else:
            result.insert("end", "4")

    def three():
        if 'error' in result.get() or '=' in result.get():
            result.delete(0, "end")
            result.insert("end", "3")
        else:
            result.insert("end", "3")

    def two():
        if 'error' in result.get() or '=' in result.get():
            result.delete(0, "end")
            result.insert("end", "2")
        else:
            result.insert("end", "2")

    def one():
        if 'error' in result.get() or '=' in result.get():
            result.delete(0, "end")
            result.insert("end", "1")
        else:
            result.insert("end", "1")

    def zero():
        if 'error' in result.get() or '=' in result.get():
            result.delete(0, "end")
            result.insert("end", "0")
        else:
            result.insert("end", "0")

    def plus():
        if 'error' in result.get() or '=' in result.get():
            result.delete(0, "end")
            result.insert("end", "+")
        else:
            result.insert("end", "+")

    def minus():
        if 'error' in result.get() or '=' in result.get():
            result.delete(0, "end")
            result.insert("end", "-")
        else:
            result.insert("end", "-")

    def mul():
        if 'error' in result.get() or '=' in result.get():
            result.delete(0, "end")
            result.insert("end", "*")
        else:
            result.insert("end", "*")

    def divide():
        if 'error' in result.get() or '=' in result.get():
            result.delete(0, "end")
            result.insert("end", "/")
        else:
            result.insert("end", "/")

    def equal():
        if result.get() == "":
            result.insert("end", "error")
        elif result.get()[0] == "0" or result.get()[0] == "+" or result.get()[0] == "*" or result.get()[0] == "/":
            result.delete(0, "end")
            result.insert("end", "error")
        elif 'error' in result.get() or '=' in result.get():
            result.delete(0, "end")


        else:
            res = result.get()
            res = eval(res)
            result.insert("end", " = ")
            result.insert("end", res)

    def clear():
        result.delete(0, "end")

    cal_frame = Frame(frame1, relief=GROOVE, bg="#f6ead4", bd=9)
    cal_frame.place(x=870, y=0, width=315, height=375)

    title_label = Label(cal_frame, text="CALCULATOR", bg='#b4a284', fg="#51361a", bd=4, relief=GROOVE, width=24,
                        font=("times new roman", 15, "bold")).place(x=0, y=0)

    result = Entry(cal_frame, width=48, relief=SUNKEN, font=("times new roman", 9, "bold"), borderwidth=3)
    result.grid(row=0, column=0, pady=(25, 0), columnspan=4)

    nine = Button(cal_frame, text="9", width=7, height=4, relief=RAISED, borderwidth=2, font=('verdana', 10, 'bold'),
                  bg='#f6ead4',
                  fg="#51361a", command=nine)
    nine.grid(row=1, column=0)
    eight = Button(cal_frame, text="8", width=7, height=4, relief=RAISED, borderwidth=2, font=('verdana', 10, 'bold'),
                   bg='#f6ead4',
                   fg="#51361a", command=eight)
    eight.grid(row=1, column=1)
    seven = Button(cal_frame, text="7", width=7, height=4, relief=RAISED, borderwidth=2, font=('verdana', 10, 'bold'),
                   bg='#f6ead4',
                   fg="#51361a", command=seven)
    seven.grid(row=1, column=2)
    plus = Button(cal_frame, text="+", width=7, height=4, relief=RAISED, borderwidth=2, font=('verdana', 10, 'bold'),
                  bg='#f6ead4',
                  fg="#51361a", command=plus)
    plus.grid(row=1, column=3)

    six = Button(cal_frame, text="6", width=7, height=4, relief=RAISED, borderwidth=2, font=('verdana', 10, 'bold'),
                 bg='#f6ead4',
                 fg="#51361a", command=six)
    six.grid(row=2, column=0)
    five = Button(cal_frame, text="5", width=7, height=4, relief=RAISED, borderwidth=2, font=('verdana', 10, 'bold'),
                  bg='#f6ead4',
                  fg="#51361a", command=five)
    five.grid(row=2, column=1)
    four = Button(cal_frame, text="4", width=7, height=4, relief=RAISED, borderwidth=2, font=('verdana', 10, 'bold'),
                  bg='#f6ead4',
                  fg="#51361a", command=four)
    four.grid(row=2, column=2)
    minus = Button(cal_frame, text="-", width=7, height=4, relief=RAISED, borderwidth=2, font=('verdana', 10, 'bold'),
                   bg='#f6ead4',
                   fg="#51361a", command=minus)
    minus.grid(row=2, column=3)
    three = Button(cal_frame, text="3", width=7, height=4, relief=RAISED, borderwidth=2, font=('verdana', 10, 'bold'),
                   bg='#f6ead4',
                   fg="#51361a", command=three)
    three.grid(row=3, column=0)
    two = Button(cal_frame, text="2", width=7, height=4, relief=RAISED, borderwidth=2, font=('verdana', 10, 'bold'),
                 bg='#f6ead4',
                 fg="#51361a", command=two)
    two.grid(row=3, column=1)
    one = Button(cal_frame, text="1", width=7, height=4, relief=RAISED, borderwidth=2, font=('verdana', 10, 'bold'),
                 bg='#f6ead4',
                 fg="#51361a", command=one)
    one.grid(row=3, column=2)
    multiply = Button(cal_frame, text="*", width=7, height=4, relief=RAISED, borderwidth=2,
                      font=('verdana', 10, 'bold'),
                      bg='#f6ead4',
                      fg="#51361a", command=mul)
    multiply.grid(row=3, column=3)

    zero = Button(cal_frame, text="0", width=7, height=4, relief=RAISED, borderwidth=2, font=('verdana', 10, 'bold'),
                  bg='#f6ead4',
                  fg="#51361a", command=zero)
    zero.grid(row=4, column=0)
    clear = Button(cal_frame, text="C", width=7, height=4, relief=RAISED, borderwidth=2, font=('verdana', 10, 'bold'),
                   bg='#f6ead4',
                   fg="#51361a", command=clear)
    clear.grid(row=4, column=1)
    equal = Button(cal_frame, text="=", width=7, height=4, relief=RAISED, borderwidth=2, font=('verdana', 10, 'bold'),
                   bg='#f6ead4',
                   fg="#51361a", command=equal)
    equal.grid(row=4, column=2)
    divide = Button(cal_frame, text="/", width=7, height=4, relief=RAISED, borderwidth=2, font=('verdana', 10, 'bold'),
                    bg='#f6ead4',
                    fg="#51361a", command=divide)
    divide.grid(row=4, column=3)

    def cal1():
        global q_turmeric_powder
        global q_sugar
        global q_jaggery
        global q_old_rice
        global q_new_rice
        global q_sona_masoori
        global q_basmati
        global q_wheat_flour
        global q_maida
        global q_multi_grain
        global q_rice_flour
        global q_besan_flour
        global q_rava
        global q_rice_rava
        global q_corn_flour
        global q_vermicelli
        global q_tamarind
        global q_red_chilli

        q_turmeric_powder = 0
        q_sugar = 0
        q_jaggery = 0
        q_old_rice = 0
        q_new_rice = 0
        q_sona_masoori = 0
        q_basmati = 0
        q_wheat_flour = 0
        q_maida = 0
        q_multi_grain = 0
        q_rice_flour = 0
        q_besan_flour = 0
        q_rava = 0
        q_rice_rava = 0
        q_corn_flour = 0
        q_vermicelli = 0
        q_tamarind = 0
        q_red_chilli = 0

        valid_number = 0

        if e_turmeric_powder.get() == "" or e_turmeric_powder.get() == 0:
            q_turmeric_powder = 0
        else:
            try:
                q_turmeric_powder = float(e_turmeric_powder.get())
            except:
                valid_number = 1

        if e_sugar.get() == "" or e_sugar.get() == 0:
            q_sugar = 0
        else:
            try:
                q_sugar = float(e_sugar.get())
            except:
                valid_number = 1

        if e_jaggery.get() == "" or e_jaggery.get() == 0:
            q_jaggery = 0
        else:
            try:
                q_jaggery = float(e_jaggery.get())
            except:
                valid_number = 1

        if e_old_rice.get() == "" or e_old_rice.get() == 0:
            q_old_rice = 0
        else:
            try:
                q_old_rice = float(e_old_rice.get())
            except:
                valid_number = 1

        if e_new_rice.get() == "" or e_new_rice.get() == 0:
            q_new_rice = 0
        else:
            try:
                q_new_rice = float(e_new_rice.get())
            except:
                valid_number = 1

        if e_sona_masoori.get() == "" or e_sona_masoori.get() == 0:
            q_sona_masoori = 0
        else:
            try:
                q_sona_masoori = float(e_sona_masoori.get())
            except:
                valid_number = 1

        if e_basmati.get() == "" or e_basmati.get() == 0:
            q_basmati = 0
        else:
            try:
                q_basmati = float(e_basmati.get())
            except:
                valid_number = 1

        if e_wheat_flour.get() == "" or e_wheat_flour.get() == 0:
            q_wheat_flour = 0
        else:
            try:
                q_wheat_flour = float(e_wheat_flour.get())
            except:
                valid_number = 1

        if e_maida.get() == "" or e_maida.get() == 0:
            q_maida = 0
        else:
            try:
                q_maida = float(e_maida.get())
            except:
                valid_number = 1

        if e_multi_grain.get() == "" or e_multi_grain.get() == 0:
            q_multi_grain = 0
        else:
            try:
                q_multi_grain = float(e_multi_grain.get())
            except:
                valid_number = 1

        if e_rice_flour.get() == "" or e_rice_flour.get() == 0:
            q_rice_flour = 0
        else:
            try:
                q_rice_flour = float(e_rice_flour.get())
            except:
                valid_number = 1

        if e_besan_flour.get() == "" or e_besan_flour.get() == 0:
            q_besan_flour = 0
        else:
            try:
                q_besan_flour = float(e_besan_flour.get())
            except:
                valid_number = 1

        if e_rava.get() == "" or e_rava.get() == 0:
            q_rava = 0
        else:
            try:
                q_rava = float(e_rava.get())
            except:
                valid_number = 1

        if e_corn_flour.get() == "" or e_corn_flour.get() == 0:
            q_corn_flour = 0
        else:
            try:
                q_corn_flour = float(e_corn_flour.get())
            except:
                valid_number = 1

        if e_vermicelli.get() == "" or e_vermicelli.get() == 0:
            q_vermicelli = 0
        else:
            try:
                q_vermicelli = float(e_vermicelli.get())
            except:
                valid_number = 1

        if e_tamarind.get() == "" or e_tamarind.get() == 0:
            q_tamarind = 0
        else:
            try:
                q_tamarind = float(e_tamarind.get())
            except:
                valid_number = 1

        if e_red_chilli.get() == "" or e_red_chilli.get() == 0:
            q_red_chilli = 0
        else:
            try:
                q_red_chilli = float(e_red_chilli.get())
            except:
                valid_number = 1
        '''
        divv = (int(q_turmeric_powder)) +(int(q_sugar)) +(int(q_toor_dal))

        king = Label(innerframe1, text=divv)
        king.grid(row=19, column=1, padx=0)
        '''
        if valid_number == 1:
            messagebox.showerror("NUMBER", "PLEASE ENTER A VALID NUMBER", parent=innerframe1)
        innerframe1.destroy()

    def rice():
        global innerframe1
        global e_turmeric_powder
        global e_sugar
        global e_jaggery
        global e_old_rice
        global e_new_rice
        global e_sona_masoori
        global e_basmati
        global e_wheat_flour
        global e_maida
        global e_multi_grain
        global e_rice_flour
        global e_besan_flour
        global e_rava
        global e_rice_rava
        global e_corn_flour
        global e_vermicelli
        global e_tamarind
        global e_red_chilli

        global change_rice
        change_rice = 1

        global rice1
        global rice2
        global rice3
        global rice4
        global rice5
        global rice6
        global rice7
        global rice8
        global rice9
        global rice10
        global rice11
        global rice12
        global rice13
        global rice14
        global rice15
        global rice16
        global rice17
        global rice18

        global r1
        global r2
        global r3
        global r4
        global r5
        global r6
        global r7
        global r8
        global r9
        global r10
        global r11
        global r12
        global r13
        global r14
        global r15
        global r16
        global r17
        global r18

        r1 = IntVar()
        r2 = IntVar()
        r3 = IntVar()
        r4 = IntVar()
        r5 = IntVar()
        r6 = IntVar()
        r7 = IntVar()
        r8 = IntVar()
        r9 = IntVar()
        r10 = IntVar()
        r11 = IntVar()
        r12 = IntVar()
        r13 = IntVar()
        r14 = IntVar()
        r15 = IntVar()
        r16 = IntVar()
        r17 = IntVar()
        r18 = IntVar()

        r1.set(0)
        r2.set(0)
        r3.set(0)
        r4.set(0)
        r5.set(0)
        r6.set(0)
        r7.set(0)
        r8.set(0)
        r9.set(0)
        r10.set(0)
        r11.set(0)
        r12.set(0)
        r13.set(0)
        r14.set(0)
        r15.set(0)
        r16.set(0)
        r17.set(0)
        r18.set(0)

        innerframe1 = Toplevel(bg="#f6ead4", relief=GROOVE, bd=9)
        # innerframe1.geometry("500x200+200+100")
        innerframe1.title("RICE AND FLOURS")
        turmeric_powder = Label(innerframe1, text="TURMERIC POWDER ", font=("Goudy old style", 15, "bold"),
                                fg="#51361a",
                                bg="#f6ead4")
        turmeric_powder.grid(row=0, column=0)
        sugar = Label(innerframe1, text="SUGAR ", font=("Goudy old style", 15, "bold"), fg="#51361a",
                      bg="#f6ead4")
        sugar.grid(row=1, column=0)
        jaggery = Label(innerframe1, text="JAGGERY ", font=("Goudy old style", 15, "bold"), fg="#51361a",
                        bg="#f6ead4")
        jaggery.grid(row=2, column=0)
        old_rice = Label(innerframe1, text="OLD RICE ( in kg) ", font=("Goudy old style", 15, "bold"), fg="#51361a",
                         bg="#f6ead4")
        old_rice.grid(row=3, column=0)
        new_rice = Label(innerframe1, text="NEW RICE ( in kg ) ", font=("Goudy old style", 15, "bold"), fg="#51361a",
                         bg="#f6ead4")
        new_rice.grid(row=4, column=0)
        sona_masoori = Label(innerframe1, text="SONA MASOORI", font=("Goudy old style", 15, "bold"), fg="#51361a",
                             bg="#f6ead4")
        sona_masoori.grid(row=5, column=0)
        basmati = Label(innerframe1, text="BASMATI RICE", font=("Goudy old style", 15, "bold"), fg="#51361a",
                        bg="#f6ead4")
        basmati.grid(row=6, column=0)
        wheat_flour = Label(innerframe1, text="WHEAT FLOUR", font=("Goudy old style", 15, "bold"), fg="#51361a",
                            bg="#f6ead4")
        wheat_flour.grid(row=7, column=0)
        maida = Label(innerframe1, text="MAIDA", font=("Goudy old style", 15, "bold"), fg="#51361a",
                      bg="#f6ead4")
        maida.grid(row=8, column=0)
        multi_grain = Label(innerframe1, text="MULTI GRAINS", font=("Goudy old style", 15, "bold"), fg="#51361a",
                            bg="#f6ead4")
        multi_grain.grid(row=9, column=0)
        rice_flour = Label(innerframe1, text="RICE FLOUR", font=("Goudy old style", 15, "bold"), fg="#51361a",
                           bg="#f6ead4")
        rice_flour.grid(row=10, column=0)
        besan_flour = Label(innerframe1, text="BESAN FLOUR", font=("Goudy old style", 15, "bold"), fg="#51361a",
                            bg="#f6ead4")
        besan_flour.grid(row=11, column=0)
        rava = Label(innerframe1, text="RAVA", font=("Goudy old style", 15, "bold"), fg="#51361a",
                     bg="#f6ead4")
        rava.grid(row=12, column=0)
        rice_rava = Label(innerframe1, text="RICE RAVA", font=("Goudy old style", 15, "bold"), fg="#51361a",
                          bg="#f6ead4")
        rice_rava.grid(row=13, column=0)
        corn_flour = Label(innerframe1, text="COURN FLOUR", font=("Goudy old style", 15, "bold"), fg="#51361a",
                           bg="#f6ead4")
        corn_flour.grid(row=14, column=0)
        vermicelli = Label(innerframe1, text="VERMICELLI ( SEVIAYAN )", font=("Goudy old style", 15, "bold"),
                           fg="#51361a",
                           bg="#f6ead4")
        vermicelli.grid(row=15, column=0)
        tamarind = Label(innerframe1, text="TAMARIND", font=("Goudy old style", 15, "bold"), fg="#51361a",
                         bg="#f6ead4")
        tamarind.grid(row=16, column=0)
        red_chilli = Label(innerframe1, text="RED CHILLI", font=("Goudy old style", 15, "bold"), fg="#51361a",
                           bg="#f6ead4")
        red_chilli.grid(row=17, column=0)

        e_turmeric_powder = Entry(innerframe1, width=50, relief=SUNKEN, bd=4)
        e_turmeric_powder.grid(row=0, column=2)
        e_sugar = Entry(innerframe1, width=50, relief=SUNKEN, bd=4)
        e_sugar.grid(row=1, column=2)
        e_jaggery = Entry(innerframe1, width=50, relief=SUNKEN, bd=4)
        e_jaggery.grid(row=2, column=2)
        e_old_rice = Entry(innerframe1, width=50, relief=SUNKEN, bd=4)
        e_old_rice.grid(row=3, column=2)
        e_new_rice = Entry(innerframe1, width=50, relief=SUNKEN, bd=4)
        e_new_rice.grid(row=4, column=2)
        e_sona_masoori = Entry(innerframe1, width=50, relief=SUNKEN, bd=4)
        e_sona_masoori.grid(row=5, column=2)
        e_basmati = Entry(innerframe1, width=50, relief=SUNKEN, bd=4)
        e_basmati.grid(row=6, column=2)
        e_wheat_flour = Entry(innerframe1, width=50, relief=SUNKEN, bd=4)
        e_wheat_flour.grid(row=7, column=2)
        e_maida = Entry(innerframe1, width=50, relief=SUNKEN, bd=4)
        e_maida.grid(row=8, column=2)
        e_multi_grain = Entry(innerframe1, width=50, relief=SUNKEN, bd=4)
        e_multi_grain.grid(row=9, column=2)
        e_rice_flour = Entry(innerframe1, width=50, relief=SUNKEN, bd=4)
        e_rice_flour.grid(row=10, column=2)
        e_besan_flour = Entry(innerframe1, width=50, relief=SUNKEN, bd=4)
        e_besan_flour.grid(row=11, column=2)
        e_rava = Entry(innerframe1, width=50, relief=SUNKEN, bd=4)
        e_rava.grid(row=12, column=2)
        e_rice_rava = Entry(innerframe1, width=50, relief=SUNKEN, bd=4)
        e_rice_rava.grid(row=13, column=2)
        e_corn_flour = Entry(innerframe1, width=50, relief=SUNKEN, bd=4)
        e_corn_flour.grid(row=14, column=2)
        e_vermicelli = Entry(innerframe1, width=50, relief=SUNKEN, bd=4)
        e_vermicelli.grid(row=15, column=2)
        e_tamarind = Entry(innerframe1, width=50, relief=SUNKEN, bd=4)
        e_tamarind.grid(row=16, column=2)
        e_red_chilli = Entry(innerframe1, width=50, relief=SUNKEN, bd=4)
        e_red_chilli.grid(row=17, column=2)

        rice1 = Checkbutton(innerframe1, text="", fg="#51361a", bg="#f6ead4", variable=r1)
        rice1.grid(row=0, column=3)
        rice2 = Checkbutton(innerframe1, text="", fg="#51361a", bg="#f6ead4", variable=r2)
        rice2.grid(row=1, column=3)
        rice3 = Checkbutton(innerframe1, text="", fg="#51361a", bg="#f6ead4", variable=r3)
        rice3.grid(row=2, column=3)
        rice4 = Checkbutton(innerframe1, text="", fg="#51361a", bg="#f6ead4", variable=r4)
        rice4.grid(row=3, column=3)
        rice5 = Checkbutton(innerframe1, text="", fg="#51361a", bg="#f6ead4", variable=r5)
        rice5.grid(row=4, column=3)
        rice6 = Checkbutton(innerframe1, text="", fg="#51361a", bg="#f6ead4", variable=r6)
        rice6.grid(row=5, column=3)
        rice7 = Checkbutton(innerframe1, text="", fg="#51361a", bg="#f6ead4", variable=r7)
        rice7.grid(row=6, column=3)
        rice8 = Checkbutton(innerframe1, text="", fg="#51361a", bg="#f6ead4", variable=r8)
        rice8.grid(row=7, column=3)
        rice9 = Checkbutton(innerframe1, text="", fg="#51361a", bg="#f6ead4", variable=r9)
        rice9.grid(row=8, column=3)
        rice10 = Checkbutton(innerframe1, text="", fg="#51361a", bg="#f6ead4", variable=r10)
        rice10.grid(row=9, column=3)
        rice11 = Checkbutton(innerframe1, text="", fg="#51361a", bg="#f6ead4", variable=r11)
        rice11.grid(row=10, column=3)
        rice12 = Checkbutton(innerframe1, text="", fg="#51361a", bg="#f6ead4", variable=r12)
        rice12.grid(row=11, column=3)
        rice13 = Checkbutton(innerframe1, text="", fg="#51361a", bg="#f6ead4", variable=r13)
        rice13.grid(row=12, column=3)
        rice14 = Checkbutton(innerframe1, text="", fg="#51361a", bg="#f6ead4", variable=r14)
        rice14.grid(row=13, column=3)
        rice15 = Checkbutton(innerframe1, text="", fg="#51361a", bg="#f6ead4", variable=r15)
        rice15.grid(row=14, column=3)
        rice16 = Checkbutton(innerframe1, text="", fg="#51361a", bg="#f6ead4", variable=r16)
        rice16.grid(row=15, column=3)
        rice17 = Checkbutton(innerframe1, text="", fg="#51361a", bg="#f6ead4", variable=r17)
        rice17.grid(row=16, column=3)
        rice18 = Checkbutton(innerframe1, text="", fg="#51361a", bg="#f6ead4", variable=r18)
        rice18.grid(row=17, column=3)

        total = Button(innerframe1, text="TOTAL", command=cal1, width=20, font=("times new roaman", 15, "bold"),
                       fg="#51361a", bg="#b4a284", relief=GROOVE, bd=9)
        total.grid(row=18, column=0, columnspan=3)

    def cal2():

        global q_toor_dal
        global q_urad_dal
        global q_moong_dal
        global q_chana_dal
        global q_rajma
        global q_white_chana
        q_toor_dal = 0
        q_urad_dal = 0
        q_moong_dal = 0
        q_chana_dal = 0
        q_rajma = 0
        q_white_chana = 0

        valid_number = 0

        if e_toor_dal.get() == "" or e_toor_dal.get() == 0:
            q_toor_dal = 0
        else:
            try:
                q_toor_dal = float(e_toor_dal.get())
            except:
                valid_number = 1
        # temp = Label(innerframe2, text=q_toor_dal)
        # temp.grid(row=7, column=0, columnspan=3)
        if e_urad_dal.get() == "" or e_urad_dal.get() == 0:
            q_urad_dal = 0
        else:
            try:
                q_urad_dal = float(e_urad_dal.get())
            except:
                valid_number = 1
        # temp1 = Label(innerframe2, text=q_urad_dal)
        # temp1.grid(row=8, column=0, columnspan=3)

        if e_moong_dal.get() == "" or e_moong_dal.get() == 0:
            q_moong_dal = 0
        else:
            try:
                q_moong_dal = float(e_moong_dal.get())
            except:
                valid_number = 1

        if e_chana_dal.get() == "" or e_chana_dal.get() == 0:
            q_chana_dal = 0
        else:
            try:
                q_chana_dal = float(e_chana_dal.get())
            except:
                valid_number = 1

        if e_rajma.get() == "" or e_rajma.get() == 0:
            q_rajma = 0
        else:
            try:
                q_rajma = float(e_rajma.get())
            except:
                valid_number = 1

        if e_white_chana.get() == "" or e_white_chana.get() == 0:
            q_white_chana = 0
        else:
            try:
                q_white_chana = float(e_white_chana.get())
            except:
                valid_number = 1

        if valid_number == 1:
            messagebox.showerror("NUMBER", "PLEASE ENTER A VALID NUMBER", parent=innerframe2)
        innerframe2.destroy()

    def chech():
        label.config(text=p1.get())

    def pulses():
        global e_toor_dal
        global e_urad_dal
        global e_moong_dal
        global e_chana_dal
        global e_rajma
        global e_white_chana
        global innerframe2

        global pulses1
        global pulses2
        global pulses3
        global pulses4
        global pulses5
        global pulses6

        global change_pulses
        change_pulses = 1

        global p1
        global p2
        global p3
        global p4
        global p5
        global p6

        p1 = IntVar()
        p2 = IntVar()
        p3 = IntVar()
        p4 = IntVar()
        p5 = IntVar()
        p6 = IntVar()

        p1.set(0)
        p2.set(0)
        p3.set(0)
        p4.set(0)
        p5.set(0)
        p6.set(0)

        innerframe2 = Toplevel(bg="#f6ead4", relief=GROOVE, bd=9)
        # innerframe1.geometry("500x200+200+100")
        innerframe2.title("PULSES AND DALS")
        toor_dal = Label(innerframe2, text="TOOR DAL", font=("Goudy old style", 15, "bold"), fg="#51361a",
                         bg="#f6ead4")
        toor_dal.grid(row=0, column=0)
        urad_dal = Label(innerframe2, text="URAD DAL", font=("Goudy old style", 15, "bold"), fg="#51361a",
                         bg="#f6ead4")
        urad_dal.grid(row=1, column=0)
        moong_dal = Label(innerframe2, text="YELLOW MOONG DAAL", font=("Goudy old style", 15, "bold"), fg="#51361a",
                          bg="#f6ead4")
        moong_dal.grid(row=2, column=0)
        chana_dal = Label(innerframe2, text="CHANA DAL", font=("Goudy old style", 15, "bold"), fg="#51361a",
                          bg="#f6ead4")
        chana_dal.grid(row=3, column=0)
        rajma = Label(innerframe2, text="RAJMA( in kg ) ", font=("Goudy old style", 15, "bold"), fg="#51361a",
                      bg="#f6ead4")
        rajma.grid(row=4, column=0)
        white_chana = Label(innerframe2, text="WHITE CHANA", font=("Goudy old style", 15, "bold"), fg="#51361a",
                            bg="#f6ead4")
        white_chana.grid(row=5, column=0)

        e_toor_dal = Entry(innerframe2, width=50, relief=SUNKEN, bd=4)
        e_toor_dal.grid(row=0, column=2)
        e_urad_dal = Entry(innerframe2, width=50, relief=SUNKEN, bd=4)
        e_urad_dal.grid(row=1, column=2)
        e_moong_dal = Entry(innerframe2, width=50, relief=SUNKEN, bd=4)
        e_moong_dal.grid(row=2, column=2)
        e_chana_dal = Entry(innerframe2, width=50, relief=SUNKEN, bd=4)
        e_chana_dal.grid(row=3, column=2)
        e_rajma = Entry(innerframe2, width=50, relief=SUNKEN, bd=4)
        e_rajma.grid(row=4, column=2)
        e_white_chana = Entry(innerframe2, width=50, relief=SUNKEN, bd=4)
        e_white_chana.grid(row=5, column=2)

        pulses1 = Checkbutton(innerframe2, text="", fg="#51361a", bg="#f6ead4", variable=p1)
        pulses1.grid(row=0, column=3)
        pulses2 = Checkbutton(innerframe2, text="", fg="#51361a", bg="#f6ead4", variable=p2)
        pulses2.grid(row=1, column=3)
        pulses3 = Checkbutton(innerframe2, text="", fg="#51361a", bg="#f6ead4", variable=p3)
        pulses3.grid(row=2, column=3)
        pulses4 = Checkbutton(innerframe2, text="", fg="#51361a", bg="#f6ead4", variable=p4)
        pulses4.grid(row=3, column=3)
        pulses5 = Checkbutton(innerframe2, text="", fg="#51361a", bg="#f6ead4", variable=p5)
        pulses5.grid(row=4, column=3)
        pulses6 = Checkbutton(innerframe2, text="", fg="#51361a", bg="#f6ead4", variable=p6)
        pulses6.grid(row=5, column=3)
        global label
        label = Label(root1, text="")
        label.pack(pady=50)

        tot = Button(innerframe2, text="TOTAL", command=chech, width=20, font=("times new roaman", 15, "bold"),
                     fg="#51361a", bg="#b4a284", relief=GROOVE, bd=9)
        tot.grid(row=8, column=0, columnspan=3)

        total2 = Button(innerframe2, text="TOTAL", command=cal2, width=20, font=("times new roaman", 15, "bold"),
                        fg="#51361a", bg="#b4a284", relief=GROOVE, bd=9)
        total2.grid(row=6, column=0, columnspan=3)

    def cal3():
        global q_crystal_salt
        global q_powder_salt
        global q_redchilli_powder
        global q_dhania_powder
        global q_garammasala_powder
        global q_chatmasala_powder
        global q_pepper_powder
        global q_sambar_powder
        global q_biryani_powder
        global q_coffee_powder
        global q_tea_powder

        q_crystal_salt = 0
        q_powder_salt = 0
        q_redchilli_powder = 0
        q_dhania_powder = 0
        q_garammasala_powder = 0
        q_chatmasala_powder = 0
        q_pepper_powder = 0
        q_sambar_powder = 0
        q_biryani_powder = 0
        q_coffee_powder = 0
        q_tea_powder = 0

        valid_number = 0

        if e_crystal_salt.get() == "" or e_crystal_salt.get() == 0:
            q_crystal_salt = 0
        else:
            try:
                q_crystal_salt = float(e_crystal_salt.get())
            except:
                valid_number = 1

        if e_powder_salt.get() == "" or e_powder_salt.get() == 0:
            q_powder_salt = 0
        else:
            try:
                q_powder_salt = float(e_powder_salt.get())
            except:
                valid_number = 1

        if e_redchilli_powder.get() == "" or e_redchilli_powder.get() == 0:
            q_redchilli_powder = 0
        else:
            try:
                q_redchilli_powder = float(e_redchilli_powder.get())
            except:
                valid_number = 1

        if e_dhania_powder.get() == "" or e_dhania_powder.get() == 0:
            q_dhania_powder = 0
        else:
            try:
                q_dhania_powder = float(e_dhania_powder.get())
            except:
                valid_number = 1

        if e_garammasala_powder.get() == "" or e_garammasala_powder.get() == 0:
            q_garammasala_powder = 0
        else:
            try:
                q_garammasala_powder = float(e_garammasala_powder.get())
            except:
                valid_number = 1

        if e_chatmasala_powder.get() == "" or e_chatmasala_powder.get() == 0:
            q_chatmasala_powder = 0
        else:
            try:
                q_chatmasala_powder = float(e_chatmasala_powder.get())
            except:
                valid_number = 1

        if e_pepper_powder.get() == "" or e_pepper_powder.get() == 0:
            q_pepper_powder = 0
        else:
            try:
                q_pepper_powder = float(e_pepper_powder.get())
            except:
                valid_number = 1

        if e_sambar_powder.get() == "" or e_sambar_powder.get() == 0:
            q_sambar_powder = 0
        else:
            try:
                q_sambar_powder = float(e_sambar_powder.get())
            except:
                valid_number = 1

        if e_biryani_powder.get() == "" or e_biryani_powder.get() == 0:
            q_biryani_powder = 0
        else:
            try:
                q_biryani_powder = float(e_biryani_powder.get())
            except:
                valid_number = 1

        if e_coffee_powder.get() == "" or e_coffee_powder.get() == 0:
            q_coffee_powder = 0
        else:
            try:
                q_coffee_powder = float(e_coffee_powder.get())
            except:
                valid_number = 1

        if e_tea_powder.get() == "" or e_tea_powder.get() == 0:
            q_tea_powder = 0
        else:
            try:
                q_tea_powder = float(e_tea_powder.get())
            except:
                valid_number = 1
        if valid_number == 1:
            messagebox.showerror("NUMBER", "PLEASE ENTER A VALID NUMBER", parent=innerframe3)
        innerframe3.destroy()

    def spices():
        global innerframe3
        global e_crystal_salt
        global e_powder_salt
        global e_redchilli_powder
        global e_dhania_powder
        global e_garammasala_powder
        global e_chatmasala_powder
        global e_pepper_powder
        global e_sambar_powder
        global e_biryani_powder
        global e_coffee_powder
        global e_tea_powder

        global spices1
        global spices2
        global spices3
        global spices4
        global spices5
        global spices6
        global spices7
        global spices8
        global spices9
        global spices10
        global spices11

        global change_spice
        change_spice = 1

        global sp1
        global sp2
        global sp3
        global sp4
        global sp5
        global sp6
        global sp7
        global sp8
        global sp9
        global sp10
        global sp11

        sp1 = IntVar()
        sp2 = IntVar()
        sp3 = IntVar()
        sp4 = IntVar()
        sp5 = IntVar()
        sp6 = IntVar()
        sp7 = IntVar()
        sp8 = IntVar()
        sp9 = IntVar()
        sp10 = IntVar()
        sp11 = IntVar()

        sp1.set(0)
        sp2.set(0)
        sp3.set(0)
        sp4.set(0)
        sp5.set(0)
        sp6.set(0)
        sp7.set(0)
        sp8.set(0)
        sp9.set(0)
        sp10.set(0)
        sp11.set(0)

        innerframe3 = Toplevel(bg="#f6ead4", relief=GROOVE, bd=9)
        # innerframe3.geometry("500x200+200+100")
        innerframe3.title("RICE AND FLOURS")
        crystal_salt = Label(innerframe3, text="CRYSTAL SALT ", font=("Goudy old style", 15, "bold"), fg="#51361a",
                             bg="#f6ead4")
        crystal_salt.grid(row=0, column=0)
        powder_salt = Label(innerframe3, text="SALT POWDER ", font=("Goudy old style", 15, "bold"), fg="#51361a",
                            bg="#f6ead4")
        powder_salt.grid(row=1, column=0)
        redchilli_powder = Label(innerframe3, text="RED CHILLI POWDER", font=("Goudy old style", 15, "bold"),
                                 fg="#51361a",
                                 bg="#f6ead4")
        redchilli_powder.grid(row=2, column=0)
        dhania_powder = Label(innerframe3, text="DHANIA POWDER ", font=("Goudy old style", 15, "bold"), fg="#51361a",
                              bg="#f6ead4")
        dhania_powder.grid(row=3, column=0)
        garammasala_powder = Label(innerframe3, text="GARAM MASALA POWDER ", font=("Goudy old style", 15, "bold"),
                                   fg="#51361a",
                                   bg="#f6ead4")
        garammasala_powder.grid(row=4, column=0)
        chatmasala_powder = Label(innerframe3, text="CHAT MASALA POWDER", font=("Goudy old style", 15, "bold"),
                                  fg="#51361a",
                                  bg="#f6ead4")
        chatmasala_powder.grid(row=5, column=0)
        pepper_powder = Label(innerframe3, text="PEPPER POWDER", font=("Goudy old style", 15, "bold"), fg="#51361a",
                              bg="#f6ead4")
        pepper_powder.grid(row=6, column=0)
        sambar_powder = Label(innerframe3, text="SAMBAR POWDER ", font=("Goudy old style", 15, "bold"), fg="#51361a",
                              bg="#f6ead4")
        sambar_powder.grid(row=7, column=0)
        biryani_powder = Label(innerframe3, text="BIRYANI POWDER", font=("Goudy old style", 15, "bold"), fg="#51361a",
                               bg="#f6ead4")
        biryani_powder.grid(row=8, column=0)
        coffee_powder = Label(innerframe3, text="COFFEE POWDER", font=("Goudy old style", 15, "bold"), fg="#51361a",
                              bg="#f6ead4")
        coffee_powder.grid(row=9, column=0)
        tea_powder = Label(innerframe3, text="TEA POWDER", font=("Goudy old style", 15, "bold"), fg="#51361a",
                           bg="#f6ead4")
        tea_powder.grid(row=10, column=0)

        e_crystal_salt = Entry(innerframe3, width=50, relief=SUNKEN, bd=4)
        e_crystal_salt.grid(row=0, column=2)
        e_powder_salt = Entry(innerframe3, width=50, relief=SUNKEN, bd=4)
        e_powder_salt.grid(row=1, column=2)
        e_redchilli_powder = Entry(innerframe3, width=50, relief=SUNKEN, bd=4)
        e_redchilli_powder.grid(row=2, column=2)
        e_dhania_powder = Entry(innerframe3, width=50, relief=SUNKEN, bd=4)
        e_dhania_powder.grid(row=3, column=2)
        e_garammasala_powder = Entry(innerframe3, width=50, relief=SUNKEN, bd=4)
        e_garammasala_powder.grid(row=4, column=2)
        e_chatmasala_powder = Entry(innerframe3, width=50, relief=SUNKEN, bd=4)
        e_chatmasala_powder.grid(row=5, column=2)
        e_pepper_powder = Entry(innerframe3, width=50, relief=SUNKEN, bd=4)
        e_pepper_powder.grid(row=6, column=2)
        e_sambar_powder = Entry(innerframe3, width=50, relief=SUNKEN, bd=4)
        e_sambar_powder.grid(row=7, column=2)
        e_biryani_powder = Entry(innerframe3, width=50, relief=SUNKEN, bd=4)
        e_biryani_powder.grid(row=8, column=2)
        e_coffee_powder = Entry(innerframe3, width=50, relief=SUNKEN, bd=4)
        e_coffee_powder.grid(row=9, column=2)
        e_tea_powder = Entry(innerframe3, width=50, relief=SUNKEN, bd=4)
        e_tea_powder.grid(row=10, column=2)

        spices1 = Checkbutton(innerframe3, text="", fg="#51361a", bg="#f6ead4", variable=sp1)
        spices1.grid(row=0, column=3)
        spices2 = Checkbutton(innerframe3, text="", fg="#51361a", bg="#f6ead4", variable=sp2)
        spices2.grid(row=1, column=3)
        spices3 = Checkbutton(innerframe3, text="", fg="#51361a", bg="#f6ead4", variable=sp3)
        spices3.grid(row=2, column=3)
        spices4 = Checkbutton(innerframe3, text="", fg="#51361a", bg="#f6ead4", variable=sp4)
        spices4.grid(row=3, column=3)
        spices5 = Checkbutton(innerframe3, text="", fg="#51361a", bg="#f6ead4", variable=sp5)
        spices5.grid(row=4, column=3)
        spices6 = Checkbutton(innerframe3, text="", fg="#51361a", bg="#f6ead4", variable=sp6)
        spices6.grid(row=5, column=3)
        spices7 = Checkbutton(innerframe3, text="", fg="#51361a", bg="#f6ead4", variable=sp7)
        spices7.grid(row=6, column=3)
        spices8 = Checkbutton(innerframe3, text="", fg="#51361a", bg="#f6ead4", variable=sp8)
        spices8.grid(row=7, column=3)
        spices9 = Checkbutton(innerframe3, text="", fg="#51361a", bg="#f6ead4", variable=sp9)
        spices9.grid(row=8, column=3)
        spices10 = Checkbutton(innerframe3, text="", fg="#51361a", bg="#f6ead4", variable=sp10)
        spices10.grid(row=9, column=3)
        spices11 = Checkbutton(innerframe3, text="", fg="#51361a", bg="#f6ead4", variable=sp11)
        spices11.grid(row=10, column=3)

        total = Button(innerframe3, text="TOTAL", command=cal3, width=20, font=("times new roaman", 15, "bold"),
                       fg="#51361a", bg="#b4a284", relief=GROOVE, bd=9)
        total.grid(row=11, column=0, columnspan=3)

    def cal4():
        valid_number = 0
        global q_cooking_oil
        global q_seasame_oil
        global q_coconut_oil
        global q_ghee
        global q_olive_oil
        q_cooking_oil = 0
        q_seasame_oil = 0
        q_coconut_oil = 0
        q_ghee = 0
        q_olive_oil = 0

        if e_cooking_oil.get() == "" or e_cooking_oil.get() == 0:
            q_cooking_oil = 0
        else:
            try:
                q_cooking_oil = float(e_cooking_oil.get())
            except:
                valid_number = 1

        if e_seasame_oil.get() == "" or e_seasame_oil.get() == 0:
            q_seasame_oil = 0
        else:
            try:
                q_seasame_oil = float(e_seasame_oil.get())
            except:
                valid_number = 1

        if e_coconut_oil.get() == "" or e_coconut_oil.get() == 0:
            q_coconut_oil = 0
        else:
            try:
                q_coconut_oil = float(e_coconut_oil.get())
            except:
                valid_number = 1

        if e_ghee.get() == "" or e_ghee.get() == 0:
            q_ghee = 0
        else:
            try:
                q_ghee = float(e_ghee.get())
            except:
                valid_number = 1

        if e_olive_oil.get() == "" or e_olive_oil.get() == 0:
            q_olive_oil = 0
        else:
            try:
                q_olive_oil = float(e_olive_oil.get())
            except:
                valid_number = 1

        if valid_number == 1:
            messagebox.showerror("NUMBER", "PLEASE ENTER A VALID NUMBER", parent=innerframe4)
        innerframe4.destroy()

    def oil():
        global e_cooking_oil
        global e_seasame_oil
        global e_coconut_oil
        global e_ghee
        global e_olive_oil
        global innerframe4

        global change_oils
        change_oils = 1

        global oils1
        global oils2
        global oils3
        global oils4
        global oils5

        global oilll1
        global oilll2
        global oilll3
        global oilll4
        global oilll5

        oilll1 = IntVar()
        oilll2 = IntVar()
        oilll3 = IntVar()
        oilll4 = IntVar()
        oilll5 = IntVar()

        oilll1.set(0)
        oilll2.set(0)
        oilll3.set(0)
        oilll4.set(0)
        oilll5.set(0)

        innerframe4 = Toplevel(bg="#f6ead4", relief=GROOVE, bd=9)
        # innerframe1.geometry("500x200+200+100")
        innerframe4.title("OILS")
        cooking_oil = Label(innerframe4, text="COOKING OIL", font=("Goudy old style", 15, "bold"), fg="#51361a",
                            bg="#f6ead4")
        cooking_oil.grid(row=0, column=0)
        seasame_oil = Label(innerframe4, text="SEASAME OIL", font=("Goudy old style", 15, "bold"), fg="#51361a",
                            bg="#f6ead4")
        seasame_oil.grid(row=1, column=0)
        coconut_oil = Label(innerframe4, text="COCONUT OIL", font=("Goudy old style", 15, "bold"), fg="#51361a",
                            bg="#f6ead4")
        coconut_oil.grid(row=2, column=0)
        ghee = Label(innerframe4, text="GHEE", font=("Goudy old style", 15, "bold"), fg="#51361a",
                     bg="#f6ead4")
        ghee.grid(row=3, column=0)
        olive_oil = Label(innerframe4, text="OLIVE OIL ", font=("Goudy old style", 15, "bold"), fg="#51361a",
                          bg="#f6ead4")
        olive_oil.grid(row=4, column=0)

        e_cooking_oil = Entry(innerframe4, width=50, relief=SUNKEN, bd=4)
        e_cooking_oil.grid(row=0, column=2)
        e_seasame_oil = Entry(innerframe4, width=50, relief=SUNKEN, bd=4)
        e_seasame_oil.grid(row=1, column=2)
        e_coconut_oil = Entry(innerframe4, width=50, relief=SUNKEN, bd=4)
        e_coconut_oil.grid(row=2, column=2)
        e_ghee = Entry(innerframe4, width=50, relief=SUNKEN, bd=4)
        e_ghee.grid(row=3, column=2)
        e_olive_oil = Entry(innerframe4, width=50, relief=SUNKEN, bd=4)
        e_olive_oil.grid(row=4, column=2)

        oils1 = Checkbutton(innerframe4, text="", fg="#51361a", bg="#f6ead4", variable=oilll1)
        oils1.grid(row=0, column=3)
        oils2 = Checkbutton(innerframe4, text="", fg="#51361a", bg="#f6ead4", variable=oilll2)
        oils2.grid(row=1, column=3)
        oils3 = Checkbutton(innerframe4, text="", fg="#51361a", bg="#f6ead4", variable=oilll3)
        oils3.grid(row=2, column=3)
        oils4 = Checkbutton(innerframe4, text="", fg="#51361a", bg="#f6ead4", variable=oilll4)
        oils4.grid(row=3, column=3)
        oils5 = Checkbutton(innerframe4, text="", fg="#51361a", bg="#f6ead4", variable=oilll5)
        oils5.grid(row=4, column=3)

        total2 = Button(innerframe4, text="TOTAL", command=cal4, width=20, font=("times new roaman", 15, "bold"),
                        fg="#51361a", bg="#b4a284", relief=GROOVE, bd=9)
        total2.grid(row=5, column=0, columnspan=3, pady=15)

    def cal5():
        valid_number = 0
        global q_mustard_seed
        global q_pepper
        global q_jeera
        global q_khus_khus
        global q_dhania
        global q_black_seasame_seeds
        global q_white_seasame_seeds
        global q_cashew_nuts
        global q_raisins
        global q_badam
        global q_peanuts
        global q_dates
        q_mustard_seed = 0
        q_pepper = 0
        q_jeera = 0
        q_khus_khus = 0
        q_dhania = 0
        q_black_seasame_seeds = 0
        q_white_seasame_seeds = 0
        q_cashew_nuts = 0
        q_raisins = 0
        q_badam = 0
        q_peanuts = 0
        q_dates = 0

        if e_mustard_seed.get() == "" or e_mustard_seed.get() == 0:
            q_mustard_seed = 0
        else:
            try:
                q_mustard_seed = float(e_mustard_seed.get())
            except:
                valid_number = 1

        if e_pepper.get() == "" or e_pepper.get() == 0:
            q_pepper = 0
        else:
            try:
                q_pepper = float(e_pepper.get())
            except:
                valid_number = 1

        if e_jeera.get() == "" or e_jeera.get() == 0:
            q_jeera = 0
        else:
            try:
                q_jeera = float(e_jeera.get())
            except:
                valid_number = 1

        if e_khus_khus.get() == "" or e_khus_khus.get() == 0:
            q_khus_khus = 0
        else:
            try:
                q_khus_khus = float(e_khus_khus.get())
            except:
                valid_number = 1

        if e_dhania.get() == "" or e_dhania.get() == 0:
            q_dhania = 0
        else:
            try:
                q_dhania = float(e_dhania.get())
            except:
                valid_number = 1

        if e_black_seasame_seeds.get() == "" or e_black_seasame_seeds.get() == 0:
            q_black_seasame_seeds = 0
        else:
            try:
                q_black_seasame_seeds = float(e_black_seasame_seeds.get())
            except:
                valid_number = 1

        if e_white_seasame_seeds.get() == "" or e_white_seasame_seeds.get() == 0:
            q_white_seasame_seeds = 0
        else:
            try:
                q_white_seasame_seeds = float(e_white_seasame_seeds.get())
            except:
                valid_number = 1

        if e_cashew_nuts.get() == "" or e_cashew_nuts.get() == 0:
            q_cashew_nuts = 0
        else:
            try:
                q_cashew_nuts = float(e_cashew_nuts.get())
            except:
                valid_number = 1

        if e_raisins.get() == "" or e_raisins.get() == 0:
            q_raisins = 0
        else:
            try:
                q_raisins = float(e_raisins.get())
            except:
                valid_number = 1

        if e_badam.get() == "" or e_badam.get() == 0:
            q_badam = 0
        else:
            try:
                q_badam = float(e_badam.get())
            except:
                valid_number = 1

        if e_peanuts.get() == "" or e_peanuts.get() == 0:
            q_peanuts = 0
        else:
            try:
                q_peanuts = float(e_peanuts.get())
            except:
                valid_number = 1

        if e_dates.get() == "" or e_dates.get() == 0:
            q_dates = 0
        else:
            try:
                q_dates = float(e_dates.get())
            except:
                valid_number = 1

        if valid_number == 1:
            messagebox.showerror("NUMBER", "PLEASE ENTER A VALID NUMBER", parent=innerframe5)
        innerframe5.destroy()

    def spice_nut():
        global innerframe5
        global e_mustard_seed
        global e_pepper
        global e_jeera
        global e_khus_khus
        global e_dhania
        global e_black_seasame_seeds
        global e_white_seasame_seeds
        global e_cashew_nuts
        global e_raisins
        global e_badam
        global e_peanuts
        global e_dates

        global spice_nut1
        global spice_nut2
        global spice_nut3
        global spice_nut4
        global spice_nut5
        global spice_nut6
        global spice_nut7
        global spice_nut8
        global spice_nut9
        global spice_nut10
        global spice_nut11
        global spice_nut12

        global change_snuts
        change_snuts = 1

        global sn1
        global sn2
        global sn3
        global sn4
        global sn5
        global sn6
        global sn7
        global sn8
        global sn9
        global sn10
        global sn11
        global sn12

        sn1 = IntVar()
        sn2 = IntVar()
        sn3 = IntVar()
        sn4 = IntVar()
        sn5 = IntVar()
        sn6 = IntVar()
        sn7 = IntVar()
        sn8 = IntVar()
        sn9 = IntVar()
        sn10 = IntVar()
        sn11 = IntVar()
        sn12 = IntVar()

        sn1.set(0)
        sn2.set(0)
        sn3.set(0)
        sn4.set(0)
        sn5.set(0)
        sn6.set(0)
        sn7.set(0)
        sn8.set(0)
        sn9.set(0)
        sn10.set(0)
        sn11.set(0)
        sn12.set(0)

        innerframe5 = Toplevel(bg="#f6ead4", relief=GROOVE, bd=9)
        # innerframe5.geometry("500x200+200+100")
        innerframe5.title("SPICES AND NUTS")
        mustard_seed = Label(innerframe5, text="MUSTARD SEEDS ", font=("Goudy old style", 15, "bold"), fg="#51361a",
                             bg="#f6ead4")
        mustard_seed.grid(row=0, column=0)
        pepper = Label(innerframe5, text="PEPPER", font=("Goudy old style", 15, "bold"), fg="#51361a",
                       bg="#f6ead4")
        pepper.grid(row=1, column=0)
        jeera = Label(innerframe5, text="JEERA ", font=("Goudy old style", 15, "bold"), fg="#51361a",
                      bg="#f6ead4")
        jeera.grid(row=2, column=0)
        khus_khus = Label(innerframe5, text="KHUS KHUS", font=("Goudy old style", 15, "bold"), fg="#51361a",
                          bg="#f6ead4")
        khus_khus.grid(row=3, column=0)
        dhania = Label(innerframe5, text="DHANIA ", font=("Goudy old style", 15, "bold"), fg="#51361a",
                       bg="#f6ead4")
        dhania.grid(row=4, column=0)
        black_seasame_seeds = Label(innerframe5, text="BLACK SEASAME SEEDS", font=("Goudy old style", 15, "bold"),
                                    fg="#51361a",
                                    bg="#f6ead4")
        black_seasame_seeds.grid(row=5, column=0)
        white_seasame_seeds = Label(innerframe5, text="WHITE SEASAME SEEDS", font=("Goudy old style", 15, "bold"),
                                    fg="#51361a",
                                    bg="#f6ead4")
        white_seasame_seeds.grid(row=6, column=0)
        cashew_nuts = Label(innerframe5, text="CASHEW NUTS", font=("Goudy old style", 15, "bold"), fg="#51361a",
                            bg="#f6ead4")
        cashew_nuts.grid(row=7, column=0)
        raisins = Label(innerframe5, text="RAISINS", font=("Goudy old style", 15, "bold"), fg="#51361a",
                        bg="#f6ead4")
        raisins.grid(row=8, column=0)
        badam = Label(innerframe5, text="BADAM", font=("Goudy old style", 15, "bold"), fg="#51361a",
                      bg="#f6ead4")
        badam.grid(row=9, column=0)
        peanuts = Label(innerframe5, text="PEANUTS", font=("Goudy old style", 15, "bold"), fg="#51361a",
                        bg="#f6ead4")
        peanuts.grid(row=10, column=0)
        dates = Label(innerframe5, text="DATES", font=("Goudy old style", 15, "bold"), fg="#51361a",
                      bg="#f6ead4")
        dates.grid(row=11, column=0)

        e_mustard_seed = Entry(innerframe5, width=50, relief=SUNKEN, bd=4)
        e_mustard_seed.grid(row=0, column=2)
        e_pepper = Entry(innerframe5, width=50, relief=SUNKEN, bd=4)
        e_pepper.grid(row=1, column=2)
        e_jeera = Entry(innerframe5, width=50, relief=SUNKEN, bd=4)
        e_jeera.grid(row=2, column=2)
        e_khus_khus = Entry(innerframe5, width=50, relief=SUNKEN, bd=4)
        e_khus_khus.grid(row=3, column=2)
        e_dhania = Entry(innerframe5, width=50, relief=SUNKEN, bd=4)
        e_dhania.grid(row=4, column=2)
        e_black_seasame_seeds = Entry(innerframe5, width=50, relief=SUNKEN, bd=4)
        e_black_seasame_seeds.grid(row=5, column=2)
        e_white_seasame_seeds = Entry(innerframe5, width=50, relief=SUNKEN, bd=4)
        e_white_seasame_seeds.grid(row=6, column=2)
        e_cashew_nuts = Entry(innerframe5, width=50, relief=SUNKEN, bd=4)
        e_cashew_nuts.grid(row=7, column=2)
        e_raisins = Entry(innerframe5, width=50, relief=SUNKEN, bd=4)
        e_raisins.grid(row=8, column=2)
        e_badam = Entry(innerframe5, width=50, relief=SUNKEN, bd=4)
        e_badam.grid(row=9, column=2)
        e_peanuts = Entry(innerframe5, width=50, relief=SUNKEN, bd=4)
        e_peanuts.grid(row=10, column=2)
        e_dates = Entry(innerframe5, width=50, relief=SUNKEN, bd=4)
        e_dates.grid(row=11, column=2)

        spice_nut1 = Checkbutton(innerframe5, text="", fg="#51361a", bg="#f6ead4", variable=sn1)
        spice_nut1.grid(row=0, column=3)
        spice_nut2 = Checkbutton(innerframe5, text="", fg="#51361a", bg="#f6ead4", variable=sn2)
        spice_nut2.grid(row=1, column=3)
        spice_nut3 = Checkbutton(innerframe5, text="", fg="#51361a", bg="#f6ead4", variable=sn3)
        spice_nut3.grid(row=2, column=3)
        spice_nut4 = Checkbutton(innerframe5, text="", fg="#51361a", bg="#f6ead4", variable=sn4)
        spice_nut4.grid(row=3, column=3)
        spice_nut5 = Checkbutton(innerframe5, text="", fg="#51361a", bg="#f6ead4", variable=sn5)
        spice_nut5.grid(row=4, column=3)
        spice_nut6 = Checkbutton(innerframe5, text="", fg="#51361a", bg="#f6ead4", variable=sn6)
        spice_nut6.grid(row=5, column=3)
        spice_nut7 = Checkbutton(innerframe5, text="", fg="#51361a", bg="#f6ead4", variable=sn7)
        spice_nut7.grid(row=6, column=3)
        spice_nut8 = Checkbutton(innerframe5, text="", fg="#51361a", bg="#f6ead4", variable=sn8)
        spice_nut8.grid(row=7, column=3)
        spice_nut9 = Checkbutton(innerframe5, text="", fg="#51361a", bg="#f6ead4", variable=sn9)
        spice_nut9.grid(row=8, column=3)
        spice_nut10 = Checkbutton(innerframe5, text="", fg="#51361a", bg="#f6ead4", variable=sn10)
        spice_nut10.grid(row=9, column=3)
        spice_nut11 = Checkbutton(innerframe5, text="", fg="#51361a", bg="#f6ead4", variable=sn11)
        spice_nut11.grid(row=10, column=3)
        spice_nut12 = Checkbutton(innerframe5, text="", fg="#51361a", bg="#f6ead4", variable=sn12)
        spice_nut12.grid(row=11, column=3)

        total = Button(innerframe5, text="TOTAL", command=cal5, width=20, font=("times new roaman", 15, "bold"),
                       fg="#51361a", bg="#b4a284", relief=GROOVE, bd=9)
        total.grid(row=12, column=0, columnspan=3, pady=15)

    def cal6():
        valid_number = 0
        global q_cheese_block
        global q_butter
        global q_yoghurt
        global q_fresh_cream
        global q_paneer
        q_cheese_block = 0
        q_butter = 0
        q_yoghurt = 0
        q_fresh_cream = 0
        q_paneer = 0

        if e_chesse_block.get() == "" or e_chesse_block.get() == 0:
            q_cheese_block = 0
        else:
            try:
                q_cheese_block = float(e_chesse_block.get())
            except:
                valid_number = 1

        if e_butter.get() == "" or e_butter.get() == 0:
            q_butter = 0
        else:
            try:
                q_butter = float(e_butter.get())
            except:
                valid_number = 1

        if e_yoghurt.get() == "" or e_yoghurt.get() == 0:
            q_yoghurt = 0
        else:
            try:
                q_yoghurt = float(e_yoghurt.get())
            except:
                valid_number = 1

        if e_fresh_cream.get() == "" or e_fresh_cream.get() == 0:
            q_fresh_cream = 0
        else:
            try:
                q_fresh_cream = float(e_fresh_cream.get())
            except:
                valid_number = 1

        if e_paneer.get() == "" or e_paneer.get() == 0:
            q_paneer = 0
        else:
            try:
                q_paneer = float(e_paneer.get())
            except:
                valid_number = 1

        if valid_number == 1:
            messagebox.showerror("NUMBER", "PLEASE ENTER A VALID NUMBER", parent=innerframe6)
        innerframe6.destroy()

    def dairy():
        global e_chesse_block
        global e_butter
        global e_yoghurt
        global e_fresh_cream
        global e_paneer
        global innerframe6

        global dairy1
        global dairy2
        global dairy3
        global dairy4
        global dairy5

        global change_dairy
        change_dairy = 1

        global d1
        global d2
        global d3
        global d4
        global d5

        d1 = IntVar()
        d2 = IntVar()
        d3 = IntVar()
        d4 = IntVar()
        d5 = IntVar()

        d1.set(0)
        d2.set(0)
        d3.set(0)
        d4.set(0)
        d5.set(0)

        innerframe6 = Toplevel(bg="#f6ead4", relief=GROOVE, bd=9)
        innerframe6.title("DAIRY PRODUCTS")
        cheese_block = Label(innerframe6, text="CHEESE BLOCK", font=("Goudy old style", 15, "bold"), fg="#51361a",
                             bg="#f6ead4")
        cheese_block.grid(row=0, column=0)
        butter = Label(innerframe6, text="BUTTER", font=("Goudy old style", 15, "bold"), fg="#51361a",
                       bg="#f6ead4")
        butter.grid(row=1, column=0)
        yoghurt = Label(innerframe6, text="YOGHURT", font=("Goudy old style", 15, "bold"), fg="#51361a",
                        bg="#f6ead4")
        yoghurt.grid(row=2, column=0)
        fresh_cream = Label(innerframe6, text="FRESH CREAM", font=("Goudy old style", 15, "bold"), fg="#51361a",
                            bg="#f6ead4")
        fresh_cream.grid(row=3, column=0)
        paneer = Label(innerframe6, text="PANEER", font=("Goudy old style", 15, "bold"), fg="#51361a",
                       bg="#f6ead4")
        paneer.grid(row=4, column=0)

        e_chesse_block = Entry(innerframe6, width=50, relief=SUNKEN, bd=4)
        e_chesse_block.grid(row=0, column=2)
        e_butter = Entry(innerframe6, width=50, relief=SUNKEN, bd=4)
        e_butter.grid(row=1, column=2)
        e_yoghurt = Entry(innerframe6, width=50, relief=SUNKEN, bd=4)
        e_yoghurt.grid(row=2, column=2)
        e_fresh_cream = Entry(innerframe6, width=50, relief=SUNKEN, bd=4)
        e_fresh_cream.grid(row=3, column=2)
        e_paneer = Entry(innerframe6, width=50, relief=SUNKEN, bd=4)
        e_paneer.grid(row=4, column=2)

        dairy1 = Checkbutton(innerframe6, text="", fg="#51361a", bg="#f6ead4", variable=d1)
        dairy1.grid(row=0, column=3)
        dairy2 = Checkbutton(innerframe6, text="", fg="#51361a", bg="#f6ead4", variable=d2)
        dairy2.grid(row=1, column=3)
        dairy3 = Checkbutton(innerframe6, text="", fg="#51361a", bg="#f6ead4", variable=d3)
        dairy3.grid(row=2, column=3)
        dairy4 = Checkbutton(innerframe6, text="", fg="#51361a", bg="#f6ead4", variable=d4)
        dairy4.grid(row=3, column=3)
        dairy5 = Checkbutton(innerframe6, text="", fg="#51361a", bg="#f6ead4", variable=d5)
        dairy5.grid(row=4, column=3)

        total2 = Button(innerframe6, text="TOTAL", command=cal6, width=20, font=("times new roaman", 15, "bold"),
                        fg="#51361a", bg="#b4a284", relief=GROOVE, bd=9)
        total2.grid(row=5, column=0, columnspan=3, pady=15)

    def cal7():
        valid_number = 0
        global q_tooth_paste
        global q_tooth_brush
        global q_bathing_soap
        global q_shampoo
        global q_face_powder
        global q_hand_sanitizer
        global q_deodarant
        global q_shaving_cream
        global q_hair_gel
        global q_razer_blade
        q_tooth_paste = 0
        q_tooth_brush = 0
        q_bathing_soap = 0
        q_shampoo = 0
        q_face_powder = 0
        q_hand_sanitizer = 0
        q_deodarant = 0
        q_shaving_cream = 0
        q_hair_gel = 0
        q_razer_blade = 0

        if e_tooth_paste.get() == "" or e_tooth_paste.get() == 0:
            q_tooth_paste = 0
        else:
            try:
                q_tooth_paste = float(e_tooth_paste.get())
            except:
                valid_number = 1

        if e_tooth_brush.get() == "" or e_tooth_brush.get() == 0:
            q_tooth_brush = 0
        else:
            try:
                q_tooth_brush = float(e_tooth_brush.get())
            except:
                valid_number = 1

        if e_bathing_soap.get() == "" or e_bathing_soap.get() == 0:
            q_bathing_soap = 0
        else:
            try:
                q_bathing_soap = float(e_bathing_soap.get())
            except:
                valid_number = 1

        if e_shampoo.get() == "" or e_shampoo.get() == 0:
            q_shampoo = 0
        else:
            try:
                q_shampoo = float(e_shampoo.get())
            except:
                valid_number = 1

        if e_face_powder.get() == "" or e_face_powder.get() == 0:
            q_face_powder = 0
        else:
            try:
                q_face_powder = float(e_face_powder.get())
            except:
                valid_number = 1

        if e_hand_sanitizer.get() == "" or e_hand_sanitizer.get() == 0:
            q_hand_sanitizer = 0
        else:
            try:
                q_hand_sanitizer = float(e_hand_sanitizer.get())
            except:
                valid_number = 1

        if e_deodarant.get() == "" or e_deodarant.get() == 0:
            q_deodarant = 0
        else:
            try:
                q_deodarant = float(e_deodarant.get())
            except:
                valid_number = 1

        if e_shaving_cream.get() == "" or e_shaving_cream.get() == 0:
            q_shaving_cream = 0
        else:
            try:
                q_shaving_cream = float(e_shaving_cream.get())
            except:
                valid_number = 1

        if e_hair_gel.get() == "" or e_hair_gel.get() == 0:
            q_hair_gel = 0
        else:
            try:
                q_hair_gel = float(e_hair_gel.get())
            except:
                valid_number = 1

        if e_razer_blade.get() == "" or e_razer_blade.get() == 0:
            q_razer_blade = 0
        else:
            try:
                q_razer_blade = float(e_razer_blade.get())
            except:
                valid_number = 1

        if valid_number == 1:
            messagebox.showerror("NUMBER", "PLEASE ENTER A VALID NUMBER", parent=innerframe7)
        innerframe7.destroy()

    def toiletrie():
        global innerframe7
        global e_tooth_paste
        global e_tooth_brush
        global e_bathing_soap
        global e_shampoo
        global e_face_powder
        global e_hand_sanitizer
        global e_deodarant
        global e_shaving_cream
        global e_hair_gel
        global e_razer_blade
        global e_rice_flour
        global e_besan_flour
        global e_rava
        global e_rice_rava
        global e_corn_flour
        global e_vermicelli
        global e_tamarind
        global e_red_chilli

        global toiletrie1
        global toiletrie2
        global toiletrie3
        global toiletrie4
        global toiletrie5
        global toiletrie6
        global toiletrie7
        global toiletrie8
        global toiletrie9
        global toiletrie10

        global change_toi
        change_toi = 1

        global t1
        global t2
        global t3
        global t4
        global t5
        global t6
        global t7
        global t8
        global t9
        global t10

        t1 = IntVar()
        t2 = IntVar()
        t3 = IntVar()
        t4 = IntVar()
        t5 = IntVar()
        t6 = IntVar()
        t7 = IntVar()
        t8 = IntVar()
        t9 = IntVar()
        t10 = IntVar()

        t1.set(0)
        t2.set(0)
        t3.set(0)
        t4.set(0)
        t5.set(0)
        t6.set(0)
        t7.set(0)
        t8.set(0)
        t9.set(0)
        t10.set(0)

        innerframe7 = Toplevel(bg="#f6ead4", relief=GROOVE, bd=9)
        innerframe7.title("TOILETRIES")
        tooth_paste = Label(innerframe7, text="TOOTH PASTE ", font=("Goudy old style", 15, "bold"), fg="#51361a",
                            bg="#f6ead4")
        tooth_paste.grid(row=0, column=0)
        tooth_brush = Label(innerframe7, text="TOOTH BRUSH", font=("Goudy old style", 15, "bold"), fg="#51361a",
                            bg="#f6ead4")
        tooth_brush.grid(row=1, column=0)
        bathing_soap = Label(innerframe7, text="BATHING SOAP", font=("Goudy old style", 15, "bold"), fg="#51361a",
                             bg="#f6ead4")
        bathing_soap.grid(row=2, column=0)
        shampoo = Label(innerframe7, text="SHAMPOO", font=("Goudy old style", 15, "bold"), fg="#51361a",
                        bg="#f6ead4")
        shampoo.grid(row=3, column=0)
        face_powder = Label(innerframe7, text="FACE POWDER", font=("Goudy old style", 15, "bold"), fg="#51361a",
                            bg="#f6ead4")
        face_powder.grid(row=4, column=0)
        hand_sanitizer = Label(innerframe7, text="HAND SANITIZER", font=("Goudy old style", 15, "bold"), fg="#51361a",
                               bg="#f6ead4")
        hand_sanitizer.grid(row=5, column=0)
        deodarant = Label(innerframe7, text="DEODARANT", font=("Goudy old style", 15, "bold"), fg="#51361a",
                          bg="#f6ead4")
        deodarant.grid(row=6, column=0)
        shaving_cream = Label(innerframe7, text="SHAVING CREAM", font=("Goudy old style", 15, "bold"), fg="#51361a",
                              bg="#f6ead4")
        shaving_cream.grid(row=7, column=0)
        hair_gel = Label(innerframe7, text="HAIR GEL", font=("Goudy old style", 15, "bold"), fg="#51361a",
                         bg="#f6ead4")
        hair_gel.grid(row=8, column=0)
        razer_blade = Label(innerframe7, text="RAZER BLADE", font=("Goudy old style", 15, "bold"), fg="#51361a",
                            bg="#f6ead4")
        razer_blade.grid(row=9, column=0)

        e_tooth_paste = Entry(innerframe7, width=50, relief=SUNKEN, bd=4)
        e_tooth_paste.grid(row=0, column=2)
        e_tooth_brush = Entry(innerframe7, width=50, relief=SUNKEN, bd=4)
        e_tooth_brush.grid(row=1, column=2)
        e_bathing_soap = Entry(innerframe7, width=50, relief=SUNKEN, bd=4)
        e_bathing_soap.grid(row=2, column=2)
        e_shampoo = Entry(innerframe7, width=50, relief=SUNKEN, bd=4)
        e_shampoo.grid(row=3, column=2)
        e_face_powder = Entry(innerframe7, width=50, relief=SUNKEN, bd=4)
        e_face_powder.grid(row=4, column=2)
        e_hand_sanitizer = Entry(innerframe7, width=50, relief=SUNKEN, bd=4)
        e_hand_sanitizer.grid(row=5, column=2)
        e_deodarant = Entry(innerframe7, width=50, relief=SUNKEN, bd=4)
        e_deodarant.grid(row=6, column=2)
        e_shaving_cream = Entry(innerframe7, width=50, relief=SUNKEN, bd=4)
        e_shaving_cream.grid(row=7, column=2)
        e_hair_gel = Entry(innerframe7, width=50, relief=SUNKEN, bd=4)
        e_hair_gel.grid(row=8, column=2)
        e_razer_blade = Entry(innerframe7, width=50, relief=SUNKEN, bd=4)
        e_razer_blade.grid(row=9, column=2)

        toiletrie1 = Checkbutton(innerframe7, text="", fg="#51361a", bg="#f6ead4", variable=t1)
        toiletrie1.grid(row=0, column=3)
        toiletrie2 = Checkbutton(innerframe7, text="", fg="#51361a", bg="#f6ead4", variable=t2)
        toiletrie2.grid(row=1, column=3)
        toiletrie3 = Checkbutton(innerframe7, text="", fg="#51361a", bg="#f6ead4", variable=t3)
        toiletrie3.grid(row=2, column=3)
        toiletrie4 = Checkbutton(innerframe7, text="", fg="#51361a", bg="#f6ead4", variable=t4)
        toiletrie4.grid(row=3, column=3)
        toiletrie5 = Checkbutton(innerframe7, text="", fg="#51361a", bg="#f6ead4", variable=t5)
        toiletrie5.grid(row=4, column=3)
        toiletrie6 = Checkbutton(innerframe7, text="", fg="#51361a", bg="#f6ead4", variable=t6)
        toiletrie6.grid(row=5, column=3)
        toiletrie7 = Checkbutton(innerframe7, text="", fg="#51361a", bg="#f6ead4", variable=t7)
        toiletrie7.grid(row=6, column=3)
        toiletrie8 = Checkbutton(innerframe7, text="", fg="#51361a", bg="#f6ead4", variable=t8)
        toiletrie8.grid(row=7, column=3)
        toiletrie9 = Checkbutton(innerframe7, text="", fg="#51361a", bg="#f6ead4", variable=t9)
        toiletrie9.grid(row=8, column=3)
        toiletrie10 = Checkbutton(innerframe7, text="", fg="#51361a", bg="#f6ead4", variable=t10)
        toiletrie10.grid(row=9, column=3)

        total = Button(innerframe7, text="TOTAL", command=cal7, width=20, font=("times new roaman", 15, "bold"),
                       fg="#51361a", bg="#b4a284", relief=GROOVE, bd=9)
        total.grid(row=10, column=0, columnspan=3)

    def cal8():
        valid_number = 0
        global q_dish_washing_soap
        global q_dish_washing_liquid
        global q_washing_powder
        global q_washing_soaps
        global q_bleaching_powder
        global q_sanitary_pad
        global q_toilet_paper
        global q_garbage_bag
        global q_dettol
        global q_mosquito_liquid
        q_dish_washing_soap = 0
        q_dish_washing_liquid = 0
        q_washing_powder = 0
        q_washing_soaps = 0
        q_bleaching_powder = 0
        q_sanitary_pad = 0
        q_toilet_paper = 0
        q_garbage_bag = 0
        q_dettol = 0
        q_mosquito_liquid = 0

        if e_dish_washing_soap.get() == "" or e_dish_washing_soap.get() == 0:
            q_dish_washing_soap = 0
        else:
            try:
                q_dish_washing_soap = float(e_dish_washing_soap.get())
            except:
                valid_number = 1

        if e_dish_washing_liquid.get() == "" or e_dish_washing_liquid.get() == 0:
            q_dish_washing_liquid = 0
        else:
            try:
                q_dish_washing_liquid = float(e_dish_washing_liquid.get())
            except:
                valid_number = 1

        if e_washing_powder.get() == "" or e_washing_powder.get() == 0:
            q_washing_powder = 0
        else:
            try:
                q_washing_powder = float(e_washing_powder.get())
            except:
                valid_number = 1

        if e_washing_soaps.get() == "" or e_washing_soaps.get() == 0:
            q_washing_soaps = 0
        else:
            try:
                q_washing_soaps = float(e_washing_soaps.get())
            except:
                valid_number = 1

        if e_bleaching_powder.get() == "" or e_bleaching_powder.get() == 0:
            q_bleaching_powder = 0
        else:
            try:
                q_bleaching_powder = float(e_bleaching_powder.get())
            except:
                valid_number = 1

        if e_sanitary_pad.get() == "" or e_sanitary_pad.get() == 0:
            q_sanitary_pad = 0
        else:
            try:
                q_sanitary_pad = float(e_sanitary_pad.get())
            except:
                valid_number = 1

        if e_toilet_paper.get() == "" or e_toilet_paper.get() == 0:
            q_toilet_paper = 0
        else:
            try:
                q_toilet_paper = float(e_toilet_paper.get())
            except:
                valid_number = 1

        if e_garbage_bag.get() == "" or e_garbage_bag.get() == 0:
            q_garbage_bag = 0
        else:
            try:
                q_garbage_bag = float(e_garbage_bag.get())
            except:
                valid_number = 1

        if e_dettol.get() == "" or e_dettol.get() == 0:
            q_dettol = 0
        else:
            try:
                q_dettol = float(e_dettol.get())
            except:
                valid_number = 1

        if e_mosquito_liquid.get() == "" or e_mosquito_liquid.get() == 0:
            q_mosquito_liquid = 0
        else:
            try:
                q_mosquito_liquid = float(e_mosquito_liquid.get())
            except:
                valid_number = 1

        if valid_number == 1:
            messagebox.showerror("NUMBER", "PLEASE ENTER A VALID NUMBER", parent=innerframe8)
        innerframe8.destroy()

    def clean():
        global innerframe8
        global e_dish_washing_soap
        global e_dish_washing_liquid
        global e_washing_powder
        global e_washing_soaps
        global e_bleaching_powder
        global e_sanitary_pad
        global e_toilet_paper
        global e_garbage_bag
        global e_dettol
        global e_mosquito_liquid

        global cl1
        global cl2
        global cl3
        global cl4
        global cl5
        global cl6
        global cl7
        global cl8
        global cl9
        global cl10

        global c1
        global c2
        global c3
        global c4
        global c5
        global c6
        global c7
        global c8
        global c9
        global c10

        c1 = IntVar()
        c2 = IntVar()
        c3 = IntVar()
        c4 = IntVar()
        c5 = IntVar()
        c6 = IntVar()
        c7 = IntVar()
        c8 = IntVar()
        c9 = IntVar()
        c10 = IntVar()

        c1.set(0)
        c2.set(0)
        c3.set(0)
        c4.set(0)
        c5.set(0)
        c6.set(0)
        c7.set(0)
        c8.set(0)
        c9.set(0)
        c10.set(0)

        innerframe8 = Toplevel(bg="#f6ead4", relief=GROOVE, bd=9)
        innerframe8.title("CLEANING PRODUCTS")
        dish_washing_soap = Label(innerframe8, text="DISH WASHING SOAP", font=("Goudy old style", 15, "bold"),
                                  fg="#51361a",
                                  bg="#f6ead4")
        dish_washing_soap.grid(row=0, column=0)
        dish_washing_liquid = Label(innerframe8, text="DISH WASHING LIQUID", font=("Goudy old style", 15, "bold"),
                                    fg="#51361a",
                                    bg="#f6ead4")
        dish_washing_liquid.grid(row=1, column=0)
        washing_powder = Label(innerframe8, text="WASHING POWDER", font=("Goudy old style", 15, "bold"), fg="#51361a",
                               bg="#f6ead4")
        washing_powder.grid(row=2, column=0)
        washing_soaps = Label(innerframe8, text="WASHING SOAP", font=("Goudy old style", 15, "bold"), fg="#51361a",
                              bg="#f6ead4")
        washing_soaps.grid(row=3, column=0)
        bleaching_powder = Label(innerframe8, text="BLEACHING POWDER", font=("Goudy old style", 15, "bold"),
                                 fg="#51361a",
                                 bg="#f6ead4")
        bleaching_powder.grid(row=4, column=0)
        sanitary_pad = Label(innerframe8, text="SANITARY PAD", font=("Goudy old style", 15, "bold"), fg="#51361a",
                             bg="#f6ead4")
        sanitary_pad.grid(row=5, column=0)
        toilet_paper = Label(innerframe8, text="TOILET PAPER", font=("Goudy old style", 15, "bold"), fg="#51361a",
                             bg="#f6ead4")
        toilet_paper.grid(row=6, column=0)
        garbage_bag = Label(innerframe8, text="GARBAGE BAG", font=("Goudy old style", 15, "bold"), fg="#51361a",
                            bg="#f6ead4")
        garbage_bag.grid(row=7, column=0)
        dettol = Label(innerframe8, text="DETTOL", font=("Goudy old style", 15, "bold"), fg="#51361a",
                       bg="#f6ead4")
        dettol.grid(row=8, column=0)
        mosquito_liquid = Label(innerframe8, text="MOSQUITO LIQUID", font=("Goudy old style", 15, "bold"), fg="#51361a",
                                bg="#f6ead4")
        mosquito_liquid.grid(row=9, column=0)

        e_dish_washing_soap = Entry(innerframe8, width=50, relief=SUNKEN, bd=4)
        e_dish_washing_soap.grid(row=0, column=2)
        e_dish_washing_liquid = Entry(innerframe8, width=50, relief=SUNKEN, bd=4)
        e_dish_washing_liquid.grid(row=1, column=2)
        e_washing_powder = Entry(innerframe8, width=50, relief=SUNKEN, bd=4)
        e_washing_powder.grid(row=2, column=2)
        e_washing_soaps = Entry(innerframe8, width=50, relief=SUNKEN, bd=4)
        e_washing_soaps.grid(row=3, column=2)
        e_bleaching_powder = Entry(innerframe8, width=50, relief=SUNKEN, bd=4)
        e_bleaching_powder.grid(row=4, column=2)
        e_sanitary_pad = Entry(innerframe8, width=50, relief=SUNKEN, bd=4)
        e_sanitary_pad.grid(row=5, column=2)
        e_toilet_paper = Entry(innerframe8, width=50, relief=SUNKEN, bd=4)
        e_toilet_paper.grid(row=6, column=2)
        e_garbage_bag = Entry(innerframe8, width=50, relief=SUNKEN, bd=4)
        e_garbage_bag.grid(row=7, column=2)
        e_dettol = Entry(innerframe8, width=50, relief=SUNKEN, bd=4)
        e_dettol.grid(row=8, column=2)
        e_mosquito_liquid = Entry(innerframe8, width=50, relief=SUNKEN, bd=4)
        e_mosquito_liquid.grid(row=9, column=2)

        cl1 = Checkbutton(innerframe8, text="", fg="#51361a", bg="#f6ead4", variable=c1)
        cl1.grid(row=0, column=3)
        cl2 = Checkbutton(innerframe8, text="", fg="#51361a", bg="#f6ead4", variable=c2)
        cl2.grid(row=1, column=3)
        cl3 = Checkbutton(innerframe8, text="", fg="#51361a", bg="#f6ead4", variable=c3)
        cl3.grid(row=2, column=3)
        cl4 = Checkbutton(innerframe8, text="", fg="#51361a", bg="#f6ead4", variable=c4)
        cl4.grid(row=3, column=3)
        cl5 = Checkbutton(innerframe8, text="", fg="#51361a", bg="#f6ead4", variable=c5)
        cl5.grid(row=4, column=3)
        cl6 = Checkbutton(innerframe8, text="", fg="#51361a", bg="#f6ead4", variable=c6)
        cl6.grid(row=5, column=3)
        cl7 = Checkbutton(innerframe8, text="", fg="#51361a", bg="#f6ead4", variable=c7)
        cl7.grid(row=6, column=3)
        cl8 = Checkbutton(innerframe8, text="", fg="#51361a", bg="#f6ead4", variable=c8)
        cl8.grid(row=7, column=3)
        cl9 = Checkbutton(innerframe8, text="", fg="#51361a", bg="#f6ead4", variable=c9)
        cl9.grid(row=8, column=3)
        cl10 = Checkbutton(innerframe8, text="", fg="#51361a", bg="#f6ead4", variable=c10)
        cl10.grid(row=9, column=3)

        total = Button(innerframe8, text="TOTAL", command=cal8, width=20, font=("times new roaman", 15, "bold"),
                       fg="#51361a", bg="#b4a284", relief=GROOVE, bd=9)
        total.grid(row=10, column=0, columnspan=3)

    def cal9():
        valid_number = 0

        global q_bandages
        global q_light_bulbs
        global q_batteries
        global q_candles
        q_bandages = 0
        q_light_bulbs = 0
        q_batteries = 0
        q_candles = 0
        if e_bandages.get() == "" or e_bandages.get() == 0:
            q_bandages = 0
        else:
            try:
                q_bandages = float(e_bandages.get())
            except:
                valid_number = 1

        if e_light_bulbs.get() == "" or e_light_bulbs.get() == 0:
            q_light_bulbs = 0
        else:
            try:
                q_light_bulbs = float(e_light_bulbs.get())
            except:
                valid_number = 1

        if e_batteries.get() == "" or e_batteries.get() == 0:
            q_batteries = 0
        else:
            try:
                q_batteries = float(e_batteries.get())
            except:
                valid_number = 1

        if e_candles.get() == "" or e_candles.get() == 0:
            q_candles = 0
        else:
            try:
                q_candles = float(e_candles.get())
            except:
                valid_number = 1

        if valid_number == 1:
            messagebox.showerror("NUMBER", "PLEASE ENTER A VALID NUMBER", parent=innerframe9)
        innerframe9.destroy()

    def miss():
        global e_bandages
        global e_light_bulbs
        global e_batteries
        global e_candles
        global innerframe9

        global change_mis
        change_mis = 1

        global miss1
        global miss2
        global miss3
        global miss4

        global m1
        global m2
        global m3
        global m4

        m1 = IntVar()
        m2 = IntVar()
        m3 = IntVar()
        m4 = IntVar()

        m1.set(0)
        m2.set(0)
        m3.set(0)
        m4.set(0)

        innerframe9 = Toplevel(bg="#f6ead4", relief=GROOVE, bd=9)
        innerframe9.title("MISCELLENEOUS")
        bandages = Label(innerframe9, text="BANDAGES", font=("Goudy old style", 15, "bold"), fg="#51361a",
                         bg="#f6ead4")
        bandages.grid(row=0, column=0)
        light_bulbs = Label(innerframe9, text="LIGHT BULB", font=("Goudy old style", 15, "bold"), fg="#51361a",
                            bg="#f6ead4")
        light_bulbs.grid(row=1, column=0)
        batteries = Label(innerframe9, text="BATTERIES", font=("Goudy old style", 15, "bold"), fg="#51361a",
                          bg="#f6ead4")
        batteries.grid(row=2, column=0)
        candles = Label(innerframe9, text="CANDLES", font=("Goudy old style", 15, "bold"), fg="#51361a",
                        bg="#f6ead4")
        candles.grid(row=3, column=0)

        e_bandages = Entry(innerframe9, width=50, relief=SUNKEN, bd=4)
        e_bandages.grid(row=0, column=2)
        e_light_bulbs = Entry(innerframe9, width=50, relief=SUNKEN, bd=4)
        e_light_bulbs.grid(row=1, column=2)
        e_batteries = Entry(innerframe9, width=50, relief=SUNKEN, bd=4)
        e_batteries.grid(row=2, column=2)
        e_candles = Entry(innerframe9, width=50, relief=SUNKEN, bd=4)
        e_candles.grid(row=3, column=2)

        miss1 = Checkbutton(innerframe9, text="", fg="#51361a", bg="#f6ead4", variable=m1)
        miss1.grid(row=0, column=3)
        miss2 = Checkbutton(innerframe9, text="", fg="#51361a", bg="#f6ead4", variable=m2)
        miss2.grid(row=1, column=3)
        miss3 = Checkbutton(innerframe9, text="", fg="#51361a", bg="#f6ead4", variable=m3)
        miss3.grid(row=2, column=3)
        miss4 = Checkbutton(innerframe9, text="", fg="#51361a", bg="#f6ead4", variable=m4)
        miss4.grid(row=3, column=3)

        total2 = Button(innerframe9, text="TOTAL", command=cal9, width=20, font=("times new roaman", 15, "bold"),
                        fg="#51361a", bg="#b4a284", relief=GROOVE, bd=9)
        total2.grid(row=4, column=0, columnspan=3, pady=15)

    def cal10():
        valid_number = 0

        global q_papad
        global q_horlicks
        global q_complan
        global q_noodles
        global q_pasta
        global q_ketchup
        global q_jam
        global q_bread_delux
        global q_bread_britania
        q_papad = 0
        q_horlicks = 0
        q_complan = 0
        q_noodles = 0
        q_pasta = 0
        q_ketchup = 0
        q_jam = 0
        q_bread_delux = 0
        q_bread_britania = 0

        if e_papad.get() == "" or e_papad.get() == 0:
            q_papad = 0
        else:
            try:
                q_papad = float(e_papad.get())
            except:
                valid_number = 1

        if e_horlicks.get() == "" or e_horlicks.get() == 0:
            q_horlicks = 0
        else:
            try:
                q_horlicks = float(e_horlicks.get())
            except:
                valid_number = 1

        if e_complan.get() == "" or e_complan.get() == 0:
            q_complan = 0
        else:
            try:
                q_complan = float(e_complan.get())
            except:
                valid_number = 1

        if e_noodles.get() == "" or e_noodles.get() == 0:
            q_noodles = 0
        else:
            try:
                q_noodles = float(e_noodles.get())
            except:
                valid_number = 1

        if e_pasta.get() == "" or e_pasta.get() == 0:
            q_pasta = 0
        else:
            try:
                q_pasta = float(e_pasta.get())
            except:
                valid_number = 1

        if e_ketchup.get() == "" or e_ketchup.get() == 0:
            q_ketchup = 0
        else:
            try:
                q_ketchup = float(e_ketchup.get())
            except:
                valid_number = 1

        if e_jam.get() == "" or e_jam.get() == 0:
            q_jam = 0
        else:
            try:
                q_jam = float(e_jam.get())
            except:
                valid_number = 1

        if e_bread_delux.get() == "" or e_bread_delux.get() == 0:
            q_bread_delux = 0
        else:
            try:
                q_bread_delux = float(e_bread_delux.get())
            except:
                valid_number = 1

        if e_bread_britania.get() == "" or e_bread_britania.get() == 0:
            q_bread_britania = 0
        else:
            try:
                q_bread_britania = float(e_bread_britania.get())
            except:
                valid_number = 1

        if valid_number == 1:
            messagebox.showerror("NUMBER", "PLEASE ENTER A VALID NUMBER", parent=innerframe10)
        innerframe10.destroy()

    def others():
        global innerframe10
        global e_papad
        global e_horlicks
        global e_complan
        global e_noodles
        global e_pasta
        global e_ketchup
        global e_jam
        global e_bread_delux
        global e_bread_britania

        global change_other
        change_other = 1

        global others1
        global others2
        global others3
        global others4
        global others5
        global others6
        global others7
        global others8
        global others9

        global o1
        global o2
        global o3
        global o4
        global o5
        global o6
        global o7
        global o8
        global o9

        o1 = IntVar()
        o2 = IntVar()
        o3 = IntVar()
        o4 = IntVar()
        o5 = IntVar()
        o6 = IntVar()
        o7 = IntVar()
        o8 = IntVar()
        o9 = IntVar()

        o1.set(0)
        o2.set(0)
        o3.set(0)
        o4.set(0)
        o5.set(0)
        o6.set(0)
        o7.set(0)
        o8.set(0)
        o9.set(0)

        innerframe10 = Toplevel(bg="#f6ead4", relief=GROOVE, bd=9)
        innerframe10.title("OTHERS")
        papad = Label(innerframe10, text="PAPAD", font=("Goudy old style", 15, "bold"), fg="#51361a",
                      bg="#f6ead4")
        papad.grid(row=0, column=0)
        horlicks = Label(innerframe10, text="HORLICKS", font=("Goudy old style", 15, "bold"), fg="#51361a",
                         bg="#f6ead4")
        horlicks.grid(row=1, column=0)
        complan = Label(innerframe10, text="COMPLAN", font=("Goudy old style", 15, "bold"), fg="#51361a",
                        bg="#f6ead4")
        complan.grid(row=2, column=0)
        noodles = Label(innerframe10, text="NOODLES", font=("Goudy old style", 15, "bold"), fg="#51361a",
                        bg="#f6ead4")
        noodles.grid(row=3, column=0)
        pasta = Label(innerframe10, text="PASTA", font=("Goudy old style", 15, "bold"), fg="#51361a",
                      bg="#f6ead4")
        pasta.grid(row=4, column=0)
        ketchup = Label(innerframe10, text="KETCHUP", font=("Goudy old style", 15, "bold"), fg="#51361a",
                        bg="#f6ead4")
        ketchup.grid(row=5, column=0)
        jam = Label(innerframe10, text="JAM", font=("Goudy old style", 15, "bold"), fg="#51361a",
                    bg="#f6ead4")
        jam.grid(row=6, column=0)
        bread_delux = Label(innerframe10, text="BREAD DELUX", font=("Goudy old style", 15, "bold"), fg="#51361a",
                            bg="#f6ead4")
        bread_delux.grid(row=7, column=0)
        bread_britania = Label(innerframe10, text="BREAD BRITANIA", font=("Goudy old style", 15, "bold"), fg="#51361a",
                               bg="#f6ead4")
        bread_britania.grid(row=8, column=0)

        e_papad = Entry(innerframe10, width=50, relief=SUNKEN, bd=4)
        e_papad.grid(row=0, column=2)
        e_horlicks = Entry(innerframe10, width=50, relief=SUNKEN, bd=4)
        e_horlicks.grid(row=1, column=2)
        e_complan = Entry(innerframe10, width=50, relief=SUNKEN, bd=4)
        e_complan.grid(row=2, column=2)
        e_noodles = Entry(innerframe10, width=50, relief=SUNKEN, bd=4)
        e_noodles.grid(row=3, column=2)
        e_pasta = Entry(innerframe10, width=50, relief=SUNKEN, bd=4)
        e_pasta.grid(row=4, column=2)
        e_ketchup = Entry(innerframe10, width=50, relief=SUNKEN, bd=4)
        e_ketchup.grid(row=5, column=2)
        e_jam = Entry(innerframe10, width=50, relief=SUNKEN, bd=4)
        e_jam.grid(row=6, column=2)
        e_bread_delux = Entry(innerframe10, width=50, relief=SUNKEN, bd=4)
        e_bread_delux.grid(row=7, column=2)
        e_bread_britania = Entry(innerframe10, width=50, relief=SUNKEN, bd=4)
        e_bread_britania.grid(row=8, column=2)

        others1 = Checkbutton(innerframe10, text="", fg="#51361a", bg="#f6ead4", variable=o1)
        others1.grid(row=0, column=3)
        others2 = Checkbutton(innerframe10, text="", fg="#51361a", bg="#f6ead4", variable=o2)
        others2.grid(row=1, column=3)
        others3 = Checkbutton(innerframe10, text="", fg="#51361a", bg="#f6ead4", variable=o3)
        others3.grid(row=2, column=3)
        others4 = Checkbutton(innerframe10, text="", fg="#51361a", bg="#f6ead4", variable=o4)
        others4.grid(row=3, column=3)
        others5 = Checkbutton(innerframe10, text="", fg="#51361a", bg="#f6ead4", variable=o5)
        others5.grid(row=4, column=3)
        others6 = Checkbutton(innerframe10, text="", fg="#51361a", bg="#f6ead4", variable=o6)
        others6.grid(row=5, column=3)
        others7 = Checkbutton(innerframe10, text="", fg="#51361a", bg="#f6ead4", variable=o7)
        others7.grid(row=6, column=3)
        others8 = Checkbutton(innerframe10, text="", fg="#51361a", bg="#f6ead4", variable=o8)
        others8.grid(row=7, column=3)
        others9 = Checkbutton(innerframe10, text="", fg="#51361a", bg="#f6ead4", variable=o9)
        others9.grid(row=8, column=3)

        total = Button(innerframe10, text="TOTAL", command=cal10, width=20, font=("times new roaman", 15, "bold"),
                       fg="#51361a", bg="#b4a284", relief=GROOVE, bd=9)
        total.grid(row=9, column=0, columnspan=3, pady=15)

    def total():
        global total1
        global p_turmeric_powder
        global p_sugar
        global p_jaggery
        global p_old_rice
        global p_new_rice
        global p_sona_masoori
        global p_basmati
        global p_wheat_flour
        global p_maida
        global p_multi_grain
        global p_rice_flour
        global p_besan_flour
        global p_rava
        global p_rice_rava
        global p_corn_flour
        global p_vermicelli
        global p_tamarind
        global p_red_chilli

        global p_turmeric_powder
        global p_sugar
        global p_jaggery
        global p_old_rice
        global p_new_rice
        global p_sona_masoori
        global p_basmati
        global p_wheat_flour
        global p_maida
        global p_multi_grain
        global p_rice_flour
        global p_besan_flour
        global p_rava
        global p_rice_rava
        global p_corn_flour
        global p_vermicelli
        global p_tamarind
        global p_red_chilli

        global p_toor_dal
        global p_urad_dal
        global p_moong_dal
        global p_chana_dal
        global p_rajma
        global p_whitp_chana

        global p_crystal_salt
        global p_powder_salt
        global p_redchilli_powder
        global p_dhania_powder
        global p_garammasala_powder
        global p_chatmasala_powder
        global p_pepper_powder
        global p_sambar_powder
        global p_biryani_powder
        global p_coffep_powder
        global p_tea_powder

        global p_cooking_oil
        global p_seasame_oil
        global p_coconut_oil
        global p_ghee
        global p_olive_oil

        global p_mustard_seed
        global p_pepper
        global p_jeera
        global p_khus_khus
        global p_dhania
        global p_black_seasamp_seeds
        global p_whitp_seasamp_seeds
        global p_cashew_nuts
        global p_raisins
        global p_badam
        global p_peanuts
        global p_dates

        global p_cheese_block
        global p_butter
        global p_yoghurt
        global p_fresh_cream
        global p_paneer

        global p_tooth_paste
        global p_tooth_brush
        global p_bathing_soap
        global p_shampoo
        global p_facp_powder
        global p_hand_sanitizer
        global p_deodarant
        global p_shaving_cream
        global p_hair_gel
        global p_razer_blade

        global p_dish_washing_soap
        global p_dish_washing_liquid
        global p_washing_powder
        global p_washing_soaps
        global p_bleaching_powder
        global p_sanitary_pad
        global p_toilet_paper
        global p_garbagp_bag
        global p_dettol
        global p_mosquito_liquid

        global p_bandages
        global p_light_bulbs
        global p_batteries
        global p_candles

        global p_papad
        global p_horlicks
        global p_complan
        global p_noodles
        global p_pasta
        global p_ketchup
        global p_jam
        global p_bread_delux
        global p_bread_britania

        global change_rice
        global change_pulses
        global change_spice
        global change_oils
        global change_snuts
        global change_dairy
        global change_toi
        global change_clean
        global change_mis
        global change_other

        global r1
        global r2
        global r3
        global r4
        global r5
        global r6
        global r7
        global r8
        global r9
        global r10
        global r11
        global r12
        global r13
        global r14
        global r15
        global r16
        global r17
        global r18

        global p1
        global p2
        global p3
        global p4
        global p5
        global p6

        global sp1
        global sp2
        global sp3
        global sp4
        global sp5
        global sp6
        global sp7
        global sp8
        global sp9
        global sp10
        global sp11

        global o1
        global o2
        global o3
        global o4
        global o5
        global o6
        global o7
        global o8
        global o9

        global m1
        global m2
        global m3
        global m4

        global c1
        global c2
        global c3
        global c4
        global c5
        global c6
        global c7
        global c8
        global c9
        global c10

        global t1
        global t2
        global t3
        global t4
        global t5
        global t6
        global t7
        global t8
        global t9
        global t10

        global d1
        global d2
        global d3
        global d4
        global d5

        global sn1
        global sn2
        global sn3
        global sn4
        global sn5
        global sn6
        global sn7
        global sn8
        global sn9
        global sn10
        global sn11
        global sn12

        global oilll1
        global oilll2
        global oilll3
        global oilll4
        global oilll5

        con1 = sqlite3.connect('price.db')

        c1 = con1.cursor()

        c1.execute(" SELECT * FROM d_rice")
        rice_111 = c1.fetchall()
        rice1 = rice_111[0]
        '''
        p_turmeric_powder = rice1[1]
        p_sugar = rice1[2]
        p_jaggery = rice1[3]
        p_old_rice = rice1[4]
        p_new_rice = rice1[5]
        p_sona_masoori = rice1[6]
        p_basmati = rice1[7]
        p_wheat_flour = rice1[8]
        p_maida = rice1[9]
        p_multi_grain = rice1[10]
        p_rice_flour = rice1[11]
        p_besan_flour = rice1[12]
        p_rava = rice1[13]
        p_rice_rava = rice1[14]
        p_corn_flour = rice1[15]
        p_vermicelli = rice1[16]
        p_tamarind = rice1[17]
        p_red_chilli = rice1[18]
        '''
        c1.execute("SELECT * FROM d_pulses")
        pulses_111 = c1.fetchall()
        pulses1 = pulses_111[0]
        '''
        p_toor_dal = pulses1[1]
        p_urad_dal = pulses1[2]
        p_moong_dal = pulses1[3]
        p_chana_dal = pulses1[4]
        p_rajma = pulses1[5]
        p_whitp_chana = pulses1[6]
        '''
        c1.execute("SELECT * FROM d_spice_powder")
        spice_powder_111 = c1.fetchall()
        spice_p1 = spice_powder_111[0]
        '''
        p_crystal_salt = spice_p1[1]
        p_powder_salt = spice_p1[2]
        p_redchilli_powder = spice_p1[3]
        p_dhania_powder = spice_p1[4]
        p_garammasala_powder = spice_p1[5]
        p_chatmasala_powder = spice_p1[6]
        p_pepper_powder = spice_p1[7]
        p_sambar_powder = spice_p1[8]
        p_biryani_powder = spice_p1[9]
        p_coffep_powder = spice_p1[10]
        p_tea_powder = spice_p1[11]
        '''
        c1.execute("SELECT * FROM d_oils")
        oil_111 = c1.fetchall()
        oil1 = oil_111[0]
        '''
        p_cooking_oil = oil1[1]
        p_seasame_oil = oil1[2]
        p_coconut_oil = oil1[3]
        p_ghee = oil1[4]
        p_olive_oil = oil1[5]
        '''
        c1.execute("SELECT * FROM d_spices_nuts")
        spice_n_111 = c1.fetchall()
        spicen1 = spice_n_111[0]
        '''
        p_mustard_seed = spicen1[1]
        p_pepper = spicen1[2]
        p_jeera = spicen1[3]
        p_khus_khus = spicen1[4]
        p_dhania = spicen1[5]
        p_black_seasamp_seeds = spicen1[6]
        p_whitp_seasamp_seeds = spicen1[7]
        p_cashew_nuts = spicen1[8]
        p_raisins = spicen1[9]
        p_badam = spicen1[10]
        p_peanuts = spicen1[11]
        p_dates = spicen1[12]
        '''
        c1.execute("SELECT * FROM d_dairy")
        dairy_111 = c1.fetchall()
        dairy1 = dairy_111[0]
        '''
        p_cheese_block = dairy1[1]
        p_butter = dairy1[2]
        p_yoghurt = dairy1[3]
        p_fresh_cream = dairy1[4]
        p_paneer = dairy1[5]
        '''
        c1.execute("SELECT * FROM d_toiletries")
        toiletries_111 = c1.fetchall()
        toil1 = toiletries_111[0]
        '''
        p_tooth_paste = toil1[1]
        p_tooth_brush = toil1[2]
        p_bathing_soap = toil1[3]
        p_shampoo = toil1[4]
        p_facp_powder = toil1[5]
        p_hand_sanitizer = toil1[6]
        p_deodarant = toil1[7]
        p_shaving_cream = toil1[8]
        p_hair_gel = toil1[9]
        p_razer_blade = toil1[10]
        '''
        c1.execute("SELECT * FROM d_clean")
        clean_111 = c1.fetchall()
        clean1 = clean_111[0]

        p_dish_washing_soap = clean1[1]
        p_dish_washing_liquid = clean1[2]
        p_washing_powder = clean1[3]
        p_washing_soaps = clean1[4]
        p_bleaching_powder = clean1[5]
        p_sanitary_pad = clean1[6]
        p_toilet_paper = clean1[7]
        p_garbagp_bag = clean1[8]
        p_dettol = clean1[9]
        p_mosquito_liquid = clean1[10]

        c1.execute("SELECT * FROM d_mis")
        mis_111 = c1.fetchall()
        mis1 = mis_111[0]
        '''
        p_bandages = mis1[1]
        p_light_bulbs = mis1[2]
        p_batteries = mis1[3]
        p_candles = mis1[4]
        '''
        c1.execute("SELECT * FROM d_others")
        other_111 = c1.fetchall()
        other1 = other_111[0]
        '''
        p_papad = other1[1]
        p_horlicks = other1[2]
        p_complan = other1[3]
        p_noodles = other1[4]
        p_pasta = other1[5]
        p_ketchup = other1[6]
        p_jam = other1[7]
        p_bread_delux = other1[8]
        p_bread_britania = other1[9]
        '''
        con1.commit()

        con1.close()

        con1 = sqlite3.connect('price.db')

        c1 = con1.cursor()

        c1.execute(" SELECT * FROM d3_rice")
        rice_11 = c1.fetchall()
        rice3 = rice_11[0]
        '''
        p_turmeric_powder = rice3[1]
        p_sugar = rice3[2]
        p_jaggery = rice3[3]
        p_old_rice = rice3[4]
        p_new_rice = rice3[5]
        p_sona_masoori = rice3[6]
        p_basmati = rice3[7]
        p_wheat_flour = rice3[8]
        p_maida = rice3[9]
        p_multi_grain = rice3[10]
        p_rice_flour = rice3[11]
        p_besan_flour = rice3[12]
        p_rava = rice3[13]
        p_rice_rava = rice3[14]
        p_corn_flour = rice3[15]
        p_vermicelli = rice3[16]
        p_tamarind = rice3[17]
        p_red_chilli = rice3[18]
        '''
        c1.execute("SELECT * FROM d3_pulses")
        pulses_11 = c1.fetchall()
        pulses3 = pulses_11[0]
        '''
        p_toor_dal = pulses3[1]
        p_urad_dal = pulses3[2]
        p_moong_dal = pulses3[3]
        p_chana_dal = pulses3[4]
        p_rajma = pulses3[5]
        p_whitp_chana = pulses3[6]
        '''

        c1.execute("SELECT * FROM d3_spice_powder")
        spice_powder_11 = c1.fetchall()
        spice_p3 = spice_powder_11[0]
        '''
        p_crystal_salt = spice_p3[1]
        p_powder_salt = spice_p3[2]
        p_redchilli_powder = spice_p3[3]
        p_dhania_powder = spice_p3[4]
        p_garammasala_powder = spice_p3[5]
        p_chatmasala_powder = spice_p3[6]
        p_pepper_powder = spice_p3[7]
        p_sambar_powder = spice_p3[8]
        p_biryani_powder = spice_p3[9]
        p_coffep_powder = spice_p3[10]
        p_tea_powder = spice_p3[11]
        '''
        c1.execute("SELECT * FROM d3_oils")
        oil_11 = c1.fetchall()
        oil3 = oil_11[0]
        '''
        p_cooking_oil = oil3[1]
        p_seasame_oil = oil3[2]
        p_coconut_oil = oil3[3]
        p_ghee = oil3[4]
        p_olive_oil = oil3[5]
        '''
        c1.execute("SELECT * FROM d3_spices_nuts")
        spice_n_11 = c1.fetchall()
        spicen3 = spice_n_11[0]
        '''
        p_mustard_seed = spicen3[1]
        p_pepper = spicen3[2]
        p_jeera = spicen3[3]
        p_khus_khus = spicen3[4]
        p_dhania = spicen3[5]
        p_black_seasamp_seeds = spicen3[6]
        p_whitp_seasamp_seeds = spicen3[7]
        p_cashew_nuts = spicen3[8]
        p_raisins = spicen3[9]
        p_badam = spicen3[10]
        p_peanuts = spicen3[11]
        p_dates = spicen3[12]
        '''
        c1.execute("SELECT * FROM d3_dairy")
        dairy_11 = c1.fetchall()
        dairy3 = dairy_11[0]
        '''
        p_cheese_block = dairy3[1]
        p_butter = dairy3[2]
        p_yoghurt = dairy3[3]
        p_fresh_cream = dairy3[4]
        p_paneer = dairy3[5]
        '''
        c1.execute("SELECT * FROM d3_toiletries")
        toiletries_11 = c1.fetchall()
        toil3 = toiletries_11[0]
        '''
        p_tooth_paste = toil3[1]
        p_tooth_brush = toil3[2]
        p_bathing_soap = toil3[3]
        p_shampoo = toil3[4]
        p_facp_powder = toil3[5]
        p_hand_sanitizer = toil3[6]
        p_deodarant = toil3[7]
        p_shaving_cream = toil3[8]
        p_hair_gel = toil3[9]
        p_razer_blade = toil3[10]
        '''
        c1.execute("SELECT * FROM d3_clean")
        clean_11 = c1.fetchall()
        clean3 = clean_11[0]
        '''
        p_dish_washing_soap = clean3[1]
        p_dish_washing_liquid = clean3[2]
        p_washing_powder = clean3[3]
        p_washing_soaps = clean3[4]
        p_bleaching_powder = clean3[5]
        p_sanitary_pad = clean3[6]
        p_toilet_paper = clean3[7]
        p_garbagp_bag = clean3[8]
        p_dettol = clean3[9]
        p_mosquito_liquid = clean3[10]
        '''
        c1.execute("SELECT * FROM d3_mis")
        mis_11 = c1.fetchall()
        mis3 = mis_11[0]
        '''
        p_bandages = mis3[1]
        p_light_bulbs = mis3[2]
        p_batteries = mis3[3]
        p_candles = mis3[4]
        '''
        c1.execute("SELECT * FROM d3_others")
        other_11 = c1.fetchall()
        other3 = other_11[0]
        '''
        p_papad = other3[1]
        p_horlicks = other3[2]
        p_complan = other3[3]
        p_noodles = other3[4]
        p_pasta = other3[5]
        p_ketchup = other3[6]
        p_jam = other3[7]
        p_bread_delux = other3[8]
        p_bread_britania = other3[9]
        '''
        con1.commit()

        con1.close()

        if change_rice == 1:
            if r1.get() == 0:
                p_turmeric_powder = rice1[1]
            else:
                p_turmeric_powder = rice3[1]
            if r2.get() == 0:
                p_sugar = rice1[2]
            else:
                p_sugar = rice3[2]
            if r3.get() == 0:
                p_jaggery = rice1[3]
            else:
                p_jaggery = rice3[3]
            if r4.get() == 0:
                p_old_rice = rice1[4]
            else:
                p_old_rice = rice3[4]
            if r5.get() == 0:
                p_new_rice = rice1[5]
            else:
                p_new_rice = rice3[5]
            if r6.get() == 0:
                p_sona_masoori = rice1[6]
            else:
                p_sona_masoori = rice3[6]
            if r7.get() == 0:
                p_basmati = rice1[7]
            else:
                p_basmati = rice3[7]
            if r8.get() == 0:
                p_wheat_flour = rice1[8]
            else:
                p_wheat_flour = rice3[8]
            if r9.get() == 0:
                p_maida = rice1[9]
            else:
                p_maida = rice3[9]
            if r10.get() == 0:
                p_multi_grain = rice1[10]
            else:
                p_multi_grain = rice3[10]
            if r11.get() == 0:
                p_rice_flour = rice1[11]
            else:
                p_rice_flour = rice3[11]
            if r12.get() == 0:
                p_besan_flour = rice1[12]
            else:
                p_besan_flour = rice3[12]
            if r13.get() == 0:
                p_rava = rice1[13]
            else:
                p_rava = rice3[13]
            if r14.get() == 0:
                p_rice_rava = rice1[14]
            else:
                p_rice_rava = rice3[14]
            if r15.get() == 0:
                p_corn_flour = rice1[15]
            else:
                p_corn_flour = rice3[15]
            if r16.get() == 0:
                p_vermicelli = rice1[16]
            else:
                p_vermicelli = rice3[16]
            if r17.get() == 0:
                p_tamarind = rice1[17]
            else:
                p_tamarind = rice3[17]
            if r18.get() == 0:
                p_red_chilli = rice1[18]
            else:
                p_red_chilli = rice3[18]
        else:
            p_turmeric_powder = 0
            p_sugar = 0
            p_jaggery = 0
            p_old_rice = 0
            p_new_rice = 0
            p_sona_masoori = 0
            p_basmati = 0
            p_wheat_flour = 0
            p_maida = 0
            p_multi_grain = 0
            p_rice_flour = 0
            p_besan_flour = 0
            p_rava = 0
            p_rice_rava = 0
            p_corn_flour = 0
            p_vermicelli = 0
            p_tamarind = 0
            p_red_chilli = 0

        if change_pulses == 1:
            if p1.get() == 0:
                p_toor_dal = pulses1[1]
            else:
                p_toor_dal = pulses3[1]
            if p2.get() == 0:
                p_urad_dal = pulses1[2]
            else:
                p_urad_dal = pulses3[2]
            if p3.get() == 0:
                p_moong_dal = pulses1[3]
            else:
                p_moong_dal = pulses3[3]
            if p4.get() == 0:
                p_chana_dal = pulses1[4]
            else:
                p_chana_dal = pulses3[4]
            if p5.get() == 0:
                p_rajma = pulses1[5]
            else:
                p_rajma = pulses3[5]
            if p6.get() == 0:
                p_whitp_chana = pulses1[6]
            else:
                p_whitp_chana = pulses3[6]
        else:
            p_toor_dal = 0
            p_urad_dal = 0
            p_moong_dal = 0
            p_chana_dal = 0
            p_rajma = 0
            p_whitp_chana = 0

        if change_spice == 1:
            if sp1.get() == 0:
                p_crystal_salt = spice_p1[1]
            else:
                p_crystal_salt = spice_p3[1]
            if sp2.get() == 0:
                p_powder_salt = spice_p1[2]
            else:
                p_powder_salt = spice_p3[2]
            if sp3.get() == 0:
                p_redchilli_powder = spice_p1[3]
            else:
                p_redchilli_powder = spice_p3[3]
            if sp4.get() == 0:
                p_dhania_powder = spice_p1[4]
            else:
                p_dhania_powder = spice_p3[4]
            if sp5.get() == 0:
                p_garammasala_powder = spice_p1[5]
            else:
                p_garammasala_powder = spice_p3[5]
            if sp6.get() == 0:
                p_chatmasala_powder = spice_p1[6]
            else:
                p_chatmasala_powder = spice_p3[6]
            if sp7.get() == 0:
                p_pepper_powder = spice_p1[7]
            else:
                p_pepper_powder = spice_p3[7]
            if sp8.get() == 0:
                p_sambar_powder = spice_p1[8]
            else:
                p_sambar_powder = spice_p3[8]
            if sp9.get() == 0:
                p_biryani_powder = spice_p1[9]
            else:
                p_biryani_powder = spice_p3[9]
            if sp10.get() == 0:
                p_coffep_powder = spice_p1[10]
            else:
                p_coffep_powder = spice_p3[10]
            if sp11.get() == 0:
                p_tea_powder = spice_p1[11]
            else:
                p_tea_powder = spice_p3[11]
        else:
            p_crystal_salt = 0
            p_powder_salt = 0
            p_redchilli_powder = 0
            p_dhania_powder = 0
            p_garammasala_powder = 0
            p_chatmasala_powder = 0
            p_pepper_powder = 0
            p_sambar_powder = 0
            p_biryani_powder = 0
            p_coffep_powder = 0
            p_tea_powder = 0

        if change_oils == 1:
            if oilll1.get() == 0:
                p_cooking_oil = oil1[1]
            else:
                p_cooking_oil = oil3[1]
            if oilll2.get() == 0:
                p_seasame_oil = oil1[2]
            else:
                p_seasame_oil = oil3[2]
            if oilll3.get() == 0:
                p_coconut_oil = oil1[3]
            else:
                p_coconut_oil = oil3[3]
            if oilll4.get() == 0:
                p_ghee = oil1[4]
            else:
                p_ghee = oil3[4]
            if oilll5.get() == 0:
                p_olive_oil = oil1[5]
            else:
                p_olive_oil = oil3[5]
        else:
            p_cooking_oil = 0
            p_seasame_oil = 0
            p_coconut_oil = 0
            p_ghee = 0
            p_olive_oil = 0

        if change_snuts == 1:
            if sn1.get() == 0:
                p_mustard_seed = spicen1[1]
            else:
                p_mustard_seed = spicen3[1]
            if sn2.get() == 0:
                p_pepper = spicen1[2]
            else:
                p_pepper = spicen3[2]
            if sn3.get() == 0:
                p_jeera = spicen1[3]
            else:
                p_jeera = spicen3[3]
            if sn4.get() == 0:
                p_khus_khus = spicen1[4]
            else:
                p_khus_khus = spicen3[4]
            if sn5.get() == 0:
                p_dhania = spicen1[5]
            else:
                p_dhania = spicen3[5]
            if sn6.get() == 0:
                p_black_seasamp_seeds = spicen1[6]
            else:
                p_black_seasamp_seeds = spicen3[6]
            if sn7.get() == 0:
                p_whitp_seasamp_seeds = spicen1[7]
            else:
                p_whitp_seasamp_seeds = spicen3[7]
            if sn8.get() == 0:
                p_cashew_nuts = spicen1[8]
            else:
                p_cashew_nuts = spicen3[8]
            if sn9.get() == 0:
                p_raisins = spicen1[9]
            else:
                p_raisins = spicen3[9]
            if sn10.get() == 0:
                p_badam = spicen1[10]
            else:
                p_badam = spicen3[10]
            if sn11.get() == 0:
                p_peanuts = spicen1[11]
            else:
                p_peanuts = spicen3[11]
            if sn12.get() == 0:
                p_dates = spicen1[12]
            else:
                p_dates = spicen3[12]
        else:
            p_mustard_seed = 0
            p_pepper = 0
            p_jeera = 0
            p_khus_khus = 0
            p_dhania = 0
            p_black_seasamp_seeds = 0
            p_whitp_seasamp_seeds = 0
            p_cashew_nuts = 0
            p_raisins = 0
            p_badam = 0
            p_peanuts = 0
            p_dates = 0

        if change_dairy == 1:
            if d1.get() == 0:
                p_cheese_block = dairy1[1]
            else:
                p_cheese_block = dairy3[1]
            if d2.get() == 0:
                p_butter = dairy1[2]
            else:
                p_butter = dairy3[2]
            if d3.get() == 0:
                p_yoghurt = dairy1[3]
            else:
                p_yoghurt = dairy3[3]
            if d4.get() == 0:
                p_fresh_cream = dairy1[4]
            else:
                p_fresh_cream = dairy3[4]
            if d5.get() == 0:
                p_paneer = dairy1[5]
            else:
                p_paneer = dairy3[5]
        else:
            p_cheese_block = 0
            p_butter = 0
            p_yoghurt = 0
            p_fresh_cream = 0
            p_paneer = 0

        if change_toi == 1:
            if t1.get() == 0:
                p_tooth_paste = toil1[1]
            else:
                p_tooth_paste = toil3[1]
            if t2.get() == 0:
                p_tooth_brush = toil1[2]
            else:
                p_tooth_brush = toil3[2]
            if t3.get() == 0:
                p_bathing_soap = toil1[3]
            else:
                p_bathing_soap = toil3[3]
            if t4.get() == 0:
                p_shampoo = toil1[4]
            else:
                p_shampoo = toil3[4]
            if t5.get() == 0:
                p_facp_powder = toil1[5]
            else:
                p_facp_powder = toil3[5]
            if t6.get() == 0:
                p_hand_sanitizer = toil1[6]
            else:
                p_hand_sanitizer = toil3[6]
            if t7.get() == 0:
                p_deodarant = toil1[7]
            else:
                p_deodarant = toil3[7]
            if t8.get() == 0:
                p_shaving_cream = toil1[8]
            else:
                p_shaving_cream = toil3[8]
            if t9.get() == 0:
                p_hair_gel = toil1[9]
            else:
                p_hair_gel = toil3[9]
            if t10.get() == 0:
                p_razer_blade = toil1[10]
            else:
                p_razer_blade = toil3[10]
        else:
            p_tooth_paste = 0
            p_tooth_brush = 0
            p_bathing_soap = 0
            p_shampoo = 0
            p_facp_powder = 0
            p_hand_sanitizer = 0
            p_deodarant = 0
            p_shaving_cream = 0
            p_hair_gel = 0
            p_razer_blade = 0

        '''
        if c1.get() == 0:
            p_dish_washing_soap = clean1[1]
        else:
            p_dish_washing_soap = clean3[1]
        if c2.get() == 0:
            p_dish_washing_liquid = clean1[2]
        else:
            p_dish_washing_liquid = clean3[2]
        if c3.get() == 0:
            p_washing_powder = clean1[3]
        else:
            p_washing_powder = clean3[3]
        if c4.get() == 0:
            p_washing_soaps = clean1[4]
        else:
            p_washing_soaps = clean3[4]
        if c5.get() == 0:
            p_bleaching_powder = clean1[5]
        else:
            p_bleaching_powder = clean3[5]
        if c6.get() == 0:
            p_sanitary_pad = clean1[6]
        else:
            p_sanitary_pad = clean3[6]
        if c7.get() == 0:
            p_toilet_paper = clean1[7]
        else:
            p_toilet_paper = clean3[7]
        if c8.get() == 0:
            p_garbagp_bag = clean1[8]
        else:
            p_garbagp_bag = clean3[8]
        if c9.get() == 0:
            p_dettol = clean1[9]
        else:
            p_dettol = clean3[9]
        if c10.get() == 0:
            p_mosquito_liquid = clean1[10]
        else:
            p_mosquito_liquid = clean3[10]
        '''

        if change_mis == 1:
            if m1.get() == 0:
                p_bandages = mis1[1]
            else:
                p_bandages = mis3[1]
            if m2.get() == 0:
                p_light_bulbs = mis1[2]
            else:
                p_light_bulbs = mis3[2]
            if m3.get() == 0:
                p_batteries = mis1[3]
            else:
                p_batteries = mis3[3]
            if m4.get() == 0:
                p_candles = mis1[4]
            else:
                p_candles = mis3[4]
        else:
            p_bandages = 0
            p_light_bulbs = 0
            p_batteries = 0
            p_candles = 0

        if change_other == 1:
            if o1.get() == 0:
                p_papad = other1[1]
            else:
                p_papad = other3[1]
            if o2.get() == 0:
                p_horlicks = other1[2]
            else:
                p_horlicks = other3[2]
            if o3.get() == 0:
                p_complan = other1[3]
            else:
                p_complan = other3[3]
            if o4.get() == 0:
                p_noodles = other1[4]
            else:
                p_noodles = other3[4]
            if o5.get() == 0:
                p_pasta = other1[5]
            else:
                p_pasta = other3[5]
            if o6.get() == 0:
                p_ketchup = other1[6]
            else:
                p_ketchup = other3[6]
            if o7.get() == 0:
                p_jam = other1[7]
            else:
                p_jam = other3[7]
            if o8.get() == 0:
                p_bread_delux = other1[8]
            else:
                p_bread_delux = other3[8]
            if o9.get() == 0:
                p_bread_britania = other1[9]
            else:
                p_bread_britania = other3[9]
        else:
            p_papad = 0
            p_horlicks = 0
            p_complan = 0
            p_noodles = 0
            p_pasta = 0
            p_ketchup = 0
            p_jam = 0
            p_bread_delux = 0
            p_bread_britania = 0

        total1 = str(
            float(float(p_turmeric_powder) * float(q_turmeric_powder)) +
            float(float(p_sugar) * float(q_sugar)) + float(
                float(p_jaggery) * float(q_jaggery)) + float(float(p_old_rice) * float(q_old_rice)) + float(
                float(p_new_rice) * float(q_new_rice)) + float(float(p_sona_masoori) * float(q_sona_masoori)) + float(
                float(p_basmati) * float(q_basmati)) + float(float(p_wheat_flour) * float(q_wheat_flour)) + float(
                float(p_maida) * float(q_maida)) + float(float(p_multi_grain) * float(q_multi_grain)) + float(
                float(p_rice_flour) * float(q_multi_grain)) + float(float(p_rice_flour) * float(q_rice_flour)) + float(
                float(p_besan_flour) * float(q_besan_flour)) + float(float(p_rava) * float(q_rava)) + float(
                float(p_rice_rava) * float(q_rice_rava)) + float(float(p_corn_flour) * float(q_corn_flour)) + float(
                float(p_vermicelli) * float(q_vermicelli)) + float(float(p_tamarind) * float(q_tamarind)) + float(
                float(p_red_chilli) * float(q_red_chilli)) + float(float(p_toor_dal) * float(q_toor_dal)) + float(
                float(p_urad_dal) * float(q_urad_dal)) + float(
                float(p_moong_dal) * float(q_moong_dal)) + float(
                float(p_chana_dal) * float(q_chana_dal)) + float(
                float(p_rajma) * float(q_rajma)) + float(
                float(p_whitp_chana) * float(q_white_chana)) + float(
                float(p_crystal_salt) * float(q_crystal_salt)) + float(
                float(p_powder_salt) * float(q_powder_salt)) + float(
                float(p_redchilli_powder) * float(q_redchilli_powder)) + float(
                float(p_dhania_powder) * float(q_dhania_powder)) + float(
                float(p_garammasala_powder) * float(q_garammasala_powder)) + float(
                float(p_chatmasala_powder) * float(q_chatmasala_powder)) +
            float(float(p_pepper_powder) * float(q_pepper_powder)) + float(
                float(p_sambar_powder) * float(q_sambar_powder)) + float(
                float(p_biryani_powder) * float(q_biryani_powder)) + float(
                float(p_coffep_powder) * float(q_coffee_powder)) + float(
                float(p_tea_powder) * float(q_tea_powder)) + float(float(p_cooking_oil) * float(q_cooking_oil)) + float(
                float(p_seasame_oil) * float(q_seasame_oil)) + float(
                float(p_coconut_oil) * float(q_coconut_oil)) + float(
                float(p_ghee) * float(q_ghee)) + float(
                float(p_olive_oil) * float(q_olive_oil)) + float(float(p_mustard_seed) * float(q_mustard_seed)) + float(
                float(p_pepper) * float(q_pepper)) + float(
                float(p_jeera) * float(q_jeera)) + float(
                float(p_khus_khus) * float(q_khus_khus)) + float(
                float(p_dhania) * float(q_dhania)) + float(
                float(p_black_seasamp_seeds) * float(q_black_seasame_seeds)) + float(
                float(p_whitp_seasamp_seeds) * float(q_white_seasame_seeds)) + float(
                float(p_cashew_nuts) * float(q_cashew_nuts)) + float(
                float(p_raisins) * float(q_raisins)) + float(
                float(p_badam) * float(q_badam)) + float(
                float(p_peanuts) * float(q_peanuts)) + float(
                float(p_dates) * float(q_dates)) + float(float(p_cheese_block) * float(q_cheese_block)) + float(
                float(p_butter) * float(q_butter)) + float(
                float(p_yoghurt) * float(q_yoghurt)) + float(
                float(p_fresh_cream) * float(q_fresh_cream)) + float(
                float(p_paneer) * float(q_paneer)) + float(float(p_tooth_paste) * float(q_tooth_paste)) + float(
                float(p_tooth_brush) * float(q_tooth_brush)) + float(
                float(p_bathing_soap) * float(q_bathing_soap)) + float(
                float(p_shampoo) * float(q_shampoo)) + float(
                float(p_facp_powder) * float(q_face_powder)) + float(
                float(p_hand_sanitizer) * float(q_hand_sanitizer)) + float(
                float(p_deodarant) * float(q_deodarant)) + float(
                float(p_shaving_cream) * float(q_shaving_cream)) + float(
                float(p_hair_gel) * float(q_hair_gel)) + float(
                float(p_razer_blade) * float(q_razer_blade)) + float(
                float(p_dish_washing_soap) * float(q_dish_washing_soap)) + float(
                float(p_dish_washing_liquid) * float(q_dish_washing_liquid)) + float(
                float(p_washing_powder) * float(q_washing_powder)) + float(
                float(p_washing_soaps) * float(q_washing_soaps)) + float(
                float(p_bleaching_powder) * float(q_bleaching_powder)) + float(
                float(p_sanitary_pad) * float(q_sanitary_pad)) + float(
                float(p_toilet_paper) * float(q_toilet_paper)) + float(
                float(p_garbagp_bag) * float(q_garbage_bag)) + float(
                float(p_dettol) * float(q_dettol)) + float(
                float(p_mosquito_liquid) * float(q_mosquito_liquid)) + float(
                float(p_bandages) * float(q_bandages)) + float(
                float(p_light_bulbs) * float(q_light_bulbs)) + float(
                float(p_batteries) * float(q_batteries)) + float(
                float(p_candles) * float(q_candles)) + float(float(p_papad) * float(q_papad)) + float(
                float(p_horlicks) * float(q_horlicks)) + float(
                float(p_complan) * float(q_complan)) + float(
                float(p_noodles) * float(q_noodles)) + float(
                float(p_pasta) * float(q_pasta)) + float(
                float(p_ketchup) * float(q_ketchup)) + float(
                float(p_jam) * float(q_jam)) + float(
                float(p_bread_delux) * float(q_bread_delux)) + float(
                float(p_bread_britania) * float(q_bread_britania)))

        global ftotal
        if total_entry.get() != "" or total_entry.get() == "Rs 0.0":
            total_entry.delete(0, END)

        total_entry.insert(0, "Rs " + total1)

    def clearr():
        global q_turmeric_powder
        global q_sugar
        global q_jaggery
        global q_old_rice
        global q_new_rice
        global q_sona_masoori
        global q_basmati
        global q_wheat_flour
        global q_maida
        global q_multi_grain
        global q_rice_flour
        global q_besan_flour
        global q_rava
        global q_rice_rava
        global q_corn_flour
        global q_vermicelli
        global q_tamarind
        global q_red_chilli
        q_turmeric_powder = 0
        q_sugar = 0
        q_jaggery = 0
        q_old_rice = 0
        q_new_rice = 0
        q_sona_masoori = 0
        q_basmati = 0
        q_wheat_flour = 0
        q_maida = 0
        q_multi_grain = 0
        q_rice_flour = 0
        q_besan_flour = 0
        q_rava = 0
        q_rice_rava = 0
        q_corn_flour = 0
        q_vermicelli = 0
        q_tamarind = 0
        q_red_chilli = 0

        global q_toor_dal
        global q_urad_dal
        global q_moong_dal
        global q_chana_dal
        global q_rajma
        global q_white_chana
        q_toor_dal = 0
        q_urad_dal = 0
        q_moong_dal = 0
        q_chana_dal = 0
        q_rajma = 0
        q_white_chana = 0

        global q_crystal_salt
        global q_powder_salt
        global q_redchilli_powder
        global q_dhania_powder
        global q_garammasala_powder
        global q_chatmasala_powder
        global q_pepper_powder
        global q_sambar_powder
        global q_biryani_powder
        global q_coffee_powder
        global q_tea_powder
        q_crystal_salt = 0
        q_powder_salt = 0
        q_redchilli_powder = 0
        q_dhania_powder = 0
        q_garammasala_powder = 0
        q_chatmasala_powder = 0
        q_pepper_powder = 0
        q_sambar_powder = 0
        q_biryani_powder = 0
        q_coffee_powder = 0
        q_tea_powder = 0

        global q_cooking_oil
        global q_seasame_oil
        global q_coconut_oil
        global q_ghee
        global q_olive_oil
        q_cooking_oil = 0
        q_seasame_oil = 0
        q_coconut_oil = 0
        q_ghee = 0
        q_olive_oil = 0

        global q_mustard_seed
        global q_pepper
        global q_jeera
        global q_khus_khus
        global q_dhania
        global q_black_seasame_seeds
        global q_white_seasame_seeds
        global q_cashew_nuts
        global q_raisins
        global q_badam
        global q_peanuts
        global q_dates
        q_mustard_seed = 0
        q_pepper = 0
        q_jeera = 0
        q_khus_khus = 0
        q_dhania = 0
        q_black_seasame_seeds = 0
        q_white_seasame_seeds = 0
        q_cashew_nuts = 0
        q_raisins = 0
        q_badam = 0
        q_peanuts = 0
        q_dates = 0

        global q_cheese_block
        global q_butter
        global q_yoghurt
        global q_fresh_cream
        global q_paneer
        q_cheese_block = 0
        q_butter = 0
        q_yoghurt = 0
        q_fresh_cream = 0
        q_paneer = 0

        global q_tooth_paste
        global q_tooth_brush
        global q_bathing_soap
        global q_shampoo
        global q_face_powder
        global q_hand_sanitizer
        global q_deodarant
        global q_shaving_cream
        global q_hair_gel
        global q_razer_blade
        q_tooth_paste = 0
        q_tooth_brush = 0
        q_bathing_soap = 0
        q_shampoo = 0
        q_face_powder = 0
        q_hand_sanitizer = 0
        q_deodarant = 0
        q_shaving_cream = 0
        q_hair_gel = 0
        q_razer_blade = 0

        global q_dish_washing_soap
        global q_dish_washing_liquid
        global q_washing_powder
        global q_washing_soaps
        global q_bleaching_powder
        global q_sanitary_pad
        global q_toilet_paper
        global q_garbage_bag
        global q_dettol
        global q_mosquito_liquid
        q_dish_washing_soap = 0
        q_dish_washing_liquid = 0
        q_washing_powder = 0
        q_washing_soaps = 0
        q_bleaching_powder = 0
        q_sanitary_pad = 0
        q_toilet_paper = 0
        q_garbage_bag = 0
        q_dettol = 0
        q_mosquito_liquid = 0

        global q_bandages
        global q_light_bulbs
        global q_batteries
        global q_candles
        q_bandages = 0
        q_light_bulbs = 0
        q_batteries = 0
        q_candles = 0

        global q_papad
        global q_horlicks
        global q_complan
        global q_noodles
        global q_pasta
        global q_ketchup
        global q_jam
        global q_bread_delux
        global q_bread_britania
        q_papad = 0
        q_horlicks = 0
        q_complan = 0
        q_noodles = 0
        q_pasta = 0
        q_ketchup = 0
        q_jam = 0
        q_bread_delux = 0
        q_bread_britania = 0
        global change_rice
        global change_pulses
        global change_spice
        global change_oils
        global change_snuts
        global change_dairy
        global change_toi
        global change_clean
        global change_mis
        global change_other

        change_rice = 0
        change_pulses = 0
        change_spice = 0
        change_oils = 0
        change_snuts = 0
        change_dairy = 0
        change_toi = 0
        change_clean = 0
        change_mis = 0
        change_other = 0
        total()

    customer_label = Label(last_frame, text="CUSTOMER NAME", bg="#f6ead4", fg="#51361a",
                           font=("times new roman", 14, "bold"))
    customer_label.grid(row=0, column=0, pady=(15, 0), padx=(15, 0))

    customer_entry = Entry(last_frame, width=35, relief=SUNKEN, bd=4)
    customer_entry.grid(row=0, column=1, pady=(15, 0), padx=(10, 0))

    customer_number = Label(last_frame, text="PHONE NUMBER", bg="#f6ead4", fg="#51361a",
                            font=("times new roman", 14, "bold"))
    customer_number.grid(row=0, column=2, pady=(15, 0), padx=(15, 0))

    number_entry = Entry(last_frame, width=35, relief=SUNKEN, bd=4)
    number_entry.grid(row=0, column=3, pady=(15, 0), padx=(10, 0))

    global c_name
    global p_no
    c_name = 0
    p_no = 0
    r_bill = random.randint(1000, 9999)

    def bill_area():
        txtarea.delete(1.0, END)
        # txtarea.insert(END, "\n")
        txtarea.insert(END, "\t\tGROCEMART")
        txtarea.insert(END, "\n" + "========================================")
        txtarea.insert(END, "\n" + "BILL NUMBER : ")
        txtarea.insert(END, r_bill)
        txtarea.insert(END, "\n" + "CUSTOMER NAME :")
        if customer_entry.get() == "":
            c_name = ""
        else:
            c_name = customer_entry.get()
        txtarea.insert(END, " " + c_name)
        txtarea.insert(END, "\n" + "PHONE NUMBER : ")
        if number_entry.get() == "":
            p_no = ""
        else:
            p_no = number_entry.get()
        txtarea.insert(END, p_no)
        txtarea.insert(END, "\n" + "========================================")
        txtarea.insert(END, "\n" + "PRODUCT NAME")
        txtarea.insert(END, "\t\t" + "QUANTITY")
        txtarea.insert(END, "\t\t" + "PRICE")
        txtarea.insert(END, "\n" + "========================================")

        if q_turmeric_powder != 0:
            txtarea.insert(END, "\n" + "turmeric powder" + "\t\t" + str(q_turmeric_powder) + "\t\t" + str(
                float(float(p_turmeric_powder) * float(q_turmeric_powder))))
        if q_sugar != 0:
            txtarea.insert(END, "\n" + "sugar" + "\t\t" + str(q_sugar) + "\t\t" + str(
                float(float(p_sugar) * float(q_sugar))))
        if q_jaggery != 0:
            txtarea.insert(END, "\n" + "jaggery" + "\t\t" + str(q_jaggery) + "\t\t" + str(
                float(float(p_jaggery) * float(q_jaggery))))
        if q_old_rice != 0:
            txtarea.insert(END, "\n" + "old rice" + "\t\t" + str(q_old_rice) + "\t\t" + str(
                float(float(p_old_rice) * float(q_old_rice))))
        if q_new_rice != 0:
            txtarea.insert(END, "\n" + "new rice" + "\t\t" + str(q_new_rice) + "\t\t" + str(
                float(float(p_new_rice) * float(q_new_rice))))
        if q_sona_masoori != 0:
            txtarea.insert(END, "\n" + "sona masoori " + "\t\t" + str(q_sona_masoori) + "\t\t" + str(
                float(float(p_sona_masoori) * float(q_sona_masoori))))
        if q_basmati != 0:
            txtarea.insert(END, "\n" + "basmati " + "\t\t" + str(q_basmati) + "\t\t" + str(
                float(float(p_basmati) * float(q_basmati))))
        if q_wheat_flour != 0:
            txtarea.insert(END, "\n" + "wheat flour" + "\t\t" + str(q_wheat_flour) + "\t\t" + str(
                float(float(p_wheat_flour) * float(q_wheat_flour))))
        if q_maida != 0:
            txtarea.insert(END, "\n" + "maida" + "\t\t" + str(q_maida) + "\t\t" + str(
                float(float(p_maida) * float(q_maida))))
        if q_multi_grain != 0:
            txtarea.insert(END, "\n" + "multi grain" + "\t\t" + str(q_multi_grain) + "\t\t" + str(
                float(float(p_multi_grain) * float(q_multi_grain))))
        if q_rice_flour != 0:
            txtarea.insert(END, "\n" + "rice flour" + "\t\t" + str(q_rice_flour) + "\t\t" + str(
                float(float(p_rice_flour) * float(q_rice_flour))))
        if q_besan_flour != 0:
            txtarea.insert(END, "\n" + "besan flour" + "\t\t" + str(q_besan_flour) + "\t\t" + str(
                float(float(p_besan_flour) * float(q_besan_flour))))
        if q_rava != 0:
            txtarea.insert(END,
                           "\n" + "rava" + "\t\t" + str(q_rava) + "\t\t" + str(float(float(p_rava) * float(q_rava))))
        if q_rice_rava != 0:
            txtarea.insert(END, "\n" + "rice rava" + "\t\t" + str(q_rice_rava) + "\t\t" + str(
                float(float(p_rice_rava) * float(q_rice_rava))))
        if q_corn_flour != 0:
            txtarea.insert(END, "\n" + "corn flour" + "\t\t" + str(q_corn_flour) + "\t\t" + str(
                float(float(p_corn_flour) * float(q_corn_flour))))
        if q_vermicelli != 0:
            txtarea.insert(END, "\n" + "vermicelli " + "\t\t" + str(q_vermicelli) + "\t\t" + str(
                float(float(p_vermicelli) * float(q_vermicelli))))
        if q_tamarind != 0:
            txtarea.insert(END, "\n" + "tamarind " + "\t\t" + str(q_tamarind) + "\t\t" + str(
                float(float(p_tamarind) * float(q_tamarind))))
        if q_red_chilli != 0:
            txtarea.insert(END, "\n" + "red chilli" + "\t\t" + str(q_red_chilli) + "\t\t" + str(
                float(float(p_red_chilli) * float(q_red_chilli))))

        if q_toor_dal != 0:
            txtarea.insert(END, "\n" + "toor dal" + "\t\t" + str(q_toor_dal) + "\t\t" + str(
                float(float(p_toor_dal) * float(q_toor_dal))))
        if q_urad_dal != 0:
            txtarea.insert(END, "\n" + "urad dal" + "\t\t" + str(q_urad_dal) + "\t\t" + str(
                float(float(p_urad_dal) * float(q_urad_dal))))
        if q_moong_dal != 0:
            txtarea.insert(END, "\n" + "moong dal" + "\t\t" + str(q_moong_dal) + "\t\t" + str(
                float(float(p_moong_dal) * float(q_moong_dal))))
        if q_chana_dal != 0:
            txtarea.insert(END, "\n" + "chana dal" + "\t\t" + str(q_chana_dal) + "\t\t" + str(
                float(float(p_chana_dal) * float(q_chana_dal))))
        if q_rajma != 0:
            txtarea.insert(END, "\n" + "rajma" + "\t\t" + str(q_rajma) + "\t\t" + str(
                float(float(p_rajma) * float(q_rajma))))
        if q_white_chana != 0:
            txtarea.insert(END, "\n" + "white chana" + "\t\t" + str(q_white_chana) + "\t\t" + str(
                float(float(p_whitp_chana) * float(q_white_chana))))

        if q_crystal_salt != 0:
            txtarea.insert(END, "\n" + "crystal salt" + "\t\t" + str(q_crystal_salt) + "\t\t" + str(
                float(float(p_crystal_salt) * float(q_crystal_salt))))
        if q_powder_salt != 0:
            txtarea.insert(END, "\n" + "powder salt" + "\t\t" + str(q_powder_salt) + "\t\t" + str(
                float(float(p_powder_salt) * float(q_powder_salt))))
        if q_redchilli_powder != 0:
            txtarea.insert(END, "\n" + "redchili powder" + "\t\t" + str(q_redchilli_powder) + "\t\t" + str(
                float(float(p_redchilli_powder) * float(q_redchilli_powder))))
        if q_dhania_powder != 0:
            txtarea.insert(END, "\n" + "dhania powder" + "\t\t" + str(q_dhania_powder) + "\t\t" + str(
                float(float(p_dhania_powder) * float(q_dhania_powder))))
        if q_garammasala_powder != 0:
            txtarea.insert(END, "\n" + "garam masala" + "\t\t" + str(q_garammasala_powder) + "\t\t" + str(
                float(float(p_garammasala_powder) * float(q_garammasala_powder))))
        if q_chatmasala_powder != 0:
            txtarea.insert(END, "\n" + "chat masala" + "\t\t" + str(q_chatmasala_powder) + "\t\t" + str(
                float(float(p_chatmasala_powder) * float(q_chatmasala_powder))))
        if q_pepper_powder != 0:
            txtarea.insert(END, "\n" + "pepper powder" + "\t\t" + str(q_pepper_powder) + "\t\t" + str(
                float(float(p_pepper_powder) * float(q_pepper_powder))))
        if q_sambar_powder != 0:
            txtarea.insert(END, "\n" + "sambhar masala" + "\t\t" + str(q_sambar_powder) + "\t\t" + str(
                float(float(p_sambar_powder) * float(q_sambar_powder))))
        if q_biryani_powder != 0:
            txtarea.insert(END, "\n" + "biryani masala" + "\t\t" + str(q_biryani_powder) + "\t\t" + str(
                float(float(p_biryani_powder) * float(q_biryani_powder))))
        if q_coffee_powder != 0:
            txtarea.insert(END, "\n" + "coffee powder" + "\t\t" + str(q_coffee_powder) + "\t\t" + str(
                float(float(p_coffep_powder) * float(q_coffee_powder))))
        if q_tea_powder != 0:
            txtarea.insert(END, "\n" + "tea powder" + "\t\t" + str(q_tea_powder) + "\t\t" + str(
                float(float(p_tea_powder) * float(q_tea_powder))))

        if q_cooking_oil != 0:
            txtarea.insert(END, "\n" + "cooking oil" + "\t\t" + str(q_cooking_oil) + "\t\t" + str(
                float(float(p_cooking_oil) * float(q_cooking_oil))))
        if q_seasame_oil != 0:
            txtarea.insert(END, "\n" + "seasame oil" + "\t\t" + str(q_seasame_oil) + "\t\t" + str(
                float(float(p_seasame_oil) * float(q_seasame_oil))))
        if q_coconut_oil != 0:
            txtarea.insert(END, "\n" + "coconut oil" + "\t\t" + str(q_coconut_oil) + "\t\t" + str(
                float(float(p_coconut_oil) * float(q_coconut_oil))))
        if q_ghee != 0:
            txtarea.insert(END,
                           "\n" + "ghee" + "\t\t" + str(q_ghee) + "\t\t" + str(float(float(p_ghee) * float(q_ghee))))
        if q_olive_oil != 0:
            txtarea.insert(END, "\n" + "olive oil" + "\t\t" + str(q_olive_oil) + "\t\t" + str(
                float(float(p_olive_oil) * float(q_olive_oil))))

        if q_mustard_seed != 0:
            txtarea.insert(END, "\n" + "mustard seed" + "\t\t" + str(q_mustard_seed) + "\t\t" + str(
                float(float(p_mustard_seed) * float(q_mustard_seed))))
        if q_pepper != 0:
            txtarea.insert(END, "\n" + "pepper" + "\t\t" + str(q_pepper) + "\t\t" + str(
                float(float(p_pepper) * float(q_pepper))))
        if q_jeera != 0:
            txtarea.insert(END, "\n" + "jeera" + "\t\t" + str(q_jeera) + "\t\t" + str(
                float(float(p_jeera) * float(q_jeera))))
        if q_khus_khus != 0:
            txtarea.insert(END, "\n" + "khus khus" + "\t\t" + str(q_khus_khus) + "\t\t" + str(
                float(float(p_khus_khus) * float(q_khus_khus))))
        if q_dhania != 0:
            txtarea.insert(END, "\n" + "dhania" + "\t\t" + str(q_dhania) + "\t\t" + str(
                float(float(p_dhania) * float(q_dhania))))
        if q_black_seasame_seeds != 0:
            txtarea.insert(END, "\n" + "blackseasame seed" + "\t\t" + str(q_black_seasame_seeds) + "\t\t" + str(
                float(float(p_black_seasamp_seeds) * float(q_black_seasame_seeds))))
        if q_white_seasame_seeds != 0:
            txtarea.insert(END, "\n" + "whiteseasame seed" + "\t\t" + str(q_white_seasame_seeds) + "\t\t" + str(
                float(float(p_whitp_seasamp_seeds) * float(q_white_seasame_seeds))))
        if q_cashew_nuts != 0:
            txtarea.insert(END, "\n" + "cashew nuts" + "\t\t" + str(q_cashew_nuts) + "\t\t" + str(
                float(float(p_cashew_nuts) * float(q_cashew_nuts))))
        if q_raisins != 0:
            txtarea.insert(END, "\n" + "raisins" + "\t\t" + str(q_raisins) + "\t\t" + str(
                float(float(p_raisins) * float(q_raisins))))
        if q_badam != 0:
            txtarea.insert(END, "\n" + "badam" + "\t\t" + str(q_badam) + "\t\t" + str(
                float(float(p_badam) * float(q_badam))))
        if q_peanuts != 0:
            txtarea.insert(END, "\n" + "peanuts" + "\t\t" + str(q_peanuts) + "\t\t" + str(
                float(float(p_peanuts) * float(q_peanuts))))
        if q_dates != 0:
            txtarea.insert(END, "\n" + "dates" + "\t\t" + str(q_dates) + "\t\t" + str(
                float(float(p_dates) * float(q_dates))))

        if q_cheese_block != 0:
            txtarea.insert(END, "\n" + "cheese block" + "\t\t" + str(q_cheese_block) + "\t\t" + str(
                float(float(p_cheese_block) * float(q_cheese_block))))
        if q_butter != 0:
            txtarea.insert(END, "\n" + "butter" + "\t\t" + str(q_butter) + "\t\t" + str(
                float(float(p_butter) * float(q_butter))))
        if q_yoghurt != 0:
            txtarea.insert(END, "\n" + "yoghurt" + "\t\t" + str(q_yoghurt) + "\t\t" + str(
                float(float(p_yoghurt) * float(q_yoghurt))))
        if q_fresh_cream != 0:
            txtarea.insert(END, "\n" + "fresh cream" + "\t\t" + str(q_fresh_cream) + "\t\t" + str(
                float(float(p_fresh_cream) * float(q_fresh_cream))))
        if q_paneer != 0:
            txtarea.insert(END, "\n" + "paneer" + "\t\t" + str(q_paneer) + "\t\t" + str(
                float(float(p_paneer) * float(q_paneer))))

        if q_tooth_paste != 0:
            txtarea.insert(END, "\n" + "tooth paste" + "\t\t" + str(q_tooth_paste) + "\t\t" + str(
                float(float(p_tooth_paste) * float(q_tooth_paste))))
        if q_tooth_brush != 0:
            txtarea.insert(END, "\n" + "tooth brush" + "\t\t" + str(q_tooth_brush) + "\t\t" + str(
                float(float(p_tooth_brush) * float(q_tooth_brush))))
        if q_bathing_soap != 0:
            txtarea.insert(END, "\n" + "bathing soap" + "\t\t" + str(q_bathing_soap) + "\t\t" + str(
                float(float(p_bathing_soap) * float(q_bathing_soap))))
        if q_shampoo != 0:
            txtarea.insert(END, "\n" + "shampoo" + "\t\t" + str(q_shampoo) + "\t\t" + str(
                float(float(p_shampoo) * float(q_shampoo))))
        if q_face_powder != 0:
            txtarea.insert(END, "\n" + "face powder" + "\t\t" + str(q_face_powder) + "\t\t" + str(
                float(float(p_facp_powder) * float(q_face_powder))))
        if q_hand_sanitizer != 0:
            txtarea.insert(END, "\n" + "hand sanitizer" + "\t\t" + str(q_hand_sanitizer) + "\t\t" + str(
                float(float(p_hand_sanitizer) * float(q_hand_sanitizer))))
        if q_deodarant != 0:
            txtarea.insert(END, "\n" + "deodarant" + "\t\t" + str(q_deodarant) + "\t\t" + str(
                float(float(p_deodarant) * float(q_deodarant))))
        if q_shaving_cream != 0:
            txtarea.insert(END, "\n" + "shaving cream" + "\t\t" + str(q_shaving_cream) + "\t\t" + str(
                float(float(p_shaving_cream) * float(q_shaving_cream))))
        if q_hair_gel != 0:
            txtarea.insert(END, "\n" + "hair gel" + "\t\t" + str(q_hair_gel) + "\t\t" + str(
                float(float(p_hair_gel) * float(q_hair_gel))))
        if q_razer_blade != 0:
            txtarea.insert(END, "\n" + "razor blade" + "\t\t" + str(q_razer_blade) + "\t\t" + str(
                float(float(p_razer_blade) * float(q_razer_blade))))

        if q_dish_washing_soap != 0:
            txtarea.insert(END, "\n" + "dish washing soap" + "\t\t" + str(q_dish_washing_soap) + "\t\t" + str(
                float(float(p_dish_washing_soap) * float(q_dish_washing_soap))))
        if q_dish_washing_liquid != 0:
            txtarea.insert(END, "\n" + "dish washing liquid" + "\t\t" + str(q_dish_washing_liquid) + "\t\t" + str(
                float(float(p_dish_washing_liquid) * float(q_dish_washing_liquid))))
        if q_washing_powder != 0:
            txtarea.insert(END, "\n" + "washing powder" + "\t\t" + str(q_washing_powder) + "\t\t" + str(
                float(float(p_washing_powder) * float(q_washing_powder))))
        if q_washing_soaps != 0:
            txtarea.insert(END, "\n" + "washing soap" + "\t\t" + str(q_washing_soaps) + "\t\t" + str(
                float(float(p_washing_soaps) * float(q_washing_soaps))))
        if q_bleaching_powder != 0:
            txtarea.insert(END, "\n" + "bleaching powder" + "\t\t" + str(q_bleaching_powder) + "\t\t" + str(
                float(float(p_bleaching_powder) * float(q_bleaching_powder))))
        if q_sanitary_pad != 0:
            txtarea.insert(END, "\n" + "sanitary pad" + "\t\t" + str(q_sanitary_pad) + "\t\t" + str(
                float(float(p_sanitary_pad) * float(q_sanitary_pad))))
        if q_toilet_paper != 0:
            txtarea.insert(END, "\n" + "toilet paper" + "\t\t" + str(q_toilet_paper) + "\t\t" + str(
                float(float(p_toilet_paper) * float(q_toilet_paper))))
        if q_garbage_bag != 0:
            txtarea.insert(END, "\n" + "garbage bag" + "\t\t" + str(q_garbage_bag) + "\t\t" + str(
                float(float(p_garbagp_bag) * float(q_garbage_bag))))
        if q_dettol != 0:
            txtarea.insert(END, "\n" + "dettol" + "\t\t" + str(q_dettol) + "\t\t" + str(
                float(float(p_dettol) * float(q_dettol))))
        if q_mosquito_liquid != 0:
            txtarea.insert(END, "\n" + "mosquito liquid" + "\t\t" + str(q_mosquito_liquid) + "\t\t" + str(
                float(float(p_mosquito_liquid) * float(q_mosquito_liquid))))

        if q_bandages != 0:
            txtarea.insert(END, "\n" + "bandages" + "\t\t" + str(q_bandages) + "\t\t" + str(
                float(float(p_bandages) * float(q_bandages))))
        if q_light_bulbs != 0:
            txtarea.insert(END, "\n" + "light bulb" + "\t\t" + str(q_light_bulbs) + "\t\t" + str(
                float(float(p_light_bulbs) * float(q_light_bulbs))))
        if q_batteries != 0:
            txtarea.insert(END, "\n" + "batteries" + "\t\t" + str(q_batteries) + "\t\t" + str(
                float(float(p_batteries) * float(q_batteries))))
        if q_candles != 0:
            txtarea.insert(END, "\n" + "candles" + "\t\t" + str(q_candles) + "\t\t" + str(
                float(float(p_candles) * float(q_candles))))

        if q_papad != 0:
            txtarea.insert(END, "\n" + "papad" + "\t\t" + str(q_papad) + "\t\t" + str(
                float(float(p_papad) * float(q_papad))))
        if q_horlicks != 0:
            txtarea.insert(END, "\n" + "horlicks" + "\t\t" + str(q_horlicks) + "\t\t" + str(
                float(float(p_horlicks) * float(q_horlicks))))
        if q_complan != 0:
            txtarea.insert(END, "\n" + "complan" + "\t\t" + str(q_complan) + "\t\t" + str(
                float(float(p_complan) * float(q_complan))))
        if q_noodles != 0:
            txtarea.insert(END, "\n" + "noodles" + "\t\t" + str(q_noodles) + "\t\t" + str(
                float(float(p_noodles) * float(q_noodles))))
        if q_pasta != 0:
            txtarea.insert(END, "\n" + "pasta" + "\t\t" + str(q_pasta) + "\t\t" + str(
                float(float(p_pasta) * float(q_pasta))))
        if q_ketchup != 0:
            txtarea.insert(END, "\n" + "ketchup" + "\t\t" + str(q_ketchup) + "\t\t" + str(
                float(float(p_ketchup) * float(q_ketchup))))
        if q_jam != 0:
            txtarea.insert(END, "\n" + "jam" + "\t\t" + str(q_jam) + "\t\t" + str(float(float(p_jam) * float(q_jam))))
        if q_bread_delux != 0:
            txtarea.insert(END, "\n" + "delux bread" + "\t\t" + str(q_bread_delux) + "\t\t" + str(
                float(float(p_bread_delux) * float(q_bread_delux))))
        if q_bread_britania != 0:
            txtarea.insert(END, "\n" + "britania bread" + "\t\t" + str(q_bread_britania) + "\t\t" + str(
                float(float(p_bread_britania) * float(q_bread_britania))))

        if total_entry.get() != "" and total_entry.get() != "Rs 0.0":
            txtarea.insert(END, "\n" + "========================================")
            ftotal = total_entry.get()
            txtarea.insert(END, "TOTAL PRICE : " + ftotal)

    test = Label(bill_frame, font=("times new roman", 15, "bold"), fg="#51361a", bd=7, relief=GROOVE, bg="#b4a284",
                 text="Bill Area").pack(fill=X)
    scrol_y = Scrollbar(bill_frame, orient=VERTICAL)
    txtarea = Text(bill_frame, yscrollcommand=scrol_y.set)
    scrol_y.pack(side=RIGHT, fill=BOTH)
    scrol_y.config(command=txtarea.yview)
    txtarea.pack(fill=BOTH)

    def exit_f():
        root1.destroy()

    global generate_bill
    generate_bill = Button(option_frame, text="generate bill", command=bill_area, width=23,
                           font=("Goudy old style", 15, "bold"), fg="#51361a", bg="#b4a284", relief=GROOVE, bd=9)
    generate_bill.grid(row=2, column=0)

    total_label = Label(option_frame, text="Your total is", font=("Goudy old style", 15, "bold"), fg="#51361a",
                        bg="#f6ead4")
    total_label.place(x=10, y=5, height=20, width=100)

    total_label1 = Label(option_frame, text=" ", font=("Goudy old style", 15, "bold"), bg="#f6ead4")
    total_label1.grid(row=0, column=0)

    total_entry = Entry(option_frame, relief=SUNKEN, bd=4)
    total_entry.place(x=145, y=5, height=20, width=100)

    total_btn = Button(option_frame, text="total", width=23, command=total, font=("Goudy old style", 15, "bold"),
                       fg="#51361a", bg="#b4a284", relief=GROOVE, bd=9)
    total_btn.grid(row=1, column=0)

    def save():
        is_save = messagebox.askyesno("save bill", "Do you want to save the bill?")
        # lab = Label(option_frame, text=is_save)
        # lab.grid(row=7, column=0, pady=10)
        if customer_entry.get() == "":
            messagebox.showerror("Enter name", "Please enter a name")
        else:
            if is_save == 1:
                bill_data = txtarea.get('1.0', END)
                f1 = open("bills/" + str(r_bill) + " " + str(customer_entry.get()) + ".txt", "w")
                f1.write(bill_data)
                f1.close()
                messagebox.showinfo("saved", f"bill no :{r_bill} for {customer_entry.get()} have been saved")
            else:
                return

    def send():
        ph_number = number_entry.get()
        messages = txtarea.get("1.0", "end-1c")

        if ph_number == "":
            messagebox.showerror("Error", 'Please fill the phone number')
        elif messages == "":
            messagebox.showerror("Error", 'Bill Details is empty')
        else:
            url = "https://www.fast2sms.com/dev/bulk"
            api = "hmcL61TyBxlzPHVODj7etCuwf0QMY2o3FEi5agIAWqJ8bZKNn47kfBIclvSjxhnDY0iVpyMmbw3XdqOo"  # go to fast2sms.com signup to get the free api and put it into here in api variable
            querystring = {"authorization": api, "sender_id": "FSTSMS", "message": messages, "language": "english",
                           "route": "p", "numbers": ph_number}

            headers = {
                'cache-control': "no-cache"
            }
            requests.request("GET", url, headers=headers, params=querystring)

            messagebox.showinfo("Send SMS", 'Bill has been send to your successfully')

    reset_btn = Button(option_frame, text="clear", command=clearr, width=23, font=("Goudy old style", 15, "bold"),
                       fg="#51361a", bg="#b4a284", relief=GROOVE, bd=9)
    reset_btn.grid(row=3, column=0)

    save_btn = Button(option_frame, text="SAVE", command=save, width=23, font=("Goudy old style", 15, "bold"),
                      fg="#51361a", bg="#b4a284", relief=GROOVE, bd=9)
    save_btn.grid(row=4, column=0)

    exit_btn = Button(option_frame, text="back", command=exit_f, width=23, font=("Goudy old style", 15, "bold"),
                      fg="#51361a", bg="#b4a284", relief=GROOVE, bd=9)
    exit_btn.grid(row=6, column=0)

    send_btn = Button(option_frame, text="send", command=send, width=23, font=("Goudy old style", 15, "bold"),
                      fg="#51361a", bg="#b4a284", relief=GROOVE, bd=9)
    send_btn.grid(row=5, column=0)

    bill_area()
    rice_flour = Button(frame1, text="RICE AND FLOURS", width=20, command=rice, font=("times new roaman", 8, "bold"),
                        fg="#51361a", bg="#b4a284", relief=GROOVE, bd=9)
    rice_flour.grid(row=0, column=0, padx=18)

    pulses_dal = Button(frame1, text="PULSES/DAL", width=20, command=pulses, font=("times new roaman", 8, "bold"),
                        fg="#51361a", bg="#b4a284", relief=GROOVE, bd=9)

    pulses_dal.grid(row=1, column=0)
    spice = Button(frame1, text="SPICE POWDER", width=20, command=spices, font=("times new roaman", 8, "bold"),
                   fg="#51361a", bg="#b4a284", relief=GROOVE, bd=9)
    spice.grid(row=2, column=0)
    oils = Button(frame1, text="OILS", width=23, command=oil, font=("times new roaman", 7, "bold"), fg="#51361a",
                  bg="#b4a284", relief=GROOVE, bd=9)
    oils.grid(row=3, column=0)
    spice_nuts = Button(frame1, text="SPICES AND NUTS", width=20, command=spice_nut,
                        font=("times new roaman", 8, "bold"), fg="#51361a", bg="#b4a284", relief=GROOVE, bd=9)
    spice_nuts.grid(row=4, column=0)
    dairy = Button(frame1, text="DAIRY PRODUCTS", width=20, command=dairy, font=("times new roaman", 8, "bold"),
                   fg="#51361a", bg="#b4a284", relief=GROOVE, bd=9)
    dairy.grid(row=5, column=0)
    toiletries = Button(frame1, text="TOILETRIES", width=20, command=toiletrie, font=("times new roaman", 8, "bold"),
                        fg="#51361a", bg="#b4a284", relief=GROOVE, bd=9)
    toiletries.grid(row=6, column=0)
    cleaning = Button(frame1, text="CLEANING PRODUCTS", width=20, command=clean, font=("times new roaman", 8, "bold"),
                      fg="#51361a", bg="#b4a284", relief=GROOVE, bd=9)
    cleaning.grid(row=7, column=0)
    miscellaneous = Button(frame1, text="MISCELLANEOUS", width=20, command=miss, font=("times new roaman", 8, "bold"),
                           fg="#51361a", bg="#b4a284", relief=GROOVE, bd=9)
    miscellaneous.grid(row=8, column=0)
    other = Button(frame1, text="OTHER INGREDIENTS", width=23, command=others, font=("times new roaman", 7, "bold"),
                   fg="#51361a", bg="#b4a284", relief=GROOVE, bd=9)
    other.grid(row=9, column=0)

    root1.mainloop()
