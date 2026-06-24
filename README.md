# CiudadSegura Backend

Este es el backend del proyecto **CiudadSegura**, una plataforma diseñada para registrar, gestionar y visualizar reportes de incidencias de seguridad en la ciudad. El sistema está construido utilizando **Python** y el framework **Django**, y utiliza **PostgreSQL** como motor de base de datos.

---

## 🛠️ Tecnologías y Herramientas

- **Lenguaje:** Python 3.10+
- **Framework Web:** Django (4.2+)
- **Base de Datos:** PostgreSQL
- **Manejo de Imágenes:** Pillow (requerido para el campo `ImageField` en Django)

---

## 📁 Estructura del Proyecto

A continuación se detalla la estructura principal del repositorio:

```text
ciudadsegura_backend/
├── Aplications/
│   └── reportes/                # Aplicación encargada de la gestión de reportes
│       ├── migrations/          # Historial de migraciones de base de datos
│       ├── admin.py             # Registro de modelos en el panel de administración
│       ├── apps.py              # Configuración de la aplicación
│       ├── models.py            # Modelos de base de datos (Report)
│       ├── serializers.py       # Serializadores (listos para Django REST Framework)
│       ├── urls.py              # Enrutamiento específico de la aplicación
│       └── views.py             # Lógica de las vistas
├── ciudadsegura_backend/        # Módulo de configuración del proyecto
│   ├── settings.py              # Configuración global de Django (Base de datos, Apps, etc.)
│   ├── urls.py                  # Rutas principales del proyecto
│   ├── wsgi.py / asgi.py        # Configuración para despliegue
│   └── media/                   # Carpeta de almacenamiento para archivos multimedia subidos
├── manage.py                    # Utilidad de línea de comandos de Django
└── README.md                    # Documentación del proyecto
```

---

## 📋 Modelo de Datos principal (`Report`)

La aplicación `reportes` cuenta con el modelo `Report`, el cual almacena la información de los incidentes de seguridad reportados por los usuarios:

| Campo | Tipo de Dato | Descripción |
| :--- | :--- | :--- |
| `id` | `AutoField` | Identificador único autoincremental (Clave primaria). |
| `description` | `TextField` | Descripción detallada de la incidencia o situación reportada. |
| `address` | `CharField(255)` | Dirección aproximada o punto de referencia del reporte. |
| `latitude` | `DecimalField(9, 6)` | Latitud geográfica del reporte (para geolocalización). |
| `longitude` | `DecimalField(9, 6)` | Longitud geográfica del reporte (para geolocalización). |
| `picture` | `ImageField` | Fotografía de evidencia asociada a la incidencia (opcional). |
| `creation_date` | `DateTimeField` | Fecha y hora de creación automática del reporte. |
| `update_date` | `DateTimeField` | Fecha y hora del último cambio realizado al reporte. |

---

## ⚙️ Requisitos e Instalación

Sigue estos pasos para levantar el entorno de desarrollo local:

### 1. Clonar el repositorio
```bash
git clone <URL_DEL_REPOSITORIO>
cd ciudadsegura_backend
```

### 2. Crear y activar un entorno virtual
En Windows:
```powershell
python -m venv venv
venv\Scripts\activate
```
En macOS/Linux:
```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Instalar las dependencias
Asegúrate de instalar Django y las librerías para base de datos y procesamiento de imágenes:
```bash
pip install django psycopg2 pillow
```
*(Opcional: Si se va a exponer una API REST en el futuro, instalar `djangorestframework`)*
```bash
pip install djangorestframework
```

### 4. Configurar la Base de Datos PostgreSQL
Asegúrate de tener instalado PostgreSQL y de que esté en ejecución en tu máquina. De acuerdo a la configuración actual en `settings.py`, debes crear una base de datos con los siguientes parámetros:
- **Database Name:** `ciudadsegura`
- **User:** `postgres`
- **Password:** `1234`
- **Host:** `localhost`
- **Port:** `5432`

> [!TIP]
> Si deseas utilizar credenciales distintas, puedes editarlas directamente en el diccionario `DATABASES` del archivo `ciudadsegura_backend/settings.py`.

### 5. Aplicar Migraciones
Ejecuta el siguiente comando para generar y aplicar las tablas en tu base de datos PostgreSQL:
```bash
python manage.py migrate
```

### 6. Crear un Superusuario (para acceder al panel de administración)
Genera una cuenta de administrador para gestionar los reportes desde la interfaz web de Django:
```bash
python manage.py createsuperuser
```
Sigue las instrucciones en la consola para definir el nombre de usuario, correo electrónico y contraseña.

### 7. Iniciar el Servidor de Desarrollo
Finalmente, ejecuta el servidor:
```bash
python manage.py runserver
```

El servidor estará disponible en la dirección local: **[http://127.0.0.1:8000/](http://127.0.0.1:8000/)**

---

## 🌐 Endpoints y Rutas Disponibles

- **Panel de Administración de Django:** [http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/)
  Permite a los administradores gestionar los reportes (`Report`), usuarios, grupos y permisos.
- **Rutas de la aplicación (futuras APIs):** La configuración base incluye la importación de `Aplications.reportes.urls` en las rutas principales, lista para ser descomentada y utilizada una vez se definan las vistas REST correspondientes.
