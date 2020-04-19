from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from profile_api import serializers
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
