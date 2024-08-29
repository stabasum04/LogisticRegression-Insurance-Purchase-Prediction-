#data collection
import pandas as pd 
file=pd.read_csv("insurance_data.csv")

#spilt data into deature and target
from sklearn.model_selection import train_test_split
y=file.bought_insurance
x=file.drop(['bought_insurance'], axis=1)


#spilt into train and test data

from sklearn.model_selection import train_test_split
#size =0.2 means 80-20 ratio of training and testing
X_train, X_test, Y_train, Y_test = train_test_split(x, y, test_size=0.2)

#apply logistic regression model


from sklearn.linear_model import LogisticRegression
model = LogisticRegression()
model.fit(X_train,Y_train)


#prediction

y_predicted = model.predict(X_test)
score=model.score(X_test,Y_test)

print("The accuracy is :",score)

print("The coeff is",model.coef_)

print("The intercept is",model.intercept_)




import math
def sigmoid(x):
  return 1 / (1 + math.exp(-x))

age=float(input("Enter age: "))
def prediction_function(age):
    
    
    z = 0.042 * age - 1.53 # 0.04150133 ~ 0.042 and -1.52726963 ~ -1.53
    y = sigmoid(z)
    if (y>0.5):
        print("He/she will buy insurance")
    else:
        print("He/she wont buy insurance")


prediction_function(age)