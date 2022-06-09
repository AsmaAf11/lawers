from rest_framework import serializers
from .models import lawyer, consultation, consultation_request, payment
from django.contrib.auth.models import User


class LawyerSerializerView(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email', 'contract_speciality']


class lawyersSerializerView(serializers.ModelSerializer):
    user = LawyerSerializerView()

    class Meta:
        model = lawyer
        fields = ['username', 'email', 'contract_speciality']
        depth = 1


class lawyerSerializer(serializers.ModelSerializer):
    class Meta:
        model = lawyer
        fields = '__all__'


class consultationSerializer(serializers.ModelSerializer):
    class Meta:
        model = consultation
        fields = '__all__'


class consultation_requestSerializer(serializers.ModelSerializer):
    class Meta:
        model = consultation_request
        fields = '__all__'


class paymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = payment
        fields = '__all__'
