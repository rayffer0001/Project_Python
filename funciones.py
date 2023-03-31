def mostrarMotos(motos):
    print('\n Lista de motos para la venta: \n')
    cont = 0
    for moto in motos:
        cont += 1
        print(f' {cont}.codigo:{moto[0]} nombre: {moto[1]} precio: {moto[2]}')
    print(' ')

def consultarMotos():
    print('Por favor ingrese las caracteristicas de la moto')
    print('caracteristicas ejemplo: (Marca Referencia Modelo)')
    
    codigoCorrecto = False
    while not codigoCorrecto:
        codigo = input('codigo de la moto: ')
        if codigo.isnumeric():
            if len(codigo) == 4:
                codigoCorrecto = True
                codigo = int(codigo)
            else:
                print('El codigo de la moto debe tener obligatoriamente 4 digitos')
        else:
            print('Por favor ingresar solo numeros para el codigo del curso')
            
    referenciaCorrecta = False
    while not referenciaCorrecta:
        referencia_moto = input('Inserte la referencia de la moto: ')
        if len(referencia_moto) <= 60:
            referenciaCorrecta = True
        else:
            print('la referencia de la moto no puede sobrepasar los 60 caracteres')
            
    precioCorrecto = True
    while precioCorrecto:
        precio = input('Ingrese un precio para moto: ')
        if precio.isnumeric():
            if len(precio) <= 9:
                if int(precio) > 0:
                    precioCorrecto = False
                    precio = int(precio)
                else:
                    print('Debe ingresar un precio no mayor a los $999.999.994 Millones_4')
            else:
                print('Debe ingresar un precio no mayor a los $999.999.995 Millones_5')        
        else:
            print('Por favor ingresar solo numeros para el precio de la moto_6')            

    moto = (codigo,referencia_moto,precio)
    return moto

def perdirDatosActualizarMotos(motos):
    mostrarMotos(motos)
    existeCod = False

    codigoCorrecto = False
    while not codigoCorrecto:
        codigo = input('codigo de la moto: ')
        if codigo.isnumeric():
            if len(codigo) == 4:
                codigoCorrecto = True
                codigo = int(codigo)
            else:
                print('El codigo de la moto debe tener obligatoriamente 4 digitos')
        else:
            print('Por favor ingresar solo numeros para el codigo de la moto')
    #revisa que el codigo que entró esta dentro de la tabla
    for moto in motos:
        if moto[0] == codigo:
            existeCod = True
            print(f'Se encontró el código {moto[0]}')
            break
    
    if existeCod: # es un true entonces entra                
        referenciacorrecta = True
        while referenciacorrecta:
            referencia_moto = input('Nueva referencia de la moto: ')
            if len(referencia_moto) <= 60:
                referenciacorrecta = False
            else:
                print('La referencia de la moto no puede sobrepasar los 60 caracteres')
                
        precioCorrecto = False
        while not precioCorrecto:
            precio = input('Modificar precio: ')
            if precio.isnumeric():
                if len(precio) <= 9:
                    if int(precio) > 0:
                        precioCorrecto = True
                        precio = int(precio)
                    else:
                        print('Debe ingresar un precio no mayor a los $999.999.993 Millones_3')
                else:
                    print('Debe ingresar un precio no mayor a los $999.999.991 Millones_1')        
            else:
                print('Debe ingresar un precio no mayor a los $999.999.992 Millones_2') 

        moto = (codigo, referencia_moto, precio)

    else:
        moto = None
    
    return moto


def perdirDatosEliminar(motos):
    mostrarMotos(motos)
    existeCod = False

    codigoCorrecto = False
    while not codigoCorrecto:
        codigo = input('codigo de la moto: ')
        if codigo.isnumeric():
            if len(codigo) == 4:
                codigoCorrecto = True
                codigo = int(codigo)
            else:
                print('El codigo de la moto debe tener obligatoriamente 4 digitos')
        else:
            print('Por favor ingresar solo numeros para el codigo de la moto')
    #revisa que el codigo que entró esta dentro de la tabla
    for moto in motos:
        if moto[0] == codigo:
            existeCod = True
            print(f'Se encontró el código {moto[0]}, se eliminara de la base de datos de ventas')
            break
    
    if not existeCod:
        print('El codigo de la moto no exite, verifique nuevamente')
        codigo = ''

    return codigo

