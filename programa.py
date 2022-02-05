import uuid
import datetime

class Programa:

    programas = []
    #En el contructor agrego el nuevo programa al listado "programas[]"
    def __init__(self, nombre_programa, fecha_creacion, status, director):
        self.nombre_programa = nombre_programa
        self.fecha_creacion = fecha_creacion
        self.status = status
        self.director = director
        self.programas.append((nombre_programa,fecha_creacion,status,director))
        #self.identificador = uuid.uuid4()

##Nombre Programa
    @property
    def nombre_programa(self):
        return self._nombre_programa
    @nombre_programa.setter
    def nombre_programa(self, value):
        self._nombre_programa = value
    @nombre_programa.deleter
    def nombre_programa(self):
        del self._nombre_programa

##Fecha Creacion
    @property
    def fecha_creacion(self):
        return self._fecha_creacion
    @fecha_creacion.setter
    def fecha_creacion(self, value):
        self._fecha_creacion = value
    @fecha_creacion.deleter
    def fecha_creacion(self):
        del self._fecha_creacion

##Status
    @property
    def status(self):
        return self._status
    @status.setter
    def status(self, value):
        self._status = value
    @status.deleter
    def status(self):
        del self._status

##Director
    @property
    def director(self):
        return self._director
    @director.setter
    def director(self, value):
        self._director = value
    @director.deleter
    def director(self):
        del self._director

##Identificador
    @property
    def identificador(self):
        return self._identificador
    @identificador.setter
    def identificador(self, value):
        self._identificador = value
    @identificador.deleter
    def identificador(self):
        del self._identificador

    #Este metodo, obtiene el listado de todos los programas agregados en "programas[]"
    @classmethod
    def get_programas(cls):
        return cls.programas

    # Este metodo, agrega un listado de programas por defecto a "programas[]"
    @classmethod
    def fill(cls):
        programa_computacion = Programa("Ing. Electronica", datetime.datetime.today(), "Activo", "Jeersson Maradiaga")
        programa_sistemas = Programa("Ing. Economica", datetime.datetime.today(), "Activo", "Steve Jobs")
        programa_arquitectura = Programa("Ing. Electrica", datetime.datetime.today(), "Activo", "Morgan Freeman")

        cls.programas.append((programa_computacion.nombre_programa, programa_computacion.fecha_creacion,
                          programa_computacion.status, programa_computacion.director))
        cls.programas.append((programa_sistemas.nombre_programa, programa_sistemas.fecha_creacion, programa_sistemas.status,
                          programa_sistemas.director))
        cls.programas.append((programa_arquitectura.nombre_programa, programa_arquitectura.fecha_creacion,
                          programa_arquitectura.status, programa_arquitectura.director))
        return cls.programas


#Para importar agregar: from programa import Programa

#Para llenar el listado con nuevos programas y obtenerlos, usar:
##Agregar: Programa("Ing. Ambiental", datetime.datetime.today(), "Activo", "Richard Stalman")
##print(Programa.get_programas())

#Para obtener el listado de clases por defecto usar:
##print(Programa.fill())