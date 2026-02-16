with trips as (
    select
        distinct vendor_id
    from {{ ref('int_trips') }}
),

vendors as (
    select
        distinct vendor_id,
        {{ get_vendor_data('vendor_id') }} as vendor_name
    from trips
)

select * from vendors