from rest_framework import serializers
from .models import employee

class employeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = employee
       # feilds = ('firstname', 'lastname')
        fields = '__all__'

    def __str__(self):
        return self.name