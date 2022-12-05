from tkinter import *
from tkinter import ttk
from employees import *

class Window(Frame):

    employee = Employees()

    #constructor de la clase y el que se encarga de crear la GUI para su uso
    def __init__(self, master=None):
        super().__init__(master, width=980, height=650)
        self.master = master
        self.pack()
        self.Create_widgets()
        self.show_data()

    def show_data(self):
        data = self.employee.take_employee()
        for row in data:
            self.grid.insert("", END, text=row[0], values=(row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9], row[10], row[11]))

    #en esta funcion cda vez que se presione el boton new se llamaran a las funciones que habilitan las cajas en donde
    #se escribe el texto y para habilitar el boton de save para guardar la informacion
    def New_button(self):
        self.use_txtbox("normal")
        self.use_newbtn("disabled")
        self.use_savebtn("normal")

    #esta funcion sirve para habilitar las cajas de texto en donde se coloca la informacion para guardadrla en la base de datos
    #en la misma se llama a configure para que cada vez que se llame la funcion y reciba como parametro la palabra normal
    #se activen las cajas de textos
    def use_txtbox(self, enable):
        self.name_text.configure(state = enable)
        self.lst_name.configure(state = enable)
        self.age_txt.configure(state = enable)
        self.sex_txt.configure(state = enable)
        self.SSN_txt.configure(state = enable)
        self.birth_txt.configure(state = enable)
        self.marital_txt.configure(state = enable)
        self.Employee_txt.configure(state = enable)
        self.Phone_num.configure(state = enable)
        self.Per_hour.configure(state = enable)
        self.Avg_work.configure(state = enable)

    def use_newbtn(self, enable):
        self.new_button.configure(state=enable)

    def use_savebtn(self, enable):
        self.save_button.configure(state=enable)
    #la funcion llama a la funcion de la clase Employees del archivo employees.py
    #para insertar la informacion que el usuario coloque en las cajas de texto
    #Ademas llama la funcion show_data que es la que se coecta a la base de datos y muestra los resultados guardados
    def fSave(self):
        self.employee.insert_employee(self.name_text.get(),self.lst_name.get(),self.age_txt.get(),self.sex_txt.get(),self.SSN_txt.get(),self.birth_txt.get(),self.marital_txt.get(),self.Employee_txt.get(),self.Phone_num.get(),self.Per_hour.get(),self.Avg_work.get())
        self.show_data()

    #funcion que especifica todas las caracteristicas de la interfaz grafica de usuario
    #desde el color de los frame hasta los botones y columnas de la misma
    def Create_widgets(self):
        frame_1 = Frame(self, bg="#9FF781") #se le da color al primer frame llamando la clase Frame de la libreria Tkinter
        frame_1.place(x=0, y=0,width=980, height=50)

        self.new_button=Button(frame_1, text="New", command=self.New_button, bg="black", fg="white")#se crea el boton New y se coloca en el primer frame en la parte superior
        self.new_button.place(x=130, y=10, width=80, height=30)

        frame_2 =Frame(self, bg="#01DF01")
        frame_2.place(x=0, y=50, width=200, height="650")

        label_1 = Label(frame_2, text="Name") 
        label_1.place(x=0, y=5) #con la funcion place se especifica el lugar en donde el label va a estar ubicada y el nombre de la misma

        self.name_text=Entry(frame_2) #con la funcion predeterminada Entry se crea la caja de texto para que el usuario indroduzca la informacion
        self.name_text.place(x=0, y=25, width=150, height=20)

        label_2 = Label(frame_2, text="Last name")
        label_2.place(x=0, y=55)

        self.lst_name=Entry(frame_2)
        self.lst_name.place(x=0, y=75, width=150, height=20)

        label_3 = Label(frame_2, text="Age")
        label_3.place(x=0, y=105)

        self.age_txt=Entry(frame_2)
        self.age_txt.place(x=0, y=125, width=150, height=20)

        label_4 = Label(frame_2, text="Sex")
        label_4.place(x=0, y=155)

        self.sex_txt=Entry(frame_2)
        self.sex_txt.place(x=0, y=175, width=150, height=20)

        label_5 = Label(frame_2, text="Social Security Number")
        label_5.place(x=0, y=205)

        self.SSN_txt=Entry(frame_2)
        self.SSN_txt.place(x=0, y=225, width=150, height=20)

        label_6 = Label(frame_2, text="Birthday")
        label_6.place(x=0, y=255)

        self.birth_txt=Entry(frame_2)
        self.birth_txt.place(x=0, y=275, width=150, height=20)

        label_7 = Label(frame_2, text="Marital Status")
        label_7.place(x=0, y=305)

        self.marital_txt=Entry(frame_2)
        self.marital_txt.place(x=0, y=325, width=150, height=20)

        label_8 = Label(frame_2, text="Employee Number")
        label_8.place(x=0, y=355)

        self.Employee_txt=Entry(frame_2)
        self.Employee_txt.place(x=0, y=375, width=150, height=20)

        label_9 = Label(frame_2, text="Phone Number")
        label_9.place(x=0, y=405)

        self.Phone_num=Entry(frame_2)
        self.Phone_num.place(x=0, y=425, width=150, height=20)

        label_10 = Label(frame_2, text="M per hour")
        label_10.place(x=0, y=455)

        self.Per_hour=Entry(frame_2)
        self.Per_hour.place(x=0, y=475, width=150, height=20)

        label_11 = Label(frame_2, text="Avg of hours worked")
        label_11.place(x=0, y=505)

        self.Avg_work=Entry(frame_2)
        self.Avg_work.place(x=0, y=525, width=150, height=20)

        self.save_button=Button(frame_2, text="Save", command=self.fSave, bg="black", fg="white")
        self.save_button.place(x=10, y=560, width=80, height=30)

        self.grid = ttk.Treeview(self, columns=("col1", "col2", "col3", "col4", "col5", "col6", "col7", "col8", "col9", "col10", "col11"))

        #se crean las columnas en donde se van a mostrar todos los campos almacenados
        self.grid.column("#0", width = 50)
        self.grid.column("col1", width=60, anchor=CENTER)
        self.grid.column("col2", width=60, anchor=CENTER)
        self.grid.column("col3", width=60, anchor=CENTER)
        self.grid.column("col4", width=60, anchor=CENTER)
        self.grid.column("col5", width=60, anchor=CENTER)
        self.grid.column("col6", width=60, anchor=CENTER)
        self.grid.column("col7", width=60, anchor=CENTER)
        self.grid.column("col8", width=60, anchor=CENTER)
        self.grid.column("col9", width=60, anchor=CENTER)
        self.grid.column("col10", width=60, anchor=CENTER)
        self.grid.column("col11", width=60, anchor=CENTER)

        #en las proximas lineas de codigo se le colocan los nombres a cada columna
        self.grid.heading("#0", text="Emp ID", anchor=CENTER)
        self.grid.heading("col1", text="Name", anchor=CENTER)
        self.grid.heading("col2", text="Last Name", anchor=CENTER)
        self.grid.heading("col3", text="Age", anchor=CENTER)
        self.grid.heading("col4", text="Sex", anchor=CENTER)
        self.grid.heading("col5", text="SSN", anchor=CENTER)
        self.grid.heading("col6", text="Birthday", anchor=CENTER)
        self.grid.heading("col7", text="MariatalSts", anchor=CENTER)
        self.grid.heading("col8", text="EmpNum", anchor=CENTER)
        self.grid.heading("col9", text="PhoneNum", anchor=CENTER)
        self.grid.heading("col10", text="MPerHour", anchor=CENTER)
        self.grid.heading("col11", text="AVGHworked", anchor=CENTER)

        #se especifica el tamano de largo y ancho del Treeview que es donde aparece la informacion guardada
        self.grid.place(x=200, y=50, width=780, height=600)