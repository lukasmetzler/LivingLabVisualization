fact_user_input_facts_column_names = [
    "user_input_mp1_id",
    "user_input_mp2_id",
    "user_input_mp3_id",
    "user_input_mp4_id",
]

fact_sensory_column_names = [
    "zed_body_tracking_id",
]

fact_raffstore_light_facts_column_names = [
    "raffstore_light_data_1og_r1_id",
    "raffstore_light_data_1og_r2_id",
    "raffstore_light_data_1og_r3_id",
    "raffstore_light_data_1og_r4_id",
    "raffstore_light_data_1og_r5_id",
]

fact_indi_hella_illum_facts_column_names = [
    "indi_hella_illum_var_mp1_id",
    "indi_hella_illum_var_mp2_id",
    "indi_hella_illum_var_mp3_id",
    "indi_hella_illum_var_mp4_id",
]

fact_indi_hella_calc_vars_facts_column_names = [
    "indi_hella_calc_var_radiance_ih_id",
    "indi_hella_tar_var_ih_id",
    "indi_hella_dgp_var_ih_id",
]

fact_environmental_data_facts_column_names = [
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
    "fact_indi_hella_illum_facts": fact_indi_hella_illum_facts_column_names,
    "fact_indi_hella_calc_vars_facts": fact_indi_hella_calc_vars_facts_column_names,
    "fact_environmental_data_facts": fact_environmental_data_facts_column_names,
}
