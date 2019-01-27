import configparser


class MysqlConfigParser(configparser.ConfigParser):

    _redundunt_keys = {'mysqld': ['binlog-do-db', 'binlog-ignore-db']}

    def _read(self, fp, fpname):
        super()._read(fp, fpname)
        if self.has_section
