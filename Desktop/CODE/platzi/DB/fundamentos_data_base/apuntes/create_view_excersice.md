Ejercicio:

Debes imprimir los siguientes 4 bloques de información:

La tabla people ya tiene información cargada. No debes agregar nueva información, solo imprimirla.

1.- Crear una vista en SQL basado en la tabla de people con los campos person_id, last_name, first_name:

Crea una vista llamada v_madrid_customers que muestre únicamente el person_id, last_name, y first_name de todas las personas que vivan en la ciudad de "Madrid".

Para crear esta vista, puedes seguir los siguientes pasos:

CREATE VIEW vista_personas AS
SELECT person_id
FROM personas

2.- Este comando creará una vista llamada vista_personas que selecciona solamente el person_id tabla personas.

Una vez que hayas creado la vista, puedes utilizar el siguiente comando para seleccionar los datos de la vista:

SELECT * FROM vista_personas;

Aquí te propongo 2 retos adicionales, vamos a poner a prueba nuestra habilidad en la manipulación de tablas en SQL.

3.- El reto es agregar un nuevo campo llamado date_of_birth con el tipo de campo DATE a la tabla people.

ALTER TABLE table_name
ADD COLUMN column_definition;

4.- El reto es eliminar el campo address de la tabla people.

ALTER TABLE table_name
DROP COLUMN ;


Solution:

CREATE VIEW v_madrid_customers AS
SELECT person_id, last_name, first_name
FROM people
WHERE city = "Madrid";

SELECT * FROM v_madrid_customers;

CREATE VIEW vistas_personas AS
SELECT person_id
FROM people;

ALTER TABLE people
ADD COLUMN date_of_birth DATE;

ALTER TABLE people
DROP COLUMN address;