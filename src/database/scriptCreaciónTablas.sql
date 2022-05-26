use acb;
drop table parrafo;
drop table plantilla;
CREATE TABLE plantilla(
	id int AUTO_INCREMENT,
    titulo varchar(100) NOT NULL,
    PRIMARY KEY(id)
);

CREATE TABLE parrafo(
	id int AUTO_INCREMENT,
    contenido varchar(10000) NOT NULL,
    id_plantilla int,
    tipo_parrafo varchar(50) NOT NULL UNIQUE,
    PRIMARY KEY(id, id_plantilla),
    CONSTRAINT FK_plantillaParrafo
		FOREIGN KEY (id_plantilla) REFERENCES plantilla(id)
);