from wsgiref.simple_server import software_version
import requests

# URL and InterfaceName from Juniper environment 
url_base = 'http://ip:port/rpc'
interface_name= 'cbp0'

# config headers + auth
headers = {
  'Accept': 'application/json',
  'Content-Type': 'application/xml',
  'Authorization': 'Basic xxxxxxxxxxxxxxxxxxx='
}

# Get and Print device software info
print("Device Software Information: \n")
software_information = requests.request("GET", f'{url_base}/get-software-information', headers=headers, verify=False)
print(software_information.text)
###########################################################################################################################################
# Get and Print interface info
print(f"Interface: {interface_name} Information: \n")
payload = f"<interface-name>{interface_name}</interface-name>"
interface_information = requests.request("POST", f'{url_base}/get-interface-information', headers=headers, data=payload, verify=False)
print(interface_information.text)




