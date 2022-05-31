""" database dependencies to support Users db examples """
from __init__ import db
from sqlalchemy.exc import IntegrityError
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin

# -- c.) SQLAlchemy ORM is layer on top of SQLAlchemy Core, then SQLAlchemy engine, SQL
class Recipes(UserMixin, db.Model):
    # define the Recipes schema
    recipeID = db.Column(db.Integer, primary_key=True)
    recipeName = db.Column(db.String(255), unique=False, nullable=False)
    userID = db.Column(db.Integer, primary_key=True)
    recipe = db.Column(db.String(255), unique=False, nullable=False)
    recipeImage = db.Column(db.String(255), unique=False, nullable=False)

    # constructor of a User object, initializes of instance variables within object
    def __init__(self, recipeID, recipeName, userID, recipe, recipeImage):
        self.recipeID = recipeID
        self.recipeName = recipeName
        self.userID = userID
        self.recipe = recipe
        self.recipeImage = recipeImage

    # CRUD create/add a new record to the table
    # returns self or None on error
    def create(self):
        try:
            # creates a person object from Users(db.Model) class, passes initializers
            db.session.add(self)  # add prepares to persist person object to Users table
            db.session.commit()  # SqlAlchemy "unit of work pattern" requires a manual commit
            return self
        except IntegrityError:
            db.session.remove()
            return None

    # CRUD read converts self to dictionary
    # returns dictionary
    def read(self):
        return {
            "recipeID": self.userID,
            "recipeName": self.recipeName,
            "userID": self.userID,
            "recipe": self.recipe,
            "recipeImage": self.recipeImage,
        }

    # CRUD update: updates users name, password, phone
    # returns self
    def update(self, recipeID, recipe, recipeImage):
        """only updates values with length"""
        if len(recipeID) > 0:
            self.recipeID = recipeID
        if len(recipe) > 0:
            self.recipe = recipe
        if len(recipeImage) > 0:
            self.recipeImage = recipeImage
        db.session.commit()
        return self

    # CRUD delete: remove self
    # None
    def delete(self):
        db.session.delete(self)
        db.session.commit()
        return None

    # required for login_user, overrides id (login_user default) to implemented userID
    def get_id(self):
        return self.userID


"""Database Creation and Testing section"""


def model_tester():
    print("--------------------------")
    print("Seed Data for Table: users")
    print("--------------------------")
    db.create_all()
    """Tester data for table"""
    table = [
      Recipes(recipeID='', recipeName='', userID='', recipe='', recipeImage=''),
      Recipes(recipeID='', recipeName='', userID='', recipe='', recipeImage=''),
      Recipes(recipeID='', recipeName='', userID='', recipe='', recipeImage='')]
    for row in table:
        try:
            db.session.add(row)
            db.session.commit()
        except IntegrityError:
            db.session.remove()
            print(f"Records exist, duplicate email, or error: {row.email}")


def model_printer():
    print("------------")
    print("Table: users with SQL query")
    print("------------")
    result = db.session.execute('select * from users')
    print(result.keys())
    for row in result:
        print(row)


if __name__ == "__main__":
    model_tester()  # builds model of Users
    model_printer()
