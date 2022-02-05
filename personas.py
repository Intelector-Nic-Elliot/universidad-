

# lista_estudiantes = []

# class Persona:
#     def __init__(self, nombre, apellido, cedula, direccion, telefono, fecha_de_nacimiento, email):
#         self.nombre = nombre
#         self.apellido = apellido
#         self.direccion = direccion
#         self.cedula = cedula
#         self.telefono = telefono
#         self.fecha_de_nacimiento = fecha_de_nacimiento
#         self.email = email


# class Estudiante(Persona):
#     pass
#     def __init__(self, nombre, apellido, cedula, direccion, telefono, fecha_de_nacimiento, email, id_estudiante):
#         super(Estudiante, self).__init__(nombre, apellido, cedula, direccion, telefono, fecha_de_nacimiento, email)
#         self.id_estudiante = id_estudiante
    
#     @property
#     def id(self):
#         return self.id_estudiante
    
#     @id.setter
#     def id(self, value):
#         self.id_estudiante = value


# class Matricula(Estudiante):
#     pass
#     def __init__(self, nombre, apellido, cedula, direccion, telefono, fecha_de_nacimiento, email, id_estudiante,fecha_estudiante,hora_matricula):
#         super().__init__(nombre, apellido, cedula, direccion, telefono, fecha_de_nacimiento, email, id_estudiante,fecha_estudiante,hora_matricula)
#         return 
    

from pydoc import describe
from datetime import datetime


Lista_alumnos = []
class Persona:
    # lista_de_personas = []

    def __init__(self, nombre, apellido, cedula, direccion, telefono, fecha_de_nacimiento, email):
        self.nombre = nombre
        self.apellido = apellido
        self.direccion = direccion
        self.cedula = cedula
        self.telefono = telefono
        self.fecha_de_nacimiento = fecha_de_nacimiento
        self.email = email

    def descripcion(self):

        print("Nombre:", self.nombre, " Apellido:", self.apellido, " Cedula:", self.cedula, " Direccion:", self.direccion, " Telefono:", self.telefono, " Fecha de nacimiento", self.fecha_de_nacimiento, " Email:", self.email)
    

class Estudiante(Persona):
    pass
    def __init__(self,id_estudiante, nombre_alumno, apellido_alumno, cedula_alumno, direccion_alumno, telefono_alumno, fecha_de_nacimiento_alumno, email_alumno):
        super().__init__(nombre_alumno, apellido_alumno, cedula_alumno, direccion_alumno, telefono_alumno, fecha_de_nacimiento_alumno, email_alumno)

        self.id_estudiante = id_estudiante

    def descripcion(self):
         super().descripcion()
         print("El Id del estudiante es: ", self.id_estudiante)

alumno1 = Estudiante("2015-0389", "Elliot", "Acuña", "001-241197-0003S", "Altamira", "22774466", "24/11/80", "elliot.acuna@uni.edu.ni")
alumno1.descripcion()

class Matricula(Estudiante):
    pass
    def __init__(self,fecha_matricula, id_estudiante, nombre_alumno, apellido_alumno, cedula_alumno, direccion_alumno, telefono_alumno, fecha_de_nacimiento_alumno, email_alumno):
        super().__init__(id_estudiante, nombre_alumno, apellido_alumno, cedula_alumno, direccion_alumno, telefono_alumno, fecha_de_nacimiento_alumno, email_alumno)
        
        self.fecha_matricula = fecha_matricula
        
    
    def descripcion(self):
        super().descripcion()
        print("La fecha y hora de matricula es: ",datetime.today().strftime("%Y-%m-%d %H:%M"), self.fecha_matricula)

matricula1 = Matricula("","2015-0389", "Elliot", "Acuña", "001-241197-0003S", "Altamira", "22774466", "24/11/80", "elliot.acuna@uni.edu.ni")
matricula1.descripcion()
