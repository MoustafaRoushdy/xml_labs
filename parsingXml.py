import xml.etree.ElementTree as ET
from tkinter import * 



#-----------------------------------functions----------------------------------

def displayEmployee():
    global eName
    global ePhone
    global eAddress
    global eEmail
    eName = employees[currentEmployee].find("name").text
    ePhone = employees[currentEmployee].find("phone").text
    eAddress = employees[currentEmployee].find("address").text
    eEmail = employees[currentEmployee].find("email").text
    Email.delete(0,"end")
    Email.insert(0,eEmail)
    Name.delete(0,"end")
    Name.insert(0,eName)
    Phone.delete(0,"end")
    Phone.insert(0,ePhone)
    Address.delete(0,"end")
    Address.insert(0,eAddress)



def getPrev():
    global currentEmployee
    if currentEmployee == 0 :
        currentEmployee = 0 
    else :
        currentEmployee-=1
    displayEmployee()

def getNext():
    global currentEmployee
    if currentEmployee == len(employees)-1 :
        currentEmployee = len(employees)-1
    else :
        currentEmployee+=1
    displayEmployee()

def searchEmp():
    global currentEmployee
    for i , employee in enumerate(employees):
        if employee.find("name").text == Name.get():
            currentEmployee = i 
            break
    displayEmployee()

def createEmployee():
    employee = ET.SubElement(company,"employee")
    name = ET.SubElement(employee,"name")
    name.text = Name.get()
    phone = ET.SubElement(employee,"phone")
    phone.text = Phone.get()
    address = ET.SubElement(employee,"address")
    address.text = Address.get()
    email = ET.SubElement(employee,"email")
    email.text = Email.get()
    tree.write("company.xml")

def updateEmp():
    employees[currentEmployee].find("name").text = Name.get()
    employees[currentEmployee].find("phone").text = Phone.get()
    employees[currentEmployee].find("address").text = Address.get()
    employees[currentEmployee].find("email").text = Email.get()
    tree.write("company.xml")







#----------------------------------parsing the company----------------------------
tree = ET.parse('company.xml')
company = tree.getroot()
employees = company.findall("employee")
currentEmployee = 0 
eName = employees[currentEmployee].find("name").text
ePhone = employees[currentEmployee].find("phone").text
eAddress =employees[currentEmployee].find("address").text
eEmail = employees[currentEmployee].find("email").text

#----------------------------------tkinter GUI -----------------------------------
window = Tk()
window.title("compan's employees")
window.geometry("300x250+800+300")

#---------------------------------Display Employee----------------------------------------
L1 = Label(window, text="Name")
L1.grid(column=1, row=1)
Name = Entry(window, bd =5)
Name.insert(0,eName)
Name.grid(column=2 ,row=1)

L2 = Label(window, text="phone")
L2.grid(column=1, row=2)
Phone = Entry(window, bd =5)
Phone.insert(0,ePhone)
Phone.grid(column=2 ,row=2)


L1 = Label(window, text="Address")
L1.grid(column=1, row=3)
Address = Entry(window, bd =5)
Address.insert(0,eAddress)
Address.grid(column=2 ,row=3)


L1 = Label(window, text="Email")
L1.grid(column=1, row=4)
Email = Entry(window, bd =5)
Email.insert(0,eEmail)
Email.grid(column=2 ,row=4)


#-------------------controlling Buttons-------------------------------

prev = Button(window, text="prev" ,fg="blue", command=getPrev)
prev.grid(row= 5 , column=1)

next = Button(window, text="next" ,fg="blue", command=getNext)
next.grid(row= 5 , column=2)

search = Button(window,text="search",fg="blue",command=searchEmp)
search.grid(row=6,column=1)

add = Button(window,text = "add",fg="blue",command=createEmployee)
add.grid(row=6,column=2)

add = Button(window,text = "update",fg="blue",command=updateEmp)
add.grid(row=7,column=1)



window.mainloop()
