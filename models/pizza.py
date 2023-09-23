from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Pizza(db.Model):
    __tablename__ = 'pizzas'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    ingredients = db.Column(db.String(255))
    pizza_restaurants = db.relationship('RestaurantPizza', back_populates='pizza')
