My task was to:
Implement REST-service (operations GET/POST/PUT/DELETE) for one of classes from lab3 with usage of python tools:
Flask
Python 3.x
Implement saving of object of the class from lab3 in database with usage of:
SQLAlchemy-1.1.15
___MySQL-5.7 / MySQL 8.0
Content
Wev-page for application using HTML, CSS
Database MySQL (using PyMySQL)
POST, PUT, DELETE methods
How to run (Windows)
Go to directory where you want to clone this repository and type in: git clone https://github.com/Zocya/lab6/pull/1
Move in this project directory.
Create your virtual environment in command line and activate it:
python -m venv venv
venv\scripts\activate.bat
Create MySQL database named flask-tutorial-db:
mysql -u root -p
CREATE USER IF NOT EXISTS 'flask-user'@'localhost' IDENTIFIED BY '1050';
exit
mysql -u flask-user -p
create database if not exists lab6flask;
exit
Install all project requirements pip install -r requirements.txt
Create needed tables in the database:
Open python interpreter with the command python
Import our database from app import db
Create all needed tables with command db.create_all()
exit()
Run application python app.py
