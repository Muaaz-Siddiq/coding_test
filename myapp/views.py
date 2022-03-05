from django.http.response import HttpResponse, JsonResponse
from django.shortcuts import render
from rest_framework.response import Response
from .models import *
from .serializer import *
from rest_framework import viewsets
from rest_framework import generics,mixins

class Customer_feedback(viewsets.ModelViewSet):
    serializer_class = feedBack_serializer
    queryset = Customer_FeedBack.objects.all()

class filter_topic(viewsets.GenericViewSet,mixins.ListModelMixin):
    queryset = Customer_FeedBack.objects.all()
    serializer_class = feedBack_serializer
    def retrieve(self, request, *args, **kwargs):
        params = kwargs
        filter_topic = Customer_FeedBack.objects.filter(topic=params['pk'])
        serializer = feedBack_serializer(filter_topic, many=True)
        if serializer.data:
            return Response(serializer.data)
        else: 
            return Response({"response:":"No Data Found"})
