select

    cast(dispatching_base_num as varchar) as dispatching_base_num,
    cast(pickup_datetime as timestamp) as pickup_datetime,
    cast(dropoff_datetime as timestamp) as dropoff_datetime,
    cast(PULocationID as integer) as pickup_location_id,
    cast(DOLocationID as integer) as dropoff_location_id,
    cast(SR_Flag as integer) as sr_flag,
    cast(Affiliated_base_number as varchar) as affiliated_base_number

from {{ source('raw_data', 'fhv_tripdata') }}

-- filtering out rows with null dispatching_base_num (data quality requirement)
where dispatching_base_num IS NOT NULL