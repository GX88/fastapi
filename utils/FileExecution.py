# _*_ coding:utf-8 _*_

import pymysql, os


class FileExecution(object):
    def __init__(self, project_path):
        self.sql_path = project_path + '/sql'
        self.sql_file = []
        self.execute_fromfile()

    def get_sql_file(self):
        """
        获取sql文件
        :return: sql文件列表
        """
        # 循环获取sql文件夹下后缀为 .sql的文件名，存入列表
        for root, dirs, files in os.walk(self.sql_path):
            for file in files:
                if file.endswith('.sql'):
                    self.sql_file.append(self.sql_path + '/' + file)

    def execute_fromfile(self):
        """
        执行sql文件
        :return: None
        """
        self.get_sql_file()
        for file in self.sql_file:
            with open(file, 'r', encoding='utf-8') as f:
                lines = f.read().splitlines()
                sql_data = ''
                for line in lines:
                    if line.startswith('--'):
                        continue
                    if not line or line.startswith('#'):
                        continue
                    sql_data += line
                sql_list = sql_data.split(';')[:-1]
                sql_list = [x.replace('\n', ' ') if '\n' in x else x for x in sql_list]
                print(sql_list)
