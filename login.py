import sqlite3
from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox
from admin import admin
from tp import finction


root = Tk()
root.title("GROCEMART")
root.geometry("1199x600+35+52")
root.resizable(False, False)
# creating a root frame
r_frame = Frame(root, bg="#000000", relief=GROOVE, bd=10)
r_frame.place(x=0, y=0, height=600, width=1199)

# creating a variable to hold background image
back_img = ImageTk.PhotoImage(file="neww.jpg")

my_label = Label(r_frame, image=back_img)
my_label.place(x=0, y=0, relwidth=1, relheight=1)

#  creating a frame for login
r1_frame = Frame(r_frame, bg="#f6ead4", relief=GROOVE, highlightbackground="black", highlightcolor="black", highlightthickness=2)
r1_frame.place(x=390, y=200, height=390, width=470)
# frame for grocemart text
r2_frame = Frame(r_frame, bg="#7F462C", relief=GROOVE, highlightbackground="black", highlightcolor="black", highlightthickness=1, bd=9)
r2_frame.place(x=130, y=35, height=150, width=950)

canvas = Canvas(r2_frame)
canvas.place(x=-1, y=0, height=128, width=930)
canvas.create_image(0, 0, image=back_img, anchor="nw")

grocemart_text = canvas.create_text(480, 70, text="GROCEMART", font=("Impact", 100, "bold"), fill="#51361a")

#my_label = Label(r2_frame, text="GROCEMART", font=("Impact", 100, "bold"), fg="#d77337", bg="white")
#my_label.grid(row=0, column=0, padx=160)




try:
    # Creating a database
    conn = sqlite3.connect('register.db')
    # Create a  cursor
    c = conn.cursor()

    # creating a table
    c.execute(""" CREATE TABLE employee(
                first_name text,
                last_name text,
                user_name text,
                password text,
                address text,
                contact_no integer)""")

    # commit changes
    conn.commit()
    # close connection
    conn.close()
except:
    pass

def bill():
    return


def login():
    # Creating a database
    conn = sqlite3.connect('register.db')
    # Create a  cursor
    c = conn.cursor()

    c.execute("SELECT user_name,password FROM employee ")
    details = c.fetchall()
    # temp = ""
    # temp2 = ""
    flag = 1
    if l_entry.get() == "" and p_entry.get() == "":
        messagebox.showerror("ERROR", "ALL FIELDS ARE REQUIRED", parent=root)
    else:
        for detail in details:

            # temp = str(temp) + str(detail[1])
            # temp2 = str(temp2) + str(detail[0])

            if detail[0] == l_entry.get() and detail[1] == p_entry.get():
                flag = 0

                # eek1 = Label(r_frame, text="loginnn")
                # eek1.grid(row=9, column=0, padx=10, pady=10)
                break

            '''
                eek3 = Label(r_frame, text="wrong")
                eek3.grid(row=9, column=0, padx=10, pady=10)
            '''
        if flag == 0:
            # closing login frame
            r1_frame.destroy()
            messagebox.showinfo("WELCOME", "LOGGED IN SUCCESFULLY", parent=root)
            # craeting frame for home window
            #r3_frame = Frame(r_frame, bg="white")
            #r3_frame.place(x=390, y=200, height=390, width=470)

            b_admin = Button(r_frame, text="admin", width=20, cursor="hand2", font=("times new roman", 20, "bold"),
                              fg="#51361a", bg="#b4a284", relief=GROOVE,highlightbackground="black", highlightcolor="black", highlightthickness=2, bd=9,command=admin)
            b_admin.place(x=450, y=270)
            #b_whatsapp = Button(r_frame, text="whatsapp", width=20, cursor="hand2", font=("times new roman", 20, "bold"),
             #fg = "#51361a", bg = "#b4a284", relief=GROOVE,highlightbackground="black", highlightcolor="black", highlightthickness=2, bd=9)
            #b_whatsapp.place(x=450, y=370)
            b_bill = Button(r_frame, text="generate bill", width=20, cursor="hand2", font=("times new roman", 20, "bold"),
             fg = "#51361a", bg = "#b4a284", command=finction, relief=GROOVE,highlightbackground="black", highlightcolor="black", highlightthickness=2, bd=9)
            b_bill.place(x=450, y=370)


        else:
            messagebox.showerror("ERROR", "INVALID USERNAME OR PASSWORD", parent=root)

    '''
    eek4 = Label(r_frame, text=temp2)
    eek4.grid(row=7, column=0, padx=10, pady=10)
    eek41 = Label(r_frame, text=temp)
    eek41.grid(row=8, column=0, padx=10, pady=10)
    eek42 = Label(r_frame, text=l_entry.get())
    eek42.grid(row=10, column=0, padx=10, pady=10)
    eek43 = Label(r_frame, text=p_entry.get())
    eek43.grid(row=11, column=0, padx=10, pady=10)
    '''

    # commit changes
    conn.commit()
    # close connection
    conn.close()


def submit():
    char = ["'", ' " ', "!", "#", "$", "%", "^", "&", "*", ":", ";", ","]
    tempp = 0
    itemp = 0
    new_temp = 0
    if first_name.get() == "":
        tempp = 1
    if last_name.get() == "":
        tempp = 1
    if contact_no.get() == "":
        tempp = 1
    if address.get() == "":
        tempp = 1
    if user_name.get() == "":
        temmp = 1
    if password.get == "":
        temmp = 1
    try:
        number = int(contact_no.get())
        i = len(str(number))
        if i != 10:
            new_temp = 1
    except:
        new_temp = 1

    for i in char:
        if i in user_name.get():
            itemp = 1
        if i in password.get():
            itemp = 1

    if tempp == 1:
        messagebox.showerror("ERROR", "All fields are required", parent=root)
    elif itemp == 1:
        messagebox.showerror("ERROR", "CHARCTERS NOT ALLOWDED")
    elif new_temp == 1:
        messagebox.showerror("ERROR", "PLease enter contact number correctly")
    else:
        # Creating a database
        conn = sqlite3.connect('register.db')
        # Create a  cursor
        c = conn.cursor()

        c.execute("INSERT INTO employee VALUES (:a, :b, :c, :d, :e, :f)",
                  {
                      'a': first_name.get(),
                      'b': last_name.get(),
                      'c': user_name.get(),
                      'd': password.get(),
                      'e': address.get(),
                      'f': contact_no.get()
                  })

        first_name.delete(0, END)
        last_name.delete(0, END)
        user_name.delete(0, END)
        password.delete(0, END)
        address.delete(0, END)
        contact_no.delete(0, END)

        # commit changes
        conn.commit()
        # close connection
        conn.close()

        success = Label(r1_frame, text="  Registration Successful ! please login", font=("Goudy old style", 15, "bold"),
                        fg="#d25d17", bg="white")
        success.grid(row=5, column=0, padx=(20, 0), pady=(5, 10), columnspan=2)

    # close new window
    r_new.destroy()


def register():
    global r_new
    global first_name
    global last_name
    global user_name
    global password
    global address
    global contact_no

    r_new = Toplevel(bg="#f6ead4")
    f_name = Label(r_new, text="First Name", font=("Goudy old style", 15, "bold"), fg="#51361a", bg="#f6ead4")
    f_name.grid(row=0, column=0, padx=10, pady=10)
    l_name = Label(r_new, text="Last Name", font=("Goudy old style", 15, "bold"), fg="#51361a", bg="#f6ead4")
    l_name.grid(row=1, column=0, padx=10, pady=10)
    u_name = Label(r_new, text="USER NAME", font=("Goudy old style", 15, "bold"),fg="#51361a", bg="#f6ead4")
    u_name.grid(row=2, column=0, padx=10, pady=10)
    passs = Label(r_new, text="PASSWORD", font=("Goudy old style", 15, "bold"), fg="#51361a", bg="#f6ead4")
    passs.grid(row=3, column=0, padx=10, pady=10)
    adds = Label(r_new, text="Address", font=("Goudy old style", 15, "bold"),fg="#51361a", bg="#f6ead4")
    adds.grid(row=4, column=0, padx=10, pady=10)
    c_no = Label(r_new, text="Contact number", font=("Goudy old style", 15, "bold"), fg="#51361a", bg="#f6ead4")
    c_no.grid(row=5, column=0, padx=10, pady=10)

    first_name = Entry(r_new, width=50, borderwidth=5, font=("times new roman", 15), bg="lightgray")
    first_name.grid(row=0, column=1)
    last_name = Entry(r_new, width=50, borderwidth=5, font=("times new roman", 15), bg="lightgray")
    last_name.grid(row=1, column=1)
    user_name = Entry(r_new, width=50, borderwidth=5, font=("times new roman", 15), bg="lightgray")
    user_name.grid(row=2, column=1)
    password = Entry(r_new, width=50, borderwidth=5, show="*", font=("times new roman", 15), bg="lightgray")
    password.grid(row=3, column=1)
    address = Entry(r_new, width=50, borderwidth=5, font=("times new roman", 15), bg="lightgray")
    address.grid(row=4, column=1)
    contact_no = Entry(r_new, width=50, borderwidth=5, font=("times new roman", 15), bg="lightgray")
    contact_no.grid(row=5, column=1)

    sub_bn = Button(r_new, text="REGISTER", bd=1, cursor="hand2", command=submit, width=15,
                    font=("times new roman", 20, "bold"),fg="#51361a", bg="#b4a284")
    sub_bn.grid(row=6, column=0, padx=(20, 0), columnspan=2)


t_label = Label(r1_frame, text="LOGIN HERE", font=("Impact", 30, "bold"), fg="#51361a", bg="#f6ead4")
t_label.grid(row=0, column=0, columnspan=2, padx=(40, 0), pady=0)

description = Label(r1_frame, text="Employee Login Here!", font=("Goudy old style", 15, "bold"), fg="#51361a",
                    bg="#f6ead4")
description.grid(row=1, column=0, columnspan=2, padx=10, pady=5)

l_label = Label(r1_frame, text="LOGIN", font=("Goudy old style", 15, "bold"), fg="#51361a", bg="#f6ead4")
l_label.grid(row=2, column=0, padx=10, pady=10)

p_label = Label(r1_frame, text="PASSWORD", font=("Goudy old style", 15, "bold"), fg="#51361a", bg="#f6ead4")
p_label.grid(row=3, column=0, padx=10, pady=10)

l_entry = Entry(r1_frame, width=30, relief=SUNKEN, bd=4, font=("times new roman", 15), bg="white")
l_entry.grid(row=2, column=1, pady=10)

p_entry = Entry(r1_frame, width=30, relief=SUNKEN, bd=4, text="password", show="*", font=("times new roman", 15), bg="white")
p_entry.grid(row=3, column=1, pady=10)

l_button = Button(r1_frame, text=" LOGIN ", width=10, command=login, cursor="hand2",
                  font=("times new roman", 20, "bold"), fg="#51361a", bg="#b4a284", relief=GROOVE, bd=9)
l_button.grid(row=4, column=0, columnspan=2, padx=(20, 0), pady=(5, 3))

r_label = Label(r1_frame, text="new user, click to register! ", font=("Goudy old style", 15, "bold"), fg="#51361a",
                bg="#f6ead4")
r_label.grid(row=5, column=0, pady=(0, 10), columnspan=2)

r_button = Button(r1_frame, text=" REGISTER ", width=15, command=register, cursor="hand2",
                  font=("times new roman", 15, "bold"), fg="#51361a", bg="#b4a284", relief=GROOVE, bd=9)
r_button.grid(row=6, column=0, columnspan=2, padx=(20, 0), pady=(0, 3))

root.mainloop()
