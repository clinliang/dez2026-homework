{{
    config(
        materialized='incremental',
        unique_key='trip_id',
        incremental_strategy='merge',
        on_schema_change='append_new_columns',
        pre_hook=[
            "SET temp_directory = '/mnt/d/github/tmp/';",
            "SET max_temp_directory_size = '40GB';",
            "SET memory_limit = '4GB';"
        ]
    )
}}


select
    t.trip_id,
    t.vendor_id,
    t.service_type,
    
    -- pickup details
    t.pickup_datetime,   
    t.pickup_location_id,
    zp.borough as pickup_borough,
    ifnull(zp.zone, 'Unknown Zone') as pickup_zone,

    -- dropoff details
    t.dropoff_datetime,
    t.dropoff_location_id,
    zd.borough as dropoff_borough,
    zd.zone as dropoff_zone,

    -- other trip details
    t.rate_code_id,
    t.store_and_fwd_flag,
    t.passenger_count,
    t.trip_distance,
    t.trip_duration_minutes,
    t.trip_type,

    -- payment details
    t.fare_amount,
    t.extra,
    t.mta_tax,
    t.tip_amount,
    t.tolls_amount,
    t.ehail_fee,
    t.improvement_surcharge,
    t.total_amount,
    t.payment_type,
    t.payment_type_detail,
    t.revenue_month

from {{ref('int_trips')}} as t
left join {{ref('dim_zones')}} as zp
    on t.pickup_location_id = zp.location_id
left join {{ref('dim_zones')}} as zd
    on t.dropoff_location_id = zd.location_id

where 1=1
{% if is_incremental() %}
  and pickup_datetime > (select max(pickup_datetime) from {{ this }})
{% endif %}