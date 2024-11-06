**Proyecto MiniCore con Flask(Backend) y Vue(Frontend)**

Inventario de Mecánica - CRUD MVC con Python, Flask y Vue.js

Este proyecto tiene como propósito crear un sistema de inventario para una mecánica. Permite la gestión de propietarios y 
vehículos asociados mediante un sistema CRUD (Crear, Leer, Actualizar, Eliminar) implementado con la arquitectura MVC (Modelo-Vista-Controlador).

La API backend se construyó usando Python y Flask, conectada a una base de datos MySQL, mientras que la interfaz de usuario (frontend) 
se implementa en Vue.js para proporcionar una experiencia de usuario interactiva y dinámica.

**Estructura del Proyecto**
El proyecto está dividido en varias carpetas:
-controllers: Aquí se encuentran los controladores de Flask que manejan las rutas y la lógica de negocio. 
  Los controladores disponibles incluyen:
    *propietarios_controller.py: Controlador para gestionar los propietarios.
    *vehiculos_controller.py: Controlador para gestionar los vehículos.
-models: Esta carpeta contiene los modelos que interactúan directamente con la base de datos MySQL.
    *propietarios.py: Modelo que define la estructura y métodos de consulta para los propietarios.
    *vehiculos.py: Modelo que define la estructura y métodos de consulta para los vehículos.
Vistas (Frontend): El frontend se desarrolla con Vue.js y contiene las vistas necesarias para interactuar con el usuario, permitiendo operaciones 
  de registro, edición y eliminación de datos de propietarios y vehículos.

**Funcionalidades**
El sistema permite realizar las siguientes operaciones para propietarios y vehículos:
Listar: Muestra todos los registros actuales.
Agregar: Permite registrar nuevos propietarios y vehículos.
Editar: Modifica los datos de un propietario o vehículo existente.
Eliminar: Elimina un registro de propietario o vehículo de la base de datos.

**Instalación**
**Requisitos Previos**
  Python: Se recomienda Python 3.8 o superior.
  Node.js y npm: Necesario para ejecutar el frontend en Vue.js.
  MySQL: Para la base de datos donde se almacenarán los registros.
  Flask y Vue CLI: Instalaciones necesarias para el desarrollo en backend y frontend.

**Para VUEJS**
**Primero: Descargar npm:**
Comando que viene integrado en la descarga de nodejs: https://nodejs.org/en/download/package-manager/current
1) En una terminal mandamos el siguiente comando para verificar si la instalación está correcta node -v
2) Así aseguramos que instalar con npm nos servirá.

**Segundo: Instalar y Crear Proyecto Vue.js**
1) En otra terminal mandamos el siguiente comando: -> npm install -g @vue/cli
2) Para crear el proyecto en la carpeta donde se va a alojar ponemos: -> vue create project
3) Se generará una carpeta con toda la estructura del proyecto Vue.js.
