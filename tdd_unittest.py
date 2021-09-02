import unittest
import pathlib as pl
from unittest.mock import patch
from readFiles import source_file, sourceColumns
import snowflakedb
import snowflake.connector

# testcase for file existence
class Filepath_TestCaseBase(unittest.TestCase):
    def assertIsFile(self, path):
        if not pl.Path(path).resolve().is_file():
            raise AssertionError("File does not exist: %s" % str(path))

class FilepathActualTest(Filepath_TestCaseBase):
    def test(self):
        path = pl.Path(source_file)
        self.assertIsFile(path)

# test case for columns existence as required
class SourceColumns_TestCaseBase(unittest.TestCase):
    def assertSourceColumns(self, sourceColumns):
        columns = ['Unnamed: 0', 'H', 'Customer_Name', 'Customer_Id', 'Open_Date', 'Last_Consulted_Date', 'Vaccination_Id', 'Dr_Name', 'State', 'Country', 'DOB', 'Is_Active']
        if columns != sourceColumns:
            raise AssertionError("Mismatch in Columns: Required columns ['Unnamed: 0', 'H', 'Customer_Name', 'Customer_Id', 'Open_Date', 'Last_Consulted_Date', 'Vaccination_Id', 'Dr_Name', 'State', 'Country', 'DOB', 'Is_Active'] ")

class SourceColumns_ActualTest(SourceColumns_TestCaseBase):
    def test(self):
        self.assertSourceColumns(sourceColumns)


# test case for mock snowflake connection
class SnowflakeDbTest(unittest.TestCase):

        @patch('writeToDB.snowflake.connector')
        def test_get_database_connection(self, mock_connection):
            mock_connection.connect.return_value = "dbconnection"
            self.assertEqual("dbconnection", snowflakedb.get_database_connection('kavya1191', 'Shree1191', 'ef60810.ap-south-1.aws', 'HEALTHCARE_CUSTOMER_DATA', 'public'))


if __name__ == "__main__":
    unittest.main()