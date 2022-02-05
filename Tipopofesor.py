from Turno import Turno

class Tipoprofesor(Turno):
    dic_tipoprofesor = {}
    vmenu_listatp = ['Agregar Tipo de profesor', 'Borrar Tipo de profesor', 'Borrar todos los Tipos de Profesor',
                   'Inicializa todos los Tipos de Profesor','Listar los Tipos de Profesor','Listar los Turnos','Ir a Menu de Turnos'
                   , 'Salir']
    def __init__(self, tipoprofesor):
        self.__tipoprofesor = tipoprofesor

    @property
    def tipoprofesor(self):
        return self.tipoprofesor

    @tipoprofesor.setter
    def tipoprofesor(self, tipoprofesor):
        self.tipoprofesor = tipoprofesor

    @tipoprofesor.deleter
    def turno(self, tipoprofesor):
        del self.tipoprofesor

    # @classmethod
    # def listar_turnos(cls):
    #     Turno.imprimir_turno()

    @classmethod
    def imprimir_tipoprofesores(cls):
        # cls.dic_tipoprofesor = {"Planta": ['Matutino', 'Vespertino'],
        #                         "Fin de semana": ['Sabatino', 'Dominical'],
        #                          "De noche": ['Nocturno']}
        if len(cls.vlista_dic_tipoprofesorturno) == 0:
            print('No hay turnos definidos \n')
        else:
            print(f'Lista de tipo de profesores  {cls.dic_tipoprofesor}')


    @classmethod
    def llenar_turno_base(cls):
        # cls.dic_tipoprofesor = {"Planta":['Matutino','Vespertino'], "Fin de semana":['Sabatino','Dominical'],"De noche":['Nocturno']}
        # people = {1: {'name': 'John', 'age': '27', 'sex': 'Male'},
        #           2: {'name': 'Marie', 'age': '22', 'sex': 'Female'}}
        pass

    @classmethod
    def menu_tipoprofesor(cls):
        vopcion_menupt = 0
        while vopcion_menupt >= 0 and vopcion_menupt <= 8:
            print(f'Menu del catalogo de Tipos de Profesor:')
            try:
                for i in range(len(cls.vmenu_listatp)):
                    print('{}: {}'.format(i + 1, cls.vmenu_listatp[i]))
                vopcion_menupt = int(input('Ingrese la opcion:\n'))
                if vopcion_menupt == 8:
                    print('Saliendo del catalogo de Tipo de Profesor!!!')
                    break
                elif vopcion_menupt == 1:
                    """Agregar un tipo de Profesor"""
                    print('En desarrollo agregar Tipos de Profesor')
                    pass
                elif vopcion_menupt == 2:
                    """Borrar un tipo de Profesor"""
                    print('En desarrollo borrar Tipos de Profesor')
                    pass
                elif vopcion_menupt == 3:
                    """Borrar todo el catalogo de tipos de profesor"""
                    print('En desarrollo Listar Tipos de Profesor')
                    pass
                elif vopcion_menupt == 4:
                    """Inicializar todo los tipos de profesor"""
                    print('En desarrollo Iniciar Tipos de Profesor')
                    pass
                elif vopcion_menupt == 5:
                    """Listar Los tipos de Profesor"""
                    cls.imprimir_tipoprofesores()
                    pass
                elif vopcion_menupt == 6:
                    """Listar los Turnos"""
                    Tipoprofesor.imprimir_turno()
                elif vopcion_menupt == 7:
                    """Ir al menu del turno"""
                    Tipoprofesor.menu_turno()
                    pass
            except(ValueError, TypeError):
                print(f'Debe seleccionar una opcion correcta {vopcion_menupt}!!!\n')

        print('Gracias!!!\n')

##Tipoprofesor.listar_turnos()
Tipoprofesor.menu_tipoprofesor()