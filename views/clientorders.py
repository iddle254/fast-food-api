"""this contains my routes"""
from flask import Blueprint

#creates an instance of flask
clientorders = Blueprint('clientorders', __name__)

VALIDATE = ValidFoodOrder()

#mock_data
ORDER_ITEMS = []

"""route that fetches and returna all the items in the list"""
@clientorders.route('/', methods=['GET'])
def orders():
    return jsonify({'ORDER_ITEMS':ORDER_ITEMS})
"""route that fetches one single order"""
@clientorders.route('/<string:name>', methods=['GET'])
def order(name):
    valid_food_name = VALIDATE.foodNameValidator(name)
    if valid_food_name:
        ordered = [item for item in ORDER_ITEMS if item['name'] == name]
        return jsonify({'item':ordered[0]})

"""route that posts a new order"""
@clientorders.route('/', methods=['POST'])
def new_order():
    item = {'name':request.json['name']}
    ORDER_ITEMS.clientordersend(item)
    return jsonify({'ORDER_ITEMS':ORDER_ITEMS})


