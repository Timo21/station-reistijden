import os
import glob
import json
from get_trip import get_smallest_travel_time
import pandas as pd

foldername = 'trip_jsons'
    
filenames = glob.glob(foldername + '/*.json')
rows = list()
for filename in filenames:
    from_eva = filename.split('-')[1]
    to_eva = filename.split('-')[2].split('.')[0]
    with open(filename, 'r+') as f:
        data = json.load(f)

    travel_times = list()
    for trip in data:
        travel_time = trip['actualDurationInMinutes']
        travel_times.append(travel_time)
    
    min_travel_time = min(travel_times)
    rows.append({'from_eva': from_eva, 'to_eva': to_eva, 'traveltime': min_travel_time})

df = pd.DataFrame(rows)
df['from_eva'] = df['from_eva'].astype(int)
df['to_eva'] = df['to_eva'].astype(int)

stations = pd.read_csv('stations.csv')
df = df.merge(stations[['naam_lang', 'eva_code']], left_on='from_eva', right_on='eva_code')
df = df.rename(columns={'naam_lang': 'naam_from'}).drop('eva_code', axis=1)

df = df.merge(stations[['naam_lang', 'eva_code']], left_on='to_eva', right_on='eva_code')
df = df.rename(columns={'naam_lang': 'naam_to'}).drop('eva_code', axis=1)

df.to_csv('data/reistijden.csv', index=False)
