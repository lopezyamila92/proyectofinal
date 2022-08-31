ENTREGA FINAL

Nombre y Apellido completo de los integrantes:
- Iozzolino, Gerardo
- Sanchez, Ayelén Alina

La división de tareas del proyecto realizado fueron bastante equitativas para que ambos podamos desarrollar y afianzar conocimientos. A continuación se detallan algunas de las mismas.

Tareas desarrolladas por Gerardo:
- Inicio del proyecto.
- Creación de models, clases y funciones.
- CRUD autos.
- Creación de templates.

Tareas desarrolladas por Ayelen:
- Creación de models, clases y funciones.
- CRUD usuarios.
- Creación de templates.
- Funcionalidad de botones.

VIDEO SOLICITADO
El siguiente video a muy resumidas cuentas una pequeña explicación de lo que contiene la página web.
link


Tabla de Contenidos:
Para acceder:
1. A tráves del Boton Registrate:
    - Ingresa el nombre de usuario que quieras.
    - Ingresa tu email.
    - Ingresa una contrseña.
    - Repeti la contraseña para estar seguros.
    - Hace "click" en el botón "Registrate!"
2. Si ya posees un usuario, debes dirigirte en la NavBar a "Inicio de Sesión"

Usuarios:
3. Si accedes a: http://127.0.0.1:8000/users/profile/ una vez que estas logueado, podras ver todos los datos de tu perfil. O también podes acceder haciendo "click" en "Mi Pefil"
Acá podes modificar tus datos de usuario, agregar alguna imagen, cambiar tu contraseña o eliminar tu cuenta.

3.1 Modicar Datos
Rellenando los campos que se te presentan en la pantalla podes moficar los datos de tu usuario. Una vez que este todo listo, hace "click" en "Enviar"
3.2 Cambiar Contraseña
Hace "click" en el botón de "Cambiar Contraseña", esto te redigira a otra página donde se te pedira tu contraseña vieja, y que escribas la contraseña nueva dos veces para seguridad.
3.3 Eliminar Cuenta
Si haces "click" en el botón "Borrar", te rediriga a una pantalla donde se te pregunta si estas seguro de esta acción, de ser así hace "click" en "Borrar" y tu cuenta sera eliminada.

Administración:
4. Ingresa a la administración de Django ingresando a http://127.0.0.1:8000/admin/ en el navegador.
4.1. Para poder acceder a esta dirección, debes tener un superusuario.

Inicio de página:
5. Se puede volver a la página de inicio del navegador ingresando a: http://127.0.0.1:8000/ o haciendo "click" en el botón "FORD" a la izquirda de la Navbar

Edición o eliminación de productos:
6. Si sos usuario administrador, podes crear, editar, borrar o eliminar un producto desde el panel de administración de Django o en "Autos" en la nabvar al desplegar los mismos, te brindará la opción. En caso que no seas usuario administrador, estas acciones no serán permitidas y la página te solicitará que te logues con un usuario administrador.

6.1. Crear Productos 
6.1.1 Desde la página: 
Deberás entrar al link http://127.0.0.1:8000/ford/create_autos/, ahí se te mostrar un formulario con los datos a completar. 
Cuando completes el nombre del producto, te pedimos que antes del mismo también escribas la clase de vehículo que es (la misma que seleccionaste arriba). Por ejemplo: SUV - nombre del producto; Deportivo - nombre del producto; etc.
6.1.2 Desde el panel de adminsitración de Django:
Deberas entrar a autos y hacer click en "Add Auto+" y ahí se te mostrar un formulario que debes completar.
Cuando completes el nombre del producto, te pedimos que antes del mismo también escribas la clase de vehículo que es (la misma que seleccionaste arriba). Por ejemplo: SUV - nombre del producto; Deportivo - nombre del producto; etc.
6.2 Edición de un producto:
Desde la Navbar entra a Autos, allí se te desplegara la lista de autos que tenemos. Hace "click" en "Editar" y se te presentara un formulario de edición del mismo.
6.3. Borrar un producto
Desde la Navbar entra a autos, allí se te desplegara la lista de autos que tenemos. Hace "click" en "Borrar" para eliminarlo de la lista. 


Condiciones para acceder a ciertas partes de la página:
7. Para poder ver la lista de autos o servicios, deberas estar logueado con un usuario.

Formulario de Contacto:
8. Si accedes a: http://127.0.0.1:8000/about/contact-us/ o desde el pie de págia en "Contactate" se va a desplegar un formulario, en el cual debes completar:
    - Tu nombre.
    - Dirección de correo para poder comunicarnos.
    - Teléfono de contacto para poder comunicarnos.
    - Tenes que seleccionar el tipo de consulta que necesitas realizar (menú desplegable).
    - Escribirnos tu mensaje.
    - Hacer click en el botón "Enviar"
    - Una vez cumplidos esos pasos, la página de rediccionaria al inicio de la misma.

Para buscar productos a través del NavBar:
9. Formulario de busqueda esta disponible en "http://127.0.0.1:8000/ford/search-products/search"
