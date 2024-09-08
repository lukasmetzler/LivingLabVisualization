SELECT * FROM pg_extension WHERE extname = 'UUID-ossp';

CREATE EXTENSION IF NOT EXISTS "uuid-ossp";

--- Dimensionstabellen

CREATE TABLE dim_metrological_data (
    metrological_data_id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    glob_irr_ver_act Numeric,
    global_irr_hor_act Numeric,
    diff_irr_hor_act Numeric,
    wind_speed_act_ms Numeric,
    sun_elevation_act Numeric,
    sun_azimuth_act Numeric,
    longitude Numeric,
    latitude Numeric,
    wind_speed_act_kmh Numeric,
    wind_direction_act Numeric,
    brightness_north_act Numeric,
    brightness_south_act Numeric,
    brightness_west_act Numeric,
    twilight_act Numeric,
    global_irr_hor_act_2 Numeric,
    precipitation_act Numeric,
    absolut_air_pressure_act Numeric,
    relative_air_pressure_act Numeric,
    absolute_humidity_act Numeric,
    relative_humidity_act Numeric,
    dew_point_temp_act Numeric,
    housing_temp_act Numeric,
    room_temp_act Numeric
    created_at TIMESTAMPTZ DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE dim_zed_body_tracking_1og_r1 (
    zed_body_tracking_id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    is_new BOOLEAN DEFAULT FALSE,
    is_tracked BOOLEAN DEFAULT FALSE,
    camera_pitch NUMERIC,
    camera_roll NUMERIC,
    camera_yaw NUMERIC,
    body_list JSON DEFAULT '[]'::JSON,
    created_at TIMESTAMPTZ DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE dim_pv_modul_data_1og_r1 (
    pv_modul_data_id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    volt_meas_act_module1 Numeric,
    curr_meas_act_module1 Numeric,
    volt_meas_act_module2 Numeric,
    curr_meas_act_module2 Numeric,
    created_at TIMESTAMPTZ DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE dim_illumination_datapoints_1og_r1 (
    illumination_datapoints_id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    illum_mp1_act Numeric,
    illum_mp2_act Numeric,
    illum_mp3_act Numeric,
    illum_mp4_act Numeric,
    created_at TIMESTAMPTZ DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE dim_raffstore_light_data (
    raffstore_light_data_id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    room_number INTEGER,
    slat_ang1_act Numeric,
    slat_pos1_act Numeric,
    slat_ang2_act Numeric,
    slat_pos2_act Numeric,
    slat_ang3_act Numeric,
    slat_pos3_act Numeric,
    light1_act Numeric,
    light2_act Numeric,
    created_at TIMESTAMPTZ DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE dim_user_input (
    user_input_id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    mp_glare_limit Numeric,
    mp_req_illum Numeric,
    mp_req_room_temp Numeric,
    measurement_point INTEGER,
    created_at TIMESTAMPTZ DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE dim_time (
    time_id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    timestamp TIMESTAMPTZ,
    date DATE,
    day_of_week VARCHAR(10),
    month VARCHAR(10),
    quarter VARCHAR(2),
    year INTEGER,
    hour INTEGER,
    created_at TIMESTAMPTZ DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE dim_location (
    location_id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    room_number INTEGER,
    building VARCHAR(50),
    created_at TIMESTAMPTZ DEFAULT CURRENT_TIMESTAMP
);

--- Faktentabellen

CREATE TABLE fact_user_input_facts (
    user_input_facts_id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    time_id UUID,
    location_id UUID,
    user_input_id UUID,
    FOREIGN KEY (time_id) REFERENCES dim_time(time_id),
    FOREIGN KEY (location_id) REFERENCES dim_location(location_id),
    FOREIGN KEY (user_input_id) REFERENCES dim_user_input(user_input_id)
);

CREATE TABLE fact_sensory (
    sensory_id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    time_id UUID,
    location_id UUID,
    zed_body_tracking_id UUID,
    FOREIGN KEY (time_id) REFERENCES dim_time(time_id),
    FOREIGN KEY (location_id) REFERENCES dim_location(location_id),
    FOREIGN KEY (zed_body_tracking_id) REFERENCES dim_zed_body_tracking_1og_r1(zed_body_tracking_id)
);

CREATE TABLE fact_raffstore_light_facts (
    raffstore_light_facts_id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    time_id UUID,
    location_id UUID,
    raffstore_light_data_id UUID,
    FOREIGN KEY (time_id) REFERENCES dim_time(time_id),
    FOREIGN KEY (location_id) REFERENCES dim_location(location_id),
    FOREIGN KEY (raffstore_light_data_id) REFERENCES dim_raffstore_light_data(raffstore_light_data_id)
);

CREATE TABLE fact_environmental_data_facts (
    environmental_data_facts_id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    time_id UUID,
    location_id UUID,
    metrological_data_id UUID,
    pv_modul_data_id UUID,
    illumination_datapoints_id UUID,
    radiation_forecast_id UUID,
    head_positions_id UUID,
    FOREIGN KEY (time_id) REFERENCES dim_time(time_id),
    FOREIGN KEY (location_id) REFERENCES dim_location(location_id),
    FOREIGN KEY (metrological_data_id) REFERENCES dim_metrological_data(metrological_data_id),
    FOREIGN KEY (pv_modul_data_id) REFERENCES dim_pv_modul_data_1og_r1(pv_modul_data_id),
    FOREIGN KEY (illumination_datapoints_id) REFERENCES dim_illumination_datapoints_1og_r1(illumination_datapoints_id),
    FOREIGN KEY (radiation_forecast_id) REFERENCES dim_radiation_forecast(radiation_forecast_id),
    FOREIGN KEY (head_positions_id) REFERENCES dim_head_positions_1og_r1(head_positions_id)
);

CREATE TABLE dim_radiation_forecast (
    radiation_forecast_id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    global_irr_hor_approx Numeric,
    diff_irr_hor_act_approx Numeric,
    created_at TIMESTAMPTZ DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE dim_head_positions_1og_r1 (
    head_positions_id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    headpose_x_1 Numeric,
    headpose_y_1 Numeric,
    headpose_z_1 Numeric,
    headpose_pitch_1 Numeric,
    headpose_yaw_1 Numeric,
    headpose_roll_1 Numeric,
    headpose_x_2 Numeric,
    headpose_y_2 Numeric,
    headpose_z_2 Numeric,
    headpose_pitch_2 Numeric,
    headpose_yaw_2 Numeric,
    headpose_roll_2 Numeric,
    headpose_x_3 Numeric,
    headpose_y_3 Numeric,
    headpose_z_3 Numeric,
    headpose_pitch_3 Numeric,
    headpose_yaw_3 Numeric,
    headpose_roll_3 Numeric,
    headpose_x_4 Numeric,
    headpose_y_4 Numeric,
    headpose_z_4 Numeric,
    headpose_pitch_4 Numeric,
    headpose_yaw_4 Numeric,
    headpose_roll_4 Numeric,
    created_at TIMESTAMPTZ DEFAULT CURRENT_TIMESTAMP
);
