# Inserting Sample data
from hubspot import HubSpot
from hubspot.crm.companies import SimplePublicObjectInput
from hubspot.crm.companies import ApiException
import pandas as pd

#Instance creation of Hubspot account
api_client = HubSpot(access_token='your_api_token')

params = {
    "jersey_number": "1",
    'player_name':"De Gea",
    'firstname' : "David",
    'lastname' : 'De Gea Quintana',
    'email' : 'degea@manchesterunited.com'
    }

try:
    simple_public_object_input = SimplePublicObjectInput(
            properties=params
        )
    api_response = api_client.crm.contacts.basic_api.create(
        simple_public_object_input=simple_public_object_input
    )
    print('-'*30)
    print(api_response)
    print('-'*30)
    print('The id is ->',api_response.id)
    print('-'*30)
except ApiException as e:
    print("Exception when creating contact: %s\n" % e)
@shoeb370
 
