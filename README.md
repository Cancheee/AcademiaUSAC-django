## Descripción del proyecto

La “Academia USAC” es una institución que ofrece una amplia variedad de cursos
especializados en el área de ingeniería. Actualmente cuentan con un sistema no
muy convencional. Por ello, se requiere de sus servicios como ingeniero con
conocimientos en programación para que desarrolle una nueva aplicación en la que
se tenga un mejor control de los cursos en los que se inscriben los estudiantes.
Se requiere que el sistema pueda ser utilizado por el administradores,
profesores y estudiantes, esto implica que la solución deberá tener un diseño
agradable e intuitivo de acorde a los requerimientos de la academia.

### Requerimientos

- Deben de existir al menos 4 roles dentro del servicio, un Administrado total,
Administrador, Colaborador u Empleado y Cliente.

- Además, toda la información deberá de estar encriptada para permitir
mantener de forma íntegra el registro, además se deberá contar con un
registro de intentos de inicio de sesión, que muestre el dispositivo, el usuario,
la fecha y hora. Además de eso se deberá de tener un registro de facturación
con correlativo único.

- La página web deberá ser una tienda virtual, en la cual se muestre una foto
del modelo, y el precio y además se deben de mostrar las tallas disponibles
en inventario junto con los colores, para agregar artículos al carrito ser debe
de iniciar sesión.

- A la hora de iniciar sesión se debe de pedir usuario y contraseña y luego la
autenticación de dos pasos, además si se ingresa más de 10 veces la
contraseña el usuario se bloqueará y solo el administrador podrá
desbloquearla en el caso de los administradores y en el caso de los clientes
se les enviará un correo de restablecimiento de contraseña automático,
también si el nombre de usuario no existe se debe sugerir registrarse. Para
el registro se debe de pedir la dirección de la persona, su CUI, un nombre de
usuario y una contraseña con las bases de una contraseña segura (un
símbolo, números, letras mayúsculas, letras mayúsculas y al menos 12
caracteres).

- El sistema debe de desarrollarse en Python utilizando Django con
Framework, PostgreSQL con gestor de base de datos, Docker como
contenedor.

### Roles

1. El **Administrador**, tendrá acceso total al sitio, para poder hacer
mantenimientos crear nuevos cursos, agregar catedraticos y hacer correcciones.
Podrá administrar todo lo referente a la pagina.

3. El **Catedratico** podrá ver los cursos y modificarlos, también podrá ver
las asignaciones

4. El **Estudiante** podrá ver los cursos disponibles, agregarlos a su carrito y
asigrnarse, junto con ver sus asignaciones pasadas y ver sus cursos matriculados

---

## Descarga y ejecución

1. Abrir la terminal de su sistema en el directorio que desea trabajar.
2. Descarge el repositorio con la instrucción: 
``` gh repo clone Cancheee/AcademiaUSAC-django ```
3. Verifique las modificaciones en los modelos con el comando:
```python manage.py makemigrations ```
4. Realice las migraciones de los modelos a la base de datos:
```python manage.py migrate ```
5. Ejecute el proyecto por medio de la instrucción: 
```python manage.py runserver ```

---


