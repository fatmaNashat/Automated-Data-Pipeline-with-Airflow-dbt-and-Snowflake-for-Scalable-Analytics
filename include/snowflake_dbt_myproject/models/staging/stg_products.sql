select
id As product_id,
name As product_name,
category As product_category,
price As product_price
FROM {{source('raw_data','products')}}