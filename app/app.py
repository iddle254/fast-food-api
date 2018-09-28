"""this contains my routes"""
from flask import Flask, jsonify, request
from validator import ValidFoodOrder

#creates an instance of flask
app = Flask(__name__)

VALIDATE = ValidFoodOrder()

#mock_data
ORDER_ITEMS = []
"""route that fetches and returna all the items in the list"""
@app.route('/api/v1/orders', methods=['GET'])
def orders():
    return jsonify({'ORDER_ITEMS':ORDER_ITEMS})
"""route that fetches one single order"""
@app.route('/api/v1/orders/<string:name>', methods=['GET'])
def order(name):
    valid_food_name = VALIDATE.foodNameValidator(name)
    if valid_food_name:
        ordered = [item for item in ORDER_ITEMS if item['name'] == name]
        return jsonify({'item':ordered[0]})

"""route that posts a new order"""
@app.route('/api/v1/orders', methods=['POST'])
def new_order():
    item = {'name':request.json['name']}
    ORDER_ITEMS.append(item)
    return jsonify({'ORDER_ITEMS':ORDER_ITEMS})

#green
"""route that updates a single order"""
@app.route('/api/v1/orders/<string:name>', methods=['PUT'])
def update(name):
    valid_food_name = VALIDATE.foodNameValidator(name)
    if valid_food_name:
        ordered = [item for item in ORDER_ITEMS if item['name'] == name]
        ordered[0]['name'] = request.json['name']
        return jsonify({'item':ordered[0]})

if __name__ == '__main__':
    app.run(debug=True)
