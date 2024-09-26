from sqlalchemy import (
    Column,
    String,
    Numeric,
    Boolean,
    JSON,
    TIMESTAMP,
    Integer,
    ForeignKey,
    func,
)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.postgresql import UUID

Base = declarative_base()


class DimMetrologicalData(Base):
    __tablename__ = "dim_metrological_data"
    metrological_data_id = Column(
        UUID(as_uuid=True), primary_key=True, server_default="uuid_generate_v4()"
    )
    glob_irr_ver_act = Column(Numeric)
    global_irr_hor_act = Column(Numeric)
    diff_irr_hor_act = Column(Numeric)
    wind_speed_act_ms = Column(Numeric)
    sun_elevation_act = Column(Numeric)
    sun_azimuth_act = Column(Numeric)
    longitude = Column(Numeric)
    latitude = Column(Numeric)
    wind_speed_act_kmh = Column(Numeric)
    wind_direction_act = Column(Numeric)
    brightness_north_act = Column(Numeric)
    brightness_south_act = Column(Numeric)
    brightness_west_act = Column(Numeric)
    twilight_act = Column(Numeric)
    global_irr_hor_act_2 = Column(Numeric)
    precipitation_act = Column(Numeric)
    absolut_air_pressure_act = Column(Numeric)
    relative_air_pressure_act = Column(Numeric)
    absolute_humidity_act = Column(Numeric)
    relative_humidity_act = Column(Numeric)
    dew_point_temp_act = Column(Numeric)
    housing_temp_act = Column(Numeric)
    room_temp_act = Column(Numeric)
    created_at = Column(TIMESTAMP, server_default=func.current_timestamp())


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
    created_at = Column(TIMESTAMP, server_default=func.current_timestamp())


class DimPvModulData1ogR1(Base):
    __tablename__ = "dim_pv_modul_data_1og_r1"
    pv_modul_data_id = Column(
        UUID(as_uuid=True), primary_key=True, server_default="uuid_generate_v4()"
    )
    volt_meas_act_module1 = Column(Numeric)
    curr_meas_act_module1 = Column(Numeric)
    volt_meas_act_module2 = Column(Numeric)
    curr_meas_act_module2 = Column(Numeric)
    created_at = Column(TIMESTAMP, server_default=func.current_timestamp())


class DimIlluminationDatapoints1ogR1(Base):
    __tablename__ = "dim_illumination_datapoints_1og_r1"
    illumination_datapoints_id = Column(
        UUID(as_uuid=True), primary_key=True, server_default="uuid_generate_v4()"
    )
    illum_mp1_act = Column(Numeric)
    illum_mp2_act = Column(Numeric)
    illum_mp3_act = Column(Numeric)
    illum_mp4_act = Column(Numeric)
    created_at = Column(TIMESTAMP, server_default=func.current_timestamp())


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
    created_at = Column(TIMESTAMP, server_default=func.current_timestamp())


class DimUserInput(Base):
    __tablename__ = "dim_user_input"
    user_input_id = Column(
        UUID(as_uuid=True), primary_key=True, server_default="uuid_generate_v4()"
    )
    mp_glare_limit = Column(Numeric)
    mp_req_illum = Column(Numeric)
    mp_req_room_temp = Column(Numeric)
    measurement_point = Column(Integer)
    created_at = Column(TIMESTAMP, server_default=func.current_timestamp())


class DimLocation(Base):
    __tablename__ = "dim_location"
    location_id = Column(
        UUID(as_uuid=True), primary_key=True, server_default="uuid_generate_v4()"
    )
    room_number = Column(Integer)
    building = Column(String(50))
    created_at = Column(TIMESTAMP, server_default=func.current_timestamp())


class DimRadiationForecast(Base):
    __tablename__ = "dim_radiation_forecast"
    radiation_forecast_id = Column(
        UUID(as_uuid=True), primary_key=True, server_default="uuid_generate_v4()"
    )
    global_irr_hor_approx = Column(Numeric)
    diff_irr_hor_act_approx = Column(Numeric)
    created_at = Column(TIMESTAMP, server_default=func.current_timestamp())


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
    created_at = Column(TIMESTAMP, server_default=func.current_timestamp())


class FactEnvironmentalDataFacts(Base):
    __tablename__ = "fact_environmental_data_facts"
    environmental_data_facts_id = Column(
        UUID(as_uuid=True), primary_key=True, server_default="uuid_generate_v4()"
    )
    location_id = Column(
        UUID(as_uuid=True), ForeignKey("dim_location.location_id"), nullable=True
    )
    metrological_data_id = Column(
        UUID(as_uuid=True),
        ForeignKey("dim_metrological_data.metrological_data_id"),
        nullable=True,
    )
    pv_modul_data_id = Column(
        UUID(as_uuid=True),
        ForeignKey("dim_pv_modul_data_1og_r1.pv_modul_data_id"),
        nullable=True,
    )
    illumination_datapoints_id = Column(
        UUID(as_uuid=True),
        ForeignKey("dim_illumination_datapoints_1og_r1.illumination_datapoints_id"),
        nullable=True,
    )
    radiation_forecast_id = Column(
        UUID(as_uuid=True),
        ForeignKey("dim_radiation_forecast.radiation_forecast_id"),
        nullable=True,
    )
    head_positions_id = Column(
        UUID(as_uuid=True),
        ForeignKey("dim_head_positions_1og_r1.head_positions_id"),
        nullable=True,
    )

    __tablename__ = "fact_environmental_data_facts"
    environmental_data_facts_id = Column(
        UUID(as_uuid=True), primary_key=True, server_default="uuid_generate_v4()"
    )
    location_id = Column(
        UUID(as_uuid=True), ForeignKey("dim_location.location_id"), nullable=True
    )
    metrological_data_id = Column(
        UUID(as_uuid=True),
        ForeignKey("dim_metrological_data.metrological_data_id"),
        nullable=True,
    )
    pv_modul_data_id = Column(
        UUID(as_uuid=True),
        ForeignKey("dim_pv_modul_data_1og_r1.pv_modul_data_id"),
        nullable=True,
    )
    illumination_datapoints_id = Column(
        UUID(as_uuid=True),
        ForeignKey("dim_illumination_datapoints_1og_r1.illumination_datapoints_id"),
        nullable=True,
    )
    radiation_forecast_id = Column(
        UUID(as_uuid=True),
        ForeignKey("dim_radiation_forecast.radiation_forecast_id"),
        nullable=True,
    )
    head_positions_id = Column(
        UUID(as_uuid=True),
        ForeignKey("dim_head_positions_1og_r1.head_positions_id"),
        nullable=True,
    )

    __tablename__ = "fact_environmental_data_facts"
    environmental_data_facts_id = Column(
        UUID(as_uuid=True), primary_key=True, server_default="uuid_generate_v4()"
    )
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
    )  # Hinzugefügt

    location = relationship("DimLocation")
    metrological_data = relationship("DimMetrologicalData")
    pv_modul_data = relationship("DimPvModulData1ogR1")
    illumination_datapoints = relationship("DimIlluminationDatapoints1ogR1")
    radiation_forecast = relationship("DimRadiationForecast")
    head_positions = relationship("DimHeadPositions1ogR1")

    __tablename__ = "fact_environmental_data_facts"
    environmental_data_facts_id = Column(
        UUID(as_uuid=True), primary_key=True, server_default="uuid_generate_v4()"
    )
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

    location = relationship("DimLocation")
    metrological_data = relationship("DimMetrologicalData")
    pv_modul_data = relationship("DimPvModulData1ogR1")
    illumination_datapoints = relationship("DimIlluminationDatapoints1ogR1")
    radiation_forecast = relationship("DimRadiationForecast")
    head_positions = relationship("DimHeadPositions1ogR1")


class FactUserInputFacts(Base):
    __tablename__ = "fact_user_input_facts"
    user_input_facts_id = Column(
        UUID(as_uuid=True), primary_key=True, server_default="uuid_generate_v4()"
    )
    location_id = Column(UUID(as_uuid=True), ForeignKey("dim_location.location_id"))
    user_input_id = Column(
        UUID(as_uuid=True), ForeignKey("dim_user_input.user_input_id")
    )

    location = relationship("DimLocation")
    user_input = relationship("DimUserInput")


class FactSensory(Base):
    __tablename__ = "fact_sensory"
    sensory_id = Column(
        UUID(as_uuid=True), primary_key=True, server_default="uuid_generate_v4()"
    )
    location_id = Column(UUID(as_uuid=True), ForeignKey("dim_location.location_id"))
    zed_body_tracking_id = Column(
        UUID(as_uuid=True),
        ForeignKey("dim_zed_body_tracking_1og_r1.zed_body_tracking_id"),
    )

    location = relationship("DimLocation")
    zed_body_tracking = relationship("DimZedBodyTracking1ogR1")


class FactRaffstoreLightFacts(Base):
    __tablename__ = "fact_raffstore_light_facts"
    raffstore_light_facts_id = Column(
        UUID(as_uuid=True), primary_key=True, server_default="uuid_generate_v4()"
    )
    location_id = Column(UUID(as_uuid=True), ForeignKey("dim_location.location_id"))
    raffstore_light_data_id = Column(
        UUID(as_uuid=True),
        ForeignKey("dim_raffstore_light_data.raffstore_light_data_id"),
    )
    location = relationship("DimLocation")
    raffstore_light_data = relationship("DimRaffstoreLightData")


engine = create_engine(
    f"postgresql+psycopg2://{c.CONSUMER_POSTGRES_USER}:{c.CONSUMER_POSTGRES_PASSWORD}@{c.CONSUMER_POSTGRES_HOST}:{c.CONSUMER_POSTGRES_PORT}/{c.CONSUMER_POSTGRES_DB}"
)
Base.metadata.create_all(engine)
