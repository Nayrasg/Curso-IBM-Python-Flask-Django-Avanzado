from gestion_inventario import GestionInventario
from producto import Producto


print('*** Inventario ***')
opcion = None
while opcion != 6:
    print(f'''Menu:
    1. Agregar producto
    2. Listar productos
    3. Buscar producto
    4. Actualizar producto
    5. Eliminar producto
    6. Salir''')
    opcion = int(input('Seleccione una opción: '))
    
    if opcion == 1:
       # Insertar cliente
        nombre_var = input('Ingrese el nombre del producto: ')
        cantidad_var = input('Ingrese la cantidad del producto: ')
        precio_var = input('Ingrese el precio del producto: ')
        categoria_var = input('Ingrese la categoría del producto: ')
        producto = Producto(nombre=nombre_var, cantidad=cantidad_var, precio=precio_var, categoria=categoria_var)
        productos_insertados = GestionInventario.insertar(producto)
        print(f'Producto insertado: {productos_insertados}')
    elif opcion == 2:
         # Listar clientes
        productos = GestionInventario.seleccionar()
        print('Productos:')
        for producto in productos:
            print(producto)
    elif opcion == 3:
        # Buscar producto
        id_producto_var = int(input('Ingrese el ID del producto a buscar: '))
        producto = GestionInventario.buscar(id_producto_var)
        if producto:
            print(f'Producto encontrado: {producto}')
        else:
            print('Producto no encontrado.')
    elif opcion == 4:
        # Actualizar producto
        id_producto_var = int(input('Ingrese el ID del producto a actualizar: '))
        nombre_var = input('Ingrese el nuevo nombre del producto: ')
        cantidad_var = input('Ingrese la nueva cantidad del producto: ')
        precio_var = input('Ingrese el nuevo precio del producto: ')
        categoria_var = input('Ingrese la nueva categoría del producto: ')
        producto = Producto(id_producto_var, nombre_var, cantidad_var, precio_var, categoria_var)
        productos_actualizados = GestionInventario.actualizar(producto)
        print(f'Producto actualizado: {productos_actualizados}')
    elif opcion == 5:
        # Eliminar producto
        id_producto_var = int(input('Ingrese el ID del producto a eliminar: '))
        producto = Producto(id=id_producto_var)
        productos_eliminados = GestionInventario.eliminar(producto)
        if productos_eliminados == 0:
            print('No se encontró el producto para eliminar.')
        else:
            print(f'Producto eliminado: {productos_eliminados}')
        
else:
    print('Saliendo del programa...')