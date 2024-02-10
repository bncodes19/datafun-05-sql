-- Show how many car models there are for each car brands

select b.brand_name, count(m.id) model_count
from car_brands b
         join car_models m on b.id = m.brand_id
group by b.brand_name;