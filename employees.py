import mysql.connector

class Employees:
    #Constructor de la clase
    def __init__(self):
        self.cnn = mysql.connector.connect(host="localhost", user="root", 
        passwd="Aron123", database="employeedb")

    def __str__(self):
        datos=self.take_employee()
        aux=""
        for row in datos:
            aux=aux + str(row) + "\n"
        return aux

    #funcion que se conecta a la base de datos y muestra los resultados guardados
    def take_employee(self):
        cur = self.cnn.cursor()
        cur.execute("SELECT * FROM employees")
        datos = cur.fetchall()
        cur.close()    
        return datos
    #esta funcion sirve para guardar la informacion en cada campo de la base de datos
    def insert_employee(self,Nam, LstName, Age, Sex, SSN, Birthday, MariatalStatus, EmployeeNum, PhoneNum, MPerHour, AVGHworked): #comp parametros la funcion resive todos los campos de la BD
        cur = self.cnn.cursor()
        #en la linea de abajo se escribe la forma e la que se inserta informacion directamente dentro de la base de datos en MySQL
        sql='''INSERT INTO employees (Nam, LstName, Age, Sex, SSN, Birthday, MariatalStatus, EmployeeNum, PhoneNum, MPerHour, AVGHworked) 
        VALUES('{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}')'''.format(Nam, LstName, Age, Sex, SSN, Birthday, MariatalStatus, EmployeeNum, PhoneNum, MPerHour, AVGHworked)
        cur.execute(sql)
        n=cur.rowcount
        self.cnn.commit()    
        cur.close()
        return n    
