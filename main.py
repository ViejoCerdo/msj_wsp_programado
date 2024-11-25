
import os
import sys
import pywhatkit
import time 
from datetime import datetime
import pyautogui


def send_message():
    num = str(input('Ingresa el numero de telefono(incluyendo su codigo de pais): '))
    msg = str(input('Ingresa el mensaje que quieres enviar: '))
    hr = int(input('ingresa la hora en formato 24hrs (solo la hora): '))
    min = int(input('Ingrese el minuto de la hora( de 00 a 59 ): '))
    pywhatkit.sendwhatmsg(num, msg, hr, min)
    time.sleep(2)   
    pyautogui.press('esc')
    time.sleep(2)
    pyautogui.press('enter')


def tutorial():
    while True:
        os.system('clear')
        print('Espere...')
        time.sleep(1)
        os.system('clear')
        print('ATENCION: Para que la aplicacion funcione tienes que tener iniciada la sesion de WhatsApp en tu navegador predeterminado.')
        print('\n \n- En el menu principal ingresar la Opcion 1 presiona 1 y enter.')
        print('- Ingresa el numero con su prefijo correspondiente ejemplo +569.')
        print('- Escribe el mensaje que decias enviar.')
        print('- La aplicacion funciona en formato 24 horas por lo que tendras que ingresar la hora, solo la hora no con los minutos.' )
        print('- Finalmente se ingresa el minuto ejemplo 00 o 59, ejemplo si quieres enviar a los 5 minutos de la hora ingresada escribes 05.')
        print('- Despues de todo eso puedes ir a dormir y el mensaje se enviara solo, no apagues el computador pero si puedes apagar el monitor\no dejarlo con un salvapantallas negro')
        input('\n \nPresione [ENTER] para volver al menu')
        return main_menu()

    


def main_menu():
    while True:
        os.system('clear')
        print("----Menu principal----")
        print(" ")

        print(" ")
        print(" ")
        print("[1] Programar mensaje")
        print("[2] Instrucciones")
        print(" ")
        print("[0] Salir")
        print(" ")
        try:
            x = int(input('Ingresa una opcion del menu: '))

            if x == 1:
                os.system('clear')
                send_message()
            elif x == 2:
                tutorial()
            elif x == 0:
                print("Saliendo de la aplicacion.")
                print("Gracias c:")
                time.sleep(2)
                os.system('clear')
                sys.exit()
            else:
                print("Ingresar solo un numero del menu.")
        except ValueError:
            print("Por favor, ingresa una opcion valida del menu")
            time.sleep(2)

main_menu()
