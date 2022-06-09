from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.authentication import JWTAuthentication
from . import models
from .serializers import *


@api_view(['POST'])
@permission_classes([IsAuthenticated])
@authentication_classes([JWTAuthentication])
def add_lawyer(request: Request):
    if not request.user.is_authenticated:
        return Response({"msg": "Not Allowed"}, status=status.HTTP_401_UNAUTHORIZED)

    request.data.update(user=request.user.id)

    new_lawyer = lawyerSerializer(data=request.data)
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
    lawyers = lawyer.objects.all()

    dataResponse = {
        "msg": "List of Lawyers:",
        "Lawyers": lawyerSerializer(instance=lawyers, many=True).data
    }

    return Response(dataResponse)


@api_view(['PUT'])
@authentication_classes([JWTAuthentication])
def update_lawyer(request: Request, lawyer_id):
    if not request.user.is_authenticated:
        return Response({"msg": "Not Allowed"}, status=status.HTTP_401_UNAUTHORIZED)
    lawyers = lawyer.objects.get(id=lawyer_id)

    updated_lawyer = lawyerSerializer(instance=lawyers, data=request.data)
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
@authentication_classes([JWTAuthentication])
def delete_lawyer(request: Request, lawyer_id):
    if not request.user.is_authenticated:
        return Response({"msg": "Not Allowed"}, status=status.HTTP_401_UNAUTHORIZED)
    Lawyer = lawyer.objects.get(id=lawyer_id)
    Lawyer.delete()
    return Response({"msg": "Deleted Successfully"})


@api_view(['POST'])
@permission_classes([IsAuthenticated])
@authentication_classes([JWTAuthentication])
def add_consultation(request: Request):
    if not request.user.is_authenticated or not request.user.has_perm('consultation.add_consultation'):
        return Response({"msg": "Not Allowed"}, status=status.HTTP_401_UNAUTHORIZED)

    request.data.update(user=request.user.id)

    new_consult = consultationSerializer(data=request.data)
    if new_consult.is_valid():
        new_consult.save()
        dataResponse = {
            "msg": "Created Successfully",
            "lawyer": new_consult.data
        }
        return Response(dataResponse)
    else:
        print(new_consult.errors)
        dataResponse = {"msg": "couldn't create a new consult"}
        return Response(dataResponse, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def list_consultation(request: Request):
    consultations = consultation.objects.all()

    dataResponse = {
        "msg": "List of Lawyers:",
        "consultations": consultationSerializer(instance=consultations, many=True).data
    }

    return Response(dataResponse)


@api_view(['DELETE'])
@authentication_classes([JWTAuthentication])
def delete_consultation(request: Request, consultation_id):
    if not request.user.is_authenticated:
        return Response({"msg": "Not Allowed"}, status=status.HTTP_401_UNAUTHORIZED)
    con = consultation.objects.get(id=consultation_id)
    con.delete()
    return Response({"msg": "Deleted Successfully"})


@api_view(['GET'])
def search_for_lawyers(request: Request):
    if 'search' in request.query_params:
        search_phrase = request.query_params['search']
        lawyers = lawyer.objects.filter(contract_speciality__contains=search_phrase)
    else:
        lawyers = lawyer.objects.all()

    responseData = {
        "msg": "list of lawyers",
        "lawyers:": lawyersSerializerView(instance=lawyers, many=True).data
    }

    return Response(responseData)


@api_view(['POST'])
def payment(request: Request):
    pass
