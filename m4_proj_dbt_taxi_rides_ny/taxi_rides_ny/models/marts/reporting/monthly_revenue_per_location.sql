with source as (
    select
        trip_id,
        passenger_count,
        trip_distance,

        pickup_zone,
        revenue_month,
        service_type,

        fare_amount,
        extra,
        mta_tax,
        tip_amount,
        tolls_amount,
        ehail_fee,
        improvement_surcharge,
        total_amount

    from {{ ref('fct_trips') }}
)

select
    -- Group by
    pickup_zone,
    revenue_month,
    service_type,

    -- Revenue
    sum(fare_amount) as monthly_fare,
    sum(extra) as monthly_extra,
    sum(mta_tax) as monthly_mta_tax,
    sum(tip_amount) as monthly_tip_amount,
    sum(tolls_amount) as monthly_tolls_amount,
    sum(ehail_fee) as monthly_ehail_fee,
    sum(improvement_surcharge) as monthly_improvement_surcharge,
    sum(total_amount) as monthly_total_amount,

    -- Analysis
    count(trip_id) as monthly_trips_number,
    avg(passenger_count) as monthly_avg_passengers,
    avg(trip_distance) as monthly_avg_trip_distance

from source
group by pickup_zone, revenue_month, service_type