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

CREATE TABLE dim_pv_modul_data_1og_r1 (
    pv_modul_data_id SERIAL PRIMARY KEY,
    VoltMeasActModule1 Numeric,
    CurrMeasActModule1 Numeric,
    VoltMeasActModule2 Numeric,
    CurrMeasActModule2 Numeric
)

CREATE TABLE dim_illumination_datapoints_1og_r1 (
    illumination_datapoints_id SERIAL PRIMARY KEY,
    IllumMP1Act Numeric,
    IllumMP2Act Numeric,
    IllumMP3Act Numeric,
    IllumMP4Act Numeric
)

CREATE TABLE dim_raffstore_light_data_1og_r1 (
    raffstore_light_data_1og_r1_id SERIAL PRIMARY KEY,
    SlatAng1Act_1OG_R1 Numeric,
    SlatPos1Act_1OG_R1 Numeric,
    Light1Act_1OG_R1 Numeric,
    Light2Act_1OG_R1 Numeric
)

CREATE TABLE dim_raffstore_light_data_1og_r2 (
    raffstore_light_data_1og_r2_id SERIAL PRIMARY KEY,
    SlatAng1Act_1OG_R2 Numeric,
    SlatPos1Act_1OG_R2 Numeric,
    Light1Act_1OG_R2 Numeric
)

CREATE TABLE dim_raffstore_light_data_1og_r3 (
    raffstore_light_data_1og_r3_id SERIAL PRIMARY KEY,
    SlatAng1Act_1OG_R3 Numeric,
    SlatPos1Act_1OG_R3 Numeric,
    Light1Act_1OG_R3 Numeric
)

CREATE TABLE dim_raffstore_light_data_1og_r4 (
    raffstore_light_data_1og_r4_id SERIAL PRIMARY KEY,
    SlatAng1Act_1OG_R4 Numeric,
    SlatPos1Act_1OG_R4 Numeric,
    SlatAng2Act_1OG_R4 Numeric,
    SlatPos2Act_1OG_R4 Numeric,
    Light1Act_1OG_R4 Numeric,
    Light2Act_1OG_R4 Numeric
)


CREATE TABLE dim_raffstore_light_data_1og_r5 (
    raffstore_light_data_1og_r5_id SERIAL PRIMARY KEY,
    SlatAng1Act_1OG_R5 Numeric,
    SlatPos1Act_1OG_R5 Numeric,
    SlatAng2Act_1OG_R5 Numeric,
    SlatPos2Act_1OG_R5 Numeric,
    SlatAng3Act_1OG_R5 Numeric,
    SlatPos3Act_1OG_R5 Numeric,
    Light1Act_1OG_R5 Numeric
)

CREATE TABLE dim_user_input_mp1_1og_r1 (
    user_input_mp1_id SERIAL PRIMARY KEY,
    MP1GlareLimit Numeric,
    MP1ReqIllum Numeric,
    MP1ReqRoomTemp Numeric
)

CREATE TABLE dim_user_input_mp2_1og_r1 (
    user_input_mp2_id SERIAL PRIMARY KEY,
    MP2GlareLimit Numeric,
    MP2ReqIllum Numeric,
    MP2ReqRoomTemp Numeric
)

CREATE TABLE dim_user_input_mp3_1og_r1 (
    user_input_mp3_id SERIAL PRIMARY KEY,
    MP3GlareLimit Numeric,
    MP3ReqIllum Numeric,
    MP3ReqRoomTemp Numeric
)

CREATE TABLE dim_user_input_mp4_1og_r1 (
    user_input_mp4_id SERIAL PRIMARY KEY,
    MP4GlareLimit Numeric,
    MP4ReqIllum Numeric,
    MP4ReqRoomTemp Numeric
)

CREATE TABLE dim_indihella_calc_var_radiance_1og_r1 (
    indi_hella_calc_var_radiance_ih_id SERIAL PRIMARY KEY,
    altitudeRadianceIH Numeric,
    azimutRadianceIH Numeric,
    xdirRadianceIH Numeric,
    ydirRadianceIH Numeric,
    zdirRadianceIH Numeric,
    irrDirNorRadianceIH Numeric,
    profileangleRadianceIH Numeric,
    epsilonRadianceIH Numeric,
    deltaRadianceIH Numeric,
    waterPrecipitableRadianceIH Numeric,
    sunnyRadianceIH Numeric,
    cutofftiltRadianceIH Numeric
)

CREATE TABLE dim_indihella_target_var_1og_r1 (
    indi_hella_tar_var_ih_id SERIAL PRIMARY KEY,
    SlatAngTarIH Numeric,
    SlatPosTarIH Numeric,
    Light1TarIH Numeric,
    Light2TarIH Numeric
)

CREATE TABLE dim_indihella_dgp_var_1og_r1 (
    indi_hella_dgp_var_ih_id SERIAL PRIMARY KEY,
    DGPMP1_0_100_IH Numeric,
    DGPMP1_5_100_IH Numeric,
    DGPMP1_10_100_IH Numeric,
    DGPMP1_15_100_IH Numeric,
    DGPMP1_20_100_IH Numeric,
    DGPMP1_25_100_IH Numeric,
    DGPMP1_30_100_IH Numeric,
    DGPMP1_35_100_IH Numeric,
    DGPMP1_40_100_IH Numeric,
    DGPMP1_45_100_IH Numeric,
    DGPMP1_50_100_IH Numeric,
    DGPMP1_55_100_IH Numeric,
    DGPMP1_60_100_IH Numeric,
    DGPMP1_65_100_IH Numeric,
    DGPMP1_70_100_IH Numeric,
    DGPMP1_75_100_IH Numeric,
    DGPMP1_80_100_IH Numeric,
    DGPMP1_85_100_IH Numeric,
    DGPMP1_0_0_IH Numeric,
    DGPMP2_0_100_IH Numeric,
    DGPMP2_5_100_IH Numeric,
    DGPMP2_10_100_IH Numeric,
    DGPMP2_15_100_IH Numeric,
    DGPMP2_20_100_IH Numeric,
    DGPMP2_25_100_IH Numeric,
    DGPMP2_30_100_IH Numeric,
    DGPMP2_35_100_IH Numeric,
    DGPMP2_40_100_IH Numeric,
    DGPMP2_45_100_IH Numeric,
    DGPMP2_50_100_IH Numeric,
    DGPMP2_55_100_IH Numeric,
    DGPMP2_60_100_IH Numeric,
    DGPMP2_65_100_IH Numeric,
    DGPMP2_70_100_IH Numeric,
    DGPMP2_75_100_IH Numeric,
    DGPMP2_80_100_IH Numeric,
    DGPMP2_85_100_IH Numeric,
    DGPMP2_0_0_IH Numeric,
    DGPMP3_0_100_IH Numeric,
    DGPMP3_5_100_IH Numeric,
    DGPMP3_10_100_IH Numeric,
    DGPMP3_15_100_IH Numeric,
    DGPMP3_20_100_IH Numeric,
    DGPMP3_25_100_IH Numeric,
    DGPMP3_30_100_IH Numeric,
    DGPMP3_35_100_IH Numeric,
    DGPMP3_40_100_IH Numeric,
    DGPMP3_45_100_IH Numeric,
    DGPMP3_50_100_IH Numeric,
    DGPMP3_55_100_IH Numeric,
    DGPMP3_60_100_IH Numeric,
    DGPMP3_65_100_IH Numeric,
    DGPMP3_70_100_IH Numeric,
    DGPMP3_75_100_IH Numeric,
    DGPMP3_80_100_IH Numeric,
    DGPMP3_85_100_IH Numeric,
    DGPMP3_0_0_IH Numeric,
    DGPMP4_0_100_IH Numeric,
    DGPMP4_5_100_IH Numeric,
    DGPMP4_10_100_IH Numeric,
    DGPMP4_15_100_IH Numeric,
    DGPMP4_20_100_IH Numeric,
    DGPMP4_25_100_IH Numeric,
    DGPMP4_30_100_IH Numeric,
    DGPMP4_35_100_IH Numeric,
    DGPMP4_40_100_IH Numeric,
    DGPMP4_45_100_IH Numeric,
    DGPMP4_50_100_IH Numeric,
    DGPMP4_55_100_IH Numeric,
    DGPMP4_60_100_IH Numeric,
    DGPMP4_65_100_IH Numeric,
    DGPMP4_70_100_IH Numeric,
    DGPMP4_75_100_IH Numeric,
    DGPMP4_80_100_IH Numeric,
    DGPMP4_85_100_IH Numeric,
    DGPMP4_0_0_IH Numeric    
)

CREATE TABLE dim_indihella_illum_var_mp1_1og_r1 (
    indi_hella_illum_var_mp1_id SERIAL PRIMARY KEY,
    hor_illumMP1_0_100_IH Numeric,
    hor_illumMP1_5_100_IH Numeric,
    hor_illumMP1_10_100_IH Numeric,
    hor_illumMP1_15_100_IH Numeric,
    hor_illumMP1_20_100_IH Numeric,
    hor_illumMP1_25_100_IH Numeric,
    hor_illumMP1_30_100_IH Numeric,
    hor_illumMP1_35_100_IH Numeric,
    hor_illumMP1_40_100_IH Numeric,
    hor_illumMP1_45_100_IH Numeric,
    hor_illumMP1_50_100_IH Numeric,
    hor_illumMP1_55_100_IH Numeric,
    hor_illumMP1_60_100_IH Numeric,
    hor_illumMP1_65_100_IH Numeric,
    hor_illumMP1_70_100_IH Numeric,
    hor_illumMP1_75_100_IH Numeric,
    hor_illumMP1_80_100_IH Numeric,
    hor_illumMP1_85_100_IH Numeric,
    hor_illumMP1_0_0_IH Numeric,
    ver_illumMP1_0_100_IH Numeric,
    ver_illumMP1_5_100_IH Numeric,
    ver_illumMP1_10_100_IH Numeric,
    ver_illumMP1_15_100_IH Numeric,
    ver_illumMP1_20_100_IH Numeric,
    ver_illumMP1_25_100_IH Numeric,
    ver_illumMP1_30_100_IH Numeric,
    ver_illumMP1_35_100_IH Numeric,
    ver_illumMP1_40_100_IH Numeric,
    ver_illumMP1_45_100_IH Numeric,
    ver_illumMP1_50_100_IH Numeric,
    ver_illumMP1_55_100_IH Numeric,
    ver_illumMP1_60_100_IH Numeric,
    ver_illumMP1_65_100_IH Numeric,
    ver_illumMP1_70_100_IH Numeric,
    ver_illumMP1_75_100_IH Numeric,
    ver_illumMP1_80_100_IH Numeric,
    ver_illumMP1_85_100_IH Numeric,
    ver_illumMP1_0_0_IH Numeric
)

CREATE TABLE dim_indihella_illum_var_mp2_1og_r1 (
    indi_hella_illum_var_mp2_id SERIAL PRIMARY KEY,
    hor_illumMP2_0_100_IH Numeric,
    hor_illumMP2_5_100_IH Numeric,
    hor_illumMP2_10_100_IH Numeric,
    hor_illumMP2_15_100_IH Numeric,
    hor_illumMP2_20_100_IH Numeric,
    hor_illumMP2_25_100_IH Numeric,
    hor_illumMP2_30_100_IH Numeric,
    hor_illumMP2_35_100_IH Numeric,
    hor_illumMP2_40_100_IH Numeric,
    hor_illumMP2_45_100_IH Numeric,
    hor_illumMP2_50_100_IH Numeric,
    hor_illumMP2_55_100_IH Numeric,
    hor_illumMP2_60_100_IH Numeric,
    hor_illumMP2_65_100_IH Numeric,
    hor_illumMP2_70_100_IH Numeric,
    hor_illumMP2_75_100_IH Numeric,
    hor_illumMP2_80_100_IH Numeric,
    hor_illumMP2_85_100_IH Numeric,
    hor_illumMP2_0_0_IH Numeric,
    ver_illumMP2_0_100_IH Numeric,
    ver_illumMP2_5_100_IH Numeric,
    ver_illumMP2_10_100_IH Numeric,
    ver_illumMP2_15_100_IH Numeric,
    ver_illumMP2_20_100_IH Numeric,
    ver_illumMP2_25_100_IH Numeric,
    ver_illumMP2_30_100_IH Numeric,
    ver_illumMP2_35_100_IH Numeric,
    ver_illumMP2_40_100_IH Numeric,
    ver_illumMP2_45_100_IH Numeric,
    ver_illumMP2_50_100_IH Numeric,
    ver_illumMP2_55_100_IH Numeric,
    ver_illumMP2_60_100_IH Numeric,
    ver_illumMP2_65_100_IH Numeric,
    ver_illumMP2_70_100_IH Numeric,
    ver_illumMP2_75_100_IH Numeric,
    ver_illumMP2_80_100_IH Numeric,
    ver_illumMP2_85_100_IH Numeric,
    ver_illumMP2_0_0_IH Numeric
)


CREATE TABLE dim_indihella_illum_var_mp3_1og_r1 (
    indi_hella_illum_var_mp3_id SERIAL PRIMARY KEY,
    hor_illumMP3_0_100_IH Numeric,
    hor_illumMP3_5_100_IH Numeric,
    hor_illumMP3_10_100_IH Numeric,
    hor_illumMP3_15_100_IH Numeric,
    hor_illumMP3_20_100_IH Numeric,
    hor_illumMP3_25_100_IH Numeric,
    hor_illumMP3_30_100_IH Numeric,
    hor_illumMP3_35_100_IH Numeric,
    hor_illumMP3_40_100_IH Numeric,
    hor_illumMP3_45_100_IH Numeric,
    hor_illumMP3_50_100_IH Numeric,
    hor_illumMP3_55_100_IH Numeric,
    hor_illumMP3_60_100_IH Numeric,
    hor_illumMP3_65_100_IH Numeric,
    hor_illumMP3_70_100_IH Numeric,
    hor_illumMP3_75_100_IH Numeric,
    hor_illumMP3_80_100_IH Numeric,
    hor_illumMP3_85_100_IH Numeric,
    hor_illumMP3_0_0_IH Numeric,
    ver_illumMP3_0_100_IH Numeric,
    ver_illumMP3_5_100_IH Numeric,
    ver_illumMP3_10_100_IH Numeric,
    ver_illumMP3_15_100_IH Numeric,
    ver_illumMP3_20_100_IH Numeric,
    ver_illumMP3_25_100_IH Numeric,
    ver_illumMP3_30_100_IH Numeric,
    ver_illumMP3_35_100_IH Numeric,
    ver_illumMP3_40_100_IH Numeric,
    ver_illumMP3_45_100_IH Numeric,
    ver_illumMP3_50_100_IH Numeric,
    ver_illumMP3_55_100_IH Numeric,
    ver_illumMP3_60_100_IH Numeric,
    ver_illumMP3_65_100_IH Numeric,
    ver_illumMP3_70_100_IH Numeric,
    ver_illumMP3_75_100_IH Numeric,
    ver_illumMP3_80_100_IH Numeric,
    ver_illumMP3_85_100_IH Numeric,
    ver_illumMP3_0_0_IH Numeric
)

CREATE TABLE dim_indihella_illum_var_mp4_1og_r1 (
    indi_hella_illum_var_mp4_id SERIAL PRIMARY KEY,
    hor_illumMP4_0_100_IH Numeric,
    hor_illumMP4_5_100_IH Numeric,
    hor_illumMP4_10_100_IH Numeric,
    hor_illumMP4_15_100_IH Numeric,
    hor_illumMP4_20_100_IH Numeric,
    hor_illumMP4_25_100_IH Numeric,
    hor_illumMP4_30_100_IH Numeric,
    hor_illumMP4_35_100_IH Numeric,
    hor_illumMP4_40_100_IH Numeric,
    hor_illumMP4_45_100_IH Numeric,
    hor_illumMP4_50_100_IH Numeric,
    hor_illumMP4_55_100_IH Numeric,
    hor_illumMP4_60_100_IH Numeric,
    hor_illumMP4_65_100_IH Numeric,
    hor_illumMP4_70_100_IH Numeric,
    hor_illumMP4_75_100_IH Numeric,
    hor_illumMP4_80_100_IH Numeric,
    hor_illumMP4_85_100_IH Numeric,
    hor_illumMP4_0_0_IH Numeric,
    ver_illumMP4_0_100_IH Numeric,
    ver_illumMP4_5_100_IH Numeric,
    ver_illumMP4_10_100_IH Numeric,
    ver_illumMP4_15_100_IH Numeric,
    ver_illumMP4_20_100_IH Numeric,
    ver_illumMP4_25_100_IH Numeric,
    ver_illumMP4_30_100_IH Numeric,
    ver_illumMP4_35_100_IH Numeric,
    ver_illumMP4_40_100_IH Numeric,
    ver_illumMP4_45_100_IH Numeric,
    ver_illumMP4_50_100_IH Numeric,
    ver_illumMP4_55_100_IH Numeric,
    ver_illumMP4_60_100_IH Numeric,
    ver_illumMP4_65_100_IH Numeric,
    ver_illumMP4_70_100_IH Numeric,
    ver_illumMP4_75_100_IH Numeric,
    ver_illumMP4_80_100_IH Numeric,
    ver_illumMP4_85_100_IH Numeric,
    ver_illumMP4_0_0_IH Numeric
)

CREATE TABLE dim_radiation_forecast (
    radiation_forecast_id SERIAL primary KEY,
    GlobalIrrHor_approx Numeric,
    DiffIrrHorAct_approx Numeric
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


