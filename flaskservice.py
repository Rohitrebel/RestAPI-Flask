from flask import Flask, request, jsonify

app = Flask(__name__)

persondetails = []

@app.route('/', methods=['GET'])
def display_form():
  return jsonify({"message": "Hello There! Do API Testing using Postman"})


@app.route('/persondetails', methods=['GET'])
def get_person_details():
  return jsonify(persondetails)

@app.route('/persondetails/<int:index>', methods=['GET'])
def get_person_by_index(index):
    if index < len(persondetails) and index >= 0:
        return jsonify(persondetails[index])
    else:
        return jsonify({"message": "Index out of range"}), 400


@app.route('/postdata', methods=['POST'])
def post_data():
  data = request.get_json()
  persondetails.append(data)
  return jsonify({"message": "Data added Successfully"}), 201

@app.route('/putdata', methods=['PUT'])
def put_data():
  global persondetails
  persondetails = [request.get_json()]
  return jsonify({"message": "data replaced successfully"}), 202

@app.route('/putdata/<int:index>', methods=['PUT'])
def put_data_index(index):
  global persondetails
  if index >= 0 and index < len(persondetails):
    if request.get_json():
      persondetails[index] = request.get_json()
    else:
      return jsonify({"message": "Data invalid"}), 400  
    return jsonify({"message": f"Data at index {index} replaced successfully"}), 202
  else:
    return jsonify({"message": "Data doesn't exist at that index"}), 400
  

@app.route('/deletedata/<int:index>', methods=['DELETE'])
def delete_data_index(index):
  if index >= 0 and index < len(persondetails):
    del persondetails[index]
    return jsonify({"message": f"Data deleted at index {index}"}), 202
  else:
    return jsonify({"message": "Data doesn't exist at that index"}), 400

@app.route('/deletedata', methods=['DELETE'])
def delete_data():
  global persondetails
  persondetails = []
  return jsonify({"message": "Data deleted"}), 202
  

if (__name__ == '__main__'):
  app.run(debug=True)