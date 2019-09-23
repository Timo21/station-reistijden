import http.client, urllib.request, urllib.parse, urllib.error, base64
from settings import settings
import json



def get_smallest_travel_time(from_eva_code, to_eva_code, date_and_time, save_json=False):
    try:
        trips = get_trips_data(from_eva_code=from_eva_code, to_eva_code=to_eva_code,
                            date_and_time=date_and_time, save_json=save_json)

        travel_times = list()
        for trip in trips:
            travel_time = trip['actualDurationInMinutes']
            travel_times.append(travel_time)
        
        min_travel_time = min(travel_times)
    except:
        min_travel_time = 0
    return(min_travel_time)


def get_trips_data(from_eva_code, to_eva_code, date_and_time, save_json=False):

    headers = {
        # Request headers
        # 'Accept': '',
        # 'X-Request-ID': '',
        # 'X-Caller-ID': '',
        # 'x-api-key': '',
        # 'Authorization': '',
        'Ocp-Apim-Subscription-Key': settings['api_key'],
    }

    params = urllib.parse.urlencode({
        # Request parameters
        # 'originLat': '{string}',
        # 'originLng': '{string}',
        # 'destinationLat': '{string}',
        # 'destinationLng': '{string}',
        # 'viaLat': '{string}',
        # 'viaLng': '{string}',
        # 'viaWaitTime': '{integer}',
        'dateTime': date_and_time,
        # 'searchForArrival': '{boolean}',
        # 'previousAdvices': '{integer}',
        # 'nextAdvices': '{integer}',
        # 'context': '{string}',
        # 'addChangeTime': '{integer}',
        # 'lang': '{string}',
        # 'polylines': '{boolean}',
        # 'fromZip': '{string}',
        # 'toZip': '{string}',
        # 'travelMethodFrom': '{string}',
        # 'travelMethodTo': '{string}',
        # 'product': '{string}',
        # 'travelClass': '{string}',
        # 'discount': '{string}',
        # 'productStationFrom': '{string}',
        # 'productStationTo': '{string}',
        # 'yearCard': '{boolean}',
        # 'originTransit': 'False',
        # 'originWalk': 'False',
        # 'originBike': 'False',
        # 'originCar': 'False',
        # 'originName': '{string}',
        # 'travelAssistanceTransferTime': '0',
        # 'searchForAccessibleTrip': 'False',
        # 'destinationTransit': 'False',
        # 'destinationWalk': 'False',
        # 'destinationBike': 'False',
        # 'destinationCar': 'False',
        # 'destinationName': '{string}',
        # 'accessibilityEquipment1': '{string}',
        # 'accessibilityEquipment2': '{string}',
        # 'excludeHighSpeedTrains': 'False',
        # 'excludeReservationRequired': 'False',
        # 'passing': 'False',
        # 'travelRequestType': '{string}',
        'originEVACode': from_eva_code,
        'destinationEVACode': to_eva_code,
        # 'viaEVACode': '{string}',
        # 'shorterChange': '{boolean}',
        # 'fromStation': '{string}',
        # 'toStation': '{string}',
        # 'originUicCode': '{string}',
        # 'destinationUicCode': '{string}',
        # 'viaUicCode': '{string}',
        # 'bikeCarriageRequired': '{boolean}',
        # 'viaStation': '{string}',
        # 'departure': '{boolean}',
        # 'minimalChangeTime': '{integer}',
    })

    # print(from_eva_code, to_eva_code)

    conn = http.client.HTTPSConnection('gateway.apiportal.ns.nl')
    conn.request("GET", "/public-reisinformatie/api/v3/trips?%s" % params, "{body}", headers)
    response = conn.getresponse()
    data = response.read()
    conn.close()
    str_data = data.decode('utf8')
    json_data = json.loads(str_data)['trips']
    if save_json:
        s = json.dumps(json_data, indent=4, sort_keys=True)
        with open('trip_jsons/trips-{}-{}.json'.format(from_eva_code, to_eva_code), 'w+') as f:
            f.write(s)
    return(json_data)


if __name__ == "__main__":
    x = get_smallest_travel_time(
        from_eva_code=8400061,
        to_eva_code=8400597,
        date_and_time='2019-09-30T07:30:00',
        save_json=True)
    print(x)