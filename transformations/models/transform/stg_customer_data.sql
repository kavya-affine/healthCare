/*Change date formate for Open_date, last_consulted_date and DOB, ephemeral*/

{{
    config(
        materialized = 'table'
    )
}}

    select 
    CAST(CUSTOMER_NAME AS VARCHAR(255)) as "CUSTOMER NAME",
    CAST(CUSTOMER_ID AS VARCHAR(18)) as "CUSTOMER ID", 
    TO_DATE(TO_CHAR(CUSTOMER_OPEN_DATE), 'YYYYMMDD') as "CUSTOMER OPEN DATE", 
    TO_DATE(TO_CHAR(LAST_CONSULTED_DATE),'YYYYMMDD') as "LAST CONSULTED DATE",
    CAST(VACCINATION_TYPE AS CHAR(5)) as "VACCINATION TYPE", 
    CAST(DOCTOR_CONSULTED AS CHAR(255)) as "DOCTOR CONSULTED", 
    CAST(STATE AS CHAR(5)) as STATE, 
    CAST(COUNTRY AS CHAR(5)) as COUNTRY,
    TO_DATE(TO_CHAR(DATE_OF_BIRTH),'MMDDYYYY') as "DATE OF BIRTH",
    CAST(ACTIVE_CUSTOMER AS CHAR(1)) as "ACTIVE CUSTOMER"
    from {{source('customer_source','customer')}}
