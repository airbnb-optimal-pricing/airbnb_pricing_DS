Within the Notebooks directory in this repo you will find the following 4 folders: Analysis, Data Cleaning, Modeling and Web Scraping.

## In the Analysis folder you will find 2 files:

  •	The 1st file is an exploratory notebook in which we create an initial baseline model (Ridge Regression) by analyzing a small number of features (i.e: room type, bathrooms, bedrooms) that we intuitively deemed to explain a high degree of our model’s variance.

  •	The 2nd file showcases visualizations that were created using the Seaborn library, in which we looked for relationships between our model’s features in order to shed light into how our users could increase daily price listings by incorporating changes to their listings (for example, by increasing the number of amenities offered or by changing the bed type). 

## In the Data Cleaning folder you will find 2 files:

  •	In the 1st file we explore some of the features of our baseline model, such as the room type and bed type.

  •	In the 2nd notebook we create our Data Transformer function by implementing Sklearn’s One Hot Encoder on our categorical features and standardizing our numeric features by applying Sklearn’s StandardScaler, and finally predicting listing prices by using our baseline model (Ridge Regression) and testing it out on dummy values.

## In the Modeling folder you will find 5 files:: 

  •	In the 1st file a Random Forest model is run with 67 features in order to establish a 2nd naïve baseline model with an ensemble method to see if it outperformed our baseline Ridge Regression. Feature Importance is also applied in order to evaluate features that provide higher explainability in our model’s variance.

  •	In the 2nd file we apply our baseline model, the Ridge Regression. 

  •	In the 3rd file we mostly implement new features through Feature Engineering in order to attempt to increase our Coefficient of Determination’s score as well as create new features in order to aid us in creating new visualizations. Some of the features created were: ‘host since’, ‘host is superhost’, ‘requires phone verification’, ‘listing is instant bookable’, ‘requires guest profile picture’ and ‘host response rate.’

  •	In our 4th notebook we further our Ensemble models’ analysis by running a Random Forest Regressor with fewer features (notably features we gathered from our 1st notebooks’s most important features, as well as features we engineered in our 3rd exploratory notebook). Furthermore, we implemented a XGBRegressor and achieved a marginal MAE accuracy score improvement from our baseline model (not sufficient to justify a more complex model to be used, thus, settling for the initial Ridge Regression model).

  •	In our 5th file we explore the feasibility of applying seasonality to our data in order to reflect greater precision to our user’s listing prices given the time of the year; accomplished by implementing Pandas’ Datetime function and vanilla data wrangling.

## In the Web Scraping folder you will find 2 files:

  •	In our 1st file we perform web scraping by using BeautifulSoup to parse the HTML from our listing data, subsequently merging our data into 1 large dataframe, and ultimately deciding to solely concentrate on US cities’ listings.

  •	In our 2nd file we provide the final code used in our Flask API, from the get request for data retrieval in the insiderairbnb website and BeautifulSoup web scraping, to the concatenation and merging of our dataframe for US cities, into one large dataframe. 
