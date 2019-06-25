from flask import Flask, request
from flask_json import FlaskJSON, JsonError, json_response
import os
import psycopg2 as pg
import requests
from .predict import get_prediction

app = Flask(__name__)
FlaskJSON(app)
cors = CORS(app)


@app.route('/')
def root():
    """
    Testing 
    """
    return "Test Successful"	
    
@app.route('/allpredictions', methods=['POST'])
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
  try:
    zipcode = data['zipcode']
    property_type = data['property_type']
    room_type = data['room_type']
    accommodates = data['accommodates']
    bathrooms = data['bathrooms']
    bedrooms = data['bedrooms']
    beds = data['beds']
    bed_type = data['bed_type']
    except (KeyError):
      raise JsonError(description='Key Error: Key missing in the request')

    result = get_prediction()

  return json_response(prediction=result)


if __name__ == '__main__':
    application.run()