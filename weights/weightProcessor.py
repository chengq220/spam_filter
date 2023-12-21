import pandas as pd
import numpy as np
import csv

class preprocessor:
    def __init__(self):
        self.df = None
        self.label = None
        self.features = None
        self.spam_occurence = {}
        self.word_occurence = {}

    """Read csv file"""
    def read_csv(self, address):
        encoding_type = ['utf-8', 'latin-1', 'cp1252']
        for encoding in encoding_type:
            try:
                self.df = pd.read_csv(address, encoding=encoding)
                file_encoding = encoding
                break
            except UnicodeDecodeError:
                print(f"Failed to read with encoding: {encoding}")

    """Format the dataframe to desired shape"""
    def format(self, start_r = 0 , start_c = 0):
        self.df = self.df.iloc[:,:2]
        self.labels = pd.get_dummies(self.df.iloc[:,:1]).iloc[:,:1].to_numpy().squeeze()
        features = self.df.iloc[:,1:2].to_numpy().squeeze()
        for i in range(features.shape[0]):
            self.tokenizeCalc(features[i], self.labels[i])

    """Tokenize the feature and calculate its sample statistics"""
    def tokenizeCalc(self, feature, label):
        tokenize = feature.lower().split(' ')
        for i in tokenize:
            if(self.word_occurence.get(i, 0) == 0):
                if(not label):
                    self.spam_occurence[i] = 1
                self.word_occurence[i] = 1
            else:
                if(not label):
                    if self.spam_occurence.get(i,0) != 0:
                        self.spam_occurence[i] = self.spam_occurence[i] + 1
                    else:
                        self.spam_occurence[i] = 1

                self.word_occurence[i] = self.word_occurence[i] + 1

    """Return the weights for the dataset"""
    def getWeight(self):
        weight = {}
        for key in self.spam_occurence.keys():
            weight[key] = self.spam_occurence[key]/self.word_occurence[key]
        return weight

    """Export the weight as """
    def exportWeight(self):
        weight = self.getWeight()
        with open('weight.csv', 'w') as csvfile:
            writer = csv.writer(csvfile)
            for key, value in weight.items():
               writer.writerow([key, value])




p = preprocessor()
p.read_csv("dataset/spam.csv")
p.format()
p.exportWeight()
