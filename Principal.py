from DB.Conexion import Dao
import funciones as fun

def menuPrincipal():
    continuar = True
    while (continuar):
        print("===== Menu Principal Venta Motos =====")
        print(" ")
        print("1. Listar Motos en Venta")
        print("2. Publicar una moto")
        print("3. Actualizar moto en venta")
        print("4. Eliminar moto vendida")
        print("5. Salir")
        print("==========================")
        opc = int(input('Seleccione el numero de la opcion: '))

        if  (opc < 1 or  opc > 5):
            print('Opcion incorrecta, intente nuevamente: ')
        elif(opc == 5):
            continuar = False
            print('Gracias por utilizar la aplicacion!')
            break
        else:
            ejecutarOpc(opc)

def ejecutarOpc(num):
    dao = Dao()
    if num == 1:
        try:
            motos = dao.listarMotos()
            if len(motos) > 0:
                fun.mostrarMotos(motos)
        except:
            print('ocurrio un error en la publicacin de la moto (except)')
    
    elif num == 2:
        try:
            motos = fun.consultarMotos()
            try:
                dao.publicarMoto(motos)
            except:
                print('ocurrio un error en el registro de la moto')
        except:
            print('ocurrio un error al registrar la moto')
    
    elif num == 3:
        try:
            motos = dao.listarMotos()
            if len(motos) > 0:
                moto = fun.perdirDatosActualizarMotos(motos)
                if moto:
                    dao.actualizarMoto(moto)
                else:
                    print('Codigo de la moto no encontrado')
            else:
                print('No se encontraron motos para listar')
        except:
            print('No se encontraron motos para listar(except)')
    
    elif num == 4:
        try:
            motos = dao.listarMotos()
            if len(motos) > 0:
                moto = fun.perdirDatosEliminar(motos)
                if not moto == '':
                    dao.eliminarMoto(moto)
                else:
                    print('Codigo de la moto no encontrado')
            else:
                print('No se encontraron motos para listar')
        except:
            print('No se encontraron motos para listar(except)')



menuPrincipal()

