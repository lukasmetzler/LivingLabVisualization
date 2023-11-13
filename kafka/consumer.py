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

consumer = KafkaConsumer(
    'dim_metrological_data_topic',  # Specify the Kafka topic
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
    cursor.execute("""
        INSERT INTO dim_metrological_data (
            GlobalIrrVerAct, GlobIrrVerAct, GlobalIrrHorAct, DifflrrHorAct, WindSpeedAct_ms,
            SunElevationAct, SunAzimuthAct, Longitude, Latitude, WindSpeedAct_kmh,
            WindDirectionAct, BrightnessNorthAct, BrightnessSouthAct, BrightnessWestAct,
            TwilightAct, GlobalIrrHorAct_2, PrecipitationAct, AbsolutAirPressureAct,
            RelativeAirPressureAct, AbsoluteHumidityAct, RelativeHumidityAct, DewPointTempAct,
            HousingTemAct, RoomTempAct
        ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
    """, (
        metrological_data['GlobalIrrVerAct'], metrological_data['GlobIrrVerAct'],
        metrological_data['GlobalIrrHorAct'], metrological_data['DifflrrHorAct'],
        metrological_data['WindSpeedAct_ms'], metrological_data['SunElevationAct'],
        metrological_data['SunAzimuthAct'], metrological_data['Longitude'],
        metrological_data['Latitude'], metrological_data['WindSpeedAct_kmh'],
        metrological_data['WindDirectionAct'], metrological_data['BrightnessNorthAct'],
        metrological_data['BrightnessSouthAct'], metrological_data['BrightnessWestAct'],
        metrological_data['TwilightAct'], metrological_data['GlobalIrrHorAct_2'],
        metrological_data['PrecipitationAct'], metrological_data['AbsolutAirPressureAct'],
        metrological_data['RelativeAirPressureAct'], metrological_data['AbsoluteHumidityAct'],
        metrological_data['RelativeHumidityAct'], metrological_data['DewPointTempAct'],
        metrological_data['HousingTemAct'], metrological_data['RoomTempAct']
    ))

    conn.commit()
