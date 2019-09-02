# Flask API
## Usage
Clone the repo:
    git clone https://github.com/airbnb-optimal-pricing/airbnb_pricing_DS/tree/master/eb-flask
    cd eb-flask

Create virtualenv:
    vertualenv virt
    source virt/bin/activate
    pip install -r requirements.txt

Run the server locally
    python.application.py

Try the endpoints:
    curl -XPOST -H "Content-Type: application/json" http://localhost:5000/prediction -d '{"zipcode": "90210",
                                                                                          "property_type": "Villa",
                                                                                          "room_type" : "Private room",
                                                                                          "accommodates": 5,
                                                                                          "bathrooms": 12,
                                                                                          "bedrooms": 2,
                                                                                          "beds": 2,
                                                                                          "bed_type": "Real Bed"
                                                                                          }'

## Files
### data_retrieval
Web scraper that extracts all the U.S. data at [insideairbnb.com](http://insideairbnb.com/get-the-data.html). Data is consolidated into a pandas dataframe and reduced to contain the columns with highest feature importances.

### data_cleaning
Data cleaning file for zip code and price columns.

### training
Model traning file on cleaned data. After testing a multitude of models, a simple ridge regression model minimized our median squared error to an acceptable level. Reference our [modeling notebooks](https://github.com/airbnb-optimal-pricing/airbnb_pricing_DS/tree/master/notebooks/Modeling) for a more in depth analysis.

### predict
Prediction function used for incoming data.

### plot
Returns array containing number of units for a given dollar range in a users inputted zip code. Data is displayed via plotly graph on front end. 

### application
Flask API Logic.
