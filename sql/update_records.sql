-- Previously, in delete_records.sql 9 out of 10 records were deleted
-- One record with a name of 'Keep This Record' remained
-- This SQL statement updates this record to a real car  model with an accurate introduced year
-- The brand ID was already correct from the insertion ('insert_records.sql'), so brand_id will not be updated in this statement

update car_models
set model_name      = 'Sorento',
    year_introduced = '2002'
where model_name = 'Keep This Record';