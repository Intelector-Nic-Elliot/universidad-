class Turno:
    vlista_turno = []
    vmenu_lista = ['Agregar Turno', 'Borrar Turno', 'Borrar todos los Turnos', 'Se Inicializaron todos los turnos',
                   'Listar Turnos actuales', 'Salir']
    def __init__(self,turno):
        self.__turno = turno

    @property
    def turno(self):
        return self.__turno

    @turno.setter
    def turno(self, turno):
        self.__turno = turno

    @turno.deleter
    def turno(self, turno):
        del self.__turno

    @classmethod
    def imprimir_turno(cls):
        # print(f'La lista de turno es {cls.lista_turno}')
        if len(cls.vlista_turno) == 0:
            print('No hay turnos definidos actualmente\n')
        else:
            print(f'La lista de turno es:')
            for i in range(len(cls.vlista_turno)):
                print('{}: {}'.format(i + 1, cls.vlista_turno[i]))
            print('\n')

    @classmethod
    def agregar_turno(cls, turno):
        cls.vlista_turno.append(turno)
        print(f'Se Agrego el turno {turno}')
        cls.imprimir_turno()

    @classmethod
    def borrar_turno(cls, turno):
        cls.vlista_turno.remove(turno)
        print(f'Se borro el turno {turno}')
        cls.imprimir_turno()

    @classmethod
    def borrar_todos_turnos(cls):
        cls.vlista_turno.clear()
        print('Se borraron Todos los turnos, tiene que agregar turnos!!!\n')

    @classmethod
    def llenar_turno_base(cls):
        cls.vlista_turno = ["Matutino", "Vespertino", "Nocturno", "Sabatino", "Dominical"]
        cls.imprimir_turno()
        # cls.lista_turno.append('Matutino')
        # cls.lista_turno.append('Vespertino')
        # cls.lista_turno.append('Nocturno')
        # cls.lista_turno.append('Sabatino')
        # cls.lista_turno.append('Dominical')

    @classmethod
    def menu_turno(cls):
        vopcion_menu = 0
        while vopcion_menu >= 0 and vopcion_menu <= 6:
            print(f'Menu del catalogo de turnos:')
            try:
                for i in range(len(cls.vmenu_lista)):
                    print('{}: {}'.format(i + 1, cls.vmenu_lista[i]))
                vopcion_menu = int(input('Ingrese la opcion\n'))
                if vopcion_menu == 6:
                    print('Saliendo del catalogo de menu')
                    break
                elif vopcion_menu == 1:
                    cls.agregar_turno(input('Íngrese el el turno que quiere agregar: '))
                    cls.imprimir_turno()
                elif vopcion_menu == 2:
                    cls.imprimir_turno()
                    cls.borrar_turno(input('Íngrese el el turno que quiere Borrar: '))
                    cls.imprimir_turno()
                elif vopcion_menu == 3:
                    cls.borrar_todos_turnos()
                elif vopcion_menu == 4:
                    cls.borrar_todos_turnos()
                    cls.llenar_turno_base()
                    cls.imprimir_turno()
                elif vopcion_menu == 5:
                    cls.imprimir_turno()
            except(ValueError, TypeError):
                print('Debe seleccionar una opcion correcta!!!\n')

        print('Gracias!!!')

#Turno.menu_turno()
# turno01 = Turno('turno en lineda')
# print(f'esto es la prueba {turno01.turno} ')
# Turno.llenar_turno_base()
# Turno.imprimir_turno()
# Turno.borrar_turno('Dominical')
# # del turno01.turno
# Turno.imprimir_turno()
# print(f'esto es la prueba {turno01.turno} ')

