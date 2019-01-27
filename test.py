import mysqlconfigparser
from pprint import pprint

c = mysqlconfigparser.MysqlConfigParser()
c.read('test.my.cnf')
pprint(c.items('mysqld'))