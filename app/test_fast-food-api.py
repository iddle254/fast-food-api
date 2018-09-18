from flask import Flask,jsonify
#imports pytest
import pytest
from app import app

#red test
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


