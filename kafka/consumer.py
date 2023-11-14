from json import loads  
from kafka import KafkaConsumer  
import psycopg2

db_params = {
    'dbname': 'EVI',
    'user': 'lukasmetzler',
    'password': 'lukasmetzler',
    'host': 'localhost',
    'port': '5432'
}

metrological_column_names = [
    'GlobalIrrVerAct', 'GlobIrrVerAct', 'GlobalIrrHorAct', 'DifflrrHorAct',
    'WindSpeedAct_ms', 'SunElevationAct', 'SunAzimuthAct', 'Longitude',
    'Latitude', 'WindSpeedAct_kmh', 'WindDirectionAct', 'BrightnessNorthAct',
    'BrightnessSouthAct', 'BrightnessWestAct', 'TwilightAct', 'GlobalIrrHorAct_2',
    'PrecipitationAct', 'AbsolutAirPressureAct', 'RelativeAirPressureAct',
    'AbsoluteHumidityAct', 'RelativeHumidityAct', 'DewPointTempAct', 'HousingTemAct',
    'RoomTempAct'
]

consumer = KafkaConsumer(
    'dim_metrological_data_topic', 
    bootstrap_servers=['localhost:9092'],
    auto_offset_reset='earliest',
    enable_auto_commit=True,
    group_id='my-group',
    value_deserializer=lambda x: loads(x.decode('utf-8'))
)

conn = psycopg2.connect(**db_params)
cursor = conn.cursor()

for message in consumer:
    metrological_data = message.value
    
    columns_placeholder = ', '.join(metrological_column_names)
    
    values_placeholder = ', '.join(['%s'] * len(metrological_column_names))

    query = f"INSERT INTO dim_metrological_data ({columns_placeholder}) VALUES ({values_placeholder})"
    
    values = [metrological_data[column] for column in metrological_column_names]
    
    cursor.execute(query, values)

    conn.commit()