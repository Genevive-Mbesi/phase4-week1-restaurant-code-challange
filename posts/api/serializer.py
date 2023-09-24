from .models import Restaurant
from .models import Pizza
from .models import RestaurantPizza

def response_serializer(restaurants:Restaurant):
    response =[]
    for Restaurant in Restaurant:
        response.append({
          "id":Restaurant.id,
          "name":Restaurant.name,
          "address":Restaurant.address,
          "restaurant_pizza":Restaurant.restaurant_pizza,
        })
    return response

def response_serializer(pizzas:Pizza):
    response =[]
    for Pizza in Pizza:
        response.append({
          "id":Pizza.id,
          "name":Pizza.name,
          "ingridients":Pizza.ingridients,
          "pizza_restaurants":Pizza.pizza_restaurants,
        })
    return response

def response_serializer(restautrantPizza:RestaurantPizza):
    response =[]
    for RestaurantPizza in RestaurantPizza:
        response.append({
          "id":RestaurantPizza.id,
          "price":RestaurantPizza.price,
          "restaurant_id":RestaurantPizza.restaurant_id,
          "pizza_id":RestaurantPizza.pizza_id,
          "restaurant":RestaurantPizza.restaurant,
          "pizza":RestaurantPizza.pizza,
        })
    return response
