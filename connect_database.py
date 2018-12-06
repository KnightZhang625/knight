# This is used for connect with database
# 

import sys
import psycopg2
import pandas as pd
from knight.Info import Info

class ConnectDatabaseAPI(object):
    def __init__(self, user, password, database = 'bayesba', host='192.168.1.6', port=5432):
        self.user = user
        self.password = password
        self.database = database
        self.host = host
        self.port = port

        self._make_Connect()
        information = Info()

    def _make_Connect(self):
        self.conn = psycopg2.connect(host=self.host, port=self.port, user=self.user, password=self.password, database=self.database)
        return self.conn

    def read_Sql(self, sql_syntax):
        return pd.read_sql(sql_syntax, self.conn)