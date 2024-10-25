from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import MultiplicationSerializer

class MultiplyView(APIView):
    def post(self, request):
        serializer = MultiplicationSerializer(data=request.data)
        if serializer.is_valid():
            value1 = serializer.validated_data['value1']
            value2 = serializer.validated_data['value2']
            result = value1 * value2
            return Response({'result': result}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)