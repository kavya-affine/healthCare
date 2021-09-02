# healthCare
Multi-Specialty Hospital chain with locations all across the world. My hospital is famous for Vaccination. To split up the customers based on the country and load them into corresponding country tables.


**tdd_unittest.py** - Contain test cases for 
1. Source file existence
2. Columns existence as required
3. Snowflake connection

**readFiles.py** - Read source file and clean data
**writeToDB.py** - Connect to Snowflake and Create table, insert data from file

**DBT for transformation**

**transformations\models\transform\schema.yml** 
1. Source table specification
2. Unique and null value testing

**transformations\models\transform\stg_customer_data.sql** - Convert datatype and date format

**transformations\macros\customer_country.sql** - macro file helps to reuse query in creating master tables

**transformations\models\master** - Models for all master tables **customer_country**
