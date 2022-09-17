import bs4
import requests
from bs4 import BeautifulSoup
url = 'http://192.168.1.8:8080/安阳工学院.html'
r = requests.get(url)

soup = BeautifulSoup(r.text,'html.parser')
print(soup.prettify())
list = soup.get_text()
import pymysql
# 连接数据库
try:
    db1 = pymysql.Connect(
        host='120.77.181.2',
        port=3306,
        user='zhongze',
        passwd='aa123123',
        db='zhongze',
        charset='utf8mb4')
    cur = db1.cursor()
    print("数据库连接成功")

    # 写一条sql语句
    sql = 'update college set introduction = \'{0}\' where id in(select a.id from (select id from college where name = "安阳工学院" )a)'.format(list)
    print("数据库连接成功sql",sql)
    cur.execute(sql)
    db1.commit()

except pymysql.Error as e:
    print("数据插入失败："+str(e))
    db1.rollback()
    db1.close()
