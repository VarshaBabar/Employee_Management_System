from tkinter import *
from tkinter.messagebox import *
from tkinter.scrolledtext import *
from sqlite3 import *
import pandas as pd
import matplotlib.pyplot as plt
from tkinter import filedialog
from requests import *
import re
from pyrebase import *


firebaseConfig = {
	"apiKey": "AIzaSyDpXRzRzHect_tMsyiHDSuUTR7P8xWtTNk",
	"authDomain": "employee-402ee.firebaseapp.com",
	"databaseURL":"https://employee-402ee-default-rtdb.firebaseio.com/",
	"projectId": "employee-402ee",
	"storageBucket": "employee-402ee.appspot.com",
	"messagingSenderId": "778492114542",
	"appId": "1:778492114542:web:1fdbc06def23080a91187f",
	"measurementId": "G-TSJCWTQYTH"
}
fb = initialize_app(firebaseConfig)
db = fb.database()


screen = Tk()
screen.title("Employee manangement system")
screen.geometry("800x600+50+50")
t = ("Century" , 30 , "bold" , "italic")
f =("Century" , 20 , "bold" , "italic")

def login(): 
	username = "varsha" 
	password = "12345"

	if entUser.get() == username and entPass.get() == password:
		showinfo("Login Successful","You have logged in Successfully")
		root.deiconify()
		screen.withdraw()

	elif entUser.get() == username and entPass.get() != password: 	
		showerror('Wrong password','Please check your password')
		entPass.delete(0 , END)
		entPass.focus() 
        
	elif entUser.get() != username and entPass.get() == password: 	
		showerror('Wrong username','Please check your username') 
		entUser.delete(0 , END)
		entUser.focus()
        
	else: 
		showerror("Login Failed","Invalid Username and password")
		entUser.delete(0 , END)
		entPass.delete(0 , END)
		entUser.focus()

labtitle1 =Label(screen , text = " Employee Management System" , font = t)
labtitle1.place(x = 100 , y = 50)

lablogin =Label(screen , text = " Login Page " , font = f)
lablogin.place(x = 330 , y = 150)

labUser =Label(screen , text = " Enter Username " , font = f)
labUser.place(x = 300 , y = 220)

entUser = Entry(screen , font = f)
entUser.place(x = 250, y = 270)

labPass =Label(screen , text = " Enter Password " , font = f)
labPass.place(x = 300 , y = 370)

entPass = Entry(screen  , font = f , show = "*")
entPass.place(x = 250, y = 420)

btnLogin = Button(screen , text = "Login" , font = f , command = login)
btnLogin.place(x= 350, y =500 )




root = Toplevel(screen)
root.title("Employee manangement system")
root.geometry("800x700+50+50")
t = ("Century" , 25 , "bold" , "italic")
f =("Arial" , 15 , "bold" , "italic")
v = ("Arial" , 10 , "bold" )

def f1():
	AddEmp.deiconify()
	root.withdraw()
def f2():
	root.deiconify()
	AddEmp.withdraw()

"""def f3():
	ViewEmp.deiconify()
	root.withdraw()"""
def f4():
	root.deiconify()
	ViewEmp.withdraw()

def f5():
	UpdateEmp.deiconify()
	root.withdraw()
def f6():
	root.deiconify()
	UpdateEmp.withdraw()

def f7():
	DeleteEmp.deiconify()
	root.withdraw()
def f8():
	root.deiconify()
	DeleteEmp.withdraw()

def f9():
	ChartEmp.deiconify()
	root.withdraw()
def f10():
	root.deiconify()
	ChartEmp.withdraw()


labtitle =Label(root , text = " Employee Management System" , font = t)
labtitle.place(x = 100 , y = 30)

btnAdd = Button(root , text = "Add" , font = f ,width = 15, command = f1)
btnAdd.place(x = 250 , y = 100)

def View():
	ViewEmp.deiconify()
	root.withdraw()
	as_data.delete(1.0 , END)
	con = None
	try : 
		con = connect("emp.db")
		cursor = con.cursor()
		sql = "select * from emp"
		cursor.execute(sql)
		data = cursor.fetchall()
		info = " "
		for d in data :
			info = info + "ID : " + str(d[0]) +"\t"+ " Name : " + str(d[1]) +"\t"+ " Salary : " + str(d[2]) + "\n" 
		as_data.insert(INSERT , info)


	except Exception as e:
		showerror("issue" , e)
	finally:
		if con is not None:
			con.close()

	con = connect("emp.db")
	df = pd.read_sql('select * from emp', con)
	df.to_csv('emp.csv', index=False)
	con.close()

btnView = Button(root , text = "View" , font = f ,width = 15, command = View)
btnView.place(x = 250 , y = 200)

btnUpdate = Button(root , text = " Update " , font = f ,width = 15, command = f5)
btnUpdate.place(x = 250 , y = 300)

btnDelete = Button(root , text = " Delete " , font = f ,width = 15, command = f7)
btnDelete.place(x = 250 , y = 400)

btnChart = Button(root , text = " Charts " , font = f ,width = 15, command = f9)
btnChart.place(x = 250 , y = 500)




def location():
	try:
		url = 'http://ipinfo.io/json'
		res = get(url)
		if res.status_code == 200:
			data = res.json()
			city = data['city']	
			msg = str(city)
			labLoc.configure(text=msg)
		else:
			labLoc.configure("issue" + str(res.status_code))
	except Exception as e:
		entLoc.configure("issue" + str(e))
	

btnLoc =Button(root , text = "Location " , font = f ,command = location)
btnLoc.place(x = 50 , y = 600)

labLoc = Label(root , font = f )
labLoc.place(x = 200 , y = 600)


def temp():
	try:
		apiKey = "84f8c0289aa3c0e18cadf5397e629f1f"
		baseURL = 'https://api.openweathermap.org/data/2.5/weather?q='
		city = labLoc.cget("text")
		completeURL = baseURL + city + "&appid=" + apiKey
		res = get(completeURL)
		if res.status_code == 200:
			data = res.json()
			temp = 	data["main"]["temp"]
			msg = str(temp)
			labTemp.configure(text=msg)
		else:
			labTemp.configure("issue" + str(res.status_code))
	except Exception as e:
		labTemp.configure("issue" + str(e))


btnTemp =Button(root , text = "temperature " , font = f , command = temp)
btnTemp.place(x = 400 , y = 600)

labTemp = Label(root , font = f )
labTemp.place(x = 550 , y = 600)

def add():
	ID = entID.get()
	name = entName.get()
	salary = entSalary.get()

	if not entID.get():
		showerror("Issue" , "You did not enter ID")
		entID.focus()
		return

	if not ID.isdigit():
		showerror("Issue" , "ID contain only digit")
		entID.delete(0 , END)
		entID.focus()
		return

	if not entName.get():
		showerror("Issue" , "You did not enter name")		
		entName.focus()
		return

	if name.isdigit():
		showerror("Issue" , "name is contain only alphabets")
		entName.delete(0 , END)
		entName.focus()
		return
	
	while True:
		if name != '' and all(chr.isalpha() or chr.isspace() for chr in name):
			break
		else:
			showerror("Issue" , " Name is contain only alphabets")
			entName.delete(0 , END)
			entName.focus()
			return

	if name.isspace():
		showerror("Issue" , "name is contain only alphabets")
		entName.delete(0 , END)
		entName.focus()
		return

	if not entSalary.get():
		showerror("Issue" , "You did not enter salary")
		entSalary.focus()
		return

	if not salary.isdigit():
		showerror("Issue" , "Salary contain only digit")
		entSalary.delete(0 , END)
		entSalary.focus()
		return

	ID = int(entID.get())
	salary = int(entSalary.get())

	con = None
	try :
		con = connect("emp.db")
		cursor = con.cursor()
		sql = "insert into emp values('%d','%s','%d')"
		cursor.execute(sql % (ID , name , salary))
		con.commit()
		showinfo("Done","added")
		entID.delete(0 , END)
		entName.delete(0 , END)
		entSalary.delete(0 , END)
		entID.focus()
	except Exception as e:
		msg= "issue: " + str(e)
		showerror("issue" ,msg)
	except ValueError as e:
		msg= "issue: " + str(e)
		showerror("issue" ,msg)
	finally :
		if con is not None:
			con.close()

	
	info = { "ID":ID , "name" : name , "salary" : salary}
	db.child("fb").push(info)


AddEmp = Toplevel(root)
AddEmp.title("Add Employee")
AddEmp.geometry("800x500+50+50")


lab = Label(AddEmp , text = "Add Employee" , font = t)
lab.place(x = 200, y =20)

labID = Label(AddEmp , text = "Enter Employee ID" , font = f)
labID.place(x = 50, y =100)

entID = Entry(AddEmp , font = f ,width = 20)
entID.place(x = 300 , y = 100)

labName = Label(AddEmp , text = "Enter Employee Name" , font = f)
labName.place(x = 50, y =200)

entName = Entry(AddEmp , font = f ,width = 20)
entName.place(x = 300 , y = 200)

labSalary = Label(AddEmp , text = "Enter Employee Salary" , font = f)
labSalary.place(x = 50, y =300)

entSalary = Entry(AddEmp , font = f ,width = 20)
entSalary.place(x = 300 , y = 300)

btnSave = Button(AddEmp , text = "save" , font = f ,width = 10 , command = add)
btnSave.place(x = 300 , y = 400)

btn = Button(AddEmp , text = "Back" , font = f ,width = 10 , command = f2)
btn.place(x = 50 , y = 400)



AddEmp.withdraw()




ViewEmp = Toplevel(root)
ViewEmp.title("View Employee")
ViewEmp.geometry("800x500+50+50")

lab = Label(ViewEmp , text = "Data of Employee" , font = t)
lab.place(x = 200, y =20)

as_data = ScrolledText(ViewEmp , width = 60 , height = 10 , font = f )
as_data.place(x= 50, y =100 )

as_btn = Button(ViewEmp , text = "Back" , font = f ,width = 10 , command = f4)
as_btn.place(x = 300 , y = 400)

ViewEmp.withdraw()

def Update():
	ID = up_entID.get()
	name = up_entName.get()
	salary = up_entSalary.get()


	if not up_entID.get():
		showerror("Issue" , "You did not enter ID")
		up_entID.focus()
		return

	if not ID.isdigit():
		showerror("Issue" , "ID contain only digit")
		up_entID.delete(0 , END)
		up_entID.focus()
		return

	if not up_entName.get():
		showerror("Issue" , "You did not enter name")		
		up_entName.focus()
		return

	if name.isdigit():
		showerror("Issue" , "name is contain only alphabets")
		up_entName.delete(0 , END)
		up_entName.focus()
		return
	
	while True:
		if name != '' and all(chr.isalpha() or chr.isspace() for chr in name):
			break
		else:
			showerror("Issue" , " Name is contain only alphabets")
			up_entName.delete(0 , END)
			up_entName.focus()
			return

	if name.isspace():
		showerror("Issue" , "name is contain only alphabets")
		up_entName.delete(0 , END)
		up_entName.focus()
		return


	if not up_entSalary.get():
		showerror("Issue" , "You did not enter salary")
		up_entSalary.focus()
		return

	if not salary.isdigit():
		showerror("Issue" , "Salary contain only digit")
		up_entSalary.delete(0 , END)
		up_entSalary.focus()
		return

	ID = int(up_entID.get())
	salary = int(up_entSalary.get())
	con = None 
	try:
		con = connect("emp.db")
		cursor = con.cursor()
		sql = "update emp set name = '%s' , salary ='%d' where ID  = '%d'"
		cursor.execute(sql % ( name  , salary , ID))
		con.commit()
		"""showinfo("Done","Update")
		up_entID.delete(0 , END)
		up_entName.delete(0 , END)
		up_entSalary.delete(0 , END)
		up_entID.focus()"""
	except Exception as e:
		msg= "issue: " + str(e)
		"""showerror("issue" ,msg)
		up_entID.delete(0 , END)
		up_entName.delete(0 , END)
		up_entSalary.delete(0 , END)
		up_entID.focus()"""
	except ValueError as e:
		msg= "issue: " + str(e)
		showerror("issue" ,msg)
	finally :
		if con is not None:
			con.close()

	ID = int(ID)
	emp_records = db.child("fb").get().val()
	record_key = None


	if emp_records:
		for key, value in emp_records.items():
			if value['ID'] == ID:
				record_key = key
				break


	if not record_key:
		showerror("Error", "Employee ID not found")
		up_entID.delete(0 , END)
		up_entName.delete(0 , END)
		up_entSalary.delete(0 , END)
		up_entID.focus()
		return

        # Update the data using the retrieved key
	updated_info = {"ID": ID , "name": name, "salary": salary}
	db.child("fb").child(record_key).update(updated_info)
	showinfo("Done", "Data Updated Successfully")
	up_entID.delete(0 , END)
	up_entName.delete(0 , END)
	up_entSalary.delete(0 , END)
	up_entID.focus()





UpdateEmp = Toplevel(root)
UpdateEmp.title("Update Employee")
UpdateEmp.geometry("800x500+50+50")

up_lab = Label(UpdateEmp , text = "Update Employee" , font = t)
up_lab.place(x = 100, y =20)

up_labID = Label(UpdateEmp , text = "Enter Employee ID" , font = f)
up_labID.place(x = 50, y =100)

up_entID = Entry(UpdateEmp , font = f ,width = 20)
up_entID.place(x = 300 , y = 100)

up_labName = Label(UpdateEmp , text = "Enter Employee Name" , font = f)
up_labName.place(x = 50, y =200)

up_entName = Entry(UpdateEmp , font = f ,width = 20)
up_entName.place(x = 300 , y = 200)

up_labSalary = Label(UpdateEmp , text = "Enter Employee Salary" , font = f)
up_labSalary.place(x = 50, y =300)

up_entSalary = Entry(UpdateEmp , font = f ,width = 20)
up_entSalary.place(x = 300 , y = 300)

up_btnSave = Button(UpdateEmp , text = "save" , font = f ,width = 10 , command = Update)
up_btnSave.place(x = 300 , y = 400)

up_btn = Button(UpdateEmp , text = "Back" , font = f ,width = 10 , command = f6)
up_btn.place(x = 50 , y = 400)

UpdateEmp.withdraw()



def delete():
	ID = as_entID.get()
	if not as_entID.get():
		showerror("Issue" , "You did not enter ID")
		as_entID.focus()
		return

	if not ID.isdigit():
		showerror("Issue" , "ID contain only digit")
		as_entID.delete(0 , END)
		as_entID.focus()
		return

	con = None 
	try:
		con = connect("emp.db")
		cursor = con.cursor()
		sql = "delete from emp where ID  = '%d'"
		ID = int(as_entID.get())
		cursor.execute(sql % (ID))
		if cursor.rowcount == 1:
			con.commit()
			"""showinfo("done","record deleted")
			as_entID.delete(0 , END)
			as_entID.focus()"""
		else :
			showinfo("issue" , "record does not exists")
			as_entID.delete(0 , END)
			as_entID.focus()
	except Exception as e:
		showerror("issue" , str(e))
		as_entID.delete(0 , END)
		as_entID.focus()
	finally:
		if con is not None:
			con.close()


	emp_id = int(ID)
	emp_records = db.child("fb").get().val()
	record_key = None

	if emp_records:
		for key, value in emp_records.items():
			if value['ID'] == emp_id:
				record_key = key
				break

	if not record_key:
		showinfo("done","Employee ID not found in Firebase")
		as_entID.delete(0 , END)
		as_entID.focus()
		return

	db.child("fb").child(record_key).remove()
	showinfo("done","Employee data deleted ")
	as_entID.delete(0 , END)
	as_entID.focus()
	return


DeleteEmp = Toplevel(root)
DeleteEmp.title(" Delete Employee")
DeleteEmp.geometry("800x500+50+50")

lab = Label(DeleteEmp , text = "Delete Employee" , font = t)
lab.place(x = 100, y =20)

labID = Label(DeleteEmp , text = "Enter Employee ID" , font = f)
labID.place(x = 50, y =100)

as_entID = Entry(DeleteEmp , font = f ,width = 20)
as_entID.place(x = 300 , y = 100)

btnSave = Button(DeleteEmp , text = "save" , font = f ,width = 10 , command = delete)
btnSave.place(x = 300 , y = 200)

btn = Button(DeleteEmp , text = "Back" , font = f ,width = 10 , command = f8)
btn.place(x = 50 , y = 200)

DeleteEmp.withdraw()


ChartEmp = Toplevel(root)
ChartEmp.title("Charts Employee")
ChartEmp.geometry("600x500+50+50")


def bar() :
	ChartEmp.deiconify()
	root.withdraw()
	data = pd.read_csv('emp.csv')
	df = pd.DataFrame(data)
	sorted_data = df.sort_values(by='salary', ascending=False)
	sd = sorted_data
	nd = sd.head(5)
	name = nd["name"].tolist()
	salary = nd["salary"].tolist()
	plt.bar(name ,salary , width = 0.5)
	plt.xlabel("Name")
	plt.ylabel("Salary")
	plt.title("Employee's salary")
	plt.show()

as_btn = Button(ChartEmp , text = "Show chart" , font = f ,width = 15 , command = bar)
as_btn.place(x = 200 , y = 100)

as_btn = Button(ChartEmp , text = "Back" , font = f ,width = 15 , command = f10)
as_btn.place(x = 200 , y = 300)

ChartEmp.withdraw()



def confirmExit():
	if askyesno('Exit' , 'Do you want to exit?'):
		root.destroy()
root.protocol('WM_DELETE_WINDOW' , confirmExit)




root.withdraw()

screen.mainloop()