import re
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from gestion_contactos.contacto import Contacto
from gestion_contactos.servicio_contactos import ServicioContactos


class GestiónContactos:
    def __init__(self):
        self.servicio_contactos = ServicioContactos()
        self.contactos = []
    
    # Llamamos función que muestra menú y función que gestiona las opciones
    def gestor_contactos(self):
        salir = False
        while not salir: # Mientras salir no sea True, el bucle se ejecuta
            try:
                opcion = self.mostrar_menu()
                salir = self.ejecutar_opcion(opcion)
            except Exception as e:
                print(f'Ocurrio un error: {e}') 

    # Función que muestra el menú
    def mostrar_menu(self):
            print(f'''SISTEMA DE GESTIÓN DE CONTACTOS:
                  1. Agregar un contacto
                  2. Mostrar todos los contactos
                  3. Buscar un contacto
                  4. Eliminar un contacto
                  5. Salir''')
            return int(input('Elige una opción: '))
    
    # Función que ejecuta la opción elegida por el usuario
    def ejecutar_opcion(self, opcion):
            if opcion == 1:
                    self.agregar_contacto()
            elif opcion ==2:
                    self.servicio_contactos.mostrar_contactos()
            elif opcion == 3:
                    self.buscar_contacto()
            elif opcion == 4:
                    self.eliminar_contacto()
            elif opcion == 5:
                    print('Regresa pronto!')
                    return True
            else:
                    print(f'Opción inválida: {opcion}')
            return False
    
    # Función que comprueba si el nombre es válido
    def pedir_nombre(self):
          datos_validos = False # Variable para verificar si los datos son válidos
          while not datos_validos: # Bucle infinito para seguir pidiendo datos hasta que sean válidos
            try:
                nombre = input('Nombre del contacto: ').strip()
                if not nombre: # Si el nombre está vacío
                    print('El nombre no puede estar vacío.')
                    continue
            except ValueError: # Capturamos la excepción si el valor no es un texto
                  print('Nombre inválido. Debe ser un texto.')
            except Exception as e:
                  print(f'Ocurrió un error: {e}')
            datos_validos = True # Si los datos son válidos, salimos del bucle
          return nombre 
    
    # Función que comprueba si el teléfono es válido
    def pedir_telefono(self):
        datos_validos = False
        while not datos_validos: # Bucle infinito para seguir pidiendo datos hasta que sean válidos
            try:
                telefono = input('Teléfono: ').strip()
                if not telefono or not telefono.isdigit(): # Si el teléfono no es un número o está vacío
                    print('El teléfono no puede estar vacío y debe ser un número.')
                    continue
            except ValueError: # Capturamos la excepción si el valor no es un número entero
                print('Teléfono inválido. Debe ser un número entero.')
            except Exception as e:
                print(f'Ocurrió un error: {e}')
            datos_validos = True # Si los datos son válidos, salimos del bucle
        return telefono
    
    # Función que comprueba si el correo es válido
    def pedir_correo(self):
        datos_validos = False
        while not datos_validos:
            try:
                correo = input('Correo: ').strip()
                # Verificamos que el correo tenga un formato válido
                if not re.match(r'^[\w\.-]+@[\w\.-]+\.\w+$', correo): # Expresión regular para validar el formato del correo
                    print('El correo no es válido.')
                    continue
            except ValueError:
                print('Correo inválido.') # Capturamos la excepción 
            except Exception as e:
                print(f'Ocurrió un error: {e}')
            datos_validos = True
        return correo


    # Función que agrega un contacto
    def agregar_contacto(self):
        nombre = self.pedir_nombre() # Llamamos a la función pedir_nombre para pedir el nombre del contacto
        telefono = self.pedir_telefono() # Llamamos a la función pedir_telefono para pedir el teléfono del contacto
        correo = self.pedir_correo() # Llamamos a la función pedir_correo para pedir el correo del contacto
        nuevo_contacto = Contacto(nombre, telefono, correo) # Creamos un nuevo objeto Contacto con los datos ingresados
        self.servicio_contactos.agregar_contacto(nuevo_contacto) # Llamamos a la función agregar_contacto de la clase ServicioContactos para agregar el contacto
        print('Contacto agregado correctamente.')

    # Función que llama a la función buscar_contacto de la clase ServicioContactos
    def buscar_contacto(self):
        dato = input('Dato del contacto a buscar: ').strip() # Pedimos al usuario el dato del contacto a buscar
        resultado_contacto = self.servicio_contactos.buscar_contacto(dato) # Llamamos a la función buscar_contacto de la clase ServicioContactos para buscar el contacto
        print('--- Resultado de la búsqueda ---')
        if resultado_contacto: # Si se encontró el contacto
            print(resultado_contacto)
        else: # Si no se encontró el contacto   
            print('No se encontró el contacto.')
    

    def eliminar_contacto(self):
        dato = input('Dato del contacto a eliminar: ').strip()
        resultado_contacto = self.servicio_contactos.eliminar_contacto(dato)
        if resultado_contacto: # Si se encontró el contacto
            print('Contacto eliminado correctamente.')
        else:
            print('No se encontró el contacto.')
        


if __name__ == '__main__': # Si el archivo se ejecuta directamente, se crea una instancia de la clase GestiónContactos y se llama a la función gestor_contactos
    # para iniciar el programa
    gestion_contactos = GestiónContactos()
    gestion_contactos.gestor_contactos() # Llamamos a la función gestor_contactos para iniciar el programa