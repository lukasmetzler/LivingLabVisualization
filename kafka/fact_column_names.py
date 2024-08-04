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


fact_table_column_names = {
    "fact_user_input_facts": fact_user_input_facts_column_names,
    "fact_sensory": fact_sensory_column_names,
    "fact_raffstore_light_facts": fact_raffstore_light_facts_column_names,
    "fact_environmental_data_facts": fact_environmental_data_facts_column_names,
}
