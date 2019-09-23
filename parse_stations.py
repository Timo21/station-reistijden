import json
import pandas as pd

with open('data/stations.json', 'r+') as f:
    data = json.load(f)

stations = data['payload']

stations_list = list()
for station in stations:
    stations_data = {
        'naam': station['namen']['kort'],
        'naam_lang': station['namen']['lang'],
        'code': station['code'],
        'type': station['stationType'],
        'land': station['land'],
        'uic_code': station['UICCode'],
        'eva_code': station['EVACode'],
        'lat': station['lat'],
        'lng': station['lng'],
    }
    stations_list.append(stations_data)

df = pd.DataFrame(stations_list)
df.to_csv('data/stations.csv', index=False)

df_filtered = df.query("land == 'NL'")
df_filtered = df_filtered[~df_filtered.type.isin(['STOPTREIN_STATION', 'FACULTATIEF_STATION'])]

df_filtered.to_csv('data/grote_stations.csv', index=False)