-- Show the newest model introduction year to oldest

select b.brand_name, b.country, b.year_founded, m.model_name, m.year_introduced as model_introduced_date
from car_brands b
         join car_models m on b.id = m.brand_id
order by m.year_introduced desc;