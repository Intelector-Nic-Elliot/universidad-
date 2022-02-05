class Estudiante():
    def __init__(self, nombre, apellido, cedula, direccion, telefono, fecha_de_nacimiento, email, id_estudiante):
        super(Estudiante, self).__init__(nombre, apellido, cedula, direccion, telefono, fecha_de_nacimiento, email)
        self.id_estudiante = id_estudiante
    

    #Nombre
    @property
    def nombre(self):
        return self.nombre
    
    @nombre.getter
    def nombre(self):
        return self.nombre

    @nombre.setter
    def nombre(self, value):
        self.nombre = value
    
    @nombre.deleter
    def nombre(self):
        del self.nombre
    

    #Apellido
    @property
    def apellido(self):
        return self.apellido
    
    @apellido.getter
    def apellido(self):
        return self.apellido
    
    @apellido.setter
    def apellido(self, value):
        self.apellido = value
    
    @apellido.deleter
    def apellido(self):
        del self.apellido
    
    #cedula
    @property
    def cedula(self):
        return self.cedula
    
    @cedula.getter
    def cedula(self):
        return self.cedula
    
    @cedula.setter
    def cedula(self, value):
        self.cedula = value
    
    @cedula.deleter
    def cedula(self):
        del self.cedula

    #Id_estudiante
    @property
    def id_estudiante(self):
        return self.id_estudiante
    
    @id_estudiante.getter
    def id_estudiante(self):
        return self.id_estudiante
    
    @id_estudiante.setter
    def id_estudiante(self, value):
        self.id_estudiante = value
    
    @id_estudiante.deleter
    def id_estudiante(self):
        del self.id_estudiante
    
    