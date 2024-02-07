def process_messages():
    try:
        with pg.postgres_connection() as connection:
            logging.debug("Verbindung erfolgreich hergestellt")

            for message in consumer:
                with connection.cursor() as cursor:
                    # Insert into dimension tables
                    dimension_ids = {}
                    for table_name, column_names in table_column_names.items():
                        inserted_id = insert_data_into_table(
                            connection,
                            cursor,
                            table_name,
                            column_names,
                            message.value,
                        )
                        dimension_ids[table_name] = inserted_id

                    # Get last inserted IDs
                    last_inserted_ids = get_last_inserted_ids(connection, cursor)
                    zed_body_tracking_id = last_inserted_ids.get(
                        "dim_zed_body_tracking_1og_r1", None
                    )
                    if zed_body_tracking_id is not None:
                        print("ID für 'zed_body_tracking_id':", zed_body_tracking_id)
                    else:
                        print("ID für 'zed_body_tracking_id' nicht gefunden.")

                    # print("Last inserted IDs:", last_inserted_ids)
                    query = (
                        f"INSERT INTO fact_sensory (zed_body_tracking_id) VALUES (%s)"
                    )
                    cursor.execute(query, (zed_body_tracking_id,))

                    connection.commit()
                    print("Dimension tables inserted successfuly")

    except Exception as e:
        logging.error(f"An error occurred: {e}")
    finally:
        consumer.close()
