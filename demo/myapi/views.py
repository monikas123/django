# views.py
from rest_framework import viewsets

from .serializers import ContactSerializer
from .models import contact


class ContactViewSet(viewsets.ModelViewSet):
    queryset = contact.objects.all().order_by('name')
    serializer_class = ContactSerializer