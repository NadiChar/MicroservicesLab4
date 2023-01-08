from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import bookList
from .serializers import bookListSerializer
import json

@api_view(['GET'])
def getBooks(request):
    books = bookList.objects.all()
    serializer = bookListSerializer(books, many=True)

    return Response(serializer.data)
    
@api_view(['GET'])
def getBookByID(request, *args, **kwargs):
    idSelected = kwargs.get('id', None)
    print(idSelected)
    try:
        selectedID =bookList.objects.get(id=idSelected)
        print(selectedID)
        serializer = bookListSerializer(selectedID, many=False)
        print(serializer.data)

        return Response(serializer.data)
    except:
        return Response({"message" : "Book does not exist!"})

@api_view(['GET'])
def getBookByName(request, *args, **kwargs):
    idSelected = kwargs.get('bookName', None)
    print("check this ", idSelected)
    try:
        selectedID =bookList.objects.get(bookName=idSelected)
        print(selectedID)
        serializer = bookListSerializer(selectedID, many=False)
        print(serializer.data)

        return Response(serializer.data)
    except:
        return Response({"message" : "Book does not exist!"})

@api_view(['POST'])
def addBook(request):
    serializer = bookListSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)
    
