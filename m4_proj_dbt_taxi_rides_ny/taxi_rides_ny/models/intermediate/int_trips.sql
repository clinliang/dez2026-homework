{{
    config(
        materialized='incremental',
        unique_key='trip_id',
        pre_hook=[
            "SET temp_directory = '/mnt/d/github/tmp/';",
            "SET max_temp_directory_size = '40GB';",
            "SET memory_limit = '4GB';"
        ]
    )
}}

with payment_type as (
    select 
        payment_type,
        payment_type_detail
    from {{ ref('payment_type_lookup') }}
),


trip_base as (  
    select

        -- primary key: trip_id md5
        {{ dbt_utils.generate_surrogate_key([
            'u.vendor_id', 
            'u.pickup_datetime', 
            'u.pickup_location_id', 
            'u.service_type'
            ]) }} as trip_id,

-- where mod(abs(hash(vendor_id, pickup_datetime, pickup_location_id, service_type)), 10) = {{ var('bucket') }}

        u.vendor_id,
        u.pickup_datetime,   
        u.pickup_location_id,
        u.service_type,

        u.rate_code_id,
        u.dropoff_datetime,
        {{ get_trip_duration_minutes('u.pickup_datetime', 'u.dropoff_datetime') }} as trip_duration_minutes,

        u.dropoff_location_id,
        u.store_and_fwd_flag,
        u.passenger_count,
        u.trip_distance,
        u.trip_type,
        u.fare_amount,
        u.extra,
        u.mta_tax,
        u.tip_amount,
        u.tolls_amount,
        u.ehail_fee,
        u.improvement_surcharge,
        u.total_amount,

         {{get_month_from_date('u.pickup_datetime')}} as revenue_month,

        ifnull(u.payment_type, 5) as payment_type,
        ifnull(t.payment_type_detail, 'unknown') as payment_type_detail

    from {{ ref('int_trips_unioned') }} as u
    left join payment_type as t
        on ifnull(u.payment_type, 5) = t.payment_type
),

bucketed as (
    select *
    from trip_base
    where mod(abs(hash(trip_id)), 10) = {{ var('bucket', 0) }}
)

select *
from bucketed

qualify row_number() over(
    partition by trip_id
    order by dropoff_datetime
) = 1