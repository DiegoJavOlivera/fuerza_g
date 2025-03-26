# Fuerza G

Fuerza G es una aplicación web desarrollada en **Flask** que permite a los estudiantes de la facultad acceder a modelos de parciales y mantenerse informados con noticias actualizadas. Su objetivo es facilitar el estudio y la organización académica proporcionando un espacio centralizado donde los alumnos puedan encontrar material de referencia y novedades relevantes

## Tecnologías utilizadas

- **Flask**: Framework web ligero y flexible.
- **MySQL**: Base de datos relacional para almacenar datos.
- **phpMyAdmin**: Herramienta de administración de bases de datos MySQL.
- **Flask-Login**: Para manejar la autenticación de usuarios.
- **Bootstrap**: Framework CSS para la interfaz de usuario responsiva.
- **Python-dotenv**: Para gestionar las variables de entorno.

## Requisitos previos

Antes de comenzar, asegúrate de tener instalados los siguientes programas en tu máquina:

- **Python 3.x**: La aplicación está desarrollada en Python.
- **MySQL**: Para la base de datos, debes tener MySQL o MariaDB instalados.
- **phpMyAdmin**: Necesitarás phpMyAdmin para gestionar la base de datos a través de una interfaz web.
- **pip**: El gestor de paquetes de Python para instalar dependencias.

### Instalación de MySQL y phpMyAdmin

1. **Instalar MySQL**:
   Si aún no tienes MySQL, instala MySQL en tu máquina:

   - En **Ubuntu**:
     ```bash
     sudo apt update
     sudo apt install mysql-server
     sudo mysql_secure_installation
     ```

   - En **Windows**: Puedes descargar MySQL desde [aquí](https://dev.mysql.com/downloads/installer/).

2. **Instalar phpMyAdmin**:
   phpMyAdmin te permitirá gestionar tu base de datos de manera más sencilla desde una interfaz web.

   - En **Ubuntu**:
     ```bash
     sudo apt update
     sudo apt install phpmyadmin
     sudo service apache2 restart
     ```

   - En **Windows**: Descarga e instala phpMyAdmin desde [aquí](https://www.phpmyadmin.net/downloads/).

   Después de instalar phpMyAdmin, accede a él desde tu navegador en la URL `http://localhost/phpmyadmin`.

3. **Crear la base de datos en phpMyAdmin**:
   Una vez que phpMyAdmin esté configurado, sigue estos pasos:
   
   - Accede a phpMyAdmin.
   - Crea una nueva base de datos con el nombre que desees, por ejemplo: `fuerzag_db`.
   - Importa el archivo **schema.sql** (si tienes uno) para crear las tablas necesarias en la base de datos. Puedes hacerlo desde la opción de **Importar** en phpMyAdmin.

## Instalación

4. Clona este repositorio en tu máquina:

   ```bash
   git clone https://github.com/DiegoJavOlivera/fuerzag.git
   cd fuerzag


5. Crea un entorno virtual (opcional, pero recomendado):
    python -m venv venv
    source venv/bin/activate  # En Linux/macOS
    venv\Scripts\activate     # En Windows

6. Instala las dependencias necesarias:
      pip install -r requirements.txt

## Configuración para enviar correos con Google y verificación en dos pasos

Si deseas usar tu cuenta de Google para enviar correos electrónicos desde tu aplicación Flask, necesitas generar una **clave de aplicación**. Para ello, debes habilitar la **verificación en dos pasos** en tu cuenta de Google y luego crear una **clave para aplicaciones**. Sigue estos pasos:

### Pasos para habilitar la verificación en dos pasos y obtener la clave para aplicaciones

7. **Habilitar la verificación en dos pasos en tu cuenta de Google**:
   - Ve a [tu cuenta de Google](https://myaccount.google.com/).
   - En el menú de la izquierda, selecciona **Seguridad**.
   - En la sección **Acceso a Google**, haz clic en **Verificación en dos pasos** y sigue los pasos para activarlo. Esto añade una capa extra de seguridad a tu cuenta.

8. **Generar una clave para aplicaciones**:
   - Una vez que hayas habilitado la verificación en dos pasos, ve a [Claves de aplicaciones](https://myaccount.google.com/apppasswords).
   - En la página de **Claves de aplicación**, selecciona el tipo de aplicación (por ejemplo, "Correo") y el dispositivo (por ejemplo, "Otro").
   - Haz clic en **Generar** para obtener tu **clave para aplicaciones**.

9. **Guardar la clave generada**:
   - Una vez generada la clave, cópiala. Esta clave es lo que usarás en tu aplicación para autenticar el envío de correos electrónicos a través de la cuenta de Google.
   
10. **Configurar Flask para enviar correos**:
   - Instala el paquete `Flask-Mail` para enviar correos electrónicos con Flask:
   
     ```bash
     pip install Flask-Mail
     ```

   - Luego, configura el archivo `.env` de tu aplicación Flask con la clave de aplicación generada:

     ```env
     MAIL_USERNAME=tu_email@gmail.com
     MAIL_PASSWORD=la_clave_de_aplicacion_generada
     ```

11. **Configurar `Flask-Mail` en tu aplicación**:
     # Configuración de correo
      
      config['MAIL_SERVER'] = 'smtp.gmail.com'
      config['MAIL_PORT'] = 587
      config['MAIL_USE_TLS'] = True
      config['MAIL_USERNAME'] = 'tu_email@gmail.com'
      config['MAIL_PASSWORD'] = 'la_clave_de_aplicacion_generada'
  




     Contactos
     Diego Javier Olivera | LinkedIn 

