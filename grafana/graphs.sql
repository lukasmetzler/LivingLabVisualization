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