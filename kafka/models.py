from sqlalchemy import (
    create_engine,
    Column,
    String,
    Numeric,
    Boolean,
    JSON,
    TIMESTAMP,
    Integer,
    ForeignKey,
)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
from config import load_config

Base = declarative_base()


class DimMetrologicalData(Base):
    __tablename__ = "dim_metrological_data"
    metrological_data_id = Column(
        UUID(as_uuid=True), primary_key=True, server_default="uuid_generate_v4()"
    )
    globirrveract = Column(Numeric)
    GlobalIrrHorAct = Column(Numeric)
    DifflrrHorAct = Column(Numeric)
    WindSpeedAct_ms = Column(Numeric)
    SunElevationAct = Column(Numeric)
    SunAzimuthAct = Column(Numeric)
    Longitude = Column(Numeric)
    Latitude = Column(Numeric)
    WindSpeedAct_kmh = Column(Numeric)
    WindDirectionAct = Column(Numeric)
    BrightnessNorthAct = Column(Numeric)
    BrightnessSouthAct = Column(Numeric)
    BrightnessWestAct = Column(Numeric)
    TwilightAct = Column(Numeric)
    GlobalIrrHorAct_2 = Column(Numeric)
    PrecipitationAct = Column(Numeric)
    AbsolutAirPressureAct = Column(Numeric)
    RelativeAirPressureAct = Column(Numeric)
    AbsoluteHumidityAct = Column(Numeric)
    RelativeHumidityAct = Column(Numeric)
    DewPointTempAct = Column(Numeric)
    HousingTemAct = Column(Numeric)
    RoomTempAct = Column(Numeric)
    created_at = Column(TIMESTAMP, server_default="CURRENT_TIMESTAMP")


class DimZedBodyTracking1ogR1(Base):
    __tablename__ = "dim_zed_body_tracking_1og_r1"
    zed_body_tracking_id = Column(
        UUID(as_uuid=True), primary_key=True, server_default="uuid_generate_v4()"
    )
    is_new = Column(Boolean, default=False)
    is_tracked = Column(Boolean, default=False)
    camera_pitch = Column(Numeric)
    camera_roll = Column(Numeric)
    camera_yaw = Column(Numeric)
    body_list = Column(JSON, default="[]")
    created_at = Column(TIMESTAMP, server_default="CURRENT_TIMESTAMP")


class DimPvModulData1ogR1(Base):
    __tablename__ = "dim_pv_modul_data_1og_r1"
    pv_modul_data_id = Column(
        UUID(as_uuid=True), primary_key=True, server_default="uuid_generate_v4()"
    )
    volt_meas_act_module1 = Column(Numeric)
    curr_meas_act_module1 = Column(Numeric)
    volt_meas_act_module2 = Column(Numeric)
    curr_meas_act_module2 = Column(Numeric)
    created_at = Column(TIMESTAMP, server_default="CURRENT_TIMESTAMP")


class DimIlluminationDatapoints1ogR1(Base):
    __tablename__ = "dim_illumination_datapoints_1og_r1"
    illumination_datapoints_id = Column(
        UUID(as_uuid=True), primary_key=True, server_default="uuid_generate_v4()"
    )
    illum_mp1_act = Column(Numeric)
    illum_mp2_act = Column(Numeric)
    illum_mp3_act = Column(Numeric)
    illum_mp4_act = Column(Numeric)
    created_at = Column(TIMESTAMP, server_default="CURRENT_TIMESTAMP")


class DimRaffstoreLightData(Base):
    __tablename__ = "dim_raffstore_light_data"
    raffstore_light_data_id = Column(
        UUID(as_uuid=True), primary_key=True, server_default="uuid_generate_v4()"
    )
    room_number = Column(Integer)
    slat_ang1_act = Column(Numeric)
    slat_pos1_act = Column(Numeric)
    slat_ang2_act = Column(Numeric)
    slat_pos2_act = Column(Numeric)
    slat_ang3_act = Column(Numeric)
    slat_pos3_act = Column(Numeric)
    light1_act = Column(Numeric)
    light2_act = Column(Numeric)
    created_at = Column(TIMESTAMP, server_default="CURRENT_TIMESTAMP")


class DimUserInput(Base):
    __tablename__ = "dim_user_input"
    user_input_id = Column(
        UUID(as_uuid=True), primary_key=True, server_default="uuid_generate_v4()"
    )
    mp_glare_limit = Column(Numeric)
    mp_req_illum = Column(Numeric)
    mp_req_room_temp = Column(Numeric)
    measurement_point = Column(Integer)
    created_at = Column(TIMESTAMP, server_default="CURRENT_TIMESTAMP")


class DimTime(Base):
    __tablename__ = "dim_time"
    time_id = Column(
        UUID(as_uuid=True), primary_key=True, server_default="uuid_generate_v4()"
    )
    timestamp = Column(TIMESTAMP)
    date = Column(String)
    day_of_week = Column(String)
    month = Column(String)
    quarter = Column(String)
    year = Column(Integer)
    hour = Column(Integer)
    created_at = Column(TIMESTAMP, server_default="CURRENT_TIMESTAMP")


class DimLocation(Base):
    __tablename__ = "dim_location"
    location_id = Column(
        UUID(as_uuid=True), primary_key=True, server_default="uuid_generate_v4()"
    )
    room_number = Column(Integer)
    building = Column(String)
    created_at = Column(TIMESTAMP, server_default="CURRENT_TIMESTAMP")


class FactUserInputFacts(Base):
    __tablename__ = "fact_user_input_facts"
    user_input_facts_id = Column(
        UUID(as_uuid=True), primary_key=True, server_default="uuid_generate_v4()"
    )
    time_id = Column(UUID(as_uuid=True), ForeignKey("dim_time.time_id"))
    location_id = Column(UUID(as_uuid=True), ForeignKey("dim_location.location_id"))
    user_input_id = Column(
        UUID(as_uuid=True), ForeignKey("dim_user_input.user_input_id")
    )


class FactSensory(Base):
    __tablename__ = "fact_sensory"
    sensory_id = Column(
        UUID(as_uuid=True), primary_key=True, server_default="uuid_generate_v4()"
    )
    time_id = Column(UUID(as_uuid=True), ForeignKey("dim_time.time_id"))
    location_id = Column(UUID(as_uuid=True), ForeignKey("dim_location.location_id"))
    zed_body_tracking_id = Column(
        UUID(as_uuid=True),
        ForeignKey("dim_zed_body_tracking_1og_r1.zed_body_tracking_id"),
    )


class FactRaffstoreLightFacts(Base):
    __tablename__ = "fact_raffstore_light_facts"
    raffstore_light_facts_id = Column(
        UUID(as_uuid=True), primary_key=True, server_default="uuid_generate_v4()"
    )
    time_id = Column(UUID(as_uuid=True), ForeignKey("dim_time.time_id"))
    location_id = Column(UUID(as_uuid=True), ForeignKey("dim_location.location_id"))
    raffstore_light_data_id = Column(
        UUID(as_uuid=True),
        ForeignKey("dim_raffstore_light_data.raffstore_light_data_id"),
    )


class FactEnvironmentalDataFacts(Base):
    __tablename__ = "fact_environmental_data_facts"
    environmental_data_facts_id = Column(
        UUID(as_uuid=True), primary_key=True, server_default="uuid_generate_v4()"
    )
    time_id = Column(UUID(as_uuid=True), ForeignKey("dim_time.time_id"))
    location_id = Column(UUID(as_uuid=True), ForeignKey("dim_location.location_id"))
    metrological_data_id = Column(
        UUID(as_uuid=True), ForeignKey("dim_metrological_data.metrological_data_id")
    )
    pv_modul_data_id = Column(
        UUID(as_uuid=True), ForeignKey("dim_pv_modul_data_1og_r1.pv_modul_data_id")
    )
    illumination_datapoints_id = Column(
        UUID(as_uuid=True),
        ForeignKey("dim_illumination_datapoints_1og_r1.illumination_datapoints_id"),
    )
    radiation_forecast_id = Column(
        UUID(as_uuid=True), ForeignKey("dim_radiation_forecast.radiation_forecast_id")
    )
    head_positions_id = Column(
        UUID(as_uuid=True), ForeignKey("dim_head_positions_1og_r1.head_positions_id")
    )


class DimRadiationForecast(Base):
    __tablename__ = "dim_radiation_forecast"
    radiation_forecast_id = Column(
        UUID(as_uuid=True), primary_key=True, server_default="uuid_generate_v4()"
    )
    global_irr_hor_approx = Column(Numeric)
    diff_irr_hor_act_approx = Column(Numeric)
    created_at = Column(TIMESTAMP, server_default="CURRENT_TIMESTAMP")


class DimHeadPositions1ogR1(Base):
    __tablename__ = "dim_head_positions_1og_r1"
    head_positions_id = Column(
        UUID(as_uuid=True), primary_key=True, server_default="uuid_generate_v4()"
    )
    headpose_x_1 = Column(Numeric)
    headpose_y_1 = Column(Numeric)
    headpose_z_1 = Column(Numeric)
    headpose_pitch_1 = Column(Numeric)
    headpose_yaw_1 = Column(Numeric)
    headpose_roll_1 = Column(Numeric)
    headpose_x_2 = Column(Numeric)
    headpose_y_2 = Column(Numeric)
    headpose_z_2 = Column(Numeric)
    headpose_pitch_2 = Column(Numeric)
    headpose_yaw_2 = Column(Numeric)
    headpose_roll_2 = Column(Numeric)
    headpose_x_3 = Column(Numeric)
    headpose_y_3 = Column(Numeric)
    headpose_z_3 = Column(Numeric)
    headpose_pitch_3 = Column(Numeric)
    headpose_yaw_3 = Column(Numeric)
    headpose_roll_3 = Column(Numeric)
    headpose_x_4 = Column(Numeric)
    headpose_y_4 = Column(Numeric)
    headpose_z_4 = Column(Numeric)
    headpose_pitch_4 = Column(Numeric)
    headpose_yaw_4 = Column(Numeric)
    headpose_roll_4 = Column(Numeric)
    created_at = Column(TIMESTAMP, server_default="CURRENT_TIMESTAMP")


def get_engine():
    config = load_config()
    db_url = (
        f"postgresql+psycopg2://{config.CONSUMER_POSTGRES_USER}:"
        f"{config.CONSUMER_POSTGRES_PASSWORD}@{config.CONSUMER_POSTGRES_HOST}:"
        f"{config.CONSUMER_POSTGRES_PORT}/{config.CONSUMER_POSTGRES_DB}"
    )
    return create_engine(db_url)
