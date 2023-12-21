import pandas as pd
import numpy as np

class NaiveBayes:
    def __init__(self, weight_loc, threshold=0.5):
        self.weight = self.getWeight(weight_loc) #P(Spam | word)
        self.spam_prob = 1 #Probability of spam
        self.word_prob = 1 #The probability that that the word shows up
        self.threshold = threshold

    def getWeight(self,address):
        weight = {}
        df = pd.read_csv(address)
        key = df.iloc[:,0].to_numpy().squeeze()
        prob = df.iloc[:,1].to_numpy().squeeze()
        for i in range(key.shape[0]):
            weight[key[i]] = prob[i]
        return weight


    def predict(self,feature):
        probability = 1
        tokenize = feature.lower().split(' ')
        for i in tokenize:
            item_prob = (self.spam_prob * self.weight.get(i,1)) / self.word_prob.get(i,1)
            #if the value does not exist in the weight, set it to 0.5 to show
            #that the model is unsure
            probability = probability * item_prob
        print(probability)
        print(self.threshold/len(tokenize))
        return probability >= self.threshold/len(tokenize)

model = NaiveBayes("../weight/weights.csv")
phrase = "You win 5000 dollars. Claim it by friday"
model.predict(phrase)
