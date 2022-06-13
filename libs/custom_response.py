from rest_framework import status
from django.http import JsonResponse

def custom_response(data, response_status=200, pagination = None, meta = None):
    if pagination is None:
        pagination = {}
    if meta is None:
        meta = {}
    responseDict={
        'data' : data,
    }

    if pagination:
        responseDict={
            'data': data,
            'pagination': pagination
        }

    if meta:
        responseDict = meta

    if response_status >= 400:
        responseDict={
            'error':{
                'status_code': response_status,
                'message': data
            }
        }

    return JsonResponse(status=response_status,data=responseDict)