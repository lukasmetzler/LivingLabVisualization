CREATE OR REPLACE FUNCTION insert_fact_user_input()
RETURNS TRIGGER AS $$
BEGIN
    INSERT INTO fact_user_input_facts (timestamp, user_input_mp1_id, user_input_mp2_id, user_input_mp3_id, user_input_mp4_id)
    VALUES (NEW.timestamp, NEW.user_input_mp1_id, NEW.user_input_mp2_id, NEW.user_input_mp3_id, NEW.user_input_mp4_id);
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER tr_insert_fact_user_input
AFTER INSERT ON dim_user_input_mp1_1og_r1
FOR EACH ROW EXECUTE FUNCTION insert_fact_user_input();


CREATE OR REPLACE FUNCTION insert_fact_sensory()
RETURNS TRIGGER AS $$
BEGIN
    INSERT INTO fact_sensory (timestamp, zed_body_tracking_id)
    VALUES (NEW.timestamp, NEW.zed_body_tracking_id);
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER tr_insert_fact_sensory
AFTER INSERT ON dim_zed_body_tracking_1og_r1
FOR EACH ROW EXECUTE FUNCTION insert_fact_sensory();

CREATE OR REPLACE FUNCTION insert_fact_raffstore_light()
RETURNS TRIGGER AS $$
BEGIN
    INSERT INTO fact_raffstore_light_facts (timestamp, raffstore_light_data_1og_r1_id, raffstore_light_data_1og_r2_id, raffstore_light_data_1og_r3_id, raffstore_light_data_1og_r4_id, raffstore_light_data_1og_r5_id)
    VALUES (NEW.timestamp, NEW.raffstore_light_data_1og_r1_id, NEW.raffstore_light_data_1og_r2_id, NEW.raffstore_light_data_1og_r3_id, NEW.raffstore_light_data_1og_r4_id, NEW.raffstore_light_data_1og_r5_id);
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER tr_insert_fact_raffstore_light
AFTER INSERT ON dim_raffstore_light_data_1og_r1
FOR EACH ROW EXECUTE FUNCTION insert_fact_raffstore_light();

CREATE OR REPLACE FUNCTION insert_fact_indi_hella_illum()
RETURNS TRIGGER AS $$
BEGIN
    INSERT INTO fact_indi_hella_illum_facts (timestamp, indi_hella_illum_var_mp1_id, indi_hella_illum_var_mp2_id, indi_hella_illum_var_mp3_id, indi_hella_illum_var_mp4_id)
    VALUES (NEW.timestamp, NEW.indi_hella_illum_var_mp1_id, NEW.indi_hella_illum_var_mp2_id, NEW.indi_hella_illum_var_mp3_id, NEW.indi_hella_illum_var_mp4_id);
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER tr_insert_fact_indi_hella_illum
AFTER INSERT ON dim_indihella_illum_var_mp1_1og_r1
FOR EACH ROW EXECUTE FUNCTION insert_fact_indi_hella_illum();

CREATE OR REPLACE FUNCTION insert_fact_indi_hella_calc_vars()
RETURNS TRIGGER AS $$
BEGIN
    INSERT INTO fact_indi_hella_calc_vars_facts (timestamp, indi_hella_calc_var_radiance_ih_id, indi_hella_tar_var_ih_id, indi_hella_dgp_var_ih_id)
    VALUES (NEW.timestamp, NEW.indi_hella_calc_var_radiance_ih_id, NEW.indi_hella_tar_var_ih_id, NEW.indi_hella_dgp_var_ih_id);
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER tr_insert_fact_indi_hella_calc_vars
AFTER INSERT ON dim_indihella_calc_var_radiance_1og_r1
FOR EACH ROW EXECUTE FUNCTION insert_fact_indi_hella_calc_vars();

CREATE OR REPLACE FUNCTION insert_fact_environmental_data()
RETURNS TRIGGER AS $$
BEGIN
    INSERT INTO fact_environmental_data_facts (timestamp, metrological_data_id, pv_modul_data_id, illumination_datapoints_id, radiation_forecast_id, head_positions_id)
    VALUES (NEW.timestamp, NEW.metrological_data_id, NEW.pv_modul_data_id, NEW.illumination_datapoints_id, NEW.radiation_forecast_id, NEW.head_positions_id);
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER tr_insert_fact_environmental_data
AFTER INSERT ON dim_metrological_data
FOR EACH ROW EXECUTE FUNCTION insert_fact_environmental_data();
