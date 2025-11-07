select
id As order_id,
customer_id ,
order_date,
status As order_status
FROM {{source('raw_data','orders')}}