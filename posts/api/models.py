from api import db
from datetime import datetime

  

class Restaurant(db.Model):
    __tablename__ = 'restaurants'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True, nullable=False)
    address = db.Column(db.String(255))
    restaurant_pizzas = db.relationship('RestaurantPizza', back_populates='restaurant')

    def __str__(self):
        return self.name
    
class Pizza(db.Model):
    __tablename__ = 'pizzas'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    ingredients = db.Column(db.String(255))
    pizza_restaurants = db.relationship('RestaurantPizza', back_populates='pizza')
    created_at =db.Column(db.DateTime,default = datetime.utcnow)
    update_at = db.Column(db.DateTime,default = datetime.utcnow)

    def __str__(self):
        return self.name

class RestaurantPizza(db.Model):
    __tablename__ = 'restaurant_pizza'
    id = db.Column(db.Integer, primary_key=True)
    price = db.Column(db.Float, nullable=False)
    restaurant_id = db.Column(db.Integer, db.ForeignKey('restaurants.id'))
    pizza_id = db.Column(db.Integer, db.ForeignKey('pizzas.id'))
    restaurant = db.relationship('Restaurant', back_populates='restaurant_pizzas')
    pizza = db.relationship('Pizza', back_populates='pizza_restaurants')
    created_at =db.Column(db.DateTime,default = datetime.utcnow,nullable = False)
    update_at = db.Column(db.DateTime,default = datetime.utcnow,nullable = False )
