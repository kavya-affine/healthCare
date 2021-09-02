/*Change date formate for Open_date, last_consulted_date and DOB, ephemeral*/



with change as(
    select 
    Customer_Name,
    Customer_Id,
    TO_DATE(Open_Date),
    TO_DATE(Last_Consulted_Date),
    Vaccination_Id,
    Dr_Name,
    State,
    Country,
    TO_DATE(DOB),
    Is_Active
    from HEALTHCARE_CUSTOMER_DATA.public.customer
)
select * from change