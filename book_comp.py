from tkinter import *
import time
from tkinter import ttk
from tkinter.ttk import *
import local_price
import ib_store
import compare_prices
import sqlite3
from tkinter import Tk

book_name = ['18 Years JEE Main Physics Chapterwise Solutions',
                     'Daily Practice Problems of PCM for JEE Main/Advanced 1 Edition',
                     'Errorless Chemistry for JEE MAIN 2020 by NTA ',
                     'Organic Chemistry 8th Edition by Leroy G. Wade',
                     ' Organic Chemistry 2nd Edition by Clayden, Greeves, Warren',
                     'JEE MAIN EXPLORER',
                     ' Principles of Physics by Walker, Halliday, Resnick',
                     ' Mathematics MCQ', 'Differential Calculus ,Author : S.K. Goyal',
                     ' Skill in Mathematics - Algebra for JEE Main', 'NEW PATTERN JEE PROBLEMS PHYSICS FOR JEE MAIN',
                     ' Problems in Physical Chemistry for JEE',
                     'Concise Inorganic Chemistry: Fifth Edition by J.D. Lee',
                     'Fundamentals of Mathematics for JEE Main/Advanced - Integral Calculus',
                     'Chapterwise Solutions of Physics for JEE Main 2002-2017']
updated=[]
for i in range(1,16):
    updated.append(0)

class Login_page():

    # ----------------------------CONNECT TO DATABASE---------------------------#

    def Database(self):
        global conn, cursor
        conn = sqlite3.connect("accounts.db")
        cursor = conn.cursor()
        cursor.execute(
            "CREATE TABLE IF NOT EXISTS `members` (id INTEGER NOT NULL PRIMARY KEY  AUTOINCREMENT, username TEXT, password TEXT)")
        cursor.execute("SELECT * FROM `members` WHERE `username` = 'admin' AND `password` = 'admin'")
        if cursor.fetchone() is None:
            cursor.execute("INSERT INTO `members` (username, password) VALUES('admin', 'admin')")
            conn.commit()

       # model_numb = ['8174505172', '8174504893', '86858']
        cursor.execute("DROP TABLE `books`")
        conn.commit()
        final_model_no = ['9789389310788', '9789353501488', '9788193766095', '9789332578586', '9780198728719',
                          '9789388899796', '9788126552566', '9788177098471', '9789384934064', '9789313191889',
                          '9789313191353', '9789384934873', '9788126515547', '9789332570276', '9789386650788']
        book_name = ['18 Years JEE Main Physics Chapterwise Solutions',
                     'Daily Practice Problems of PCM for JEE Main/Advanced 1 Edition',
                     'Errorless Chemistry for JEE MAIN 2020 by NTA ',
                     'Organic Chemistry 8th Edition by Leroy G. Wade',
                     ' Organic Chemistry 2nd Edition by Clayden, Greeves, Warren',
                     'JEE MAIN EXPLORER',
                     ' Principles of Physics by Walker, Halliday, Resnick',
                     ' Mathematics MCQ', 'Differential Calculus ,Author : S.K. Goyal',
                     ' Skill in Mathematics - Algebra for JEE Main', 'NEW PATTERN JEE PROBLEMS PHYSICS FOR JEE MAIN',
                     ' Problems in Physical Chemistry for JEE',
                     'Concise Inorganic Chemistry: Fifth Edition by J.D. Lee',
                     'Fundamentals of Mathematics for JEE Main/Advanced - Integral Calculus',
                     'Chapterwise Solutions of Physics for JEE Main 2002-2017']
        cursor.execute(
            "CREATE TABLE IF NOT EXISTS `books` (id INTEGER NOT NULL PRIMARY KEY  AUTOINCREMENT, model_no TEXT, name TEXT)")  # *****BOOKS NAME TO BE ADDED****
        cursor.execute("SELECT * FROM `books` WHERE `id` = 1 AND `model_no` = '9789389310788'")
        if cursor.fetchone() is None:
            for i in range(len(final_model_no)):
                cursor.execute("INSERT INTO `books` (model_no, name) VALUES (?,?)",
                               (final_model_no[i], book_name[i]))
                conn.commit()

        cursor.execute(
            "CREATE TABLE IF NOT EXISTS `book_record` (sno INTEGER NOT NULL PRIMARY KEY  AUTOINCREMENT, user_id INTEGER, book_id INTEGER, count INTEGER )")
        conn.commit()

        # -------------------------------FRONTEND-------------------------------------#

    def __init__(self, master):
        self.master = master
        self.style = ttk.Style()
        self.master.title("Book Comparator-Login")
        self.master.geometry('1000x1000')
        self.style.configure('TFrame', background='Lightskyblue2')
        self.frame=ttk.Frame(self.master,style='TFrame')
        self.frame.pack()

        self.style.configure('W.TButton', font=
        ('verdana', 10, 'bold'),
                             foreground='black',background='blue2')
        self.style.configure('TLabel', background='Lightskyblue2')
        self.topframe=Frame(self.frame, width=10000, height=3000,style='new.TFrame')
        self.topframe.grid(row=5,column=0,pady=20)
        self.bottomframe = Frame(self.frame, width=1000, height=5000,style='new.TFrame')
        self.bottomframe.grid(row=20,column=0,)

        self.login_btn = ttk.Button(self.bottomframe, text="Login",style="W.TButton",command=self.Login)
        self.login_btn.grid(row=3, column=2)
        self.login_btn.bind('<Return>', self.Login)
        self.register_btn = ttk.Button(self.bottomframe, text="Register",style="W.TButton", command=self.Register)
        self.register_btn.grid(row=3, column=3,padx=15)
        self.register_btn.bind('<Return>', self.Register)

        self.title=ttk.Label(self.topframe,text="Book Comparator!",font=('Cambria',30,'bold'),style='TLabel')
        self.title.grid()
        self.headline= ttk.Label(self.topframe, text="Hello user! Register if you are a new user or login if you already have an account.",font=('Cambria',15),style='TLabel')
        self.headline.grid(row=1, column=0,pady=20)

        # -------------------------------LOGIN FORM-------------------------------------#

        self.caption = Label(self.topframe, text="", font=('arial', 10))
        self.username = StringVar()
        self.password = StringVar()
        self.user_text = ttk.Label(self.topframe, text="Username:", font=('arial', 18),style='TLabel')
        self.user_text.grid(row=2, column=0, pady=5, sticky=W)
        self.user_value = Entry(self.topframe, textvariable=self.username)
        self.user_value.grid(row=2, column=0)
        self.pwd_text = ttk.Label(self.topframe, text="Password:", font=('arial', 18),style='TLabel')
        self.pwd_text.grid(row=3, column=0, sticky=W)
        self.pwd_value = Entry(self.topframe, textvariable=self.password, show="*")
        self.pwd_value.grid(row=3, column=0)
        self.lbl_text = ttk.Label(self.bottomframe,style='TLabel')
        self.lbl_text.grid(row=5, column=2, pady=10)
        #-------------------------------------------------#

    def new_page(self):
        self.NewPage = Toplevel(self.master)
        self.project = main_page(self.NewPage)
        self.project.config(bg='Lightskyblue2')

    # -------------------------------LOGIN FUNCTION-------------------------------------#

    def Login(self, event=None):
        self.Database()
        if self.username.get() == "" or self.password.get() == "":
            self.lbl_text.config(text="Please complete the required field!")
        else:
            cursor.execute("SELECT * FROM `members` WHERE `username` = ? AND `password` = ?",
                           (self.username.get(), self.password.get()))
            data = cursor.fetchone()

            cursor.execute("SELECT * FROM `members` WHERE `username` = ? AND `password` = ?",
                           (self.username.get(), self.password.get()))
            if cursor.fetchone() is not None:
                self.username.set("")
                self.password.set("")
                self.lbl_text.config(text="")
                self.user_id = data[0]
                main_page.get_id(main_page, self.user_id)  # sends id of the logged in user
                self.new_page()

            else:
                self.lbl_text.config(text="Invalid username or password")
                self.username.set("")
                self.password.set("")
        cursor.close()
        conn.close()

    # -------------------------------REGISTER FUNCTION-------------------------------------#

    def Register(self, event=None):
        self.Database()
        if self.username.get() == "" or self.password.get() == "":
            self.lbl_text.config(text="Please complete the required field!")
        else:
            cursor.execute("SELECT * FROM `members` WHERE `username` = ? AND `password` = ?",
                           (self.username.get(), self.password.get()))
            if cursor.fetchone() is not None:
                self.username.set("")
                self.password.set("")
                self.lbl_text.config(text="")
                self.lbl_text.config(text="Account with this username already exists.")
            else:
                cursor.execute("INSERT INTO `members` (username, password) VALUES (?,?)",
                               (self.username.get(), self.password.get()))
                conn.commit()
                self.lbl_text.config(text="Account created successfully!")
                self.username.set("")
                self.password.set("")

        cursor.close()
        conn.close()


# -------------------------------NEW WINDOW(MAIN)-------------------------------------#

class main_page():

    def get_id(self, user_id):
        self.user_id = user_id
        return self.user_id

    def get_book_id(self, recieved):
        self.book_id = recieved
        return self.book_id
    # -------------------------------FETCH PRICES-------------------------------------#

    def project(id, list):
        Login_page.Database(Login_page)
        sql = "SELECT * FROM `books` WHERE id=(?)"
        cursor.execute(sql, (id,))
        model = cursor.fetchone()
        model_number = model[1]
        list.delete(0, END)
        price = local_price.get_local_price(model_number)
        list.insert(0,"Book price in offline stores : "+price)
        on_price1, on_price2 = ib_store.get_online_price(model_number)
        list.insert(1,"Book price on Amazon : "+on_price1)
        list.insert(2, "Book price on Flipkart : "+on_price2)
        updated[id-1]=min(compare_prices.price_ib(on_price1),compare_prices.price_ib(on_price2),compare_prices.price_local(price))
        print(updated)

    # -------------------------------SHOW SECOND WINDOW-------------------------------------#

    def __init__(self, master1):
        self.master1 = master1
        self.style = ttk.Style()
        self.master1.title("Book Comparator")
        self.width=root.winfo_screenwidth()
        self.height=root.winfo_screenheight()
        self.master1.geometry("%dx%d" % (self.width,self.height))
        self.frame = Frame(self.master1)
        self.frame.pack()
        self.style.configure('TFrame',background='Lightskyblue2')
        Mainframe = ttk.Frame(self.master1,style='TFrame')
        Mainframe.pack()
        self.style.configure('TLabel', background='Lightskyblue2')
        self.title=ttk.Label(Mainframe,text="Book Comparator!",font=('Cambria',30,'bold'),style='TLabel')
        self.title.pack()
        self.sub_title = ttk.Label(Mainframe, text="Your Prices are shown here:", font=('Cambria', 15),style='TLabel')
        self.sub_title.place(x=10,y=66)
        Dataframe = Frame(Mainframe, width=900, height=100)
        Dataframe.pack(side=LEFT)
        ARframe=Frame(Mainframe,width=500,height=100)
        ARframe.pack(side=BOTTOM)
        self.ARframe_2=ARframe
        self.Dataframe_2 = Dataframe  # new frame created so as to display the "add to cart" content
        self.sub_title = ttk.Label(self.Dataframe_2, text="Amount to be paid:", font=('Cambria', 15),style='TLabel')
        self.sub_title.place(x=10,y=210)
        self.show_price= Listbox(Dataframe, width=20, bd=10, relief='groove', fg='Gray')
        self.show_price.grid(row=1, column=0, padx=8,pady=20)
        Buttonframe = Frame(Mainframe, width=600, height=950)
        Buttonframe.pack(side=RIGHT)
        self.Buttonframe=Buttonframe
        list = Listbox(Dataframe, width=50)
        list.grid(row=0,column=0,sticky=N,pady=30)
        self.display_cost = 0
        self.style.configure('W.TButton', font= ('verdana', 9), foreground='black',background='blue2')
        self.style.configure('TButton', font=('Times New Roman',12,'bold'), foreground='black',background='navy',relief='flat')
        # created 15 buttons each with different functionality by assigning different id's to them.
        for buttons in range(1, 16):
            book1 = ttk.Button(Buttonframe, text=book_name[buttons - 1],style='W.TButton',
                           command=lambda buttons=buttons: main_page.get_book_id(main_page,buttons))
            book1.grid(row=buttons+1, column=0,sticky=W,pady=5)
        showprice = ttk.Button(Buttonframe, text="SHOW PRICE",style='TButton',
                       command=lambda buttons=buttons: main_page.project(self.book_id,list))
        showprice.grid(row=0, column=0,pady=10)
        add_to_cart_button = ttk.Button(Buttonframe, text="ADD TO CART", style='TButton', command=self.add_to_cart)
        add_to_cart_button.grid(row=18, column=0,pady=7)

        # -------------------------------ADD TO CART-------------------------------------#

    def add_book(self, book, cart_list):
        Login_page.Database(Login_page)
        cursor.execute("SELECT * FROM `book_record` WHERE `user_id` = ? AND `book_id` = ?", (self.user_id, book))
        if cursor.fetchone() is not None:
            cursor.execute("UPDATE `book_record` SET count=count+1 WHERE `user_id` = ? AND `book_id` = ?",
                           (self.user_id, book))
            conn.commit()
        else:
            cursor.execute("INSERT INTO `book_record` (user_id, book_id, count) VALUES (?,?,?)", (self.user_id, book, 1))
            conn.commit()
        sql = "SELECT model_no,name FROM `books` WHERE id=(?)"
        cursor.execute(sql, (book,))
        model = cursor.fetchone()
        cart_list.insert(END, "Added    " + str(model[1]))
        if updated[book-1]==0:
            cost, avail = compare_prices.compare(model[0])
            updated[book - 1]=cost
        else:
            cost=updated[book-1]
        self.display_cost += cost
        self.show_price.delete(0, END)
        self.show_price.insert(END, self.display_cost)
        print(self.display_cost)
        # -------------------------------REMOVE FROM CART-------------------------------------#

    def remove_book(self, book, cart_list):
        Login_page.Database(Login_page)
        sql = "SELECT model_no FROM `books` WHERE id=(?)"
        cursor.execute(sql, (book,))
        model = cursor.fetchone()
        cursor.execute("SELECT count FROM `book_record` WHERE `user_id` = ? AND `book_id` = ?", (self.user_id, book))
        rec = cursor.fetchone()
        if rec is not None:
            if updated[book-1] == 0:
                cost, avail = compare_prices.compare(model[0])
                updated[book - 1]=cost
            else:
                cost = updated[book-1]
            self.display_cost -= cost
            if rec[0] == 1:
                cursor.execute("DELETE FROM `book_record` WHERE `user_id` = ? AND `book_id` = ?", (self.user_id, book))
                conn.commit()
            else:
                cursor.execute("UPDATE `book_record` SET count=count-1 WHERE `user_id` = ? AND `book_id` = ?",
                               (self.user_id, book))
                conn.commit()
        else:
            pass
        cart_list.delete(0, END)
        self.show_price.delete(0, END)
        self.show_price.insert(END, self.display_cost)

        record_sql = "SELECT * FROM `book_record` WHERE user_id=(?)"
        cursor.execute(record_sql, (self.user_id,))
        result = cursor.fetchall()
        for r in result:
            sql_1 = "SELECT model_no,name FROM `books` WHERE id=(?)"
            cursor.execute(sql_1, (r[2],))
            book_display = cursor.fetchone()
            b = book_display[1]
            string = str(b) + "         Quantity :" + str(r[3])
            cart_list.insert(END, string)

        # -------------------------------DISPLAY CURRENT CART-------------------------------------#

    def add_to_cart(self):
        cart_list = Listbox(self.Dataframe_2, width=75)
        scroll = Scrollbar(self.Dataframe_2, command=cart_list.yview, orient=VERTICAL)
        cart_list.configure(yscrollcommand=scroll.set)
        cart_list.grid(row=3, column=0, padx=8)
        scroll.grid(row=3, column=3, sticky=N + S)
        self.sub_title = ttk.Label(self.Dataframe_2, text="Your Cart:", font=('Cambria', 15),style='TLabel')
        self.sub_title.place(x=10,y=410)
        add_1 = ttk.Button(self.Buttonframe, text="Add", command=lambda: main_page.add_book(self, self.book_id, cart_list))
        add_1.grid(row=6, column=2,sticky='W')

        remove_1 = ttk.Button(self.Buttonframe, text="Remove",
                          command=lambda: main_page.remove_book(self, self.book_id, cart_list))
        remove_1.grid(row=6, column=3,sticky='E')


        Login_page.Database(Login_page)
        #self.display_cost = 0
        record_sql = "SELECT * FROM `book_record` WHERE user_id=(?)"
        cursor.execute(record_sql, (self.user_id,))
        result = cursor.fetchall()
        for r in result:

            sql_1 = "SELECT model_no,name FROM `books` WHERE id=(?)"
            cursor.execute(sql_1, (r[2],))
            book_display = cursor.fetchone()

            modelno = book_display[0]
            quantity = r[3]
            string = str(book_display[1]) + "       Quantity :" + str(quantity)
            cart_list.insert(END, string)

            if updated[r[2]-1] == 0:
                cost, avail = compare_prices.compare(modelno)
                updated[r[2] - 1]=cost
            else:
                cost = updated[r[2]-1]
            if (avail == 0):
                pass
            else:
                self.display_cost += quantity * (cost)
        self.show_price.delete(0, END)
        self.show_price.insert(END, self.display_cost)
        print(self.display_cost)

    def config(self, bg):
        self.master1.configure(bg='Lightskyblue2')


root=Tk()
project = Login_page(root)
imagelist = ['images/book1.gif','images/book2.gif','images/book3.gif','images/book4.gif','images/book5.gif','images/book6.gif']
photo = PhotoImage(file=imagelist[0])
width = photo.width()
height = photo.height()
canvas = Canvas(width=width, height=height)
canvas.pack()
giflist = []
for imagefile in imagelist:
    photo = PhotoImage(file=imagefile)
    giflist.append(photo)
for k in range(0, 1000):
    for gif in giflist:
        canvas.delete(ALL)
        canvas.create_image(width/2.0, height/2.0, image=gif)
        canvas.update()
        time.sleep(1)
#root.configure(bg='Lightskyblue2')
root.mainloop()