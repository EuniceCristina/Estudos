DROP TABLE IF EXISTS users;
CREATE TABLE users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    matricula INT NOT NULL,
    email TEXT NOT NULL,
    senha TEXT NOT NULL
);

DROP TABLE IF EXISTS exercicios;
CREATE TABLE exercicios (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    usuario INT NOT NULL,
    nome TEXT NOT NULL,
    comentario TEXT NOT NULL
);