## read customer data from .csv file and load data to staging tables
import pandas as pd
import writeToDB

source_file = "customer_data.csv"
# pandas function to read source data
customer_df = pd.read_csv(source_file, delimiter="|")
# columns in source file
sourceColumns =  list(customer_df)

def cleanData(customer_df):
    # remove unwanted column "Unnamed: 0" and  "H"
    customer_df.drop('Unnamed: 0', inplace=True, axis=1)
    customer_df.drop('H', inplace=True, axis=1)
    customer_df = customer_df.rename(columns={"Customer_Name": "CUSTOMER_NAME", "Customer_Id": "CUSTOMER_ID", "Open_Date":"CUSTOMER_OPEN_DATE", "Last_Consulted_Date":"LAST_CONSULTED_DATE",
    "Vaccination_Id":"VACCINATION_TYPE", "Dr_Name":"DOCTOR_CONSULTED", "State":"STATE", "Country":"COUNTRY", "DOB":"DATE_OF_BIRTH", "Is_Active":"ACTIVE_CUSTOMER"})
    return customer_df

if __name__ == '__main__':
    customer_df = cleanData(customer_df)
    writeToDB.writeToTable(customer_df)