import requests
import json

#port: 6001
#url_extension: /api/world/objects
#it returns the entire JSON
def request(port, url_extension):
    url = "http://127.0.0.1:" + port

    r = requests.get(url + url_extension)

    # Response, status etc
    if r.status_code == 200:
        data = r.json()
        return data

    return "ERROR"

if __name__ == "__main__":
    print(request("6001", "/api/world/objects"))



#payload = {'key1': 'value1', 'key2': 'value2'}

# GET

# GET with params in URL
#r = requests.get(url, params=payload)

# POST with form-encoded data
#r = requests.post(url, data=payload)

# POST with JSON
#r = requests.post(url, data=json.dumps(payload))
