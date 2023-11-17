
```sql
CREATE TABLE Artist (
	"id" INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
	"name" TEXT
);

CREATE TABLE Genre (
	id		INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
	name 	TEXT
);

CREATE TABLE Album (
	id		INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
	artist_id INTEGER,
	title 	TEXT
);

CREATE TABLE Track (
	id		INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
	title 	TEXT,
	album_id INTEGER,
	gener_id INTEGER,
	len INTEGER,
	rating INTEGER,
	count INTEGER
);

INSERT INTO Artist (name) VALUES ("Hans");
INSERT INTO Artist (name) VALUES ("Homeyra");

INSERT INTO Genre (name) VALUES ("Rock");
INSERT INTO Genre (name) VALUES ("Metal");

INSERT INTO Album (title, artist_id) VALUES ("Who made it", 1);
INSERT INTO Album (title, artist_id) VALUES ("VI", 1)

INSERT INTO Track (title, rating, len, count, album_id, gener_id) VALUES ("Black Dog", 5, 279, 0, 2, 1 );
INSERT INTO Track (title, rating, len, count, album_id, gener_id) VALUES ("Stairway", 5, 482, 0, 2, 1 );
INSERT INTO Track (title, rating, len, count, album_id, gener_id) VALUES ("About to rock", 5, 313, 0, 2, 1 );
INSERT INTO Track (title, rating, len, count, album_id, gener_id) VALUES ("Who made who", 5, 207, 0, 2, 1 )

SELECT Album.title, Artist.name FROM Album JOIN Artist WHERE Album.artist_id = Artist.id

SELECT Track.title, Genre.name FROM Track JOIN Genre on Track.gener_id = Genre.id
```

# Many to Many

```sql
CREATE TABLE User (
	id		INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
	name	TEXT,
	email	TEXT
);

CREATE TABLE Course (
	id		INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
	title	TEXT
);

CREATE TABLE Member (
	user_id		INTEGER,
	course_id	INTEGER,
	role		INTEGER,
	PRIMARY KEY (user_id, course_id)
);
```

```sql
INSERT INTO User (name, email) VALUES ("jane", "jane@tsugi.org");
INSERT INTO User (name, email) VALUES ("Ed", "ed@tsugi.org");
INSERT INTO User (name, email) VALUES ("Sue", "sue@tsugi.org");

INSERT INTO Course (title) VALUES ("Python");
INSERT INTO Course (title) VALUES ("SQL");
INSERT INTO Course (title) VALUES ("PHP");

INSERT INTO Member (user_id, course_id, role) VALUES (1, 1, 1);
INSERT INTO Member (user_id, course_id, role) VALUES (2, 1, 0);
INSERT INTO Member (user_id, course_id, role) VALUES (3, 1, 0);

INSERT INTO Member (user_id, course_id, role) VALUES (1, 2, 0);
INSERT INTO Member (user_id, course_id, role) VALUES (2, 2, 1);

INSERT INTO Member (user_id, course_id, role) VALUES (2, 3, 1);
INSERT INTO Member (user_id, course_id, role) VALUES (3, 3, 0);

SELECT User.name, Member.role, Course.title 
FROM User JOIN Member JOIN Course
ON Member.user_id = User.id AND Member.course_id = Course.id
ORDER BY Course.title, Member.role DESC, User.name
```


