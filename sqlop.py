import pymysql
import tkinter.messagebox
from tkinter import *
import string


class sql():
    #初始化数据库，用于和本地mysql数据库进行连接
    def __init__(self):
        self.conn = pymysql.connect(host='127.0.0.1'  # 连接名称，默认127.0.0.1
                                    , user='root'  # 用户名
                                    , passwd='abczzq123456789'  # 密码
                                    , port=3306  # 端口，默认为3306
                                    , db='school'  # 数据库名称
                                    , charset='utf8'  # 字符编码
                                    )

        self.cur = self.conn.cursor()  # 生成游标对象

    #在数据库中执行insert插入操作
    def opadd(self, sql):
        try:
            self.cur.execute(sql)
            self.conn.commit()
            return 1
        except Exception as e:
            tkinter.messagebox.showinfo("提示", message=e)
            return -1

    #在数据库中执行select查询操作
    def opselect(self, sql, root):
        try:
            self.cur.execute(sql)
            li = sql.split(" ")
            for i in li:
                if i == 's':
                    flag = 1
                    break
                elif i == 'sc':
                    flag = 2
                    break
                elif i == 'c':
                    flag = 3
                    break
            data = self.cur.fetchall()
            if not data:
                tkinter.messagebox.showinfo('提示', '没有符合条件的数据')
            else:
                dtas = Toplevel(root)
                cont = Text(dtas)
                cont.grid()
                if flag == 1:
                    cont.insert(END, "   学号       姓名    性别     年龄     专业\n\n")
                elif flag == 2:
                    cont.insert(END, "   学号   课程号   成绩\n\n")
                elif flag == 3:
                    cont.insert(END, " 课程号   课程名   学分\n\n")
                for i in data:
                    for j in i:
                        cont.insert(END, " ")
                        cont.insert(END, j)
                        cont.insert(END, "    ")
                    cont.insert(END, '\n\n')
            return data
        except Exception as e:
            tkinter.messagebox.showinfo("提示", message=e)

    #在数据库中执行delete删除操作
    def opdelete(self, sql):
        try:
            self.cur.execute(sql)
            if tkinter.messagebox.askokcancel(title='警告', message='请再次确认删除数据？'):
                self.conn.commit()
                tkinter.messagebox.showinfo('提示', '删除成功')
            else:
                tkinter.messagebox.showinfo('温馨提示', '数据未删除成功')
        except Exception as e:
            tkinter.messagebox.showinfo("提示", message=e)
            return -1

    #在数据库中执行update更新操作
    def opupdate(self, root, condi, old, new, flag):
        if flag == 1:
            name = "s"
        elif flag == 2:
            name = "sc"
        else:
            name = "c"
        str = "select * from " + name + " where " + condi
        data=self.opselect(str, root)
        if not data:
            return
        info = list()
        str = ""
        keys = old.keys()
        for i in keys:
            if old[i] != new[i] and new[i]!="":
                info.append(i)
                str += i + "的值" + "变为" + new[i] + " "
        upd = ""
        for i in range(len(info)):
            if info[i] != 'grade' or info[i] != 'ccredit' or info[i] != 'sage':
                upd = upd + info[i] + " = " + '\'' + new[info[i]] + '\''
            else:
                upd = upd + info[i] + " = " + new[info[i]]
            if i != len(info) - 1: upd += " and "
        if len(info) != 0 and tkinter.messagebox.askokcancel(title="提示", message="您确定将" + str):
            sql = "update " + name + " set " + upd + " where " + condi
            print(sql)
            if tkinter.messagebox.askokcancel(title="提示", message="您确定要更新数据吗"):
                try:
                    self.cur.execute(sql)
                    self.conn.commit()
                    tkinter.messagebox.showinfo("提示", "更新成功")
                except Exception as e:
                    tkinter.messagebox.showinfo("提示", message=e)
        return

    #该函数用于高级操作模块，用于执行从该模块中返回的任意SQL语句
    def func(self,sql):
        try:
            self.cur.execute(sql)
            self.conn.commit()
            tkinter.messagebox.showinfo("提示",message="执行成功")
        except Exception as e:
            tkinter.messagebox.showinfo("提示",message=e)

    #关闭与本地mysql数据库的连接
    def shutdown(self):
        self.cur.close()  #关闭游标
        self.conn.close() #关闭连接
