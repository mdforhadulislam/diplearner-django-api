from rest_framework.response import Response
from rest_framework import status


def respons_setup(message: str, data: any, statuss: int):
    return Response({
        'messsage': message,
        'data': data,
        'status': statuss
    }, status.HTTP_200_OK)
