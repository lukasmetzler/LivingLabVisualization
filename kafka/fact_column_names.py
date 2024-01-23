fact_user_input_facts_column_names = {
    "timestamp": "TIMESTAMPTZ DEFAULT CURRENT_TIMESTAMP",
    "user_input_mp1_id": "int",
    "user_input_mp2_id": "int",
    "user_input_mp3_id": "int",
    "user_input_mp4_id": "int",
}

fact_sensory_column_names = {
    "timestamp": "TIMESTAMPTZ DEFAULT CURRENT_TIMESTAMP",
    "zed_body_tracking_id": "int",
}

fact_raffstore_light_facts_column_names = {
    "timestamp": "TIMESTAMPTZ DEFAULT CURRENT_TIMESTAMP",
    "raffstore_light_data_1og_r1_id": "int",
    "raffstore_light_data_1og_r2_id": "int",
    "raffstore_light_data_1og_r3_id": "int",
    "raffstore_light_data_1og_r4_id": "int",
    "raffstore_light_data_1og_r5_id": "int",
}

fact_indi_hella_illum_facts_column_names = {
    "timestamp": "TIMESTAMPTZ DEFAULT CURRENT_TIMESTAMP",
    "indi_hella_illum_var_mp1_id": "int",
    "indi_hella_illum_var_mp2_id": "int",
    "indi_hella_illum_var_mp3_id": "int",
    "indi_hella_illum_var_mp4_id": "int",
}

fact_indi_hella_calc_vars_facts_column_names = {
    "timestamp": "TIMESTAMPTZ DEFAULT CURRENT_TIMESTAMP",
    "indi_hella_calc_var_radiance_ih_id": "int",
    "indi_hella_tar_var_ih_id": "int",
    "indi_hella_dgp_var_ih_id": "int",
}

fact_environmental_data_facts_column_names = {
    "timestamp": "TIMESTAMPTZ DEFAULT CURRENT_TIMESTAMP",
    "metrological_data_id": "int",
    "pv_modul_data_id": "int",
    "illumination_datapoints_id": "int",
    "radiation_forecast_id": "int",
    "head_positions_id": "int",
}
