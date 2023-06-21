# ----------------
# Copyright
# ----------------
# Written by John Capobianco, March 2023
# Copyright (c) 2023 John Capobianco

# ----------------
# Python
# ----------------
import json
import urllib3
import requests
import rich_click as click
import django
django.setup()
from whip.models import whip_Credentials,whip_api_to_get,whip_api_output

urllib3.disable_warnings()

db_token = whip_Credentials.objects.all().values('token')

token = db_token[0]['token']

db_api = whip_api_to_get.objects.all().values('whip_api')

api = db_api[0]['whip_api']

class WHIP_Plugin():
    def whip_plugin(self):
        self.get_json(token)
   
    def get_json(self,token):
        payload={}
        headers = {
        'token': token
        }
        response = requests.request("GET", api, headers=headers, data=payload)
        all_json = response.json()
        for answer in all_json:
            if 'Last Updated' in answer:
                del answer['Last Updated']
            
        chatGPTAnswer=whip_api_output(whip_api_output = json.dumps(all_json,sort_keys=True,indent=4))
        chatGPTAnswer.save()    

        deleteme = whip_api_to_get.objects.all()
        deleteme.delete()

@click.command()
def cli():
    invoke_class = WHIP_Plugin()
    invoke_class.whip_plugin()

if __name__ == "__main__":
    cli()