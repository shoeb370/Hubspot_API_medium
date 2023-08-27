# -*- coding: utf-8 -*-
"""
Created on Sun Aug 27 16:31:30 2023

@author: HP
"""

import pandas as pd
from hubspot import HubSpot
#Import Hubspot API exceptions
from hubspot.crm.companies import ApiException

# Create an hubspot client Instances
api_client = HubSpot(access_token='Your_API_Key')


def contact_details():
    try:
        #limit is not more than 100
        # contact_fetched = api_client.crm.contacts.basic_api.get_page(limit = 100, archived=False, properties = ['firstname', 'lastname', 'email', 'phone'],after=Id or hs_id)
        contact_fetched = api_client.crm.contacts.basic_api.get_page(limit = 100, archived=False, properties = ['firstname', 'lastname', 'email', 'phone'],after=893)

    except ApiException as e:
        print("Exception when requesting Companies by id: %s\n" % e)
    
    id_list = []; df =pd.DataFrame()    
    for i in range(len(contact_fetched.results)):
        df_properties = pd.DataFrame([contact_fetched.results[i].properties])
        id_list.append(contact_fetched.results[i].id)
        df = pd.concat([df, df_properties], ignore_index=True)
    df["Id"] = id_list
    df = df[['Id', 'hs_object_id', 'firstname', 'lastname', 'email', 'phone', 'createdate', 'lastmodifieddate']]
    return df
