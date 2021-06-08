from tkinter import *
import sqlop
import mainwindow
import tkinter.messagebox
class advanced():
    def exectue(self):
        sql=self.text.get('1.0',END)
        a=sqlop.sql()
        a.func(sql)
        return
    def reback(self):
        self.interface.destroy()
        mainwindow.mainwindow(self.root)
    def __init__(self,master):
        self.root=master
        self.interface=Frame(self.root)
        self.interface.grid()
        self.text=Text(self.interface,height=22,width=100)
        self.text.grid(row=0)
        button=Button(self.interface, text="执行", fg='black', font=('黑体',12), command=self.exectue)
        button2 = Button(self.interface, text="返回", fg='black', font=('黑体', 12), command=self.reback)
        button.grid(row=1,pady=5)
        button2.grid(row=2,pady=5)