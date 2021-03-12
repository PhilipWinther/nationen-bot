#INSTALLING DEPENDENCIES: 

sudo apt update
sudo apt upgrade -y

sudo apt install mysql-server
sudo apt install xvfb
sudo apt install firefox

sudo apt install python3
sudo apt install python3-pip

pip3 install requests
pip3 install bs4 
pip install mysql-connector-python 
pip3 install selenium
pip3 install pyvirtualdisplay

-----------------------------------------------
#CREATE DATABASE:

CREATE DATABASE "nationen" CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci;

use nationen;

CREATE TABLE comments(id INT AUTO_INCREMENT PRIMARY KEY, url VARCHAR(255), dateimported datetime, comment TEXT(1000) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci);

CREATE TABLE url(id INT AUTO_INCREMENT PRIMARY KEY, url VARCHAR(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci);

CREATE USER 'USER'@'localhost' IDENTIFIED BY 'password';

GRANT ALL PRIVILEGES ON nationen.* TO 'user'@'localhost';

FLUSH PRIVILEGES;


-----------------------------------------------
#RUNNING BOT:

1.  run get-url.py
2. run eblinks.py
3. run get-comments.py

fix ressource problem, it keeps adding new xfvb sessions
