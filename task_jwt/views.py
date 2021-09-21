from functools import partial
import re
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import *
from .serializer import *
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth.decorators import login_required
# Create your views here.
 
# Rendering Login Page
def index(request):
    return render(request,"Login.html")



# Rendering Register Page
def Register(request):
    return render(request, 'register.html')


# Rendering UserDetails page

def userDetails(request):
    return render(request, 'userDetails.html')

# AJAX





# User API
class userAPI(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        try:
            user_object = User.objects.get(id = request.GET.get('id'))
            serializer = userSerializer(user_object)
            return Response({'status':200,"payload":serializer.data})

        except:

            user_objects = User.objects.all()
            serializer = userSerializer(user_objects , many=True)
            return Response({'status':200,"payload":serializer.data})


    def patch(self, request):
        user_object = User.objects.get(id = request.data['id'])
        serializer = userSerializer(user_object,data=request.data,partial=True)
        if not serializer.is_valid():
            print(serializer.errors,"###")
            try:
                if serializer.errors['username']:
                    return Response({'status':403,'errors':serializer.errors,"message":"username exist","error":"error"})
            except:
                pass
            try:
                if serializer.errors['email']:
                    return Response({'status':403,'errors':serializer.errors,"message":"email exist","error":"error"})
            except:
                pass
            return Response({'status':403,'errors':serializer.errors,"message":"something went wrong","error":"error"})
        serializer.save()
        return Response({'status':200,"payload": serializer.data ,"message": "data saved","error":"no"})

    def delete(self,request):
        print("delete method called",request.data['id'])
        id = request.data['id']
        user_object = User.objects.get(id = id)
        print(user_object,"delete ")
        user_object.delete()
        return Response({"status":200,"message":"Deleted Successfully"})



# @api_view(['GET'])
# def userDetailsAPI(request):
#     user_objects = User.objects.all()
#     print(user_objects,"###")
#     serializer = userSerializer(user_objects , many=True)
#     print(serializer,"_-------")
#     return Response({'status':200,"payload":serializer.data})

@api_view(['POST'])
def signUpAPI(request):
    serializer = userSerializer(data=request.data)
    if not serializer.is_valid():
        try:
            if User.objects.get(email= request.data['email']):
                return Response({"status":403,"message":"Email exist","error":"error"})
        except:
            pass
        try:
                if User.objects.get(username= request.data['username']):
                    return Response({"status":403,"message":"username exist","error":"error"})
        except:
            pass
                
        else:
            return Response({'status':403,'errors':serializer.errors,"message":"something went wrong","error":"error"})
    serializer.save()
    return Response({'status':200,"payload": serializer.data ,"message": "data saved","error":"no"})



# @api_view(['PATCH'])
# def updateAPI(request,id):
#     user_object = User.objects.get(id = id)
#     serializer = userSerializer(user_object,data=request.data,partial=True)
    
#     if not serializer.is_valid():
#         print(serializer.errors)
#         return Response({'status':403,'errors':serializer.errors,"message":"something went wrong"})
#     serializer.save()
#     return Response({'status':200,"payload": serializer.data ,"message": "data saved"})
# @api_view(['DELETE'])
# def deleteAPI(request):
#     id = request.GET.get('id')
#     user_object = User.objects.get(id = id)
#     user_object.delete()
#     return Response({"status":200,"message":"Deleted Successfully"})
#
# {
#     "email":"ab@gmail.com",
#     "password":"1234",
#     "address":"1234"
# }
# 127.0.0.1:8000/userAPI/ 'Authorization: Bearer 