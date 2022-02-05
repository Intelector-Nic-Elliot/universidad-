from Persona import Persona


if __name__ == '__main__':
    pass

def separador_menus(clase):
    print(f'-------{clase}-------')
    print('Opciones, escriba "salir" para volver')


def test_salir(entrada):
    if entrada.lower() == 'salir':
        return True
    return False


def menu1():
    while True:
        separador_menus('Persona')
        print('1: Agregar una nueva persona.')
        print('2: Mostrar personas existentes.')
        print('3: Borrar una persona con una id.')
        print('4: Buscar personas.')
        if test_salir():
            break
        entrada = int(input('Seleccione una opción: '))
        if entrada == 1:
            Persona.crear_persona()
        elif entrada == 2:
            Persona.mostrar_personas()
        elif entrada == 3:
            Persona.borrar_persona()
        elif entrada == 4:
            Persona.buscar_persona()


def menu_principal():
    while True:
        try:
            print('---Bienvenido al sistema de la universidad Oxford---')
            print('Se le mostrará un menú acontinuación, escriba "salir" para volver.')
            print('1: Persona.')
            print('2: Estudiante')
            print('3: Tipo Profesor')
            print('4: Turno Profesor')
            print('5: Profesor')
            print('6: Matricula')
            print('7: Programa')
            print('8: Cursos')
            print('9: Edificio')
            print('10: Aulas')
            entrada = input('Ingrese la opción que desea utilizar: ')
            if int(entrada) < 0 or int(entrada) > 10:
                print('Ha ingresado una opción errónea')
            else:
                eval('menu'+entrada+'()')
        except ValueError:
            print('Ha habido un error de entrada por lo que se le ha regresado al menú principal.')
