from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import bookPurchased
from .serializers import bookPurchasedSerializer
import json
import requests

# Create your views here.

@api_view(['GET'])
def getPurchasedBooks(request):
    booksPurchased = bookPurchased.objects.all()
    serializer = bookPurchasedSerializer(booksPurchased, many=True)
    return Response(serializer.data)
    
@api_view(['GET'])
def getBooksDetails(request, *args, **kwargs):
    nameSelected = kwargs.get('bookName', None)
    print(nameSelected)
    bookD = requests.get('http://127.0.0.1:9001/bookInformation/bookN/%s' % nameSelected).json()
    print(bookD)

    return Response(bookD)

@api_view(['Post'])
def purchaseBook(request):
    serializer = bookPurchasedSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)
