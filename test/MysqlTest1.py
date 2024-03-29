# coding=utf-8
# 导入pymysql的包
import pymysql as pymysql

# 获取一个数据库连接，注意如果是UTF-8类型的，需要制定数据库
# port 必须是数字不能为字符串

connection = pymysql.connect(host='localhost',
                             user='root',
                             password='123456',
                             db='test',
                             port=3306,
                             charset='utf8')
try:
    # 获取一个游标
    with connection.cursor() as cursor:
        sql = 'select * from user'
        count = cursor.execute(sql)
        print("数量： " + str(count))

        for row in cursor.fetchall():
            print("ID: " + str(row[0]) + '  名字： ' + row[1] + "  性别： " + row[2])
        connection.commit()
except Exception:
    print("出错啦")

finally:
    connection.close()
