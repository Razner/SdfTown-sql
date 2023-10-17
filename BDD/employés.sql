CREATE TABLE "employés" (
	"idEmployés"	INTEGER NOT NULL,
	"prénom"	VARCHAR(50) NOT NULL,
	"nom"	VARCHAR(50) NOT NULL,
	"adresse"	VARCHAR(50) NOT NULL,
	"mail"	VARCHAR(50) NOT NULL,
	"ville"	VARCHAR(50) NOT NULL,
	"poste"	INTEGER NOT NULL,
	FOREIGN KEY("poste") REFERENCES "postes"("idPoste"),
	PRIMARY KEY("idEmployés")
);