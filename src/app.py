
from flask import Flask, render_template, request, redirect, url_for, flash
from config import * #nos traiga todo lo que hay en config

con_bd = EstablecerConexion() #Estamos llamando nuestra funcion donde almacenamos en otra variable de nombre con_bd

app=Flask(__name__)

@app.route('/')
def menu():
    cursor = con_bd.cursor()
    sql = "SELECT*FROM usuarios"
    cursor.execute(sql)
    UsuariosRegistrados = cursor.fetchall()
    #print(PersonasRegistradas)
    return render_template('index.html', usuarios = UsuariosRegistrados)

@app.route('/guardar_usuario', methods=['POST'])
def agregarUsuario():
    cursor = con_bd.cursor() #con esta linea nos permite la manipulacion de nuestra base de datos 
    email = request.form['email']
    password = request.form['password']
    
    if email and password:
        sql = """INSERT INTO usuarios(email, password) VALUES(%s, %s)""" 
        #guardar los datos en nuestra base de datos, en la table que ya creamos
        cursor.execute(sql,(email,password)) 
        con_bd.commit() 
        flash("Registro De Usuario Guardado Correctamente")
        #son mensajes que nos saldra a medida que completemos una accion
        return redirect(url_for('index'))
    else:
        return "Hay Algo Mal En La Consulta- Por Favor Verificar"

def crearTablaUsuarios():
    cursor = con_bd.cursor()
    cursor.execute("""CREATE TABLE IF NOT EXISTS usuarios(id serial NOT NULL, 
                   email character varying(50),
                   password character(50),  
                   CONSTRAINT pk_productos_id PRIMARY KEY (id));""")
    con_bd.commit() #sirve para confirmar los cambios en la base de datos



#------------------------------------------------------------------------------------------------
@app.route('/')
def index():
    cursor = con_bd.cursor()
    sql = "SELECT*FROM productos"
    cursor.execute(sql)
    ProductosRegistrados = cursor.fetchall()
    #print(PersonasRegistradas)
    return render_template('index.html', productos = ProductosRegistrados)

@app.route('/guardar_producto', methods=['POST'])
def agregarProducto():
    cursor = con_bd.cursor() #con esta linea nos permite la manipulacion de nuestra base de datos 
    nombre_producto = request.form['nombre_producto']
    valor_producto = request.form['valor_producto']
    cantidad = request.form['cantidad']
    
    if nombre_producto and valor_producto and cantidad:
        sql = """INSERT INTO productos(nombre_producto, valor_producto, cantidad) VALUES(%s, %s, %s)""" 
        #guardar los datos en nuestra base de datos, en la table que ya creamos
        cursor.execute(sql,(nombre_producto,valor_producto,cantidad)) 
        #aca estamos reemplazando los $s de la anterior linea por cada uno de nuestras variables
        con_bd.commit() 
        #el commit() nos sirve para confirmar la conexion y los cambios y estos se guarden es la base de datos
        #y se hace directamente con nuestra variable de conexion a base de datos
        flash("Registro Guardado Correctamente")
        #son mensajes que nos saldra a medida que completemos una accion
        return redirect(url_for('index'))
    else:
        return "Hay Algo Mal En La Consulta- Por Favor Verificar"
    

#-----------------------------------------------------------------------------------------------------------------------------
#crear una funcion que antes de hacer una consulta, va a crear la tabla en caso de que esta no exista en nuestra base de datos.
def crearTablaProductos():
    cursor = con_bd.cursor()
    cursor.execute("""CREATE TABLE IF NOT EXISTS productos(id serial NOT NULL, 
                   nombre_productos character varying(100),
                   valor_producto integer, 
                   cantidad integer, 
                   CONSTRAINT pk_productos_id PRIMARY KEY (id));""")
    con_bd.commit() #sirve para confirmar los cambios en la base de datos

#----------------------------------------------------------------------------------------------   
@app.route('/eliminar_producto/<int:id_producto>')
def eliminar(id_producto):
    cursor = con_bd.cursor()
    sql = "DELETE FROM productos WHERE id ={0}".format(id_producto)#borreme donde el id sea 0 y despues remplazelo por el id_persona
    cursor.execute(sql)
    con_bd.commit()#sirve para confirmar nuestros cambios en la base de datos y que son de manera permanentes
    flash("Registro Eliminado Correctamente")
    return redirect(url_for('index')) #estamos redirigiendo a una funcion, en caso de cumplir la anterior funcion

#------------------------------------------------------------------------------------------------------
@app.route('/editar_producto/<int:id_producto>', methods=['POST'])
def editar(id_producto):
    cursor = con_bd.cursor()
    nombre_producto = request.form['nombre_producto']
    valor_producto = request.form['valor_producto']
    cantidad = request.form['cantidad']
    if nombre_producto and valor_producto and cantidad:
        sql = """UPDATE productos
            SET nombre_producto=%s, 
            valor_producto=%s, 
            cantidad=%s
            WHERE id =%s""" 
        cursor.execute(sql,(nombre_producto,valor_producto,cantidad,id_producto)) 
        #aca estamos reemplazando los $s de la anterior linea por cada uno de nuestras variables
        con_bd.commit() #el commit() nos sirve para confirmar la conexion y los cambios y estos se guarden es la base de datos
        #y se hace directamente con nuestra variable de conexion a base de datos
        flash("Datos Actualizados Correctamente")
        return redirect(url_for('index'))
    else:
        return "Hay Algo Mal A La Hora de Actualizar Los Datos - Por Favor Verificar"
#--------------------------------------------------------------------------------------------

if __name__ =='__main__':
    app.secret_key = '123456789'
    app.run(debug=True, port=5555)

