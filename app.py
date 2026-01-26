from flask import (render_template, 
                   request, 
                   redirect, 
                   url_for)
from flask_sqlalchemy import SQLAlchemy
from models import Pet, db, app

# script to run a server
# Flask API with SQLAlchemy


# remove class base declarative base if importing from a models.py - db = SQLAlchemy(app) is the replacement
# needed to connect the db

# association table with no model used to map relationships
# relational databases cannot have many to many relationships. must have a middle table that stores pairs of ids
# from flasksqlalchemy official documentation
"""
import sqlalchemy as sa
user_book_m2m = db.Table(
    "user_book",
    sa.Column("user_id", sa.ForeignKey(User.id), primary_key=True),
    sa.Column("book_id", sa.ForeignKey(Book.id), primary_key=True),
)
"""

@app.route("/")
def index():
    # query over all records in the db # pets is an instance of an object
    pets = Pet.query.all() # query is a subclass. # the query object will deduplicate entries based on primary key
    return render_template("index.html", pets=pets)


@app.route("/add-pet", methods=["GET", "POST"])
def add_pet():
    if request.form:
        new_pet = Pet(name=request.form['name'], 
                      age=request.form['age'],
                      breed=request.form["breed"], 
                      color=request.form["color"],
                      size=request.form['size'], 
                      weight=request.form['weight'],
                      url=request.form['url'], 
                      url_tag=request.form['alt'],
                      pet_type=request.form['pet'], 
                      gender=request.form['gender'],
                      spay=request.form['spay'], 
                      house_trained=request.form['housetrained'],
                      description=request.form['description'])
        db.session.add(new_pet)
        db.session.commit() # transaction closed
        return redirect(url_for('index'))
    return render_template("addpet.html")


@app.route("/pet/<id>")
def pet(id): # used with url_for under index.html jinja template {{ % % }}
    pet = Pet.query.get_or_404(id) # how to get, return a query. get user by primary key
    return render_template("pet.html", pet=pet)


@app.route('/edit/<id>', methods=["GET", "POST"])
def edit_pet(id):
    pet = Pet.query.get_or_404(id)
    if request.form:
        pet.name = request.form['name'] # notice there is no comma ending the row
        pet.age = request.form['age']
        pet.breed = request.form['breed']
        pet.color = request.form['color']
        pet.size = request.form['size']
        pet.weight = request.form['weight']
        pet.url= request.form['url']
        pet.url_tag = request.form['alt']
        pet.name = request.form['name']
        pet.pet_type = request.form['pet']
        pet.gender = request.form['gender']
        pet.spay = request.form['spay']
        pet.house_trained = request.form['housetrained']
        pet.description = request.form["description"]
        db.session.commit()
        return redirect(url_for('index'))

    return render_template('editpet.html', pet=pet) # custom made



@app.route("/delete/<id>")
def delete_pet(id):
    pet = Pet.query.get_or_404(id)
    db.session.delete(pet)
    db.session.commit()
    return redirect(url_for('index'))

@app.errorhandler(404) # from custom error page in flask documentation
def not_found(error):
    return render_template('404.html', msg=error), 404


if __name__ == "__main__":
    with app.app_context():
        db.create_all() # replace the base.metadata.create_all from sqlalchemy
    app.run(debug=True, port=8000, host="127.0.0.1") # host different used in docker in db connection
