USE Backoffice;

CREATE TABLE Livros (
    id integer not null auto_increment,
    autor varchar(100),
    titulo varchar(100),
    PRIMARY KEY (id)
);

SET character_set_client = utf8;
SET character_set_connection = utf8;
SET character_set_results = utf8;
SET collation_connection = utf8_general_ci;

INSERT INTO Livros (autor, titulo) VALUES('J.R.R Jolkien', 'O Senhor dos Anéis - A Sociedade do Anel');
INSERT INTO Livros (autor, titulo) VALUES('J.K Howling', 'Harry Potter e a Pedra Filosofal');
INSERT INTO Livros (autor, titulo) VALUES('L. Frank Baum', 'O Mágico de Oz');

CREATE TABLE Usuarios (
    id integer not null auto_increment,
    email varchar(100),
    senha varchar(100),
    PRIMARY KEY (id)
);

SET character_set_client = utf8;
SET character_set_connection = utf8;
SET character_set_results = utf8;
SET collation_connection = utf8_general_ci;

INSERT INTO Usuario (email, senha) VALUES('cesar teste', 'teste123');
INSERT INTO Usuario (email, senha) VALUES('mylycy teste', '123teste');
