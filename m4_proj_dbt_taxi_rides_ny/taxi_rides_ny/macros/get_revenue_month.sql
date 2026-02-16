{% macro get_month_from_date(date_column) %}
    {% if target.type == 'bigquery' %}
        cast(date_trunc({{ date_column }}, month) as date)
    {% elif target.type == 'duckdb' %}
        date_trunc('month', {{ date_column }})::date
    {% elif target.type == 'snowflake' %}
        date_trunc('month', {{ date_column }})::date
    {% elif target.type == 'postgres' %}
        date_trunc('month', {{ date_column }})::date
    {% else %}
        date_trunc('month', {{ date_column }})
    {% endif %}
{% endmacro %}