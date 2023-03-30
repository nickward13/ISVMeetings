import asyncio
import configparser
from azure.identity import InteractiveBrowserCredential
from kiota_authentication_azure.azure_identity_authentication_provider import AzureIdentityAuthenticationProvider
from msgraph import GraphRequestAdapter
from msgraph import GraphServiceClient

config=configparser.ConfigParser()
config.read('config.cfg')
azure_settings = config['azure']
tenant_id = azure_settings['tenantId']
client_id = azure_settings['clientId']
redirect_uri = azure_settings['redirectUri']

scopes=['User.Read']
credential = InteractiveBrowserCredential(client_id=client_id, tenant_id = tenant_id, redirect_uri=redirect_uri)
auth_provider = AzureIdentityAuthenticationProvider(credential, scopes=scopes)
request_adapter = GraphRequestAdapter(auth_provider)
client = GraphServiceClient(request_adapter)

async def me():
    try:
        me = await client.me.get()
        print(me.display_name)
    except Exception as e:
        print("Exception occurred: " + str(e))
    

asyncio.run(me())