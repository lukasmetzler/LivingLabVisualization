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
    func,
    event,
)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
from config import load_config
from datetime import datetime


c = load_config()
Base = declarative_base()


class DimMetrologicalData(Base):
    __tablename__ = "dim_metrological_data"
    metrological_data_id = Column(
        UUID(as_uuid=True), primary_key=True, server_default="uuid_generate_v4()"
    )
    GlobIrrVerAct = Column(Numeric)
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
    created_at = Column(TIMESTAMP, server_default=func.current_timestamp())


class DimTime(Base):
    __tablename__ = "dim_time"
    time_id = Column(
        UUID(as_uuid=True), primary_key=True, server_default=func.uuid_generate_v4()
    )
    timestamp = Column(TIMESTAMP, nullable=False)
    date = Column(String)
    day_of_week = Column(String)
    month = Column(String)
    quarter = Column(String)
    year = Column(Integer)
    hour = Column(Integer)
    created_at = Column(TIMESTAMP, server_default=func.current_timestamp())

    def __init__(self, timestamp=None):
        if timestamp:
            self.timestamp = timestamp
            self.date = timestamp.strftime("%Y-%m-%d")
            self.day_of_week = timestamp.strftime("%A")
            self.month = timestamp.strftime("%B")
            self.quarter = f"Q{((timestamp.month - 1) // 3) + 1}"
            self.year = timestamp.year
            self.hour = timestamp.hour

    @classmethod
    def from_datetime(cls, dt):
        return cls(timestamp=dt)


@event.listens_for(DimTime, "before_insert")
def receive_before_insert(mapper, connection, target):
    if target.timestamp:
        target.date = target.timestamp.strftime("%Y-%m-%d")
        target.day_of_week = target.timestamp.strftime("%A")
        target.month = target.timestamp.strftime("%B")
        target.quarter = f"Q{((target.timestamp.month - 1) // 3) + 1}"
        target.year = target.timestamp.year
        target.hour = target.timestamp.hour


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
    illumination_data_id = Column(
        UUID(as_uuid=True), primary_key=True, server_default="uuid_generate_v4()"
    )
    illuminance = Column(Numeric)
    illuminance_type = Column(String)
    created_at = Column(TIMESTAMP, server_default=func.current_timestamp())


class FactEnvironmentalDataFacts(Base):
    __tablename__ = "fact_environmental_data_facts"
    fact_id = Column(
        UUID(as_uuid=True), primary_key=True, server_default=func.uuid_generate_v4()
    )
    time_id = Column(UUID(as_uuid=True), ForeignKey("dim_time.time_id"))
    metrological_data_id = Column(
        UUID(as_uuid=True), ForeignKey("dim_metrological_data.metrological_data_id")
    )
    created_at = Column(TIMESTAMP, server_default=func.current_timestamp())

    time = relationship("DimTime")
    metrological_data = relationship("DimMetrologicalData")


engine = create_engine(
    f"postgresql+psycopg2://{c.CONSUMER_POSTGRES_USER}:{c.CONSUMER_POSTGRES_PASSWORD}@{c.CONSUMER_POSTGRES_HOST}:{c.CONSUMER_POSTGRES_PORT}/{c.CONSUMER_POSTGRES_DB}"
)
Base.metadata.create_all(engine)
