from rest_framework import serializers
from .models import Lawyer, Consultation, Consultation_request, Consultation_replay
from django.contrib.auth.models import User


class UserSerializerView(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email']


class LawyersSerializerView(serializers.ModelSerializer):
    user = UserSerializerView()

    class Meta:
        model = Lawyer
        fields = '__all__'
        depth = 1


class LawyerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lawyer
        fields = '__all__'


class ConsultationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Consultation
        fields = '__all__'


class Consultation_requestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Consultation_request
        fields = '__all__'


class Consultation_replaySerializer(serializers.ModelSerializer):
    class Meta:
        model = Consultation_replay
        fields = '__all__'
