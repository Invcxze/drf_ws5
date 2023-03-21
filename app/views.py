from .serializers import *
from rest_framework.generics import *


class PetApiView(ListCreateAPIView):
    queryset = Pets.objects.all()
    serializer_class = PetSerializer


class SinglePetView(RetrieveUpdateDestroyAPIView):
    queryset = Pets.objects.all()
    serializer_class = PetSerializer


class OrderView(RetrieveUpdateDestroyAPIView):
    queryset = OrderOf.objects.all()
    serializer_class = OrderSerializer


class OrderApiView(ListCreateAPIView):
    queryset = OrderOf.objects.all()
    serializer_class = OrderSerializer
