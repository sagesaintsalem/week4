DROP TABLE lightsabers;
DROP TABLE characters;


CREATE TABLE characters (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    darkside BOOLEAN,
    age INT
);

CREATE TABLE lightsabers (
    id SERIAL PRIMARY KEY,
    character_id INT REFERENCES characters(id),
    colour VARCHAR(255) NOT NULL,
    hilt_metal VARCHAR(255) NOT NULL


);

INSERT INTO characters (name, darkside, age)
VALUES ('Obi-Wan', false, 27);
INSERT INTO characters (name, darkside, age)
VALUES ('Anakin', false, 19);
INSERT INTO characters (name, darkside, age)
VALUES ('Darth Maul', true, 32);
INSERT INTO characters (name, darkside, age)
VALUES ('Yoda', false, null);



-- UPDATE characters SET darkside = true;
UPDATE characters SET (name, darkside) = ('Darth Vader', true) WHERE name = 'Anakin';
UPDATE characters SET age = 65 WHERE name = 'Obi-Wan';

INSERT INTO characters (name, darkside, age)
VALUES ('Luke', false, 17);

DELETE FROM characters WHERE name = 'Darth Maul';


INSERT INTO characters (name, darkside, age) VALUES ('Stormtrooper', true, 25);
INSERT INTO characters (name, darkside, age) VALUES ('Stormtrooper', true, 25);
INSERT INTO characters (name, darkside, age) VALUES ('Stormtrooper', true, 25);
INSERT INTO characters (name, darkside, age) VALUES ('Stormtrooper', true, 25);
INSERT INTO characters (name, darkside, age) VALUES ('Stormtrooper', true, 25);

UPDATE characters SET age = 29 WHERE id = 9;

SELECT * FROM characters;

INSERT INTO lightsabers (character_id, colour, hilt_metal)
VALUES (1, 'green', 'palladium'),
       (2, 'blue', 'palladium'),
       (4, 'red', 'gold'),
       (2, 'red', 'titanium');

SELECT * FROM lightsabers;

SELECT * FROM lightsabers WHERE character_id = 2;