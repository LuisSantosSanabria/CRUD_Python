from BD.conexion import Datos
import funciones


def menuPrincipal():
    continuar = True #para q se repita el menu
    while(continuar): #bucle para validar opciones
        opcionCorrecta = False
        while(not opcionCorrecta):
            print("\n⚽ 🏀 🏐  CLUB ATLETICO LABORATORO IV  ⚽ 🏀 🏐\n")
            print(" MENU PRINCIPAL: ")
            print("1- Lista de Deportes disponibles")
            print("2- Registrar Deporte")
            print("3- Editar Deporte")
            print("4- Eliminar Deporte")
            print("5- Profesores")
            print("6- Salir")
            opcion = int(input("Seleccione una opcion: "))

            if opcion < 1 or opcion > 6:
                print("Elija entre 1 y 6!")
            elif opcion == 6:
                continuar = False
                print("Adioooooooooooooos")
                break
            else:
                opcionCorrecta = True
                ejecutarOpcion(opcion)


def ejecutarOpcion(opcion):
    datosCrud = Datos()

    if opcion == 1:
        try:
            cursos = datosCrud.listarDeportes()
            if len(cursos) > 0:
                funciones.listarDeportes(cursos)
            else:
                print("No se encontraron cursos")
        except:
            print("Ocurrio un error")

    elif opcion == 2:
        curso = funciones.pedirDatosRegistro()
        try:
            datosCrud.registrarCurso(curso)
        except:
            print("Ocurrio un error")

    elif opcion == 3:
        try:
            cursos = datosCrud.listarDeportes()
            if len(cursos) > 0:
                curso = funciones.modifcarDatos(cursos)
                if curso:
                    datosCrud.actualizarDeportes(curso)
                else:
                    print("Que queres actualizar si no hay curso?\n")
            else:
                print("No se encontraron cursos")
        except:
            print("Ocurri un error")

    elif opcion == 4:
        try:
            cursos = datosCrud.listarDeportes()
            if len(cursos) > 0: #comprobar que existen resultados
                codigoEliminar = funciones.pedirDatosEliminacion(cursos)
                if not(codigoEliminar == ""):
                    datosCrud.eliminarDeportes(codigoEliminar)
                else:
                    print("Codigo sin curso\n")
            else:
                print("No se encontraron cursos")
        except:
            print("Ocurrió un error")

    elif opcion == 5:
            profe = datosCrud.listarProfesores()
            if len(profe) > 0:
                funciones.listarProfesor(profe)
            else:
                print("No se encontraron Profesores")

menuPrincipal()
