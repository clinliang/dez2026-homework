with source as (

    select * from {{ source('raw_data', 'yellow_tripdata') }}

    where vendorid is not null -- filter out null vendorid rows

    {% if target.name == 'dev' %}
    and tpep_pickup_datetime >= '2019-01-01'
    and tpep_pickup_datetime < '2019-02-01'
    {% endif %}
),


renamed as (

    select
        -- identifiers
        cast(Vendorid as integer) as vendor_id,
        cast(RatecodeID as integer) as rate_code_id,
        cast(PULocationID as integer) as pickup_location_id,
        cast(DOLocationID as integer) as dropoff_location_id,

        -- timesstamps
        cast(tpep_pickup_datetime as timestamp) as pickup_datetime,
        cast(tpep_dropoff_datetime as timestamp) as dropoff_datetime,
        
        -- drop information
        cast(store_and_fwd_flag as string) as store_and_fwd_flag,
        cast(passenger_count as integer) as passenger_count,
        cast(trip_distance as numeric) as trip_distance,

        --payment information
        cast(fare_amount as numeric) as fare_amount,
        cast(extra as numeric) as extra,
        cast(mta_tax as numeric) as mta_tax,
        cast(tip_amount as numeric) as tip_amount,
        cast(tolls_amount as numeric) as tolls_amount,
        cast(improvement_surcharge as numeric) as improvement_surcharge,
        cast(total_amount as numeric) as total_amount,
        cast(payment_type as integer) as payment_type

    from source
)

select * from renamed
