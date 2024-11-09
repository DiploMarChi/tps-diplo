#functiones, clases, etc
from general import *

import matplotlib.pyplot as plt


#items vs ocurrencias
def estadisticasA(data: MenuData):
    itemVendidos = data.orders.itemsOcurrences

    plt.bar(list(itemVendidos.keys()), list(itemVendidos.values()), color ='green', width = 0.4)

    plt.xlabel("Items a la venta")
    plt.ylabel("No. de items vendidos")
    plt.title("Venta de items")
    plt.show()
    return data

#paths vs veces
def estadisticasB(data: MenuData):
    usoDePaths = data.options.ocurrences

    plt.bar(list(usoDePaths.keys()), list(usoDePaths.values()), color ='green', width = 0.4)

    plt.xlabel("'Paths'")
    plt.ylabel("No. de veces que se ha visitado")
    plt.title("Uso del menu")
    plt.show()
    return data 

#items vs ganancia
def estadisticasC(data: MenuData):
    ordenDeItems = data.orders.itemsOcurrences
    costoDeItems = data.orders.itemsCost

    gananciaTotalDeItems = {}
    for item, value in ordenDeItems.items():
        if item in gananciaTotalDeItems:
            gananciaTotalDeItems[item] += (costoDeItems[item] * ordenDeItems[item])

        else:
            gananciaTotalDeItems[item] = (costoDeItems[item] * ordenDeItems[item])

    plt.bar(list(gananciaTotalDeItems.keys()), list(gananciaTotalDeItems.values()), color ='green', width = 0.4)

    plt.xlabel("Item")
    plt.ylabel("Ganancias")
    plt.title("Ganancias totales de cada item | Ganancias totales: " + str(data.orders.itemsTotalCost))
    plt.show()
    return data 

def verOrdenes(data: MenuData):
    cls()
    print(str(data.orders))
    waitForKeyPress()

    return data

def verOrden(data: MenuData):
    cls()
    print(str(data.order))
    waitForKeyPress()

    return data

def confirmarOrden(data: MenuData):
    if not data.order.isOrderEmpty():
        data.confirmOrder()

        cls()
        print("Orden confirmada")
        waitForKeyPress()
    else:
        cls()
        print("Orden vacia")
        waitForKeyPress()

    data.options.setBack()

    return data

def cancelarOrden(data: MenuData):
    data.order = data.orders.getNewOrder()
    
    data.options.setBack()

    return data

def atras(data: MenuData):
    data.options.setBack()

    return data

def salir(data: MenuData):
    data.setKeepExcecuting(False)

    return data

def agregarAgua(data: MenuData):
    data.order.addItemToOrder("Agua", 100)

    cls()
    print("Item Agregado\n")
    waitForKeyPress()

    return data

def agregarAsado(data: MenuData):
    data.order.addItemToOrder("Asado", 10000)

    cls()
    print("Item Agregado\n")
    waitForKeyPress()

    return data

def agregarPostreBalcarce(data: MenuData):
    data.order.addItemToOrder("Postre Balcarce", 15000)

    cls()
    print("Item Agregado\n")
    waitForKeyPress()

    return data

def agregarPicadaA(data: MenuData):
    data.order.addItemToOrder("Picada Abstracta", 20000)

    cls()
    print("Item Agregado\n")
    waitForKeyPress()

    return data

def agregarEmpanadaC(data: MenuData):
    data.order.addItemToOrder("Empanada de Carne", 6000)

    cls()
    print("Item Agregado\n")
    waitForKeyPress()

    return data

menuTree = {
    "Nueva orden": {
        "Agregar": {
            "Bebidas": {
                "Agua" : { 
                    "label": " -- 100$",
                    "function": agregarAgua 
                },

                "Atras": { "function": atras }
            },

            "Postres": {
                "Postre Balcarce" : { 
                    "label": " -- 15000$",
                    "function": agregarPostreBalcarce 
                },
                
                "Atras": { "function": atras }
            },

            "Picadas": {
                "Picada Abstracta" : { 
                    "label": " -- 20000$",
                    "function": agregarPicadaA
                },
                
                "Atras": { "function": atras }
            },

            "Comida": {
                "Empanada de Carne" : { 
                    "label": " -- 6u * 6000$",
                    "function": agregarEmpanadaC
                },

                "Atras": { "function": atras }
            },

            "Especialidad": {
                "Asado": { 
                    "label": " -- 10.000$",
                    "function": agregarAsado 
                },

                "Atras": { "function": atras }
            },

            "Atras": { "function": atras }
        },

        "Ver orden": { "function": verOrden },
        "Confirmar": { "function": confirmarOrden },
        "Cancelar": { "function": cancelarOrden }
    },

    "Ver ordenes": { "function": verOrdenes },

    "Estadisticas": {
        "1": { 
            "label": ": -- Numero de veces que items han aparecido en total",
            "function": estadisticasA 
        },

        "2": { 
            "label": ": -- Ganancia de cada item vendido",
            "function": estadisticasB 
        },

        "3": { 
            "label": ": -- Veces que se ha visto la mayoria de opciones",
            "function": estadisticasC 
        },

        "Atras": { "function": atras }
    },

    "Ayuda": {
        "Atras": {
            "label": " -- Para navegar el menu debe escribir el nombre de la opcion que desea seleccionar, independientemente de mayusculas y minusculas; algunas opciones tendran una etiqueta de texto marcado con '--' de antemano en estos casos deberia ignorar esa parte de la opcion para seleccionarla",
            "function": atras
        }
    },

    "Salir": { "function": salir }
}
