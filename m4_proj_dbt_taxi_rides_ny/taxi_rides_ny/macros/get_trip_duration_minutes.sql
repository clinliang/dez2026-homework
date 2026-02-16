-- macros/get_trip_duration_minutes.sql
{% macro get_trip_duration_minutes(start_time, end_time) %}

    {% if target.type == 'bigquery' %}
        TIMESTAMP_DIFF({{ end_time }}, {{ start_time }}, MINUTE)

    {% elif target.type == 'snowflake' %}
        DATEDIFF(MINUTE, {{ start_time }}, {{ end_time }})

    {% elif target.type == 'postgres' %}
        EXTRACT(EPOCH FROM ({{ end_time }} - {{ start_time }}))/60
        
    {% elif target.type == 'duckdb' %}
        DATEDIFF('minute', {{ start_time }}, {{ end_time }})

    {% endif %}
{% endmacro %}