CREATE TABLE "postes" (
	"idPoste"	INTEGER NOT NULL,
	"nomPoste"	VARCHAR(50) NOT NULL,
	"département" INTEGER NOT NULL REFERENCES départements(idDépartement),
	PRIMARY KEY("idPoste")
);