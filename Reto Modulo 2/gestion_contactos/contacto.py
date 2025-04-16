class Contacto:
    def __init__(self, nombre, telefono, correo):
        self.nombre = nombre
        self.telefono = telefono
        self.correo = correo

    def __str__(self):
        return f"Nombre: {self.nombre}, Teléfono: {self.telefono}, Correo: {self.correo}"
    
    def escribir_contacto(self):
        return f"{self.nombre},{self.telefono},{self.correo}" # Método para escribir el contacto en el archivo