from flask import Flask,jsonify,json

#creates an instance of flask
app = Flask(__name__)

#mock_data
order_items = []		
#green
@app.route('/api/v1/orders',methods=['GET'])
def orders():	
	return jsonify({'order_items':order_items})

#green 
@app.route('/api/v1/order/<string:name>',methods=['GET'])
def order(name):
	ordered = [item for item in order_items if item['name']==name]
	return jsonify({'item':ordered[0]})

#green
@app.route('/api/v1/order/<string:name>',methods=['PUT'])
def update(name):
	ordered = [item for item in order_items if item['name']==name]
	ordered[0]['name'] = request.json['name']
	return jsonify({'item':ordered[0]})

if __name__ == '__main__':
	app.run(debug=True)