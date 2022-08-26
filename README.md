La pagina "personas" llama a la función "personas" del archivo AppFami.views. En esta pagina se pueden ingresar nuevas personas, ademas trae todas las personas existentes en la tabla de base de datos de PERSONA.

La pagina "hijos" llama a la función "hijos" del archivo AppFami.views. En esta pagina se pueden ingresar nuevas relaciones de una persona y su hijo, ademas trae todas las relaciones persona - hijos existentes en la tabla de base de datos de HIJO.

La pagina "padres" llama a la función "padres" del archivo AppFami.views. En esta pagina se pueden ingresar nuevas relaciones de una persona y cuales son sus padres, ademas trae todas las relaciones persona - padres existentes en la tabla de base de datos de PADRE.

La pagina "buscar" llama a la función "buscar_persona" del archivo AppFami.views. En esta pagina se puede fuscar los datos de una persona desde la base de datos tabla PADRE.


Modelo de BD

Tabla: Persona
Columnas: nombre,rutpersona,genero,fecnacimiento

Tabla: Padre
Columnas: rutpersona,rutpadre

Tabla: Hijo
Columnas: rutpersona,ruthijo