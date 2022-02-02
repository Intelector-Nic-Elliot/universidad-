
class Persona():
    def __init__(self, nombre, apellido, cedula, direccion, telefono, fecha_de_nacimiento, email):
        self.nombre = nombre
        self.apellido = apellido
        self.direccion = direccion
        self.cedula = cedula
        self.telefono = telefono
        self.fecha_de_nacimiento = fecha_de_nacimiento
        self.email = email


class Estudiante(Persona):
    def __init__(self, nombre, apellido, cedula, direccion, telefono, fecha_de_nacimiento, email, id_estudiante):
        super(Estudiante, self).__init__(nombre, apellido, cedula, direccion, telefono, fecha_de_nacimiento, email)
        self.id_estudiante = id_estudiante


    def matricular(self):
        self