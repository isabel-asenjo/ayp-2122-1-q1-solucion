'''
Una tienda de discos de vinilo requiere que desarrolles un software para llevar su administración. El sistema consta de dos módulos:
Inventario
Ventas

El módulo de inventario debe contar con lo siguiente:
Ver toda la información de todos los discos disponibles (no vale solo imprimir la estructura de datos que los tiene, debe presentarse en consola de forma ordenada y legible)
Buscar información de un disco en específico por nombre

El módulo de ventas debe tener las siguientes funcionalidades:
Registrar una nueva venta (guardando en una estructura de datos dni y nombre del comprador y id del disco que se compró. Solo se puede comprar un disco a la vez)
Ver cantidad total de ventas


Requerimientos técnicos:
TODOS LOS INPUTS deben estar validados
Cada vez que se haga una compra, debe suceder lo siguiente: se pide el dni y el nombre del comprador, se muestran los discos disponibles, se ingresa la elección del comprador, se muestra un resumen de la compra y se actualiza la cantidad de discos comprada y la cantidad disponible
Guardar la información de las compras en la estructura de datos de su elección
Utilizar el diccionario de discos dado
El software debe contar con un menú inicial donde se pueda seleccionar qué se va a hacer. Al terminarse la operación en curso, debe volverse a dicho menú


BONO (3pts):
Si los últimos 3 números del DNI de un cliente es un número incremental, otorgarle un 20% de descuento en su compra final.

Número incremental: Se le llama “número de dígitos incrementales” a aquel número para el que cada uno de sus dígitos es menor o igual al que le sigue. Por ejemplo, 1338 es un número de dígitos incrementales; porque 1<3, 3=3 y 3<8. Por otro lado, 597 no lo es; porque 5<9 pero 9>7.
'''

vinyls = {
  '1': { 'name': 'Cuando Los Acéfalos Predominan',
        'author': 'Rawayana',
        'release_year': '2021',
        'stock': 1000,
        'sold': 0,
        'price': 10,
      },
  '2': { 'name': 'Notes on a Conditional Form',
        'author': 'The 1975',
        'release_year': '2020',
        'stock': 1200,
        'sold': 0,
        'price': 20,
      },
  '3': { 'name': 'Call Me If You Get Lost',
        'author': 'Tyler, the Creator',
        'release_year': '2021',
        'stock': 900,
        'sold': 0,
        'price': 30,
      },
  '4': { 'name': 'El Mal Querer',
        'author': 'Rosalía',
        'release_year': '2018',
        'stock': 980,
        'sold': 0,
        'price': 40,
      },
  '5': { 'name': 'The Dark Side of the Moon',
        'author': 'Pink Floyd',
        'release_year': '1973',
        'stock': 500,
        'sold': 0,
        'price': 50,
      },
}


purchases = {}

while True: # loop para que el programa corra hasta que quiera detenerlo
    print("Bienvenido a la tienda de discos de vinilo.\n1. Inventario\n2. Ventas\n3. Salir")
    module = input("Ingrese el número correspondiente al módulo al que desea ingresar: ")
    while (module != "1" and module != "2" and module != "3"): # validar input
        module = input("Ingreso inválido, ingrese el número correspondiente al módulo al que desea ingresar: ")
    
    print()

    if (module == "1"): # módulo de inventario
        print("Módulo de inventario\n1. Ver inventario\n2. Buscar por nombre")
        option = input("Ingrese el número correspondiente a la acción que desea realizar: ")
        while (option != "1" and option != "2"): # validar input
            option = input("Ingreso inválido, ingrese el número correspondiente a la acción que desea realizar: ")
        
        if (option == "1"): # ver todos los discos
            print("\nDISCOS DISPONIBLES")
            for vinyl_id, info in vinyls.items(): # loop sobre el diccionario
                print(f"\n--{vinyl_id}--------------")
                for k,v in info.items(): # loop para cada diccionario con información del disco
                    print(f"\t{k.title()}: {v}")
        
        if (option == "2"): # ver discos que coincidan con el input
            title = input("\nIngrese el título del album que desea buscar: ")
            found = False # esta variable nos va a ayudar aw mostrar un mensaje de error en caso de no encontrar nada
            print("\nRESULTADOS DE LA BÚSQUEDA\n")
            for vinyl_id, info in vinyls.items(): # loop sobre el diccionario
                if title.lower() in info['name'].lower(): # se verifica si el input está en el nombre del disco
                    found = True # se marca la variable como True para no mostrar el mensaje de error
                    for k,v in info.items(): # se muestra la información de las coincidencias
                        print(f"\t{k.title()}: {v}")
                    print()
            if not found:
                print("No se consiguieron discos con el nombre dado.")

        print()


    elif module == "2": # módulo de ventas
        print("Módulo de ventas\n1. Registrar venta\n2. Ver cantidad total de ventas")
        option = input("Ingrese el número correspondiente a la acción que desea realizar: ")
        while (option != "1" and option != "2"): # validar input
            option = input("Ingreso inválido, ingrese el número correspondiente a la acción que desea realizar: ")
        print()
        if (option == "1"): # registro de venta
            dni = input("Ingrese el dni del cliente: ")
            while not dni.isnumeric() or int(dni) == 0: # validación de dni
                dni = input("Ingreso inválido, ingrese el dni del cliente: ")
            name = input("Ingrese el nombre del cliente: ").title()
            while not name.replace(" ", "").isalpha(): # validación de nombre del comprador
                name = input("Ingreso inválido, ingrese el nombre del cliente: ").title()
            
            print("\nDISCOS DISPONIBLES")
            for vinyl_id, info in vinyls.items(): # se muestran todos los discos disponibles
                print(f"\n--{vinyl_id}--------------")
                for k,v in info.items():
                    print(f"\t{k.title()}: {v}")

            vinyl = input("\nIngrese el número correspondiente al disco a comprar: ") # se selecciona el disco que se quiera comprar
            while not vinyl.isnumeric() or int(vinyl) not in range(1, len(vinyls)+1): # validar input
                vinyl = input("Ingreso inválido, ingrese el número correspondiente al disco a comprar: ")
            
            discount = False # variable que nos sirve para mostrar en la factura el descuento (en caso de tenerlo)
            if (len(dni) >= 3): # se valida que el dni tenga tres o más dígitos porque si no, no funciona la validación de adentro
                if (dni[-1] >= dni[-2] and dni[-2] >= dni[-3]): # se valida que el último dígito sea mayor o igual que el penúltimo y que el penúltimo sea mayor o igual que el antepenúltimo
                    discount = True # se marca la variable como True para mostrar descuento en factura
                    print("\nPor tener como tres últimos dígitos de su dni un número de dígitos incrementales, se le otorgará un 20% de descuento en su compra.")

            purchases[f'{len(purchases) + 1}'] = { 'dni': dni, 'name': name, 'vinyl_id': vinyl } # se agrega la compra al diccionario que guarda las compras
            print("\nINFORMACIÓN DE LA COMPRA") # se muestra la factura. se usa len(purchases) porque ese sería el key de la última compra registrada en el diccionario
            print(f"\n--{len(purchases)}--------------")
            for k,v in purchases[f'{len(purchases)}'].items():
                print(f"\t{k.title()}: {v}")
            if discount: # esto se muestra solo si hay descuento
                print("\tDiscount: 20%")
                print(f"\tFinal price: {vinyls[f'{vinyl}']['price']-(vinyls[f'{vinyl}']['price']*0.2)}")
            
            # se actualiza el stock y la cantidad de unidades vendidas
            vinyls[vinyl]['stock'] -= 1
            vinyls[vinyl]['sold'] += 1

        else: # cantidad de ventas registradas. simplemente se imprime la longitud del diccionario que guarda las ventas
            print(f"Cantidad de ventas registradas: {len(purchases)}")

    else: # salir del sistema
        print("¡Hasta la próxima!")
        break # este break rompe el loop

    print()
            