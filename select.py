from tkinter import *
import mainwindow
import tkinter.messagebox
import sqlop
import string


class select():
    def select_S(self):
        ssno = self.sinput1.get()
        ssname = self.sinput2.get()
        ssex = self.sinput3.get()
        sage = self.sinput4.get()
        sdepth = self.sinput5.get()
        if ssno == "" and ssname == "" and ssex == "" and sage == "" and sdepth == "":
            if tkinter.messagebox.askokcancel(title="提示", message='您是想查询 S 表中所有数据吗？如果不是请输入筛选条件!'):
                str = "select * from s"
                a = sqlop.sql()
                a.opselect(str, self.root)
                a.shutdown()
            return
        st = ""
        if ssno != "":
            st = "sno=" + '\'' + ssno + '\''
        if ssname != "":
            if st == "":
                st += "sname=" + '\'' + ssname + '\''
            else:
                st += "and sname=" + '\'' + ssname + '\''
        if ssex != "":
            if st == "":
                st += "ssex=" + '\'' + ssex + '\''
            else:
                st += "and ssex=" + '\'' + ssex + '\''
        if sage != "":
            if st == "":
                st += "sage=" + '\'' + sage + '\''
            else:
                st += "and sage=" + '\'' + sage + '\''
        if sdepth != "":
            if st == "":
                st += "sdept=" + '\'' + sdepth + '\''
            else:
                st += "and sdept=" + '\'' + sdepth + '\''
        st += ';'
        str = "select * from s where " + st
        #        print(str)
        a = sqlop.sql()
        a.opselect(str, self.root)
        a.shutdown()

        return

    def select_SC(self):
        sno = self.scinput1.get()
        cno = self.scinput2.get()
        grade = self.scinput3.get()
        if sno == "" and cno == "" and grade == "":
            if tkinter.messagebox.askokcancel(title="提示", message='您是想查询 SC 表中所有数据吗？如果不是请输入筛选条件!'):
                str = "select * from sc"
                a = sqlop.sql()
                a.opselect(str, self.root)
                a.shutdown()
            return
        st = ""
        if sno != "":
            st = "sno=" + '\'' + sno + '\''
        if cno != "":
            if st == "":
                st += "cno=" + '\'' + cno + '\''
            else:
                st += "and cno=" + '\'' + cno + '\''
        if grade != "":
            if st == "":
                st += "grade=" + grade
            else:
                st += "and grade=" + grade
        st += ';'
        str = "select * from sc where " + st
        #        print(str)
        a = sqlop.sql()
        a.opselect(str, self.root)
        a.shutdown()
        return

    def select_C(self):
        cno = self.cinput1.get()
        cname = self.cinput2.get()
        ccredit = self.cinput3.get()
        if cno == "" and cname == "" and ccredit == "":
            if tkinter.messagebox.askokcancel(title="提示", message='您是想查询 C 表中所有数据吗？如果不是请输入筛选条件!'):
                str = "select * from c"
                a = sqlop.sql()
                a.opselect(str, self.root)
                a.shutdown()
            return
        st = ""
        if cno != "":
            st = "cno=" + '\'' + cno + '\''
        if cname != "":
            if st == "":
                st += "cname=" + '\'' + cname + '\''
            else:
                st += "and cname=" + '\'' + cname + '\''
        if ccredit != "":
            if st == "":
                st += "ccredit=" + ccredit
            else:
                st += "and ccredit=" + ccredit
        st += ';'
        str = "select * from c where " + st   # 确定的查询sql语句
        #        print(str)
        a = sqlop.sql()     # 实例化一个sqlop中的sql对象
        a.opselect(str, self.root)     #执行opselect() 方法
        a.shutdown()
        return

    def reback(self):
        self.initface.destroy()
        mainwindow.mainwindow(self.root)

    def __init__(self, master):
        self.root = master
        self.root.title('查询')
        self.initface = Frame(self.root)
        self.initface.grid()
        lb1 = Label(self.initface, text='S表')
        scln1 = Label(self.initface, text='学号').grid(row=0, column=1)
        scln2 = Label(self.initface, text='姓名').grid(row=0, column=2)
        scln3 = Label(self.initface, text='性别').grid(row=0, column=3)
        scln4 = Label(self.initface, text='年龄').grid(row=0, column=4)
        scln5 = Label(self.initface, text='专业').grid(row=0, column=5)
        lb2 = Label(self.initface, text='SC表')
        sccln1 = Label(self.initface, text='学号').grid(row=2, column=1)
        sccln2 = Label(self.initface, text='课程号').grid(row=2, column=2)
        sccln3 = Label(self.initface, text='成绩').grid(row=2, column=3)
        lb3 = Label(self.initface, text='C表')
        ccln1 = Label(self.initface, text='课程号').grid(row=4, column=1)
        ccln2 = Label(self.initface, text='课程名').grid(row=4, column=2)
        ccln3 = Label(self.initface, text='学分').grid(row=4, column=3)
        btnadd = Button(self.initface, text='查询S表', command=self.select_S).grid(row=6, column=1)
        btnadd = Button(self.initface, text='查询SC表', command=self.select_SC).grid(row=6, column=2)
        btnadd = Button(self.initface, text='查询C表', command=self.select_C).grid(row=6, column=3)
        btnback = Button(self.initface, text='返回', command=self.reback).grid(row=6, column=4)
        self.sinput1 = Entry(self.initface, width=14)
        self.sinput2 = Entry(self.initface, width=14)
        self.sinput3 = Entry(self.initface, width=14)
        self.sinput4 = Entry(self.initface, width=14)
        self.sinput5 = Entry(self.initface, width=14)
        self.scinput1 = Entry(self.initface, width=14)
        self.scinput2 = Entry(self.initface, width=14)
        self.scinput3 = Entry(self.initface, width=14)
        self.cinput1 = Entry(self.initface, width=14)
        self.cinput2 = Entry(self.initface, width=14)
        self.cinput3 = Entry(self.initface, width=14)
        lb1.grid(row=1, pady=6, padx=5)
        lb2.grid(row=3, pady=6, padx=5)
        lb3.grid(row=5, pady=6, padx=5)
        self.sinput1.grid(row=1, column=1, padx=5)
        self.sinput2.grid(row=1, column=2, padx=5)
        self.sinput3.grid(row=1, column=3, padx=5)
        self.sinput4.grid(row=1, column=4, padx=5)
        self.sinput5.grid(row=1, column=5, padx=5)
        self.scinput1.grid(row=3, column=1, padx=5)
        self.scinput2.grid(row=3, column=2, padx=5)
        self.scinput3.grid(row=3, column=3, padx=5)
        self.cinput1.grid(row=5, column=1, padx=5)
        self.cinput2.grid(row=5, column=2, padx=5)
        self.cinput3.grid(row=5, column=3, padx=5)
