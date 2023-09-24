from api import db, api
from flask_restful import Resource
from .models import Restaurant
from .models import Pizza
from .models import RestaurantPizza
from .serializer import response_serializer

# Define the routes and associated resources
class RestaurantsResource(Resource):
    def get(self):
        Restaurant = Restaurant.query.all()
        response = response_serializer(Restaurant)
        return response,200

class RestaurantResource(Resource):
    def get(self, restaurant_id):
        restaurant_id = restaurant_id.query.all()
        response = response_serializer(restaurant_id)
        return response,200
        
    
    def delete(self, restaurant_id):
         
        pass

class PizzasResource(Resource):
    def get(self):
        Pizza = Pizza.query.all()
        response = response_serializer(Pizza)
        return response,200

class RestaurantPizzasResource(Resource):
    def post(self):
        RestaurantPizza = RestaurantPizza.query.all()
        response = response_serializer(RestaurantPizza)
        return response,200

# Add resources to the API
api.add_resource(RestaurantsResource, '/restaurants')
api.add_resource(RestaurantResource, '/restaurants/<int:restaurant_id>')
api.add_resource(PizzasResource, '/pizzas')
api.add_resource(RestaurantPizzasResource, '/restaurant_pizzas')
