from typing import Any
import cx_Oracle


class connectionb:
    def __init__(self):
         self.host = "192.168.21.146"
         self.port = "1521"
         self.service_name = "bsdesa"
         self.username = "BSDESA"
         self.password = "DESA1234"
         self.connection = None
        # self.host = "192.168.21.165"
        # self.port = "1521"
        # self.service_name = "SQL"
        # self.username = "bscc"
        # self.password = "titan66"
        # self.connection = None

    def connect(self):
        try:
            dsn_tns = cx_Oracle.makedsn(self.host, self.port, service_name=self.service_name)
            self.connection = cx_Oracle.connect(user=self.username, password=self.password, dsn=dsn_tns)
            print("-----------------------------------------")
            print("Conexión a la base de datos exitosa de Inyeccion")
            print("-----------------------------------------")
            return self.connection
        except cx_Oracle.Error as error:
            print("-----------------------------------------")
            print("Error al conectar a la base de datos:", error)
            print("-----------------------------------------")
            return None

    def close(self):
        if self.connection:
            self.connection.close()

    def execute_query(self, query: str, parameters: tuple = ()) -> Any:
        try:
            with self.connection.cursor() as cursor:
                cursor.execute(query, parameters)
                result = cursor.fetchall()
                return result
        except cx_Oracle.Error as error:
            print("-----------------------------------------")
            print("Error al ejecutar la consulta:", error)
            print("-----------------------------------------")
            return None

    def insert_data(self, query: str) -> bool:
        try:
            with self.connection.cursor() as cursor:
                cursor.execute(query)
                self.connection.commit()
                print("-----------------------------------------")
                print("Datos insertados exitosamente.")
                print("-----------------------------------------")
                return True
        except cx_Oracle.Error as error:
            print("-----------------------------------------")
            print("Error al insertar datos:", error)
            print("-----------------------------------------")
            self.connection.rollback()
            return False
