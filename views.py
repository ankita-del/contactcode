from rest_framework import generics
from .models import ContactDetails
from .serializers import ContactDetailsSerializer

class ContactDetailsList(generics.ListAPIView):
    queryset = ContactDetails.objects.all()
    serializer_class = ContactDetailsSerializer
