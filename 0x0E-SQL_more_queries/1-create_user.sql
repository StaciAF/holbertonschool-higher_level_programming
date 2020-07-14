-- script creates new user with given password
-- using MySQL server
CREATE USER IF NOT EXISTS 'user_0d_1'@'localhost'
IDENTIFIED by 'user_0d_1_pwd'
GRANT ALL PRIVILEGES ON *.*
TO 'user_0d_1'@'localhost'
IDENTIFIED by 'user_0d_1_pwd';
