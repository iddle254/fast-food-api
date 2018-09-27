import os
from flask import Blueprint
from .models import ValidFoodOrder
profile = Blueprint('profile', __name__, url_prefix='/api/v1/orders')

validate = ValidFoodOrder()

#mock_data
order_items = []
item_to_be_added = {'name':'ugali'}

@profile.url_value_preprocessor
def get_profile_owner(endpoint, values):
    query = User.query.filter_by(url_slug=values.pop('/api/v1/orders'))
    g.profile_owner = query.first_or_404()

@profile.route('/',methods=['GET'])
def orders():	
	return jsonify({'order_items':order_items})

 
@profile.route('/<string:name>',methods=['GET'])
def order(name):
    validFoodName = validate.foodNameValidator(name)
    if validFoodName:
	    ordered = [item for item in order_items if item['name']==name]	
	    return jsonify({'item':ordered[0]})


@profile.route('/',methods=['POST'])
def new_order():  	
	item = {'name':request.json['name']}
	order_items.append(item)
	return jsonify({'order_items':order_items})