DROP TABLE IF EXISTS notes;

CREATE TABLE notes (
    id SERIAL PRIMARY KEY,
    title VARCHAR(255),
    content VARCHAR(255)
);


TRUNCATE TABLE NOTES;

ALTER SEQUENCE notes_id_seq RESTART with 1;

INSERT INTO notes(title, content) VALUES ('Michael Scott', 'Sometimes I’ll start a sentence and I don’t even know where it’s going. I just hope I find it along the way.');
INSERT INTO notes(title, content) VALUES ('Kelly Kapoor', 'I talk a lot, so I’ve learned to tune myself out.');
INSERT INTO notes(title, content) VALUES ('Stanley Hudson', 'If I don’t have some cake soon, I might die.');
INSERT INTO notes(title, content) VALUES ('Dwight Schrute', 'Identity theft is not a joke, Jim! Millions of families suffer every year.');
INSERT INTO notes(title, content) VALUES ('Kevin Malone', 'I just want to lie on the beach and eat hot dogs. That’s all I’ve ever wanted.');