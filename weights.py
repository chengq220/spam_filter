import numpy as np
import pandas as pd


class preprocessor:
    def __init__(self):
        self.df = None
        self.label = None
        self.features = None

    #read the csv file
    def read_csv(self, address):
        encoding_type = ['utf-8', 'latin-1', 'cp1252']
        for encoding in encoding_type:
            try:
                self.df = pd.read_csv(address, encoding=encoding)
                file_encoding = encoding
                break
            except UnicodeDecodeError:
                print(f"Failed to read with encoding: {encoding}")

    #format the dataframe to desired shape
    def format(self, start_r = 0 , start_c = 0):
        self.df = self.df.iloc[:,:2]
        self.labels = pd.get_dummies(self.df.iloc[:,:1]).iloc[:,:1].to_numpy()
        # print(labels)
        self.features = self.df.iloc[:,1:2].to_numpy()
        self.__process_features()

    #change all the labels into numerical values and
    #process the features into array of individual words
    def __process_features(self):
         # labels = pd.get_dummies(self.labels)
         # self.labels = labels[:,0]
         print(self.labels.shape)
         print(self.features.shape)


    #return the first n elements in the numpy dataset
    def get_top(self, n = 1):
        return self.labels[:n], self.features[:n]




p = preprocessor()
p.read_csv("dataset/spam.csv")
p.format(start_c = 1)
a, b = p.get_top(2)
# print(p.labels)
