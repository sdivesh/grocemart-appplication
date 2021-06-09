from tkinter import *
from tkinter import messagebox
import sqlite3
from PIL import ImageTk, Image


def admin():
    root1 = Tk()
    root1.title("GROCEMART")
    root1.geometry("1199x600+35+52")
    root1.resizable(False, False)
    back_img1 = ImageTk.PhotoImage(file="neww.jpg")
    frame1 = Frame(root1, bg="#f6ead4", bd=12, relief=GROOVE)
    frame1.place(x=0, y=120, height=490, width=1200)

    bill_title = Label(root1, bg="#f6ead4", font=("times new roman", 60, "bold"), relief=GROOVE, bd=12, fg="#51361a",
                       text="GROCEMART").pack(fill=X)

    def exit_f():
        root1.destroy()

    exit_btn = Button(root1, text="back", command=exit_f, width=23, font=("Goudy old style", 15, "bold"),
                      fg="#51361a", bg="#b4a284", relief=GROOVE, bd=9)
    exit_btn.place(x=1030, y=30, height=60, width=90)

    try:
        con = sqlite3.connect('price.db')

        c1 = con.cursor()

        c1.execute(""" CREATE TABLE d_rice(
            id primary key,
            v_turmeric_powder real,
            v_sugar real,
            v_jaggery real,
            v_old_rice real,
            v_new_rice real,
            v_sona_masoori real,
            v_basmati real,
            v_wheat_flour real,
            v_maida real,
            v_multi_grain real,
            v_rice1_flour real,
            v_besan_flour real,
            v_rava real,
            v_rice1_rava real,
            v_corn_flour real,
            v_vermicelli real,
            v_tamarind real,
            v_red_chilli real)""")

        con.commit()

        con.close()
    except:
        pass

    try:
        con = sqlite3.connect('price.db')

        c1 = con.cursor()

        c1.execute(""" CREATE TABLE d_pulses(
            id primary key,
            v_toor_dal real,
            v_urad_dal real,
            v_moong_dal real,
            v_chana_dal real,
            v_rajma real,
            v_white1_chana real)""")

        con.commit()

        con.close()
    except:
        pass

    try:
        con = sqlite3.connect('price.db')

        c1 = con.cursor()

        c1.execute(""" CREATE TABLE d_spice_powder(
            id primary key,
             v_crystal_salt real,
             v_powder_salt real,
             v_redchilli_powder real,
             v_dhania_powder real,
             v_garammasala_powder real,
             v_chatmasala_powder real,
             v_pepper_powder real,
             v_sambar_powder real,
             v_biryani_powder real,
             v_coffee1_powder real,
             v_tea_powder real)""")

        con.commit()

        con.close()
    except:
        pass

    try:
        con = sqlite3.connect('price.db')

        c1 = con.cursor()

        c1.execute(""" CREATE TABLE d_oils(
            id primary key,
            v_cooking_oil real,
             v_seasame1_oil real,
             v_coconut_oil real,
             v_ghee real,
             v_olive1_oil real)""")

        con.commit()

        con.close()
    except:
        pass

    try:
        con = sqlite3.connect('price.db')

        c1 = con.cursor()

        c1.execute(""" CREATE TABLE d_spices_nuts(
            id primary key,
            v_mustard_seed real,
             v_pepper real,
             v_jeera real,
             v_khus_khus real,
             v_dhania real,
             v_black_seasame1_seeds real,
             v_white1_seasame1_seeds real,
             v_cashew_nuts real,
             v_raisins real,
             v_badam real,
             v_peanuts real,
             v_dates real)""")

        con.commit()

        con.close()
    except:
        pass

    try:
        con = sqlite3.connect('price.db')

        c1 = con.cursor()

        c1.execute(""" CREATE TABLE d_dairy(
            id primary key,
            v_cheese1_block real,
             v_butter real,
             v_yoghurt real,
             v_fresh_cream real,
             v_paneer real)""")

        con.commit()

        con.close()
    except:
        pass

    try:
        con = sqlite3.connect('price.db')

        c1 = con.cursor()

        c1.execute(""" CREATE TABLE d_toiletries(
            id primary key,
             v_tooth_paste real,
             v_tooth_brush real,
             v_bathing_soap real,
             v_shampoo real,
             v_face1_powder real,
             v_hand_sanitizer real,
             v_deodarant real,
             v_shaving_cream real,
             v_hair_gel real,
             v_razer_blade real)""")

        con.commit()

        con.close()
    except:
        pass

    try:
        con = sqlite3.connect('price.db')

        c1 = con.cursor()

        c1.execute(""" CREATE TABLE d_clean(
            id primary key,
             v_dish_washing_soap real,
             v_dish_washing_liquid real,
             v_washing_powder real,
             v_washing_soaps real,
             v_bleaching_powder real,
             v_sanitary_pad real,
             v_toilet_paper real,
             v_garbage1_bag real,
             v_dettol real,
             v_mosquito_liquid real)""")

        con.commit()

        con.close()
    except:
        pass

    try:
        con = sqlite3.connect('price.db')

        c1 = con.cursor()

        c1.execute(""" CREATE TABLE d_mis(
            id primary key,
             v_bandages real,
             v_light_bulbs real,
             v_batteries real,
             v_candles real)""")

        con.commit()

        con.close()
    except:
        pass

    try:
        con = sqlite3.connect('price.db')

        c1 = con.cursor()

        c1.execute(""" CREATE TABLE d_others(
            id primary key,
             v_papad real,
             v_horlicks real,
             v_complan real,
             v_noodles real,
             v_pasta real,
             v_ketchup real,
             v_jam real,
             v_bread_delux real,
             v_bread_britania real)""")

        con.commit()

        con.close()
    except:
        pass

    try:
        con = sqlite3.connect('price.db')

        c1 = con.cursor()

        c1.execute(""" CREATE TABLE d3_rice(
            id primary key,
            v3_turmeric_powder real,
            v3_sugar real,
            v3_jaggery real,
            v3_old3_rice real,
            v3_new_rice real,
            v3_sona_masoori real,
            v3_basmati real,
            v3_wheat_flour real,
            v3_maida real,
            v3_multi_grain real,
            v3_rice3_flour real,
            v3_besan_flour real,
            v3_rava real,
            v3_rice3_rava real,
            v3_corn_flour real,
            v3_vermicelli real,
            v3_tamarind real,
            v3_red3_chilli real)""")

        c1.execute(""" CREATE TABLE d3_pulses(
            id primary key,
            v3_toor_dal real,
            v3_urad3_dal real,
            v3_moong_dal real,
            v3_chana_dal real,
            v3_rajma real,
            v3_white3_chana real)""")

        c1.execute(""" CREATE TABLE d3_spice_powder(
            id primary key,
             v3_crystal_salt real,
             v3_powder_salt real,
             v3_redchilli_powder real,
             v3_dhania_powder real,
             v3_garammasala_powder real,
             v3_chatmasala_powder real,
             v3_pepper_powder real,
             v3_sambar_powder real,
             v3_biryani_powder real,
             v3_coffee3_powder real,
             v3_tea_powder real)""")

        c1.execute(""" CREATE TABLE d3_oils(
            id primary key,
            v3_cooking_oil real,
             v3_seasame3_oil real,
             v3_coconut_oil real,
             v3_ghee real,
             v3_olive3_oil real)""")

        c1.execute(""" CREATE TABLE d3_spices_nuts(
            id primary key,
            v3_mustard3_seed real,
             v3_pepper real,
             v3_jeera real,
             v3_khus_khus real,
             v3_dhania real,
             v3_black_seasame3_seeds real,
             v3_white3_seasame3_seeds real,
             v3_cashew_nuts real,
             v3_raisins real,
             v3_badam real,
             v3_peanuts real,
             v3_dates real)""")

        c1.execute(""" CREATE TABLE d3_dairy(
            id primary key,
            v3_cheese3_block real,
             v3_butter real,
             v3_yoghurt real,
             v3_fresh_cream real,
             v3_paneer real)""")

        c1.execute(""" CREATE TABLE d3_toiletries(
            id primary key,
             v3_tooth_paste real,
             v3_tooth_brush real,
             v3_bathing_soap real,
             v3_shampoo real,
             v3_face3_powder real,
             v3_hand3_sanitizer real,
             v3_deodarant real,
             v3_shaving_cream real,
             v3_hair_gel real,
             v3_razer_blade real)""")

        c1.execute(""" CREATE TABLE d3_clean(
            id primary key,
             v3_dish_washing_soap real,
             v3_dish_washing_liquid real,
             v3_washing_powder real,
             v3_washing_soaps real,
             v3_bleaching_powder real,
             v3_sanitary_pad real,
             v3_toilet_paper real,
             v3_garbage3_bag real,
             v3_dettol real,
             v3_mosquito_liquid real)""")

        c1.execute(""" CREATE TABLE d3_mis(
            id primary key,
             v3_bandages real,
             v3_light_bulbs real,
             v3_batteries real,
             v3_candles real)""")

        c1.execute(""" CREATE TABLE d3_others(
            id primary key,
             v3_papad real,
             v3_horlicks real,
             v3_complan real,
             v3_noodles real,
             v3_pasta real,
             v3_ketchup real,
             v3_jam real,
             v3_bread3_delux real,
             v3_bread3_britania real)""")

        con.commit()

        con.close()
    except:
        pass

    def cal1():
        global v_turmeric_powder
        global v_sugar
        global v_jaggery
        global v_old_rice
        global v_new_rice
        global v_sona_masoori
        global v_basmati
        global v_wheat_flour
        global v_maida
        global v_multi_grain
        global v_rice1_flour
        global v_besan_flour
        global v_rava
        global v_rice1_rava
        global v_corn_flour
        global v_vermicelli
        global v_tamarind
        global v_red_chilli
        required_number = 0
        valid_number = 0

        global v3_turmeric_powder
        global v3_sugar
        global v3_jaggery
        global v3_old3_rice
        global v3_new_rice
        global v3_sona_masoori
        global v3_basmati
        global v3_wheat_flour
        global v3_maida
        global v3_multi_grain
        global v3_rice3_flour
        global v3_besan_flour
        global v3_rava
        global v3_rice3_rava
        global v3_corn_flour
        global v3_vermicelli
        global v3_tamarind
        global v3_red3_chilli
        required3_number = 0
        valid3_number = 0

        if e1_turmeric_powder.get() == "" or e1_turmeric_powder.get() == 0:
            required_number = 1
        else:
            try:
                v_turmeric_powder = float(e1_turmeric_powder.get())
            except:
                valid_number = 1

        if e1_sugar.get() == "" or e1_sugar.get() == 0:
            required_number = 1
        else:
            try:
                v_sugar = float(e1_sugar.get())
            except:
                valid_number = 1

        if e1_jaggery.get() == "" or e1_jaggery.get() == 0:
            required_number = 1
        else:
            try:
                v_jaggery = float(e1_jaggery.get())
            except:
                valid_number = 1

        if e1_old_rice.get() == "" or e1_old_rice.get() == 0:
            required_number = 1
        else:
            try:
                v_old_rice = float(e1_old_rice.get())
            except:
                valid_number = 1

        if e1_new_rice.get() == "" or e1_new_rice.get() == 0:
            required_number = 1
        else:
            try:
                v_new_rice = float(e1_new_rice.get())
            except:
                valid_number = 1

        if e1_sona_masoori.get() == "" or e1_sona_masoori.get() == 0:
            required_number = 1
        else:
            try:
                v_sona_masoori = float(e1_sona_masoori.get())
            except:
                valid_number = 1

        if e1_basmati.get() == "" or e1_basmati.get() == 0:
            required_number = 1
        else:
            try:
                v_basmati = float(e1_basmati.get())
            except:
                valid_number = 1

        if e1_wheat_flour.get() == "" or e1_wheat_flour.get() == 0:
            required_number = 1
        else:
            try:
                v_wheat_flour = float(e1_wheat_flour.get())
            except:
                valid_number = 1

        if e1_maida.get() == "" or e1_maida.get() == 0:
            required_number = 1
        else:
            try:
                v_maida = float(e1_maida.get())
            except:
                valid_number = 1

        if e1_multi_grain.get() == "" or e1_multi_grain.get() == 0:
            required_number = 1
        else:
            try:
                v_multi_grain = float(e1_multi_grain.get())
            except:
                valid_number = 1

        if e1_rice1_flour.get() == "" or e1_rice1_flour.get() == 0:
            required_number = 1
        else:
            try:
                v_rice1_flour = float(e1_rice1_flour.get())
            except:
                valid_number = 1

        if e1_besan_flour.get() == "" or e1_besan_flour.get() == 0:
            required_number = 1
        else:
            try:
                v_besan_flour = float(e1_besan_flour.get())
            except:
                valid_number = 1

        if e1_rava.get() == "" or e1_rava.get() == 0:
            required_number = 1
        else:
            try:
                v_rava = float(e1_rava.get())
            except:
                valid_number = 1

        if e1_rice1_rava.get() == "" or e1_rice1_rava.get() == 0:
            required_number = 1
        else:
            try:
                v_rice1_rava = float(e1_rice1_rava.get())
            except:
                valid_number = 1

        if e1_corn_flour.get() == "" or e1_corn_flour.get() == 0:
            required_number = 1
        else:
            try:
                v_corn_flour = float(e1_corn_flour.get())
            except:
                valid_number = 1

        if e1_vermicelli.get() == "" or e1_vermicelli.get() == 0:
            required_number = 1
        else:
            try:
                v_vermicelli = float(e1_vermicelli.get())
            except:
                valid_number = 1

        if e1_tamarind.get() == "" or e1_tamarind.get() == 0:
            required_number = 1
        else:
            try:
                v_tamarind = float(e1_tamarind.get())
            except:
                valid_number = 1

        if e1_red_chilli.get() == "" or e1_red_chilli.get() == 0:
            required_number = 1
        else:
            try:
                v_red_chilli = float(e1_red_chilli.get())
            except:
                valid_number = 1

        if required_number == 1:
            messagebox.showerror("REQUIRED FIELD", "ALL FIELDS ARE REQUIRED", parent=innerframe1)
        if valid_number == 1:
            messagebox.showerror("NUMBER", "PLEASE ENTER A VALID NUMBER", parent=innerframe1)

        if e3_turmeric_powder.get() == "":
            e3_turmeric_powder.insert(0, "0")
        if e3_sugar.get() == "":
            e3_sugar.insert(0, "0")
        if e3_jaggery.get() == "":
            e3_jaggery.insert(0, "0")
        if e3_old3_rice.get() == "":
            e3_old3_rice.insert(0, "0")
        if e3_new_rice.get() == "":
            e3_new_rice.insert(0, "0")
        if e3_sona_masoori.get() == "":
            e3_sona_masoori.insert(0, "0")
        if e3_basmati.get() == "":
            e3_basmati.insert(0, "0")
        if e3_wheat_flour.get() == "":
            e3_wheat_flour.insert(0, "0")
        if e3_maida.get() == "":
            e3_maida.insert(0, "0")
        if e3_multi_grain.get() == "":
            e3_multi_grain.insert(0, "0")
        if e3_multi_grain.get() == "":
            e3_multi_grain.insert(0, "0")
        if e3_rice3_flour.get() == "":
            e3_rice3_flour.insert(0, "0")
        if e3_besan_flour.get() == "":
            e3_besan_flour.insert(0, "0")
        if e3_rava.get() == "":
            e3_rava.insert(0, "0")
        if e3_rice3_rava.get() == "":
            e3_rice3_rava.insert(0, "0")
        if e3_corn_flour.get() == "":
            e3_corn_flour.insert(0, "0")
        if e3_vermicelli.get() == "":
            e3_vermicelli.insert(0, "0")
        if e3_tamarind.get() == "":
            e3_tamarind.insert(0, "0")
        if e3_red3_chilli.get() == "":
            e3_red3_chilli.insert(0, "0")

        if e3_turmeric_powder.get() == "":
            pass
        else:
            try:
                v3_turmeric_powder = float(e3_turmeric_powder.get())
            except:
                valid3_number = 1

        if e3_sugar.get() == "":
            pass
        else:
            try:
                v3_sugar = float(e3_sugar.get())
            except:
                valid3_number = 1

        if e3_jaggery.get() == "":
            pass
        else:
            try:
                v3_jaggery = float(e3_jaggery.get())
            except:
                valid3_number = 1

        if e3_old3_rice.get() == "":
            pass
        else:
            try:
                v3_old3_rice = float(e3_old3_rice.get())
            except:
                valid3_number = 1

        if e3_new_rice.get() == "":
            pass
        else:
            try:
                v3_new_rice = float(e3_new_rice.get())
            except:
                valid3_number = 1

        if e3_sona_masoori.get() == "":
            pass
        else:
            try:
                v3_sona_masoori = float(e3_sona_masoori.get())
            except:
                valid3_number = 1

        if e3_basmati.get() == "":
            pass
        else:
            try:
                v3_basmati = float(e3_basmati.get())
            except:
                valid3_number = 1

        if e3_wheat_flour.get() == "":
            pass
        else:
            try:
                v3_wheat_flour = float(e3_wheat_flour.get())
            except:
                valid3_number = 1

        if e3_maida.get() == "":
            pass
        else:
            try:
                v3_maida = float(e3_maida.get())
            except:
                valid3_number = 1

        if e3_multi_grain.get() == "":
            pass
        else:
            try:
                v3_multi_grain = float(e3_multi_grain.get())
            except:
                valid3_number = 1

        if e3_rice3_flour.get() == "":
            pass
        else:
            try:
                v3_rice3_flour = float(e3_rice3_flour.get())
            except:
                valid3_number = 1

        if e3_besan_flour.get() == "":
            pass
        else:
            try:
                v3_besan_flour = float(e3_besan_flour.get())
            except:
                valid3_number = 1

        if e3_rava.get() == "":
            pass
        else:
            try:
                v3_rava = float(e3_rava.get())
            except:
                valid3_number = 1

        if e3_rice3_rava.get() == "":
            pass
        else:
            try:
                v3_rice3_rava = float(e3_rice3_rava.get())
            except:
                valid3_number = 1

        if e3_corn_flour.get() == "":
            pass
        else:
            try:
                v3_corn_flour = float(e3_corn_flour.get())
            except:
                valid3_number = 1

        if e3_vermicelli.get() == "":
            pass
        else:
            try:
                v3_vermicelli = float(e3_vermicelli.get())
            except:
                valid3_number = 1

        if e3_tamarind.get() == "":
            pass
        else:
            try:
                v3_tamarind = float(e3_tamarind.get())
            except:
                valid3_number = 1

        if e3_red3_chilli.get() == "":
            pass
        else:
            try:
                v3_red3_chilli = float(e3_red3_chilli.get())
            except:
                valid3_number = 1

        if valid3_number == 1:
            messagebox.showerror("NUMBER", "PLEASE ENTER A VALID NUMBER", parent=innerframe1)

        con = sqlite3.connect('price.db')

        c1 = con.cursor()
        id = 1
        c1.execute(
            "INSERT OR REPLACE into d3_rice VALUES (:id,:a, :b, :c, :d, :e, :f, :g, :h, :i,:j, :k, :l, :m, :n, :o, :p, :q, :r)",
            {'id': id,
             'a': float(v3_turmeric_powder),
             'b': float(v3_sugar),
             'c': float(v3_jaggery),
             'd': float(v3_old3_rice),
             'e': float(v3_new_rice),
             'f': float(v3_sona_masoori),
             'g': float(v3_basmati),
             'h': float(v3_wheat_flour),
             'i': float(v3_maida),
             'j': float(v3_multi_grain),
             'k': float(v3_rice3_flour),
             'l': float(v3_besan_flour),
             'm': float(v3_rava),
             'n': float(v3_rice3_rava),
             'o': float(v3_corn_flour),
             'p': float(v3_vermicelli),
             'q': float(v3_tamarind),
             'r': float(v3_red3_chilli)
             })

        con.commit()

        con.close()

        con = sqlite3.connect('price.db')

        c1 = con.cursor()
        id = 1
        c1.execute(
            "INSERT OR REPLACE into d_rice VALUES (:id,:a, :b, :c, :d, :e, :f, :g, :h, :i,:j, :k, :l, :m, :n, :o, :p, :q, :r)",
            {'id': id,
             'a': float(v_turmeric_powder),
             'b': float(v_sugar),
             'c': float(v_jaggery),
             'd': float(v_old_rice),
             'e': float(v_new_rice),
             'f': float(v_sona_masoori),
             'g': float(v_basmati),
             'h': float(v_wheat_flour),
             'i': float(v_maida),
             'j': float(v_multi_grain),
             'k': float(v_rice1_flour),
             'l': float(v_besan_flour),
             'm': float(v_rava),
             'n': float(v_rice1_rava),
             'o': float(v_corn_flour),
             'p': float(v_vermicelli),
             'q': float(v_tamarind),
             'r': float(v_red_chilli)
             })

        con.commit()

        con.close()
        innerframe1.destroy()

    def rice():
        global innerframe1
        global e1_turmeric_powder
        global e1_sugar
        global e1_jaggery
        global e1_old_rice
        global e1_new_rice
        global e1_sona_masoori
        global e1_basmati
        global e1_wheat_flour
        global e1_maida
        global e1_multi_grain
        global e1_rice1_flour
        global e1_besan_flour
        global e1_rava
        global e1_rice1_rava
        global e1_corn_flour
        global e1_vermicelli
        global e1_tamarind
        global e1_red_chilli

        global e3_turmeric_powder
        global e3_sugar
        global e3_jaggery
        global e3_old3_rice
        global e3_new_rice
        global e3_sona_masoori
        global e3_basmati
        global e3_wheat_flour
        global e3_maida
        global e3_multi_grain
        global e3_rice3_flour
        global e3_besan_flour
        global e3_rava
        global e3_rice3_rava
        global e3_corn_flour
        global e3_vermicelli
        global e3_tamarind
        global e3_red3_chilli

        innerframe1 = Toplevel(bg="#f6ead4", relief=GROOVE, bd=9)
        # innerframe1.geometry("500x200+200+100")
        innerframe1.title("RICE AND FLOURS")
        turmeric_powder = Label(innerframe1, text="TURMERIC POWDER ", font=("times new roman", 15, "bold"),
                                fg="#51361a",
                                bg="#f6ead4")
        turmeric_powder.grid(row=0, column=0)
        sugar = Label(innerframe1, text="SUGAR ", font=("times new roman", 15, "bold"), fg="#51361a",
                      bg="#f6ead4")
        sugar.grid(row=1, column=0)
        jaggery = Label(innerframe1, text="JAGGERY ", font=("times new roman", 15, "bold"), fg="#51361a",
                        bg="#f6ead4")
        jaggery.grid(row=2, column=0)
        old_rice = Label(innerframe1, text="OLD RICE ( in kg) ", font=("times new roman", 15, "bold"), fg="#51361a",
                         bg="#f6ead4")
        old_rice.grid(row=3, column=0)
        new_rice = Label(innerframe1, text="NEW RICE ( in kg ) ", font=("times new roman", 15, "bold"), fg="#51361a",
                         bg="#f6ead4")
        new_rice.grid(row=4, column=0)
        sona_masoori = Label(innerframe1, text="SONA MASOORI", font=("times new roman", 15, "bold"), fg="#51361a",
                             bg="#f6ead4")
        sona_masoori.grid(row=5, column=0)
        basmati = Label(innerframe1, text="BASMATI RICE", font=("times new roman", 15, "bold"), fg="#51361a",
                        bg="#f6ead4")
        basmati.grid(row=6, column=0)
        wheat_flour = Label(innerframe1, text="WHEAT FLOUR", font=("times new roman", 15, "bold"), fg="#51361a",
                            bg="#f6ead4")
        wheat_flour.grid(row=7, column=0)
        maida = Label(innerframe1, text="MAIDA", font=("times new roman", 15, "bold"), fg="#51361a",
                      bg="#f6ead4")
        maida.grid(row=8, column=0)
        multi_grain = Label(innerframe1, text="MULTI GRAINS", font=("times new roman", 15, "bold"), fg="#51361a",
                            bg="#f6ead4")
        multi_grain.grid(row=9, column=0)
        rice1_flour = Label(innerframe1, text="RICE FLOUR", font=("times new roman", 15, "bold"), fg="#51361a",
                            bg="#f6ead4")
        rice1_flour.grid(row=10, column=0)
        besan_flour = Label(innerframe1, text="BESAN FLOUR", font=("times new roman", 15, "bold"), fg="#51361a",
                            bg="#f6ead4")
        besan_flour.grid(row=11, column=0)
        rava = Label(innerframe1, text="RAVA", font=("times new roman", 15, "bold"), fg="#51361a",
                     bg="#f6ead4")
        rava.grid(row=12, column=0)
        rice1_rava = Label(innerframe1, text="RICE RAVA", font=("times new roman", 15, "bold"), fg="#51361a",
                           bg="#f6ead4")
        rice1_rava.grid(row=13, column=0)
        corn_flour = Label(innerframe1, text="COURN FLOUR", font=("times new roman", 15, "bold"), fg="#51361a",
                           bg="#f6ead4")
        corn_flour.grid(row=14, column=0)
        vermicelli = Label(innerframe1, text="VERMICELLI ( SEVIAYAN )", font=("times new roman", 15, "bold"),
                           fg="#51361a",
                           bg="#f6ead4")
        vermicelli.grid(row=15, column=0)
        tamarind = Label(innerframe1, text="TAMARIND", font=("times new roman", 15, "bold"), fg="#51361a",
                         bg="#f6ead4")
        tamarind.grid(row=16, column=0)
        red_chilli = Label(innerframe1, text="RED CHILLI", font=("times new roman", 15, "bold"), fg="#51361a",
                           bg="#f6ead4")
        red_chilli.grid(row=17, column=0)

        e1_turmeric_powder = Entry(innerframe1, width=25, relief=SUNKEN, bd=4)
        e1_turmeric_powder.grid(row=0, column=2)
        e1_sugar = Entry(innerframe1, width=25, relief=SUNKEN, bd=4)
        e1_sugar.grid(row=1, column=2)
        e1_jaggery = Entry(innerframe1, width=25, relief=SUNKEN, bd=4)
        e1_jaggery.grid(row=2, column=2)
        e1_old_rice = Entry(innerframe1, width=25, relief=SUNKEN, bd=4)
        e1_old_rice.grid(row=3, column=2)
        e1_new_rice = Entry(innerframe1, width=25, relief=SUNKEN, bd=4)
        e1_new_rice.grid(row=4, column=2)
        e1_sona_masoori = Entry(innerframe1, width=25, relief=SUNKEN, bd=4)
        e1_sona_masoori.grid(row=5, column=2)
        e1_basmati = Entry(innerframe1, width=25, relief=SUNKEN, bd=4)
        e1_basmati.grid(row=6, column=2)
        e1_wheat_flour = Entry(innerframe1, width=25, relief=SUNKEN, bd=4)
        e1_wheat_flour.grid(row=7, column=2)
        e1_maida = Entry(innerframe1, width=25, relief=SUNKEN, bd=4)
        e1_maida.grid(row=8, column=2)
        e1_multi_grain = Entry(innerframe1, width=25, relief=SUNKEN, bd=4)
        e1_multi_grain.grid(row=9, column=2)
        e1_rice1_flour = Entry(innerframe1, width=25, relief=SUNKEN, bd=4)
        e1_rice1_flour.grid(row=10, column=2)
        e1_besan_flour = Entry(innerframe1, width=25, relief=SUNKEN, bd=4)
        e1_besan_flour.grid(row=11, column=2)
        e1_rava = Entry(innerframe1, width=25, relief=SUNKEN, bd=4)
        e1_rava.grid(row=12, column=2)
        e1_rice1_rava = Entry(innerframe1, width=25, relief=SUNKEN, bd=4)
        e1_rice1_rava.grid(row=13, column=2)
        e1_corn_flour = Entry(innerframe1, width=25, relief=SUNKEN, bd=4)
        e1_corn_flour.grid(row=14, column=2)
        e1_vermicelli = Entry(innerframe1, width=25, relief=SUNKEN, bd=4)
        e1_vermicelli.grid(row=15, column=2)
        e1_tamarind = Entry(innerframe1, width=25, relief=SUNKEN, bd=4)
        e1_tamarind.grid(row=16, column=2)
        e1_red_chilli = Entry(innerframe1, width=25, relief=SUNKEN, bd=4)
        e1_red_chilli.grid(row=17, column=2)

        e3_turmeric_powder = Entry(innerframe1, width=25, relief=SUNKEN, bd=4)
        e3_turmeric_powder.grid(row=0, column=3)
        e3_sugar = Entry(innerframe1, width=25, relief=SUNKEN, bd=4)
        e3_sugar.grid(row=1, column=3)
        e3_jaggery = Entry(innerframe1, width=25, relief=SUNKEN, bd=4)
        e3_jaggery.grid(row=2, column=3)
        e3_old3_rice = Entry(innerframe1, width=25, relief=SUNKEN, bd=4)
        e3_old3_rice.grid(row=3, column=3)
        e3_new_rice = Entry(innerframe1, width=25, relief=SUNKEN, bd=4)
        e3_new_rice.grid(row=4, column=3)
        e3_sona_masoori = Entry(innerframe1, width=25, relief=SUNKEN, bd=4)
        e3_sona_masoori.grid(row=5, column=3)
        e3_basmati = Entry(innerframe1, width=25, relief=SUNKEN, bd=4)
        e3_basmati.grid(row=6, column=3)
        e3_wheat_flour = Entry(innerframe1, width=25, relief=SUNKEN, bd=4)
        e3_wheat_flour.grid(row=7, column=3)
        e3_maida = Entry(innerframe1, width=25, relief=SUNKEN, bd=4)
        e3_maida.grid(row=8, column=3)
        e3_multi_grain = Entry(innerframe1, width=25, relief=SUNKEN, bd=4)
        e3_multi_grain.grid(row=9, column=3)
        e3_rice3_flour = Entry(innerframe1, width=25, relief=SUNKEN, bd=4)
        e3_rice3_flour.grid(row=10, column=3)
        e3_besan_flour = Entry(innerframe1, width=25, relief=SUNKEN, bd=4)
        e3_besan_flour.grid(row=11, column=3)
        e3_rava = Entry(innerframe1, width=25, relief=SUNKEN, bd=4)
        e3_rava.grid(row=12, column=3)
        e3_rice3_rava = Entry(innerframe1, width=25, relief=SUNKEN, bd=4)
        e3_rice3_rava.grid(row=13, column=3)
        e3_corn_flour = Entry(innerframe1, width=25, relief=SUNKEN, bd=4)
        e3_corn_flour.grid(row=14, column=3)
        e3_vermicelli = Entry(innerframe1, width=25, relief=SUNKEN, bd=4)
        e3_vermicelli.grid(row=15, column=3)
        e3_tamarind = Entry(innerframe1, width=25, relief=SUNKEN, bd=4)
        e3_tamarind.grid(row=16, column=3)
        e3_red3_chilli = Entry(innerframe1, width=25, relief=SUNKEN, bd=4)
        e3_red3_chilli.grid(row=17, column=3)

        try:
            con = sqlite3.connect('price.db')

            c1 = con.cursor()

            c1.execute("SELECT * FROM d3_rice")
            insert_rice = c1.fetchall()
            insert = insert_rice[0]
            # la = Label(innerframe1, text=insert)
            # la.grid(row=0, column=3)

            e3_turmeric_powder.insert(0, insert[1])
            e3_sugar.insert(0, insert[2])
            e3_jaggery.insert(0, insert[3])
            e3_old3_rice.insert(0, insert[4])
            e3_new_rice.insert(0, insert[5])
            e3_sona_masoori.insert(0, insert[6])
            e3_basmati.insert(0, insert[7])
            e3_wheat_flour.insert(0, insert[8])
            e3_maida.insert(0, insert[9])
            e3_multi_grain.insert(0, insert[10])
            e3_rice3_flour.insert(0, insert[11])
            e3_besan_flour.insert(0, insert[12])
            e3_rava.insert(0, insert[13])
            e3_rice3_rava.insert(0, insert[14])
            e3_corn_flour.insert(0, insert[15])
            e3_vermicelli.insert(0, insert[16])
            e3_tamarind.insert(0, insert[17])
            e3_red3_chilli.insert(0, insert[18])

            con.commit()

            con.close()
        except:
            pass

        try:
            con = sqlite3.connect('price.db')

            c1 = con.cursor()

            c1.execute("SELECT * FROM d_rice")
            insert_rice = c1.fetchall()
            insert = insert_rice[0]
            # la = Label(innerframe1, text=insert)
            # la.grid(row=0, column=3)

            e1_turmeric_powder.insert(0, insert[1])
            e1_sugar.insert(0, insert[2])
            e1_jaggery.insert(0, insert[3])
            e1_old_rice.insert(0, insert[4])
            e1_new_rice.insert(0, insert[5])
            e1_sona_masoori.insert(0, insert[6])
            e1_basmati.insert(0, insert[7])
            e1_wheat_flour.insert(0, insert[8])
            e1_maida.insert(0, insert[9])
            e1_multi_grain.insert(0, insert[10])
            e1_rice1_flour.insert(0, insert[11])
            e1_besan_flour.insert(0, insert[12])
            e1_rava.insert(0, insert[13])
            e1_rice1_rava.insert(0, insert[14])
            e1_corn_flour.insert(0, insert[15])
            e1_vermicelli.insert(0, insert[16])
            e1_tamarind.insert(0, insert[17])
            e1_red_chilli.insert(0, insert[18])

            con.commit()

            con.close()
        except:
            pass

        total = Button(innerframe1, text="OK", command=cal1, width=20, font=("times new roaman", 20, "bold"),
                       fg="#51361a", bg="#b4a284", relief=GROOVE, bd=9)
        total.grid(row=18, column=0, columnspan=3, pady=15)

    def cal2():
        global v_toor_dal
        global v_urad_dal
        global v_moong_dal
        global v_chana_dal
        global v_rajma
        global v_white1_chana
        v_toor_dal = 0
        v_urad_dal = 0
        v_moong_dal = 0
        v_chana_dal = 0
        v_rajma = 0
        v_white1_chana = 0
        required_number = 0
        valid_number = 0

        global v3_toor_dal
        global v3_urad3_dal
        global v3_moong_dal
        global v3_chana_dal
        global v3_rajma
        global v3_white3_chana
        v3_toor_dal = 0
        v3_urad3_dal = 0
        v3_moong_dal = 0
        v3_chana_dal = 0
        v3_rajma = 0
        v3_white3_chana = 0
        required3_number = 0
        valid3_number = 0

        if e1_toor_dal.get() == "" or e1_toor_dal.get() == 0:
            required_number = 1
        else:
            try:
                v_toor_dal = float(e1_toor_dal.get())
            except:
                valid_number = 1

        if e1_urad_dal.get() == "" or e1_urad_dal.get() == 0:
            required_number = 1
        else:
            try:
                v_urad_dal = float(e1_urad_dal.get())
            except:
                valid_number = 1

        if e1_moong_dal.get() == "" or e1_moong_dal.get() == 0:
            required_number = 1
        else:
            try:
                v_moong_dal = float(e1_moong_dal.get())
            except:
                valid_number = 1

        if e1_chana_dal.get() == "" or e1_chana_dal.get() == 0:
            required_number = 1
        else:
            try:
                v_chana_dal = float(e1_chana_dal.get())
            except:
                valid_number = 1

        if e1_rajma.get() == "" or e1_rajma.get() == 0:
            required_number = 1
        else:
            try:
                v_rajma = float(e1_rajma.get())
            except:
                valid_number = 1

        if e1_white1_chana.get() == "" or e1_white1_chana.get() == 0:
            required_number = 1
        else:
            try:
                v_white1_chana = float(e1_white1_chana.get())
            except:
                valid_number = 1

        if required_number == 1:
            messagebox.showerror("REQUIRED FIELD", "ALL FIELDS ARE REQUIRED", parent=innerframe2)
        if valid_number == 1:
            messagebox.showerror("NUMBER", "PLEASE ENTER A VALID NUMBER", parent=innerframe2)

        if e3_toor_dal.get() == "":
            pass
        else:
            try:
                v3_toor_dal = float(e3_toor_dal.get())
            except:
                valid3_number = 1

        if e3_urad3_dal.get() == "":
            pass
        else:
            try:
                v3_urad3_dal = float(e3_urad3_dal.get())
            except:
                valid3_number = 1

        if e3_moong_dal.get() == "":
            pass
        else:
            try:
                v3_moong_dal = float(e3_moong_dal.get())
            except:
                valid3_number = 1

        if e3_chana_dal.get() == "":
            pass
        else:
            try:
                v3_chana_dal = float(e3_chana_dal.get())
            except:
                valid3_number = 1

        if e3_rajma.get() == "":
            pass
        else:
            try:
                v3_rajma = float(e3_rajma.get())
            except:
                valid3_number = 1

        if e3_white3_chana.get() == "":
            pass
        else:
            try:
                v3_white3_chana = float(e3_white3_chana.get())
            except:
                valid3_number = 1

        if valid3_number == 1:
            messagebox.showerror("NUMBER", "PLEASE ENTER A VALID NUMBER", parent=innerframe2)

        con = sqlite3.connect('price.db')
        c1 = con.cursor()
        id = 1
        c1.execute("INSERT OR REPLACE into d3_pulses VALUES (:id,:a, :b, :c, :d, :e, :f)",
                   {'id': id,
                    'a': float(v3_toor_dal),
                    'b': float(v3_urad3_dal),
                    'c': float(v3_moong_dal),
                    'd': float(v3_chana_dal),
                    'e': float(v3_rajma),
                    'f': float(v3_white3_chana)
                    })

        con.commit()

        con.close()

        con = sqlite3.connect('price.db')
        c1 = con.cursor()
        id = 1
        c1.execute("INSERT OR REPLACE into d_pulses VALUES (:id,:a, :b, :c, :d, :e, :f)",
                   {'id': id,
                    'a': float(v_toor_dal),
                    'b': float(v_urad_dal),
                    'c': float(v_moong_dal),
                    'd': float(v_chana_dal),
                    'e': float(v_rajma),
                    'f': float(v_white1_chana)
                    })

        con.commit()

        con.close()

        innerframe2.destroy()

    def pulses():
        global e1_toor_dal
        global e1_urad_dal
        global e1_moong_dal
        global e1_chana_dal
        global e1_rajma
        global e1_white1_chana
        global innerframe2

        global e3_toor_dal
        global e3_urad3_dal
        global e3_moong_dal
        global e3_chana_dal
        global e3_rajma
        global e3_white3_chana

        innerframe2 = Toplevel(bg="#f6ead4", relief=GROOVE, bd=9)
        # innerframe1.geometry("500x200+200+100")
        innerframe2.title("PULSES AND DALS")
        toor_dal = Label(innerframe2, text="TOOR DAL", font=("times new roman", 15, "bold"), fg="#51361a",
                         bg="#f6ead4")
        toor_dal.grid(row=0, column=0)
        urad_dal = Label(innerframe2, text="URAD DAL", font=("times new roman", 15, "bold"), fg="#51361a",
                         bg="#f6ead4")
        urad_dal.grid(row=1, column=0)
        moong_dal = Label(innerframe2, text="YELLOW MOONG DAAL", font=("times new roman", 15, "bold"), fg="#51361a",
                          bg="#f6ead4")
        moong_dal.grid(row=2, column=0)
        chana_dal = Label(innerframe2, text="CHANA DAL", font=("times new roman", 15, "bold"), fg="#51361a",
                          bg="#f6ead4")
        chana_dal.grid(row=3, column=0)
        rajma = Label(innerframe2, text="RAJMA( in kg ) ", font=("times new roman", 15, "bold"), fg="#51361a",
                      bg="#f6ead4")
        rajma.grid(row=4, column=0)
        white1_chana = Label(innerframe2, text="WHITE CHANA", font=("times new roman", 15, "bold"), fg="#51361a",
                             bg="#f6ead4")
        white1_chana.grid(row=5, column=0)

        e1_toor_dal = Entry(innerframe2, width=25, relief=SUNKEN, bd=4)
        e1_toor_dal.grid(row=0, column=2)
        e1_urad_dal = Entry(innerframe2, width=25, relief=SUNKEN, bd=4)
        e1_urad_dal.grid(row=1, column=2)
        e1_moong_dal = Entry(innerframe2, width=25, relief=SUNKEN, bd=4)
        e1_moong_dal.grid(row=2, column=2)
        e1_chana_dal = Entry(innerframe2, width=25, relief=SUNKEN, bd=4)
        e1_chana_dal.grid(row=3, column=2)
        e1_rajma = Entry(innerframe2, width=25, relief=SUNKEN, bd=4)
        e1_rajma.grid(row=4, column=2)
        e1_white1_chana = Entry(innerframe2, width=25, relief=SUNKEN, bd=4)
        e1_white1_chana.grid(row=5, column=2)

        e3_toor_dal = Entry(innerframe2, width=25, relief=SUNKEN, bd=4)
        e3_toor_dal.grid(row=0, column=3)
        e3_urad3_dal = Entry(innerframe2, width=25, relief=SUNKEN, bd=4)
        e3_urad3_dal.grid(row=1, column=3)
        e3_moong_dal = Entry(innerframe2, width=25, relief=SUNKEN, bd=4)
        e3_moong_dal.grid(row=2, column=3)
        e3_chana_dal = Entry(innerframe2, width=25, relief=SUNKEN, bd=4)
        e3_chana_dal.grid(row=3, column=3)
        e3_rajma = Entry(innerframe2, width=25, relief=SUNKEN, bd=4)
        e3_rajma.grid(row=4, column=3)
        e3_white3_chana = Entry(innerframe2, width=25, relief=SUNKEN, bd=4)
        e3_white3_chana.grid(row=5, column=3)

        try:
            con = sqlite3.connect('price.db')

            c1 = con.cursor()

            c1.execute("SELECT * FROM d3_pulses")
            insert_rice = c1.fetchall()
            insert = insert_rice[0]

            e3_toor_dal.insert(0, insert[1])
            e3_urad3_dal.insert(0, insert[2])
            e3_moong_dal.insert(0, insert[3])
            e3_chana_dal.insert(0, insert[4])
            e3_rajma.insert(0, insert[5])
            e3_white3_chana.insert(0, insert[6])

            con.commit()

            con.close()
        except:
            pass

        try:
            con = sqlite3.connect('price.db')

            c1 = con.cursor()

            c1.execute("SELECT * FROM d_pulses")
            insert_rice = c1.fetchall()
            insert = insert_rice[0]

            e1_toor_dal.insert(0, insert[1])
            e1_urad_dal.insert(0, insert[2])
            e1_moong_dal.insert(0, insert[3])
            e1_chana_dal.insert(0, insert[4])
            e1_rajma.insert(0, insert[5])
            e1_white1_chana.insert(0, insert[6])

            con.commit()

            con.close()
        except:
            pass

        total2 = Button(innerframe2, text="OK", command=cal2, width=20, font=("times new roaman", 20, "bold"),
                        fg="#51361a", bg="#b4a284", relief=GROOVE, bd=9)
        total2.grid(row=6, column=0, columnspan=3, pady=15)

    def cal3():
        global v_crystal_salt
        global v_powder_salt
        global v_redchilli_powder
        global v_dhania_powder
        global v_garammasala_powder
        global v_chatmasala_powder
        global v_pepper_powder
        global v_sambar_powder
        global v_biryani_powder
        global v_coffee1_powder
        global v_tea_powder
        v_crystal_salt = 0
        v_powder_salt = 0
        v_redchilli_powder = 0
        v_dhania_powder = 0
        v_garammasala_powder = 0
        v_chatmasala_powder = 0
        v_pepper_powder = 0
        v_sambar_powder = 0
        v_biryani_powder = 0
        v_coffee1_powder = 0
        v_tea_powder = 0
        required_number = 0
        valid_number = 0

        global v3_crystal_salt
        global v3_powder_salt
        global v3_redchilli_powder
        global v3_dhania_powder
        global v3_garammasala_powder
        global v3_chatmasala_powder
        global v3_pepper_powder
        global v3_sambar_powder
        global v3_biryani_powder
        global v3_coffee3_powder
        global v3_tea_powder
        v3_crystal_salt = 0
        v3_powder_salt = 0
        v3_redchilli_powder = 0
        v3_dhania_powder = 0
        v3_garammasala_powder = 0
        v3_chatmasala_powder = 0
        v3_pepper_powder = 0
        v3_sambar_powder = 0
        v3_biryani_powder = 0
        v3_coffee3_powder = 0
        v3_tea_powder = 0
        required3_number = 0
        valid3_number = 0

        if e1_crystal_salt.get() == "" or e1_crystal_salt.get() == 0:
            required_number = 1
        else:
            try:
                v_crystal_salt = float(e1_crystal_salt.get())
            except:
                valid_number = 1

        if e1_powder_salt.get() == "" or e1_powder_salt.get() == 0:
            required_number = 1
        else:
            try:
                v_powder_salt = float(e1_powder_salt.get())
            except:
                valid_number = 1

        if e1_redchilli_powder.get() == "" or e1_redchilli_powder.get() == 0:
            required_number = 1
        else:
            try:
                v_redchilli_powder = float(e1_redchilli_powder.get())
            except:
                valid_number = 1

        if e1_dhania_powder.get() == "" or e1_dhania_powder.get() == 0:
            required_number = 1
        else:
            try:
                v_dhania_powder = float(e1_dhania_powder.get())
            except:
                valid_number = 1

        if e1_garammasala_powder.get() == "" or e1_garammasala_powder.get() == 0:
            required_number = 1
        else:
            try:
                v_garammasala_powder = float(e1_garammasala_powder.get())
            except:
                valid_number = 1

        if e1_chatmasala_powder.get() == "" or e1_chatmasala_powder.get() == 0:
            required_number = 1
        else:
            try:
                v_chatmasala_powder = float(e1_chatmasala_powder.get())
            except:
                valid_number = 1

        if e1_pepper_powder.get() == "" or e1_pepper_powder.get() == 0:
            required_number = 1
        else:
            try:
                v_pepper_powder = float(e1_pepper_powder.get())
            except:
                valid_number = 1

        if e1_sambar_powder.get() == "" or e1_sambar_powder.get() == 0:
            required_number = 1
        else:
            try:
                v_sambar_powder = float(e1_sambar_powder.get())
            except:
                valid_number = 1

        if e1_biryani_powder.get() == "" or e1_biryani_powder.get() == 0:
            required_number = 1
        else:
            try:
                v_biryani_powder = float(e1_biryani_powder.get())
            except:
                valid_number = 1

        if e1_coffee1_powder.get() == "" or e1_coffee1_powder.get() == 0:
            required_number = 1
        else:
            try:
                v_coffee1_powder = float(e1_coffee1_powder.get())
            except:
                valid_number = 1

        if e1_tea_powder.get() == "" or e1_tea_powder.get() == 0:
            required_number = 1
        else:
            try:
                v_tea_powder = float(e1_tea_powder.get())
            except:
                valid_number = 1

        if required_number == 1:
            messagebox.showerror("REQUIRED FIELD", "ALL FIELDS ARE REQUIRED", parent=innerframe3)
        if valid_number == 1:
            messagebox.showerror("NUMBER", "PLEASE ENTER A VALID NUMBER", parent=innerframe3)

        if e3_crystal_salt.get() == "":
            pass
        else:
            try:
                v3_crystal_salt = float(e3_crystal_salt.get())
            except:
                valid3_number = 1

        if e3_powder_salt.get() == "":
            pass
        else:
            try:
                v3_powder_salt = float(e3_powder_salt.get())
            except:
                valid3_number = 1

        if e3_redchilli_powder.get() == "":
            pass
        else:
            try:
                v3_redchilli_powder = float(e3_redchilli_powder.get())
            except:
                valid3_number = 1

        if e3_dhania_powder.get() == "":
            pass
        else:
            try:
                v3_dhania_powder = float(e3_dhania_powder.get())
            except:
                valid3_number = 1

        if e3_garammasala_powder.get() == "":
            pass
        else:
            try:
                v3_garammasala_powder = float(e3_garammasala_powder.get())
            except:
                valid3_number = 1

        if e3_chatmasala_powder.get() == "":
            pass
        else:
            try:
                v3_chatmasala_powder = float(e3_chatmasala_powder.get())
            except:
                valid3_number = 1

        if e3_pepper_powder.get() == "":
            pass
        else:
            try:
                v3_pepper_powder = float(e3_pepper_powder.get())
            except:
                valid3_number = 1

        if e3_sambar_powder.get() == "":
            pass
        else:
            try:
                v3_sambar_powder = float(e3_sambar_powder.get())
            except:
                valid3_number = 1

        if e3_biryani_powder.get() == "":
            pass
        else:
            try:
                v3_biryani_powder = float(e3_biryani_powder.get())
            except:
                valid3_number = 1

        if e3_coffee3_powder.get() == "":
            pass
        else:
            try:
                v3_coffee3_powder = float(e3_coffee3_powder.get())
            except:
                valid3_number = 1

        if e3_tea_powder.get() == "":
            pass
        else:
            try:
                v3_tea_powder = float(e3_tea_powder.get())
            except:
                valid3_number = 1

        if valid3_number == 1:
            messagebox.showerror("NUMBER", "PLEASE ENTER A VALID NUMBER", parent=innerframe3)

        con = sqlite3.connect('price.db')

        c1 = con.cursor()
        id = 1
        c1.execute("INSERT OR REPLACE into d3_spice_powder VALUES (:id,:a, :b, :c, :d,:e, :f, :g, :h, :i,:j, :k)",
                   {'id': id,
                    'a': float(v3_crystal_salt),
                    'b': float(v3_powder_salt),
                    'c': float(v3_redchilli_powder),
                    'd': float(v3_dhania_powder),
                    'e': float(v3_garammasala_powder),
                    'f': float(v3_chatmasala_powder),
                    'g': float(v3_pepper_powder),
                    'h': float(v3_sambar_powder),
                    'i': float(v3_biryani_powder),
                    'j': float(v3_coffee3_powder),
                    'k': float(v3_tea_powder)})

        con.commit()

        con.close()

        con = sqlite3.connect('price.db')

        c1 = con.cursor()
        id = 1
        c1.execute("INSERT OR REPLACE into d_spice_powder VALUES (:id,:a, :b, :c, :d,:e, :f, :g, :h, :i,:j, :k)",
                   {'id': id,
                    'a': float(v_crystal_salt),
                    'b': float(v_powder_salt),
                    'c': float(v_redchilli_powder),
                    'd': float(v_dhania_powder),
                    'e': float(v_garammasala_powder),
                    'f': float(v_chatmasala_powder),
                    'g': float(v_pepper_powder),
                    'h': float(v_sambar_powder),
                    'i': float(v_biryani_powder),
                    'j': float(v_coffee1_powder),
                    'k': float(v_tea_powder)})

        con.commit()

        con.close()

        innerframe3.destroy()

    def spices():
        global innerframe3
        global e1_crystal_salt
        global e1_powder_salt
        global e1_redchilli_powder
        global e1_dhania_powder
        global e1_garammasala_powder
        global e1_chatmasala_powder
        global e1_pepper_powder
        global e1_sambar_powder
        global e1_biryani_powder
        global e1_coffee1_powder
        global e1_tea_powder

        global e3_crystal_salt
        global e3_powder_salt
        global e3_redchilli_powder
        global e3_dhania_powder
        global e3_garammasala_powder
        global e3_chatmasala_powder
        global e3_pepper_powder
        global e3_sambar_powder
        global e3_biryani_powder
        global e3_coffee3_powder
        global e3_tea_powder

        innerframe3 = Toplevel(bg="#f6ead4", relief=GROOVE, bd=9)
        # innerframe3.geometry("500x200+200+100")
        innerframe3.title("RICE AND FLOURS")
        crystal_salt = Label(innerframe3, text="CRYSTAL SALT ", font=("times new roman", 15, "bold"), fg="#51361a",
                             bg="#f6ead4")
        crystal_salt.grid(row=0, column=0)
        powder_salt = Label(innerframe3, text="SALT POWDER ", font=("times new roman", 15, "bold"), fg="#51361a",
                            bg="#f6ead4")
        powder_salt.grid(row=1, column=0)
        redchilli_powder = Label(innerframe3, text="RED CHILLI POWDER", font=("times new roman", 15, "bold"),
                                 fg="#51361a",
                                 bg="#f6ead4")
        redchilli_powder.grid(row=2, column=0)
        dhania_powder = Label(innerframe3, text="DHANIA POWDER ", font=("times new roman", 15, "bold"), fg="#51361a",
                              bg="#f6ead4")
        dhania_powder.grid(row=3, column=0)
        garammasala_powder = Label(innerframe3, text="GARAM MASALA POWDER ", font=("times new roman", 15, "bold"),
                                   fg="#51361a",
                                   bg="#f6ead4")
        garammasala_powder.grid(row=4, column=0)
        chatmasala_powder = Label(innerframe3, text="CHAT MASALA POWDER", font=("times new roman", 15, "bold"),
                                  fg="#51361a",
                                  bg="#f6ead4")
        chatmasala_powder.grid(row=5, column=0)
        pepper_powder = Label(innerframe3, text="PEPPER POWDER", font=("times new roman", 15, "bold"), fg="#51361a",
                              bg="#f6ead4")
        pepper_powder.grid(row=6, column=0)
        sambar_powder = Label(innerframe3, text="SAMBAR POWDER ", font=("times new roman", 15, "bold"), fg="#51361a",
                              bg="#f6ead4")
        sambar_powder.grid(row=7, column=0)
        biryani_powder = Label(innerframe3, text="BIRYANI POWDER", font=("times new roman", 15, "bold"), fg="#51361a",
                               bg="#f6ead4")
        biryani_powder.grid(row=8, column=0)
        coffee1_powder = Label(innerframe3, text="COFFEE POWDER", font=("times new roman", 15, "bold"), fg="#51361a",
                               bg="#f6ead4")
        coffee1_powder.grid(row=9, column=0)
        tea_powder = Label(innerframe3, text="TEA POWDER", font=("times new roman", 15, "bold"), fg="#51361a",
                           bg="#f6ead4")
        tea_powder.grid(row=10, column=0)

        e1_crystal_salt = Entry(innerframe3, width=25, relief=SUNKEN, bd=4)
        e1_crystal_salt.grid(row=0, column=2)
        e1_powder_salt = Entry(innerframe3, width=25, relief=SUNKEN, bd=4)
        e1_powder_salt.grid(row=1, column=2)
        e1_redchilli_powder = Entry(innerframe3, width=25, relief=SUNKEN, bd=4)
        e1_redchilli_powder.grid(row=2, column=2)
        e1_dhania_powder = Entry(innerframe3, width=25, relief=SUNKEN, bd=4)
        e1_dhania_powder.grid(row=3, column=2)
        e1_garammasala_powder = Entry(innerframe3, width=25, relief=SUNKEN, bd=4)
        e1_garammasala_powder.grid(row=4, column=2)
        e1_chatmasala_powder = Entry(innerframe3, width=25, relief=SUNKEN, bd=4)
        e1_chatmasala_powder.grid(row=5, column=2)
        e1_pepper_powder = Entry(innerframe3, width=25, relief=SUNKEN, bd=4)
        e1_pepper_powder.grid(row=6, column=2)
        e1_sambar_powder = Entry(innerframe3, width=25, relief=SUNKEN, bd=4)
        e1_sambar_powder.grid(row=7, column=2)
        e1_biryani_powder = Entry(innerframe3, width=25, relief=SUNKEN, bd=4)
        e1_biryani_powder.grid(row=8, column=2)
        e1_coffee1_powder = Entry(innerframe3, width=25, relief=SUNKEN, bd=4)
        e1_coffee1_powder.grid(row=9, column=2)
        e1_tea_powder = Entry(innerframe3, width=25, relief=SUNKEN, bd=4)
        e1_tea_powder.grid(row=10, column=2)

        e3_crystal_salt = Entry(innerframe3, width=25, relief=SUNKEN, bd=4)
        e3_crystal_salt.grid(row=0, column=3)
        e3_powder_salt = Entry(innerframe3, width=25, relief=SUNKEN, bd=4)
        e3_powder_salt.grid(row=1, column=3)
        e3_redchilli_powder = Entry(innerframe3, width=25, relief=SUNKEN, bd=4)
        e3_redchilli_powder.grid(row=2, column=3)
        e3_dhania_powder = Entry(innerframe3, width=25, relief=SUNKEN, bd=4)
        e3_dhania_powder.grid(row=3, column=3)
        e3_garammasala_powder = Entry(innerframe3, width=25, relief=SUNKEN, bd=4)
        e3_garammasala_powder.grid(row=4, column=3)
        e3_chatmasala_powder = Entry(innerframe3, width=25, relief=SUNKEN, bd=4)
        e3_chatmasala_powder.grid(row=5, column=3)
        e3_pepper_powder = Entry(innerframe3, width=25, relief=SUNKEN, bd=4)
        e3_pepper_powder.grid(row=6, column=3)
        e3_sambar_powder = Entry(innerframe3, width=25, relief=SUNKEN, bd=4)
        e3_sambar_powder.grid(row=7, column=3)
        e3_biryani_powder = Entry(innerframe3, width=25, relief=SUNKEN, bd=4)
        e3_biryani_powder.grid(row=8, column=3)
        e3_coffee3_powder = Entry(innerframe3, width=25, relief=SUNKEN, bd=4)
        e3_coffee3_powder.grid(row=9, column=3)
        e3_tea_powder = Entry(innerframe3, width=25, relief=SUNKEN, bd=4)
        e3_tea_powder.grid(row=10, column=3)

        try:
            con = sqlite3.connect('price.db')

            c1 = con.cursor()

            c1.execute("SELECT * FROM d3_spice_powder")
            insert_rice = c1.fetchall()
            insert = insert_rice[0]

            e3_crystal_salt.insert(0, insert[1])
            e3_powder_salt.insert(0, insert[2])
            e3_redchilli_powder.insert(0, insert[3])
            e3_dhania_powder.insert(0, insert[4])
            e3_garammasala_powder.insert(0, insert[5])
            e3_chatmasala_powder.insert(0, insert[6])
            e3_pepper_powder.insert(0, insert[7])
            e3_sambar_powder.insert(0, insert[8])
            e3_biryani_powder.insert(0, insert[9])
            e3_coffee3_powder.insert(0, insert[10])
            e3_tea_powder.insert(0, insert[11])

            con.commit()

            con.close()
        except:
            pass

        try:
            con = sqlite3.connect('price.db')

            c1 = con.cursor()

            c1.execute("SELECT * FROM d_spice_powder")
            insert_rice = c1.fetchall()
            insert = insert_rice[0]

            e1_crystal_salt.insert(0, insert[1])
            e1_powder_salt.insert(0, insert[2])
            e1_redchilli_powder.insert(0, insert[3])
            e1_dhania_powder.insert(0, insert[4])
            e1_garammasala_powder.insert(0, insert[5])
            e1_chatmasala_powder.insert(0, insert[6])
            e1_pepper_powder.insert(0, insert[7])
            e1_sambar_powder.insert(0, insert[8])
            e1_biryani_powder.insert(0, insert[9])
            e1_coffee1_powder.insert(0, insert[10])
            e1_tea_powder.insert(0, insert[11])

            con.commit()

            con.close()
        except:
            pass

        total = Button(innerframe3, text="OK", command=cal3, width=20, font=("times new roaman", 20, "bold"),
                       fg="#51361a", bg="#b4a284", relief=GROOVE, bd=9)
        total.grid(row=11, column=0, columnspan=3, pady=15)

    def cal4():
        global v_cooking_oil
        global v_seasame1_oil
        global v_coconut_oil
        global v_ghee
        global v_olive1_oil

        v_cooking_oil = 0
        v_seasame1_oil = 0
        v_coconut_oil = 0
        v_ghee = 0
        v_olive1_oil = 0
        required_number = 0
        valid_number = 0

        global v3_cooking_oil
        global v3_seasame3_oil
        global v3_coconut_oil
        global v3_ghee
        global v3_olive3_oil

        v3_cooking_oil = 0
        v3_seasame3_oil = 0
        v3_coconut_oil = 0
        v3_ghee = 0
        v3_olive3_oil = 0
        required3_number = 0
        valid3_number = 0

        if e1_cooking_oil.get() == "" or e1_cooking_oil.get() == 0:
            required_number = 1
        else:
            try:
                v_cooking_oil = float(e1_cooking_oil.get())
            except:
                valid_number = 1

        if e1_seasame1_oil.get() == "" or e1_seasame1_oil.get() == 0:
            required_number = 1
        else:
            try:
                v_seasame1_oil = float(e1_seasame1_oil.get())
            except:
                valid_number = 1

        if e1_coconut_oil.get() == "" or e1_coconut_oil.get() == 0:
            required_number = 1
        else:
            try:
                v_coconut_oil = float(e1_coconut_oil.get())
            except:
                valid_number = 1

        if e1_ghee.get() == "" or e1_ghee.get() == 0:
            required_number = 1
        else:
            try:
                v_ghee = float(e1_ghee.get())
            except:
                valid_number = 1

        if e1_olive1_oil.get() == "" or e1_olive1_oil.get() == 0:
            required_number = 1
        else:
            try:
                v_olive1_oil = float(e1_olive1_oil.get())
            except:
                valid_number = 1

        if required_number == 1:
            messagebox.showerror("REQUIRED FIELD", "ALL FIELDS ARE REQUIRED", parent=innerframe4)
        if valid_number == 1:
            messagebox.showerror("NUMBER", "PLEASE ENTER A VALID NUMBER", parent=innerframe4)

        if e3_cooking_oil.get() == "":
            pass
        else:
            try:
                v3_cooking_oil = float(e3_cooking_oil.get())
            except:
                valid3_number = 1

        if e3_seasame3_oil.get() == "":
            pass
        else:
            try:
                v3_seasame3_oil = float(e3_seasame3_oil.get())
            except:
                valid3_number = 1

        if e3_coconut_oil.get() == "":
            pass
        else:
            try:
                v3_coconut_oil = float(e3_coconut_oil.get())
            except:
                valid3_number = 1

        if e3_ghee.get() == "":
            pass
        else:
            try:
                v3_ghee = float(e3_ghee.get())
            except:
                valid3_number = 1

        if e3_olive3_oil.get() == "":
            pass
        else:
            try:
                v3_olive3_oil = float(e3_olive3_oil.get())
            except:
                valid3_number = 1

            if valid3_number == 1:
                messagebox.showerror("NUMBER", "PLEASE ENTER A VALID NUMBER", parent=innerframe4)

        con = sqlite3.connect('price.db')

        c1 = con.cursor()
        id = 1
        c1.execute("INSERT OR REPLACE into d3_oils VALUES (:id,:a, :b, :c, :d,:e)",
                   {'id': id,
                    'a': float(v3_cooking_oil),
                    'b': float(v3_seasame3_oil),
                    'c': float(v3_coconut_oil),
                    'd': float(v3_ghee),
                    'e': float(v3_olive3_oil)})

        con.commit()

        con.close()

        con = sqlite3.connect('price.db')

        c1 = con.cursor()
        id = 1
        c1.execute("INSERT OR REPLACE into d_oils VALUES (:id,:a, :b, :c, :d,:e)",
                   {'id': id,
                    'a': float(v_cooking_oil),
                    'b': float(v_seasame1_oil),
                    'c': float(v_coconut_oil),
                    'd': float(v_ghee),
                    'e': float(v_olive1_oil)})

        con.commit()

        con.close()

        innerframe4.destroy()

    def oil():
        global e1_cooking_oil
        global e1_seasame1_oil
        global e1_coconut_oil
        global e1_ghee
        global e1_olive1_oil
        global innerframe4

        global e3_cooking_oil
        global e3_seasame3_oil
        global e3_coconut_oil
        global e3_ghee
        global e3_olive3_oil

        innerframe4 = Toplevel(bg="#f6ead4", relief=GROOVE, bd=9)
        # innerframe1.geometry("500x200+200+100")
        innerframe4.title("OILS")
        cooking_oil = Label(innerframe4, text="COOKING OIL", font=("times new roman", 15, "bold"), fg="#51361a",
                            bg="#f6ead4")
        cooking_oil.grid(row=0, column=0)
        seasame1_oil = Label(innerframe4, text="SEASAME OIL", font=("times new roman", 15, "bold"), fg="#51361a",
                             bg="#f6ead4")
        seasame1_oil.grid(row=1, column=0)
        coconut_oil = Label(innerframe4, text="COCONUT OIL", font=("times new roman", 15, "bold"), fg="#51361a",
                            bg="#f6ead4")
        coconut_oil.grid(row=2, column=0)
        ghee = Label(innerframe4, text="GHEE", font=("times new roman", 15, "bold"), fg="#51361a",
                     bg="#f6ead4")
        ghee.grid(row=3, column=0)
        olive1_oil = Label(innerframe4, text="OLIVE OIL ", font=("times new roman", 15, "bold"), fg="#51361a",
                           bg="#f6ead4")
        olive1_oil.grid(row=4, column=0)

        e1_cooking_oil = Entry(innerframe4, width=25, relief=SUNKEN, bd=4)
        e1_cooking_oil.grid(row=0, column=2)
        e1_seasame1_oil = Entry(innerframe4, width=25, relief=SUNKEN, bd=4)
        e1_seasame1_oil.grid(row=1, column=2)
        e1_coconut_oil = Entry(innerframe4, width=25, relief=SUNKEN, bd=4)
        e1_coconut_oil.grid(row=2, column=2)
        e1_ghee = Entry(innerframe4, width=25, relief=SUNKEN, bd=4)
        e1_ghee.grid(row=3, column=2)
        e1_olive1_oil = Entry(innerframe4, width=25, relief=SUNKEN, bd=4)
        e1_olive1_oil.grid(row=4, column=2)

        e3_cooking_oil = Entry(innerframe4, width=25, relief=SUNKEN, bd=4)
        e3_cooking_oil.grid(row=0, column=3)
        e3_seasame3_oil = Entry(innerframe4, width=25, relief=SUNKEN, bd=4)
        e3_seasame3_oil.grid(row=1, column=3)
        e3_coconut_oil = Entry(innerframe4, width=25, relief=SUNKEN, bd=4)
        e3_coconut_oil.grid(row=2, column=3)
        e3_ghee = Entry(innerframe4, width=25, relief=SUNKEN, bd=4)
        e3_ghee.grid(row=3, column=3)
        e3_olive3_oil = Entry(innerframe4, width=25, relief=SUNKEN, bd=4)
        e3_olive3_oil.grid(row=4, column=3)

        try:
            con = sqlite3.connect('price.db')

            c1 = con.cursor()

            c1.execute("SELECT * FROM d3_oils")
            insert_rice = c1.fetchall()
            insert = insert_rice[0]

            e3_cooking_oil.insert(0, insert[1])
            e3_seasame3_oil.insert(0, insert[2])
            e3_coconut_oil.insert(0, insert[3])
            e3_ghee.insert(0, insert[4])
            e3_olive3_oil.insert(0, insert[5])

            con.commit()

            con.close()
        except:
            pass

        try:
            con = sqlite3.connect('price.db')

            c1 = con.cursor()

            c1.execute("SELECT * FROM d_oils")
            insert_rice = c1.fetchall()
            insert = insert_rice[0]

            e1_cooking_oil.insert(0, insert[1])
            e1_seasame1_oil.insert(0, insert[2])
            e1_coconut_oil.insert(0, insert[3])
            e1_ghee.insert(0, insert[4])
            e1_olive1_oil.insert(0, insert[5])

            con.commit()

            con.close()
        except:
            pass

        total2 = Button(innerframe4, text="OK", command=cal4, width=20, font=("times new roaman", 20, "bold"),
                        fg="#51361a", bg="#b4a284", relief=GROOVE, bd=9)
        total2.grid(row=5, column=0, columnspan=3, pady=15)

    def cal5():
        global v_mustard_seed
        global v_pepper
        global v_jeera
        global v_khus_khus
        global v_dhania
        global v_black_seasame1_seeds
        global v_white1_seasame1_seeds
        global v_cashew_nuts
        global v_raisins
        global v_badam
        global v_peanuts
        global v_dates

        v_mustard_seed = 0
        v_pepper = 0
        v_jeera = 0
        v_khus_khus = 0
        v_dhania = 0
        v_black_seasame1_seeds = 0
        v_white1_seasame1_seeds = 0
        v_cashew_nuts = 0
        v_raisins = 0
        v_badam = 0
        v_peanuts = 0
        v_dates = 0
        required_number = 0
        valid_number = 0

        global v3_mustard3_seed
        global v3_pepper
        global v3_jeera
        global v3_khus_khus
        global v3_dhania
        global v3_black_seasame3_seeds
        global v3_white3_seasame3_seeds
        global v3_cashew_nuts
        global v3_raisins
        global v3_badam
        global v3_peanuts
        global v3_dates

        v3_mustard3_seed = 0
        v3_pepper = 0
        v3_jeera = 0
        v3_khus_khus = 0
        v3_dhania = 0
        v3_black_seasame3_seeds = 0
        v3_white3_seasame3_seeds = 0
        v3_cashew_nuts = 0
        v3_raisins = 0
        v3_badam = 0
        v3_peanuts = 0
        v3_dates = 0
        required3_number = 0
        valid3_number = 0

        if e1_mustard_seed.get() == "" or e1_mustard_seed.get() == 0:
            required_number = 1
        else:
            try:
                v_mustard_seed = float(e1_mustard_seed.get())
            except:
                valid_number = 1

        if e1_pepper.get() == "" or e1_pepper.get() == 0:
            required_number = 1
        else:
            try:
                v_pepper = float(e1_pepper.get())
            except:
                valid_number = 1

        if e1_jeera.get() == "" or e1_jeera.get() == 0:
            required_number = 1
        else:
            try:
                v_jeera = float(e1_jeera.get())
            except:
                valid_number = 1

        if e1_khus_khus.get() == "" or e1_khus_khus.get() == 0:
            required_number = 1
        else:
            try:
                v_khus_khus = float(e1_khus_khus.get())
            except:
                valid_number = 1

        if e1_dhania.get() == "" or e1_dhania.get() == 0:
            required_number = 1
        else:
            try:
                v_dhania = float(e1_dhania.get())
            except:
                valid_number = 1

        if e1_black_seasame1_seeds.get() == "" or e1_black_seasame1_seeds.get() == 0:
            required_number = 1
        else:
            try:
                v_black_seasame1_seeds = float(e1_black_seasame1_seeds.get())
            except:
                valid_number = 1

        if e1_white1_seasame1_seeds.get() == "" or e1_white1_seasame1_seeds.get() == 0:
            required_number = 1
        else:
            try:
                v_white1_seasame1_seeds = float(e1_white1_seasame1_seeds.get())
            except:
                valid_number = 1

        if e1_cashew_nuts.get() == "" or e1_cashew_nuts.get() == 0:
            required_number = 1
        else:
            try:
                v_cashew_nuts = float(e1_cashew_nuts.get())
            except:
                valid_number = 1

        if e1_raisins.get() == "" or e1_raisins.get() == 0:
            required_number = 1
        else:
            try:
                v_raisins = float(e1_raisins.get())
            except:
                valid_number = 1

        if e1_badam.get() == "" or e1_badam.get() == 0:
            required_number = 1
        else:
            try:
                v_badam = float(e1_badam.get())
            except:
                valid_number = 1

        if e1_peanuts.get() == "" or e1_peanuts.get() == 0:
            required_number = 1
        else:
            try:
                v_peanuts = float(e1_peanuts.get())
            except:
                valid_number = 1

        if e1_dates.get() == "" or e1_dates.get() == 0:
            required_number = 1
        else:
            try:
                v_dates = float(e1_dates.get())
            except:
                valid_number = 1

        if required_number == 1:
            messagebox.showerror("REQUIRED FIELD", "ALL FIELDS ARE REQUIRED", parent=innerframe5)
        if valid_number == 1:
            messagebox.showerror("NUMBER", "PLEASE ENTER A VALID NUMBER", parent=innerframe5)

        if e3_mustard3_seed.get() == "":
            pass
        else:
            try:
                v3_mustard3_seed = float(e3_mustard3_seed.get())
            except:
                valid3_number = 1

        if e3_pepper.get() == "":
            pass
        else:
            try:
                v3_pepper = float(e3_pepper.get())
            except:
                valid3_number = 1

        if e3_jeera.get() == "":
            pass
        else:
            try:
                v3_jeera = float(e3_jeera.get())
            except:
                valid3_number = 1

        if e3_khus_khus.get() == "":
            pass
        else:
            try:
                v3_khus_khus = float(e3_khus_khus.get())
            except:
                valid3_number = 1

        if e3_dhania.get() == "":
            pass
        else:
            try:
                v3_dhania = float(e3_dhania.get())
            except:
                valid3_number = 1

        if e3_black_seasame3_seeds.get() == "":
            pass
        else:
            try:
                v3_black_seasame3_seeds = float(e3_black_seasame3_seeds.get())
            except:
                valid3_number = 1

        if e3_white3_seasame3_seeds.get() == "":
            pass
        else:
            try:
                v3_white3_seasame3_seeds = float(e3_white3_seasame3_seeds.get())
            except:
                valid3_number = 1

        if e3_cashew_nuts.get() == "":
            pass
        else:
            try:
                v3_cashew_nuts = float(e3_cashew_nuts.get())
            except:
                valid3_number = 1

        if e3_raisins.get() == "":
            pass
        else:
            try:
                v3_raisins = float(e3_raisins.get())
            except:
                valid3_number = 1

        if e3_badam.get() == "":
            pass
        else:
            try:
                v3_badam = float(e3_badam.get())
            except:
                valid3_number = 1

        if e3_peanuts.get() == "":
            pass
        else:
            try:
                v3_peanuts = float(e3_peanuts.get())
            except:
                valid3_number = 1

        if e3_dates.get() == "":
            pass
        else:
            try:
                v3_dates = float(e3_dates.get())
            except:
                valid3_number = 1

        if valid3_number == 1:
            messagebox.showerror("NUMBER", "PLEASE ENTER A VALID NUMBER", parent=innerframe5)

        con = sqlite3.connect('price.db')

        c1 = con.cursor()
        id = 1
        c1.execute("INSERT OR REPLACE into d3_spices_nuts VALUES (:id,:a, :b, :c, :d, :e, :f, :g, :h, :i,:j, :k, :l)",
                   {'id': id,
                    'a': float(v3_mustard3_seed),
                    'b': float(v3_pepper),
                    'c': float(v3_jeera),
                    'd': float(v3_khus_khus),
                    'e': float(v3_dhania),
                    'f': float(v3_black_seasame3_seeds),
                    'g': float(v3_white3_seasame3_seeds),
                    'h': float(v3_cashew_nuts),
                    'i': float(v3_raisins),
                    'j': float(v3_badam),
                    'k': float(v3_peanuts),
                    'l': float(v3_dates)
                    })

        con.commit()

        con.close()

        con = sqlite3.connect('price.db')

        c1 = con.cursor()
        id = 1
        c1.execute("INSERT OR REPLACE into d_spices_nuts VALUES (:id,:a, :b, :c, :d, :e, :f, :g, :h, :i,:j, :k, :l)",
                   {'id': id,
                    'a': float(v_mustard_seed),
                    'b': float(v_pepper),
                    'c': float(v_jeera),
                    'd': float(v_khus_khus),
                    'e': float(v_dhania),
                    'f': float(v_black_seasame1_seeds),
                    'g': float(v_white1_seasame1_seeds),
                    'h': float(v_cashew_nuts),
                    'i': float(v_raisins),
                    'j': float(v_badam),
                    'k': float(v_peanuts),
                    'l': float(v_dates)
                    })

        con.commit()

        con.close()

        innerframe5.destroy()

    def spice1_nut():
        global innerframe5
        global e1_mustard_seed
        global e1_pepper
        global e1_jeera
        global e1_khus_khus
        global e1_dhania
        global e1_black_seasame1_seeds
        global e1_white1_seasame1_seeds
        global e1_cashew_nuts
        global e1_raisins
        global e1_badam
        global e1_peanuts
        global e1_dates

        global e3_mustard3_seed
        global e3_pepper
        global e3_jeera
        global e3_khus_khus
        global e3_dhania
        global e3_black_seasame3_seeds
        global e3_white3_seasame3_seeds
        global e3_cashew_nuts
        global e3_raisins
        global e3_badam
        global e3_peanuts
        global e3_dates

        innerframe5 = Toplevel(bg="#f6ead4", relief=GROOVE, bd=9)
        # innerframe5.geometry("500x200+200+100")
        innerframe5.title("SPICES AND NUTS")
        mustard_seed = Label(innerframe5, text="MUSTARD SEEDS ", font=("times new roman", 15, "bold"), fg="#51361a",
                             bg="#f6ead4")
        mustard_seed.grid(row=0, column=0)
        pepper = Label(innerframe5, text="PEPPER", font=("times new roman", 15, "bold"), fg="#51361a",
                       bg="#f6ead4")
        pepper.grid(row=1, column=0)
        jeera = Label(innerframe5, text="JEERA ", font=("times new roman", 15, "bold"), fg="#51361a",
                      bg="#f6ead4")
        jeera.grid(row=2, column=0)
        khus_khus = Label(innerframe5, text="KHUS KHUS", font=("times new roman", 15, "bold"), fg="#51361a",
                          bg="#f6ead4")
        khus_khus.grid(row=3, column=0)
        dhania = Label(innerframe5, text="DHANIA ", font=("times new roman", 15, "bold"), fg="#51361a",
                       bg="#f6ead4")
        dhania.grid(row=4, column=0)
        black_seasame1_seeds = Label(innerframe5, text="BLACK SEASAME SEEDS", font=("times new roman", 15, "bold"),
                                     fg="#51361a",
                                     bg="#f6ead4")
        black_seasame1_seeds.grid(row=5, column=0)
        white1_seasame1_seeds = Label(innerframe5, text="WHITE SEASAME SEEDS", font=("times new roman", 15, "bold"),
                                      fg="#51361a",
                                      bg="#f6ead4")
        white1_seasame1_seeds.grid(row=6, column=0)
        cashew_nuts = Label(innerframe5, text="CASHEW NUTS", font=("times new roman", 15, "bold"), fg="#51361a",
                            bg="#f6ead4")
        cashew_nuts.grid(row=7, column=0)
        raisins = Label(innerframe5, text="RAISINS", font=("times new roman", 15, "bold"), fg="#51361a",
                        bg="#f6ead4")
        raisins.grid(row=8, column=0)
        badam = Label(innerframe5, text="BADAM", font=("times new roman", 15, "bold"), fg="#51361a",
                      bg="#f6ead4")
        badam.grid(row=9, column=0)
        peanuts = Label(innerframe5, text="PEANUTS", font=("times new roman", 15, "bold"), fg="#51361a",
                        bg="#f6ead4")
        peanuts.grid(row=10, column=0)
        dates = Label(innerframe5, text="DATES", font=("times new roman", 15, "bold"), fg="#51361a",
                      bg="#f6ead4")
        dates.grid(row=11, column=0)

        e1_mustard_seed = Entry(innerframe5, width=25, relief=SUNKEN, bd=4)
        e1_mustard_seed.grid(row=0, column=2)
        e1_pepper = Entry(innerframe5, width=25, relief=SUNKEN, bd=4)
        e1_pepper.grid(row=1, column=2)
        e1_jeera = Entry(innerframe5, width=25, relief=SUNKEN, bd=4)
        e1_jeera.grid(row=2, column=2)
        e1_khus_khus = Entry(innerframe5, width=25, relief=SUNKEN, bd=4)
        e1_khus_khus.grid(row=3, column=2)
        e1_dhania = Entry(innerframe5, width=25, relief=SUNKEN, bd=4)
        e1_dhania.grid(row=4, column=2)
        e1_black_seasame1_seeds = Entry(innerframe5, width=25, relief=SUNKEN, bd=4)
        e1_black_seasame1_seeds.grid(row=5, column=2)
        e1_white1_seasame1_seeds = Entry(innerframe5, width=25, relief=SUNKEN, bd=4)
        e1_white1_seasame1_seeds.grid(row=6, column=2)
        e1_cashew_nuts = Entry(innerframe5, width=25, relief=SUNKEN, bd=4)
        e1_cashew_nuts.grid(row=7, column=2)
        e1_raisins = Entry(innerframe5, width=25, relief=SUNKEN, bd=4)
        e1_raisins.grid(row=8, column=2)
        e1_badam = Entry(innerframe5, width=25, relief=SUNKEN, bd=4)
        e1_badam.grid(row=9, column=2)
        e1_peanuts = Entry(innerframe5, width=25, relief=SUNKEN, bd=4)
        e1_peanuts.grid(row=10, column=2)
        e1_dates = Entry(innerframe5, width=25, relief=SUNKEN, bd=4)
        e1_dates.grid(row=11, column=2)

        e3_mustard3_seed = Entry(innerframe5, width=25, relief=SUNKEN, bd=4)
        e3_mustard3_seed.grid(row=0, column=3)
        e3_pepper = Entry(innerframe5, width=25, relief=SUNKEN, bd=4)
        e3_pepper.grid(row=1, column=3)
        e3_jeera = Entry(innerframe5, width=25, relief=SUNKEN, bd=4)
        e3_jeera.grid(row=2, column=3)
        e3_khus_khus = Entry(innerframe5, width=25, relief=SUNKEN, bd=4)
        e3_khus_khus.grid(row=3, column=3)
        e3_dhania = Entry(innerframe5, width=25, relief=SUNKEN, bd=4)
        e3_dhania.grid(row=4, column=3)
        e3_black_seasame3_seeds = Entry(innerframe5, width=25, relief=SUNKEN, bd=4)
        e3_black_seasame3_seeds.grid(row=5, column=3)
        e3_white3_seasame3_seeds = Entry(innerframe5, width=25, relief=SUNKEN, bd=4)
        e3_white3_seasame3_seeds.grid(row=6, column=3)
        e3_cashew_nuts = Entry(innerframe5, width=25, relief=SUNKEN, bd=4)
        e3_cashew_nuts.grid(row=7, column=3)
        e3_raisins = Entry(innerframe5, width=25, relief=SUNKEN, bd=4)
        e3_raisins.grid(row=8, column=3)
        e3_badam = Entry(innerframe5, width=25, relief=SUNKEN, bd=4)
        e3_badam.grid(row=9, column=3)
        e3_peanuts = Entry(innerframe5, width=25, relief=SUNKEN, bd=4)
        e3_peanuts.grid(row=10, column=3)
        e3_dates = Entry(innerframe5, width=25, relief=SUNKEN, bd=4)
        e3_dates.grid(row=11, column=3)

        try:
            con = sqlite3.connect('price.db')

            c1 = con.cursor()

            c1.execute("SELECT * FROM d3_spices_nuts")
            insert_rice = c1.fetchall()
            insert = insert_rice[0]

            e3_mustard3_seed.insert(0, insert[1])
            e3_pepper.insert(0, insert[2])
            e3_jeera.insert(0, insert[3])
            e3_khus_khus.insert(0, insert[4])
            e3_dhania.insert(0, insert[5])
            e3_black_seasame3_seeds.insert(0, insert[6])
            e3_white3_seasame3_seeds.insert(0, insert[7])
            e3_cashew_nuts.insert(0, insert[8])
            e3_raisins.insert(0, insert[9])
            e3_badam.insert(0, insert[10])
            e3_peanuts.insert(0, insert[11])
            e3_dates.insert(0, insert[12])

            con.commit()

            con.close()
        except:
            pass

        try:
            con = sqlite3.connect('price.db')

            c1 = con.cursor()

            c1.execute("SELECT * FROM d_spices_nuts")
            insert_rice = c1.fetchall()
            insert = insert_rice[0]

            e1_mustard_seed.insert(0, insert[1])
            e1_pepper.insert(0, insert[2])
            e1_jeera.insert(0, insert[3])
            e1_khus_khus.insert(0, insert[4])
            e1_dhania.insert(0, insert[5])
            e1_black_seasame1_seeds.insert(0, insert[6])
            e1_white1_seasame1_seeds.insert(0, insert[7])
            e1_cashew_nuts.insert(0, insert[8])
            e1_raisins.insert(0, insert[9])
            e1_badam.insert(0, insert[10])
            e1_peanuts.insert(0, insert[11])
            e1_dates.insert(0, insert[12])

            con.commit()

            con.close()
        except:
            pass

        total = Button(innerframe5, text="OK", command=cal5, width=20, font=("times new roaman", 20, "bold"),
                       fg="#51361a", bg="#b4a284", relief=GROOVE, bd=9)
        total.grid(row=12, column=0, columnspan=3, pady=15)

    def cal6():
        global v_cheese1_block
        global v_butter
        global v_yoghurt
        global v_fresh_cream
        global v_paneer

        v_cheese1_block = 0
        v_butter = 0
        v_yoghurt = 0
        v_fresh_cream = 0
        v_paneer = 0
        required_number = 0
        valid_number = 0

        global v3_cheese3_block
        global v3_butter
        global v3_yoghurt
        global v3_fresh_cream
        global v3_paneer

        v3_cheese3_block = 0
        v3_butter = 0
        v3_yoghurt = 0
        v3_fresh_cream = 0
        v3_paneer = 0
        required3_number = 0
        valid3_number = 0

        if e1_cheese1_block.get() == "" or e1_cheese1_block.get() == 0:
            required_number = 1
        else:
            try:
                v_cheese1_block = float(e1_cheese1_block.get())
            except:
                valid_number = 1

        if e1_butter.get() == "" or e1_butter.get() == 0:
            required_number = 1
        else:
            try:
                v_butter = float(e1_butter.get())
            except:
                valid_number = 1

        if e1_yoghurt.get() == "" or e1_yoghurt.get() == 0:
            required_number = 1
        else:
            try:
                v_yoghurt = float(e1_yoghurt.get())
            except:
                valid_number = 1

        if e1_fresh_cream.get() == "" or e1_fresh_cream.get() == 0:
            required_number = 1
        else:
            try:
                v_fresh_cream = float(e1_fresh_cream.get())
            except:
                valid_number = 1

        if e1_paneer.get() == "" or e1_paneer.get() == 0:
            required_number = 1
        else:
            try:
                v_paneer = float(e1_paneer.get())
            except:
                valid_number = 1

        if required_number == 1:
            messagebox.showerror("REQUIRED FIELD", "ALL FIELDS ARE REQUIRED", parent=innerframe6)
        if valid_number == 1:
            messagebox.showerror("NUMBER", "PLEASE ENTER A VALID NUMBER", parent=innerframe6)

        if e3_cheese3_block.get() == "":
            pass
        else:
            try:
                v3_cheese3_block = float(e3_cheese3_block.get())
            except:
                valid3_number = 1

        if e3_butter.get() == "":
            pass
        else:
            try:
                v3_butter = float(e3_butter.get())
            except:
                valid3_number = 1

        if e3_yoghurt.get() == "":
            pass
        else:
            try:
                v3_yoghurt = float(e3_yoghurt.get())
            except:
                valid3_number = 1

        if e3_fresh_cream.get() == "":
            pass
        else:
            try:
                v3_fresh_cream = float(e3_fresh_cream.get())
            except:
                valid3_number = 1

        if e3_paneer.get() == "":
            pass
        else:
            try:
                v3_paneer = float(e3_paneer.get())
            except:
                valid3_number = 1

        if valid3_number == 1:
            messagebox.showerror("NUMBER", "PLEASE ENTER A VALID NUMBER", parent=innerframe6)

        con = sqlite3.connect('price.db')

        c1 = con.cursor()
        id = 1
        c1.execute("INSERT OR REPLACE into d3_dairy VALUES (:id,:a, :b, :c, :d, :e)",
                   {'id': id,
                    'a': float(v3_cheese3_block),
                    'b': float(v3_butter),
                    'c': float(v3_yoghurt),
                    'd': float(v3_fresh_cream),
                    'e': float(v3_paneer)

                    })

        con.commit()

        con.close()

        con = sqlite3.connect('price.db')

        c1 = con.cursor()
        id = 1
        c1.execute("INSERT OR REPLACE into d_dairy VALUES (:id,:a, :b, :c, :d, :e)",
                   {'id': id,
                    'a': float(v_cheese1_block),
                    'b': float(v_butter),
                    'c': float(v_yoghurt),
                    'd': float(v_fresh_cream),
                    'e': float(v_paneer)

                    })

        con.commit()

        con.close()

        innerframe6.destroy()

    def dairy():
        global e1_cheese1_block
        global e1_butter
        global e1_yoghurt
        global e1_fresh_cream
        global e1_paneer
        global innerframe6

        global e3_cheese3_block
        global e3_butter
        global e3_yoghurt
        global e3_fresh_cream
        global e3_paneer

        innerframe6 = Toplevel(bg="#f6ead4", relief=GROOVE, bd=9)
        innerframe6.title("DAIRY PRODUCTS")
        cheese1_block = Label(innerframe6, text="CHEESE BLOCK", font=("times new roman", 15, "bold"), fg="#51361a",
                              bg="#f6ead4")
        cheese1_block.grid(row=0, column=0)
        butter = Label(innerframe6, text="BUTTER", font=("times new roman", 15, "bold"), fg="#51361a",
                       bg="#f6ead4")
        butter.grid(row=1, column=0)
        yoghurt = Label(innerframe6, text="YOGHURT", font=("times new roman", 15, "bold"), fg="#51361a",
                        bg="#f6ead4")
        yoghurt.grid(row=2, column=0)
        fresh_cream = Label(innerframe6, text="FRESH CREAM", font=("times new roman", 15, "bold"), fg="#51361a",
                            bg="#f6ead4")
        fresh_cream.grid(row=3, column=0)
        paneer = Label(innerframe6, text="PANEER", font=("times new roman", 15, "bold"), fg="#51361a",
                       bg="#f6ead4")
        paneer.grid(row=4, column=0)

        e1_cheese1_block = Entry(innerframe6, width=25, relief=SUNKEN, bd=4)
        e1_cheese1_block.grid(row=0, column=2)
        e1_butter = Entry(innerframe6, width=25, relief=SUNKEN, bd=4)
        e1_butter.grid(row=1, column=2)
        e1_yoghurt = Entry(innerframe6, width=25, relief=SUNKEN, bd=4)
        e1_yoghurt.grid(row=2, column=2)
        e1_fresh_cream = Entry(innerframe6, width=25, relief=SUNKEN, bd=4)
        e1_fresh_cream.grid(row=3, column=2)
        e1_paneer = Entry(innerframe6, width=25, relief=SUNKEN, bd=4)
        e1_paneer.grid(row=4, column=2)

        e3_cheese3_block = Entry(innerframe6, width=25, relief=SUNKEN, bd=4)
        e3_cheese3_block.grid(row=0, column=3)
        e3_butter = Entry(innerframe6, width=25, relief=SUNKEN, bd=4)
        e3_butter.grid(row=1, column=3)
        e3_yoghurt = Entry(innerframe6, width=25, relief=SUNKEN, bd=4)
        e3_yoghurt.grid(row=2, column=3)
        e3_fresh_cream = Entry(innerframe6, width=25, relief=SUNKEN, bd=4)
        e3_fresh_cream.grid(row=3, column=3)
        e3_paneer = Entry(innerframe6, width=25, relief=SUNKEN, bd=4)
        e3_paneer.grid(row=4, column=3)

        try:
            con = sqlite3.connect('price.db')

            c1 = con.cursor()

            c1.execute("SELECT * FROM d3_dairy")
            insert_rice = c1.fetchall()
            insert = insert_rice[0]

            e3_cheese3_block.insert(0, insert[1])
            e3_butter.insert(0, insert[2])
            e3_yoghurt.insert(0, insert[3])
            e3_fresh_cream.insert(0, insert[4])
            e3_paneer.insert(0, insert[5])

            con.commit()

            con.close()
        except:
            pass

        try:
            con = sqlite3.connect('price.db')

            c1 = con.cursor()

            c1.execute("SELECT * FROM d_dairy")
            insert_rice = c1.fetchall()
            insert = insert_rice[0]

            e1_cheese1_block.insert(0, insert[1])
            e1_butter.insert(0, insert[2])
            e1_yoghurt.insert(0, insert[3])
            e1_fresh_cream.insert(0, insert[4])
            e1_paneer.insert(0, insert[5])

            con.commit()

            con.close()
        except:
            pass

        total2 = Button(innerframe6, text="OK", command=cal6, width=20, font=("times new roaman", 20, "bold"),
                        fg="#51361a", bg="#b4a284", relief=GROOVE, bd=9)
        total2.grid(row=5, column=0, columnspan=3, pady=15)

    def cal7():
        global v_tooth_paste
        global v_tooth_brush
        global v_bathing_soap
        global v_shampoo
        global v_face1_powder
        global v_hand_sanitizer
        global v_deodarant
        global v_shaving_cream
        global v_hair_gel
        global v_razer_blade

        v_tooth_paste = 0
        v_tooth_brush = 0
        v_bathing_soap = 0
        v_shampoo = 0
        v_face1_powder = 0
        v_hand_sanitizer = 0
        v_deodarant = 0
        v_shaving_cream = 0
        v_hair_gel = 0
        v_razer_blade = 0
        required_number = 0
        valid_number = 0

        global v3_tooth_paste
        global v3_tooth_brush
        global v3_bathing_soap
        global v3_shampoo
        global v3_face3_powder
        global v3_hand3_sanitizer
        global v3_deodarant
        global v3_shaving_cream
        global v3_hair_gel
        global v3_razer_blade

        v3_tooth_paste = 0
        v3_tooth_brush = 0
        v3_bathing_soap = 0
        v3_shampoo = 0
        v3_face3_powder = 0
        v3_hand3_sanitizer = 0
        v3_deodarant = 0
        v3_shaving_cream = 0
        v3_hair_gel = 0
        v3_razer_blade = 0
        required3_number = 0
        valid3_number = 0

        if e1_tooth_paste.get() == "" or e1_tooth_paste.get() == 0:
            required_number = 1
        else:
            try:
                v_tooth_paste = float(e1_tooth_paste.get())
            except:
                valid_number = 1

        if e1_tooth_brush.get() == "" or e1_tooth_brush.get() == 0:
            required_number = 1
        else:
            try:
                v_tooth_brush = float(e1_tooth_brush.get())
            except:
                valid_number = 1

        if e1_bathing_soap.get() == "" or e1_bathing_soap.get() == 0:
            required_number = 1
        else:
            try:
                v_bathing_soap = float(e1_bathing_soap.get())
            except:
                valid_number = 1

        if e1_shampoo.get() == "" or e1_shampoo.get() == 0:
            required_number = 1
        else:
            try:
                v_shampoo = float(e1_shampoo.get())
            except:
                valid_number = 1

        if e1_face1_powder.get() == "" or e1_face1_powder.get() == 0:
            required_number = 1
        else:
            try:
                v_face1_powder = float(e1_face1_powder.get())
            except:
                valid_number = 1

        if e1_hand_sanitizer.get() == "" or e1_hand_sanitizer.get() == 0:
            required_number = 1
        else:
            try:
                v_hand_sanitizer = float(e1_hand_sanitizer.get())
            except:
                valid_number = 1

        if e1_deodarant.get() == "" or e1_deodarant.get() == 0:
            required_number = 1
        else:
            try:
                v_deodarant = float(e1_deodarant.get())
            except:
                valid_number = 1

        if e1_shaving_cream.get() == "" or e1_shaving_cream.get() == 0:
            required_number = 1
        else:
            try:
                v_shaving_cream = float(e1_shaving_cream.get())
            except:
                valid_number = 1

        if e1_hair_gel.get() == "" or e1_hair_gel.get() == 0:
            required_number = 1
        else:
            try:
                v_hair_gel = float(e1_hair_gel.get())
            except:
                valid_number = 1

        if e1_razer_blade.get() == "" or e1_razer_blade.get() == 0:
            required_number = 1
        else:
            try:
                v_razer_blade = float(e1_razer_blade.get())
            except:
                valid_number = 1

        if required_number == 1:
            messagebox.showerror("REQUIRED FIELD", "ALL FIELDS ARE REQUIRED", parent=innerframe7)
        if valid_number == 1:
            messagebox.showerror("NUMBER", "PLEASE ENTER A VALID NUMBER", parent=innerframe7)

        if e3_tooth_paste.get() == "":
            pass
        else:
            try:
                v3_tooth_paste = float(e3_tooth_paste.get())
            except:
                valid3_number = 1

        if e3_tooth_brush.get() == "":
            pass
        else:
            try:
                v3_tooth_brush = float(e3_tooth_brush.get())
            except:
                valid3_number = 1

        if e3_bathing_soap.get() == "":
            pass
        else:
            try:
                v3_bathing_soap = float(e3_bathing_soap.get())
            except:
                valid3_number = 1

        if e3_shampoo.get() == "":
            pass
        else:
            try:
                v3_shampoo = float(e3_shampoo.get())
            except:
                valid3_number = 1

        if e3_face3_powder.get() == "":
            pass
        else:
            try:
                v3_face3_powder = float(e3_face3_powder.get())
            except:
                valid3_number = 1

        if e3_hand3_sanitizer.get() == "":
            pass
        else:
            try:
                v3_hand3_sanitizer = float(e3_hand3_sanitizer.get())
            except:
                valid3_number = 1

        if e3_deodarant.get() == "":
            pass
        else:
            try:
                v3_deodarant = float(e3_deodarant.get())
            except:
                valid3_number = 1

        if e3_shaving_cream.get() == "":
            pass
        else:
            try:
                v3_shaving_cream = float(e3_shaving_cream.get())
            except:
                valid3_number = 1

        if e3_hair_gel.get() == "":
            pass
        else:
            try:
                v3_hair_gel = float(e3_hair_gel.get())
            except:
                valid3_number = 1

        if e3_razer_blade.get() == "":
            pass
        else:
            try:
                v3_razer_blade = float(e3_razer_blade.get())
            except:
                valid3_number = 1

        if valid3_number == 1:
            messagebox.showerror("NUMBER", "PLEASE ENTER A VALID NUMBER", parent=innerframe7)

        con = sqlite3.connect('price.db')

        c1 = con.cursor()
        id = 1
        c1.execute("INSERT OR REPLACE into d3_toiletries VALUES (:id,:a, :b, :c, :d, :e, :f, :g, :h, :i,:j)",
                   {'id': id,
                    'a': float(v3_tooth_paste),
                    'b': float(v3_tooth_brush),
                    'c': float(v3_bathing_soap),
                    'd': float(v3_shampoo),
                    'e': float(v3_face3_powder),
                    'f': float(v3_hand3_sanitizer),
                    'g': float(v3_deodarant),
                    'h': float(v3_shaving_cream),
                    'i': float(v3_hair_gel),
                    'j': float(v3_razer_blade)
                    })

        con.commit()

        con.close()

        con = sqlite3.connect('price.db')

        c1 = con.cursor()
        id = 1
        c1.execute("INSERT OR REPLACE into d_toiletries VALUES (:id,:a, :b, :c, :d, :e, :f, :g, :h, :i,:j)",
                   {'id': id,
                    'a': float(v_tooth_paste),
                    'b': float(v_tooth_brush),
                    'c': float(v_bathing_soap),
                    'd': float(v_shampoo),
                    'e': float(v_face1_powder),
                    'f': float(v_hand_sanitizer),
                    'g': float(v_deodarant),
                    'h': float(v_shaving_cream),
                    'i': float(v_hair_gel),
                    'j': float(v_razer_blade)
                    })

        con.commit()

        con.close()

        innerframe7.destroy()

    def toiletrie():
        global innerframe7
        global e1_tooth_paste
        global e1_tooth_brush
        global e1_bathing_soap
        global e1_shampoo
        global e1_face1_powder
        global e1_hand_sanitizer
        global e1_deodarant
        global e1_shaving_cream
        global e1_hair_gel
        global e1_razer_blade

        global e3_tooth_paste
        global e3_tooth_brush
        global e3_bathing_soap
        global e3_shampoo
        global e3_face3_powder
        global e3_hand3_sanitizer
        global e3_deodarant
        global e3_shaving_cream
        global e3_hair_gel
        global e3_razer_blade

        innerframe7 = Toplevel(bg="#f6ead4", relief=GROOVE, bd=9)
        innerframe7.title("TOILETRIES")
        tooth_paste = Label(innerframe7, text="TOOTH PASTE ", font=("times new roman", 15, "bold"), fg="#51361a",
                            bg="#f6ead4")
        tooth_paste.grid(row=0, column=0)
        tooth_brush = Label(innerframe7, text="TOOTH BRUSH", font=("times new roman", 15, "bold"), fg="#51361a",
                            bg="#f6ead4")
        tooth_brush.grid(row=1, column=0)
        bathing_soap = Label(innerframe7, text="BATHING SOAP", font=("times new roman", 15, "bold"), fg="#51361a",
                             bg="#f6ead4")
        bathing_soap.grid(row=2, column=0)
        shampoo = Label(innerframe7, text="SHAMPOO", font=("times new roman", 15, "bold"), fg="#51361a",
                        bg="#f6ead4")
        shampoo.grid(row=3, column=0)
        face1_powder = Label(innerframe7, text="FACE POWDER", font=("times new roman", 15, "bold"), fg="#51361a",
                             bg="#f6ead4")
        face1_powder.grid(row=4, column=0)
        hand_sanitizer = Label(innerframe7, text="HAND SANITIZER", font=("times new roman", 15, "bold"), fg="#51361a",
                               bg="#f6ead4")
        hand_sanitizer.grid(row=5, column=0)
        deodarant = Label(innerframe7, text="DEODARANT", font=("times new roman", 15, "bold"), fg="#51361a",
                          bg="#f6ead4")
        deodarant.grid(row=6, column=0)
        shaving_cream = Label(innerframe7, text="SHAVING CREAM", font=("times new roman", 15, "bold"), fg="#51361a",
                              bg="#f6ead4")
        shaving_cream.grid(row=7, column=0)
        hair_gel = Label(innerframe7, text="HAIR GEL", font=("times new roman", 15, "bold"), fg="#51361a",
                         bg="#f6ead4")
        hair_gel.grid(row=8, column=0)
        razer_blade = Label(innerframe7, text="RAZER BLADE", font=("times new roman", 15, "bold"), fg="#51361a",
                            bg="#f6ead4")
        razer_blade.grid(row=9, column=0)

        e1_tooth_paste = Entry(innerframe7, width=25, relief=SUNKEN, bd=4)
        e1_tooth_paste.grid(row=0, column=2)
        e1_tooth_brush = Entry(innerframe7, width=25, relief=SUNKEN, bd=4)
        e1_tooth_brush.grid(row=1, column=2)
        e1_bathing_soap = Entry(innerframe7, width=25, relief=SUNKEN, bd=4)
        e1_bathing_soap.grid(row=2, column=2)
        e1_shampoo = Entry(innerframe7, width=25, relief=SUNKEN, bd=4)
        e1_shampoo.grid(row=3, column=2)
        e1_face1_powder = Entry(innerframe7, width=25, relief=SUNKEN, bd=4)
        e1_face1_powder.grid(row=4, column=2)
        e1_hand_sanitizer = Entry(innerframe7, width=25, relief=SUNKEN, bd=4)
        e1_hand_sanitizer.grid(row=5, column=2)
        e1_deodarant = Entry(innerframe7, width=25, relief=SUNKEN, bd=4)
        e1_deodarant.grid(row=6, column=2)
        e1_shaving_cream = Entry(innerframe7, width=25, relief=SUNKEN, bd=4)
        e1_shaving_cream.grid(row=7, column=2)
        e1_hair_gel = Entry(innerframe7, width=25, relief=SUNKEN, bd=4)
        e1_hair_gel.grid(row=8, column=2)
        e1_razer_blade = Entry(innerframe7, width=25, relief=SUNKEN, bd=4)
        e1_razer_blade.grid(row=9, column=2)

        e3_tooth_paste = Entry(innerframe7, width=25, relief=SUNKEN, bd=4)
        e3_tooth_paste.grid(row=0, column=3)
        e3_tooth_brush = Entry(innerframe7, width=25, relief=SUNKEN, bd=4)
        e3_tooth_brush.grid(row=1, column=3)
        e3_bathing_soap = Entry(innerframe7, width=25, relief=SUNKEN, bd=4)
        e3_bathing_soap.grid(row=2, column=3)
        e3_shampoo = Entry(innerframe7, width=25, relief=SUNKEN, bd=4)
        e3_shampoo.grid(row=3, column=3)
        e3_face3_powder = Entry(innerframe7, width=25, relief=SUNKEN, bd=4)
        e3_face3_powder.grid(row=4, column=3)
        e3_hand3_sanitizer = Entry(innerframe7, width=25, relief=SUNKEN, bd=4)
        e3_hand3_sanitizer.grid(row=5, column=3)
        e3_deodarant = Entry(innerframe7, width=25, relief=SUNKEN, bd=4)
        e3_deodarant.grid(row=6, column=3)
        e3_shaving_cream = Entry(innerframe7, width=25, relief=SUNKEN, bd=4)
        e3_shaving_cream.grid(row=7, column=3)
        e3_hair_gel = Entry(innerframe7, width=25, relief=SUNKEN, bd=4)
        e3_hair_gel.grid(row=8, column=3)
        e3_razer_blade = Entry(innerframe7, width=25, relief=SUNKEN, bd=4)
        e3_razer_blade.grid(row=9, column=3)

        try:
            con = sqlite3.connect('price.db')

            c1 = con.cursor()

            c1.execute("SELECT * FROM d3_toiletries")
            insert_rice = c1.fetchall()
            insert = insert_rice[0]

            e3_tooth_paste.insert(0, insert[1])
            e3_tooth_brush.insert(0, insert[2])
            e3_bathing_soap.insert(0, insert[3])
            e3_shampoo.insert(0, insert[4])
            e3_face3_powder.insert(0, insert[5])
            e3_hand3_sanitizer.insert(0, insert[6])
            e3_deodarant.insert(0, insert[7])
            e3_shaving_cream.insert(0, insert[8])
            e3_hair_gel.insert(0, insert[9])
            e3_razer_blade.insert(0, insert[10])

            con.commit()

            con.close()
        except:
            pass

        try:
            con = sqlite3.connect('price.db')

            c1 = con.cursor()

            c1.execute("SELECT * FROM d_toiletries")
            insert_rice = c1.fetchall()
            insert = insert_rice[0]

            e1_tooth_paste.insert(0, insert[1])
            e1_tooth_brush.insert(0, insert[2])
            e1_bathing_soap.insert(0, insert[3])
            e1_shampoo.insert(0, insert[4])
            e1_face1_powder.insert(0, insert[5])
            e1_hand_sanitizer.insert(0, insert[6])
            e1_deodarant.insert(0, insert[7])
            e1_shaving_cream.insert(0, insert[8])
            e1_hair_gel.insert(0, insert[9])
            e1_razer_blade.insert(0, insert[10])

            con.commit()

            con.close()
        except:
            pass

        total = Button(innerframe7, text="OK", command=cal7, width=20, font=("times new roaman", 20, "bold"),
                       fg="#51361a", bg="#b4a284", relief=GROOVE, bd=9)
        total.grid(row=10, column=0, columnspan=3, pady=15)

    def cal8():
        global v_dish_washing_soap
        global v_dish_washing_liquid
        global v_washing_powder
        global v_washing_soaps
        global v_bleaching_powder
        global v_sanitary_pad
        global v_toilet_paper
        global v_garbage1_bag
        global v_dettol
        global v_mosquito_liquid

        v_dish_washing_soap = 0
        v_dish_washing_liquid = 0
        v_washing_powder = 0
        v_washing_soaps = 0
        v_bleaching_powder = 0
        v_sanitary_pad = 0
        v_toilet_paper = 0
        v_garbage1_bag = 0
        v_dettol = 0
        v_mosquito_liquid = 0
        required_number = 0
        valid_number = 0

        global v3_dish_washing_soap
        global v3_dish_washing_liquid
        global v3_washing_powder
        global v3_washing_soaps
        global v3_bleaching_powder
        global v3_sanitary_pad
        global v3_toilet_paper
        global v3_garbage3_bag
        global v3_dettol
        global v3_mosquito_liquid

        v3_dish_washing_soap = 0
        v3_dish_washing_liquid = 0
        v3_washing_powder = 0
        v3_washing_soaps = 0
        v3_bleaching_powder = 0
        v3_sanitary_pad = 0
        v3_toilet_paper = 0
        v3_garbage3_bag = 0
        v3_dettol = 0
        v3_mosquito_liquid = 0
        required3_number = 0
        valid3_number = 0

        if e1_dish_washing_soap.get() == "" or e1_dish_washing_soap.get() == 0:
            required_number = 1
        else:
            try:
                v_dish_washing_soap = float(e1_dish_washing_soap.get())
            except:
                valid_number = 1

        if e1_dish_washing_liquid.get() == "" or e1_dish_washing_liquid.get() == 0:
            required_number = 1
        else:
            try:
                v_dish_washing_liquid = float(e1_dish_washing_liquid.get())
            except:
                valid_number = 1

        if e1_washing_powder.get() == "" or e1_washing_powder.get() == 0:
            required_number = 1
        else:
            try:
                v_washing_powder = float(e1_washing_powder.get())
            except:
                valid_number = 1

        if e1_washing_soaps.get() == "" or e1_washing_soaps.get() == 0:
            required_number = 1
        else:
            try:
                v_washing_soaps = float(e1_washing_soaps.get())
            except:
                valid_number = 1

        if e1_bleaching_powder.get() == "" or e1_bleaching_powder.get() == 0:
            required_number = 1
        else:
            try:
                v_bleaching_powder = float(e1_bleaching_powder.get())
            except:
                valid_number = 1

        if e1_sanitary_pad.get() == "" or e1_sanitary_pad.get() == 0:
            required_number = 1
        else:
            try:
                v_sanitary_pad = float(e1_sanitary_pad.get())
            except:
                valid_number = 1

        if e1_toilet_paper.get() == "" or e1_toilet_paper.get() == 0:
            required_number = 1
        else:
            try:
                v_toilet_paper = float(e1_toilet_paper.get())
            except:
                valid_number = 1

        if e1_garbage1_bag.get() == "" or e1_garbage1_bag.get() == 0:
            required_number = 1
        else:
            try:
                v_garbage1_bag = float(e1_garbage1_bag.get())
            except:
                valid_number = 1

        if e1_dettol.get() == "" or e1_dettol.get() == 0:
            required_number = 1
        else:
            try:
                v_dettol = float(e1_dettol.get())
            except:
                valid_number = 1

        if e1_mosquito_liquid.get() == "" or e1_mosquito_liquid.get() == 0:
            required_number = 1
        else:
            try:
                v_mosquito_liquid = float(e1_mosquito_liquid.get())
            except:
                valid_number = 1

        if required_number == 1:
            messagebox.showerror("REQUIRED FIELD", "ALL FIELDS ARE REQUIRED", parent=innerframe8)
        if valid_number == 1:
            messagebox.showerror("NUMBER", "PLEASE ENTER A VALID NUMBER", parent=innerframe8)

        if e3_dish_washing_soap.get() == "":
            pass
        else:
            try:
                v3_dish_washing_soap = float(e3_dish_washing_soap.get())
            except:
                valid3_number = 1

        if e3_dish_washing_liquid.get() == "":
            pass
        else:
            try:
                v3_dish_washing_liquid = float(e3_dish_washing_liquid.get())
            except:
                valid3_number = 1

        if e3_washing_powder.get() == "":
            pass
        else:
            try:
                v3_washing_powder = float(e3_washing_powder.get())
            except:
                valid3_number = 1

        if e3_washing_soaps.get() == "":
            pass
        else:
            try:
                v3_washing_soaps = float(e3_washing_soaps.get())
            except:
                valid3_number = 1

        if e3_bleaching_powder.get() == "":
            pass
        else:
            try:
                v3_bleaching_powder = float(e3_bleaching_powder.get())
            except:
                valid3_number = 1

        if e3_sanitary_pad.get() == "":
            pass
        else:
            try:
                v3_sanitary_pad = float(e3_sanitary_pad.get())
            except:
                valid3_number = 1

        if e3_toilet_paper.get() == "":
            pass
        else:
            try:
                v3_toilet_paper = float(e3_toilet_paper.get())
            except:
                valid3_number = 1

        if e3_garbage3_bag.get() == "":
            pass
        else:
            try:
                v3_garbage3_bag = float(e3_garbage3_bag.get())
            except:
                valid3_number = 1

        if e3_dettol.get() == "":
            pass
        else:
            try:
                v3_dettol = float(e3_dettol.get())
            except:
                valid3_number = 1

        if e3_mosquito_liquid.get() == "":
            pass
        else:
            try:
                v3_mosquito_liquid = float(e3_mosquito_liquid.get())
            except:
                valid3_number = 1

        if valid3_number == 1:
            messagebox.showerror("NUMBER", "PLEASE ENTER A VALID NUMBER", parent=innerframe8)

        con = sqlite3.connect('price.db')

        c1 = con.cursor()
        id = 1
        c1.execute("INSERT OR REPLACE into d3_clean VALUES (:id,:a, :b, :c, :d, :e, :f, :g, :h, :i,:j)",
                   {'id': id,
                    'a': float(v3_dish_washing_soap),
                    'b': float(v3_dish_washing_liquid),
                    'c': float(v3_washing_powder),
                    'd': float(v3_washing_soaps),
                    'e': float(v3_bleaching_powder),
                    'f': float(v3_sanitary_pad),
                    'g': float(v3_toilet_paper),
                    'h': float(v3_garbage3_bag),
                    'i': float(v3_dettol),
                    'j': float(v3_mosquito_liquid)
                    })

        con.commit()

        con.close()

        con = sqlite3.connect('price.db')

        c1 = con.cursor()
        id = 1
        c1.execute("INSERT OR REPLACE into d_clean VALUES (:id,:a, :b, :c, :d, :e, :f, :g, :h, :i,:j)",
                   {'id': id,
                    'a': float(v_dish_washing_soap),
                    'b': float(v_dish_washing_liquid),
                    'c': float(v_washing_powder),
                    'd': float(v_washing_soaps),
                    'e': float(v_bleaching_powder),
                    'f': float(v_sanitary_pad),
                    'g': float(v_toilet_paper),
                    'h': float(v_garbage1_bag),
                    'i': float(v_dettol),
                    'j': float(v_mosquito_liquid)
                    })

        con.commit()

        con.close()

        innerframe8.destroy()

    def clean():
        global innerframe8
        global e1_dish_washing_soap
        global e1_dish_washing_liquid
        global e1_washing_powder
        global e1_washing_soaps
        global e1_bleaching_powder
        global e1_sanitary_pad
        global e1_toilet_paper
        global e1_garbage1_bag
        global e1_dettol
        global e1_mosquito_liquid

        global e3_dish_washing_soap
        global e3_dish_washing_liquid
        global e3_washing_powder
        global e3_washing_soaps
        global e3_bleaching_powder
        global e3_sanitary_pad
        global e3_toilet_paper
        global e3_garbage3_bag
        global e3_dettol
        global e3_mosquito_liquid

        innerframe8 = Toplevel(bg="#f6ead4", relief=GROOVE, bd=9)
        innerframe8.title("CLEANING PRODUCTS")
        dish_washing_soap = Label(innerframe8, text="DISH WASHING SOAP", font=("times new roman", 15, "bold"),
                                  fg="#51361a",
                                  bg="#f6ead4")
        dish_washing_soap.grid(row=0, column=0)
        dish_washing_liquid = Label(innerframe8, text="DISH WASHING LIQUID", font=("times new roman", 15, "bold"),
                                    fg="#51361a",
                                    bg="#f6ead4")
        dish_washing_liquid.grid(row=1, column=0)
        washing_powder = Label(innerframe8, text="WASHING POWDER", font=("times new roman", 15, "bold"), fg="#51361a",
                               bg="#f6ead4")
        washing_powder.grid(row=2, column=0)
        washing_soaps = Label(innerframe8, text="WASHING SOAP", font=("times new roman", 15, "bold"), fg="#51361a",
                              bg="#f6ead4")
        washing_soaps.grid(row=3, column=0)
        bleaching_powder = Label(innerframe8, text="BLEACHING POWDER", font=("times new roman", 15, "bold"),
                                 fg="#51361a",
                                 bg="#f6ead4")
        bleaching_powder.grid(row=4, column=0)
        sanitary_pad = Label(innerframe8, text="SANITARY PAD", font=("times new roman", 15, "bold"), fg="#51361a",
                             bg="#f6ead4")
        sanitary_pad.grid(row=5, column=0)
        toilet_paper = Label(innerframe8, text="TOILET PAPER", font=("times new roman", 15, "bold"), fg="#51361a",
                             bg="#f6ead4")
        toilet_paper.grid(row=6, column=0)
        garbage1_bag = Label(innerframe8, text="GARBAGE BAG", font=("times new roman", 15, "bold"), fg="#51361a",
                             bg="#f6ead4")
        garbage1_bag.grid(row=7, column=0)
        dettol = Label(innerframe8, text="DETTOL", font=("times new roman", 15, "bold"), fg="#51361a",
                       bg="#f6ead4")
        dettol.grid(row=8, column=0)
        mosquito_liquid = Label(innerframe8, text="MOSQUITO LIQUID", font=("times new roman", 15, "bold"), fg="#51361a",
                                bg="#f6ead4")
        mosquito_liquid.grid(row=9, column=0)

        e1_dish_washing_soap = Entry(innerframe8, width=25, relief=SUNKEN, bd=4)
        e1_dish_washing_soap.grid(row=0, column=2)
        e1_dish_washing_liquid = Entry(innerframe8, width=25, relief=SUNKEN, bd=4)
        e1_dish_washing_liquid.grid(row=1, column=2)
        e1_washing_powder = Entry(innerframe8, width=25, relief=SUNKEN, bd=4)
        e1_washing_powder.grid(row=2, column=2)
        e1_washing_soaps = Entry(innerframe8, width=25, relief=SUNKEN, bd=4)
        e1_washing_soaps.grid(row=3, column=2)
        e1_bleaching_powder = Entry(innerframe8, width=25, relief=SUNKEN, bd=4)
        e1_bleaching_powder.grid(row=4, column=2)
        e1_sanitary_pad = Entry(innerframe8, width=25, relief=SUNKEN, bd=4)
        e1_sanitary_pad.grid(row=5, column=2)
        e1_toilet_paper = Entry(innerframe8, width=25, relief=SUNKEN, bd=4)
        e1_toilet_paper.grid(row=6, column=2)
        e1_garbage1_bag = Entry(innerframe8, width=25, relief=SUNKEN, bd=4)
        e1_garbage1_bag.grid(row=7, column=2)
        e1_dettol = Entry(innerframe8, width=25, relief=SUNKEN, bd=4)
        e1_dettol.grid(row=8, column=2)
        e1_mosquito_liquid = Entry(innerframe8, width=25, relief=SUNKEN, bd=4)
        e1_mosquito_liquid.grid(row=9, column=2)

        e3_dish_washing_soap = Entry(innerframe8, width=25, relief=SUNKEN, bd=4)
        e3_dish_washing_soap.grid(row=0, column=3)
        e3_dish_washing_liquid = Entry(innerframe8, width=25, relief=SUNKEN, bd=4)
        e3_dish_washing_liquid.grid(row=1, column=3)
        e3_washing_powder = Entry(innerframe8, width=25, relief=SUNKEN, bd=4)
        e3_washing_powder.grid(row=2, column=3)
        e3_washing_soaps = Entry(innerframe8, width=25, relief=SUNKEN, bd=4)
        e3_washing_soaps.grid(row=3, column=3)
        e3_bleaching_powder = Entry(innerframe8, width=25, relief=SUNKEN, bd=4)
        e3_bleaching_powder.grid(row=4, column=3)
        e3_sanitary_pad = Entry(innerframe8, width=25, relief=SUNKEN, bd=4)
        e3_sanitary_pad.grid(row=5, column=3)
        e3_toilet_paper = Entry(innerframe8, width=25, relief=SUNKEN, bd=4)
        e3_toilet_paper.grid(row=6, column=3)
        e3_garbage3_bag = Entry(innerframe8, width=25, relief=SUNKEN, bd=4)
        e3_garbage3_bag.grid(row=7, column=3)
        e3_dettol = Entry(innerframe8, width=25, relief=SUNKEN, bd=4)
        e3_dettol.grid(row=8, column=3)
        e3_mosquito_liquid = Entry(innerframe8, width=25, relief=SUNKEN, bd=4)
        e3_mosquito_liquid.grid(row=9, column=3)

        try:
            con = sqlite3.connect('price.db')

            c1 = con.cursor()

            c1.execute("SELECT * FROM d3_clean")
            insert_rice = c1.fetchall()
            insert = insert_rice[0]

            e3_dish_washing_soap.insert(0, insert[1])
            e3_dish_washing_liquid.insert(0, insert[2])
            e3_washing_powder.insert(0, insert[3])
            e3_washing_soaps.insert(0, insert[4])
            e3_bleaching_powder.insert(0, insert[5])
            e3_sanitary_pad.insert(0, insert[6])
            e3_toilet_paper.insert(0, insert[7])
            e3_garbage3_bag.insert(0, insert[8])
            e3_dettol.insert(0, insert[9])
            e3_mosquito_liquid.insert(0, insert[10])

            con.commit()

            con.close()
        except:
            pass

        try:
            con = sqlite3.connect('price.db')

            c1 = con.cursor()

            c1.execute("SELECT * FROM d_clean")
            insert_rice = c1.fetchall()
            insert = insert_rice[0]

            e1_dish_washing_soap.insert(0, insert[1])
            e1_dish_washing_liquid.insert(0, insert[2])
            e1_washing_powder.insert(0, insert[3])
            e1_washing_soaps.insert(0, insert[4])
            e1_bleaching_powder.insert(0, insert[5])
            e1_sanitary_pad.insert(0, insert[6])
            e1_toilet_paper.insert(0, insert[7])
            e1_garbage1_bag.insert(0, insert[8])
            e1_dettol.insert(0, insert[9])
            e1_mosquito_liquid.insert(0, insert[10])

            con.commit()

            con.close()
        except:
            pass

        total = Button(innerframe8, text="OK", command=cal8, width=20, font=("times new roaman", 20, "bold"),
                       fg="#51361a", bg="#b4a284", relief=GROOVE, bd=9)
        total.grid(row=10, column=0, columnspan=3, pady=15)

    def cal9():
        global v_bandages
        global v_light_bulbs
        global v_batteries
        global v_candles

        v_bandages = 0
        v_light_bulbs = 0
        v_batteries = 0
        v_candles = 0
        required_number = 0
        valid_number = 0

        global v3_bandages
        global v3_light_bulbs
        global v3_batteries
        global v3_candles

        v3_bandages = 0
        v3_light_bulbs = 0
        v3_batteries = 0
        v3_candles = 0
        required3_number = 0
        valid3_number = 0

        if e1_bandages.get() == "" or e1_bandages.get() == 0:
            required_number = 1
        else:
            try:
                v_bandages = float(e1_bandages.get())
            except:
                valid_number = 1

        if e1_light_bulbs.get() == "" or e1_light_bulbs.get() == 0:
            required_number = 1
        else:
            try:
                v_light_bulbs = float(e1_light_bulbs.get())
            except:
                valid_number = 1

        if e1_batteries.get() == "" or e1_batteries.get() == 0:
            required_number = 1
        else:
            try:
                v_batteries = float(e1_batteries.get())
            except:
                valid_number = 1

        if e1_candles.get() == "" or e1_candles.get() == 0:
            required_number = 1
        else:
            try:
                v_candles = float(e1_candles.get())
            except:
                valid_number = 1

        if required_number == 1:
            messagebox.showerror("REQUIRED FIELD", "ALL FIELDS ARE REQUIRED", parent=innerframe9)
        if valid_number == 1:
            messagebox.showerror("NUMBER", "PLEASE ENTER A VALID NUMBER", parent=innerframe9)

        if e3_bandages.get() == "":
            pass
        else:
            try:
                v3_bandages = float(e3_bandages.get())
            except:
                valid3_number = 1

        if e3_light_bulbs.get() == "":
            pass
        else:
            try:
                v3_light_bulbs = float(e3_light_bulbs.get())
            except:
                valid3_number = 1

        if e3_batteries.get() == "":
            pass
        else:
            try:
                v3_batteries = float(e3_batteries.get())
            except:
                valid3_number = 1

        if e3_candles.get() == "":
            pass
        else:
            try:
                v3_candles = float(e3_candles.get())
            except:
                valid3_number = 1

        if valid3_number == 1:
            messagebox.showerror("NUMBER", "PLEASE ENTER A VALID NUMBER", parent=innerframe9)

        con = sqlite3.connect('price.db')

        c1 = con.cursor()
        id = 1
        c1.execute("INSERT OR REPLACE into d3_mis VALUES (:id,:a, :b, :c, :d)",
                   {'id': id,
                    'a': float(v3_bandages),
                    'b': float(v3_light_bulbs),
                    'c': float(v3_batteries),
                    'd': float(v3_candles)
                    })

        con.commit()

        con.close()

        con = sqlite3.connect('price.db')

        c1 = con.cursor()
        id = 1
        c1.execute("INSERT OR REPLACE into d_mis VALUES (:id,:a, :b, :c, :d)",
                   {'id': id,
                    'a': float(v_bandages),
                    'b': float(v_light_bulbs),
                    'c': float(v_batteries),
                    'd': float(v_candles)
                    })

        con.commit()

        con.close()

        innerframe9.destroy()

    def miss():
        global e1_bandages
        global e1_light_bulbs
        global e1_batteries
        global e1_candles
        global innerframe9

        global e3_bandages
        global e3_light_bulbs
        global e3_batteries
        global e3_candles

        innerframe9 = Toplevel(bg="#f6ead4", relief=GROOVE, bd=9)
        innerframe9.title("MISCELLENEOUS")
        bandages = Label(innerframe9, text="BANDAGES", font=("times new roman", 15, "bold"), fg="#51361a",
                         bg="#f6ead4")
        bandages.grid(row=0, column=0)
        light_bulbs = Label(innerframe9, text="LIGHT BULB", font=("times new roman", 15, "bold"), fg="#51361a",
                            bg="#f6ead4")
        light_bulbs.grid(row=1, column=0)
        batteries = Label(innerframe9, text="BATTERIES", font=("times new roman", 15, "bold"), fg="#51361a",
                          bg="#f6ead4")
        batteries.grid(row=2, column=0)
        candles = Label(innerframe9, text="CANDLES", font=("times new roman", 15, "bold"), fg="#51361a",
                        bg="#f6ead4")
        candles.grid(row=3, column=0)

        e1_bandages = Entry(innerframe9, width=25, relief=SUNKEN, bd=4)
        e1_bandages.grid(row=0, column=2)
        e1_light_bulbs = Entry(innerframe9, width=25, relief=SUNKEN, bd=4)
        e1_light_bulbs.grid(row=1, column=2)
        e1_batteries = Entry(innerframe9, width=25, relief=SUNKEN, bd=4)
        e1_batteries.grid(row=2, column=2)
        e1_candles = Entry(innerframe9, width=25, relief=SUNKEN, bd=4)
        e1_candles.grid(row=3, column=2)

        e3_bandages = Entry(innerframe9, width=25, relief=SUNKEN, bd=4)
        e3_bandages.grid(row=0, column=3)
        e3_light_bulbs = Entry(innerframe9, width=25, relief=SUNKEN, bd=4)
        e3_light_bulbs.grid(row=1, column=3)
        e3_batteries = Entry(innerframe9, width=25, relief=SUNKEN, bd=4)
        e3_batteries.grid(row=2, column=3)
        e3_candles = Entry(innerframe9, width=25, relief=SUNKEN, bd=4)
        e3_candles.grid(row=3, column=3)

        try:
            con = sqlite3.connect('price.db')

            c1 = con.cursor()

            c1.execute("SELECT * FROM d3_mis")
            insert_rice = c1.fetchall()
            insert = insert_rice[0]

            e3_bandages.insert(0, insert[1])
            e3_light_bulbs.insert(0, insert[2])
            e3_batteries.insert(0, insert[3])
            e3_candles.insert(0, insert[4])

            con.commit()

            con.close()
        except:
            pass

        try:
            con = sqlite3.connect('price.db')

            c1 = con.cursor()

            c1.execute("SELECT * FROM d_mis")
            insert_rice = c1.fetchall()
            insert = insert_rice[0]

            e1_bandages.insert(0, insert[1])
            e1_light_bulbs.insert(0, insert[2])
            e1_batteries.insert(0, insert[3])
            e1_candles.insert(0, insert[4])

            con.commit()

            con.close()
        except:
            pass

        total2 = Button(innerframe9, text="OK", command=cal9, width=20, font=("times new roaman", 20, "bold"),
                        fg="#51361a", bg="#b4a284", relief=GROOVE, bd=9)
        total2.grid(row=4, column=0, columnspan=3, pady=15)

    def cal10():
        global v_papad
        global v_horlicks
        global v_complan
        global v_noodles
        global v_pasta
        global v_ketchup
        global v_jam
        global v_bread_delux
        global v_bread_britania

        v_papad = 0
        v_horlicks = 0
        v_complan = 0
        v_noodles = 0
        v_pasta = 0
        v_ketchup = 0
        v_jam = 0
        v_bread_delux = 0
        v_bread_britania = 0
        required_number = 0
        valid_number = 0

        global v3_papad
        global v3_horlicks
        global v3_complan
        global v3_noodles
        global v3_pasta
        global v3_ketchup
        global v3_jam
        global v3_bread3_delux
        global v3_bread3_britania

        v3_papad = 0
        v3_horlicks = 0
        v3_complan = 0
        v3_noodles = 0
        v3_pasta = 0
        v3_ketchup = 0
        v3_jam = 0
        v3_bread3_delux = 0
        v3_bread3_britania = 0
        required3_number = 0
        valid3_number = 0

        if e1_papad.get() == "" or e1_papad.get() == 0:
            required_number = 1
        else:
            try:
                v_papad = float(e1_papad.get())
            except:
                valid_number = 1

        if e1_horlicks.get() == "" or e1_horlicks.get() == 0:
            required_number = 1
        else:
            try:
                v_horlicks = float(e1_horlicks.get())
            except:
                valid_number = 1

        if e1_complan.get() == "" or e1_complan.get() == 0:
            required_number = 1
        else:
            try:
                v_complan = float(e1_complan.get())
            except:
                valid_number = 1

        if e1_noodles.get() == "" or e1_noodles.get() == 0:
            required_number = 1
        else:
            try:
                v_noodles = float(e1_noodles.get())
            except:
                valid_number = 1

        if e1_pasta.get() == "" or e1_pasta.get() == 0:
            required_number = 1
        else:
            try:
                v_pasta = float(e1_pasta.get())
            except:
                valid_number = 1

        if e1_ketchup.get() == "" or e1_ketchup.get() == 0:
            required_number = 1
        else:
            try:
                v_ketchup = float(e1_ketchup.get())
            except:
                valid_number = 1

        if e1_jam.get() == "" or e1_jam.get() == 0:
            required_number = 1
        else:
            try:
                v_jam = float(e1_jam.get())
            except:
                valid_number = 1

        if e1_bread_delux.get() == "" or e1_bread_delux.get() == 0:
            required_number = 1
        else:
            try:
                v_bread_delux = float(e1_bread_delux.get())
            except:
                valid_number = 1

        if e1_bread_britania.get() == "" or e1_bread_britania.get() == 0:
            required_number = 1
        else:
            try:
                v_bread_britania = float(e1_bread_britania.get())
            except:
                valid_number = 1

        if required_number == 1:
            messagebox.showerror("REQUIRED FIELD", "ALL FIELDS ARE REQUIRED", parent=innerframe10)
        if valid_number == 1:
            messagebox.showerror("NUMBER", "PLEASE ENTER A VALID NUMBER", parent=innerframe10)

        if e3_papad.get() == "":
            pass
        else:
            try:
                v3_papad = float(e3_papad.get())
            except:
                valid3_number = 1

        if e3_horlicks.get() == "":
            pass
        else:
            try:
                v3_horlicks = float(e3_horlicks.get())
            except:
                valid3_number = 1

        if e3_complan.get() == "":
            pass
        else:
            try:
                v3_complan = float(e3_complan.get())
            except:
                valid3_number = 1

        if e3_noodles.get() == "":
            pass
        else:
            try:
                v3_noodles = float(e3_noodles.get())
            except:
                valid3_number = 1

        if e3_pasta.get() == "":
            pass
        else:
            try:
                v3_pasta = float(e3_pasta.get())
            except:
                valid3_number = 1

        if e3_ketchup.get() == "":
            pass
        else:
            try:
                v3_ketchup = float(e3_ketchup.get())
            except:
                valid3_number = 1

        if e3_jam.get() == "":
            pass
        else:
            try:
                v3_jam = float(e3_jam.get())
            except:
                valid3_number = 1

        if e3_bread3_delux.get() == "":
            pass
        else:
            try:
                v3_bread3_delux = float(e3_bread3_delux.get())
            except:
                valid3_number = 1

        if e3_bread3_britania.get() == "":
            pass
        else:
            try:
                v3_bread3_britania = float(e3_bread3_britania.get())
            except:
                valid3_number = 1

        if valid3_number == 1:
            messagebox.showerror("NUMBER", "PLEASE ENTER A VALID NUMBER", parent=innerframe10)

        con = sqlite3.connect('price.db')

        c1 = con.cursor()
        id = 1
        c1.execute("INSERT OR REPLACE into d3_others VALUES (:id,:a, :b, :c, :d, :e, :f, :g, :h, :i)",
                   {'id': id,
                    'a': float(v3_papad),
                    'b': float(v3_horlicks),
                    'c': float(v3_complan),
                    'd': float(v3_noodles),
                    'e': float(v3_pasta),
                    'f': float(v3_ketchup),
                    'g': float(v3_jam),
                    'h': float(v3_bread3_delux),
                    'i': float(v3_bread3_britania)
                    })

        con.commit()

        con.close()

        con = sqlite3.connect('price.db')

        c1 = con.cursor()
        id = 1
        c1.execute("INSERT OR REPLACE into d_others VALUES (:id,:a, :b, :c, :d, :e, :f, :g, :h, :i)",
                   {'id': id,
                    'a': float(v_papad),
                    'b': float(v_horlicks),
                    'c': float(v_complan),
                    'd': float(v_noodles),
                    'e': float(v_pasta),
                    'f': float(v_ketchup),
                    'g': float(v_jam),
                    'h': float(v_bread_delux),
                    'i': float(v_bread_britania)
                    })

        con.commit()

        con.close()

        innerframe10.destroy()

    def others():
        global innerframe10
        global e1_papad
        global e1_horlicks
        global e1_complan
        global e1_noodles
        global e1_pasta
        global e1_ketchup
        global e1_jam
        global e1_bread_delux
        global e1_bread_britania

        global e3_papad
        global e3_horlicks
        global e3_complan
        global e3_noodles
        global e3_pasta
        global e3_ketchup
        global e3_jam
        global e3_bread3_delux
        global e3_bread3_britania

        innerframe10 = Toplevel(bg="#f6ead4", relief=GROOVE, bd=9)
        innerframe10.title("OTHERS")
        papad = Label(innerframe10, text="PAPAD", font=("times new roman", 15, "bold"), fg="#51361a",
                      bg="#f6ead4")
        papad.grid(row=0, column=0)
        horlicks = Label(innerframe10, text="HORLICKS", font=("times new roman", 15, "bold"), fg="#51361a",
                         bg="#f6ead4")
        horlicks.grid(row=1, column=0)
        complan = Label(innerframe10, text="COMPLAN", font=("times new roman", 15, "bold"), fg="#51361a",
                        bg="#f6ead4")
        complan.grid(row=2, column=0)
        noodles = Label(innerframe10, text="NOODLES", font=("times new roman", 15, "bold"), fg="#51361a",
                        bg="#f6ead4")
        noodles.grid(row=3, column=0)
        pasta = Label(innerframe10, text="PASTA", font=("times new roman", 15, "bold"), fg="#51361a",
                      bg="#f6ead4")
        pasta.grid(row=4, column=0)
        ketchup = Label(innerframe10, text="KETCHUP", font=("times new roman", 15, "bold"), fg="#51361a",
                        bg="#f6ead4")
        ketchup.grid(row=5, column=0)
        jam = Label(innerframe10, text="JAM", font=("times new roman", 15, "bold"), fg="#51361a",
                    bg="#f6ead4")
        jam.grid(row=6, column=0)
        bread_delux = Label(innerframe10, text="BREAD DELUX", font=("times new roman", 15, "bold"), fg="#51361a",
                            bg="#f6ead4")
        bread_delux.grid(row=7, column=0)
        bread_britania = Label(innerframe10, text="BREAD BRITANIA", font=("times new roman", 15, "bold"), fg="#51361a",
                               bg="#f6ead4")
        bread_britania.grid(row=8, column=0)

        e1_papad = Entry(innerframe10, width=25, relief=SUNKEN, bd=4)
        e1_papad.grid(row=0, column=2)
        e1_horlicks = Entry(innerframe10, width=25, relief=SUNKEN, bd=4)
        e1_horlicks.grid(row=1, column=2)
        e1_complan = Entry(innerframe10, width=25, relief=SUNKEN, bd=4)
        e1_complan.grid(row=2, column=2)
        e1_noodles = Entry(innerframe10, width=25, relief=SUNKEN, bd=4)
        e1_noodles.grid(row=3, column=2)
        e1_pasta = Entry(innerframe10, width=25, relief=SUNKEN, bd=4)
        e1_pasta.grid(row=4, column=2)
        e1_ketchup = Entry(innerframe10, width=25, relief=SUNKEN, bd=4)
        e1_ketchup.grid(row=5, column=2)
        e1_jam = Entry(innerframe10, width=25, relief=SUNKEN, bd=4)
        e1_jam.grid(row=6, column=2)
        e1_bread_delux = Entry(innerframe10, width=25, relief=SUNKEN, bd=4)
        e1_bread_delux.grid(row=7, column=2)
        e1_bread_britania = Entry(innerframe10, width=25, relief=SUNKEN, bd=4)
        e1_bread_britania.grid(row=8, column=2)

        e3_papad = Entry(innerframe10, width=25, relief=SUNKEN, bd=4)
        e3_papad.grid(row=0, column=3)
        e3_horlicks = Entry(innerframe10, width=25, relief=SUNKEN, bd=4)
        e3_horlicks.grid(row=1, column=3)
        e3_complan = Entry(innerframe10, width=25, relief=SUNKEN, bd=4)
        e3_complan.grid(row=2, column=3)
        e3_noodles = Entry(innerframe10, width=25, relief=SUNKEN, bd=4)
        e3_noodles.grid(row=3, column=3)
        e3_pasta = Entry(innerframe10, width=25, relief=SUNKEN, bd=4)
        e3_pasta.grid(row=4, column=3)
        e3_ketchup = Entry(innerframe10, width=25, relief=SUNKEN, bd=4)
        e3_ketchup.grid(row=5, column=3)
        e3_jam = Entry(innerframe10, width=25, relief=SUNKEN, bd=4)
        e3_jam.grid(row=6, column=3)
        e3_bread3_delux = Entry(innerframe10, width=25, relief=SUNKEN, bd=4)
        e3_bread3_delux.grid(row=7, column=3)
        e3_bread3_britania = Entry(innerframe10, width=25, relief=SUNKEN, bd=4)
        e3_bread3_britania.grid(row=8, column=3)

        try:
            con = sqlite3.connect('price.db')

            c1 = con.cursor()

            c1.execute("SELECT * FROM d3_others")
            insert_rice = c1.fetchall()
            insert = insert_rice[0]

            e3_papad.insert(0, insert[1])
            e3_horlicks.insert(0, insert[2])
            e3_complan.insert(0, insert[3])
            e3_noodles.insert(0, insert[4])
            e3_pasta.insert(0, insert[5])
            e3_ketchup.insert(0, insert[6])
            e3_jam.insert(0, insert[7])
            e3_bread3_delux.insert(0, insert[8])
            e3_bread3_britania.insert(0, insert[9])

            con.commit()

            con.close()
        except:
            pass

        try:
            con = sqlite3.connect('price.db')

            c1 = con.cursor()

            c1.execute("SELECT * FROM d_others")
            insert_rice = c1.fetchall()
            insert = insert_rice[0]

            e1_papad.insert(0, insert[1])
            e1_horlicks.insert(0, insert[2])
            e1_complan.insert(0, insert[3])
            e1_noodles.insert(0, insert[4])
            e1_pasta.insert(0, insert[5])
            e1_ketchup.insert(0, insert[6])
            e1_jam.insert(0, insert[7])
            e1_bread_delux.insert(0, insert[8])
            e1_bread_britania.insert(0, insert[9])

            con.commit()

            con.close()
        except:
            pass

        total = Button(innerframe10, text="OK", command=cal10, width=20, font=("times new roaman", 20, "bold"),
                       fg="#51361a", bg="#b4a284", relief=GROOVE, bd=9)
        total.grid(row=9, column=0, columnspan=3, pady=15)

    rice_img = ImageTk.PhotoImage(file="image/rice.PNG",master=frame1)
    pulse_img = ImageTk.PhotoImage(file="image/pulses.PNG",master=frame1)
    spice_img = ImageTk.PhotoImage(file="image/spices.PNG",master=frame1)
    oil_img = ImageTk.PhotoImage(file="image/oils.PNG",master=frame1)
    nut_img = ImageTk.PhotoImage(file="image/nuts.PNG",master=frame1)
    dairy_img = ImageTk.PhotoImage(file="image/dairy.PNG",master=frame1)
    toi_img = ImageTk.PhotoImage(file="image/toi.PNG",master=frame1)
    clean_img = ImageTk.PhotoImage(file="image/clean.PNG",master=frame1)
    mis_img = ImageTk.PhotoImage(file="image/mis.PNG",master=frame1)

    rice1_flour = Button(frame1, text="RICE AND FLOURS", image=rice_img, relief=GROOVE, bd=9, width=20,
                         font=("times new roaman", 20, "bold"), fg="#51361a", bg="#b4a284", command=rice)
    rice1_flour.place(x=175, y=10, width=300, height=80)
    pulses_dal = Button(frame1, text="PULSES/DAL", width=20, image=pulse_img, font=("times new roaman", 20, "bold"),
                        fg="#51361a",
                        bg="#b4a284", command=pulses, relief=GROOVE, bd=9)
    pulses_dal.place(x=650, y=10, width=300, height=80)
    spice = Button(frame1, text="SPICE POWDER", width=20, image=spice_img, font=("times new roaman", 20, "bold"),
                   fg="#51361a",
                   bg="#b4a284", command=spices, relief=GROOVE, bd=9)
    spice.place(x=175, y=100, width=300, height=80)
    oils = Button(frame1, text="OILS", width=20, image=oil_img, font=("times new roaman", 20, "bold"), fg="#51361a",
                  bg="#b4a284",
                  command=oil, relief=GROOVE, bd=9)
    oils.place(x=650, y=100, width=300, height=80)
    spice1_nuts = Button(frame1, text="SPICES AND NUTS", image=nut_img, width=20, font=("times new roaman", 20, "bold"),
                         fg="#51361a",
                         bg="#b4a284", command=spice1_nut, relief=GROOVE, bd=9)
    spice1_nuts.place(x=175, y=190, width=300, height=80)
    dairy = Button(frame1, text="DAIRY PRODUCTS", width=20, image=dairy_img, command=dairy,
                   font=("times new roaman", 20, "bold"),
                   fg="#51361a", bg="#b4a284", relief=GROOVE, bd=9)
    dairy.place(x=650, y=190, width=300, height=80)
    toiletries = Button(frame1, text="TOILETRIES", width=20, image=toi_img, command=toiletrie,
                        font=("times new roaman", 20, "bold"),
                        fg="#51361a", bg="#b4a284", relief=GROOVE, bd=9)
    toiletries.place(x=175, y=280, width=300, height=80)
    cleaning = Button(frame1, text="CLEANING PRODUCTS", width=20, image=clean_img, command=clean,
                      font=("times new roaman", 20, "bold"),
                      fg="#51361a", bg="#b4a284", relief=GROOVE, bd=9)
    cleaning.place(x=650, y=280, width=300, height=80)
    miscellaneous = Button(frame1, text="MISCELLANEOUS", width=20, image=mis_img, command=miss,
                           font=("times new roaman", 20, "bold"),
                           fg="#51361a", bg="#b4a284", relief=GROOVE, bd=9)
    miscellaneous.place(x=175, y=370, width=300, height=80)
    other = Button(frame1, text="OTHER INGREDIENTS", width=20, command=others, font=("times new roaman", 18, "bold"),
                   fg="#51361a", bg="white", relief=GROOVE, bd=9)
    other.place(x=650, y=370, width=300, height=80)

    root1.mainloop()
