CREATE TABLE "clients" (
	"idClient"	INTEGER NOT NULL,
	"prénom"	VARCHAR(50) NOT NULL,
	"nom"	VARCHAR(50) NOT NULL,
	"mot de passe"	VARCHAR(50) NOT NULL,
	"email"	VARCHAR(50) NOT NULL,
	"téléphone"	INTEGER NOT NULL,
	PRIMARY KEY("idClient")
);