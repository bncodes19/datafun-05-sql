-- Show the country of car models by country as well as the oldest model and newest model introduction year for each country

select b.country, count(m.id) count_of_car_models, min(m.year_introduced) oldest_model_year, max(m.year_introduced) newest_model_year
from car_brands b
         join car_models m on b.id = m.brand_id
group by b.country;