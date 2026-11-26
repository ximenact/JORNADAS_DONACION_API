# JORNADA_API – API REST para la gestión de jornadas de donación de sangre

## 1. Descripción del proyecto

**JORNADA_API** es una API REST desarrollada con Python y FastAPI, orientada a la gestión de jornadas de donación de sangre y usuarios.

El proyecto permite realizar operaciones CRUD (Crear, Leer, Actualizar y Eliminar) sobre dos módulos principales: usuarios y jornadas de donación.

La aplicación utiliza PostgreSQL como sistema de gestión de bases de datos, alojado en Neon, y está organizada mediante una arquitectura por capas que facilita la separación de responsabilidades, el mantenimiento y la escalabilidad del código.

Además, la API cuenta con documentación interactiva mediante Swagger UI y se encuentra preparada para su despliegue en Render.

---

## 2. Objetivo general

Desarrollar una API REST que permita administrar la información de usuarios y jornadas de donación de sangre, implementando operaciones CRUD mediante una arquitectura por capas, utilizando FastAPI, SQLAlchemy y PostgreSQL.

### Objetivos específicos

- Implementar un módulo para la gestión de usuarios.
- Implementar un módulo para la gestión de jornadas de donación.
- Desarrollar operaciones de creación, consulta, actualización y eliminación de registros.
- Implementar validaciones para garantizar la integridad de los datos.
- Organizar el código mediante una arquitectura por capas.
- Conectar la aplicación con una base de datos PostgreSQL alojada en Neon.
- Documentar y probar los endpoints mediante Swagger.
- Desplegar la API en Render para permitir su acceso desde internet.
- Gestionar el código fuente y sus versiones mediante Git y GitHub.

---

## 3. Tecnologías utilizadas

| Tecnología | Descripción |
|---|---|
| Python | Lenguaje de programación utilizado para desarrollar la API. |
| FastAPI | Framework utilizado para construir los endpoints y gestionar las solicitudes HTTP. |
| PostgreSQL | Sistema de gestión de bases de datos relacional. |
| Neon | Servicio en la nube utilizado para alojar la base de datos PostgreSQL. |
| SQLAlchemy | ORM utilizado para interactuar con la base de datos desde Python. |
| Pydantic | Herramienta utilizada para validar y estructurar los datos. |
| pwdlib | Biblioteca utilizada para generar hashes seguros de contraseñas. |
| Uvicorn | Servidor ASGI utilizado para ejecutar la aplicación. |
| Python-dotenv | Biblioteca utilizada para cargar variables de entorno desde el archivo `.env`. |
| Swagger UI | Interfaz para visualizar y probar los endpoints de la API. |
| Git | Sistema de control de versiones. |
| GitHub | Plataforma utilizada para alojar el repositorio. |
| Render | Plataforma utilizada para desplegar la aplicación. |

---

## 4. Arquitectura del proyecto

El proyecto implementa una **arquitectura por capas**, en la que cada carpeta tiene una responsabilidad específica.

Esta organización permite mantener el código estructurado, facilitar su mantenimiento y separar la lógica del negocio de las operaciones relacionadas con la base de datos.

### Estructura de carpetas

```text
JORNADA_API/
│
├── app/
│   │
│   ├── database/
│   │   └── conexion.py
│   │
│   ├── models/
│   │   ├── usuario.py
│   │   └── jornada.py
│   │
│   ├── repositories/
│   │   ├── usuario_repository.py
│   │   └── jornada_repository.py
│   │
│   ├── routes/
│   │   ├── usuarios.py
│   │   └── jornadas.py
│   │
│   ├── schemas/
│   │   ├── usuario_schema.py
│   │   └── jornada_schema.py
│   │
│   └── services/
│       ├── usuario_service.py
│       └── jornada_service.py
│
├── main.py
├── requirements.txt
├── .env
├── .gitignore
└── README.md
```

### Responsabilidad de cada carpeta

#### 4.1. Database

Contiene la configuración necesaria para establecer la conexión con PostgreSQL.

Archivo principal:

- `conexion.py`: configura la conexión mediante SQLAlchemy, crea el motor de conexión, configura las sesiones y proporciona la dependencia para acceder a la base de datos.

#### 4.2. Models

Contiene los modelos de SQLAlchemy, que representan las tablas de la base de datos.

Archivos:

- `usuario.py`: define la estructura de la tabla de usuarios.
- `jornada.py`: define la estructura de la tabla de jornadas.

#### 4.3. Repositories

Contiene las operaciones que interactúan directamente con la base de datos.

Archivos:

- `usuario_repository.py`: implementa las consultas y operaciones CRUD de usuarios.
- `jornada_repository.py`: implementa las consultas y operaciones CRUD de jornadas.

#### 4.4. Routes

Contiene las rutas o endpoints que permiten acceder a las funcionalidades de la API.

Archivos:

- `usuarios.py`: define los endpoints relacionados con los usuarios.
- `jornadas.py`: define los endpoints relacionados con las jornadas.

#### 4.5. Schemas

Contiene los esquemas de Pydantic encargados de validar los datos que recibe y devuelve la API.

Archivos:

- `usuario_schema.py`: define las estructuras de entrada y salida para los usuarios.
- `jornada_schema.py`: define las estructuras de entrada y salida para las jornadas.

#### 4.6. Services

Contiene la lógica del negocio y coordina las operaciones entre Routes y Repositories.

Archivos:

- `usuario_service.py`: gestiona las reglas y operaciones relacionadas con los usuarios.
- `jornada_service.py`: gestiona las reglas y operaciones relacionadas con las jornadas.

#### 4.7. Main.py

Es el punto de entrada de la aplicación.

Se encarga de crear la instancia de FastAPI, registrar las rutas y configurar el inicio de la aplicación.

---

## 5. Funcionamiento de la arquitectura por capas

Las capas trabajan de manera coordinada para procesar las solicitudes que recibe la API.

El flujo principal de comunicación es:

```text
Cliente / Swagger
       |
       v
     Routes
       |
       v
    Services
       |
       v
  Repositories
       |
       v
 Models / Database
       |
       v
 PostgreSQL - Neon
```

### Ejemplo: registro de un usuario

1. El cliente envía una solicitud POST con los datos del usuario.
2. Routes recibe la solicitud y valida su estructura mediante Schemas.
3. Services procesa la información y aplica las reglas del negocio.
4. Repositories ejecuta la operación de inserción.
5. SQLAlchemy interactúa con PostgreSQL alojado en Neon.
6. La API devuelve una respuesta al cliente.

Cada capa tiene una responsabilidad independiente, evitando concentrar toda la funcionalidad en un único archivo.

---

## 6. Base de datos

El proyecto utiliza PostgreSQL como sistema de gestión de bases de datos y Neon como proveedor de alojamiento en la nube.

La base de datos contiene dos tablas principales:

### 6.1. Tabla usuarios

Almacena la información de los usuarios registrados en el sistema.

| Campo | Descripción |
|---|---|
| `id` | Identificador único del usuario. |
| `nombre` | Nombre del usuario. |
| `correo` | Correo electrónico del usuario. Debe ser único. |
| `contrasena_hash` | Contraseña almacenada mediante un hash seguro. |

### 6.2. Tabla jornadas

Almacena la información de las jornadas de donación de sangre.

| Campo | Descripción |
|---|---|
| `id` | Identificador único de la jornada. |
| `nombre` | Nombre de la jornada de donación. |
| `lugar` | Ubicación donde se realizará la jornada. |
| `fecha` | Fecha programada para la jornada. |
| `hora` | Hora de realización. |
| `capacidad_maxima` | Número máximo de participantes permitidos. |
| `entidad_organizadora` | Entidad responsable de organizar la jornada. |

### 6.3. Relaciones entre tablas

Las tablas `usuarios` y `jornadas` son independientes.

No existe una clave foránea entre ellas, debido a que los requisitos del proyecto no contemplan una relación directa entre los usuarios registrados y las jornadas.

---

## 7. Operaciones CRUD implementadas

La API cuenta con dos módulos principales.

### 7.1. CRUD de usuarios

Permite administrar los registros de usuarios.

| Operación | Método HTTP | Funcionalidad |
|---|---|---|
| Crear | POST | Registrar un usuario. |
| Consultar todos | GET | Obtener la lista de usuarios. |
| Consultar por ID | GET | Buscar un usuario específico. |
| Actualizar | PUT | Modificar la información de un usuario. |
| Eliminar | DELETE | Eliminar un usuario. |

### 7.2. CRUD de jornadas

Permite administrar las jornadas de donación de sangre.

| Operación | Método HTTP | Funcionalidad |
|---|---|---|
| Crear | POST | Registrar una jornada. |
| Consultar todas | GET | Obtener todas las jornadas. |
| Consultar por ID | GET | Buscar una jornada específica. |
| Filtrar por lugar | GET | Consultar jornadas según su ubicación. |
| Actualizar | PUT | Modificar la información de una jornada. |
| Eliminar | DELETE | Eliminar una jornada. |

### 7.3. Validaciones implementadas

La API incorpora validaciones para garantizar que la información ingresada sea correcta.

Entre ellas:

- Validación de los datos recibidos mediante Pydantic.
- Validación del formato del correo electrónico.
- Prevención de registros con correos duplicados.
- Protección de contraseñas mediante hash.
- Validación de identificadores existentes.
- Validación de campos y restricciones de las jornadas.
- Control de errores mediante códigos de estado HTTP.

Algunos códigos de respuesta utilizados:

| Código | Significado |
|---|---|
| 200 | Solicitud procesada correctamente. |
| 201 | Registro creado correctamente. |
| 204 | Operación realizada sin contenido de respuesta, si aplica. |
| 404 | Recurso no encontrado. |
| 409 | Conflicto, por ejemplo, un correo duplicado. |
| 422 | Error de validación de los datos enviados. |

---

## 8. Instalación y configuración del proyecto

Para ejecutar el proyecto localmente se necesitan:

- Python instalado.
- Git instalado.
- Una base de datos PostgreSQL en Neon.
- Un editor de código, como Visual Studio Code.

### 8.1. Clonar el repositorio

Abrir una terminal y ejecutar:

```bash
git clone https://github.com/ximenact/JORNADAS_DONACION_API.git
```

Ingresar a la carpeta:

```bash
cd JORNADAS_DONACION_API
```

### 8.2. Crear un entorno virtual

```bash
python -m venv .venv
```

Activar el entorno virtual en Windows:

```bash
.venv\Scripts\activate
```

### 8.3. Instalar las dependencias

```bash
pip install -r requirements.txt
```

### 8.4. Configurar las variables de entorno

Crear un archivo llamado `.env` en la raíz del proyecto.

Agregar la siguiente variable:

```env
DATABASE_URL=postgresql+psycopg://USUARIO:CONTRASEÑA@HOST/BASE_DE_DATOS?sslmode=require
```

Se debe reemplazar el contenido de ejemplo por la cadena de conexión real proporcionada por Neon.

**Importante:** el archivo `.env` contiene credenciales privadas y no debe subirse al repositorio de GitHub.

### 8.5. Ejecutar la aplicación

Desde la raíz del proyecto ejecutar:

```bash
uvicorn main:app --reload
```

Si la aplicación inicia correctamente, estará disponible en:

```text
http://127.0.0.1:8000
```

---

## 9. Documentación y pruebas con Swagger

FastAPI genera automáticamente documentación interactiva mediante Swagger UI.

Para acceder a la documentación local:

```text
http://127.0.0.1:8000/docs
```

Desde esta interfaz es posible:

- Visualizar los endpoints disponibles.
- Consultar los métodos HTTP.
- Enviar solicitudes a la API.
- Registrar usuarios.
- Consultar usuarios y jornadas.
- Actualizar registros.
- Eliminar registros.
- Comprobar las respuestas y los códigos de estado HTTP.

También se puede acceder a la documentación mediante la URL pública de Render, agregando `/docs`.

---

## 10. Conexión con Neon

La aplicación utiliza SQLAlchemy para comunicarse con PostgreSQL.

La configuración se encuentra en:

```text
app/database/conexion.py
```

Este archivo utiliza la variable de entorno `DATABASE_URL` para establecer la conexión con la base de datos.

La conexión permite que los Repositories ejecuten las operaciones necesarias para consultar, registrar, modificar y eliminar información.

Neon proporciona el servicio de PostgreSQL en la nube, permitiendo que los datos permanezcan disponibles incluso cuando la aplicación se ejecuta desde otro entorno.

---

## 11. Despliegue en Render

El proyecto está preparado para desplegarse en Render.

### Configuración utilizada

| Configuración | Valor |
|---|---|
| Plataforma | Render |
| Lenguaje | Python |
| Rama | main |
| Build Command | `pip install -r requirements.txt` |
| Start Command | `uvicorn main:app --host 0.0.0.0 --port $PORT` |

### Variables de entorno

En la configuración del servicio de Render se debe registrar:

```text
DATABASE_URL
```

El valor corresponde a la cadena de conexión de PostgreSQL proporcionada por Neon.

### Acceso a la API desplegada

Una vez que el servicio se encuentre activo, se puede acceder a la API mediante la URL pública proporcionada por Render.

La documentación interactiva se encuentra en:

```text
https://TU-URL-DE-RENDER/docs
```

---

## 12. Control de versiones con Git y GitHub

El proyecto utiliza Git para controlar los cambios realizados durante el desarrollo y GitHub para almacenar el repositorio de manera remota.

Repositorio:

**https://github.com/ximenact/JORNADAS_DONACION_API**

Comandos principales utilizados:

```bash
git status
```

Consultar el estado de los archivos.

```bash
git add .
```

Preparar los cambios para realizar un commit.

```bash
git commit -m "Descripción del cambio"
```

Guardar los cambios en el historial del proyecto.

```bash
git push origin main
```

Enviar los cambios al repositorio remoto.

```bash
git pull origin main
```

Obtener los cambios disponibles en el repositorio remoto.

---

## 13. Seguridad y buenas prácticas

Durante el desarrollo se aplicaron algunas medidas para proteger la información y mejorar la organización del código:

- Almacenamiento de contraseñas mediante hash, evitando guardar contraseñas en texto plano.
- Uso de variables de entorno para las credenciales de conexión.
- Exclusión del archivo `.env` mediante `.gitignore`.
- Validación de datos con Pydantic.
- Control de errores mediante excepciones HTTP.
- Separación de responsabilidades mediante arquitectura por capas.
- Uso de una base de datos PostgreSQL para almacenar la información.

---

## 14. Evidencias del proyecto

Para documentar el funcionamiento de la API se pueden incluir las siguientes evidencias:

1. **Arquitectura por capas:** imagen del diagrama de comunicación entre Routes, Services, Repositories y Database.
2. **Diagrama de base de datos:** imagen del diagrama ERD generado desde DBeaver.
3. **Pruebas de usuarios:** capturas de las operaciones POST, GET, PUT y DELETE en Swagger.
4. **Pruebas de jornadas:** capturas de las operaciones CRUD y del filtro por lugar.
5. **Conexión con Neon:** evidencia de la base de datos y sus tablas.
6. **Repositorio GitHub:** captura del repositorio y su estructura.
7. **Despliegue en Render:** captura del servicio activo y de la API funcionando mediante Swagger.

---

## 15. Conclusión

El desarrollo de JORNADA_API permitió aplicar conocimientos sobre construcción de APIs REST, programación con Python, manejo de bases de datos relacionales y organización de proyectos mediante arquitectura por capas.

La implementación de FastAPI permitió desarrollar endpoints para administrar usuarios y jornadas de donación de sangre, mientras que SQLAlchemy facilitó la interacción con PostgreSQL alojado en Neon.

Finalmente, el uso de GitHub permitió gestionar las versiones del proyecto y Render facilitó su despliegue para que la API pueda ser consultada desde internet.

---

## 16. Información del proyecto

| Elemento | Información |
|---|---|
| Nombre | JORNADA_API |
| Tipo de proyecto | API REST |
| Lenguaje | Python |
| Framework | FastAPI |
| Base de datos | PostgreSQL |
| Alojamiento de base de datos | Neon |
| Despliegue | Render |
| Repositorio | [GitHub - JORNADAS_DONACION_API](https://github.com/ximenact/JORNADAS_DONACION_API) |

Proyecto académico desarrollado como ejercicio de implementación de una API REST con arquitectura por capas.
