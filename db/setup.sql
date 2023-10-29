CREATE DATABASE test_db;
\c test_db
CREATE TABLE test_table (
    id SERIAL PRIMARY KEY,
    value1 INT,
    value2 INT
);


\c lukasmetzler
SELECT * FROM test_table;
