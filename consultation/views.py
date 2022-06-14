from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.authentication import JWTAuthentication
from . import models
from .serializers import *


@api_view(['POST'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def add_lawyer(request: Request):
    """this endpoint is for adding lawyers"""
    if not request.user.is_authenticated:
        return Response({"msg": "Not Allowed"}, status=status.HTTP_401_UNAUTHORIZED)

    request.data.update(user=request.user.id)

    new_lawyer = LawyerSerializer(data=request.data)
    if new_lawyer.is_valid():
        new_lawyer.save()
        dataResponse = {
            "msg": "Created Successfully",
            "lawyer": new_lawyer.data
        }
        return Response(dataResponse)
    else:
        print(new_lawyer.errors)
        dataResponse = {"msg": "couldn't create a new consult"}
        return Response(dataResponse, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def list_lawyers(request: Request):
    """this endpoint is for listing lawyers"""
    lawyers = Lawyer.objects.all()

    dataResponse = {
        "msg": "List of Lawyers:",
        "Lawyers": LawyersSerializerView(instance=lawyers, many=True).data
    }

    return Response(dataResponse)


@api_view(['PUT'])
@authentication_classes([JWTAuthentication])
def update_lawyer(request: Request, lawyer_id):
    """this endpoint is for updating lawyers"""
    if not request.user.is_authenticated:
        return Response({"msg": "Not Allowed"}, status=status.HTTP_401_UNAUTHORIZED)
    lawyers = Lawyer.objects.get(id=lawyer_id)

    updated_lawyer = LawyerSerializer(instance=lawyers, data=request.data)
    if updated_lawyer.is_valid():
        updated_lawyer.save()
        responseData = {
            "msg": "updated successfully"
        }

        return Response(responseData)
    else:
        print(updated_lawyer.errors)
        return Response({"msg": "bad request, cannot update"}, status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
@authentication_classes([JWTAuthentication])
def delete_lawyer(request: Request, lawyer_id):
    """this endpoint is for deleting lawyers"""
    lawyer = Lawyer.objects.get(id=lawyer_id)
    lawyer.delete()
    return Response({"msg": "Deleted Successfully"})


@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
@authentication_classes([JWTAuthentication])
def delete_user(request: Request, user_id):
    """this endpoint is for deleting a user"""
    lawyer = User.objects.get(id=user_id)
    lawyer.delete()
    return Response({"msg": "Deleted Successfully"})


@api_view(['POST'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def add_user(request: Request):
    """this endpoint is for adding users"""
    if not request.user.is_authenticated:
        return Response({"msg": "Not Allowed"}, status=status.HTTP_401_UNAUTHORIZED)

    request.data.update(user=request.user.id)

    new_user = UsersSerializer(data=request.data)
    if new_user.is_valid():
        new_user.save()
        dataResponse = {
            "msg": "Created Successfully",
            "user": new_user.data
        }
        return Response(dataResponse)
    else:
        print(new_user.errors)
        dataResponse = {"msg": "couldn't create a new user"}
        return Response(dataResponse, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def list_users(request: Request):
    """this endpoint is for listing users"""
    users = Users.objects.all()

    dataResponse = {
        "msg": "List of Users:",
        "Users": UsersSerializerView(instance=users, many=True).data
    }

    return Response(dataResponse)


@api_view(['PUT'])
@authentication_classes([JWTAuthentication])
def update_users(request: Request, users_id):
    """this endpoint is for updating users"""
    if not request.user.is_authenticated:
        return Response({"msg": "Not Allowed"}, status=status.HTTP_401_UNAUTHORIZED)
    users = Users.objects.get(id=users_id)

    updated_user = UsersSerializer(instance=users, data=request.data)
    if updated_user.is_valid():
        updated_user.save()
        responseData = {
            "msg": "updated successfully"
        }

        return Response(responseData)
    else:
        print(updated_user.errors)
        return Response({"msg": "bad request, cannot update"}, status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
@authentication_classes([JWTAuthentication])
def delete_user(request: Request, users_id):
    """this endpoint is for deleting users"""
    user = Users.objects.get(id=users_id)
    user.delete()
    return Response({"msg": "Deleted Successfully"})


@api_view(['POST'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def request_consultation(request: Request, lawyer_id):
    """this endpoint is for users to request a consultation from a lawyer"""
    print(request.user)
    if not request.user.is_authenticated or not request.user.has_perm('consultation.add_consultation_request'):
        return Response({"msg": "Not Allowed"}, status=status.HTTP_401_UNAUTHORIZED)

    request.data.update(user=request.user.id)

    consultationRequest = Consultation_requestSerializer(data=request.data)
    if consultationRequest.is_valid():
        consultationRequest.save()
        dataResponse = {
            "msg": "Created Successfully",
            "consultation request": consultationRequest.data
        }
        return Response(dataResponse)
    else:
        print(consultationRequest.errors)
        dataResponse = {"msg": "couldn't request a consult"}
        return Response(dataResponse, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def list_consultation(request: Request):
    """this endpoint is for listing consultations"""
    consultations = Consultation_request.objects.all()
    lawyers = Lawyer.objects.all()

    dataResponse = {
        "msg": "List of Consultations:",
        "consultations": ConsultationsSerializerView(instance=consultations, many=True).data,
        # "lawyers info:": LawyersSerializerView(instance=lawyers, many=True).data
    }

    return Response(dataResponse)


@api_view(['DELETE'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def delete_consultation_request(request: Request, consultation_request_id):
    """this endpoint is for deleting a consultation request by the user"""
    con = Consultation_request.objects.get(id=consultation_request_id)
    con.delete()
    return Response({"msg": "Deleted Successfully"})


@api_view(['POST'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def replay_consultation(request: Request, consultation_request_id):
    """this endpoint allows lawyers to replay to consultation requests"""
    if not request.user.is_authenticated or not request.user.has_perm('consultation.add_consultation_replay'):
        return Response({"msg": "Not Allowed"}, status=status.HTTP_401_UNAUTHORIZED)

    request.data.update(user=request.user.id)

    consultationReplay = Consultation_replaySerializer(data=request.data)
    if consultationReplay.is_valid():
        consultationReplay.save()
        dataResponse = {
            "msg": "Created Successfully",
            "consultation replay": consultationReplay.data
        }
        return Response(dataResponse)
    else:
        print(consultationReplay.errors)
        dataResponse = {"msg": "couldn't replay"}
        return Response(dataResponse, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def search_for_lawyers(request: Request):
    """this endpoint allows users to search for lawyers"""
    if request.method == 'GET':
        lawyers = Lawyer.objects.all()
        contract_speciality = request.GET.get('contract_speciality', None)
        if contract_speciality is not None:
            search_s = Lawyer.objects.filter(contract_speciality=contract_speciality)
            search_lawyer = {
                "lawyer": LawyersSerializerView(instance=search_s, many=True).data
            }
            return Response(search_lawyer)
    return Response("none")


@api_view(['GET'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def view_consultation_replay(request: Request):
    """this endpoint is for listing consultations"""
    consultations = Consultation_request.objects.all()
    replay = Consultation_replay.objects.all()

    dataResponse = {
        "msg": "List of Consultations:",
        "consultations": ConsultationsSerializerView(instance=consultations, many=True).data,
        "replay:": Consultation_replaySerializer(instance=replay, many=True).data
    }

    return Response(dataResponse)