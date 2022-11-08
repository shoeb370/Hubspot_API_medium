import hubspot
from hubspot.crm.properties import ApiException

client = hubspot.Client.create(access_token="your_api_token")

try:
    # api_response = client.crm.properties.core_api.get_all(object_type="objectType", archived=False)
    api_response = client.crm.properties.core_api.get_all(object_type = 'contacts',archived=False)
    #api_response = client.crm.properties.core_api.get_all(object_type = 'companies',archived=False)
    # api_response = client.crm.properties.core_api.get_by_name(object_type = 'contact', property_name = 'Annual Revenue',archived=False)

    print(api_response)
except ApiException as e:
    print("Exception when calling core_api->get_all: %s\n" % e)
    
with open('field_of_contact.txt', 'w') as f:
    f.write(str(api_response))
