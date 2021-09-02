{% macro create_customer_country(var_country)%}
SELECT *
FROM {{ref('stg_customer_data')}}
WHERE COUNTRY={{var_country}}
{% endmacro %}