Sistema de Gestión de Equipo de Carreras
Este es un sistema de gestión para un equipo de carreras que permite registrar empleados, autos, equipos y simular carreras.

Descripción
El sistema consta de las siguientes clases:

Empleado: Clase base que almacena información básica del empleado.
Piloto: Subclase de Empleado que representa a un piloto, incluyendo detalles como puntaje, número de auto, etc.
Mecanico: Subclase de Empleado para representar mecánicos con un puntaje asociado.
DirectorEquipo: Subclase de Empleado para los directores de equipo.
Además, hay una clase Auto que almacena información sobre el modelo, año y puntaje de un auto.

La clase Gestor es el punto de entrada del programa y contiene métodos para alta de empleados, autos y equipos, así como para simular carreras y realizar consultas.

Uso
Alta de empleado: Permite ingresar los datos de un empleado y asignarlo a su respectivo rol (piloto, mecánico o director de equipo).
Alta de auto: Permite registrar información sobre un nuevo auto.
Alta de equipo: Permite crear un equipo seleccionando un auto disponible y empleados existentes.
Simular carrera: Simula una carrera permitiendo ingresar datos sobre los eventos durante la misma, como pilotos lesionados, abandonos, errores en pits y penalidades.
Realizar consulta: Ofrece distintos tipos de consultas como el top 10 de pilotos con más puntos en el campeonato, resumen del campeonato de constructores, top 5 de pilotos mejores pagados, top 3 de pilotos más habilidosos y la lista de jefes de equipo.
Ejecución

Para ejecutar el programa, ejecuta el archivo entregable.py. Se presentará un menú con las opciones mencionadas anteriormente.










