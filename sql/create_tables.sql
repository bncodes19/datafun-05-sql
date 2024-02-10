DROP TABLE IF EXISTS car_models;
DROP TABLE IF EXISTS car_brands;

CREATE TABLE car_brands
(
    id           bigint not null
        constraint car_brands_pk
            primary key,
    brand_name   text,
    year_founded integer,
    country      text
);

CREATE TABLE car_models
(
    id              bigint,
    model_name      text,
    brand_id        bigint
        constraint car_models_car_brands_fk
            references car_brands,
    year_introduced text
);