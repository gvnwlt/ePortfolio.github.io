# linear regression on mongodb stock market data using machine learning and a restful api 
# Predict: Profit Margin given (ROA, IT, SG, and SR) 
# schema of stock companies containing roughly 78 different factors of the company ranging from the Ticker symbol to the 50-day moving average. The plan for extracting the data goes as follows:
#  1. select a variable of interest that will be used for prediction.
#  2. select potential predictors that will be used to train a linear model that 
#  will predict the feature of interest.
#  3. use the function framework created with pymongo and the restful api to extract data to be used
#  in a sample that will train the model 
#  4. prepprocess the data and train the model 
#  5. use the trained model as a function that can recieve an input on suitable predictors and 
#  make a fairly good prediction on the outcome.  
# package: 
#  "Profit Margin", 
#  "Return on Assests", 
#  "Insider Transactions", 
#  "Short Ratio"    
 

# scikitlearn in baked into monogdb 
from pandas.io.json import json_normalize 
from pymongo import MongoClient 
from sklearn import linear_model 
from sklearn.model_selection import train_test_split
import numpy as np  
import seaborn as sns 
import matplotlib as plt
import pickle 

# extract data from all documents in collection for features of interest
# use the bottle framework to "unpickle" the model at server startup and call
# the "predict_profit_margin" function in an HTTP request handler

uri = "localhost', 2017" 
connection_client = MongoClient(uri) 

# market is the db and stocks is the collection
market_db = connection_client['market']['stocks']

#  "Profit Margin", 
#  "Return on Assests", 
#  "Insider Transactions", 
#  "Short Ratio"             

# project (display) values
projection = {
        "$projection": {
                "_id" : 0,
                "Profit Margin": 1,
                "Retrun on Assets": 1,
                "Insider Transactions": 1,
                "Short Ration": 1,
        }
}

# get a sample from the database of 10000 documents 
sample_stage = { "$sample" : { "size" : 50 } }

# pass the stages to db aggregate command to get cursor 
cursor = market_db.aggregate({
        projection,
        sample_stage
})

# exhaust (extract from) the cursor and store in market data as a list (array) 
market_data = list(cursor)

# show example of one of the documents
market_data[0]

# marshall into dataframe
df = json_normalize(market_data)

# check out the dataframe
df.head()

# enables seaborn to use its graphs 
# matplotlib


# use pairwise comparisons against every variable -- for visualization  
# use these pair plots to see what has a good linear correlation 
# sns.pairplot(df)

# drop out profit margin from the margin  
df_x = df.drop(['Profit Margin'], axis=1)

# create another dataframe that just has Profit Margin 
df_y = df['Profit Margin']

# the regressor -- uses order least squares model from scikit learn 
reg = linear_model.LinearRegression()

# split into test and train datasets with 80% train 20% test 
x_train, x_test, y_train, y_test = train_test_split(df_x, df_y, test_size=0.2)

# fit the model
reg.fit(x_train, y_train)

# calculate weights used to predict the Profit Margin 
# look at coefficients here 
reg.coef_

# check out the intercept 
reg.intercept_

# make the prediction 
reg.predict(x_test)

# analyze the results -- get the mean squared error (given predictors how 
# much will they be off)   
np.mean((reg.predict(x_test) - y_test)**2)

# pickle and export the model out (serialize) to use as a function in restful api  
with open("regressionmodel.pickle", "wb") as modelfile:
  pickle.dump(reg, modelfile)
  
