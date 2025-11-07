select
id As customer_id,
name As customer_name,
email,
country
FROM {{source('raw_data','customers')}}