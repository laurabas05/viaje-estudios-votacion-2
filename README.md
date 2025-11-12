# Práctica: VIAJE DE ESTUDIOS — arma el stack con Docker Compose

## ¿Qué hemos hecho en esta práctica?

He creado un archivo `docker-compose.yaml` con dos contenedores referentes a dos servicios 'fiesta_app' y 'fiesta_nginx'.

En el primer contenedor `fiesta_app` he usado nuestro Dockerfile para que construya la imagen, y lo he expuesto en el puerto interno 8000, sin publicarlo al host. 

En el segundo contenedor `fiesta_nginx` he usado una imagen oficial de `nginx`, he montado el archivo de configuracion local dentro del contenedor de nginx (en solo lectura), he mapeado el puerto `8080` del host al puerto `8000` del contenedor de nginx y, por último, con `depends_on` he hecho que Docker inicie primero el contenedor `fiesta_app` antes de levantar nuestro contenedor `web`.

## App accesible en `http://localhost:8080/`

<img width="1613" height="958" alt="Captura de pantalla 2025-11-12 231111" src="https://github.com/user-attachments/assets/43bcc8ea-67aa-4a40-9227-79684aea9dd9" />

## Comandos utilizados

Levantar la app: `docker compose up`

Detener la app: `docker compose down -v`

## ¿Por qué Nginx va delante de Flask/Gunicorn?

Nginx va delante de Flask/Gunicorn porque se encarga de gestionar las peticiones HTTP del cliente y luego las reparte al backend. Además, también se encarga de servir los archivos estáticos. También ayuda a que la página web aguante más cuando hay mucha gente conectada y a mantenerla más segura.

Gunicorn solo se dedica a ejecutar el código de la app Flask.
