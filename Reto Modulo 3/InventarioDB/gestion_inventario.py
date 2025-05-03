from conexion import Conexion
from producto import Producto


class GestionInventario:
    SELECCIONAR = "SELECT * FROM productos ORDER BY id"
    INSERTAR = "INSERT INTO productos (nombre, cantidad, precio, categoria) VALUES (%s, %s, %s, %s)"
    ACTUALIZAR = "UPDATE productos SET nombre=%s, cantidad=%s, precio=%s, categoria=%s WHERE id=%s"
    ELIMINAR = "DELETE FROM productos WHERE id=%s"
    BUSCAR = "SELECT * FROM productos WHERE id=%s"

    @classmethod
    def seleccionar(cls):
        conexion = None
        try:
            conexion = Conexion.obtener_conexion()
            cursor = conexion.cursor()
            cursor.execute(cls.SELECCIONAR)
            registros = cursor.fetchall()
            # Mapeo de clase-tabla cliente
            productos = []
            for registro in registros:
                producto = Producto(registro[0], registro[1], registro[2], registro[3], registro[4])
                # Se asigna el objeto cliente a la lista de clientes
                productos.append(producto)
            return productos
        except Exception as e:
                print(f"Error al seleccionar productos: {e}")
        finally:
            if conexion is not None:
                cursor.close()
                Conexion.liberar_conexion(conexion)

    
    @classmethod
    def insertar(cls, producto):
        conexion = None
        try:
            conexion = Conexion.obtener_conexion()
            cursor = conexion.cursor()
            valores = (producto.nombre, producto.cantidad, producto.precio, producto.categoria)
            # Se asigna el objeto cliente a la lista de clientes
            cursor.execute(cls.INSERTAR, valores)
            conexion.commit()
            return cursor.rowcount 
        except Exception as e:
            print(f"Error al insertar productos: {e}")
        finally:
            if conexion is not None:
                cursor.close()
                Conexion.liberar_conexion(conexion)
    @classmethod
    def buscar(cls, id):
        conexion = None
        try:
            conexion = Conexion.obtener_conexion()
            cursor = conexion.cursor()
            cursor.execute(cls.BUSCAR, (id,))
            registro = cursor.fetchone()
            if registro:
                producto = Producto(registro[0], registro[1], registro[2], registro[3], registro[4])
                return producto
            else:
                return None
        except Exception as e:
            print(f"Error al buscar producto: {e}")
        finally:
            if conexion is not None:
                cursor.close()
                Conexion.liberar_conexion(conexion)

    @classmethod
    def actualizar(cls, producto):
        conexion = None
        try:
            conexion = Conexion.obtener_conexion()
            cursor = conexion.cursor()
            valores = (producto.nombre, producto.cantidad, producto.precio, producto.categoria, producto.id)
            # Se asigna el objeto cliente a la lista de clientes
            cursor.execute(cls.ACTUALIZAR, valores)
            conexion.commit()
            return cursor.rowcount 
        except Exception as e:
            print(f"Error al actualizar productos: {e}")
        finally:
            if conexion is not None:
                cursor.close()
                Conexion.liberar_conexion(conexion)      
    
    @classmethod
    def eliminar(cls, producto):
        conexion = None
        try:
            conexion = Conexion.obtener_conexion()
            cursor = conexion.cursor()
            valores = (producto.id,)
            cursor.execute(cls.ELIMINAR, valores)
            conexion.commit()
            return cursor.rowcount 
        except Exception as e:
            print(f"Error al eliminar productos: {e}")
        finally:
            if conexion is not None:
                cursor.close()
                Conexion.liberar_conexion(conexion) 

if __name__ == "__main__":
    # Ejemplo de uso de la clase GestionInventario
    gestion = GestionInventario()
    # Insertar un producto
    nuevo_producto = Producto(nombre="Laptop", cantidad=10, precio=1500.00, categoria="Electrónica")
    gestion.insertar(nuevo_producto)
    
    # Listar productos
    productos = gestion.seleccionar()
    for producto in productos:
        print(producto)
    
    # Buscar un producto
    producto_buscado = gestion.buscar(1)
    if producto_buscado:
        print(f"Producto encontrado: {producto_buscado}")
    
    # Actualizar un producto
    producto_actualizado = Producto(id=1, nombre="Laptop Actualizada", cantidad=5, precio=1200.00, categoria="Electrónica")
    gestion.actualizar(producto_actualizado)
    
    # Eliminar un producto
    gestion.eliminar(producto_actualizado)