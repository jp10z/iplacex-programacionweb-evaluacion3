# IPLACEX - Programación Web - Evaluación 3

Este repositorio contiene el desarrollo de la evaluación 3 de la asignatura
`Programación web`.

## Datos

- Nombre: José Ramos
- Periodo: 2024-2B
- Asignatura: Programación Web

## Consideraciones

- Estoy usando .gitignore para no subir al repositorio la carpeta del entorno virtual (venv) y otros archivos temporales, dado que no sería buena práctiva.

- El paquete flask lo instalo mediante archivo requeriments.txt, luego de la instalación utilicé el comando `pip freeze > requeriments-freeze.txt` para volcar la info de las versiones de las dependencias para no tener problemas de compatibilidad en futuras instalaciones.

## Ejecutar

1. Crear entorno virtual

```shell
python3 -m venv venv
```

2. Ingresar a entorno virtual

```shell
source venv/bin/activate
```

3. Instalar requisitos usando pip

```shell
pip install -r requeriments-freeze.txt
```

4. Levantar servicio

```shell
python3 app/main.py
```

5. Ingresar con un navegador a la página

```
http://localhost:5000/
```

## Capturas de pantalla

A continuación presento capturas de pantalla de la web en ejecución

### Ejecución desde terminal

![Imágen ejecución](assets/imagen-ejecucion.png)

### Home del sitio

![Imágen home](assets/imagen-home.png)

### Ejercicio 1

![Imágen ejercicio 1](assets/imagen-ejercicio1.png)

### Ejercicio 2

![Imágen ejercicio 2](assets/imagen-ejercicio2.png)