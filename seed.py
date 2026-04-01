import sqlite3
connection = sqlite3.connect("wagtopia.db")
cur=connection.cursor()

# parents
cur.execute(
    "INSERT INTO parents (parent_name, phone) VALUES ('Helen Dame', '(951)234-5354')"
);
cur.execute(
    "INSERT INTO parents (parent_name, phone) VALUES ('Sharon Lee', '(951)234-5353')"
);
cur.execute(
    "INSERT INTO parents (parent_name, phone) VALUES ('Shelly He', '(951)234-5352')"
);
cur.execute(
    "INSERT INTO parents (parent_name, phone) VALUES ('James Park', '(714)555-1011')"
)
cur.execute(
    "INSERT INTO parents (parent_name, phone) VALUES ('Maria Gomez', '(714)555-2022')"
)
cur.execute(
    "INSERT INTO parents (parent_name, phone) VALUES ('Kevin Nguyen', '(714)555-3033')"
)

# dogs
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
cur.execute(
    "INSERT INTO dogs (dog_name, breed, parent_id) VALUES ('Biscuit', 'Labrador', 4)"
)
cur.execute(
    "INSERT INTO dogs (dog_name, breed, parent_id) VALUES ('Shadow', 'German Shepherd', 4)"
)
cur.execute(
    "INSERT INTO dogs (dog_name, breed, parent_id) VALUES ('Coco', 'Shih Tzu', 5)"
)
cur.execute(
    "INSERT INTO dogs (dog_name, breed, parent_id) VALUES ('Pepper', 'Dachshund', 5)"
)
cur.execute(
    "INSERT INTO dogs (dog_name, breed, parent_id) VALUES ('Noodle', 'Poodle', 6)"
)
cur.execute(
    "INSERT INTO dogs (dog_name, breed, parent_id) VALUES ('Tank', 'Bulldog', 6)"
)
cur.execute(
    "INSERT INTO dogs (dog_name, breed, parent_id) VALUES ('Maple', 'Golden Retriever', 6)"
)

# groomers
cur.execute(
    "INSERT INTO groomers (groomer_name) VALUES ('Walter White')"
);
cur.execute(
    "INSERT INTO groomers (groomer_name) VALUES ('Rarity Shine')"
);
cur.execute(
    "INSERT INTO groomers (groomer_name) VALUES ('Daniel Evens')"
);

# services
cur.execute(
    "INSERT INTO services (service_name, duration_minutes) VALUES ('Wash', 60)"
);
cur.execute(
    "INSERT INTO services (service_name, duration_minutes) VALUES ('Grooming', 60)"
);

# Bookings
cur.execute(
    """
    INSERT INTO bookings (parent_id, dog_id, groomer_id, service_id, start_time, end_time, appointment_date) 
    VALUES (1, 2, 1, 1, '15:00', '16:00' , '2026-03-31')
    """
);
cur.execute(
    """
    INSERT INTO bookings (parent_id, dog_id, groomer_id, service_id, start_time, end_time, appointment_date) 
    VALUES (2, 4, 2, 1, '09:00', '10:00' , '2026-03-31')
    """
);
cur.execute(
    """
    INSERT INTO bookings (parent_id, dog_id, groomer_id, service_id, start_time, end_time, appointment_date) 
    VALUES (3, 6, 3, 1, '12:00', '13:00' , '2026-03-30')
    """
);
cur.execute(
    """
    INSERT INTO bookings (parent_id, dog_id, groomer_id, service_id, start_time, end_time, appointment_date)
    VALUES (4, 7, 1, 2, '10:00', '11:00', '2026-04-02')
    """
);
cur.execute(
    """
    INSERT INTO bookings (parent_id, dog_id, groomer_id, service_id, start_time, end_time, appointment_date)
    VALUES (4, 8, 2, 1, '13:00', '14:00', '2026-04-02')
    """
);
cur.execute(
    """
    INSERT INTO bookings (parent_id, dog_id, groomer_id, service_id, start_time, end_time, appointment_date)
    VALUES (5, 9, 3, 2, '09:00', '10:00', '2026-04-03')
    """
);
cur.execute(
    """
    INSERT INTO bookings (parent_id, dog_id, groomer_id, service_id, start_time, end_time, appointment_date)
    VALUES (5, 10, 1, 1, '11:00', '12:00', '2026-04-03')
    """
);
cur.execute(
    """
    INSERT INTO bookings (parent_id, dog_id, groomer_id, service_id, start_time, end_time, appointment_date)
    VALUES (6, 11, 2, 2, '14:00', '15:00', '2026-04-04')
    """
);
cur.execute(
    """
    INSERT INTO bookings (parent_id, dog_id, groomer_id, service_id, start_time, end_time, appointment_date)
    VALUES (6, 13, 3, 1, '10:00', '11:00', '2026-04-05')
    """
);

connection.commit()
connection.close()
print("database seeded")