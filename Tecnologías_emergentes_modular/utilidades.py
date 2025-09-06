import os  # Proporciona funciones para interactuar con el sistema operativo.
# Permite acceder al sistema de archivos, ejecutar comandos del sistema, manejar rutas,
# variables de entorno, procesos, etc.
import msvcrt  # "msvcrt" (Microsoft Visual C Runtime Library), exclusiva de Windows,
# que permite acceder a funciones del sistema como captura de teclas

def clrscr():
    """ Función para limpiar la consola """
    # Ejecuta el comando adecuado según el sistema operativo
    os.system('cls' if os.name == 'nt' else 'clear')

def getch():
    """
    Muestra un mensaje en consola y pausa la ejecución hasta que se presione cualquier tecla.
    Funciona únicamente en sistemas Windows.
    """
    print("Presione cualquier tecla para continuar ...")
    msvcrt.getch()
    
if __name__ == "__main__":
    clrscr()
    print("Pantalla limpiada. Ahora se espera una tecla.")
    getch()
