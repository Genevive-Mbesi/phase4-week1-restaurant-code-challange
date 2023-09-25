from api import db, api
from flask_restful import Resource,reqparse 
from .models import Restaurant
from .models import Pizza
from .models import RestaurantPizza
from .serializer import response_serializer
from datetime import datetime

parser = reqparse.RequestParser()
parser.add_argument('price')
parser.add_argument('restauran_id')
parser.add_argument('pizz_id')
parser.add_argument('restaurant')
parser.add_argument('pizza') 
parser.add_argument('created_at') 
parser.add_argument('update_at') 





# Define the routes and associated resources
class RestaurantsResource(Resource):
    def get(self):
        Restaurant = Restaurant.query.all()
        response = response_serializer(Restaurant)
        return response,200

class RestaurantData(Resource):
    def get(self, id):
        restaurant = Restaurant.query.get(int(id))
        
        if restaurant:
            response = response_serializer([restaurant])
            return response, 200
        else:
            return{"message":"Not found"}
        
    def put(self,id):
        data = parser.parse_args() 

        print("===",data)
        date = datetime.strptime(data["created_at"],"%d/%m/%y") 
        data["created_at"]= date


    def _update_data(self,data, pizza,created_at,updated_at):
        pizza.name = data["name"]
        pizza.ingridients = data ["ingridients"]
        pizza.created_at = created_at ["created_at"]
        pizza.updated_at = updated_at["updated_at"]

        db.session.add(pizza)
        db.session.commit()

        response =response_serializer([pizza])
        return response,200
    
    def delete(self,id):
         
        pass

class PizzasResource(Resource):
    def get(self):
        Pizza = Pizza.query.all()
        response = response_serializer(Pizza)
        return response,200

class RestaurantPizzasResource(Resource):
    def post(self):
        data = parser.parse_args() 

        print("===",data)
        date = datetime.strptime(data["created_at"],"%d/%m/%y") 
        data["created_at"]= date
        new_data = RestaurantPizza(**data)

        print("===new__value==",new_data)
        db.session.add[new_data]
        db.session.commit()
        data['created_at'] = str(date)
        return data, 201  

        


# Add resources to the API
api.add_resource(RestaurantsResource, '/restaurants')
api.add_resource(RestaurantData, '/restaurants/<int:id>')
api.add_resource(PizzasResource, '/pizzas')
api.add_resource(RestaurantPizzasResource, '/restaurant_pizzas')
