from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from bayes_back.apps import BayesBackConfig

@api_view(['POST'])
def handlePredict(request):
    if(request.method == 'POST'):
        print("received post request")
        input = list(request.data.keys())[0]
        # print(list(request.data.keys())[0])
        bayes_pred = BayesBackConfig.MODEL.predict(input)
        print("prediction: ", bayes_pred)
        if(bayes_pred):
            return Response(1)
        else:
            return Response(0)
