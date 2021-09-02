import snowflake.connector

def get_database_connection(user, password, account, database, schema):
    print("DB Connection : START : " + __name__)
    try:
        return snowflake.connector.connect(
            user=user,
            password=password,
            account=account,
            database=database,
            schema = schema
        )
    except Exception:
        print("Exception while creating connection")