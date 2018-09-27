import os
from flask import Blueprint
from .models import ValidFoodOrder
profile = Blueprint('profile', __name__, url_prefix='/api/v1/orders')

validate = ValidFoodOrder()

#mock_data
order_items = []
item_to_be_added = {'name':'ugali'}

@profile.route('/',methods=['GET'])
def orders():	
	return jsonify({'order_items':order_items})

@profile.route('/<string:name>',methods=['GET'])
def order(name):
    validFoodName = validate.foodNameValidator(name)
    if validFoodName:
	    ordered = [item for item in order_items if item['name']==name]	
	    return jsonify({'item':ordered[0]})

@profile.route('/<string:name>',methods=['PUT'])
def update(name):
	validFoodName = validate.foodNameValidator(name)
	if validFoodName:
	    ordered = [item for item in order_items if item['name']==name]
	    ordered[0]['name'] = request.json['name']
	    return jsonify({'item':ordered[0]})