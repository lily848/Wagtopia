import sqlite3
connection = sqlite3.connect("wagtopia.db")
cur=connection.cursor()

#parents
cur.execute(
    "INSERT INTO parents (parent_name, phone) VALUES ('Helen Dame', '(951)234-5354')"
);
cur.execute(
    "INSERT INTO parents (parent_name, phone) VALUES ('Sharon Lee', '(951)234-5353')"
);
cur.execute(
    "INSERT INTO parents (parent_name, phone) VALUES ('Shelly He', '(951)234-5352')"
);

#dogs
cur.execute(
    "INSERT INTO dogs (dog_name, breed, parent_id) VALUES ('Eeny', 'Golden Retriever', 1)"
);
cur.execute(
    "INSERT INTO dogs (dog_name, breed, parent_id) VALUES ('Meeny', 'Poodle', 1)"
);
cur.execute(
    "INSERT INTO dogs (dog_name, breed, parent_id) VALUES ('Miny', 'Poodle', 1)"
);
cur.execute(
    "INSERT INTO dogs (dog_name, breed, parent_id) VALUES ('Moe', 'Chihuahua', 2)"
);
cur.execute(
    "INSERT INTO dogs (dog_name, breed, parent_id) VALUES ('Sky', 'Poodle', 2)"
);
cur.execute(
    "INSERT INTO dogs (dog_name, breed, parent_id) VALUES ('Daisy', 'Chihuahua', 3)"
);

#groomers
cur.execute(
    "INSERT INTO groomers (groomer_name) VALUES ('Walter White')"
);
cur.execute(
    "INSERT INTO groomers (groomer_name) VALUES ('Rarity Shine')"
);
cur.execute(
    "INSERT INTO groomers (groomer_name) VALUES ('Daniel Evens')"
);

#services
cur.execute(
    "INSERT INTO services (service_name, duration_minutes) VALUES ('Wash', 60)"
);
cur.execute(
    "INSERT INTO services (service_name, duration_minutes) VALUES ('Dry', 60)"
);

#Bookings
cur.execute(
    """
    INSERT INTO bookings (parent_id, dog_id, groomer_id, service_id, start_time, end_time, appointment_date) 
    VALUES (1, 2, 1, 1, '2:00', '3:00' , '2026-03-31')
    """
);
cur.execute(
    """
    INSERT INTO bookings (parent_id, dog_id, groomer_id, service_id, start_time, end_time, appointment_date) 
    VALUES (2, 4, 2, 1, '4:00', '5:00' , '2026-03-31')
    """
);
cur.execute(
    """
    INSERT INTO bookings (parent_id, dog_id, groomer_id, service_id, start_time, end_time, appointment_date) 
    VALUES (3, 6, 3, 1, '6:00', '7:00' , '2026-03-30')
    """
);

connection.commit()
connection.close()
print("database seeded")