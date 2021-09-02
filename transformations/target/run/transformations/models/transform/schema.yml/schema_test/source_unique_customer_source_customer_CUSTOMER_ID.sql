select
      count(*) as failures,
      count(*) != 0 as should_warn,
      count(*) != 0 as should_error
    from (
      
    
    

select
    CUSTOMER_ID,
    count(*) as n_records

from HEALTHCARE_CUSTOMER_DATA.public_intermediate_stg.customer
where CUSTOMER_ID is not null
group by CUSTOMER_ID
having count(*) > 1



      
    ) dbt_internal_test