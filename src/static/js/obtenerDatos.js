
function obtenerDatos(id){
    ///lo que estamos haciendo a continuacion es cambiando la accion que ejecuta el formulario
    document.getElementById('formulario').action = '/editar_producto/'+id 
    document.getElementById('boton').innerHTML = 'Actualizar'
    // nos sirve para recuperar nuestro campo unico
    //extrayendo los datos de cada reglon de nuestra tabla, en cada uno de los campos unicos
    nombreactual = document.getElementById('tabla_nombre'+id).innerHTML 
    //el innerHTML lo utilizamos para obtener el texto interno de cada uno de los renglones
    valoractual = document.getElementById('tabla_valor'+id).innerHTML
    cantidadactual = document.getElementById('tabla_cantidad'+id).innerHTML
    document.getElementById('nombre_producto').value = nombreactual
    document.getElementById('valor_producto').value = valoractual
    document.getElementById('cantidad').value = cantidadactual

} 