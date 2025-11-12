# Práctica: VIAJE DE ESTUDIOS — arma el stack con Docker Compose

## ¿Qué recibes?

- Código completo de la app Flask (`app/`) con su `Dockerfile` listo para construir Gunicorn.
- Configuración de Nginx (`nginx/default.conf`) que ya apunta a `http://fiesta_app:8000`.
- **No** se incluye `docker-compose.yaml`: es lo que debes crear tú.

## Objetivo

Construye un `docker-compose.yaml` que levante toda la solución y exponga la web en `http://localhost:8080/`, manteniendo a Flask detrás de Nginx.

## Requisitos mínimos del `docker-compose.yaml`

1. **Servicio `fiesta_app`**
   - usa el Dockerfile entregado.
   - Expone Gunicorn en el puerto interno `8000` (no publiques ese puerto al host).

2. **Servicio `fiesta_nginx`**
   - Imagen `nginx:1.27-alpine`.
   - Depende de que se ejecute antes fiesta_app
   - Volumen `./nginx/default.conf:/etc/nginx/conf.d/default.conf:ro`.

3. **Red**
   - Usa la red por defecto que crea Compose.


## Qué debes entregar

1. `docker-compose.yaml` funcionando.
2. Captura o evidencia de la app accesible en `http://localhost:8080/`.
3. Lista de comandos utilizados para levantar y detener la solución.
4. Breve explicación (3–5 líneas) de por qué Nginx va delante de Flask/Gunicorn.

## Evaluación (10 pt)

- Compose levanta ambos servicios y respeta la arquitectura (4 pt).
- Nginx sirve la app correctamente y se accede por `8080` (3 pt).
- Entrega bien documentada (README + capturas + comandos) (2 pt).
- Buenas prácticas adicionales (restart, variables, bonus de seguridad) (1 pt).

> Recuerda: ningún navegador se conecta directamente a Flask; todo debe pasar por Nginx → Gunicorn → Flask dentro de la red creada por Docker Compose.
