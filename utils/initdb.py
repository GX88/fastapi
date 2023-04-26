import os
import pymysql
import shutil


class initdb(object):
    def __init__(self):
        self.host = "localhost"
        self.port = 3306
        self.username = "root"
        self.password = "199907173030bz"
        self.database = "fastapi"
        self.orm = "database.ORM_CONFIG"
        self.db = pymysql.connect(host=self.host, port=int(self.port), user=self.username, password=self.password,
                                  charset='utf8mb4')

    def is_exist_database(self) -> bool:
        cursor = self.db.cursor()
        sql = "select * from information_schema.SCHEMATA WHERE SCHEMA_NAME = '%s'  ; " % self.database
        res = cursor.execute(sql)
        if res:
            # print('\033[31m---> 数据库已经存在,为防止误初始化,请手动删除 %s 数据库\033[0m' % str(
            #     self.database))
            return True
        self.init_database()

    def init_database(self):
        if os.path.exists(os.path.join(os.getcwd(),'migrations')):
            shutil.rmtree(os.path.join(os.getcwd(),'migrations'))
            print("""\033[32m---> 删除冗余文件\033[0m""")
        cursor = self.db.cursor()
        sql = "CREATE DATABASE IF NOT EXISTS %s CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;" % self.database
        res = cursor.execute(sql)
        if res:
            print('\033[32m---> 数据库%s创建成功\033[0m' % str(self.database))
            self.create_table()

    def create_table(self) -> bool:
        if os.system('c init -t %s' % self.orm) != 0:
            print("""\033[31m 当您看到此信息时，说明 aerich 初始化错误，但是我并不能为你捕获此错误; 但导致出现问题出现的原因有：
                1. TORTOISE_ORM配置的位置错误, 您可能把配置变成了路径，但他实质为 文件夹.文件.配置名称
                2. 不存在此文件夹
            \033[0m""")
            return False
        if os.system('aerich init-db ') == 0:
            print('\033[32m---> 数据库写入成功\033[0m')
        return True

        
    def __del__(self):
        try:
            self.db.close()
        except pymysql.Error as e:
            pass

init_db = initdb()