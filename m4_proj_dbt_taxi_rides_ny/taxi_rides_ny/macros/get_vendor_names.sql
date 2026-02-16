{% macro get_vendor_data(vendor_id_column) %}

{# 
    PURPOSE: Map vendor IDs to their business names using a CASE statement.
    ARGUMENTS: 
        - vendor_id_column: The name of the column containing vendor IDs (string).
#}

{%- set vendors = {
    1: 'Creative Mobile Technologies',
    2: 'VeriFone Inc.',
    4: 'Unknown/Other'
} -%}

case {{ vendor_id_column }}
    {% for vendor_id, vendor_name in vendors.items() -%}
    when {{ vendor_id }} then '{{ vendor_name }}'
    {% endfor -%}
    else 'N/A'
end

{% endmacro %}