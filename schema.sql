-- Enable foreign key enforcement (required in SQLite)
PRAGMA foreign_keys = ON;

-- Parents (dog owners / customers)
CREATE TABLE IF NOT EXISTS parents (
    parent_id   INTEGER PRIMARY KEY AUTOINCREMENT,
    parent_name TEXT    NOT NULL,
    phone       TEXT
);

-- Dogs
CREATE TABLE IF NOT EXISTS dogs (
    dog_id      INTEGER PRIMARY KEY AUTOINCREMENT,
    parent_id   INTEGER NOT NULL,
    dog_name    TEXT    NOT NULL,
    breed       TEXT,
    FOREIGN KEY (parent_id) REFERENCES parents(parent_id)
);

-- Groomers
CREATE TABLE IF NOT EXISTS groomers (
    groomer_id   INTEGER PRIMARY KEY AUTOINCREMENT,
    groomer_name TEXT NOT NULL
);

-- Services (wash, grooming, etc.)
CREATE TABLE IF NOT EXISTS services (
    service_id       INTEGER PRIMARY KEY AUTOINCREMENT,
    service_name     TEXT    NOT NULL,  -- e.g. 'wash', 'grooming'
    duration_minutes INTEGER NOT NULL
);

-- Bookings (links everything together)
CREATE TABLE IF NOT EXISTS bookings (
    booking_id  INTEGER PRIMARY KEY AUTOINCREMENT,
    parent_id   INTEGER NOT NULL,
    dog_id      INTEGER NOT NULL,
    groomer_id  INTEGER NOT NULL,
    service_id  INTEGER NOT NULL,
    start_time  TEXT    NOT NULL,  -- store as ISO 8601: '2026-04-01 10:00'
    end_time    TEXT    NOT NULL,
    created_at  TEXT    DEFAULT (datetime('now')),
    appointment_date TEXT NOT NULL,
    FOREIGN KEY (parent_id)  REFERENCES parents(parent_id),
    FOREIGN KEY (dog_id)     REFERENCES dogs(dog_id),
    FOREIGN KEY (groomer_id) REFERENCES groomers(groomer_id),
    FOREIGN KEY (service_id) REFERENCES services(service_id)
);