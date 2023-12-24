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
        self.spam_total = 0
        self.total = 0

    """Read from CSV file and format the dataframe to desired shape"""
    def formatFromCSV(self, address, start_r = 0 , start_c = 0):
        self.df = read_csv(address)
        self.df = self.df.iloc[:,:2]
        self.labels = pd.get_dummies(self.df.iloc[:,:1]).iloc[:,:1].to_numpy().squeeze()
        features = self.df.iloc[:,1:2].to_numpy().squeeze()
        self.total = features.shape[0]
        for i in range(self.total):
            self.tokenizeCalc(features[i], self.labels[i])
        # print(self.spam_total)
        self.spam_total = self.spam_total/self.total

    """Read from CSV file and format the dataframe to desired shape"""
    def formatDF(self, x_df, y_df):
        labels = pd.get_dummies(y_df).iloc[:,:1].to_numpy().squeeze()
        features = x_df.to_numpy().squeeze()
        self.total = features.shape[0]
        for i in range(self.total):
            self.tokenizeCalc(features[i], labels[i])
        # print(self.spam_total)
        self.spam_total = self.spam_total/self.total

    """Tokenize the feature and calculate its sample statistics"""
    def tokenizeCalc(self, feature, label):
        tokenize = feature.lower().split(' ')
        if not label:
            self.spam_total = self.spam_total + 1
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
    def getWeights(self):
        pba = {}
        pa = {}
        for key in self.spam_occurence.keys():
            pba[key] = self.spam_occurence[key]/self.word_occurence[key]
            pa[key] = self.word_occurence[key]/self.total
        return pba, pa, self.spam_total

    """Export the weight as csv and txt files"""
    def exportWeights(self):
        pba, pa, pb = self.getWeights()
        with open('weight_pba.csv', 'w') as csvfile:
            writer = csv.writer(csvfile)
            for key, value in pba.items():
               writer.writerow([key, value])
        with open('weight_pa.csv', 'w') as csvfile:
            writer = csv.writer(csvfile)
            for key, value in pa.items():
               writer.writerow([key, value])
        with open('weight_pb.txt', 'w') as file:
            writer = csv.writer(file)
            writer.writerow([pb])

"""Read csv file"""
def read_csv(address):
    encoding_type = ['utf-8', 'latin-1', 'cp1252']
    for encoding in encoding_type:
        try:
            df = pd.read_csv(address, encoding=encoding)
            file_encoding = encoding
            return df
        except UnicodeDecodeError:
            print(f"Failed to read with encoding: {encoding}")

if __name__ == "__main__":
    p = preprocessor()
    p.format("../dataset/spam.csv")
    p.exportWeights()
