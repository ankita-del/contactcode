from rest_framework import serializers
from .models import ContactDetails, Interest

class InterestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Interest
        fields = ['interest']

class ContactDetailsSerializer(serializers.ModelSerializer):
    interests = InterestSerializer(source='interest_set', many=True)

    class Meta:
        model = ContactDetails
        fields = ['phone', 'first_name', 'last_name', 'designation', 'email', 'interests']
