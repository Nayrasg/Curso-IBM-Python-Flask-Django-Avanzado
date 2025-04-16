import os

from gestion_contactos.contacto import Contacto


class ServicioContactos:
    NOMBRE_ARCHIVO = 'contactos.txt'

    def __init__(self):
        self.contactos = []
        # Revisar si ya existe el archivo contactos
        # Si ya existe, obtenemos los contactos del archivo
        if os.path.isfile(self.NOMBRE_ARCHIVO):
            self.contactos = self.obtener_contactos()
        # Sino, cargamos algunos snacks iniciales
        else:
            print("No existen contactos.")

    # Función para guardar contactos en el archivo
    def guardar_contactos_archivo(self, contactos):
        try:
            with open(self.NOMBRE_ARCHIVO, 'a') as archivo: # Abrimos el archivo en modo append (agregar al final)
                # Escribimos cada contacto en el archivo
                for contacto in contactos:
                    archivo.write(f'{contacto.escribir_contacto()}\n') # Llamamos al método escribir_contacto de la clase Contacto
        except Exception as e:
            print(f"Error al guardar contactos en el archivo: {e}")

    
    def agregar_contacto(self, contacto):
        self.contactos.append(contacto)     # Agregamos el contacto a la lista de contactos
        self.guardar_contactos_archivo([contacto]) # Llamos a la función guardar_contactos_archivo para guardar los contactos en el archivo

    # Función para leer los contactos del archivo
    # Esta función lee el archivo de contactos y crea objetos Contacto a partir de los datos leídos
    def obtener_contactos(self):
        contactos = [] # Creamos una lista vacía para almacenar los contactos
        try:
            with open(self.NOMBRE_ARCHIVO, 'r') as archivo: # Abrimos el archivo en modo lectura
                for linea in archivo: # Leemos cada línea del archivo
                    nombre, telefono, correo = linea.strip().split(',') # Separamos los datos por comas y eliminamos espacios en blanco
                    contacto = Contacto(nombre, telefono, correo) # Creamos un objeto Contacto con los datos leídos
                    contactos.append(contacto) # Agregamos el contacto a la lista de contactos
        except Exception as e:
            print(f"Error al obtener contactos del archivo: {e}")
        return contactos # Devolvemos la lista de contactos

    # Función para mostrar los contactos
    # Esta función imprime en consola la lista de contactos
    def mostrar_contactos(self):
        print("--- Lista de contactos: ---")
        for contacto in self.contactos: # Recorremos la lista de contactos
            print(contacto)
        print("----------------------------")

    # Función para obtener la lista de contactos
    def get_contactos(self):
        return self.contactos
    
    # Función para buscar un contacto
    # Esta función busca un contacto por nombre, teléfono o correo
    def buscar_contacto(self, dato):
        for contacto in self.contactos:
            if contacto.nombre.lower() == dato.lower() or \
                contacto.telefono == dato or \
                contacto.correo.lower() == dato.lower(): # Comparamos los nombres. telefonos y correos sin importar mayúsculas o minúsculas
                return contacto
    
    # Función para eliminar un contacto
    # Esta función elimina un contacto de la lista de contactos
    def eliminar_contacto(self, dato):
        contacto_a_eliminar = self.buscar_contacto(dato)  # Buscamos el contacto
        if contacto_a_eliminar:  # Si se encuentra el contacto
            self.contactos.remove(contacto_a_eliminar)  # Lo eliminamos de la lista
            try:
                # Sobreescribimos el archivo con los contactos restantes
                with open(self.NOMBRE_ARCHIVO, 'w') as archivo:
                    for contacto in self.contactos:
                        archivo.write(contacto.escribir_contacto() + '\n')
                return True  # Indicamos que el contacto fue eliminado
            except Exception as e:
                print(f"Error al escribir en el archivo: {e}")
                return False
        else:
            return False  # Si no se encuentra el contacto, devolvemos False
                
           