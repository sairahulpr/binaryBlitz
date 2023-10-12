from django.views.decorators.csrf import csrf_exempt
from rest_framework.views import APIView
from rest_framework.response import Response

class Index(APIView):

    @csrf_exempt
    def post(self, request):
        return Response({'message': 'Got some data!'})