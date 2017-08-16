# -*- coding: UTF-8 -*-
import mysql.connector

cnx = mysql.connector.connect(user='root', password='tcbj',
                              host='192.168.103.107',
                              database='wxexchange')
if cnx.is_connected():
	print '已连接数据库'
else:
	print '数据库连接失败'

cursor = cnx.cursor(buffered=True)

# query = "SELECT * FROM product WHERE gift_id = %(gift_id)s"
# query = ("SELECT * FROM product")

# cursor.execute(query)

cursor.execute('SELECT * FROM product WHERE gift_id = "1-2DJ-98"')
if cursor.with_rows:
	print "有数据"
# row = cursor.fetchone()
# print row
# for row in cursor:
#   print(row)

cursor.close()
cnx.close()