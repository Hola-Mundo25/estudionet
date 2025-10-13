import mysql.connector
from mysql.connector import Error

class Database:
    def get_connection(self):
        """Obtiene una conexión a la base de datos"""
        try:
            connection = mysql.connector.connect(
                host='localhost',
                database='estudionet_db',
                user='root',
                password=''
            )
            return connection
        except Error as e:
            print(f"❌ Error conectando a MySQL: {e}")
            return None
    
    def execute_query(self, query, params=None):
        """
        Ejecuta una query y retorna los resultados si es SELECT,
        o retorna True si es INSERT/UPDATE/DELETE exitoso
        
        Args:
            query (str): Query SQL a ejecutar
            params (tuple, optional): Parámetros para la query
        
        Returns:
            list: Lista de diccionarios con los resultados (para SELECT)
            bool: True si la operación fue exitosa (para INSERT/UPDATE/DELETE)
            None: Si hubo error
        """
        connection = self.get_connection()
        if not connection:
            return None
        
        cursor = None
        try:
            cursor = connection.cursor(dictionary=True)
            
            if params:
                cursor.execute(query, params)
            else:
                cursor.execute(query)
            
            # Si es un SELECT, retornar resultados
            if query.strip().upper().startswith('SELECT'):
                results = cursor.fetchall()
                return results
            
            # Si es INSERT, UPDATE o DELETE, hacer commit y retornar True
            connection.commit()
            return True
            
        except Error as e:
            print(f"❌ Error ejecutando query: {e}")
            if connection:
                connection.rollback()
            return None
            
        finally:
            if cursor:
                cursor.close()
            if connection:
                connection.close()
    
    def execute_query_one(self, query, params=None):
        """
        Ejecuta una query y retorna solo el primer resultado
        
        Args:
            query (str): Query SQL a ejecutar
            params (tuple, optional): Parámetros para la query
        
        Returns:
            dict: Diccionario con el primer resultado
            None: Si no hay resultados o hubo error
        """
        results = self.execute_query(query, params)
        if results and len(results) > 0:
            return results[0]
        return None