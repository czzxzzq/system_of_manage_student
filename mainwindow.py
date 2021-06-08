from tkinter import *
from add import *
import login
import select
import delete
import update
import advanced

class mainwindow():
    def add_ele(self):
        self.initface.destroy()
        self.root.title('增加')
        add(self.root)

    def reback(self):
        self.initface.destroy()
        login.login(self.root)

    def sel_ele(self):
        self.initface.destroy()
        select.select(self.root)

    def del_ele(self):
        self.initface.destroy()
        delete.delete(self.root)

    def upd_ele(self):
        self.initface.destroy()
        update.update(self.root)
    def advanced(self):
        self.initface.destroy()
        advanced.advanced(self.root)
    def __init__(self, master):
        self.root = master
        self.root.title('管理')
        self.initface = Frame(self.root, )
        self.initface.pack()
        btnadd = Button(self.initface, text='增加数据', fg='black', font=('黑体', 9), command=self.add_ele)
        btndel = Button(self.initface, text='删除数据', fg='black', font=('黑体', 9), command=self.del_ele)
        btnsel = Button(self.initface, text='查询数据', fg='black', font=('黑体', 9), command=self.sel_ele)
        btnupd = Button(self.initface, text='更新数据', fg='black', font=('黑体', 9), command=self.upd_ele)
        btnadv = Button(self.initface, text='高级操作', fg='black', font=('黑体', 9),command=self.advanced)
        btnback = Button(self.initface, text='退出登录', fg='black', font=('黑体', 9), command=self.reback)
        btnadd.grid(row=2, ipadx=10, ipady=10, pady=5)
        btnupd.grid(row=3, ipadx=10, ipady=10, pady=5)
        btndel.grid(row=4, ipadx=10, ipady=10, pady=5)
        btnsel.grid(row=5, ipadx=10, ipady=10, pady=5)
        btnadv.grid(row=6, ipadx=10, ipady=10, pady=5)
        btnback.grid(row=7, ipadx=10, ipady=10, pady=5)
