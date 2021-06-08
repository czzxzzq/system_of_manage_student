from tkinter import *
import tkinter.messagebox
import sqlop
import mainwindow


class add():
    def add_S(self):
        ssno = self.sinput1.get()
        ssname = self.sinput2.get()
        ssex = self.sinput3.get()
        sage = self.sinput4.get()
        sdepth = self.sinput5.get()
        if ssno != "":
            a = sqlop.sql()
            str = "insert into s values(\'" + ssno + "\',\'" + ssname + "\',\'" + ssex + "\'," + sage + ",\'" + sdepth + "\');"
            flag = a.opadd(str)
            if flag == 1:
                tkinter.messagebox.showinfo('提示', '插入成功')
            else:
                tkinter.messagebox.showinfo('警告', '插入失败，可能是数据库出现问题')
            a.shutdown()
        else:
            tkinter.messagebox.showinfo("警告", '主键缺失，不符合实体完整性')

    def add_SC(self):
        sno = self.scinput1.get()
        cno = self.scinput2.get()
        grade = self.scinput3.get()
        if sno != "" and cno != " ":
            str = "insert into sc values(\'" + sno + "\',\'" + cno + "\'," + grade + ");"  # 即将执行的SQl语句
            a = sqlop.sql()  # 实例化一个sqlop对象
            flag = a.opadd(str)  # 执行语句，并通过返回值判断是否执行成功
            if flag == 1:
                tkinter.messagebox.showinfo('提示', '插入成功')
            else:
                tkinter.messagebox.showinfo('警告', '插入失败，可能是数据库出现问题')
            a.shutdown()
        else:
            tkinter.messagebox.showinfo("警告", '主键缺失，不符合实体完整性')

    def add_C(self):
        cno = self.cinput1.get()
        cname = self.cinput2.get()
        ccredit = self.cinput3.get()
        if cno != "":
            a = sqlop.sql()
            str = "insert into c values(\'" + cno + "\',\'" + cname + "\'," + ccredit + ");"
            print(str)
            flag = a.opadd(str)
            if flag == 1:
                tkinter.messagebox.showinfo('提示', '插入成功')
            else:
                tkinter.messagebox.showinfo('警告', '插入失败，可能是数据库出现问题')
            a.shutdown()
        else:
            tkinter.messagebox.showinfo("警告", '主键缺失，不符合实体完整性')

    def reback(self):
        self.initface.destroy()
        mainwindow.mainwindow(self.root)

    def __init__(self, master):
        self.root = master
        self.root.title('插入')
        self.initface = Frame(master)
        self.initface.grid(sticky=W + E + N + S)
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
        btnadd = Button(self.initface, text='增加S表', command=self.add_S).grid(row=6, column=1)
        btnadd = Button(self.initface, text='增加SC表', command=self.add_SC).grid(row=6, column=2)
        btnadd = Button(self.initface, text='增加C表', command=self.add_C).grid(row=6, column=3)
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
