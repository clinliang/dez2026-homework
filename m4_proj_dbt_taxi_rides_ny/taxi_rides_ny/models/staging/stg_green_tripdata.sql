with source as (
    
    select * from {{ source('raw_data', 'green_tripdata') }}

    where vendorid is not null -- filter out null vendorid rows

    {% if target.name == 'dev' %}
    and lpep_pickup_datetime >= '2019-01-01'
    and lpep_pickup_datetime < '2019-02-01'
    {% endif %}
),

renamed as (

    select
        -- identifiers
        cast(Vendorid as integer) as vendor_id,
        {{safe_cast('RatecodeID', 'integer')}} as rate_code_id,
        cast(PULocationID as integer) as pickup_location_id,
        cast(DOLocationID as integer) as dropoff_location_id,

        -- timesstamps
        cast(lpep_pickup_datetime as timestamp) as pickup_datetime,
        cast(lpep_dropoff_datetime as timestamp) as dropoff_datetime,
        
        -- drop information
        store_and_fwd_flag,
        cast(passenger_count as integer) as passenger_count,
        cast(trip_distance as numeric) as trip_distance,
        {{safe_cast('trip_type', 'integer')}} as trip_type,

        --payment information
        cast(fare_amount as numeric) as fare_amount,
        cast(extra as numeric) as extra,
        cast(mta_tax as numeric) as mta_tax,
        cast(tip_amount as numeric) as tip_amount,
        cast(tolls_amount as numeric) as tolls_amount,
        cast(ehail_fee as numeric) as ehail_fee,
        cast(improvement_surcharge as numeric) as improvement_surcharge,
        cast(total_amount as numeric) as total_amount,
        {{safe_cast('payment_type', 'integer')}} as payment_type

    from source 
)

select * from renamed

