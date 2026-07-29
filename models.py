from flask import Flask
import datetime
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
# localhost does not work in usb docker mysql
# set chasrset of client as utf8mb4. not latin1 breaks unicode
# a basic db connection URL uses. username, password, host, and port
# 127.0.0.1 forces tcp docker port mapping forwards to container
# dialect://username:password@host:port/database
# has hostname,
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://flask_user:flask_password@127.0.0.1:3306/pet_adoption_db?charset=utf8mb4'
db = SQLAlchemy(app)
#db.init_app(app)# do not call db.init_app(app) when already passed the app to sqlalchemy(app)



class Pet(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    created = db.Column('Created', db.DateTime, default=datetime.datetime.now)
    # string is varchar in mysql. varchar requires length in mysql
    name = db.Column('Name', db.String(50))
    age = db.Column('Age', db.String(50))
    breed = db.Column('Breed', db.String(50))
    color = db.Column('Color', db.String(50))
    size = db.Column('Size', db.String(50))
    weight = db.Column('Weight', db.String(50))
    url = db.Column('URL', db.Text)
    url_tag = db.Column("Alt Tag", db.String(50))
    pet_type = db.Column('Pet Type', db.String(50))
    gender = db.Column('Gender', db.String(50))
    spay = db.Column('Spay', db.String(50))
    house_trained = db.Column('House Trained', db.String(50))
    # text is char in mysql. trailing spaces are removed upon retrieval
    description = db.Column('Description', db.Text)


    def __repr__(self): # self is a class
        return f'''<Pet (Name: {self.name}
                Age: {self.age}
                Breed: {self.breed}
                Color: {self.color}
                Size: {self.size}
                Weight: {self.weight}
                URL: {self.url}
                Tag: {self.url_tag}
                Gender: {self.gender}
                Spay: {self.spay}
                House Trained: {self.house_trained}
                Description: {self.description})'''