from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

@api_view(['POST'])
def handlePredict(request):
    if(request.method == 'POST'):
        print("received post request")
        prediction = True
        if(prediction):
            return Response(1)
        else:
            return Response(0)
