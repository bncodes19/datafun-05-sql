-- There have already been 20 records inserted from a CSV named 'car_models.csv'
-- This SQL statement adds 10 new records into car_models

insert into car_models (id, model_name, brand_id, year_introduced)
values ('21', 'Test', '1', '1990'),
       ('22', 'Test', '2', '1991'),
       ('23', 'Test', '3', '1992'),
       ('24', 'Test', '4', '1993'),
       ('25', 'Test', '5', '1994'),
       ('26', 'Test', '6', '1995'),
       ('27', 'Test', '7', '1996'),
       ('28', 'Test', '1', '1997'),
       ('29', 'Test', '2', '1998'),
       ('30', 'Keep This Record', '3', '1999');