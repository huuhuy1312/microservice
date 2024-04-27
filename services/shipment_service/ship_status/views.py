from __future__ import unicode_literals
from django.http import HttpResponse
from django.shortcuts import render
import json
from django.views.decorators.csrf import csrf_exempt
from ship_status.models import shipment

# Create your views here.
def ship_data_insert(first_name, last_name, email, mobile, address, product_id, quantity, payment_status, transaction_id, shipment_status):
    shipment_data = shipment(first_name = first_name,last_name = last_name, email = email, mobile = mobile, address = address, product_id = product_id, quantity = quantity, payment_status = payment_status, transaction_id = transaction_id,    shipment_status = shipment_status)
    shipment_data.save()
    return 1

@csrf_exempt
def shipment_reg_update(request):
    if request.method == 'POST':
        if 'application/json' in request.META['CONTENT_TYPE']:
            val1 = json.loads(request.body)
            first_name = val1.get("First Name")
            last_name = val1.get("Last Name")
            email = val1.get("Email Id")
            mobile = val1.get("Mobile Number")
            address = val1.get("Address")
            product_id = val1.get("Product Id")
            quantity = val1.get("Quantity")
            payment_status = val1.get("Payment Status")
            transaction_id = val1.get("Transaction Id")
            shipment_status = "ready to dispatch"
            resp = {}
            respdata = ship_data_insert(first_name, last_name, email, mobile, address, product_id, quantity, payment_status, transaction_id, shipment_status)

            if respdata:
                resp['status'] = 'Success'
                resp['status_code'] = '200'
                resp['message'] = 'Product is ready to dispatch.'
            else:
                resp['status'] = 'Failed'
                resp['status_code'] = '400'
                resp['message'] = 'Failed to update shipment details.'
    return HttpResponse(json.dumps(resp), content_type = 'application/json')

def shipment_data(username):
    data = shipment.objects.filter(email = username)
    for val in data.values():
        return val
    
@csrf_exempt
def shipment_status(request):
    if request.method == 'POST':
        if 'application/json' in request.META['CONTENT_TYPE']:
            variable1 = json.loads(request.body)
            
            username = variable1.get("User Name")
            resp = {}
            
            respdata = shipment_data(username)
            
            if respdata:
                resp['status'] = 'Success'
                resp['status_code'] = '200'
                resp['message'] = respdata

            else:
                resp['status'] = 'Failed'
                resp['status_code'] = '400'
                resp['message'] = 'User data is not available.'
    return HttpResponse(json.dumps(resp), content_type = 'application/json')