import http.client, urllib.request, urllib.parse, urllib.error, base64
import json
from settings import settings

headers = {
    # Request headers
    'Ocp-Apim-Subscription-Key': settings['api_key'],
}

params = urllib.parse.urlencode({
})

conn = http.client.HTTPSConnection('gateway.apiportal.ns.nl')
conn.request("GET", "/public-reisinformatie/api/v2/stations?%s" % params, "{body}", headers)
response = conn.getresponse()
data = response.read().decode('utf-8')
conn.close()
json_data = json.loads(data)
s = json.dumps(json_data, indent=4, sort_keys=True)
with open('data/stations.json', 'w+') as f:
    f.write(s)

####################################
                                                
               