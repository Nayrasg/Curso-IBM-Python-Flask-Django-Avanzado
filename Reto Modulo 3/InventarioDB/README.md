# InventarioDB

Este proyecto es una aplicación de consola para la gestión de inventarios, desarrollada en Python. Permite realizar operaciones CRUD (Crear, Leer, Actualizar, Eliminar) sobre productos almacenados en una base de datos.

## Funcionalidades

- **Agregar productos**: Registra nuevos productos en el inventario.
- **Listar productos**: Muestra todos los productos almacenados.
- **Buscar productos**: Permite buscar un producto específico por su ID.
- **Actualizar productos**: Modifica los datos de un producto existente.
- **Eliminar productos**: Elimina un producto del inventario.

## Estructura del Proyecto
```
InventarioDB/
├── inventario_app.py       # Archivo principal que ejecuta el programa.
├── gestion_inventario.py   # Clase para realizar operaciones CRUD en la base de datos.
├── producto.py             # Clase que representa un producto.
├── conexion.py             # Módulo para gestionar la conexión a la base de datos.
└── README.md               # Documentación del proyecto.
```

### Archivos Principales

1. **`inventario_app.py`**:
   - Archivo principal que contiene el menú interactivo para gestionar el inventario.
   - Permite al usuario seleccionar opciones para realizar operaciones CRUD.
   - Utiliza las clases `GestionInventario` y `Producto` para interactuar con la base de datos.

2. **`gestion_inventario.py`**:
   - Contiene la clase `GestionInventario`, que implementa las operaciones CRUD:
     - `insertar`: Agrega un nuevo producto.
     - `seleccionar`: Recupera todos los productos.
     - `buscar`: Busca un producto por su ID.
     - `actualizar`: Actualiza los datos de un producto.
     - `eliminar`: Elimina un producto por su ID.

3. **`producto.py`**:
   - Define la clase `Producto`, que representa un producto en el inventario.
   - Atributos:
     - `id`: Identificador único del producto.
     - `nombre`: Nombre del producto.
     - `cantidad`: Cantidad disponible.
     - `precio`: Precio del producto.
     - `categoria`: Categoría del producto.

4. **`conexion.py`**:
   - Gestiona la conexión a la base de datos.
   - Proporciona métodos para establecer y cerrar conexiones.

## Requisitos

- Python 3.10 o superior.
- Base de datos MySQL..
- Librería `mysql-connector-python`.

## Instalación

1. Clona este repositorio en tu máquina local:
   ```bash
   git clone https://github.com/usuario/InventarioDB.git
   cd InventarioDB
   ```

2. (Opcional) Crea y activa un entorno virtual:
   - En Windows:
     ```bash
     python -m venv venv
     venv\Scripts\activate
     ```
   - En macOS/Linux:
     ```bash
     python3 -m venv venv
     source venv/bin/activate
     ```

3. Instala las dependencias necesarias, incluyendo mysql-connector-python :
   ```bash
   pip install mysql-connector-python
   ```

4. Configura la base de datos en el archivo `conexion.py` según tu entorno.

## Uso

1. Ejecuta el archivo principal:
   ```bash
   python inventario_app.py
   ```

2. Sigue las instrucciones del menú para realizar las operaciones deseadas.

### Menú de Opciones

```plaintext
*** Inventario ***
Menu:
1. Agregar producto
2. Listar productos
3. Buscar producto
4. Actualizar producto
5. Eliminar producto
6. Salir
Seleccione una opción:
```

### Ejemplo de Uso

#### Agregar un Producto
```plaintext
Seleccione una opción: 1
Ingrese el nombre del producto: Laptop
Ingrese la cantidad del producto: 10
Ingrese el precio del producto: 1500.00
Ingrese la categoría del producto: Electrónica
Producto insertado: 1
```

#### Listar Productos
```plaintext
Seleccione una opción: 2
Productos:
Producto(id=1, nombre='Laptop', cantidad=10, precio=1500.0, categoria='Electrónica')
```

