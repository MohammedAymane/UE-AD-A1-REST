import requests
                 
TOKEN = "abcd123"
API = "http://0.1.2.3"
EGY_URL = "https://www.egybest.org/movie/top-gun-maverick-2022"       
HEADERS = {'Authorization': 'Bearer ' + TOKEN, 'Accept': 'application/json', 'Content-Type': 'application/json'}
PARAMS = {"url": EGY_URL, "v": 2}                      
URL = API +  "/similar"

response = requests.get(URL, headers=HEADERS, params=PARAMS)

print(response.status_code)
print(response.json())