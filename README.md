
<h1>Prueba técnica, becario en desarrollo web.</h1>

<h2> Pedro Ortiz Clavijo </h2>
<p>
<img width="180" src="img/logo].png">
</p>

![Static Badge](https://img.shields.io/badge/app-v1.0.0-red)
![GitHub Created At](https://img.shields.io/github/created-at/arik06/PruebaTecnica1)
<img alt="Static Badge" src="https://img.shields.io/badge/github-arik06-black?logo=github">


# Aplicación Web para Inventario

### Introducción

Esta aplicación web permite gestionar el inventario de una tienda de videojuegos. Los usuarios pueden visualizar todos los productos en stock, ordenarlos por precio y fecha de creación, y filtrarlos por características específicas.

### Tecnologías Utilizadas

- **Frontend:**
  - React
  - Bootstrap
  - Axios
  - GitHub Pages

- **Backend:**
  - Django
  - Django REST Framework
  - PostgreSQL

### Instalación y Configuración

#### Requisitos Previos

- Node.js
- Python
- Git

#### Clonación del Repositorio

```bash
git clone https://github.com/arik06/PruebaTecnica1.git
cd repositorio descargado
```

#### Instalación de Dependencias 
#### Frontend:
```bash

cd frontend
npm install
```

#### Backend:
```bash
cd backend
pip install -r requirements.txt
```

### Configuración del Entorno

```bash
#Crea un archivo .env en el directorio del backend con las siguientes variables:
SECRET_KEY=tu_secreto
DEBUG=True
DATABASE_URL=postgres://tu_usuario:tu_contraseña@localhost:5432/tu_base_de_datos
```

### 3. **Estructura del Proyecto**
```bash




### Estructura del Proyecto


tu-repositorio/
│
├── backend/
│   ├── manage.py
│   ├── myshop/
│   │   ├── settings.py
│   │   ├── urls.py
│   │   ├── wsgi.py
│   ├── inventory/
│       ├── models.py
│       ├── views.py
│       ├── serializers.py
│       ├── urls.py
│       ├── ...
│
├── frontend/
│   ├── public/
│   ├── src/
│       ├── components/
│       ├── App.js
│       ├── index.js
│   ├── package.json
│
└── README.md
```
#### Descripción de Componentes Principales
Backend:

#### models.py: Define los modelos de datos.
#### views.py: Contiene las vistas de la API.
#### serializers.py: Define los serializadores para los modelos.
#### Frontend:

#### components/: Contiene los componentes React.
#### App.js: Componente principal de la aplicación.
#### index.js: Punto de entrada de la aplicación React.




### Capturas de Pantalla

![Home](img/npm.png)


![Home](img/npm%20start.png)


#### Proyecto Frontend con React Corriendo 
![Home](img/react%20local%20host.png)


#### Backend localhost

![Home](img/backend.png)

#### SERVIDOR EN EJECUCION
![Home](img/BACKENDRUN.png)



#### django UI
![Home](img/django%20.png)

### Creación del Superusuario en Django

Para poder acceder al panel de administración de Django y gestionar los productos (consolas, juegos y accesorios), primero debes crear un superusuario. Sigue estos pasos:

1. Abre una terminal y navega al directorio de tu proyecto Django.
2. Ejecuta el siguiente comando para crear un superusuario:

```bash
   python manage.py createsuperuser
```
Sigue las instrucciones en la terminal para ingresar un nombre de usuario, correo electrónico y contraseña.
Una vez creado el superusuario, puedes acceder al panel de administración.

#### Gestión de Consolas, Juegos y Accesorios desde el Admin de Django
Inicia el servidor de desarrollo de Django:

```bash
python manage.py runserver
````

Abre un navegador web y ve a http://127.0.0.1:8000/admin.

Inicia sesión con las credenciales del superusuario que creaste anteriormente.

Después de iniciar sesión, verás el panel de administración de Django.

Agregar Consolas, Juegos y Accesorios
Agregar Juegos:

En el panel de administración, busca y haz clic en "Products".
Haz clic en "Add Product" (Agregar Producto).
Completa el formulario con los detalles del juego (nombre, descripción, precio, plataforma, condición, imagen, etc.).
Haz clic en "Save" (Guardar).
Agregar Consolas:

En el panel de administración, busca y haz clic en "Consoles".
Haz clic en "Add Console" (Agregar Consola).
Completa el formulario con los detalles de la consola (nombre, descripción, precio, portátil o de hogar, imagen, etc.).
Haz clic en "Save" (Guardar).
Agregar Accesorios:

En el panel de administración, busca y haz clic en "Accessories".
Haz clic en "Add Accessory" (Agregar Accesorio).
Completa el formulario con los detalles del accesorio (nombre, descripción, precio, imagen, etc.).
Haz clic en "Save" (Guardar).
Visualización y Edición de Productos
Desde el panel de administración, puedes ver la lista de todos los productos (juegos, consolas y accesorios) que has agregado.
Puedes hacer clic en cualquier producto para editar sus detalles o eliminarlo.
Ejemplo de Configuración de Admin para Consoles y Accessories
Aquí tienes un ejemplo de cómo puedes registrar los modelos de Consoles y Accessories en el archivo admin.py:

```bash
from django.contrib import admin
from .models import Product, Console, Accessory

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'platform', 'condition', 'created_at')
    search_fields = ('name', 'platform')

@admin.register(Console)
class ConsoleAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'portable', 'created_at')
    search_fields = ('name', )

@admin.register(Accessory)
class AccessoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'created_at')
    search_fields = ('name', )
```

Con esta configuración, los modelos de productos, consolas y accesorios estarán disponibles en el panel de administración de Django, permitiendo su gestión completa desde allí.


#### Documentación de la API
Endpoints Disponibles
Productos (Products)

GET /api/products/: Obtiene una lista de todos los productos. <br>
POST /api/products/: Crea un nuevo producto. <br>
GET /api/products/
/: Obtiene los detalles de un producto específico. <br>
PUT /api/products/
/: Actualiza un producto específico.<br>
DELETE /api/products/
/: Elimina un producto específico.
Consolas (Consoles)

GET /api/consoles/: Obtiene una lista de todas las consolas.<br>
POST /api/consoles/: Crea una nueva consola.<br>
GET /api/consoles/
/: Obtiene los detalles de una consola específica.<br>
PUT /api/consoles/
/: Actualiza una consola específica.<br>
DELETE /api/consoles/
/: Elimina una consola específica.
Accesorios (Accessories)

GET /api/accessories/: Obtiene una lista de todos los accesorios.<br>
POST /api/accessories/: Crea un nuevo accesorio.<br>
GET /api/accessories/
/: Obtiene los detalles de un accesorio específico.<br>
PUT /api/accessories/
/: Actualiza un accesorio específico.<br>
DELETE /api/accessories/
/: Elimina un accesorio específico.<br>

Parámetros de Consulta
Los endpoints GET para productos, consolas y accesorios admiten varios parámetros de consulta para filtrado, ordenamiento y búsqueda.

sort: Permite ordenar los resultados. Los valores posibles son: <br>

price-asc: Ordenar por precio ascendente. <br>
price-desc: Ordenar por precio descendente.<br>
date-asc: Ordenar por fecha de creación ascendente.<br>
date-desc: Ordenar por fecha de creación descendente.<br>
filter: Permite filtrar los resultados por nombre del producto.<br>

min_price: Filtra los resultados para mostrar solo productos con un precio mayor o igual al valor especificado.<br>

max_price: Filtra los resultados para mostrar solo productos con un precio menor o igual al valor especificado.<br>

platform: Filtra los resultados por plataforma (PC, Xbox, Nintendo, PlayStation).<br>

condition: Filtra los resultados por condición (Nuevo, Usado).<br>

portable (solo para consolas): Filtra las consolas por si son portátiles o de hogar.<br>

### Ejemplos de Solicitudes y Respuestas

Obtener todos los productos:

### Solicitud:
```bash
GET /api/products/

```

### Respuesta
```bash
[
  {
    "id": 1,
    "name": "Juego 1",
    "description": "Descripción del juego 1",
    "price": 59.99,
    "platform": "PC",
    "condition": "Nuevo",
    "created_at": "2024-06-18T12:34:56Z",
    "updated_at": "2024-06-18T12:34:56Z",
    "image": "http://127.0.0.1:8000/media/products/juego1.png"
  },
  ...
]

```

<br>
Crear un nuevo producto:

### Solicitud:

```bash
POST /api/products/
Content-Type: application/json

{
  "name": "Nuevo Juego",
  "description": "Descripción del nuevo juego",
  "price": 49.99,
  "platform": "Xbox",
  "condition": "Nuevo",
  "image": "http://127.0.0.1:8000/media/products/nuevojuego.png"
}

```

### Respuesta
```bash
{
  "id": 2,
  "name": "Nuevo Juego",
  "description": "Descripción del nuevo juego",
  "price": 49.99,
  "platform": "Xbox",
  "condition": "Nuevo",
  "created_at": "2024-06-18T13:45:00Z",
  "updated_at": "2024-06-18T13:45:00Z",
  "image": "http://127.0.0.1:8000/media/products/nuevojuego.png"
}

```

### Descripción de Modelos y Serializadores
Modelos <br>
Product

```bash
from django.db import models

class Product(models.Model):
    PLATFORM_CHOICES = [
        ('PC', 'PC'),
        ('Xbox', 'Xbox'),
        ('Nintendo', 'Nintendo'),
        ('PlayStation', 'PlayStation'),
    ]

    CONDITION_CHOICES = [
        ('Nuevo', 'Nuevo'),
        ('Usado', 'Usado'),
    ]

    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    platform = models.CharField(max_length=50, choices=PLATFORM_CHOICES)
    condition = models.CharField(max_length=50, choices=CONDITION_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to='products/', blank=True, null=True)

    def __str__(self):
        return self.name
```
### Consolas

```bash
from django.db import models

class Console(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    portable = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to='consoles/', blank=True, null=True)

    def __str__(self):
        return self.name

```

### Accesorios

```bash
from django.db import models

class Accessory(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to='accessories/', blank=True, null=True)

    def __str__(self):
        return self.name

```

### Serializadores

```bash
from rest_framework import serializers
from .models import Product

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'
```
### Pruebas de la API
Puedes realizar pruebas de la API utilizando herramientas como Postman o cURL para verificar que todos los endpoints funcionan correctamente y devuelven las respuestas esperadas.

Ejemplo con Postman
Obtener todos los productos:

Método: GET

URL: http://127.0.0.1:8000/api/products/ <br>

Crear un nuevo producto:

Método: POST

URL: http://127.0.0.1:8000/api/products/ <br>

Body

Actualizar un producto:

Método: PUT

URL: http://127.0.0.1:8000/api/products/1/ 



```bash
{
  "name": "Juego Actualizado",
  "description": "Descripción actualizada del juego",
  "price": 59.99,
  "platform": "PC",
  "condition": "Usado",
  "image": "http://127.0.0.1:8000/media/products/juegoactualizado.png"
}
```
Eliminar un producto:

Método: DELETE

URL: http://127.0.0.1:8000/api/products/1/

![Home](img/postman.png)

### Conclusiones

#### Estado Actual del Proyecto

La aplicación se encuentra en una fase funcional y cumple con los objetivos planteados en el caso de estudio. Las principales características implementadas son:

- Visualización de productos (juegos, consolas y accesorios) en un inventario.
- Filtrado y ordenación de productos por precio y fecha de creación.
- Subida y visualización de imágenes para los productos.
- Gestión de productos a través del panel de administración de Django.
- Implementación de una API RESTful para la interacción con los datos del inventario.

La estructura del proyecto es sólida y utiliza tecnologías modernas como React para el frontend y Django para el backend, lo que proporciona una base escalable y mantenible.


<h1>Referencias</h1>

- [Documentación de React](https://reactjs.org/docs/getting-started.html)
- [Documentación de Django](https://docs.djangoproject.com/en/stable/)
- [Bootstrap](https://getbootstrap.com/)
