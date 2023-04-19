from rest_framework.generics import CreateAPIView
from rest_framework.views import APIView, Response

from .serilizers import TwoSumSerializer, ContactFormSerializer


class TwoSumAPIView(APIView):
    """
    API view for calculating the sum of two integers.

    POST method accepts two integer values and returns their sum.

    serializer_class: Serializer class to serialize and validate request data.

    Example request:
    {
        "num1": 5,
        "num2": 10
    }

    Example response:
    {
        "sum": 15
    }
    """
    serializer_class = TwoSumSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        response = {"sum": serializer.get_sum(serializer.validated_data)}
        return Response(data=response)


class ContactCreateAPIView(CreateAPIView):
    """
    API view for creating a new contact.

    POST method accepts contact form data and creates a new contact.

    serializer_class: Serializer class to serialize and validate contact form data.

    Example request:
    {
        "first_name": "Mohammad",
        "last_name" : "Azimi" ,
        "phone_number" : "09212518775" ,
        "email": "Mohammad.azimi.1996@gmail.com",
        "message": "Hello ! it is mazimi !"
    }

    Example response:
    {
        "id": 1,
        "first_name": "Mohammad",
        "last_name" : "Azimi" ,
        "phone_number" : "09212518775" ,
        "email": "Mohammad.azimi.1996@gmail.com",
        "message": "Hello ! it is mazimi !"
    }
    """
    serializer_class = ContactFormSerializer
