from flask import Flask,jsonify
#imports pytest
import pytest
from app import app

#creates an instance of flask
app = Flask(__name__)

#red test
def test_orders():
	#test to see if orders returns all the orders	
    result=app.test_client()
    response= result.get('/api/v1/orders',content_type='application/json')
    assert(response.status_code==200)


if __name__ == '__main__':
	app.run(debug=True)