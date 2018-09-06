from flask import Flask,jsonify
#imports pytest
import pytest

#creates an instance of flask
app = Flask(__name__)

#mock_data
order_items = [{'name':'pizza'},{'name':'steak'},{'name':'rice'},{'name':'Fries'}]


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

if __name__ == '__main__':
	app.run(debug=True)