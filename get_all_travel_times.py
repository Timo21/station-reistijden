import pandas as pd
from get_trip import get_smallest_travel_time, get_trips_data

stations = pd.read_csv('data/grote_stations.csv')
stations = stations[['eva_code', 'naam_lang']]
stations['fake_key'] = 0

from_to_stations = stations.merge(stations, how='outer', on='fake_key')
from_to_stations = from_to_stations.drop('fake_key', axis=1)
from_to_stations = from_to_stations.rename(columns={
    'eva_code_x': 'from_eva_code',
    'naam_lang_x': 'from_naam',
    'eva_code_y': 'to_eva_code',
    'naam_lang_y': 'to_naam'
})

from_to_stations = from_to_stations.query('from_eva_code != to_eva_code')

from_to_stations['traveltime'] = from_to_stations.apply(
    lambda x: get_trips_data(
        from_eva_code=x['from_eva_code'],
        to_eva_code=x['to_eva_code'],
        date_and_time='2019-09-30T07:30:00',
        save_json=True
    ), axis=1)

from_to_stations.to_csv('data/reistijden.csv', index=False)