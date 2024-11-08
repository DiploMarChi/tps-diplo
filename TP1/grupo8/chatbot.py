import matplotlib.pyplot as plt
from collections import Counter


# Función para validar el ingreso de opciones
def validar_opcion(mensaje, min_opcion, max_opcion):
    while True:
        try:
            opcion = int(input(mensaje))
            if min_opcion <= opcion <= max_opcion:
                return opcion
            else:
                print(f"Opción no válida. Por favor, elige un número entre {min_opcion} y {max_opcion}.")
        except ValueError:
            print("Entrada no válida. Debes ingresar un número.")

# Diccionario de actividades de pileta y sus horarios por día de la semana
actividades_pileta = {
    "Pileta Libre": {
        "Lunes": ["08:00 - 12:00", "13:00 - 17:00", "19:30 - 22:00"],
        "Martes": ["08:00 - 12:00", "13:00 - 17:00", "21:00 - 22:00"],
        "Miércoles": ["08:00 - 12:00", "13:00 - 17:00", "19:30 - 22:00"],
        "Jueves": ["08:00 - 12:00", "13:00 - 17:00", "19:30 - 22:00"],
        "Viernes": ["08:00 - 10:00", "13:00 - 17:00", "21:00 - 22:00"]
    },
    "Pre Infantil (3 a 5 Años)": {
        "Lunes": ["10:00 - 11:00"],
        "Miércoles": ["10:00 - 11:00"],
        "Viernes": ["10:00 - 11:00"]
    },
    "Infantil (6 a 12 años)": {
        "Martes": ["10:00 - 11:30"],
        "Jueves": ["10:00 - 11:30"]
    },
    "Hidrogym": {
        "Lunes": ["17:00 - 18:00"],
        "Miércoles": ["17:00 - 18:00"],
        "Viernes": ["17:00 - 18:00"]
    },
    "Terapéutica": {
        "Martes": ["11:00 - 12:00"],
        "Jueves": ["11:00 - 12:00"]
    },
    "Revisación": {
        "Lunes": ["18:00 - 19:00"],
        "Miércoles": ["18:00 - 19:00"]
    }
}

# Diccionario de actividades deportivas y sus horarios
actividades_deportivas = {
    "Fútbol": ["Martes y Jueves: 18:00 a 20:00", "Sábado: 10:00 a 12:00"],
    "Básquet": ["Lunes y Miércoles: 17:00 a 19:00", "Viernes: 16:00 a 18:00"],
    "Vóley": ["Martes y Jueves: 19:00 a 21:00"],
    "Yoga": ["Lunes, Miércoles y Viernes: 09:00 a 10:00"],
    "Zumba": ["Martes y Jueves: 18:00 a 19:00"]
}

# Lista para almacenar las opciones seleccionadas
opciones_seleccionadas = []

print("¡Bienvenido al Chatbot de Horarios del Polideportivo de Santa Clara del Mar!")

continuar = True
while continuar:
    # Mostrar menú principal
    print("\n¿En qué puedo ayudarte hoy?")
    print("1. Ver horarios de pileta")
    print("2. Ver horarios de actividades deportivas")
    print("3. Información general")
    print("4. Ver actividades seleccionadas")
    print("5. Ver gráfico de actividades seleccionadas")
    print("6. Salir")
    
    opcion = validar_opcion("Elige una opción (1-6): ", 1, 6)

    if opcion == 1:
        # Selección de actividad de pileta
        print("\nActividades de pileta disponibles:")
        for i, actividad in enumerate(actividades_pileta, 1):
            print(f"{i}. {actividad}")
        
        seleccion_actividad = validar_opcion("Elige una opción (1-6): ", 1, len(actividades_pileta))
        
        # Mapear la selección de actividad al nombre de la actividad
        actividad_seleccionada = list(actividades_pileta.keys())[seleccion_actividad - 1]
        opciones_seleccionadas.append(actividad_seleccionada)  # Guardar en la lista
        
        # Mostrar horarios de la actividad seleccionada para todos los días
        print(f"\nHorarios de {actividad_seleccionada}:")
        for dia, horarios in actividades_pileta[actividad_seleccionada].items():
            print(f"- {dia}:")
            for horario in horarios:
                print(f"  {horario}")

    elif opcion == 2:
        # Mostrar actividades deportivas
        print("\nActividades deportivas disponibles:")
        for i, actividad in enumerate(actividades_deportivas, 1):
            print(f"{i}. {actividad}")

        seleccion_actividad_deportiva = validar_opcion("Elige una opción (1-5): ", 1, len(actividades_deportivas))
        
        # Mapear la selección de actividad deportiva al nombre de la actividad
        actividad_seleccionada = list(actividades_deportivas.keys())[seleccion_actividad_deportiva - 1]
        opciones_seleccionadas.append(actividad_seleccionada)  # Guardar en la lista
        
        # Mostrar horarios de la actividad deportiva seleccionada
        print(f"\nHorarios de {actividad_seleccionada}:")
        for horario in actividades_deportivas[actividad_seleccionada]:
            print(f"- {horario}")

    elif opcion == 3:
        print("\nInformación general del Polideportivo:")
        print("- Dirección: Calle Principal 123, Santa Clara del Mar.")
        print("- Teléfono de contacto: (0223) 123-4567.")
        print("- Horarios de atención: Lunes a Viernes de 08:00 a 20:00.")
    
    elif opcion == 4:
        # Mostrar las actividades seleccionadas hasta el momento
        if opciones_seleccionadas:
            print("\nActividades seleccionadas:")
            for actividad in opciones_seleccionadas:
                print(f"- {actividad}")
        else:
            print("\nNo has seleccionado ninguna actividad aún.")
    
    elif opcion == 5:
        # Generar gráfico de actividades seleccionadas
        
        if opciones_seleccionadas:
            
            actividad_frecuencias = Counter(opciones_seleccionadas)  # Contar la frecuencia de cada actividad
            actividades = list(actividad_frecuencias.keys())
            cantidades = list(actividad_frecuencias.values())
            colores=['red','blue','green','purple','orange']           
            plt.figure(figsize=(10, 6))
            plt.bar(actividades, cantidades, color=colores)
            plt.xlabel('Actividades')
            plt.ylabel('Cantidad de Selecciones')
            plt.title('Actividades más seleccionadas')
            plt.xticks(rotation=90, ha='right')
            plt.yticks(range(1,10,1))
            plt.tight_layout()  # Ajustar para que los elementos no se solapen
            plt.show()
            #Limpiar el grafico
            #plt.clf()
        else:
            print("\nNo has seleccionado ninguna actividad aún para generar un gráfico.")

    elif opcion == 6:
        continuar = False
        print("¡Gracias por usar el Chatbot del Polideportivo! Que tengas un buen día.")