select
      count(*) as failures,
      count(*) != 0 as should_warn,
      count(*) != 0 as should_error
    from (
      
    
    

select *
from HEALTHCARE_CUSTOMER_DATA.public_intermediate_stg.customer
where CUSTOMER_NAME is null



      
    ) dbt_internal_test