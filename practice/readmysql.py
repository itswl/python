


import pymysql.cursors

connection = pymysql.connect(host = 'localhost',
                user = 'root',
                password = 'password',
                db = 'baikeurl',
                charset = 'utf8mb4',
                     )
try:
    # 获取会话指针
    with connection.cursor() as cursor:
        # 查询sql 语句
        sql = 'select `urlname` , `urlhref` from `urls` where `id` is not null'
        # 执行sql 语句
        conut = cursor.execute(sql)
        print(conut)

        # result = cursor.fetchall()
        # print(result)

finally:
    connection.close()

    '''
查询数据库

cursor.execute()   得到总记录数
cursor.fetchone()  查询下一行
cursor.fetchmany(size=None)   得到指定大小
cursor.fetchall    得到全部
 
'''