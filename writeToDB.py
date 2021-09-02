import snowflake.connector
from sqlalchemy import create_engine
from snowflake.connector.pandas_tools import pd_writer
import readFiles

def writeToTable(customer_data):

    # Fill in your SFlake details here
    engine = create_engine(
        'snowflake://{user}:{password}@{account_identifier}/{database}/{schema}'.format(
            user='kavya1191',
            password='Shree1191',
            account_identifier='ef60810.ap-south-1.aws',
            database='HEALTHCARE_CUSTOMER_DATA',
            schema = 'public_intermediate_stg'
        )
    )

    try:
        customer_data.to_sql('customer', engine, index=False, method=pd_writer) #make sure index is False, Snowflake doesnt accept indexes
        print("DATA INSERTED")
    except Exception as e:
        print("ERROR!!")
        print(e)

    engine.dispose()