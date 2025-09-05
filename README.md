# Tapara Dev - Sitio Web Corporativo

Sitio web dinámico y gestionable para Tapara Dev, especializado en desarrollo de aplicaciones web, móviles e integraciones con sistemas externos.

## Características

- **CMS Integrado**: Sistema de gestión de contenido usando Django Admin
- **Diseño Responsivo**: Interfaz moderna y minimalista que se adapta a todos los dispositivos
- **Gestión de Contenido**:
  - Servicios ofrecidos
  - Portafolio de proyectos
  - Equipo de trabajo
  - Información corporativa
  - Formulario de contacto
- **Panel Administrativo**: Interfaz amigable para gestionar todo el contenido

## Tecnologías Utilizadas

- **Backend**: Django 5.0.4
- **Frontend**: Bootstrap 5, HTML5, CSS3, JavaScript
- **Base de Datos**: PostgreSQL (configurado para SQLite en desarrollo)
- **Formularios**: Django Crispy Forms
- **Iconos**: Font Awesome 6

## Instalación y Configuración

### Requisitos Previos

- Python 3.8 o superior
- pip (gestor de paquetes de Python)

### Configuración Local

1. **Clonar el repositorio**:
```bash
git clone https://github.com/csubero/tapara-web.git
cd tapara-web
```

2. **Crear entorno virtual**:
```bash
python -m venv venv
source venv/bin/activate  # En Windows: venv\Scripts\activate
```

3. **Instalar dependencias**:
```bash
pip install -r requirements.txt
```

4. **Configurar variables de entorno**:
```bash
cp .env.example .env
# Editar .env con tus configuraciones
```

5. **Ejecutar migraciones**:
```bash
python manage.py makemigrations
python manage.py migrate
```

6. **Crear superusuario**:
```bash
python manage.py createsuperuser
```

7. **Cargar datos de ejemplo**:
```bash
python manage.py create_sample_data
```

8. **Ejecutar servidor de desarrollo**:
```bash
python manage.py runserver
```

El sitio estará disponible en `http://localhost:8000`
El panel administrativo en `http://localhost:8000/admin`

## Configuración para Producción

### Base de Datos PostgreSQL

1. **Instalar PostgreSQL** y crear una base de datos

2. **Actualizar .env**:
```env
DEBUG=False
DB_NAME=tapara_db
DB_USER=tu_usuario
DB_PASSWORD=tu_contraseña
DB_HOST=localhost
DB_PORT=5432
SECRET_KEY=tu_clave_secreta_segura
```

3. **Instalar psycopg2**:
```bash
pip install psycopg2-binary
```

4. **Actualizar settings.py** para usar PostgreSQL:
```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': config('DB_NAME'),
        'USER': config('DB_USER'),
        'PASSWORD': config('DB_PASSWORD'),
        'HOST': config('DB_HOST'),
        'PORT': config('DB_PORT'),
    }
}
```

### Archivos Estáticos

```bash
python manage.py collectstatic
```

## Estructura del Proyecto

```
tapara-web/
├── tapara_dev/          # Configuración principal de Django
├── content/             # App de gestión de contenido
│   ├── models.py        # Modelos de datos
│   ├── views.py         # Vistas de la aplicación
│   ├── admin.py         # Configuración del admin
│   ├── forms.py         # Formularios
│   └── templatetags/    # Filtros personalizados
├── templates/           # Plantillas HTML
├── static/              # Archivos CSS, JS, imágenes
├── media/               # Archivos subidos por usuarios
└── requirements.txt     # Dependencias
```

## Administración de Contenido

### Panel Administrativo

Accede a `http://localhost:8000/admin` para gestionar:

- **Información de la Empresa**: Logo, descripción, misión, visión, contacto
- **Servicios**: Gestión de servicios ofrecidos
- **Proyectos**: Portafolio con imágenes, tecnologías y enlaces
- **Equipo**: Miembros del equipo con fotos y redes sociales
- **Mensajes de Contacto**: Visualizar mensajes enviados desde el formulario

### Tipos de Contenido

#### Servicios
- Nombre del servicio
- Descripción completa y corta
- Icono (clases de Font Awesome)
- Marcado como destacado
- Orden de visualización

#### Proyectos
- Información del proyecto
- Imágenes
- Estado (Completado, En Progreso, Planificado)
- Tecnologías utilizadas
- Enlaces externos y GitHub

#### Equipo
- Información personal y profesional
- Foto de perfil
- Enlaces a redes sociales
- Estado activo/inactivo

## Personalización

### Colores y Estilo

Los colores principales se definen en `static/css/main.css`:

```css
:root {
    --primary-color: #3b82f6;
    --secondary-color: #64748b;
    --accent-color: #f59e0b;
}
```

### Logo y Branding

1. Subir logo desde el panel administrativo
2. Actualizar información de la empresa
3. Personalizar colores en el CSS

## Soporte

Para soporte técnico o consultas:

- **Email**: contacto@tapara.dev
- **Teléfono**: +58 424-1234567
- **GitHub**: [csubero/tapara-web](https://github.com/csubero/tapara-web)

## Licencia

Este proyecto está licenciado bajo los términos que se establezcan con Tapara Dev.

---

**Tapara Dev** - Transformamos ideas en soluciones digitales