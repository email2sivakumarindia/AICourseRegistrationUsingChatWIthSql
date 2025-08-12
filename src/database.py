
from langchain_community.utilities import SQLDatabase
from urllib.parse import quote_plus


def init_database(user: str, password: str, host: str, port: str, database: str) -> SQLDatabase:
  #db_uri = f"mysql+mysqlconnector://{user}:{password}@{host}:{port}/{database}"
  password = "Welcome@1"  # Example password with special characters
  encoded_password = quote_plus(password)  # Encodes '@' -> '%40', '!' -> '%21'

  db_uri = f"mysql+mysqlconnector://root:{encoded_password}@localhost:3306/testsqlai"
  #db_uri = "mysql+mysqlconnector://root:Welcome@123@localhost:3306/mydatabase"
  return SQLDatabase.from_uri(db_uri)