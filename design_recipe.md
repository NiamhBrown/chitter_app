# Two Tables Design Recipe Template

## 1. Extract nouns from the user stories or specification

```
As a Maker
So that I can let people know what I am doing
I want to post a message (peep) to chitter

As a maker
So that I can see what others are saying
I want to see all peeps in reverse chronological order

As a Maker
So that I can better appreciate the context of a peep
I want to see the time at which it was made

As a Maker
So that I can post messages on Chitter as me
I want to sign up for Chitter
```

```
Nouns:

peep, time_posted, user,email, password, name, username 
```

## 2. Infer the Table Name and Columns

Put the different nouns in this table. Replace the example with your own nouns.

| Record                | Properties          |
| --------------------- | ------------------  |
| peep                  | user_id, content, time_posted
| user                  | email, password, name, username 

1. Name of the first table (always plural): `peeps` 

    Column names: `user`, `content`, `time_posted`

2. Name of the second table (always plural): `users` 

    Column names: `email`, `password`, `name`, `username` 

## 3. Decide the column types

[Here's a full documentation of PostgreSQL data types](https://www.postgresql.org/docs/current/datatype.html).

Most of the time, you'll need either `text`, `int`, `bigint`, `numeric`, or `boolean`. If you're in doubt, do some research or ask your peers.

Remember to **always** have the primary key `id` as a first column. Its type will always be `SERIAL`.

```
# EXAMPLE:

Table: peeps
id: SERIAL
user_id: int
content: TEXT
time_posted: TIMESTAMP DEFAULT CURRENT_TIMESTAMP

Table: users
id: SERIAL
name: TEXT
email: TEXT
password: TEXT
username: TEXT
```

## 4. Decide on The Tables Relationship

Most of the time, you'll be using a **one-to-many** relationship, and will need a **foreign key** on one of the two tables.

To decide on which one, answer these two questions:

1. Can one peep have many users? (No)
2. Can one user have many peeps? (Yes)

You'll then be able to say that:

1. **[A] has many [B]**
2. And on the other side, **[B] belongs to [A]**
3. In that case, the foreign key is in the table [B]

THE FOREIGN KEY WILL BE ON PEEPS

## 5. Write the SQL

```sql
-- file: chitter_tables.sql

CREATE TABLE users (
  id SERIAL PRIMARY KEY,
  name TEXT,
  email TEXT,
  password TEXT,
  username TEXT,

);

CREATE TABLE peeps (
  id SERIAL PRIMARY KEY,
  content TEXT,
  time_posted TIMESTAMP DEFAULT CURRENT_TIMESTAMP
  -- The foreign key name is always {other_table_singular}_id
  user_id int,
  constraint fk_user foreign key(user_id)
    references users(id)
    on delete cascade
);

```

## 6. Create the tables

```bash
psql -h 127.0.0.1 chitter_app < chitter_tables.sql
```