import pandas as pd
import numpy as np
import os

class NaiveBayes:
    def __init__(self, weight_loc, threshold=0.5):
        self.weight, self.word_prob, self.spam_prob= self.getWeight(weight_loc)
        self.threshold = threshold

    """Initilialize the weights for the model"""
    def getWeight(self,address):
        weight = {}
        path = os.path.expanduser("~/spam_filter/weights/weight_pba.csv")
        df = pd.read_csv(path)
        key = df.iloc[:,0].to_numpy().squeeze()
        prob = df.iloc[:,1].to_numpy().squeeze()
        for i in range(key.shape[0]):
            weight[key[i]] = prob[i]

        word_prob = {}
        path = os.path.expanduser("~/spam_filter/weights/weight_pa.csv")
        df = pd.read_csv(path)
        key = df.iloc[:,0].to_numpy().squeeze()
        prob = df.iloc[:,1].to_numpy().squeeze()
        for i in range(key.shape[0]):
            word_prob[key[i]] = prob[i]

        path = os.path.expanduser("~/spam_filter/weights/weight_pb.txt")
        file = open(path, "r")
        spam_prob = float(file.read())

        return weight, word_prob, spam_prob


    def predict(self, feature):
        probability = 1
        tokenize = feature.lower().split(' ')

        itemProbNotSpam = 1
        for i in tokenize:
            #Bayes theorem
            #if the value does not exist in the weight, set it to 0.5 to show
            #that the model is unsure
            if(self.word_prob.get(i,0) == 0):
                itemProbSpam = 1
            else:
                itemProbSpam = (self.word_prob[i] * self.weight[i])
                itemProbNotSpam = itemProbNotSpam * (1 -self.word_prob[i]) * (1-self.weight[i])

            #The probability is the produt of all the probability of the word given
            #that it is a scam
            #
            probability = probability * itemProbSpam
        normalize = 0
        for i in range(2):
            if(i%2 == 0):
                normalize = normalize + self.spam_prob * probability
            else:
                normalize = normalize + (1 - self.spam_prob) * itemProbNotSpam
        probability = probability/normalize
        return probability >= self.threshold

if __name__ == "__main__":
    model = NaiveBayes("../weights")
    phrase = "I'll be going to school now"
    prediction = model.predict(phrase)
    print(prediction)
