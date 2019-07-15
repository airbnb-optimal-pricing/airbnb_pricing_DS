from flask import Flask, request
from flask_json import FlaskJSON, JsonError, json_response
import os
import requests
from predict import get_prediction, get_simp_prediction
from flask_cors import CORS
from flask_swagger_ui import get_swaggerui_blueprint


application = app = Flask(__name__)
FlaskJSON(app)
cors = CORS(app)


#----------- Swagger ------------#
@app.route('/static/<path:path>')
def send_static(path):
  return send_from_directory('static', path)

#----------- Test Route -----------#
@app.route('/')
def root():
    """
    Testing 
    """
    return "Test Successful"	

#-----------Full Prediction---------#    
@app.route('/prediction', methods=['POST'])
def get_all_predictions():
  """
  Gets predicted price of Airbnb unit given selected inputs.

  Inputs:
    1. Zipcode
    2. Property Type
    3. Room Type
    4. How many people the unit accommadates
    5. Number of Bathrooms
    6. Number of Bedrooms
    7. Number of Beds
    8. Type of Bed
  
  Outputs:
    1. Predicted Price
  """
  data = request.get_json(force=True)
  print(data)

  zipcode = data['zipcode']
  property_type = data['property_type']
  room_type = data['room_type']
  accommodates = data['accommodates']
  bathrooms = data['bathrooms']
  bedrooms = data['bedrooms']
  beds = data['beds']
  bed_type = data['bed_type']

  result = get_prediction(zipcode=zipcode, property_type=property_type, room_type=room_type,
                          accommodates=accommodates, bathrooms=bathrooms, bedrooms=bedrooms,
                          beds=beds, bed_type=bed_type)

  return json_response(prediction=result)

if __name__ == '__main__':
    application.run()
    