#for sleep functionality
import time

#functiones, clases, etc
from general import *

#especifications related to the menu
from menu import *

#Interaction with user
def menu(data: MenuData):
    #preparing for an option to "exit"
    while data.doWeKeepExcecuting():
        menu = data.options.getOptions()
        
        #clear the console and print the current menu
        cls()
        print("Ultimas selecciones: \n")
        if len(data.options.lastSelections()) >= 3:
            for option in data.options.lastSelections():
                print(option)

            print("----------------\n\n")    

        for key, children in menu.items():
            print(children)

        #print most viewed option in menu


        #try to obtain input from the user try to cach any EOF
        selection = ""
        try:
            selection = input("\nIngrese el nombre de su seleccion:\n")
        except: #EOF
            selection = ""
            print("Error de entrada")
            waitForKeyPress()
        
        uppercases = {}
        for key in menu.keys():
            uppercases[key.upper()] = key

        selection = selection.upper()

        #check if input is key in the menu if not select again some option after a notification
        if selection in uppercases:
            #get selected menu option: menu or function to excecute "actions" and "functions" and store the
            #path
            selected = data.options.getSelected(uppercases[selection])
            data = selected.excecute(data)

        else:
            print("Opcion incorrecta")
            time.sleep(1)




#Requiere graficos (estadistica) (cosas mas usadas, etc), ultimas opciones, menu progresivo, "ayuda"

#Excecution
menu(MenuData(menuTree))