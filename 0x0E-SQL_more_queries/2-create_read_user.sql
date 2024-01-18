-- CReate user and Database 

-- Create a new user
CREATE USER IF NOT EXISTS 'user_0d_2'@'localhost' IDENTIFIED BY 'user_0d_2_pwd';

-- Create a new Database
CREATE DATABASE IF NOT EXISTS hbtn_0d_2;
-- Grant nee user Permissions
GRANT SELECT ON hbtn_0d_2.* TO 'user_0d_2'@'localhost';
