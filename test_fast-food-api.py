from flask import Flask,jsonify,json
#imports pytest
import pytest

#creates an instance of flask
app = Flask(__name__)

#mock_data
order_items = [{'name':'pizza'},{'name':'steak'},{'name':'rice'},{'name':'Fries'}]
item_to_be_added = [{'name':'ugali'}]

#red test
def test_orders():
	#test to see if orders returns all the orders	
    result=app.test_client()
    response= result.get('/api/v1/orders',content_type='application/json')
    assert(response.status_code==200)
#green
@app.route('/api/v1/orders',methods=['GET'])
def orders():	
	return jsonify({'order_items':order_items})
"""
tests the update order

"""
#red test
def test_update():	
	#test to see if the order updates
    result=app.test_client()
    response= result.put('/api/v1/order', data=json.dumps(item_to_be_added) ,content_type='application/json')
    assert(response.status_code==404)
#green
@app.route('/api/v1/order/<string:name>',methods=['PUT'])
def update(name):
	ordered = [item for item in order_items if item['name']==name]
	ordered[0]['name'] = request.json['name']
	return jsonify({'item':ordered[0]})


if __name__ == '__main__':
	app.run(debug=True)