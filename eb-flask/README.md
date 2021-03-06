# Flask API
## Usage
Clone the repo:<br>
```git clone https://github.com/airbnb-optimal-pricing/airbnb_pricing_DS``` <br>
```cd eb-flask```

Create virtualenv:<br>
```virtualenv virt``` <br>
```source virt/bin/activate``` <br>
```pip install -r requirements.txt``` 

Run the server locally <br>
```python application.py```

Try the endpoints:  <br>
```Post Request```
```http://127.0.0.1:5000/prediction```

Sample request and response:

![](../pictures/request.png)

![](../pictures/response.png)


## Files
### data_retrieval.py
Web scraper that extracts all the U.S. data at [insideairbnb.com](http://insideairbnb.com/get-the-data.html). Data is consolidated into a pandas dataframe and reduced to contain the columns with highest feature importances.

### data_cleaning.py
Data cleaning file for zip code and price columns.

### training.py
Model traning file on cleaned data. After testing a multitude of models, a simple ridge regression model minimized our median squared error to an acceptable level. Reference our [modeling notebooks](https://github.com/airbnb-optimal-pricing/airbnb_pricing_DS/tree/master/notebooks/Modeling) for a more in depth analysis.

### predict.py
Prediction algorithm for incoming data.

### plot.py
Returns array containing number of units for a given dollar range in a users inputted zip code. Data is displayed via plotly graph on front end. 

### application.py
Flask API Logic. Recurrent time-based reinitialization can be set via the POOL_TIME variable. 
