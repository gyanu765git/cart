from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
# Create your views here.

class HomeView(APIView):

    @staticmethod
    def get(request):
        return Response({"success":True, "message":"Welcome to home page", "data":[]}, status=status.HTTP_200_OK)