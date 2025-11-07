select
id As item_id,
order_id,
product_id,
quantity,
unit_price,
(quantity*unit_price) As total_price
FROM {{source('raw_data','order_items')}}