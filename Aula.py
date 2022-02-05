class Aula:
    def __init__(self, nombre, apellido, aula, piso, edificio):
        self._nombre = nombre
        self._apellido = apellido
        self._aula = aula
        self._piso = piso
        self._edificio = edificio

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, nombre):
        self._nombre = nombre

    @property
    def apellido(self):
        return self._apellido

    @apellido.setter
    def apellido(self, apellido):
        self._apellido = apellido

    @property
    def aula(self):
        return self._aula

    @aula.setter
    def aula(self, aula):
        self._aula = aula

    @property
    def piso(self):
        return self._piso

    @piso.setter
    def piso(self, piso):
        self._piso = piso

    @property
    def edificio(self):
        return self._edificio

    @edificio.setter
    def edificio(self, edificio):
        self._edificio = edificio


cantidad = Aula("carlos", "calderon", 23, 1, "sistemas")
print(cantidad.nombre)
cantidad.nombre = "ies"
print(cantidad.nombre)
