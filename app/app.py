from flask import Flask,jsonify,json,request

#creates an instance of flask
app = Flask(__name__)

#mock_data
order_items = []
item_to_be_added = {'name':'ugali'}		
#green
@app.route('/api/v1/orders',methods=['GET'])
def orders():	
	return jsonify({'order_items':order_items})

#green 
@app.route('/api/v1/orders/<string:name>',methods=['GET'])
def order(name):
	ordered = [item for item in order_items if item['name']==name]
	return jsonify({'item':ordered[0]})

@app.route('/api/v1/orders',methods=['POST'])
def new_order():	     
	item = {'name':request.json['name']}
	order_items.append(item)
	return jsonify({'order_items':order_items})

#green
@app.route('/api/v1/orders/<string:name>',methods=['PUT'])
def update(name):
	ordered = [item for item in order_items if item['name']==name]
	ordered[0]['name'] = request.json['name']
	return jsonify({'item':ordered[0]})

if __name__ == '__main__':
	app.run(debug=True)