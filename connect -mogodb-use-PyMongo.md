# python连接MongoDB

## 依赖库

+ pymongo
  安装方式：
  
  ```python
  pip install pymongo
  ```

\# 连接MongoDB<br>
import pymongo<br>
\# 连接<br>
mydbclient =  pymongo.MongoClient("mongodb://locakhost:port/")

\# 查看文件名称 <br>
blist = myclient.list_database_names()
