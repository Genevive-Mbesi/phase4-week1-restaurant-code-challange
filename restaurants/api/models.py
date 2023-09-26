from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy_serializer import SerializerMixin

db = SQLAlchemy()

class Restaurant(db.Model, SerializerMixin):
    __tablename__ = 'restaurants'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True, nullable=False)
    address = db.Column(db.String(255))
    pizzas = db.relationship("Pizza",secondary = "restaurant_pizzas",back_populates="restaurants")


    def __str__(self):
        return self.name
    
class Pizza(db.Model, SerializerMixin):
    __tablename__ = 'pizzas'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    ingredients = db.Column(db.String(255))
    created_at =db.Column(db.DateTime,default = datetime.utcnow)
    update_at = db.Column(db.DateTime,default = datetime.utcnow)
    restaurants = db.relationship("Restaurant",secondary = "restaurant_pizzas",back_populates="pizzas")

    def __str__(self):
        return self.name

class RestaurantPizza(db.Model, SerializerMixin):
    __tablename__ = 'restaurant_pizzas'
    id = db.Column(db.Integer, primary_key=True)
    price = db.Column(db.Float, nullable=False)
    restaurant_id = db.Column(db.Integer, db.ForeignKey('restaurants.id'))
    pizza_id = db.Column(db.Integer, db.ForeignKey('pizzas.id'))
    created_at =db.Column(db.DateTime,default = datetime.utcnow,nullable = False)
    update_at = db.Column(db.DateTime,default = datetime.utcnow,nullable = False )
