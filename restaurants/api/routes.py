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


# class RestaurantData(Resource):
#     def get(self, id):
#         restaurant = Restaurant.query.get(int(id))
        
#         if restaurant:
#             response = response_serializer([restaurant])
#             return response, 200
#         else:
#             return{"message":"Not found"}
        
    
    # def delete(self,id):
         
        # pass

# class PizzasResource(Resource):
#     def get(self):
#         Pizza = Pizza.query.all()
#         response = response_serializer(Pizza)
#         return response,200
    
#     def put(self,id):
#         data = parser.parse_args() 

#         print("===",data)
#         date = datetime.strptime(data["created_at"],"%d/%m/%y") 
#         data["created_at"]= date


    # def _update_data(self,data, pizza,created_at,updated_at):
    #     pizza.name = data["name"]
    #     pizza.ingridients = data ["ingridients"]
    #     pizza.created_at = created_at ["created_at"]
    #     pizza.updated_at = updated_at["updated_at"]

    #     db.session.add(pizza)
    #     db.session.commit()

    #     response =response_serializer([pizza])
    #     return response,200

# class RestaurantPizzasResource(Resource):
#     def post(self):
#         data = parser.parse_args() 

#         print("===",data)
#         date = datetime.strptime(data["created_at"],"%d/%m/%y") 
#         data["created_at"]= date
#         new_data = RestaurantPizza(**data)

#         print("===new__value==",new_data)
#         db.session.add[new_data]
#         db.session.commit()
#         data['created_at'] = str(date)
#         return data, 201  

        


# Add resources to the API
api.add_resource(RestaurantsResource, '/restaurants')
api.add_resource(RestaurantByIdResource, '/restaurants/<int:id>')
api.add_resource(PizzaResource, '/pizzas')
# api.add_resource(PizzasResource, '/pizzas')
# api.add_resource(RestaurantPizzasResource, '/restaurant_pizzas')
