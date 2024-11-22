-- Drop the database if it exists, then create a new one
DROP DATABASE IF EXISTS adopt;
CREATE DATABASE adopt;
USE adopt;

-- Create the pets table
CREATE TABLE pets (
  id SERIAL PRIMARY KEY,
  name TEXT NOT NULL,
  species TEXT NOT NULL,
  photo_url TEXT,
  age INT,
  notes TEXT,
  available BOOLEAN NOT NULL DEFAULT TRUE
);

-- Adding pet data into the pets table
INSERT INTO pets (name, species, photo_url, age, notes, available)
VALUES
  ('Woofly', 'dog', 'https://images.unsplash.com/photo-1447684808650-354ae64db5b8?q=80&w=1167&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D', 3, 'Incredibly adorable.', TRUE),
  ('Porchetta', 'porcupine', 'http://kids.sandiegozoo.org/sites/default/files/2017-12/porcupine-incisors.jpg', 4, 'Somewhat spiky!', TRUE),
  ('Snargle', 'cat', 'https://images.unsplash.com/photo-1495360010541-f48722b34f7d?q=80&w=1036&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D', NULL, NULL, TRUE),
  ('Dr. Claw', 'cat', NULL, NULL, NULL, TRUE);
