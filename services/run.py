import subprocess
import os

services = [
    'manager_service',
    'category_service',
    'book_service',
    'clothes_service',
    'mobile_service',
    'cart_service',
    'order_service',
    'payment_service',
    'shipment_service',
    'search_service',
    'user_service'
]
ports = [
    7999,  
    8001, 
    8002, 
    8003, 
    8004, 
    8005, 
    8006, 
    8007, 
    8008, 
    8009,
    8010
]

# Run each project
for service, port in zip(services, ports):
    command = f"py D://dulieukhach//Workspace//django_project//services//{service}//manage.py runserver {port}"
    subprocess.Popen(command, shell=True)

print("All Django projects have been started.")
