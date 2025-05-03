from mysql.connector import pooling, Error


class Conexion:
    DATABASE = 'inventario_db'
    USERNAME = 'root'
    PASSWORD = 'admin'
    DB_PORT = 3306
    HOST = 'localhost'
    POOL_SIZE = 5
    POOL_NAME = 'inventario_pool'
    pool = None

    @classmethod
    def obtener_pool(cls):
        if cls.pool is None: # Se crea el pool de conexiones si no existe
            try:
                cls.pool = pooling.MySQLConnectionPool(
                    pool_name=cls.POOL_NAME,
                    pool_size=cls.POOL_SIZE,
                    host=cls.HOST,
                    user=cls.USERNAME,
                    password=cls.PASSWORD,
                    database=cls.DATABASE,
                    port=cls.DB_PORT
                )
                return cls.pool
            except Error as e:
                print(f"Error al crear el pool de conexiones: {e}")
        else:
            return cls.pool  
       
    @classmethod
    def obtener_conexion(cls):
        return cls.obtener_pool().get_connection()

    @classmethod
    def liberar_conexion(cls, conexion):
        conexion.close()

if __name__ == '__main__':
     # Creamos un objeto pool
    pool = Conexion.obtener_pool()
    print(f"Pool de conexiones creado: {pool}")
    conexion1 = pool.get_connection()
    print(f"Conexión 1: {conexion1}")
    Conexion.liberar_conexion(conexion1)
    print(f"Conexión 1 liberada: {conexion1}")
   