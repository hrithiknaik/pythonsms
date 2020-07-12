from tkinter import *
from tkinter.messagebox import *
from tkinter.scrolledtext import *
from sqlite3 import *
import socket
import requests
import bs4
import sqlite3
import matplotlib.pyplot as plt

def f1():
	adst.deiconify()
	root.withdraw()
def f2():
	root.deiconify()
	adst.withdraw()
def f3():
	vist.deiconify()
	root.withdraw()
	vist_stdata.delete(1.0, END)
	con = None
	try:
		con = connect("student.db")
		cursor = con.cursor()
		sql = "select * from student"
		cursor.execute(sql)
		data = cursor.fetchall()
		msg = ""
		for d in data:
			msg = msg + "rno :" + str(d[0]) +  "  "  + "name : " + str(d[1]) + " "  + "marks :" + str(d[2]) +  "\n"
		vist_stdata.insert(INSERT, msg)
	except Exception as e:
		showerror("Issue", e)
	finally:
		if con is not None:
			con.close()
def f4():
	root.deiconify()
	vist.withdraw()

def f5():
	con = None
	try:
		
		if len(adst_entrno.get()) == 0:
			showerror("error","Enter rno")
		if len(adst_entname.get()) == 0:
			showerror("error","Enter name")
		if len(adst_entmarks.get()) == 0:
			showerror("error","Enter marks")
		
		
		con = connect("student.db")
		cursor = con.cursor()
		sql = "insert into student values('%d' , '%s','%d')"
		rno = int(adst_entrno.get())
		name = adst_entname.get()
		marks = int(adst_entmarks.get())
		if  rno<1:
	
			showerror("error","rno cannot be negative or 0")
		elif len(name) < 3:
			showerror("Error", "name cannot be less than 2 characters")
		elif not name.isalpha():
			showerror("Error","name shud contain only characters")
		elif marks<0 or marks>100:
			showerror("Error","marks needs to be between 0 to 100")

		else:
			cursor.execute(sql % (rno,name,marks))
			con.commit()
			showinfo("success" , "record added")
	except Exception as e:
		con.rollback()
		showerror("Issue", e)
	finally:
		if con is not None:
			con.close()
		adst_entrno.delete(0,END)
		adst_entname.delete(0,END)
		adst_entmarks.delete(0,END)
		adst_entrno.focus()
def f6():
	upst.deiconify()
	root.withdraw()
def f7():
	root.deiconify()
	upst.withdraw()
def f8():
	con = None
	try:
		
		if len(upst_entrno.get()) == 0:
			showerror("error","Enter rno")
		if len(upst_entname.get()) == 0:
			showerror("error","Enter name")
		if len(upst_entmarks.get()) == 0:
			showerror("error","Enter marks")
		
		con = connect("student.db")
		cursor = con.cursor()
		sql = "update student set name ='%s' , marks='%d' where rno='%d' "
		rno = int(upst_entrno.get())
		name = upst_entname.get()
		marks = int(upst_entmarks.get())
		if  rno<1:

			showerror("error","rno cannot be negative or 0")
		elif len(name) < 2:
			showerror("Error", "name cannot be less than 2 characters")
		elif not name.isalpha():
			showerror("Error","name shud contain only characters")
		elif marks<0 or marks>100:
			showerror("Error","marks needs to be between 0 to 100")

		else:
			cursor.execute(sql % (name,marks,rno))
			if cursor.rowcount > 0:
				con.commit()
				showinfo("success" , "record updated")
			else:
				showerror("error","record does not exists")
	except Exception as e:
		con.rollback()
		showerror("Issue", e)
	finally:
		if con is not None:
			con.close()
		upst_entrno.delete(0,END)
		upst_entname.delete(0,END)
		upst_entmarks.delete(0,END)
		upst_entrno.focus()
def f9():
	try:
		con = sqlite3.connect("student.db")
		cursor = con.cursor()
		sql = "select name,marks from student"
		cursor.execute(sql)
		data = cursor.fetchall()
		name = []
		marks = []
		for r in data:
			name.append(r[0])
			marks.append(r[1])
		plt.bar(name,marks,width=0.25,color = ['red','black','blue'])
		plt.title("Batch Informartion")
		plt.xlabel("Names")
		plt.ylabel("Marks")
		
		plt.show()	
	
	except Exception as e:
		showerror("error" , e)

def f10():
	con = None
	try:
		if len(dest_entrno.get()) == 0:
			showerror("error","Enter rno")
		con = connect("student.db")
		cursor = con.cursor()
		sql = "delete from student where rno = '%d'"
		rno = int(dest_entrno.get())
		
		if rno<1:
			showerror("error", "rno cannot be negative or 0")
		else:
			cursor.execute(sql%(rno))
			if cursor.rowcount > 0:
				con.commit()
				showinfo("success","Record deleted")
			else:
				showerror("error", "Record does not exists")
	except Exception as e:
		con.rollback()
		showerror("Issue", e)
	finally:
		if con is not None:
			con.close()
		dest_entrno.delete(0,END)
		dest_entrno.focus()	
def f11():
	dest.deiconify()
	root.withdraw()
def f12():
	root.deiconify()
	dest.withdraw()


	

root = Tk()
root.title("S.M.S")
root.geometry("520x450+400+100")
root.configure(background = '#CCFF99')


btnadd = Button(root, text="Add" ,width = 10,font=("arial",13,"bold"),command=f1)
btnview = Button(root, text="View" ,width = 10, font=("arial",13,"bold"),command=f3)
btnupdate = Button(root, text="Update" ,width = 10,font=("arial",13,"bold"),command=f6)
btndelete = Button(root, text="Delete" ,width = 10, font=("arial",13,"bold"),command=f11)
btncharts = Button(root, text="Charts" ,width = 10,font=("arial",13,"bold"),command = f9)
stdata = Text(root,width=40, height=1,background = '#CCFF99', font=("arial",20,"bold"))
stdata1 = Text(root,width=50, height=3,background = '#CCFF99', font=("arial",15,"bold"))


btnadd.pack(pady=10)
btnview.pack(pady=10)
btnupdate.pack(pady=10)
btndelete.pack(pady=10)
btncharts.pack(pady=10)
stdata.pack(pady=10)
stdata1.pack(pady=10)
try:
	
	res = requests.get("https://ipinfo.io")
	data = res.json()
	city = data['city']

	a1 = "http://api.openweathermap.org/data/2.5/weather?units=metric"
	a2 = "&q=" + city 
	a3 = "&appid=c6e315d09197cec231495138183954bd"
	api_address =  a1 + a2  + a3 		
	res = requests.get(api_address)
	
	data=res.json()
	main=data['main']

	t=main['temp']
	p = str(t)
	msg = " " + "Location :" + city+  "     " + "Temp : " + p + "°C"
	stdata.insert(INSERT, msg)
except Exception as e:
	showerror("issue",e)

try:
	
	r = requests.get("https://www.brainyquote.com/quote_of_the_day")	
	soup=bs4.BeautifulSoup(r.text,"lxml")
	data=soup.find("img",{"class":"p-qotd"})
	txt = data['alt']
	msg1 = "QOTD:" + " " + txt
	stdata1.insert(INSERT,msg1)

except Exception as e:
	showerror("issue ",e)

adst = Toplevel(root)
adst.title("Add st. ")
adst.geometry("500x400+400+100")


adst_lblrno = Label(adst, text="enter rno ", font=("arial",10,"bold") )
adst_entrno = Entry(adst, bd =5, font=("arial",10,"bold") )
adst_lblname = Label(adst, text="enter name ", font=("arial",10,"bold") )
adst_entname = Entry(adst, bd=5, font=("arial",10,"bold") )
adst_lblmarks = Label(adst, text="enter marks ", font=("arial",10,"bold") )
adst_entmarks = Entry(adst, bd=5, font=("arial",10,"bold") )
adst_btnsave = Button(adst, text="Save ", font=("arial",10,"bold") , command = f5)
adst_btnback = Button(adst, text="Back ", font=("arial",10,"bold"),command=f2 )

adst_lblrno.pack(pady=10)
adst_entrno.pack(pady=10)
adst_lblname.pack(pady=10)
adst_entname.pack(pady=10)
adst_lblmarks.pack(pady=10)
adst_entmarks.pack(pady=10)
adst_btnsave.pack(pady=10)
adst_btnback.pack(pady=10)
adst.withdraw()

vist = Toplevel(root)
vist.title("View st. ")
vist.geometry("500x400+400+100")
vist.configure(background = '#E0E0E0')
vist_stdata = ScrolledText(vist,width=30, height=10,background = '#E0E0E0',font=("arial",18,"bold"))
vist_btnback = Button(vist, text="Back",font=("arial",18,"bold"),command=f4)
vist_stdata.pack(pady=10)
vist_btnback.pack(pady=10)
vist.withdraw()

upst = Toplevel(root)
upst.title("Update st. ")
upst.geometry("500x400+400+100")

upst_lblrno = Label(upst, text="enter rno ", font=("arial",10,"bold") )
upst_entrno = Entry(upst, bd =5, font=("arial",10,"bold") )
upst_lblname = Label(upst, text="enter name ", font=("arial",10,"bold") )
upst_entname = Entry(upst, bd=5, font=("arial",10,"bold") )
upst_lblmarks = Label(upst, text="enter marks ", font=("arial",10,"bold") )
upst_entmarks = Entry(upst, bd=5, font=("arial",10,"bold") )
upst_btnsave = Button(upst, text="Save ", font=("arial",10,"bold"),command=f8 )
upst_btnback = Button(upst, text="Back ", font=("arial",10,"bold"),command=f7)

upst_lblrno.pack(pady=10)
upst_entrno.pack(pady=10)
upst_lblname.pack(pady=10)
upst_entname.pack(pady=10)
upst_lblmarks.pack(pady=10)
upst_entmarks.pack(pady=10)
upst_btnsave.pack(pady=10)
upst_btnback.pack(pady=10)
upst.withdraw()

dest = Toplevel(root)
dest.title("Delete st. ")
dest.geometry("500x400+400+100")
dest_lblrno = Label(dest, text="enter rno ", font=("arial",10,"bold") )
dest_entrno = Entry(dest, bd =5, font=("arial",10,"bold") )
dest_btnsave = Button(dest, text="Save ", font=("arial",10,"bold"),command=f10 )
dest_btnback = Button(dest, text="Back ", font=("arial",10,"bold"),command=f12)

dest_lblrno.pack(pady=10)
dest_entrno.pack(pady=10)
dest_btnsave.pack(pady=10)
dest_btnback.pack(pady=10)
dest.withdraw()

root.mainloop()