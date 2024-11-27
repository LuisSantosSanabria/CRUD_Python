import mysql.connector
from mysql.connector import Error

#Conexion a base de datos
class Datos():

    def __init__(self):
        try:
            self.conexion = mysql.connector.connect( #parametros
                host='localhost', 
                port=3306,
                user='root',
                password='root',
                db='clublab'
            )
        except Error as ex:
            print("Error al intentar la conexion: {0}".format(ex))
#Los datose se van almacenar en la variabvle conexion
    def listarDeportes(self):
        if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor()
                cursor.execute("SELECT * FROM curso ORDER BY nombre ASC")
                resultados = cursor.fetchall() #metodo que obtiene los registros de la conl sql

                return resultados
            except Error as ex:
                print("Error al intentar la conexión: {0}".format(ex))
    
    def listarProfesores(self):
        if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor()
                cursor.execute("SELECT * FROM profesor ORDER BY nombre ASC")
                profesor = cursor.fetchall()

                return profesor
            except Error as ex:
                print("Error al intentar la conexión: {0}".format(ex))

    def registrarCurso(self, curso):
        if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor()
                sql = "INSERT INTO curso (codigo, nombre) VALUES ('{0}', '{1}')"
                cursor.execute(sql.format(curso[0], curso[1])) #marcadores de posicion
                self.conexion.commit() #confirma el registro
                print("Curso registrado!\n")
            except Error as ex:
                print("Error al intentar la conexión: {0}".format(ex))

    def actualizarDeportes(self, curso):
        if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor()
                sql = "UPDATE curso SET nombre = '{0}' WHERE codigo = '{1}'"
                cursor.execute(sql.format(curso[1], curso[0]))
                self.conexion.commit()
                print("Curso actualizado!\n")
            except Error as ex:
                print("Error al intentar la conexión: {0}".format(ex))

    def eliminarDeportes(self, codigoCursoEliminar):
        if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor()
                sql = "DELETE FROM curso WHERE codigo = '{0}'"
                cursor.execute(sql.format(codigoCursoEliminar))
                self.conexion.commit()
                print("Curso eliminado!\n")
            except Error as ex:
                print("Error al intentar la conexión: {0}".format(ex))
