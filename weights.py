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
        features = self.df.iloc[:,1:2]
        self.features = self.__tokenize_features(features)

    #tokenize the features using space tokenization
    def __tokenize_features(self, features):
        features = features['v2'].str.lower().str.split(' ').to_numpy()
        return features

    #Take the simple approach and just take the product of whether a
    #text message contains the keyword (without regard to the frequency of such)
    #word in the text
    def calc_weights(self):
        ## TODO: think of a way to efficiently process all the list and
        ##       and to store the different element and its probability
        dict = {}
        for i,feature in enumerate(self.features):
            label = self.labels[i]
            print(np.unique(feature).shape)
            print(label)
            break

    def forward(self, address):
        self.read_csv(address)
        self.format()
        self.calc_weights()
        # return weight


    #return the first n elements in the numpy dataset
    def get_top(self, n = 1):
        return self.labels[:n], self.features[:n]




p = preprocessor()
p.forward("dataset/spam.csv")
a, b = p.get_top(2)
# print(p.labels)
