from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from civic_sandbox.all_layers import layers
from .packages import packages



@api_view(['GET'])
def sandbox_registry(request, format=None): 
    # try: ##TODO
    # except model_class.DoesNotExist:
    #     return Response(status.HTTP_404_NOT_FOUND)

    registry_keys = [
        'name',
        'type', 
        'endpoint', 
        'visualization', 
        'primary_attribute_column',
        'primary_attribute_label',
        'secondary_attribute_column',
        'secondary_attribute_label',
        'date_attribute_column',
        'date_granularity',
        'default_date_filter',
        'min_date',
        'min_date',
        ]

    new_layers = {}
    new_layer_dict = {}
    for key, val in layers.items():

        new_layer_dict[key] = {}

        for sub_key, sub_val in val.items():
            if sub_key in registry_keys: 
                new_layer_dict[key][sub_key] = sub_val
                new_layers.update(new_layer_dict)
                

    response= { 
        'packages': packages,
        'layers': new_layers
    }
    return Response(response)





