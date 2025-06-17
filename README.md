# RoadTripFoodies (Tercera Entrega Mateo Luis Rubio)

**RoadTripFoodies** es un blog que combina recetas y viajes, permitiendo registrar platos típicos asociados a destinos turísticos, junto con sus autores. Este proyecto fue desarrollado en Django para la 3era entrega de la comisión 69560 del curso de Python de la plataforma CoderHouse.

## Funcionalidades

- Registro de Recetas, Autores y Destinos mediante formularios HTML.
- Listado de todas las recetas en la página principal.
- Búsqueda de recetas por título o por nombre del destino.
- Vistas detalladas de cada receta, autor y destino.
- Estilo responsivo y moderno utilizando Bootstrap 5.
- Panel de administración de Django habilitado para gestión completa.

## Estructura del proyecto

- **Modelos (`models.py`)**:
  - `Autor`: nombre, biografía y email.
  - `Destino`: nombre, país, descripción.
  - `Receta`: título, descripción, ingredientes, pasos, autor y destino.

- **Formularios (`forms.py`)**:
  - `AutorForm`, `DestinoForm`, `RecetaForm`.

- **Vistas (`views.py`)**:
  - Página principal (`home`)
  - Formulario para crear recetas, autores y destinos
  - Vistas de detalle para cada entidad

- **Templates con herencia (`templates/core/`)**:
  - `base.html` (estructura principal)
  - `home.html`, `receta_form.html`, `autor_form.html`, `destino_form.html`
  - `receta_detalle.html`, `autor_detalle.html`, `destino_detalle.html`

## Cómo ejecutar el proyecto

1. Clonar el repositorio:

   ```bash
   git clone https://github.com/tu_usuario/roadtripfoodies.git
   cd roadtripfoodies

2. Crear y activar un entorno virtual:

   ```bash
   python -m venv env
   source env/bin/activate        # En Windows: env\Scripts\activate

3. Instalar las dependencias necesarias:

   ```bash
    pip install django

4. Aplicar las migraciones iniciales:

    ```bash
    python manage.py migrate

5. Crear un superusuario (recomendado):

   ```bash
   python manage.py createsuperuser

6. Ejecutar el servidor:

   ```bash
    python manage.py runserver

7. Acceder desde el navegador:

   ```bash
    Página principal: http://127.0.0.1:8000/
	Panel de administración: http://127.0.0.1:8000/admin/

## Estructura de carpetas

    roadtripfoodies/
    ├── core/
    │   ├── models.py
    │   ├── views.py
    │   ├── forms.py
    │   ├── templates/
    │   │   └── core/
    │   │       ├── base.html
    │   │       ├── home.html
    │   │       ├── receta_form.html
    │   │       ├── autor_form.html
    │   │       ├── destino_form.html
    │   │       ├── receta_detalle.html
    │   │       ├── autor_detalle.html
    │   │       └── destino_detalle.html
    ├── roadtripfoodies/
    │   └── settings.py
    ├── db.sqlite3
    ├── manage.py