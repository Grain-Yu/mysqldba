# -*- coding: utf-8 -*-#

# -------------------------------------------------------------------------------
# Name:         snapshot
# Description:
# Author:       xucl
# Date:         2019-04-17
# -------------------------------------------------------------------------------

from utils import *
from db_pool import DBAction


class Topsql(object):
    def __init__(self, connection_settings):
        self.conn_setting = connection_settings
        print("")
        print("starting mysql topsql")

    def run(self):
        global dbaction

        # 第一次获取MySQL&系统状态
        dbaction = DBAction(self.conn_setting)
        sorted_dict = sort_fromfile()
        topsql_dict = get_topsql(dbaction,sorted_dict)
        for i in range(len(topsql_dict)):
            print(topsql_dict[i])

if __name__ == '__main__':
    args = command_line_args(sys.argv[1:])
    conn_setting = {'host': args.host, 'port': args.port,
                    'user': args.user, 'password': args.password, 'charset': 'utf8'}
    topsql = Topsql(connection_settings=conn_setting)
    topsql.run()
