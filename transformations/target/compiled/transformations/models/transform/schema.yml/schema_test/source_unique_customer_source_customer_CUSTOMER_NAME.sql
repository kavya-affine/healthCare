
    
    

select
    CUSTOMER_NAME,
    count(*) as n_records

from HEALTHCARE_CUSTOMER_DATA.public_intermediate_stg.customer
where CUSTOMER_NAME is not null
group by CUSTOMER_NAME
having count(*) > 1


