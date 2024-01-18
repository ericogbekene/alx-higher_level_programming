-- Script to create a new sql user

-- IF NOT EXISTS
CREATE USER IF NOT EXISTS 'user_0d_1'@'localhost' IDENTIFIED BY 'user_0d_1_pwd';

-- GRANT ALL PRIVILEGE TO 'user_0d_1'@'localhost'

GRANT ALL PRIVILEGES ON *.* TO 'user_0d_1'@'localhost' WITH GRANT OPTION;
