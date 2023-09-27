from api import db, api
from flask import make_response, jsonify
from flask_restful import Resource,reqparse 
from .models import Restaurant
from .models import Pizza
from .models import RestaurantPizza
from datetime import datetime

class PizzaResource(Resource):
    def get(self):
        pizzas = Pizza.query.all()
        pizzas_dict =  [{"id": pizza.id, "name": pizza.name, "ingredients": pizza.ingredients } for pizza in pizzas ]
        response = make_response(jsonify(pizzas_dict), 200)
        return response

# Define the routes and associated resources
class RestaurantsResource(Resource):
    def get(self):
        restaurants = Restaurant.query.all()
        restaurants_dict = []
        for r in restaurants:
            restaurant_dict = {"id":r.id, "name": r.name, "address": r.address}
            restaurants_dict.append(restaurant_dict)
        response = make_response(jsonify(restaurants_dict), 200)
        return response
    
class RestaurantByIdResource(Resource):
    def get(self, id):
        restaurant = Restaurant.query.filter_by(id=id).first()
        if restaurant:
            pizzas =  [{"id": pizza.id, "name": pizza.name, "ingredients": pizza.ingredients } for pizza in restaurant.pizzas ]
            restaurant_dict = {
                "id": restaurant.id,
                "name": restaurant.name,
                "address": restaurant.address,
                "pizzas": pizzas
            }
            response = make_response(jsonify(restaurant_dict), 200)
            return response
        else:
            response = make_response(jsonify({ "error": "Restaurant not found"}), 404)
            return response
    def delete(self, id):
        restaurant = Restaurant.query.filter_by(id=id).first()
        if restaurant:
            RestaurantPizza.query.filter_by(restaurant_id=id).delete()
            db.session.delete(restaurant)
            db.session.commit()
            response = make_response(jsonify(""), 204)
            return response
        else:
            response = make_response(jsonify({ "error": "Restaurant not found"}), 404)
            return response

class RestaurantPizzaResource(Resource):
    def get (self):
        restaurant_pizzas = RestaurantPizza.query.all()
        restaurant_pizzas_dict =[
            {"id":rp.id,"price":rp.price}for rp in restaurant_pizzas
        ]
        return make_response(jsonify(restaurant_pizzas_dict),200)
        


# Add resources to the API
api.add_resource(RestaurantsResource, '/restaurants')
api.add_resource(RestaurantByIdResource, '/restaurants/<int:id>')
api.add_resource(PizzaResource, '/pizzas')
api.add_resource(RestaurantPizzaResource,"/restaurant_pizzas")
