import mysqlconfigparser
from pprint import pprint

c = mysqlconfigparser.MysqlConfigParser(strict=False)
c.read('test.my.cnf')

pprint(c.get('mysqld','test'))
pprint(c.get('mysqld','test2'))
pprint(c.items('mysqld'))