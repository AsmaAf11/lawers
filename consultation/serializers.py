from rest_framework import serializers
from .models import Lawyer, Consultation_request, Consultation_replay, Users
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


class UsersSerializer(serializers.ModelSerializer):


    class Meta:
        model = Users
        fields = '__all__'


class UsersSerializerView(serializers.ModelSerializer):
    user = UserSerializerView()

    class Meta:
        model = Users
        fields = '__all__'
        depth = 1


'''class ConsultationSerializer(serializers.ModelSerializer):
    user = UserSerializerView()

    class Meta:
        model = Consultation
        fields = '__all__'
        '''


class ConsultationsSerializerView(serializers.ModelSerializer):
    user = UserSerializerView()

    class Meta:
        model = Consultation_request
        fields = '__all__'
        depth = 1


class Consultation_requestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Consultation_request
        fields = '__all__'


class Consultation_replaySerializer(serializers.ModelSerializer):
    class Meta:
        model = Consultation_replay
        fields = '__all__'
