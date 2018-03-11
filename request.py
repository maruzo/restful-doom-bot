import requests
import json

#port: 6001
#url_extension: /api/world/objects
#it returns the entire JSON

port = "6001"
ip = "http://127.0.0.1:"

def get(url_extension):
    url = ip + port

    r = requests.get(url + url_extension)

    # Response and status
    if r.status_code == 200:
        data = r.json()
        return data

    return "ERROR"

#port: 6001
#url_extension: /api/world/objects
#pyload: {'type': 'strafe-left','amount': 25}
def post(url_extension, payload):
    url = ip + port

    r = requests.post(url + url_extension, data=json.dumps(payload))

    # status
    return r.status_code


if __name__ == "__main__":
    print(get("/api/world/objects"))
    print(post("/api/player/actions", {'type': 'strafe-left','amount': 25}))



#payload = {'key1': 'value1', 'key2': 'value2'}

# GET

# GET with params in URL
#r = requests.get(url, params=payload)

# POST with form-encoded data
#r = requests.post(url, data=payload)

# POST with JSON
#r = requests.post(url, data=json.dumps(payload))
