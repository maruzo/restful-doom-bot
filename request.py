import requests
import json

#port: 6001
#url_extension: /api/world/objects
#it returns the entire JSON
def get(port, url_extension):
    url = "http://127.0.0.1:" + port

    r = requests.get(url + url_extension)

    # Response and status
    if r.status_code == 200:
        data = r.json()
        return data

    return "ERROR"

#port: 6001
#url_extension: /api/world/objects
#pyload: {'type': 'strafe-left','amount': 25}
def post(port, url_extension, payload):
    url = "http://127.0.0.1:" + port

    r = requests.post(url + url_extension, data=json.dumps(payload))

    # status
    return r.status_code


if __name__ == "__main__":
    print(get("6001", "/api/world/objects"))
    print(post("6001", "/api/player/actions", {'type': 'strafe-left','amount': 25}))



#payload = {'key1': 'value1', 'key2': 'value2'}

# GET

# GET with params in URL
#r = requests.get(url, params=payload)

# POST with form-encoded data
#r = requests.post(url, data=payload)

# POST with JSON
#r = requests.post(url, data=json.dumps(payload))
