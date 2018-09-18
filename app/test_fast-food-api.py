from flask import Flask,jsonify,json
#imports pytest
import pytest
from app import app

item_to_be_added={"ugali":"choma"}
#red testa
def test_orders():
	#test to see if orders returns all the orders	
    result=app.test_client()
    response= result.get('/api/v1/orders',content_type='application/json')
    assert(response.status_code==200)

#test to see if only one order is returned
def test_order():		
    result=app.test_client()
    response= result.get('/api/v1/order',content_type='application/json')
    assert(response.status_code==404)

#red test
def test_update():	
	#test to see if the order updates
    result=app.test_client()
    response= result.put('/api/v1/order', data=json.dumps(item_to_be_added) ,content_type='application/json')
    assert(response.status_code==404)


