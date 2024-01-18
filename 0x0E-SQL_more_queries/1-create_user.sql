-- Script to create a new sql user

CREATE USER 'user_0d_1'@'localhost' IDENTIFIED WITH authentication_plugin BY 'user_0d_1_pwd';

-- GRANT ALL PRIVILEGE TO 'user_0d_1'@'localhost'

GRANT ALL PRIVILEGES ON *.* TO 'user_0d_1'@'localhost' WITH GRANT OPTION;
