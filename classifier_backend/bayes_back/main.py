from sklearn.model_selection import train_test_split
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from weights.weightProcessor import preprocessor, read_csv
from model.BayesClassifier import NaiveBayes



#load the dataset
df = read_csv("dataset/spam.csv")
X = df.iloc[:,1]
y = df.iloc[:,0]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

if(False):
    weightProcessor = preprocessor()
    weightProcessor.formatDF(X_train,y_train)

#convert to numpy array for better random access
X_test = X_test.to_numpy()
y_test = y_test.to_numpy()

#Test the model
model = NaiveBayes("weights",threshold = 0.5)
tp = 0
fp = 0
tn = 0
fn = 0

for i in range(X_test.shape[0]):
    pred = model.predict(X_test[i])
    if(pred == True and y_test[i] == "spam"):
        tp = tp + 1
    elif(pred == False and y_test[i] == "ham"):
        tn = tn + 1
    elif(pred == True and y_test[i] == "ham"):
        fp = fp + 1
    else:
        fn = fn + 1

precision = tp / (tp + fp)
recall = tp/ (tp + fn)
f1 = (2 * precision * recall) / (precision + recall)
accuracy = (tp + tn) / (tp + fp + tn + fp)
print("F1 Score: ", f1)
print("Accuracy: ", accuracy)
