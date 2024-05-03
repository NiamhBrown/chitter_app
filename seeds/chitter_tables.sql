-- The job of this file is to reset all of our important database tables.
-- And add any data that is needed for the tests to run.
-- This is so that our tests, and application, are always operating from a fresh
-- database state, and that tests don't interfere with each other.

-- First, we must delete (drop) all our tables
DROP TABLE IF EXISTS users CASCADE;
DROP TABLE IF EXISTS peeps;
DROP SEQUENCE IF EXISTS users_id_seq;
DROP SEQUENCE IF EXISTS peeps_id_seq;

-- Then, we recreate them
CREATE SEQUENCE IF NOT EXISTS users_id_seq;
CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    name TEXT,
    email TEXT,
    password TEXT,
    username TEXT
);

-- time_posted TIMESTAMP DEFAULT CURRENT_TIMESTAMP
CREATE TABLE peeps (
    id SERIAL PRIMARY KEY,
    content TEXT,
    time_posted int,
    user_id int,
    constraint fk_user foreign key(user_id)
        references users(id)
        on delete cascade
);

-- Finally, we add any records that are needed for the tests to run

INSERT INTO users (name, email, username, password) VALUES ('Niamh', 'niamh@me.com', 'niamhb', 'niamh123!');
INSERT INTO users (name, email, username, password) VALUES ('Grace', 'grace@me.com', 'gracee', 'grace123!');

INSERT INTO peeps (content, time_posted, user_id) VALUES ('niamhs first peep', 11,1);
INSERT INTO peeps (content, time_posted, user_id) VALUES ('graces first peep', 12,2);

