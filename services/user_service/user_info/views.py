from __future__ import unicode_literals
from django.shortcuts import render
from django.http import HttpResponse
import json
from django.views.decorators.csrf import csrf_exempt
from user_model.models import User 

# Create your views here.
def user_data(username):
    user = User.objects.filter(email = username)

    for data in user.values():
        return data
    
@csrf_exempt
def user_info(request):
    if request.method == 'POST':
        if('application/json' in request.META['CONTENT_TYPE']):
            val1 = json.loads(request.body)
            username = val1.get("User Name")
            print(username)
            resp = {}
            if username:
                respdata = user_data(username)
                dict1 = {}
                if respdata:
                    dict1['First Name'] = respdata.get('first_name','')
                    dict1['Last Name'] = respdata.get('last_name','')
                    dict1['Mobile Number'] = respdata.get('mobile','')
                    dict1['Email Id'] = respdata.get('email','')
                    dict1['Address'] = respdata.get('address','')

                if dict1:
                    resp['status'] = 'Success'
                    resp['status_code'] = '200'
                    resp['data'] = dict1
                else:
                    resp['status'] = 'Failed'
                    resp['status_code'] = '400'
                    resp['message'] = 'User Not Found.'
            else:
                resp['status'] = 'Failed'
                resp['status_code'] = '400'
                resp['message'] = 'Fields is mandatory.'
        else:
            resp['status'] = 'Failed'
            resp['status_code'] = '400'
            resp['message'] = 'Request type is not matched.'   
    else:
        resp['status'] = 'Failed'
        resp['status_code'] = '400'
        resp['message'] = 'Request type is not matched.'   
    
    return  HttpResponse(json.dumps(resp), content_type = 'application/json')      
