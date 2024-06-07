from flask import Flask, request, jsonify

app = Flask(__name__)

# In-memory data storage (for simplicity)
data = []

# Route for GET request to retrieve all items
@app.route('/items', methods=['GET'])
def get_items():
    return jsonify(data)

# Route for POST request to create a new item
@app.route('/items', methods=['POST'])
def add_item():
    item = request.json
    data.append(item)
    return jsonify(item), 201

# Route for GET request to retrieve a single item by id
@app.route('/items/<int:item_id>', methods=['GET'])
def get_item(item_id):
    item = next((item for item in data if item['id'] == item_id), None)
    if item is None:
        return jsonify({'message': 'Item not found'}), 404
    return jsonify(item)

# Route for PUT request to update an item by id
@app.route('/items/<int:item_id>', methods=['PUT'])
def update_item(item_id):
    item = next((item for item in data if item['id'] == item_id), None)
    if item is None:
        return jsonify({'message': 'Item not found'}), 404
    updated_item = request.json
    item.update(updated_item)
    return jsonify(item)

# Route for DELETE request to delete an item by id
@app.route('/items/<int:item_id>', methods=['DELETE'])
def delete_item(item_id):
    global data
    data = [item for item in data if item['id'] != item_id]
    return '', 204

if __name__ == '__main__':
    app.run(debug=True)
