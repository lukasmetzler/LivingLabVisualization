dim_metrological_column_names = [
    "metrological_data_id",
    "GlobIrrVerAct",
    "GlobalIrrHorAct",
    "DifflrrHorAct",
    "WindSpeedAct_ms",
    "SunElevationAct",
    "SunAzimuthAct",
    "Longitude",
    "Latitude",
    "WindSpeedAct_kmh",
    "WindDirectionAct",
    "BrightnessNorthAct",
    "BrightnessSouthAct",
    "BrightnessWestAct",
    "TwilightAct",
    "GlobalIrrHorAct_2",
    "PrecipitationAct",
    "AbsolutAirPressureAct",
    "RelativeAirPressureAct",
    "AbsoluteHumidityAct",
    "RelativeHumidityAct",
    "DewPointTempAct",
    "HousingTemAct",
    "RoomTempAct",
]

dim_zed_body_tracking_1og_r1_column_names = [
    "zed_body_tracking_id",
    "is_new",
    "is_tracked",
    "camera_pitch",
    "camera_roll",
    "camera_yaw",
    "body_list",
]

dim_pv_modul_data_1og_r1_column_names = [
    "pv_modul_data_id",
    "volt_meas_act_module1",
    "curr_meas_act_module1",
    "volt_meas_act_module2",
    "curr_meas_act_module2",
]

dim_illumination_datapoints_1og_r1_column_names = [
    "illumination_datapoints_id",
    "illum_mp1_act",
    "illum_mp2_act",
    "illum_mp3_act",
    "illum_mp4_act",
]

dim_raffstore_light_data_column_names = [
    "raffstore_light_data_id",
    "room_number",
    "slat_ang1_act",
    "slat_pos1_act",
    "slat_ang2_act",
    "slat_pos2_act",
    "slat_ang3_act",
    "slat_pos3_act",
    "light1_act",
    "light2_act",
]

dim_user_input_column_names = [
    "user_input_id",
    "mp_glare_limit",
    "mp_req_illum",
    "mp_req_room_temp",
    "measurement_point",
]

dim_time_column_names = [
    "time_id",
    "timestamp",
    "date",
    "day_of_week",
    "month",
    "quarter",
    "year",
    "hour",
]

dim_location_column_names = [
    "location_id",
    "room_number",
    "building",
]

dim_radiation_forecast_column_names = [
    "radiation_forecast_id",
    "global_irr_hor_approx",
    "diff_irr_hor_act_approx",
]

dim_head_positions_1og_r1_column_names = [
    "head_positions_id",
    "headpose_x_1",
    "headpose_y_1",
    "headpose_z_1",
    "headpose_pitch_1",
    "headpose_yaw_1",
    "headpose_roll_1",
    "headpose_x_2",
    "headpose_y_2",
    "headpose_z_2",
    "headpose_pitch_2",
    "headpose_yaw_2",
    "headpose_roll_2",
    "headpose_x_3",
    "headpose_y_3",
    "headpose_z_3",
    "headpose_pitch_3",
    "headpose_yaw_3",
    "headpose_roll_3",
    "headpose_x_4",
    "headpose_y_4",
    "headpose_z_4",
    "headpose_pitch_4",
    "headpose_yaw_4",
    "headpose_roll_4",
]

fact_user_input_facts_column_names = [
    "user_input_facts_id",
    "time_id",
    "location_id",
    "user_input_id",
]

fact_sensory_column_names = [
    "sensory_id",
    "time_id",
    "location_id",
    "zed_body_tracking_id",
]

fact_raffstore_light_facts_column_names = [
    "raffstore_light_facts_id",
    "time_id",
    "location_id",
    "raffstore_light_data_id",
]

fact_environmental_data_facts_column_names = [
    "environmental_data_facts_id",
    "time_id",
    "location_id",
    "metrological_data_id",
    "pv_modul_data_id",
    "illumination_datapoints_id",
    "radiation_forecast_id",
    "head_positions_id",
]

table_column_names = {
    "dim_metrological_data": dim_metrological_column_names,
    "dim_zed_body_tracking_1og_r1": dim_zed_body_tracking_1og_r1_column_names,
    "dim_pv_modul_data_1og_r1": dim_pv_modul_data_1og_r1_column_names,
    "dim_illumination_datapoints_1og_r1": dim_illumination_datapoints_1og_r1_column_names,
    "dim_raffstore_light_data": dim_raffstore_light_data_column_names,
    "dim_user_input": dim_user_input_column_names,
    "dim_time": dim_time_column_names,
    "dim_location": dim_location_column_names,
    "dim_radiation_forecast": dim_radiation_forecast_column_names,
    "dim_head_positions_1og_r1": dim_head_positions_1og_r1_column_names,
    "fact_user_input_facts": fact_user_input_facts_column_names,
    "fact_sensory": fact_sensory_column_names,
    "fact_raffstore_light_facts": fact_raffstore_light_facts_column_names,
    "fact_environmental_data_facts": fact_environmental_data_facts_column_names,
}
