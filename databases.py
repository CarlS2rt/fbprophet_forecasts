import pyodbc
import cx_Oracle
from sqlalchemy import create_engine
from sqlalchemy.engine import URL
from sqlalchemy.types import String


def ssms():
    connection_string = '''DRIVER={SQL Server};
            SERVER=TVERINT01FMSN\IMPACT360,1433;
            DATABASE=BPMAINDB;
            Trusted_Connection=yes;'''
    connection_url = URL.create("mssql+pyodbc", query={"odbc_connect": connection_string})

    engine = create_engine(connection_url,fast_executemany=True)
    verint = engine.connect()
    return verint
    print('Verint connected')

def oracle(user,password):
    DIALECT = 'oracle'
    SQL_DRIVER = 'cx_oracle'
    USERNAME = user
    PASSWORD = password
    HOST = 'RACPRD06.TDS.LOCAL'
    PORT = 1521
    SERVICE = 'DB070'
    ENGINE_PATH_WIN_AUTH = DIALECT + '+' + SQL_DRIVER + '://' + USERNAME + ':' + PASSWORD +'@' + HOST + ':' + str(PORT) + '/?service_name=' + SERVICE

    engine = create_engine(ENGINE_PATH_WIN_AUTH)
    ods = engine.connect()
    return ods
    print(f'{user} Connected')

def variables():
    sql_server = '''DRIVER={SQL Server};
                SERVER=TVERINT01FMSN\IMPACT360,1433;
                DATABASE=BPMAINDB;
                Trusted_Connection=yes;'''
    sql_server_url = URL.create("mssql+pyodbc", query={"odbc_connect": sql_server})
    return sql_server_url