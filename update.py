from tkinter import *
import mainwindow
import tkinter.messagebox
import sqlop

class update():
    def upd_S(self):
        ssno = self.sinput1.get()
        ssname = self.sinput2.get()
        ssex = self.sinput3.get()
        sage = self.sinput4.get()
        sdepth = self.sinput5.get()
        old = {"sno": ssname, "sname": ssname, "ssex": ssex, "sage": sage, "sdept": sdepth}
        if ssno == "" and ssname == "" and ssex == "" and sage == "" and sdepth == "":
            tkinter.messagebox.showinfo("提示",message="请输入要更新数据的筛选条件")
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
        new_ssno = self.updsinput1.get()
        new_ssname = self.updsinput2.get()
        new_ssex = self.updsinput3.get()
        new_sage = self.updsinput4.get()
        new_sdepth = self.updsinput5.get()
        new={"sno":new_ssname,"sname":new_ssname,"ssex":new_ssex,"sage":new_sage,"sdept":new_sdepth}
        a = sqlop.sql()
        a.opupdate(self.root,st,old,new,1)  # st为用户输入的更新条件
        a.shutdown()
        return

    def upd_SC(self):
        sno = self.scinput1.get()
        cno = self.scinput2.get()
        grade = self.scinput3.get()
        old = {"sno": sno, "cno": cno, "grade": grade}
        if sno == "" and cno == "" and grade == "":
            tkinter.messagebox.showinfo("提示", message="请输入要更新数据的筛选条件")
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
        sno = self.updscinput1.get()
        cno = self.updscinput2.get()
        grade = self.updscinput3.get()
        new = {"sno": sno, "cno": cno, "grade": grade}
        a = sqlop.sql()
        a.opupdate(self.root,st,old,new,2)
        a.shutdown()
        return

    def upd_C(self):
        cno = self.cinput1.get()
        cname = self.cinput2.get()
        ccredit = self.cinput3.get()
        old = {"cno": cno, "cname": cname, "ccredit": ccredit}
        if cno == "" and cname == "" and ccredit == "":
            tkinter.messagebox.showinfo("提示", message="请输入要更新数据的筛选条件")
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
        cno = self.updcinput1.get()
        cname = self.updcinput2.get()
        ccredit = self.updcinput3.get()
        new = {"cno": cno, "cname": cname, "ccredit": ccredit}
        a = sqlop.sql()
        a.opupdate(self.root,st,old,new,3)
        a.shutdown()

        return

    def reback(self):
        self.initface.destroy()
        mainwindow.mainwindow(self.root)

    def __init__(self, master):
        self.root = master
        self.root.title('更新')
        self.initface = Frame(self.root)
        self.initface.grid()

        Label(self.initface, text='学号').grid(row=0, column=1)
        Label(self.initface, text='姓名').grid(row=0, column=2)
        Label(self.initface, text='性别').grid(row=0, column=3)
        Label(self.initface, text='年龄').grid(row=0, column=4)
        Label(self.initface, text='专业').grid(row=0, column=5)

        lb1 = Label(self.initface, text='S表')
        lb1.grid(row=1, pady=6, padx=5)
        self.sinput1 = Entry(self.initface, width=14)
        self.sinput2 = Entry(self.initface, width=14)
        self.sinput3 = Entry(self.initface, width=14)
        self.sinput4 = Entry(self.initface, width=14)
        self.sinput5 = Entry(self.initface, width=14)
        self.sinput1.grid(row=1, column=1, padx=5)
        self.sinput2.grid(row=1, column=2, padx=5)
        self.sinput3.grid(row=1, column=3, padx=5)
        self.sinput4.grid(row=1, column=4, padx=5)
        self.sinput5.grid(row=1, column=5, padx=5)

        lb1upd = Label(self.initface, text='更新为')
        lb1upd.grid(row=2, pady=6, padx=5)
        self.updsinput1 = Entry(self.initface, width=14)
        self.updsinput2 = Entry(self.initface, width=14)
        self.updsinput3 = Entry(self.initface, width=14)
        self.updsinput4 = Entry(self.initface, width=14)
        self.updsinput5 = Entry(self.initface, width=14)
        self.updsinput1.grid(row=2, column=1, padx=5)
        self.updsinput2.grid(row=2, column=2, padx=5)
        self.updsinput3.grid(row=2, column=3, padx=5)
        self.updsinput4.grid(row=2, column=4, padx=5)
        self.updsinput5.grid(row=2, column=5, padx=5)

        Label(self.initface, text='学号').grid(row=3, column=1)
        Label(self.initface, text='课程号').grid(row=3, column=2)
        Label(self.initface, text='成绩').grid(row=3, column=3)

        lb2 = Label(self.initface, text='SC表')
        lb2.grid(row=4, pady=6, padx=5)
        self.scinput1 = Entry(self.initface, width=14)
        self.scinput2 = Entry(self.initface, width=14)
        self.scinput3 = Entry(self.initface, width=14)
        self.scinput1.grid(row=4, column=1, padx=5)
        self.scinput2.grid(row=4, column=2, padx=5)
        self.scinput3.grid(row=4, column=3, padx=5)

        lb2upd = Label(self.initface, text='更新为')
        lb2upd.grid(row=5, pady=6, padx=5)
        self.updscinput1 = Entry(self.initface, width=14)
        self.updscinput2 = Entry(self.initface, width=14)
        self.updscinput3 = Entry(self.initface, width=14)
        self.updscinput1.grid(row=5, column=1, padx=5)
        self.updscinput2.grid(row=5, column=2, padx=5)
        self.updscinput3.grid(row=5, column=3, padx=5)

        Label(self.initface, text='课程号').grid(row=6, column=1)
        Label(self.initface, text='课程名').grid(row=6, column=2)
        Label(self.initface, text='学分').grid(row=6, column=3)

        lb3 = Label(self.initface, text='C表')
        lb3.grid(row=7, pady=6, padx=5)
        self.cinput1 = Entry(self.initface, width=14)
        self.cinput2 = Entry(self.initface, width=14)
        self.cinput3 = Entry(self.initface, width=14)
        self.cinput1.grid(row=7, column=1, padx=5)
        self.cinput2.grid(row=7, column=2, padx=5)
        self.cinput3.grid(row=7, column=3, padx=5)

        lb3upd = Label(self.initface, text='更新为')
        lb3upd.grid(row=8, pady=6, padx=5)
        self.updcinput1 = Entry(self.initface, width=14)
        self.updcinput2 = Entry(self.initface, width=14)
        self.updcinput3 = Entry(self.initface, width=14)
        self.updcinput1.grid(row=8, column=1, padx=5)
        self.updcinput2.grid(row=8, column=2, padx=5)
        self.updcinput3.grid(row=8, column=3, padx=5)

        Button(self.initface, text='更新S表', command=self.upd_S).grid(row=9, column=1)
        Button(self.initface, text='更新SC表', command=self.upd_SC).grid(row=9, column=2)
        Button(self.initface, text='更新C表', command=self.upd_C).grid(row=9, column=3)
        Button(self.initface, text='返回', command=self.reback).grid(row=9, column=4)
