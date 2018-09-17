from flask import Flask,jsonify
#imports pytest
import pytest

#creates an instance of flask
app = Flask(__name__)

#mock_data
order_items = []

#green
@app.route('/api/v1/orders',methods=['GET'])
def orders():	
	return jsonify({'order_items':order_items})

if __name__ == '__main__':
	app.run(debug=True)