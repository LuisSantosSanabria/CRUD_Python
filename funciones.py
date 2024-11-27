def listarDeportes(cursos):
    print("\nDEPORTES:")
    contador = 1
    #recorre la lista de los cursos
    for cur in cursos:
        datos = "Codigo: {1} | Nombre: {2}"
        print(datos.format(contador, cur[0], cur[1]))
        contador = contador + 1

def listarProfesor(profesor):
    print("\nPROFESORES:")
    contador = 1
    #recorre la lista de los profesores
    for prof in profesor:
        datos = "Legajo: {1} | Nombre: {2} | Deporte: {3}" 
        print(datos.format(contador, prof[0], prof[1], prof [2])) #marcadores de posicion

def pedirDatosRegistro():
    codigoCorrecto = False #asegura q el codigo ingresado sea el correcto
    while(not codigoCorrecto):
        codigo = input("Ingrese código: ")
        if len(codigo) == 2:
            codigoCorrecto = True
        else:
            print("Codigo incorrecto: Debe tener 2 digitos.")

    nombre = input("Ingrese nombre: ")
    curso = (codigo, nombre)
    return curso

def modifcarDatos(cursos):
    listarDeportes(cursos)
    existeCodigo = False
    codigoEditar = input("Ingrese el codigo del deporte: ")
    for cur in cursos:
        if cur[0] == codigoEditar:
            existeCodigo = True
            break

    if existeCodigo:
        nombre = input("Ingrese nombre a modificar: ")
        curso = (codigoEditar, nombre)
    else:
        curso = None
    
    return curso

def pedirDatosEliminacion(cursos):
    listarDeportes(cursos)
    existeCodigo = False
    codigoEliminar = input("Ingrese el codigo del deporte a eliminar: ")
    for cur in cursos:
        if cur[0] == codigoEliminar:
            existeCodigo = True
            break

    if not existeCodigo:
        codigoEliminar = ""

    return codigoEliminar
