# Proyecto de control de stock
## Trabajo integrador Alkemy - Django
### Author:  @SPablo2191 🐱‍🚀
## Introducción
Este proyecto fue desarrollado para el curso de propuesto por Alkemy para el aprendizaje de framework de python conocido como Django, el mismo presenta una interfaz sencilla para el agregado de productos y proveedores.

## ¿Como probarlo?

Para hacer uso del proyecto de manera local es necesario realizar los siguientes pasos:

1) Ingresar los siguiente comandos en consola:

```python
python3 -m venv [nombreDelEntornoVirtual]
```

este comando les creara un entorno virtual para para poder importar posteriormente los paquetes ahi.Para activarlo se emplea el siguiente comando:

```python
source nombreDelEntornoVirtual/bin/activate
```

y para apagarlo:

```python
deactivate
```

2) Despues correr el siguiente comando para obtener los paquetes empleados en la API:

```python
pip install -r requirements.txt
```

3) Inicializar el servidor por medio del siguiente comando:
```python
python manage.py runserver
```
NOTA: previo al uso del aplicativo, tiene que hacer las migraciones correspondientes para que se generen las tablas en la base de datos a partir de los models que se disponen con el siguiente comando:
```python
python manage.py makemigrations
```
4) Ya esta listo para cargar productos y proveedores!