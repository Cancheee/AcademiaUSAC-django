## Descripción del proyecto

La “Academia USAC” es una institución que ofrece una amplia variedad de cursos
especializados en el área de ingeniería. Actualmente cuentan con un sistema no
muy convencional. Por ello, se requiere de sus servicios como ingeniero con
conocimientos en programación para que desarrolle una nueva aplicación en la que
se tenga un mejor control de los cursos en los que se inscriben los estudiantes.
Se requiere que el sistema pueda ser utilizado por el administradores,
profesores y estudiantes, esto implica que la solución deberá tener un diseño
agradable e intuitivo de acorde a los requerimientos de la academia.



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


