from tkinter import *
from tkinter import messagebox
from tkinter.ttk import Combobox
import sqlite3 as sql

con = sql.connect(database="studentdb.sqlite")
cursor = con.cursor()
try:
    cursor.execute("create table students(stu_id int,stu_name text, stu_mob text,stu_course text,reg_fee int,bal int)")
    cursor.execute("create table course(course_name text ,course_fee int)")
    con.commit()
except Exception as e:
    print(e)
con.close()

win = Tk()
win.state('zoomed')
win.resizable(width=False, height=False)
header_fem = Frame(win)
header_fem.configure(bg='light pink')
header_fem.place(x=0, y=0, relwidth=1, relheight=0.2)

title_lbl = Label(header_fem, text='Student Management System', bg='light pink',
                  font=('courier', 50, 'bold', 'underline'))
title_lbl.pack()


def main_body():
    def reset():
        user_entry.delete(0, "end")
        Pass_entry.delete(0, "end")
        user_entry.focus()

    def login():
        u = user_entry.get()
        p = Pass_entry.get()
        if len(u) == 0 or len(p) == 0:
            messagebox.showwarning('validation', "UserName/Password Can't Be Empty")
        else:
            if u == "admin" or p == "admin":
                frm.destroy()
                login_body()
            else:
                messagebox.showerror('validation', "Invalid UserName/Password")

    frm = Frame(win)
    frm.configure(bg='light blue')
    frm.place(x=0, rely=0.2, relwidth=1, relheight=0.8)

    user_lbl = Label(frm, text='UserName', bg='light blue', font=('Comic Sans MS', 20, 'bold'))
    user_lbl.place(relx=0.3, rely=0.2)

    user_entry = Entry(frm, font=('', 20, 'bold'), bd=7)
    user_entry.focus()
    user_entry.place(relx=0.45, rely=0.2)

    Pass_lbl = Label(frm, text='Password', bg='light blue', font=('Comic Sans MS', 20, 'bold'))
    Pass_lbl.place(relx=0.3, rely=0.35)

    Pass_entry = Entry(frm, font=('', 20, 'bold'), bd=7, show='*')
    Pass_entry.place(relx=0.45, rely=0.35)

    log_btn = Button(frm, text='LogIn', font=('Comic Sans MS', 20, 'bold'), bd=7, command=login)
    log_btn.place(relx=0.4, rely=0.5)

    Reset_btn = Button(frm, text='Reset', font=('Comic Sans MS', 20, 'bold'), bd=7, command=reset)
    Reset_btn.place(relx=0.55, rely=0.5)


def login_body():
    def logout():
        frm.destroy()
        main_body()

    def register():
        frm.destroy()
        register_student_body()

    def find():
        frm.destroy()
        find_student_body()

    def deposit():
        frm.destroy()
        deposit_fee_body()

    def add():
        frm.destroy()
        add_course_body()

    def update():
        frm.destroy()
        update_course_body()

    frm = Frame(win)
    frm.configure(bg='light blue')
    frm.place(x=0, rely=0.2, relwidth=1, relheight=0.8)

    wel_lbl = Label(frm, text="Welcome Prakash", font=('Comic Sans MS', 15, 'bold'), bg='light blue')
    wel_lbl.place(relx=0, rely=0)

    log_btn = Button(frm, text="LogOut", font=('Comic Sans MS', 18, 'bold'), bd=7, command=logout)
    log_btn.place(relx=0.90, rely=0)

    register_btn = Button(frm, text="Register Student", font=('Comic Sans MS', 18, 'bold'), bd=7, width=15,
                          command=register)
    register_btn.place(relx=0.45, rely=.05)

    find_btn = Button(frm, text="Find Student", font=('Comic Sans MS', 18, 'bold'), bd=7, width=15, command=find)
    find_btn.place(relx=0.45, rely=.25)

    dep_btn = Button(frm, text="Deposit Fee", font=('Comic Sans MS', 18, 'bold'), bd=7, width=15, command=deposit)
    dep_btn.place(relx=0.45, rely=.45)

    cour_btn = Button(frm, text="Add Course", font=('Comic Sans MS', 18, 'bold'), bd=7, width=15, command=add)
    cour_btn.place(relx=0.45, rely=.65)

    upd_cors_btn = Button(frm, text="Update Course", font=('Comic Sans MS', 18, 'bold'), bd=7, width=15, command=update)
    upd_cors_btn.place(relx=0.45, rely=.85)


def register_student_body():
    def logout():
        frm.destroy()
        main_body()

    def home():
        frm.destroy()
        login_body()

    def register_student_db():
        id = id_entry.get()
        name = name_entry.get()
        mob = mobile_entry.get()
        cour_se = course_list.get()
        fee = fee_entry.get()
        course, course_fee = cour_se.split()

        con = sql.connect(database="studentdb.sqlite")
        cursor = con.cursor()
        if len(name) <= 0:
            messagebox.showwarning('validation', "Student Name not be Empty")
        elif len(mob) < 10:
            messagebox.showwarning('validation', "Mobile number should be 10 digit")
        elif int(fee) <= 0 or int(fee) > int(course_fee):
            messagebox.showwarning('validation', f"Fee must be between 1 to {course_fee}")
        else:
            try:
                cursor.execute("insert into students values(?,?,?,?,?,?)",(id, name, mob, course, fee, (int(course_fee) - int(fee))))
                con.commit()
                messagebox.showinfo('Comic Sans MS', 'Registration Successful')
            except Exception as e:
                messagebox.showerror('validation', str(e))
            con.close()
            frm.destroy()
            register_student_body()

    frm = Frame(win)
    frm.configure(bg='light blue')
    frm.place(x=0, rely=0.2, relwidth=1, relheight=0.8)

    wel_lbl = Label(frm, text="Welcome Prakash", font=('Comic Sans MS', 15, 'bold'), bg='light blue')
    wel_lbl.place(relx=0, rely=0)

    log_btn = Button(frm, text="LogOut", font=('Comic Sans MS', 18, 'bold'), bd=7, command=logout)
    log_btn.place(relx=0.90, rely=0)

    home_btn = Button(frm, text="Home", font=('Comic Sans MS', 18, 'bold'), bd=7, command=home)
    home_btn.place(relx=0.80, rely=0)

    con = sql.connect(database="studentdb.sqlite")
    cursor = con.cursor()
    cursor.execute("select max(stu_id) from students ")
    max_id = cursor.fetchone()
    if max_id[0] == None:
        stu_id_db = 1
    else:
        stu_id_db = max_id[0] + 1
    con.close()

    student_id = Label(frm, text='Student Id', bg='light blue', font=('', 20, 'bold'))
    student_id.place(relx=0.3, rely=0.01)

    id_entry = Entry(frm, font=('Comic Sans MS', 20), bd=7)
    id_entry.insert(0, str(stu_id_db))
    id_entry.place(relx=0.5, rely=0.01)
    id_entry.configure(state='disabled')

    student_name = Label(frm, text='Student Name', bg='light blue', font=('Comic Sans MS', 20, 'bold'))
    student_name.place(relx=0.3, rely=0.15)

    name_entry = Entry(frm, font=('Comic Sans MS', 20), bd=7)
    name_entry.focus()
    name_entry.place(relx=0.5, rely=0.15)

    mobile_lbl = Label(frm, text='Student Mobile', bg='light blue', font=('Comic Sans MS', 20, 'bold'))
    mobile_lbl.place(relx=0.3, rely=0.3)

    mobile_entry = Entry(frm, font=('Comic Sans MS', 20), bd=7)
    mobile_entry.place(relx=0.5, rely=0.3)

    std_course = Label(frm, text='Select Course', bg='light blue', font=('Comic Sans MS', 20, 'bold'))
    std_course.place(relx=0.3, rely=0.45)

    con = sql.connect(database="studentdb.sqlite")
    cursor = con.cursor()
    cursor.execute("select * from course")
    courses = cursor.fetchall()
    courses.insert(0, "----------Select------------")
    con.close()
    course_list = Combobox(frm, values=courses, font=('Comic Sans MS', 15))
    course_list.place(relx=0.5, rely=0.45)
    course_list.current(0)

    student_fee = Label(frm, text='Registraction Fee', bg='light blue', font=('Comic Sans MS', 20, 'bold'))
    student_fee.place(relx=0.3, rely=0.6)

    fee_entry = Entry(frm, font=('Comic Sans MS', 20), bd=7)
    fee_entry.place(relx=0.5, rely=0.6)

    reg_btn = Button(frm, text="Register", font=('Comic Sans MS', 18, 'bold'), bd=7, command=register_student_db)
    reg_btn.place(relx=0.5, rely=0.80)


def find_student_body():
    def logout():
        frm.destroy()
        main_body()

    def home():
        frm.destroy()
        login_body()

    def search():
        id = serch_id_entry.get()
        con = sql.connect(database="studentdb.sqlite")
        cursor = con.cursor()
        cursor.execute("select * from students where stu_id=?", (id,))
        row = cursor.fetchone()
        if row == None:
            messagebox.showwarning('Search', "Student Id not Found....")
        else:
            messagebox.showinfo('Search', str(row))
            frm.destroy()
            find_student_body()

    frm = Frame(win)
    frm.configure(bg='light blue')
    frm.place(x=0, rely=0.2, relwidth=1, relheight=0.8)

    wel_lbl = Label(frm, text="Welcome Prakash", font=('Comic Sans MS', 15, 'bold'), bg='light blue')
    wel_lbl.place(relx=0, rely=0)

    log_btn = Button(frm, text="LogOut", font=('Comic Sans MS', 18, 'bold'), bd=7, command=logout)
    log_btn.place(relx=0.90, rely=0)

    home_btn = Button(frm, text="Home", font=('Comic Sans MS', 18, 'bold'), bd=7, command=home)
    home_btn.place(relx=0.80, rely=0)

    serch_student_id = Label(frm, text='Student Id', bg='light blue', font=('Comic Sans MS', 20, 'bold'))
    serch_student_id.place(relx=0.25, rely=0.3)

    serch_id_entry = Entry(frm, font=('Comic Sans MS', 20, 'bold'), bd=7)
    serch_id_entry.place(relx=0.45, rely=0.3)
    serch_id_entry.focus()

    srch_btn = Button(frm, text="Search", font=('Comic Sans MS', 18, 'bold'), bd=7, command=search)
    srch_btn.place(relx=0.5, rely=0.5)


def deposit_fee_body():
    def logout():
        frm.destroy()
        main_body()

    def home():
        frm.destroy()
        login_body()

    def fetch_fee(event):
        id = serch_id_entry.get()
        id = serch_id_entry.get()
        con = sql.connect(database="studentdb.sqlite")
        cursor = con.cursor()
        cursor.execute("select bal from students where stu_id=?", (id,))
        row = cursor.fetchone()

        if row == None:
            messagebox.showwarning('Search', "Student does not Exits....")
        else:
            rem_fee_entry.configure(state="normal")
            rem_fee_entry.delete(0, "end")
            rem_fee_entry.insert(0, row[0])
            rem_fee_entry.configure(state="disabled")
            depo_entry.focus()

    def deposit():
        id = serch_id_entry.get()
        depo_fee = depo_entry.get()
        con = sql.connect(database="studentdb.sqlite")
        cursor = con.cursor()
        cursor.execute("update students set bal=bal-? where stu_id=?", (int(depo_fee), id))
        con.commit()
        con.close()
        messagebox.showinfo('', " Fee Deposited")
        frm.destroy()
        deposit_fee_body()

    frm = Frame(win)
    frm.configure(bg='light blue')
    frm.place(x=0, rely=0.2, relwidth=1, relheight=0.8)

    wel_lbl = Label(frm, text="Welcome Prakash", font=('Comic Sans MS', 15, 'bold'), bg='light blue')
    wel_lbl.place(relx=0, rely=0)

    log_btn = Button(frm, text="LogOut", font=('Comic Sans MS', 18, 'bold'), bd=7, command=logout)
    log_btn.place(relx=0.90, rely=0)

    home_btn = Button(frm, text="Home", font=('Comic Sans MS', 18, 'bold'), bd=7, command=home)
    home_btn.place(relx=0.80, rely=0)

    serch_student_id = Label(frm, text='Student Id', bg='light blue', font=('Comic Sans MS', 20, 'bold'))
    serch_student_id.place(relx=0.3, rely=0.15)

    serch_id_entry = Entry(frm, font=('Comic Sans MS', 20, 'bold'), bd=7)
    serch_id_entry.place(relx=0.45, rely=0.15)
    serch_id_entry.focus()
    serch_id_entry.bind("<FocusOut>", fetch_fee)

    rem_fee = Label(frm, text='Remaning Fee', bg='light blue', font=('Comic Sans MS', 20, 'bold'))
    rem_fee.place(relx=0.3, rely=0.3)

    rem_fee_entry = Entry(frm, font=('Comic Sans MS', 20, 'bold'), bd=7)
    rem_fee_entry.place(relx=0.45, rely=0.3)
    rem_fee_entry.configure(state='disabled')

    deposit_fee = Label(frm, text='Deposit Fee', bg='light blue', font=('Comic Sans MS', 20, 'bold'))
    deposit_fee.place(relx=0.3, rely=0.45)

    depo_entry = Entry(frm, font=('Comic Sans MS', 20, 'bold'), bd=7)
    depo_entry.place(relx=0.45, rely=0.45)

    deposit_btn = Button(frm, text="Deposit", font=('Comic Sans MS', 18, 'bold'), bd=7, command=deposit)
    deposit_btn.place(relx=0.5, rely=0.75)


def add_course_body():
    def logout():
        frm.destroy()
        main_body()

    def home():
        frm.destroy()
        login_body()

    def add_course_db():
        n = course_name_entry.get()
        n = n.upper()
        f = course_amt_entry.get()
        con = sql.connect(database="studentdb.sqlite")
        cursor = con.cursor()
        if len(n) == 0 and len(f) == 0:
            messagebox.showwarning('validation', "Course Name And Amount not be Empty")
        else:
            try:
                cursor.execute("insert into course values(?,?)", (n, f))
                con.commit()
                messagebox.showinfo('Comic Sans MS', 'Course Added')
            except Exception as e:
                messagebox.showerror('Comic Sans MS', str(e))
            con.close()
            frm.destroy()
            add_course_body()

    frm = Frame(win)
    frm.configure(bg='light blue')
    frm.place(x=0, rely=0.2, relwidth=1, relheight=0.8)

    wel_lbl = Label(frm, text="Welcome Prakash", font=('Comic Sans MS', 15, 'bold'), bg='light blue')
    wel_lbl.place(relx=0, rely=0)

    log_btn = Button(frm, text="LogOut", font=('Comic Sans MS', 18, 'bold'), bd=7, command=logout)
    log_btn.place(relx=0.90, rely=0)

    home_btn = Button(frm, text="Home", font=('Comic Sans MS', 18, 'bold'), bd=7, command=home)
    home_btn.place(relx=0.80, rely=0)

    course_name = Label(frm, text='Course Name', bg='light blue', font=('Comic Sans MS', 20, 'bold'))
    course_name.place(relx=0.25, rely=0.15)

    course_name_entry = Entry(frm, font=('Comic Sans MS', 20, 'bold'), bd=7)
    course_name_entry.place(relx=0.45, rely=0.15)
    course_name_entry.focus()

    course_amt = Label(frm, text='Course Amount', bg='light blue', font=('Comic Sans MS', 20, 'bold'))
    course_amt.place(relx=0.25, rely=0.3)

    course_amt_entry = Entry(frm, font=('Comic Sans MS', 20, 'bold'), bd=7)
    course_amt_entry.place(relx=0.45, rely=0.3)

    add_btn = Button(frm, text="Add Course", font=('Comic Sans MS', 18, 'bold'), bd=7, command=add_course_db)
    add_btn.place(relx=0.5, rely=0.5)


def update_course_body():
    def logout():
        frm.destroy()
        main_body()

    def home():
        frm.destroy()
        login_body()

    def update_course_db():
        course = update_cour_list.get()
        amt = update_amt_entry.get()
        co_urse, course_fee = course.split()

        con = sql.connect(database="studentdb.sqlite")
        cursor = con.cursor()
        cursor.execute("update course set course_fee=? where course_name=?", (amt, co_urse))
        con.commit()
        con.close()
        messagebox.showinfo('', " Course Updated...")
        frm.destroy()
        update_course_body()

    frm = Frame(win)
    frm.configure(bg='light blue')
    frm.place(x=0, rely=0.2, relwidth=1, relheight=0.8)

    wel_lbl = Label(frm, text="Welcome Prakash", font=('Comic Sans MS', 15, 'bold'), bg='light blue')
    wel_lbl.place(relx=0, rely=0)
    home_btn = Button(frm, text="Home", font=('Comic Sans MS', 18, 'bold'), bd=7, command=home)
    home_btn.place(relx=0.80, rely=0)
    log_btn = Button(frm, text="LogOut", font=('Comic Sans MS', 18, 'bold'), bd=7, command=logout)
    log_btn.place(relx=0.90, rely=0)

    update_cour = Label(frm, text='Course Name', bg='light blue', font=('Comic Sans MS', 20, 'bold'))
    update_cour.place(relx=0.25, rely=0.15)

    con = sql.connect(database="studentdb.sqlite")
    cursor = con.cursor()
    cursor.execute("select * from course")
    courses = cursor.fetchall()
    courses.insert(0, "----------Select------------")
    con.close()

    update_cour_list = Combobox(frm, values=courses, font=('Comic Sans MS', 15))
    update_cour_list.place(relx=0.5, rely=0.15)
    update_cour_list.current(0)

    update_amt = Label(frm, text='Course Amount', bg='light blue', font=('Comic Sans MS', 20, 'bold'))
    update_amt.place(relx=0.25, rely=0.3)

    update_amt_entry = Entry(frm, font=('Comic Sans MS', 20, 'bold'), bd=7)
    update_amt_entry.place(relx=0.45, rely=0.3)

    update_btn = Button(frm, text="Update Course", font=('Comic Sans MS', 18, 'bold'), bd=7, command=update_course_db)
    update_btn.place(relx=0.5, rely=0.5)


main_body()
win.mainloop()
