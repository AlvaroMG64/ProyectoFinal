# 🎵 ProyectoAlbumes

Aplicación web desarrollada con Django para la gestión de álbumes musicales, artistas y canciones.

Permite autenticación de usuarios y administración completa (CRUD) de las entidades principales del sistema.

---

## 🚀 Tecnologías utilizadas

- Python 3
- Django
- Bootstrap 5
- SQLite

---

## 📁 Estructura del proyecto

```
ProyectoAlbumes/
│
├── ProyectoAlbumes/
│   ├── settings.py
│   ├── urls.py
│   └── ...
│
├── AlbumManager/
│   ├── models.py
│   ├── views.py
│   ├── forms.py
│   ├── urls.py
│   ├── templates/
│   └── ...
│
├── db.sqlite3
├── manage.py
└── README.md
```

---

## 🔐 Autenticación

El proyecto utiliza el sistema de autenticación integrado de Django:

- Login mediante `LoginView`
- Logout mediante `LogoutView` (requiere POST en Django 5)
- Protección de vistas con `@login_required`

Rutas principales:

- `/login/`
- `/logout/`

---

## 📊 Funcionalidades

### 🏠 Dashboard

- Card centrado
- Muestra el nombre del usuario autenticado
- Fecha y hora en formato español `DD/MM/AAAA HH:MM:SS`
- Mensajes de reglas de negocio:
  - "Un álbum no puede tener más de 20 canciones."  
  - "Un artista no puede lanzar más de 2 álbumes en el mismo año."  
  - "Eliminar un álbum eliminará sus canciones asociadas."  

### 🎵 Gestión de Álbumes

- Listar álbumes (fecha en formato `DD/MM/AAAA`)
- Crear álbum
- Editar álbum
- Eliminar álbum (Cascada: borra canciones asociadas)
- Número de canciones calculado automáticamente

### 🎤 Gestión de Artistas

- Listar artistas
- Crear artista
- Editar artista
- Eliminar artista
- Campo **Género** obligatorio

### 🎶 Gestión de Canciones

- Listar canciones (duración en formato `MM:SS`)
- Crear canción (input adaptado a minutos:segundos)
- Editar canción
- Eliminar canción

---

## 🧠 Modelos principales

### Artista
- nombre (CharField)
- pais (CharField)
- genero (CharField)  # obligatorio

### Álbum
- titulo (CharField)
- artista (ForeignKey a Artista)
- fecha_lanzamiento (DateField)
- es_explicit (BooleanField)
- usuario (ForeignKey a User)
- num_canciones (calculado automáticamente)
- **Reglas de negocio:**
  - Máximo 20 canciones por álbum
  - Un artista no puede lanzar más de 2 álbumes en el mismo año
  - Al eliminar un álbum, se eliminan sus canciones asociadas

### Cancion
- titulo (CharField)
- duracion (DurationField, editable en MM:SS)
- album (ForeignKey a Álbum)

---

## 🖥️ Instalación y ejecución

### 1️⃣ Clonar el repositorio

```bash
git clone <url-del-repositorio>
cd ProyectoAlbumes
```

### 2️⃣ Crear entorno virtual

```bash
python -m venv venv
```

Activar entorno:

**Windows**

```bash
venv\Scripts\activate
```

**Mac/Linux**

```bash
source venv/bin/activate
```

### 3️⃣ Instalar dependencias

```bash
pip install django
```

### 4️⃣ Aplicar migraciones

```bash
python manage.py makemigrations
python manage.py migrate
```

### 5️⃣ Crear superusuario

```bash
python manage.py createsuperuser
```

### 6️⃣ Ejecutar servidor

```bash
python manage.py runserver
```

Abrir en el navegador:

```
http://127.0.0.1:8000/login/
```

---

## 🎨 Diseño

- Bootstrap 5 para el layout
- Navbar con icono musical
- Logout en rojo
- Formularios estilizados con clases `form-control`
- Login sin header ni footer

---

## 🔒 Seguridad

- CSRF habilitado
- Logout por POST (Django 5)
- Acceso restringido a usuarios autenticados

---

## 📌 Notas importantes

- El número de canciones en Álbum se calcula automáticamente.
- El logout requiere método POST.
- El login no hereda de `base.html`.

---

## 👨‍💻 Autor

Álvaro Mozo Gaspar

---

## 📄 Licencia

Proyecto educativo sin fines comerciales.