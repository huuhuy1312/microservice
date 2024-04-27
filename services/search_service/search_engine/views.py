from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import action
import requests


# Create your views here.
class SearchEngineViewSet(viewsets.ViewSet):

    @action(methods=["GET"], detail=False, url_path="search/(?P<keywords>.+)")
    def search(self, request, keywords=None):
        response = {
            "keywords": keywords,
            "results": [],
        }
        books = requests.get("http://localhost:8002/api/v1/books/").json()
        clothes = requests.get("http://localhost:8003/api/v1/clothes/").json()
        mobiles = requests.get("http://localhost:8004/api/v1/mobiles/").json()
        print(books)
        for book in books:
            if (
                keywords in str(book.get("name")).lower()
                or keywords in str(book.get("author")).lower()
                or keywords in str(book.get("description")).lower()
            ):
                response.get("results").append(book)

        for cloth in clothes:
            if (
                keywords in str(cloth.get("name")).lower()
                or keywords in str(cloth.get("brand")).lower()
                or keywords in str(cloth.get("description")).lower()
            ):
                response.get("results").append(cloth)

        for mobile in mobiles:
            if (
                keywords in str(mobile.get("name")).lower()
                or keywords in str(mobile.get("brand")).lower()
                or keywords in str(mobile.get("description")).lower()
            ):
                response.get("results").append(mobile)

        return Response(
            data=response, status=status.HTTP_200_OK, content_type="application/json"
        )
