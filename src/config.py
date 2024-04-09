
from psycopg2 import connect

HOST = 'localhost'
PORT = 5432
BD = 'bd_parcial'
USUARIO = 'postgres'
PASSWORD = '123456789'

def EstablecerConexion():
    try:
        conexion = connect(host=HOST, port=PORT, dbname=BD, user=USUARIO,password=PASSWORD)
    except ConnectionError: #En caso de error de conexion, este nos imprimieria por consola un mensaje
        print("Error De Conexion")
    return conexion #estamos retornando nuestra conexion


