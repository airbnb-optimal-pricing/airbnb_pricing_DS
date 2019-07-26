from flask import Flask, request
from flask_json import FlaskJSON, JsonError, json_response
import os
import requests
from flask_cors import CORS
# from flask_swagger_ui import get_swaggerui_blueprint
from threading import Thread, Event, Lock
import atexit
import json

# Inner imports
from data_retrieval import data_retrieval
from data_cleaning import data_cleaning
from training import training
from predict import load_pickle_files, get_prediction
from plot import zip_list


class RecurringThread(Thread):

    def __init__(self, event):
        Thread.__init__(self)
        self.stopped = event

    def run(self):
        POOL_TIME = 86400  # Seconds
        while not self.stopped.wait(POOL_TIME):
            # call load function
            load_model()


application = app = Flask(__name__)
FlaskJSON(app)
cors = CORS(app)

# Lock to control access to variable
dataLock = Lock()


# Data loading and training sequence
def load_model():
    data_retrieval()
    data_cleaning()
    training()
    with dataLock:
        load_pickle_files()


# Stop thread at exit
def interrupt():
    stopFlag.set()

# ----------- Swagger ------------ #
# @app.route('/static/<path:path>')
# def send_static(path):
#     return send_from_directory('static', path)

# ----------- Test Route ----------- #
@app.route('/')
def root():
    """
    Testing
    """
    return "Test Successful"

# -----------Full Prediction--------- #
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

    zipcode = data['zipcode']
    property_type = data['property_type']
    room_type = data['room_type']
    accommodates = data['accommodates']
    bathrooms = data['bathrooms']
    bedrooms = data['bedrooms']
    beds = data['beds']
    bed_type = data['bed_type']

    with dataLock:
        result = get_prediction(zipcode=zipcode,
                                property_type=property_type,
                                room_type=room_type,
                                accommodates=accommodates,
                                bathrooms=bathrooms,
                                bedrooms=bedrooms,
                                beds=beds,
                                bed_type=bed_type)


        plot_values, bins = zip_list(zipcode=zipcode)

        plot_values = [int(i) for i in plot_values]

    return json_response(prediction=result,
                         plot_values=plot_values,
                         bins=bins)

if __name__ == '__main__':

    # Threading related
    # Lock to control access to variable
    #dataLock = Lock()

    # Load model
    #load_model()


    # TEMPORARY --------------------
    with dataLock:
        load_pickle_files()

    # Start thread
    stopFlag = Event()
    load_thread = RecurringThread(stopFlag)
    load_thread.start()

    # When you kill Flask (SIGTERM), clear the trigger for the next thread
    atexit.register(interrupt)

    application.run()
