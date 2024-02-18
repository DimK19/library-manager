BEGIN TRANSACTION;
CREATE TABLE IF NOT EXISTS "author" (
	"id"	INTEGER,
	"first_name"	TEXT,
	"last_name"	TEXT NOT NULL,
	PRIMARY KEY("id")
);
CREATE TABLE IF NOT EXISTS "location" (
	"id"	INTEGER,
	"place"	TEXT NOT NULL,
	PRIMARY KEY("id")
);
CREATE TABLE IF NOT EXISTS "publisher" (
	"id"	INTEGER,
	"name"	TEXT NOT NULL,
	PRIMARY KEY("id")
);
CREATE TABLE IF NOT EXISTS "collection_type" (
	"id"	INTEGER,
	"category"	TEXT,
	PRIMARY KEY("id")
);
CREATE TABLE IF NOT EXISTS "book_author" (
	"author_id"	INTEGER,
	"book_id"	INTEGER,
	FOREIGN KEY("author_id") REFERENCES "author"("id"),
	FOREIGN KEY("book_id") REFERENCES "book"("id") ON DELETE CASCADE
);
CREATE TABLE IF NOT EXISTS "collection" (
	"id"	INTEGER,
	"title"	TEXT NOT NULL,
	"collection_type_id"	INTEGER,
	FOREIGN KEY("collection_type_id") REFERENCES "collection_type"("id"),
	PRIMARY KEY("id")
);
CREATE TABLE IF NOT EXISTS "book" (
	"id"	INTEGER,
	"title"	TEXT NOT NULL,
	"volume"	INTEGER,
	"publisher_id"	INTEGER,
	"location_id"	INTEGER,
	"collection_id"	INTEGER DEFAULT NULL,
	"edition"	INTEGER DEFAULT NULL,
	FOREIGN KEY("publisher_id") REFERENCES "publisher"("id"),
	FOREIGN KEY("location_id") REFERENCES "location"("id"),
	FOREIGN KEY("collection_id") REFERENCES "collection"("id"),
	PRIMARY KEY("id")
);
COMMIT;
