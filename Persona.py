class Persona:
    lista_de_personas = []

    def __init__(self, nombre, apellido, cedula, direccion, telefono, fecha_de_nacimiento, email):
        self.nombre = nombre
        self.apellido = apellido
        self.direccion = direccion
        self.cedula = cedula
        self.telefono = telefono
        self.fecha_de_nacimiento = fecha_de_nacimiento
        self.email = email
        self.lista_de_personas.append([nombre, apellido, direccion, cedula, telefono, fecha_de_nacimiento, email])

    @classmethod
    def crear_persona(cls):
        """Pide al usuario el input de una persona a la base de datos (en RAM) de la clase."""
        nombre = input('Ingrese el nombre: ')
        apellido = input('Ingrese el apellido: ')
        direccion = input('Ingrese la direccion: ')
        cedula = input('Ingrese el cedula: ')
        telefono = input('Ingrese el telefono: ')
        fecha_de_nacimiento = input('Ingrese el fecha_de_nacimiento: ')
        email = input('Ingrese el email: ')
        print(
            f'Esta persona se ha agregado satisfactoriamente a la base de datos, y estará en'
            f' el índice número: {len(cls.lista_de_personas)}')
        cls.lista_de_personas.append([nombre, apellido, direccion, cedula, telefono, fecha_de_nacimiento, email])

    @classmethod
    def agregar_persona_ya_existente(cls, persona):
        """Agrega una lista de una persana ya existente a la lista de personas"""
        cls.lista_de_personas.append(persona)

    @classmethod
    def buscar_persona(cls):
        """Pide al usuario datos para buscar una persona."""
        tipo = input('Ingrese el índice o el nombre por el que desea buscar a la persona: ')
        try:
            if tipo.isnumeric():
                print(cls.lista_de_personas[int(tipo)])
            else:
                filtered = filter(lambda persona: persona.lower() == tipo.lower(), cls.lista_de_personas)
                print('Las personas que tienen ese nombre son: ')
                for i in filtered:
                    print(i)
        except:
            print('La persona que intenta buscar no existe.')

    @classmethod
    def buscar_por_id(cls, indice):
        return cls.lista_de_personas[indice]

    @classmethod
    def mostrar_personas(cls):
        print('Se mostrará el nombre de todas las personas en la base de datos.')
        for i in cls.lista_de_personas:
            print(f'{cls.lista_de_personas.index(i)} :{i}')

    @classmethod
    def borrar_persona(cls):
        indice = input('Ingrese el indice de la persona que desea borrar: ')

    # Nombre
    @property
    def nombre(self):
        return self._nombre

    @nombre.getter
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, value):
        self._nombre = value

    @nombre.deleter
    def nombre(self):
        del self._nombre

    # Apellido
    @property
    def apellido(self):
        return self._apellido

    @apellido.setter
    def apellido(self, value):
        self._apellido = value

    @apellido.getter
    def apellido(self):
        return self._apellido

    @apellido.deleter
    def apellido(self):
        del self._apellido

    # Cedula
    @property
    def cedula(self):
        return self._cedula

    @cedula.getter
    def cedula(self):
        return self._cedula

    @cedula.setter
    def cedula(self, value):
        self._cedula = value

    @cedula.deleter
    def cedula(self):
        del self._cedula

    # direccion
    @property
    def direccion(self):
        return self._direccion

    @direccion.getter
    def direccion(self):
        return self._direccion

    @direccion.setter
    def direccion(self, value):
        self._direccion = value

    @direccion.deleter
    def direccion(self):
        del self._direccion

    # telefono
    @property
    def telefono(self):
        return self._telefono

    @telefono.getter
    def telefono(self):
        return self._telefono

    @telefono.setter
    def telefono(self, value):
        self._telefono = value

    @telefono.deleter
    def telefono(self):
        del self._telefono

    # fecha_de_nacimiento
    @property
    def fecha_de_nacimiento(self):
        return self._fecha_de_nacimiento

    @fecha_de_nacimiento.getter
    def fecha_de_nacimiento(self):
        return self._fecha_de_nacimiento

    @fecha_de_nacimiento.setter
    def fecha_de_nacimiento(self, value):
        self._fecha_de_nacimiento = value

    @fecha_de_nacimiento.deleter
    def fecha_de_nacimiento(self):
        del self._fecha_de_nacimiento

    # email
    @property
    def email(self):
        return self._email

    @email.getter
    def email(self):
        return self._email

    @email.setter
    def email(self, value):
        self._email = value

    @email.deleter
    def email(self):
        del self._email


