import mysql.connector
from mysql.connector import Error

#Delta access object = DAO
class Dao():
    #try captura el error para poder seguir trabajando, try sirve para manejar los error
    try:
        conexion = mysql.connector.connect(
            host = 'localhost',
            port = '3306',
            user = 'root',
            password = '1234',
            database = 'ventamotos'
        )

        print(conexion.is_connected())

    except Error as err:
        print(f'error al intentar conectar a la BD {err}')
    
    def listarMotos(self):
        if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor() #con cursos puedo hacer queries a la base de datos
                cursor.execute('SELECT * FROM motos ORDER BY codigo ASC')
                resultado = cursor.fetchall()#fetchall recorre lo que trae la linea anterior y lo pone en resultado
                return resultado
            except Error as err:
                print(f'Error de conexion en el metodo listar motos, Error {err}')
    


    def publicarMoto(self, moto):
        if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor() 
                sql = f"INSERT INTO motos VALUES({moto[0]},'{moto[1]}',{moto[2]})"
                cursor.execute(sql)
                self.conexion.commit()#mandando esto, y confirmerlo
                print('se publico la moto correctamente')
                self.conexion.commit()#confirma los cambios
            except Error as err:
                print(f'Error de conexion en el metodo publicar moto, Error {err}')
   

    def actualizarMoto(self, moto):
        if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor() 
                sql = f"UPDATE motos SET referencia = '{moto[1]}', precio = {moto[2]} WHERE codigo = {moto[0]}"
                cursor.execute(sql)
                self.conexion.commit()
                print('su nueva moto se actualizo correctamente')
                
            except Error as err:
                print(f'Error de la conexion en el metodo actualizar motos, Error {err}')


    def eliminarMoto(self, codMotoElim):
        if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor() 
                sql = f"DELETE FROM motos WHERE codigo = {codMotoElim}"
                cursor.execute(sql)
                self.conexion.commit()
                print('Se elimino la moto correctamente')
                
            except Error as err:
                print(f'Error de la conexion en el metodo eliminar, Error {err}')
