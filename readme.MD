sqlalchemy,
    db_model
flasksqlalchemy,
    jinja
docker compose
mysql db inside .yml
html
    templates
css
    bootstrap
javascript
    dropdown menu
pymysql
    use docker with mysql server
flask,
    request,
        -proxy
        -access incoming request data after using url_for and GET and POST methods
    url_for,
        send-subbmit the html form. not just leave it in the browser user-agent as a post request
    render_template
    redirect

# docker image and container runs in a usb with mysql db

# to run the table model and server. not the db:
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt

# maybe initialize first mysql and then the orm mapper of sqlalchemy in python????


# run docker. once the docker image is in the system
docker compose up -d # make new container

# create the table columns rows mapping with the orm
# create the table from the model with sqlalchemy
python3 app.py

# the database is made with docker-compose.yml and the table with flask
# flask server is running and the table is made automatically from the compose.yml and sqlalchemy model
# check as mysql root
# do not use root in flask
docker exec -it mysql-usb mysql -uroot -p # empty password
## login as flask_user to mysql. should have all privileges already to create tables
docker exec -it mysql-usb mysql -uflask_user -p
# docker mysql password
flask_password
# check mysql user
SELECT USER(); # shoulde be: flask_user

# run docker mysql
check if mysql is running in docker ?
check charset in mysql db for client. should be unicode...
STATUS;


# mysql while in flask_user
SHOW DATABASES;
USE pet_adoption_db;
SHOW TABLES;
DESCRIBE table_name;

# check pymysql for db connection
# create a dedicated mysql user for flask docker container
SELECT user, host FROM mysql.user;


# or socket
# create flask user that allows tcp connections. with docker. because of docker it needs a tcp. or it can go through the socket
CREATE USER 'flask_user'@'%' IDENTIFIED BY 'flask_password';
GRANT ALL PRIVILEGES ON pet_adoption_db.* TO 'flask_user'@'%';
FLUSH PRIVILEGES;
app.config['SQLALCHEMY_DATABASE_URI'] = (
    "mysql+pymysql://flask_user:flask_password@127.0.0.1:3306/pet_adoption_db?charset=utf8mb4"
)
# 127.0.0.1:3306 → TCP connection to Docker MySQL. docker is not automatically involved
# Use TCP (127.0.0.1), not localhost if connecting to Docker.

# /var/run/mysqld/mysqld.sock exists only inside the mysql container

# show mysql shell process list
SHOW PROCESSLIST\G;

# test connection from python repl venv
-Use SQLAlchemy if you want models, ORM queries, sessions, and easier Flask integration.
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import text

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://flask_user:flask_password@127.0.0.1:3306/pet_adoption_db?charset=utf8mb4"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

with app.app_context():
    with db.engine.connect() as conn:
        result = conn.execute(text("SELECT 1"))
        print(result.fetchall())  # [(1,)]
#
-Use PyMySQL directly if you want raw SQL, or for quick scripts.
import pymysql

conn = pymysql.connect(
    host="127.0.0.1",
    user="flask_user",
    password="flask_password",
    database="users_some_tablename",
    charset="utf8mb4"
)

with conn.cursor() as cursor:
    cursor.execute("SELECT 1")
    print(cursor.fetchall())  # [(1,)]

conn.close()

# access the server
https://requests.readthedocs.io/en/latest/user/quickstart/
https://pypi.org/project/requests/
in python
import requests
r = requests.get("http://127.0.0.1:8000")
print(r.status_code)
r.content # get html # same as curl "http://somepage.com"

# check further reading. popular flask extensions
flask-login
flask-security-too
flask-user. registration,emailverification, password mannagement

# flask-sqlalchemy extension creates sessionn and commits everything to use query orm class 
create engine
crete session
handles teardown automatically per request
#
db.session is wrapped
obj = db.session.query(class_name).all()
obj = class_name.query.all() # same as above

# __tablename__ is assumed with flasksqlalchemy extension within the model
# 

# flask sqlalchemy manages a session per request. open, add, commit or rollback, and session closed()
## index.html image jinja templates 
src = {{ class_instance.attribute }}
alt ='{{ class_instance.attribute }}'

## for loops over instance attributes:
{% for each in class_instance %}
{% endfor %}
## block buttons
{% block button_name %}
{% endblock %}
# block content
{% block content %}
{% endblock %}

#
{{ function_name.some_model_attribute }}

#
{{ function_name.name }}

#
{{ url_for(flask_function) }}

# image size default is 100w without srcset
# html image size with src or srcset
<a>
  href = html attribute
</a>
img src='https://somepage.com.jpg'
img srcset='https://some.com.jpg, width = 200w'
img srcset handles multiple device widths

# srcset attribute in html. benefits web accessibility for people with disabilities
# best practice provide more than one size width url w
Benefits
✔ Faster loading on small screens
✔ Saves bandwidth
✔ Higher-quality image when needed
✔ Browser chooses optimal source


# how to see the data from within mysql shell
flask shell
class_name.query.all() # query subclass with more classes

# jinja variables and or expressions
# jinja tags, variables
# jinja different kind of delimiters:
statements
{% ... %}
expressions
{{ ... }}
comments
{# ... #}

# variables in jinja
{{ foo.bar }}
{{ foo['bar'] }}


# jinja index.html. get rid of the https:url more than 150 char sometimes
<a href="{{ url_for('pet', id=pet.id) }}">
    <div class="card">
        <img src='{{ pet.url }}' alt='{{ pet.url_tag }}'>
        <h2>{{ pet.name }}</h2>
        <h3>{{ pet.age }}</h3>
        <p>{{ pet.description }}</p>
    </div>
</a>

# how to print in the edit page the value of the string from the model inside a form
<input id="alt" name="alt" type="text" placeholder="This photo is..." value="{{ pet.url_tag }}">



# handling application errors from flask official documentation
- client terminated the request early and the application was still reading from the incoming data
- the database server as overloaded and could not handle the query
- filesystem is full
- harddrive crashed
- backend server overloaded
- programming error in a used library
- network connection of the server to another system failed
# flask custom error pages
https://werkzeug.palletsprojects.com/en/stable/exceptions/#werkzeug.exceptions.HTTPException
# error logging tools
# error handlers, registering, handling, generic exception handlers, unhandled exceptions
# custom error pages
# blueprint error handlers
# returning api errors as json


# javascript using html class

# what is a class attribute in html?
    - a class is reusable in several files
# what is an id attribute in html?
    - only one id per page
# what is href attribute in html?
    - hypertext reference
# what is anchor in html?