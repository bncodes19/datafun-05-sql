-- Join the car_brands and car_models tables together based on their relation

select b.brand_name, m.model_name, m.year_introduced as model_introduce_date
from car_brands b
         join car_models m on b.id = m.brand_id;