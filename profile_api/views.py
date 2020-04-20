from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from profile_api import serializers
from rest_framework import viewsets

# Create your views here.

class HelloApiView(APIView):
    """Test API View"""
    serializer_class = serializers.HelloSerializer
    def get(self,request,fromat=None):
        """Returns list of API VIew features"""
        an_apiview = [
            'Uses HTTP methods as function(get,post,patch,put,delete)',
            'Is similar to traditional Django View',
            'Gives you the most control over you application logic',
            'Is mapped manually to URL',
        ]

        return Response({'message':'Hello','an_apiview':an_apiview})

    def post(self,request):
        """Create a hello message with name"""
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}'
            return Response({'message':message})

        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk=None):
        """Handle Updating object"""
        return Response({'method':'PUT'})


    def patch(self,request,pk=None):
        """Handle a partial update of object"""
        return Response({'method':'PATCH'})


    def delete(self,request,pk=None):
        """Delete an object in database"""
        return Response({'method':'DELETE'})


class HelloViewSet(viewsets.ViewSet):
    """Test API Viewset"""
    serializer_class = serializers.HelloSerializer
    def list(self, request):
        """Return Hello Message"""
        a_viewset = [
        'Uses Actions (list, create, retrieve, update, partial update)',
        'Automatically maps to URLs using Routers',
        'Provides more functionality with less code',
        ]

        return Response({'message':'Hello', 'a_viewset':a_viewset})


    def create(self, request):
        """Create a new Hello message"""
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message  = f'Hello {name}!'
            return Response({'message':message})

        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    def retrieve(self, request, pk=None):
        """Handle getting object by ID"""
        return Response({'http_method':'GET'})

    def update(self, request, pk=None):
        """Handle updating an object"""
        return Response({'http_method':'PUT'})

    def partial_update(self,request,pk=None):
        """Handle update part of an object"""
        return Response({'http_method':'PATCH'})

    def destroy(self,request, pk=None):
        """Handle Removing an object"""
        return Response({'http_method':'DELETE'})
