USE sqs;

CREATE USER 'docker'@'%' IDENTIFIED BY 'docker';
GRANT ALL PRIVILEGES ON *.* TO 'docker'@'%';
INSERT INTO authtoken_token (`key`, created, user_id) VALUES ('dcd52b4996698b6c5db63df6894550fe1069d2a0','1994-07-29', '1');