-- Wetterstation
-- Graph1
SELECT timestamp, globirrveract, globalirrhoract, difflrrhoract FROM dim_metrological_data dmd JOIN fact_environmental_data_facts fedf ON dmd.metrological_data_id = fedf.metrological_data_id
-- Graph2
SELECT timestamp, housingtemact FROM dim_metrological_data dmd JOIN fact_environmental_data_facts fedf ON dmd.metrological_data_id = fedf.metrological_data_id
-- Graph3
SELECT timestamp, brightnessnorthact, brightnesssouthact, brightnesswestact FROM dim_metrological_data dmd JOIN fact_environmental_data_facts fedf ON dmd.metrological_data_id = fedf.metrological_data_id
-- Graph4
SELECT timestamp, WindSpeedAct_kmh FROM dim_metrological_data dmd JOIN fact_environmental_data_facts fedf ON dmd.metrological_data_id = fedf.metrological_data_id

-- 1.OG Raum 1
-- Graph1
SELECT timestamp, illum_mp1_act, illum_mp2_act, illum_mp3_act, illum_mp4_act FROM dim_illumination_datapoints_1og_r1 did1 JOIN fact_environmental_data_facts fedf ON did1.illumination_datapoints_id = fedf.illumination_datapoints_id
-- Graph2
SELECT timestamp, mp1_req_room_temp FROM dim_user_input_mp1_1og_r1 duim1 JOIN fact_user_input_facts fuif ON duim1.user_input_mp1_id = fuif.user_input_mp1_id
-- Graph3
SELECT timestamp, slat_ang1_act_1og_r1, slat_pos1_act_1og_r1 FROM dim_raffstore_light_data_1og_r1 drld1 JOIN fact_raffstore_light_facts frlf ON drld1.raffstore_light_data_1og_r1_id = frlf.raffstore_light_data_1og_r1_id
-- Graph4
SELECT timestamp, light1_act_1og_r1, light2_act_1og_r1 FROM dim_raffstore_light_data_1og_r1 drld1 JOIN fact_raffstore_light_facts frlf ON drld1.raffstore_light_data_1og_r1_id = frlf.raffstore_light_data_1og_r1_id

-- 1.OG Raum 2
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
-- Graph1
SELECT timestamp, headpose_yaw_1 FROM dim_head_positions_1og_r1 dhp1 JOIN fact_environmental_data_facts fedf ON dhp1.head_positions_id = fedf.head_positions_id
SELECT timestamp, headpose_pitch_1 FROM dim_head_positions_1og_r1 dhp1 JOIN fact_environmental_data_facts fedf ON dhp1.head_positions_id = fedf.head_positions_id
SELECT timestamp, headpose_roll_1 FROM dim_head_positions_1og_r1 dhp1 JOIN fact_environmental_data_facts fedf ON dhp1.head_positions_id = fedf.head_positions_id
-- Graph2
SELECT timestamp, headpose_x_1 AS x, headpose_y_1 AS y, headpose_z_1 AS z FROM dim_head_positions_1og_r1 dhp1 JOIN fact_environmental_data_facts fedf ON dhp1.head_positions_id = fedf.head_positions_id
-- Same for Graph 3 and Graph 4 etc

-- 1.OG Raum 2
SELECT timestamp,slat_ang1_act_1og_r2,slat_pos1_act_1og_r2 FROM dim_raffstore_light_data_1og_r2 drld2 JOIN fact_raffstore_light_facts frlf ON drld2.raffstore_light_data_1og_r2_id = frlf.raffstore_light_light_facts_id
SELECT timestamp,light1_act_1og_r2 FROM dim_raffstore_light_data_1og_r2 drld2 JOIN fact_raffstore_light_facts frlf ON drld2.raffstore_light_data_1og_r2_id = frlf.raffstore_light_light_facts_id
-- 1.OG Raum 3
SELECT timestamp,slat_ang1_act_1og_r3,slat_pos1_act_1og_r3 FROM dim_raffstore_light_data_1og_r3 drld3 JOIN fact_raffstore_light_facts frlf ON drld3.raffstore_light_data_1og_r3_id = frlf.raffstore_light_light_facts_id
SELECT timestamp,light1_act_1og_r3 FROM dim_raffstore_light_data_1og_r3 drld3 JOIN fact_raffstore_light_facts frlf ON drld3.raffstore_light_data_1og_r3_id = frlf.raffstore_light_light_facts_id
-- 1.OG Raum 4
SELECT timestamp,slat_ang1_act_1og_r5,slat_pos1_act_1og_r5 FROM dim_raffstore_light_data_1og_r5 drld5 JOIN fact_raffstore_light_facts frlf ON drld5.raffstore_light_data_1og_r5_id = frlf.raffstore_light_light_facts_id
SELECT timestamp,slat_ang2_act_1og_r5,slat_pos2_act_1og_r5 FROM dim_raffstore_light_data_1og_r5 drld5 JOIN fact_raffstore_light_facts frlf ON drld5.raffstore_light_data_1og_r5_id = frlf.raffstore_light_light_facts_id
SELECT timestamp,slat_ang3_act_1og_r5,slat_pos3_act_1og_r5 FROM dim_raffstore_light_data_1og_r5 drld5 JOIN fact_raffstore_light_facts frlf ON drld5.raffstore_light_data_1og_r5_id = frlf.raffstore_light_light_facts_id
SELECT timestamp,light1_act_1og_r5 FROM dim_raffstore_light_data_1og_r5 drld5 JOIN fact_raffstore_light_facts frlf ON drld5.raffstore_light_data_1og_r5_id = frlf.raffstore_light_light_facts_id
-- 1.OG Raum 5