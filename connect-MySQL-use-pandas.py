## 需要的包
import pymysql
import pandas as pd
from sqlalchemy import create_engine

## 创建链接实例
engine = create_engine("mysql+pymysql://{}:{}@{}:{}/{}".format('usename', 'password', 'server ', 'hostname', 'database'))

# 查询语句
sql= 'select * from test_table'

# pd读取
df = pd.read_sql_query(sql,engine)


'''
返回DataFrame对象
'''
