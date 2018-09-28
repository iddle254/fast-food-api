import os
import re


valid_food=''

class ValidFoodOrder(object):    

    def foodNameValidator(self, food):
        lowercase = re.search("[a-z]",item)
        uppercase = re.search("[A-Z]",item)
        characters = re.search("[$#@]",item)
        for item in food:
            if type(item) != str or characters:
                api.abort(406, "food items can only be words. {} is not a string!".format(food))        
        if uppercase:
        	valid_food = food.lower()
        else:
        	valid_food = food
        return True    

    def priceValidator(self, price):
        if type(price) != int:
            api.abort(406, "the price can only be an integer. {} is not an integer".format(price))
        return True

    def validOrder(self,food):
	    for food_item in food_items:
		    if food_item.get('title') == food:
			    api.abort(302,"The order {} already exists. Maybe you would like something else instead".format(food))
	    return true