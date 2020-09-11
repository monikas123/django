from rest_framework import serializers

from .models import contact

class ContactSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = contact
        fields = ('name', 'email')