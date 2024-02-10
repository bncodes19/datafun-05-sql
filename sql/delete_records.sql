-- Previously, 10 records were inserted into car_models from insert_records.sql
-- 9 of these records had a model_name of 'Test'
-- This statement deletes these 9

delete from car_models where model_name = 'Test';