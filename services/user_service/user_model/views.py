from django.forms import model_to_dict
from user_model.models import User
from rest_framework import viewsets
from .serializers import UserSerializer
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
import json
from django.core.serializers import serialize
# Create your views here.

        
class UserViewSet(viewsets.ViewSet):
    # @action(detail=False, methods=['GET'], url_name="")
    def list(self, request):
        queryset = User.objects.all()
        serializer = UserSerializer(queryset, many=True)
        return Response(data=serializer.data)
    
    def retrieve(self, request, pk=None):
        queryset = User.objects.all()
        user = get_object_or_404(queryset, pk=pk)
        serializer = UserSerializer(user)
        return Response(data=serializer.data)

    @action(detail=False, methods=['POST'],url_path="register")
    def register(self, request):
        first_name = request.data.get("first_name")
        last_name = request.data.get("last_name")
        email = request.data.get("email")
        mobile = request.data.get("tel")
        password = request.data.get("password")
        cnf_password = request.data.get("confirm_password")
        address = request.data.get("address")
        role = request.data.get("role")
        print(first_name)
        print(last_name)
        print(email)
        user_existed_email = User.objects.filter(email=email)
        user_extsted_phone = User.objects.filter(mobile=mobile)
        response = {}
        if first_name and last_name and email and mobile and password and cnf_password and address:
            if not user_existed_email and not user_extsted_phone:
                if len(str(mobile))==10:
                    if(password==cnf_password):
                        response_data = User(first_name = first_name, last_name = last_name, email = email, mobile = mobile, password = password, address = address,role=role)
                        if response_data:
                            response_data.save()
                            user_dict = {
                                "id": response_data.id,
                                "first_name": response_data.first_name,
                                "last_name": response_data.last_name,
                                "email": response_data.email,
                                "mobile": response_data.mobile,
                                "password": response_data.password,
                                "address": response_data.address,
                                "role":response_data.role
                            }
                            response['data'] = user_dict
                            response['status'] = 'Success'
                            response['status_code'] = '200'
                            response['message'] = 'User is registered successfully.'
                        else:
                            response['status'] = 'Failed'
                            response['status_code'] = '400'
                            response['message'] = 'Unable to register user. Please try again.'
                    else:
                        response['status'] = 'Failed'
                        response['status_code'] = '400'
                        response['message'] = 'Password and Confirm Password should be same.'
                else:
                    response['status'] = 'Failed'
                    response['status_code'] = '400'
                    response['message'] = 'Mobile Number should be 10 digits.'
            else:
                response['status'] = 'Failed'
                response['status_code'] = '400'
                response['message'] = 'Email or Mobile Number existed.'
        else:
            response['status'] = 'Failed'
            response['status_code'] = '400'
            response['message'] = 'All fields are mandatory.' 
        return Response(data=response, status=response['status_code'], content_type='application/json')
    @action(methods=['POST'], detail=False,url_path="login")
    def login(self, request):
        username = request.data.get("user_name")
        password = request.data.get("password")
        response = {}
        if username and password:
            user_data = User.objects.filter(email = username, password = password).first()
            if user_data:
                response['status'] = "Success"
                user_dict = {
                "id": user_data.id,
                "first_name": user_data.first_name,
                "last_name": user_data.last_name,
                "email": user_data.email,
                "mobile": user_data.mobile,
                "password": user_data.password,
                "address": user_data.address,
                "role":user_data.role
                }
                response['data'] = user_dict
                response['status_code'] = '200'
                response['message'] = 'Welcome to Ecommerce website...'
            else:
                response['status'] = 'Failed'
                response['status_code']  = '400'
                response['message'] = 'Invalid credentials.'
        else:
            response['status'] = 'Failed'
            response['status_code']  = '400'
            response['message'] = 'All fields are mandatory.'
        return Response(data=response, status=response['status_code'], content_type = 'application/json')
    