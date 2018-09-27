from flask import Flask,jsonify,json,request
#imports pytest
import pytest

order_items=[]
item_to_be_added = {'name':'ugali'}
#red testa
def test_orders():
	#test to see if orders returns all the orders	
    result=app.test_client()
    response= result.get('/api/v1/orders',content_type='application/json')
    assert(response.status_code==200)
    

#test to see if only one order is returned
def test_order():		
    result=app.test_client()
    response= result.get('/api/v1/orders',content_type='application/json')
    assert(response.status_code==200)

#red test
def test_new_order():
	#test to see if a new order is created
	result=app.test_client()
	no_orders=len(order_items)
	response= result.post('/api/v1/orders', data=json.dumps(item_to_be_added) ,content_type='application/json')
	data=json.loads(response.data)
	no_new_orders = len (data)+no_orders    
	assert no_orders + 1 == no_new_orders
	assert(response.status_code==200)
#red test
def test_update():	
	#test to see if the order updates
    result=app.test_client()
    response= result.put('/api/v1/order', data=json.dumps(item_to_be_added) ,content_type='application/json')
    assert(response.status_code==404)


