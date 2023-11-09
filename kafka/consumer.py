from kafka import KafkaConsumer
import json
import psycopg2

consumer = KafkaConsumer('metrological-topic',
                         bootstrap_servers=['localhost:9092'],
                         auto_offset_reset='earliest',
                         value_deserializer=lambda m: json.loads(m.decode('utf-8')))

# PostgreSQL Connection
conn = psycopg2.connect(
    host="localhost",
    database="EVI",
    user="lukasmetzler",
    password="lukasmetzler",
)

for message in consumer:
    data = message.value

    # Speichern in PostgreSQL
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO metrological_data (GlobIrrVerAct, GlobalIrrHorAct, DifflrrHorAct, WindSpeedAct_ms, SunElevationAct, SunAzimuthAct, Longitude, Latitude, WindSpeedAct_kmh, WindDirectionAct, BrightnessNorthAct, BrightnessSouthAct, BrightnessWestAct, TwilightAct, GlobalIrrHorAct_2, PrecipitationAct, AbsolutAirPressureAct, RelativeAirPressureAct, AbsoluteHumidityAct, RelativeHumidityAct, DewPointTempAct, HousingTemAct, RoomTempAct) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",
        (data["GlobIrrVerAct"], data["GlobalIrrHorAct"], data["DifflrrHorAct"], data["WindSpeedAct_ms"], data["SunElevationAct"], data["SunAzimuthAct"], data["Longitude"], data["Latitude"], data["WindSpeedAct_kmh"], data["WindDirectionAct"], data["BrightnessNorthAct"], data["BrightnessSouthAct"], data["BrightnessWestAct"], data["TwilightAct"], data["GlobalIrrHorAct_2"], data["PrecipitationAct"], data["AbsolutAirPressureAct"], data["RelativeAirPressureAct"], data["AbsoluteHumidityAct"], data["RelativeHumidityAct"], data["DewPointTempAct"], data["HousingTemAct"], data["RoomTempAct"])
    )
    conn.commit()
    cursor.close()

    print("Data saved to PostgreSQL")
