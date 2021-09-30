import requests
from requests.structures import CaseInsensitiveDict
print('Welcome! Change your HypeSquad house here!')
token = input('What is your discord token?: ')
url = "https://discord.com/api/v9/hypesquad/online"
id = input('What house do you want 1-3(1: Bravery, 2: Brilliance, 3: Balance)?')
headers = CaseInsensitiveDict()
headers["Authorization"] = token
headers["Content-Type"] = "application/json"

data = '{"house_id":' + id + '}'
resp = requests.post(url, headers=headers, data=data)
if resp.status_code == 204:
    input('Success! Press Enter to Exit')
if resp.status_code != 204:
    input('Not a Success? Press enter to exit. Error code ' + str(resp.status_code))
