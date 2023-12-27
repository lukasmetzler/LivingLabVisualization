--- Dimensionstabellen
CREATE TABLE dim_metrological_data (
    metrological_data_id SERIAL PRIMARY KEY,
    GlobIrrVerAct Numeric,
    GlobalIrrHorAct Numeric,
    DifflrrHorAct Numeric,
    WindSpeedAct_ms Numeric,
    SunElevationAct Numeric,
    SunAzimuthAct Numeric,
    Longitude Numeric,
    Latitude Numeric,
    WindSpeedAct_kmh Numeric,
    WindDirectionAct Numeric,
    BrightnessNorthAct Numeric,
    BrightnessSouthAct Numeric,
    BrightnessWestAct Numeric,
    TwilightAct Numeric,
    GlobalIrrHorAct_2 Numeric,
    PrecipitationAct Numeric,
    AbsolutAirPressureAct Numeric,
    RelativeAirPressureAct Numeric,
    AbsoluteHumidityAct Numeric,
    RelativeHumidityAct Numeric,
    DewPointTempAct Numeric,
    HousingTemAct Numeric,
    RoomTempAct Numeric
)

CREATE TABLE dim_zed_body_tracking_1og_r1 (
    zed_body_tracking_id SERIAL PRIMARY KEY,
    is_new Boolean,
    is_tracked Boolean,
    camera_pitch Float,
    camera_roll Float,
    camera_yaw Float,
    body_list JSON
);

CREATE TABLE dim_pv_modul_data_1og_r1 (
    pv_modul_data_id SERIAL PRIMARY KEY,
    volt_meas_act_module1 Numeric,
    curr_meas_act_module1 Numeric,
    volt_meas_act_module2 Numeric,
    curr_meas_act_module2 Numeric
);

CREATE TABLE dim_illumination_datapoints_1og_r1 (
    illumination_datapoints_id SERIAL PRIMARY KEY,
    illum_mp1_act Numeric,
    illum_mp2_act Numeric,
    illum_mp3_act Numeric,
    illum_mp4_act Numeric
);

CREATE TABLE dim_raffstore_light_data_1og_r1 (
    raffstore_light_data_1og_r1_id SERIAL PRIMARY KEY,
    slat_ang1_act_1og_r1 Numeric,
    slat_pos1_act_1og_r1 Numeric,
    light1_act_1og_r1 Numeric,
    light2_act_1og_r1 Numeric
);

CREATE TABLE dim_raffstore_light_data_1og_r2 (
    raffstore_light_data_1og_r2_id SERIAL PRIMARY KEY,
    slat_ang1_act_1og_r2 Numeric,
    slat_pos1_act_1og_r2 Numeric,
    light1_act_1og_r2 Numeric
);

CREATE TABLE dim_raffstore_light_data_1og_r3 (
    raffstore_light_data_1og_r3_id SERIAL PRIMARY KEY,
    slat_ang1_act_1og_r3 Numeric,
    slat_pos1_act_1og_r3 Numeric,
    light1_act_1og_r3 Numeric
);

CREATE TABLE dim_raffstore_light_data_1og_r4 (
    raffstore_light_data_1og_r4_id SERIAL PRIMARY KEY,
    slat_ang1_act_1og_r4 Numeric,
    slat_pos1_act_1og_r4 Numeric,
    slat_ang2_act_1og_r4 Numeric,
    slat_pos2_act_1og_r4 Numeric,
    light1_act_1og_r4 Numeric,
    light2_act_1og_r4 Numeric
);


CREATE TABLE dim_raffstore_light_data_1og_r5 (
    raffstore_light_data_1og_r5_id SERIAL PRIMARY KEY,
    slat_ang1_act_1og_r5 Numeric,
    slat_pos1_act_1og_r5 Numeric,
    slat_ang2_act_1og_r5 Numeric,
    slat_pos2_act_1og_r5 Numeric,
    slat_ang3_act_1og_r5 Numeric,
    slat_pos3_act_1og_r5 Numeric,
    light1_act_1og_r5 Numeric
);


CREATE TABLE dim_user_input_mp1_1og_r1 (
    user_input_mp1_id SERIAL PRIMARY KEY,
    mp1_glare_limit Numeric,
    mp1_req_illum Numeric,
    mp1_req_room_temp Numeric
);

CREATE TABLE dim_user_input_mp2_1og_r1 (
    user_input_mp2_id SERIAL PRIMARY KEY,
    mp2_glare_limit Numeric,
    mp2_req_illum Numeric,
    mp2_req_room_temp Numeric
);

CREATE TABLE dim_user_input_mp3_1og_r1 (
    user_input_mp3_id SERIAL PRIMARY KEY,
    mp3_glare_limit Numeric,
    mp3_req_illum Numeric,
    mp3_req_room_temp Numeric
);

CREATE TABLE dim_user_input_mp4_1og_r1 (
    user_input_mp4_id SERIAL PRIMARY KEY,
    mp4_glare_limit Numeric,
    mp4_req_illum Numeric,
    mp4_req_room_temp Numeric
);

CREATE TABLE dim_indihella_calc_var_radiance_1og_r1 (
    indi_hella_calc_var_radiance_ih_id SERIAL PRIMARY KEY,
    altitude_radiance_ih Numeric,
    azimut_radiance_ih Numeric,
    xdir_radiance_ih Numeric,
    ydir_radiance_ih Numeric,
    zdir_radiance_ih Numeric,
    irr_dir_nor_radiance_ih Numeric,
    profile_angle_radiance_ih Numeric,
    epsilon_radiance_ih Numeric,
    delta_radiance_ih Numeric,
    water_precipitable_radiance_ih Numeric,
    sunny_radiance_ih Numeric,
    cutoff_tilt_radiance_ih Numeric
)

CREATE TABLE dim_indihella_target_var_1og_r1 (
    indi_hella_tar_var_ih_id SERIAL PRIMARY KEY,
    slat_ang_tar_ih Numeric,
    slat_pos_tar_ih Numeric,
    light1_tar_ih Numeric,
    light2_tar_ih Numeric
)

CREATE TABLE dim_indihella_dgp_var_1og_r1 (
    indi_hella_dgp_var_ih_id SERIAL PRIMARY KEY,
    dgpmp1_0_100_ih Numeric,
    dgpmp1_5_100_ih Numeric,
    dgpmp1_10_100_ih Numeric,
    dgpmp1_15_100_ih Numeric,
    dgpmp1_20_100_ih Numeric,
    dgpmp1_25_100_ih Numeric,
    dgpmp1_30_100_ih Numeric,
    dgpmp1_35_100_ih Numeric,
    dgpmp1_40_100_ih Numeric,
    dgpmp1_45_100_ih Numeric,
    dgpmp1_50_100_ih Numeric,
    dgpmp1_55_100_ih Numeric,
    dgpmp1_60_100_ih Numeric,
    dgpmp1_65_100_ih Numeric,
    dgpmp1_70_100_ih Numeric,
    dgpmp1_75_100_ih Numeric,
    dgpmp1_80_100_ih Numeric,
    dgpmp1_85_100_ih Numeric,
    dgpmp1_0_0_ih Numeric,
    dgpmp2_0_100_ih Numeric,
    dgpmp2_5_100_ih Numeric,
    dgpmp2_10_100_ih Numeric,
    dgpmp2_15_100_ih Numeric,
    dgpmp2_20_100_ih Numeric,
    dgpmp2_25_100_ih Numeric,
    dgpmp2_30_100_ih Numeric,
    dgpmp2_35_100_ih Numeric,
    dgpmp2_40_100_ih Numeric,
    dgpmp2_45_100_ih Numeric,
    dgpmp2_50_100_ih Numeric,
    dgpmp2_55_100_ih Numeric,
    dgpmp2_60_100_ih Numeric,
    dgpmp2_65_100_ih Numeric,
    dgpmp2_70_100_ih Numeric,
    dgpmp2_75_100_ih Numeric,
    dgpmp2_80_100_ih Numeric,
    dgpmp2_85_100_ih Numeric,
    dgpmp2_0_0_ih Numeric,
    dgpmp3_0_100_ih Numeric,
    dgpmp3_5_100_ih Numeric,
    dgpmp3_10_100_ih Numeric,
    dgpmp3_15_100_ih Numeric,
    dgpmp3_20_100_ih Numeric,
    dgpmp3_25_100_ih Numeric,
    dgpmp3_30_100_ih Numeric,
    dgpmp3_35_100_ih Numeric,
    dgpmp3_40_100_ih Numeric,
    dgpmp3_45_100_ih Numeric,
    dgpmp3_50_100_ih Numeric,
    dgpmp3_55_100_ih Numeric,
    dgpmp3_60_100_ih Numeric,
    dgpmp3_65_100_ih Numeric,
    dgpmp3_70_100_ih Numeric,
    dgpmp3_75_100_ih Numeric,
    dgpmp3_80_100_ih Numeric,
    dgpmp3_85_100_ih Numeric,
    dgpmp3_0_0_ih Numeric,
    dgpmp4_0_100_ih Numeric,
    dgpmp4_5_100_ih Numeric,
    dgpmp4_10_100_ih Numeric,
    dgpmp4_15_100_ih Numeric,
    dgpmp4_20_100_ih Numeric,
    dgpmp4_25_100_ih Numeric,
    dgpmp4_30_100_ih Numeric,
    dgpmp4_35_100_ih Numeric,
    dgpmp4_40_100_ih Numeric,
    dgpmp4_45_100_ih Numeric,
    dgpmp4_50_100_ih Numeric,
    dgpmp4_55_100_ih Numeric,
    dgpmp4_60_100_ih Numeric,
    dgpmp4_65_100_ih Numeric,
    dgpmp4_70_100_ih Numeric,
    dgpmp4_75_100_ih Numeric,
    dgpmp4_80_100_ih Numeric,
    dgpmp4_85_100_ih Numeric,
    dgpmp4_0_0_ih Numeric
)

CREATE TABLE dim_indihella_illum_var_mp1_1og_r1 (
    indi_hella_illum_var_mp1_id SERIAL PRIMARY KEY,
    hor_illummp1_0_100_ih Numeric,
    hor_illummp1_5_100_ih Numeric,
    hor_illummp1_10_100_ih Numeric,
    hor_illummp1_15_100_ih Numeric,
    hor_illummp1_20_100_ih Numeric,
    hor_illummp1_25_100_ih Numeric,
    hor_illummp1_30_100_ih Numeric,
    hor_illummp1_35_100_ih Numeric,
    hor_illummp1_40_100_ih Numeric,
    hor_illummp1_45_100_ih Numeric,
    hor_illummp1_50_100_ih Numeric,
    hor_illummp1_55_100_ih Numeric,
    hor_illummp1_60_100_ih Numeric,
    hor_illummp1_65_100_ih Numeric,
    hor_illummp1_70_100_ih Numeric,
    hor_illummp1_75_100_ih Numeric,
    hor_illummp1_80_100_ih Numeric,
    hor_illummp1_85_100_ih Numeric,
    hor_illummp1_0_0_ih Numeric,
    ver_illummp1_0_100_ih Numeric,
    ver_illummp1_5_100_ih Numeric,
    ver_illummp1_10_100_ih Numeric,
    ver_illummp1_15_100_ih Numeric,
    ver_illummp1_20_100_ih Numeric,
    ver_illummp1_25_100_ih Numeric,
    ver_illummp1_30_100_ih Numeric,
    ver_illummp1_35_100_ih Numeric,
    ver_illummp1_40_100_ih Numeric,
    ver_illummp1_45_100_ih Numeric,
    ver_illummp1_50_100_ih Numeric,
    ver_illummp1_55_100_ih Numeric,
    ver_illummp1_60_100_ih Numeric,
    ver_illummp1_65_100_ih Numeric,
    ver_illummp1_70_100_ih Numeric,
    ver_illummp1_75_100_ih Numeric,
    ver_illummp1_80_100_ih Numeric,
    ver_illummp1_85_100_ih Numeric,
    ver_illummp1_0_0_ih Numeric
)

CREATE TABLE dim_indihella_illum_var_mp2_1og_r1 (
    indi_hella_illum_var_mp2_id SERIAL PRIMARY KEY,
    hor_illummp2_0_100_ih Numeric,
    hor_illummp2_5_100_ih Numeric,
    hor_illummp2_10_100_ih Numeric,
    hor_illummp2_15_100_ih Numeric,
    hor_illummp2_20_100_ih Numeric,
    hor_illummp2_25_100_ih Numeric,
    hor_illummp2_30_100_ih Numeric,
    hor_illummp2_35_100_ih Numeric,
    hor_illummp2_40_100_ih Numeric,
    hor_illummp2_45_100_ih Numeric,
    hor_illummp2_50_100_ih Numeric,
    hor_illummp2_55_100_ih Numeric,
    hor_illummp2_60_100_ih Numeric,
    hor_illummp2_65_100_ih Numeric,
    hor_illummp2_70_100_ih Numeric,
    hor_illummp2_75_100_ih Numeric,
    hor_illummp2_80_100_ih Numeric,
    hor_illummp2_85_100_ih Numeric,
    hor_illummp2_0_0_ih Numeric,
    ver_illummp2_0_100_ih Numeric,
    ver_illummp2_5_100_ih Numeric,
    ver_illummp2_10_100_ih Numeric,
    ver_illummp2_15_100_ih Numeric,
    ver_illummp2_20_100_ih Numeric,
    ver_illummp2_25_100_ih Numeric,
    ver_illummp2_30_100_ih Numeric,
    ver_illummp2_35_100_ih Numeric,
    ver_illummp2_40_100_ih Numeric,
    ver_illummp2_45_100_ih Numeric,
    ver_illummp2_50_100_ih Numeric,
    ver_illummp2_55_100_ih Numeric,
    ver_illummp2_60_100_ih Numeric,
    ver_illummp2_65_100_ih Numeric,
    ver_illummp2_70_100_ih Numeric,
    ver_illummp2_75_100_ih Numeric,
    ver_illummp2_80_100_ih Numeric,
    ver_illummp2_85_100_ih Numeric,
    ver_illummp2_0_0_ih Numeric
)


CREATE TABLE dim_indihella_illum_var_mp3_1og_r1 (
    indi_hella_illum_var_mp3_id SERIAL PRIMARY KEY,
    hor_illummp3_0_100_ih Numeric,
    hor_illummp3_5_100_ih Numeric,
    hor_illummp3_10_100_ih Numeric,
    hor_illummp3_15_100_ih Numeric,
    hor_illummp3_20_100_ih Numeric,
    hor_illummp3_25_100_ih Numeric,
    hor_illummp3_30_100_ih Numeric,
    hor_illummp3_35_100_ih Numeric,
    hor_illummp3_40_100_ih Numeric,
    hor_illummp3_45_100_ih Numeric,
    hor_illummp3_50_100_ih Numeric,
    hor_illummp3_55_100_ih Numeric,
    hor_illummp3_60_100_ih Numeric,
    hor_illummp3_65_100_ih Numeric,
    hor_illummp3_70_100_ih Numeric,
    hor_illummp3_75_100_ih Numeric,
    hor_illummp3_80_100_ih Numeric,
    hor_illummp3_85_100_ih Numeric,
    hor_illummp3_0_0_ih Numeric,
    ver_illummp3_0_100_ih Numeric,
    ver_illummp3_5_100_ih Numeric,
    ver_illummp3_10_100_ih Numeric,
    ver_illummp3_15_100_ih Numeric,
    ver_illummp3_20_100_ih Numeric,
    ver_illummp3_25_100_ih Numeric,
    ver_illummp3_30_100_ih Numeric,
    ver_illummp3_35_100_ih Numeric,
    ver_illummp3_40_100_ih Numeric,
    ver_illummp3_45_100_ih Numeric,
    ver_illummp3_50_100_ih Numeric,
    ver_illummp3_55_100_ih Numeric,
    ver_illummp3_60_100_ih Numeric,
    ver_illummp3_65_100_ih Numeric,
    ver_illummp3_70_100_ih Numeric,
    ver_illummp3_75_100_ih Numeric,
    ver_illummp3_80_100_ih Numeric,
    ver_illummp3_85_100_ih Numeric,
    ver_illummp3_0_0_ih Numeric
)

CREATE TABLE dim_indihella_illum_var_mp4_1og_r1 (
    indi_hella_illum_var_mp4_id SERIAL PRIMARY KEY,
    hor_illummp4_0_100_ih Numeric,
    hor_illummp4_5_100_ih Numeric,
    hor_illummp4_10_100_ih Numeric,
    hor_illummp4_15_100_ih Numeric,
    hor_illummp4_20_100_ih Numeric,
    hor_illummp4_25_100_ih Numeric,
    hor_illummp4_30_100_ih Numeric,
    hor_illummp4_35_100_ih Numeric,
    hor_illummp4_40_100_ih Numeric,
    hor_illummp4_45_100_ih Numeric,
    hor_illummp4_50_100_ih Numeric,
    hor_illummp4_55_100_ih Numeric,
    hor_illummp4_60_100_ih Numeric,
    hor_illummp4_65_100_ih Numeric,
    hor_illummp4_70_100_ih Numeric,
    hor_illummp4_75_100_ih Numeric,
    hor_illummp4_80_100_ih Numeric,
    hor_illummp4_85_100_ih Numeric,
    hor_illummp4_0_0_ih Numeric,
    ver_illummp4_0_100_ih Numeric,
    ver_illummp4_5_100_ih Numeric,
    ver_illummp4_10_100_ih Numeric,
    ver_illummp4_15_100_ih Numeric,
    ver_illummp4_20_100_ih Numeric,
    ver_illummp4_25_100_ih Numeric,
    ver_illummp4_30_100_ih Numeric,
    ver_illummp4_35_100_ih Numeric,
    ver_illummp4_40_100_ih Numeric,
    ver_illummp4_45_100_ih Numeric,
    ver_illummp4_50_100_ih Numeric,
    ver_illummp4_55_100_ih Numeric,
    ver_illummp4_60_100_ih Numeric,
    ver_illummp4_65_100_ih Numeric,
    ver_illummp4_70_100_ih Numeric,
    ver_illummp4_75_100_ih Numeric,
    ver_illummp4_80_100_ih Numeric,
    ver_illummp4_85_100_ih Numeric,
    ver_illummp4_0_0_ih Numeric
)

CREATE TABLE dim_radiation_forecast (
    radiation_forecast_id SERIAL primary KEY,
    global_irr_hor_approx Numeric,
    diff_irr_hor_act_approx Numeric
)

CREATE TABLE dim_head_positions_1og_r1 (
    head_positions_id SERIAL PRIMARY KEY,
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
    headpose_roll_4 Numeric
)

--- Faktentabellen
CREATE TABLE fact_user_input_facts (
    user_input_facts_id SERIAL PRIMARY KEY,
    timestamp timestamp,
    user_input_mp1_id int,
    user_input_mp2_id int,
    user_input_mp3_id int,
    user_input_mp4_id int,
    FOREIGN KEY (user_input_mp1_id) REFERENCES dim_user_input_mp1_1og_r1(user_input_mp1_id),
    FOREIGN KEY (user_input_mp2_id) REFERENCES dim_user_input_mp2_1og_r1(user_input_mp2_id),
    FOREIGN KEY (user_input_mp3_id) REFERENCES dim_user_input_mp3_1og_r1(user_input_mp3_id),
    FOREIGN KEY (user_input_mp4_id) REFERENCES dim_user_input_mp4_1og_r1(user_input_mp4_id)
)

CREATE TABLE fact_sensory (
    sensory_id SERIAL PRIMARY KEY,
    timestamp timestamp,
    zed_body_tracking_id int,
    FOREIGN KEY (zed_body_tracking_id) REFERENCES dim_zed_body_tracking_1og_r1(zed_body_tracking_id)
)

CREATE TABLE fact_raffstore_light_facts (
    raffstore_light_light_facts_id SERIAL PRIMARY KEY,
    timestamp timestamp,
    raffstore_light_data_1og_r1_id int,
    raffstore_light_data_1og_r2_id int,
    raffstore_light_data_1og_r3_id int,
    raffstore_light_data_1og_r4_id int,
    raffstore_light_data_1og_r5_id int,
    FOREIGN KEY (raffstore_light_data_1og_r1_id) REFERENCES dim_raffstore_light_data_1og_r1(raffstore_light_data_1og_r1_id),
    FOREIGN KEY (raffstore_light_data_1og_r2_id) REFERENCES dim_raffstore_light_data_1og_r2(raffstore_light_data_1og_r2_id),
    FOREIGN KEY (raffstore_light_data_1og_r3_id) REFERENCES dim_raffstore_light_data_1og_r3(raffstore_light_data_1og_r3_id),
    FOREIGN KEY (raffstore_light_data_1og_r4_id) REFERENCES dim_raffstore_light_data_1og_r4(raffstore_light_data_1og_r4_id),
    FOREIGN KEY (raffstore_light_data_1og_r5_id) REFERENCES dim_raffstore_light_data_1og_r5(raffstore_light_data_1og_r5_id)
)

CREATE TABLE fact_indi_hella_illum_facts (
    indi_hella_illum_var_facts_id SERIAL PRIMARY KEY,
    timestamp timestamp,
    indi_hella_illum_var_mp1_id int,
    indi_hella_illum_var_mp2_id int,
    indi_hella_illum_var_mp3_id int,
    indi_hella_illum_var_mp4_id int,
    FOREIGN KEY (indi_hella_illum_var_mp1_id) REFERENCES dim_indihella_illum_var_mp1_1og_r1(indi_hella_illum_var_mp1_id),
    FOREIGN KEY (indi_hella_illum_var_mp2_id) REFERENCES dim_indihella_illum_var_mp2_1og_r1(indi_hella_illum_var_mp2_id),
    FOREIGN KEY (indi_hella_illum_var_mp3_id) REFERENCES dim_indihella_illum_var_mp3_1og_r1(indi_hella_illum_var_mp3_id),
    FOREIGN KEY (indi_hella_illum_var_mp4_id) REFERENCES dim_indihella_illum_var_mp4_1og_r1(indi_hella_illum_var_mp4_id)
)

CREATE TABLE fact_indi_hella_calc_vars_facts (
    indi_hella_illum_var_facts_id SERIAL PRIMARY KEY,
    timestamp timestamp,
    indi_hella_calc_var_radiance_ih_id int,
    indi_hella_tar_var_ih_id int,
    indi_hella_dgp_var_ih_id int,
    FOREIGN KEY (indi_hella_calc_var_radiance_ih_id) REFERENCES dim_indihella_calc_var_radiance_1og_r1(indi_hella_calc_var_radiance_ih_id),
    FOREIGN KEY (indi_hella_tar_var_ih_id) REFERENCES dim_indihella_target_var_1og_r1(indi_hella_tar_var_ih_id),
    FOREIGN KEY (indi_hella_dgp_var_ih_id) REFERENCES dim_indihella_dgp_var_1og_r1(indi_hella_dgp_var_ih_id),
)

CREATE TABLE fact_environmental_data_facts (
    fact_table_id SERIAL PRIMARY KEY,
    timestamp timestamp,
    metrological_data_id int,
    pv_modul_data_id int,
    illumination_datapoints_id int,
    radiation_forecast_id int,
    head_positions_id int,
    
    FOREIGN KEY (metrological_data_id) REFERENCES dim_metrological_data(metrological_data_id),
    FOREIGN KEY (pv_modul_data_id) REFERENCES dim_pv_modul_data_1og_r1(pv_modul_data_id),
    FOREIGN KEY (illumination_datapoints_id) REFERENCES dim_illumination_datapoints_1og_r1(illumination_datapoints_id),
    FOREIGN KEY (radiation_forecast_id) REFERENCES dim_radiation_forecast(radiation_forecast_id),
    FOREIGN KEY (head_positions_id) REFERENCES dim_head_positions_1og_r1(head_positions_id)
)


