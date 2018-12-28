import MySQLdb

class MysqlSearch:
    def __init__(self):
        self.get_connection()
    
    def get_connection(self):
        try:
            self.connection = MySQLdb.connect(
                host = 'localhost',
                user = 'root',
                password = 'password',
                db = 'school',
                charset = 'utf8mb4',
                port = 3306 # 默认3306，可不填port
            )          
        except MySQLdb.Error as e:
            print('Error : %s ' % e)

    def close_connection(self):
        try:
            if self.connection:
                self.connection.close()
        except MySQLdb.Error as e:
            print('Error : %s ' % e)

    def get_one(self):
        # 获取会话指针
        cursor = self.connection.cursor()
        # 准备sql
        sql = 'SELECT * FROM `students`WHERE`name`=%s ORDER BY `in_time`DESC;'
        # 执行sql
        cursor.execute(sql,('weilai',)) 
        # print(cursor.description)
        ## (('id', 3, 1, 11, 11, 0, 0), ('name', 253, 6, 80, 80, 0, 0), 
        ## ('nickname', 253, 4, 80, 80, 0, 1), ('sex', 254, 3, 4, 4, 0, 1),
        ## ('in_time', 12, 19, 19, 19, 0, 1))
        ## 获得一条结果
        # a = [k[0] for k in cursor.description],
        ## a = ['id', 'name', 'nickname', 'sex', 'in_time']
        # b = [k[0] for k in cursor.description],cursor.fetchone()
        ## (['id', 'name', 'nickname', 'sex', 'in_time'],
        ##  (7, 'weilai', 'imwl', '男', datetime.datetime(2018, 12, 27, 22, 5, 41)))
        result = dict(zip([k[0] for k in cursor.description],cursor.fetchone()))  
        # 关闭 cursor 和连接
        cursor.close()
        self.close_connection()
        return result

    def get_more(self):
            cursor = self.connection.cursor()
            sql = 'SELECT * FROM `students`WHERE`name`=%s ORDER BY `in_time`DESC;'
            cursor.execute(sql,('weilai',)) 
            result = [dict(zip([k[0] for k in cursor.description],row))
                for row in cursor.fetchall()] 
            # print(result) 
            # [{'id': 7, 'name': 'weilai', 'nickname': 'imwl', 'sex': '男', 'in_time': datetime.datetime(2018, 12, 27, 22, 5, 41)}, 
            # {'id': 8, 'name':'weilai', 'nickname': 'imwl', 'sex': '男', 'in_time': datetime.datetime(2018, 12, 27, 22, 5, 41)},
            # {'id': 9, 'name': 'weilai', 'nickname': 'imwl', 'sex': '男', 'in_time': datetime.datetime(2018, 12, 27, 22, 5, 41)}]
            cursor.close()
            self.close_connection()
            return result


    def get_more_by_pages(self, page, page_size):
        # 分页查询数据
        offset =  (page -1) * page_size

        cursor = self.connection.cursor()
        sql = 'SELECT * FROM `students`WHERE`name`=%s ORDER BY `in_time`DESC LIMIT %s , %s;'
        cursor.execute(sql,('weilai', offset, page_size)) 
        result = [dict(zip([k[0] for k in cursor.description],row))
         for row in cursor.fetchall()] 
            # print(result) 
            # [{'id': 7, 'name': 'weilai', 'nickname': 'imwl', 'sex': '男', 'in_time': datetime.datetime(2018, 12, 27, 22, 5, 41)}, 
            # {'id': 8, 'name':'weilai', 'nickname': 'imwl', 'sex': '男', 'in_time': datetime.datetime(2018, 12, 27, 22, 5, 41)},
            # {'id': 9, 'name': 'weilai', 'nickname': 'imwl', 'sex': '男', 'in_time': datetime.datetime(2018, 12, 27, 22, 5, 41)}]
        cursor.close()
        self.close_connection()
        return result

    def add_one(self):
        # 准备SQL
        try:
            sql = (
                "INSERT INTO `students` (`name`,`nickname`,`sex`,`in_time`) VALUE"
                "(%s,%s,%s,%s);"
                )
            cursor = self.connection.cursor()

            # 可以提交多条
            cursor.execute(sql,('name1', 'nickname1', '男', None))
            cursor.execute(sql,('name2', 'nickname2', '男', 'haha'))
            # 提交事务
            self.connection.commit()
            # 关闭cursor和连接
            cursor.close()
            
        except MySQLdb.Error as e:
            print('Error : %s ' % e)
            self.connection.rollback()
        
        self.close_connection()


def main():
    obj = MysqlSearch()
    # a = obj.get_one()
    # print(a)
    # print(a['id'])

    # b = obj.get_more()
    # for item in b:
    #     print(item)

    # b = obj.get_more_by_pages(1,2)
    # for item in b:
    #     print(item)
    obj.add_one()

if __name__ == '__main__':
    main()

# zip函数
'''
zip() 将对象中对应的元素打包成一个个元组，然后返回由这些元组组成的对象，元素个数与最短的一致
>>> a = [1,2,3]
>>> b = [4,5,6]
>>> c = [4,5,6,7,8]
>>> zipped = zip(a,b)     # 返回一个对象
>>> zipped
<zip object at 0x103abc288>
>>> list(zipped)  # list() 转换为列表
[(1, 4), (2, 5), (3, 6)]
>>> list(zip(a,c))              # 元素个数与最短的列表一致
[(1, 4), (2, 5), (3, 6)]
 
>>> a1, a2 = zip(*zip(a,b))          # 与 zip 相反，zip(*) 可理解为解压，返回二维矩阵式
>>> list(a1)
[1, 2, 3]
>>> list(a2)
[4, 5, 6]
'''