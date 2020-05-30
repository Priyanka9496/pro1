from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from profile_api import serializers
from rest_framework import viewsets


class HelloApiView(APIView):
    serializer_class=serializers.HelloSerializer


    def get(self,request,format=None):

        an_apiview=[
            'Uses HTTP methods as function(get,post,patch,put,delete)',
            'Is similar to traditional Django View',
            'Gives th most control over you application logic',
            'Is mapped manually to URLs'
        ]
        return Response({'message':'Hello!','an_apiview':an_apiview})


    def post(self,request):
        serializer=self.serializer_class(data=request.data)

        if serializer.is_valid():
            name=serializer.validated_data.get('name')
            message=f'Hello {name}'
            return Response({'message':message})

        else:
            return Response(serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
            )


    def put(self,request,pk=None):
        return Response({'method':'PUT'})


    def patch(self,request,pk=None):
        return Response({'method':'PATCH'})

    def delete(self,request,pk=None):
        return Response({'method':'DELETE'})

class HelloViewSet(viewsets.ViewSet):

    serializer_class=serializers.HelloSerializer

    def list(self,request):
        a_viewset=[
            'uses actions(list,create,retrive,update,destroy)',
            'automatically maps to urls using routers',
            'Provides more functonality with less code',
        ]


        return Response({'messgae':'Hello!','a_viewset':a_viewset})


    def create(self,request):
        serializer=self.serializer_class(data=request.data)
        if serializer.is_valid():
            name=serializer.validated_data.get('name')
            message=f'Hello {name}'
            return Response({'message':message})

        else:
            return Response(serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
            )


    def retrive(self,request,pk=None):
        return Response({'http_method':'GET'})

    def update(self,request,pk=None):
        return Response({'http_method':'PUT'})

    def partial_update(self,request,pk=None):
        return Response({'http_method':'PATCH'})

    def destroy(self,request,pk=None):
        return Response({'http_method':'DELETE'})
