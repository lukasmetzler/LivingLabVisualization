-- Create sources table
CREATE TABLE sources (
    source_id SERIAL PRIMARY KEY,
    source_name VARCHAR(255)
);

-- Insert source data
INSERT intO sources (source_name)
VALUES 
    ('Beckhoff'),
    ('ONYX'),
    ('indiHELLA'),
    ('Frogcast'),
    ('E3D');


-- Create parameters table
CREATE TABLE parameters (
    parameter_id SERIAL PRIMARY KEY,
    parameter_name VARCHAR(255),
    description VARCHAR(255),
    data_type VARCHAR(255),
    unit VARCHAR(255),
    range_min float,
    range_max float
);

-- Insert parameter data
INSERT intO parameters (parameter_name, description, data_type, unit, range_min, range_max)
VALUES 
    ('GlobIrrVerAct', 'Globalstrahlung vertikal aktuell gemessen', 'int', 'W/m2', 0, 1300),
    ('GlobalIrrHorAct', 'Globalstrahlung horizontal aktuell gemessen', 'int', 'W/m2', 0, 2000),
    ('DiffIrrHorAct', 'Diffuse Strahlung horizontal aktuell gemessen', 'int', 'W/m2', 0, 2000),
    ('AirTempAct', 'Lufttemperatur aktuell gemessen', 'int', '°C', -30, 40),
    ('WindSpeedAct_ms', 'Windgeschwindigkeit [m/s] aktuell gemessen', 'int', 'm/s', 0, 40),
    ('SunElevationAct', 'Sonnen Elevation aktuell gemessen', 'float', '°', -90, 90),
    ('SunAzimuthAct', 'Sonne Azimut aktuell gemessen', 'float', '°', NULL, NULL),
    ('Longitude', 'Längengrad', 'float', '°', -180, 180),
    ('Latitude', 'Breitengrad', 'float', '°', -90, 90),
    ('WindSpeedAct_kmh', 'Windgeschwindigkeit [km/h] aktuell gemessen', 'int', 'km/h', 0, 100),
    ('WindDirectionAct', 'Windrichtung aktuell gemessen', 'int', '°', 0, 360),
    ('BrightnessNorthAct', 'Helligkeit Norden aktuell gemessen', 'int', 'klx', 0, 150),
    ('BrightnessEastAct', 'Helligkeit Osten aktuell gemessen', 'int', 'klx', 0, 150),
    ('BrightnessSouthAct', 'Helligkeit Süden aktuell gemessen', 'int', 'klx', 0, 150),
    ('BrightnessWestAct', 'Helligkeit Westen aktuell gemessen', 'int', 'klx', 0, 150),
    ('TwilightAct', 'Dämmerung aktuell gemessen', 'int', 'lx', 0, 500),
    ('GlobalIrrHorAct_2', 'Globalstrahlung horizontal aktuell gemessen', 'int', 'W/m2', 0, 1300),
    ('PrecipitationAct', 'Niederschlag aktuell gemessen', 'int', 'boolean', NULL, NULL),
    ('AbsolutAirPressureAct', 'Absoluter Luftdruck aktuell gemessen', 'int', 'hPa', 300, 1100),
    ('RelativeAirPressureAct', 'Relativer Luftdruck aktuell gemessen', 'int', 'hPa', 300, 1100),
    ('AbsoluteHumidityAct', 'Absolute Luftfeuchtigkeit aktuell gemessen', 'int', 'g/m3', NULL, NULL),
    ('RelativeHumidityAct', 'Relative Luftfeuchtigkeit aktuell gemessen', 'int', '%', 0, 100),
    ('DewPointTempAct', 'Taupunkt aktuell gemessen', 'int', '°C', NULL, NULL),
    ('HousingTemAct', 'Sensorgehäusetemperatur aktuell gemessen', 'int', '°C', NULL, NULL),
    ('VoltMeasActModule1', 'Spannung PV-Modul 1 aktuell gemessen', 'float', 'V', NULL, NULL),
    ('CurrMeasActModule1', 'Strom PV-Modul 1 aktuell gemessen', 'float', 'A', NULL, NULL),
    ('VoltMeasActModule2', 'Spannung PV-Modul 2 aktuell gemessen', 'float', 'V', NULL, NULL),
    ('CurrMeasActModule2', 'Strom PV-Modul 2 aktuell gemessen', 'float', 'A', NULL, NULL),
    ('IllumMP1Act', 'Helligkeit Messpunkt 1 aktuell gemessen', 'int', 'lx', 0, 1000),
    ('IllumMP2Act', 'Helligkeit Messpunkt 2 aktuell gemessen', 'int', 'lx', 0, 1000),
    ('IllumMP3Act', 'Helligkeit Messpunkt 3 aktuell gemessen', 'int', 'lx', 0, 1000),
    ('IllumMP4Act', 'Helligkeit Messpunkt 4 aktuell gemessen', 'int', 'lx', 0, 10000),
    ('RoomTempAct', 'Raumtemperatur aktuell gemessen', 'int', '°C', 15, 35),
    ('SlatAng1Act_1OG_R1', 'Lamellenwinkel Motor 1 aktuell gemessen Raum 1 1.OG', 'int', '°', 0, 85),
    ('SlatPos1Act_1OG_R1', 'Raffstoreposition Motor 1 Höhe aktuell gemessen Raum 1 1.OG', 'int', '%', 0, 100),
    ('Light1Act_1OG_R1', 'Lichtreihe 1 aktuell Raum 1 1.OG', 'int', 'boolean', NULL, NULL),
    ('Light2Act_1OG_R1', 'Lichtreihe 2 aktuell Raum 1 1.OG', 'int', 'boolean', NULL, NULL),
    ('SlatAng1Act_1OG_R2', 'Lamellenwinkel Motor 1 aktuell gemessen Raum 2 1.OG', 'int', '°', 0, 85),
    ('SlatPos1Act_1OG_R2', 'Raffstoreposition Motor 1 Höhe aktuell gemessen Raum 2 1.OG', 'int', '%', 0, 100),
    ('Light1Act_1OG_R2', 'Lichtreihe 1 aktuell Raum 2 1.OG', 'int', 'boolean', NULL, NULL),
    ('SlatAng1Act_1OG_R3', 'Lamellenwinkel Motor 1 aktuell gemessen Raum 3 1.OG', 'int', '°', 0, 85),
    ('SlatPos1Act_1OG_R3', 'Raffstoreposition Motor 1 Höhe aktuell gemessen Raum 3 1.OG', 'int', '%', 0, 100),
    ('Light1Act_1OG_R3', 'Lichtreihe 1 aktuell Raum 3 1.OG', 'int', 'boolean', NULL, NULL),
    ('SlatAng1Act_1OG_R4', 'Lamellenwinkel Motor 1 aktuell gemessen Raum 4 1.OG', 'int', '°', 0, 85),
    ('SlatPos1Act_1OG_R4', 'Raffstoreposition Motor 1 Höhe aktuell gemessen Raum 4 1.OG', 'int', '%', 0, 100),
    ('SlatAng2Act_1OG_R4', 'Lamellenwinkel Motor 2 aktuell gemessen Raum 4 1.OG', 'int', '°', 0, 85),
    ('SlatPos2Act_1OG_R4', 'Raffstoreposition Motor 2 Höhe aktuell gemessen Raum 4 1.OG', 'int', '%', 0, 100),
    ('SlatAng3Act_1OG_R4', 'Lamellenwinkel Motor 3 aktuell gemessen Raum 4 1.OG', 'int', '°', 0, 85),
    ('SlatPos3Act_1OG_R4', 'Raffstoreposition Motor 3 Höhe aktuell gemessen Raum 4 1.OG', 'int', '%', 0, 100),
    ('SlatAng4Act_1OG_R4', 'Lamellenwinkel Motor 4 aktuell gemessen Raum 4 1.OG', 'int', '°', 0, 85),
    ('SlatPo4Act_1OG_R4', 'Raffstoreposition Motor 4 Höhe aktuell gemessen Raum 4 1.OG', 'int', '%', 0, 100),
    ('SlatAng5Act_1OG_R4', 'Lamellenwinkel Motor 5 aktuell gemessen Raum 4 1.OG', 'int', '°', 0, 85),
    ('SlatPos5Act_1OG_R4', 'Raffstoreposition Motor 5 Höhe aktuell gemessen Raum 4 1.OG', 'int', '%', 0, 100),
    ('Light1Act_1OG_R4', 'Lichtreihe 1 aktuell Raum 4 1.OG', 'int', 'boolean', NULL, NULL),
    ('Light2Act_1OG_R4', 'Lichtreihe 1 aktuell Raum 4 1.OG', 'int', 'boolean', NULL, NULL),
    ('MP1GlareLimit', 'Benutzer-Input Schwellwert Blendung Messpunkt 1', 'int', 'DGP', NULL, NULL),
    ('MP1ReqIllum', 'Benutzer-Input gewünschte Helligkeit Messpunkt 1', 'int', 'lx', NULL, NULL),
    ('MP1ReqRoomTemp', 'Benutzer-Input gewünschte Raumtemperatur Messpunkt 1', 'int', '°C', NULL, NULL),
    ('MP2GlareLimit', 'Benutzer-Input Blendung Messpunkt 2', 'int', 'DGP', NULL, NULL),
    ('MP2ReqIllum', 'Benutzer-Input gewünschte Helligkeit Messpunkt 2', 'int', 'lx', NULL, NULL),
    ('MP2ReqRoomTemp', 'Benutzer-Input gewünschte Raumtemperatur Messpunkt 2', 'int', '°C', NULL, NULL),
    ('MP3GlareLimit', 'Benutzer-Input Blendung Messpunkt 3', 'int', 'DGP', NULL, NULL),
    ('MP3ReqIllum', 'Benutzer-Input gewünschte Helligkeit Messpunkt 3', 'int', 'lx', NULL, NULL),
    ('MP3ReqRoomTemp', 'Benutzer-Input gewünschte Raumtemperatur Messpunkt 3', 'int', '°C', NULL, NULL),
    ('MP4GlareLimit', 'Benutzer-Input Blendung Messpunkt 4', 'int', 'DGP', NULL, NULL),
    ('MP4ReqIllum', 'Benutzer-Input gewünschte Helligkeit Messpunkt 4', 'int', 'lx', NULL, NULL),
    ('MP4ReqRoomTemp', 'Benutzer-Input gewünschte Raumtemperatur Messpunkt 4', 'int', '°C', NULL, NULL),
    ('altitudeRadianceIH', 'Berechnungsvariable indiHELLA', 'float', '°', NULL, NULL),
    ('azimutRadianceIH', 'Berechnungsvariable indiHELLA', 'float', '°', NULL, NULL),
    ('xdirRadianceIH', 'Berechnungsvariable indiHELLA', 'float', NULL, NULL, NULL),
    ('ydirRadianceIH', 'Berechnungsvariable indiHELLA', 'float', NULL, NULL, NULL),
    ('zdirRadianceIH', 'Berechnungsvariable indiHELLA', 'float', NULL, NULL, NULL),
    ('irrDirNorRadianceIH', 'Berechnungsvariable indiHELLA', 'float', 'W/m2', NULL, NULL),
    ('profileangleRadianceIH', 'Berechnungsvariable indiHELLA', 'float', '°', NULL, NULL),
    ('epsilonRadianceIH', 'Berechnungsvariable indiHELLA', 'float', NULL, NULL, NULL),
    ('deltaRadianceIH', 'Berechnungsvariable indiHELLA', 'float', NULL, NULL, NULL),
    ('waterPrecipitableRadianceIH', 'Berechnungsvariable indiHELLA', 'float', NULL, NULL, NULL),
    ('sunynRadianceIH', 'Berechnungsvariable indiHELLA', 'int', 'boolean', NULL, NULL),
    ('cutofftiltRadianceIH', 'Berechnungsvariable indiHELLA', 'int', '°', NULL, NULL),
    ('SlatAngTarIH', 'Berechnungsvariable indiHELLA: Soll Lamellenwinkel', 'int', '°', NULL, NULL),
    ('SlatPosTarIH', 'Berechnungsvariable indiHELLA: Soll Raffstorehöhe', 'int', '%', NULL, NULL),
    ('Light1TarIH', 'Berechnungsvariable indiHELLA: Soll Licht 1', 'int', 'boolean', NULL, NULL),
    ('Light2TarIH', 'Berechnungsvariable indiHELLA: Soll Licht 2', 'int', 'boolean', NULL, NULL),
    ('DGPMP1_XX_XXX_IH', 'Berechnungsvariable indiHELLA: Daylight Glare Probability für Messpunkt 1', 'float', 'DGP', NULL, NULL),
    ('DGPMP2_XX_XXX_IH', 'Berechnungsvariable indiHELLA: Daylight Glare Probability für Messpunkt 2', 'float', 'DGP', NULL, NULL),
    ('DGPMP3_XX_XXX_IH', 'Berechnungsvariable indiHELLA: Daylight Glare Probability für Messpunkt 3', 'float', 'DGP', NULL, NULL),
    ('DGPMP4_XX_XXX_IH', 'Berechnungsvariable indiHELLA: Daylight Glare Probability für Messpunkt 4', 'float', 'DGP', NULL, NULL),
    ('DillumMP1Hor_XX_XXX_IH', 'Berechnungsvariable indiHELLA: Helligkeit vertikal für Messpunkt 1', 'float', 'lx', NULL, NULL),
    ('DillumMP2Hor_XX_XXX_IH', 'Berechnungsvariable indiHELLA: Helligkeit vertikal für Messpunkt 2', 'float', 'lx', NULL, NULL),
    ('DillumMP3Hor_XX_XXX_IH', 'Berechnungsvariable indiHELLA: Helligkeit vertikal für Messpunkt 3', 'float', 'lx', NULL, NULL),
    ('DillumMP4Hor_XX_XXX_IH', 'Berechnungsvariable indiHELLA: Helligkeit vertikal für Messpunkt 4', 'float', 'lx', NULL, NULL),
    ('DillumMP1Ver_XX_XXX_IH', 'Berechnungsvariable indiHELLA: Helligkeit horizontal für Messpunkt 1', 'float', 'lx', NULL, NULL),
    ('DillumMP2Ver_XX_XXX_IH', 'Berechnungsvariable indiHELLA: Helligkeit horizontal für Messpunkt 2', 'float', 'lx', NULL, NULL),
    ('DillumMP3Ver_XX_XXX_IH', 'Berechnungsvariable indiHELLA: Helligkeit horizontal für Messpunkt 3', 'float', 'lx', NULL, NULL),
    ('DillumMP4Ver_XX_XXX_IH', 'Berechnungsvariable indiHELLA: Helligkeit horizontal für Messpunkt 4', 'float', 'lx', NULL, NULL),
    ('GlobalIrrHor_approx', 'Globalstrahlung horizontal Vorhersage', 'float[]', 'W/m2', 0, 2000),
    ('DiffIrrHorAct_approx', 'Diffuse Strahlung horizontal aktuell Vorhersage', 'float[]', 'W/m2', 0, 2000),
    ('num_headpose', 'Anzahl der detektierten Köpfe im Raum', 'int', NULL, 0, 4),
    ('headpose_x_1', 'Kopfposition X Person 1', 'float', 'm', NULL, NULL),
    ('headpose_y_1', 'Kopfposition Y Person 1', 'float', 'm', NULL, NULL),
    ('headpose_z_1', 'Kopfposition Z Person 1', 'float', 'm', NULL, NULL),
    ('headpose_pitch_1', 'Kopfwinkel Pitch Person 1', 'float', '°', NULL, NULL),
    ('headpose_yaw_1', 'Kopfwinkel Yaw Person 1', 'float', '°', NULL, NULL),
    ('headpose_roll_1', 'Kopfwinkel Roll Person 1', 'float', '°', NULL, NULL),
    ('headpose_x_2', 'Kopfposition X Person 2', 'float', 'm', NULL, NULL),
    ('headpose_y_2', 'Kopfposition Y Person 2', 'float', 'm', NULL, NULL),
    ('headpose_z_2', 'Kopfposition Z Person 2', 'float', 'm', NULL, NULL),
    ('headpose_pitch_2', 'Kopfwinkel Pitch Person 2', 'float', '°', NULL, NULL),
    ('headpose_yaw_2', 'Kopfwinkel Yaw Person 2', 'float', '°', NULL, NULL),
    ('headpose_roll_2', 'Kopfwinkel Roll Person 2', 'float', '°', NULL, NULL),
    ('headpose_x_3', 'Kopfposition X Person 3', 'float', 'm', NULL, NULL),
    ('headpose_y_3', 'Kopfposition Y Person 3', 'float', 'm', NULL, NULL),
    ('headpose_z_3', 'Kopfposition Z Person 3', 'float', 'm', NULL, NULL),
    ('headpose_pitch_3', 'Kopfwinkel Pitch Person 3', 'float', '°', NULL, NULL),
    ('headpose_yaw_3', 'Kopfwinkel Yaw Person 3', 'float', '°', NULL, NULL),
    ('headpose_roll_3', 'Kopfwinkel Roll Person 3', 'float', '°', NULL, NULL),
    ('headpose_x_4', 'Kopfposition X Person 4', 'float', 'm', NULL, NULL),
    ('headpose_y_4', 'Kopfposition Y Person 4', 'float', 'm', NULL, NULL),
    ('headpose_z_4', 'Kopfposition Z Person 4', 'float', 'm', NULL, NULL),
    ('headpose_pitch_4', 'Kopfwinkel Pitch Person 4', 'float', '°', NULL, NULL),
    ('headpose_yaw_4', 'Kopfwinkel Yaw Person 4', 'float', '°', NULL, NULL),
    ('headpose_roll_4', 'Kopfwinkel Roll Person 4', 'float', '°', NULL, NULL);


CREATE OR REPLACE FUNCTION get_parameter_value(parameter_id INT) 
RETURNS JSONB AS $$
DECLARE
    param_data_type VARCHAR(255);
    result_value JSONB;
BEGIN
    SELECT data_type INTO param_data_type
    FROM parameters
    WHERE parameter_id = get_parameter_value.parameter_id;

    CASE param_data_type
        WHEN 'int' THEN
            result_value := '{"value": 10, "type": "int"}';
        WHEN 'float' THEN
            result_value := '{"value": 10.5, "type": "float"}';
        WHEN 'boolean' THEN
            result_value := '{"value": true, "type": "boolean"}';
        ELSE
            RAISE EXCEPTION 'Unbekannter data_type: %', param_data_type;
    END CASE;

    RETURN result_value;
END;
$$ LANGUAGE plpgsql;


-- Create measurements table
CREATE TABLE measurements (
    timestamp TIMESTAMP,
    source_id int,
    parameter_id int,
    value JSONB,
    FOREIGN KEY (source_id) REFERENCES sources(source_id),
    FOREIGN KEY (parameter_id) REFERENCES parameters(parameter_id),
);

-- Create indexes
CREATE INDEX idx_measurements ON measurements (timestamp, source_id, parameter_id);
CREATE INDEX idx_sources ON sources (source_name);
CREATE INDEX idx_parameters ON parameters (parameter_name);