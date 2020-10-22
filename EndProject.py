from tkinter import *
import datetime
import os #operating system- for the files
'''
def lateAttReport():
'''


def monthlyAttReport():
    global screen7
    screen7 = Toplevel(screen)  # opens a new "window"
    screen7.title("Generate Monthly Report")
    screen7.geometry("300x250")
    currmonth = now.strftime("%m")



def employeeAttReportGenerate():
    idReport = idToReport.get()
    with open('Employees.txt', "r") as f:
        lines = f.readlines()
    if idReport+"\n" not in lines:
        Label(screen6, text="Id is not registered in the system", fg="red").pack()
    else:
        with open('Attendance.txt', "r") as f:
            lines2 = f.readlines()
        numOfLines = len(lines2)
        for i in range(numOfLines):
            if lines2[i] == idReport+"\n":
                print(lines2[i + 1], lines2[i + 2])
                i = i+2
        Label(screen6, text="Attendance Report Generated In Console", fg="green").pack()



def employeeAttReport():
    global screen6
    global idToReport
    global idToReport_entry
    screen6 = Toplevel(screen)  # opens a new "window"
    screen6.title("Mark Attendance")
    screen6.geometry("300x250")
    idToReport = StringVar()
    Label(screen6, text="Please enter ID:").pack()
    Label(screen6, text="").pack()
    Label(screen6, text="ID *").pack()
    Label(screen6, text="").pack()
    idToReport_entry = Entry(screen6, textvariable=idToReport).pack()
    Button(screen6, text="Generate Report", height="1", width="12", bg="pink", command=employeeAttReportGenerate).pack()

def markAttendance():
    idAttend = idToAttend.get()
    with open('Employees.txt', "r") as f:
        lines = f.readlines()
    if idAttend+"\n" not in lines:
        Label(screen5, text="Id is not registered to the system", fg="red").pack()
    else:
        with open('Attendance.txt', "a") as f:
            f.write(idAttend+'\n')
            now = datetime.datetime.now()
            d = now.strftime("%d/%m/%Y"+"\n")
            f.write(d)
            t = now.strftime("%H:%M" + "\n")
            f.write(t)
        Label(screen5, text="Successful log", fg="green").pack()


def logEmployee():
    global screen5
    global idToAttend
    global idToAttend_entry
    screen5 = Toplevel(screen)  # opens a new "window"
    screen5.title("Mark Attendance")
    screen5.geometry("300x250")
    idToAttend = StringVar()
    Label(screen5, text="Please enter ID:").pack()
    Label(screen5, text="").pack()
    Label(screen5, text="ID *").pack()
    Label(screen5, text="").pack()
    idToAttend_entry = Entry(screen5, textvariable=idToAttend).pack()
    Button(screen5, text="Log ID", height="1", width="10", bg="pink", command=markAttendance).pack()

def theDeleteFromFile():
    fpToDelete = fp1.get()
    with open(fpToDelete, "r") as f:
        idsToDelete = f.readlines() #has the list of IDs to delete
    if len(idsToDelete) == 0:
        Label(screen4, text="There's no ID to delete", fg="red").pack()
    else:
        with open('Employees.txt', "r") as f:
            lines = f.readlines()
        for id in idsToDelete:
            idx = lines.index(id)
            numoflines = len(lines)
            for i in range(numoflines):
                if i != idx and i != idx + 1 and i != idx + 2 and i != idx + 3:
                    f.write(lines[i])
        Label(screen4, text="Delete Completed", fg="green").pack()

def deleteEmployeeFromFile():
    global screen4
    global fp1
    global fp_entry1
    screen4 = Toplevel(screen)  # opens a new "window"
    screen4.title("Delete Employee From File")
    screen4.geometry("300x250")
    fp1 = StringVar()
    Label(screen4, text="Please enter the file name:").pack()
    Label(screen4, text="").pack()
    Label(screen4, text="File Name *").pack()
    Label(screen4, text="").pack()
    fp_entry1 = Entry(screen4, textvariable=fp1).pack()
    Button(screen4, text="Delete", height="1", width="10", bg="pink", command=theDeleteFromFile).pack()

def theDelete():
    id_delete = idToDelete.get()
    with open('Employees.txt', "r") as f:
        lines = f.readlines()
    if id_delete+"\n" in lines:
        with open('Employees.txt', "w") as f:
            idx = lines.index(id_delete+"\n")
            numoflines = len(lines)
            for i in range(numoflines):
                if i != idx and i != idx + 1 and i != idx + 2 and i != idx + 3:
                    f.write(lines[i])
            Label(screen3, text="Delete Completed", fg="green").pack()
    else:
        Label(screen3, text="There's no ID to delete", fg="red").pack()

def deleteEmployee():
    global screen3
    global idToDelete
    global idToDelete_entry
    screen3 = Toplevel(screen)  # opens a new "window"
    screen3.title("Delete Employee")
    screen3.geometry("300x250")
    idToDelete = StringVar()
    Label(screen3, text="Please enter the Employee ID to delete:").pack()
    Label(screen3, text="").pack()
    Label(screen3, text="Id *").pack()
    idToDelete_entry = Entry(screen3, textvariable=idToDelete).pack()
    Label(screen3, text="").pack()
    Button(screen3, text="Delete", height="1", width="10", bg="pink", command=theDelete).pack()

def enterEmployeeFromFile():
    fp_name = fp.get()
    file = open(fp_name, "r")
    file_employee = open('Employees.txt', "a")
    while True:
        id_info = file.readline()
        if not id_info:
            break
        name_info = file.readline()
        if not name_info:
            Label(screen2, text="There's not name information for employee" + id_info, fg="red").pack()
            break
        phone_info = file.readline()
        if not phone_info:
            Label(screen2, text="There's not phone information for employee" + id_info, fg="red").pack()
            break
        age_info = file.readline()
        if not age_info:
            Label(screen2, text="There's not age information for employee" + id_info, fg="red").pack()
            break
        file_employee.write(id_info + "\n")
        file_employee.write(name_info + "\n")
        file_employee.write(phone_info + "\n")
        file_employee.write(age_info + "\n")
    file_employee.close()
    file.close()
    with open('Employees.txt') as file:
        if id_info in file.read():
            Label(screen1, text="This Employee ID already exists, Please try again", fg="red").pack()
        else:
            file = open("Employees.txt", "a")
            file.write("\n")
            file.write(id_info + "\n")
            file.write(name_info + "\n")
            file.write(phone_info + "\n")
            file.write(age_info)
            file.close()
            Label(screen1, text="Registration successfull", fg="green").pack()

def registerNewEmployeeFromFile():
    global screen2
    global fp
    global fp_entry
    fp= StringVar()
    screen2 = Toplevel(screen)  # opens a new "window"
    screen2.title("Register From File")
    screen2.geometry("300x250")
    Label(screen2, text="Please enter the file name:").pack()
    Label(screen2, text="").pack()
    Label(screen2, text="File Name *").pack()
    fp_entry = Entry(screen2, textvariable=fp).pack()
    Button(screen2, text="Register", height="1", width="10", bg="pink", command=enterEmployeeFromFile).pack()

def enterEmployee():
    id_info = id.get()
    name_info = name.get()
    phone_info = phone.get()
    age_info = age.get()
    with open('Employees.txt') as file:
        if id_info in file.read():
            Label(screen1, text="This Employee ID already exists, Please try again", fg="red").pack()
        else:
            file = open("Employees.txt", "a")
            file.write("\n")
            file.write(id_info + "\n")
            file.write(name_info + "\n")
            file.write(phone_info + "\n")
            file.write(age_info)
            file.close()
            Label(screen1, text="Registration successfull", fg="green").pack()

def registerNewEmployee():
    global screen1
    global id, name, phone, age
    global id_entry, name_entry, phone_entry, age_entry

    screen1 = Toplevel(screen) #opens a new "window"
    screen1.title("Register")
    screen1.geometry("300x250")
    Label(screen1, text="Please enter the following details:").pack()
    Label(screen1, text="").pack()
    id= StringVar()
    name= StringVar()
    phone = StringVar()
    age= StringVar()
    Label(screen1, text="Id *").pack()
    id_entry= Entry(screen1, textvariable= id).pack()
    Label(screen1, text="Name *").pack()
    name_entry= Entry(screen1, textvariable=name).pack()
    Label(screen1, text="Phone *").pack()
    phone_entry= Entry(screen1, textvariable=phone).pack()
    Label(screen1, text="Age *").pack()
    age_entry= Entry(screen1, textvariable=age).pack()
    Label(screen1, text="").pack()
    Button(screen1, text="Register", height="1", width="10", bg="pink", command=enterEmployee).pack()

def mainScreen():
    global screen
    screen= Tk()
    screen.geometry("300x250")
    screen.title("Employee Management System")
    Label(text="Employee Management System", bg="light blue", font=("Ariel",14)).pack()
    Label(text="").pack()  # acts as /n
    Label(text="Hello! Welcome to the Employee Management System!", font=("Ariel",12)).pack()
    Label(text="").pack()
    Label(text="").pack()
    Button(text="Add New Employee", height="1", width="25", command=registerNewEmployee).pack()
    Button(text="Add Employee From File", height="1", width="25", command=registerNewEmployeeFromFile).pack()
    Button(text="Delete Employee", height="1", width="25", command=deleteEmployee).pack()
    Button(text="Delete Employee From File", height="1", width="25", command=deleteEmployeeFromFile).pack()
    Button(text="Log Attendance", height="1", width="25", command=logEmployee).pack()
    Button(text="Employee Attendance Report", height="1", width="25", command=employeeAttReport).pack()
    Button(text="Monthly Attendance Report", height="1", width="27", command=monthlyAttReport).pack()
    '''
    Button(text="Late Attendance Report", height="1", width="27", command=lateAttReport).pack()
        '''
    screen.mainloop()

mainScreen()