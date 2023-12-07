create database rpg;
use rpg;
-- Tabela Usuário
CREATE TABLE Usuario (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(255) NOT NULL,
    senha VARCHAR(255) NOT NULL,
    email VARCHAR(255) NOT NULL,
    personagens INT DEFAULT 0
);

-- Tabela Personagens
CREATE TABLE Personagens (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nivel INT,
    forca INT,
    inteligencia INT,
    agilidade INT,
    vigor INT,
    inventario INT,
    apelido VARCHAR(255),
    classe VARCHAR(255),
    grupo INT,
    usuarioID INT NOT NULL,
    FOREIGN KEY (usuarioID) REFERENCES  Usuario(id)
);

-- Tabela Inventario
CREATE TABLE Inventario (
    id INT AUTO_INCREMENT PRIMARY KEY,
    itens VARCHAR(255),
    quantidade INT,
    tamanho_maximo INT,
    ouro INT,
    personagemID INT NOT NULL,
    FOREIGN KEY (personagemID) REFERENCES  Personagens(id)  
);

-- Tabela Item
CREATE TABLE Item (
    id INT AUTO_INCREMENT PRIMARY KEY,
    tipo VARCHAR(255),
    peso INT,
    dano INT,
    valor INT,
    descricao TEXT,
    inventarioID int not null,
    FOREIGN KEY (inventarioID) REFERENCES Inventario(id)
);

-- Tabela Grupos
CREATE TABLE Grupos (
    id INT AUTO_INCREMENT PRIMARY KEY,
    tamanho INT,
    nome varchar(20)
);

-- join table 

CREATE TABLE GruposPersonagem(
	id INT AUTO_INCREMENT PRIMARY KEY,
    grupoID INT NOT null,
    itenID INT NOT null,
    FOREIGN KEY (grupoID) REFERENCES Grupos(id),
    FOREIGN KEY (itenID) REFERENCES Item(id)
);
