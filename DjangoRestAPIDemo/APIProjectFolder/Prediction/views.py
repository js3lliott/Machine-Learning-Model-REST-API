from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView

# Create your views here.
@api_view(['GET', 'POST'])
def api_add(request):
    sum = 0
    response_dict = {}
    if request.method == 'GET':
        # Do nothing
        pass
    elif request.method == 'POST':
        # Add the numbers 
        data = request.data
        for key in data:
            sum += data[key]
        response_dict = {'sum': sum}
    return Response(response_dict, status=status.HTTP_201_CREATED)

# Class based view to add numbers
class Add_Values(APIView):
    def post(self, request, format=None):
        sum = 0
        # Add the numbers
        data = request.data
        for key in data:
            sum += data[key]
        response_dict = {"sum": sum}
        return Response(response_dict, status=status.HTTP_201_CREATED)