

      create or replace transient table HEALTHCARE_CUSTOMER_DATA.PUBLIC.customer_newyork  as
      (


SELECT *
FROM HEALTHCARE_CUSTOMER_DATA.PUBLIC_intermediate_stg.stg_customer_data
WHERE COUNTRY='NYC'

      );
    