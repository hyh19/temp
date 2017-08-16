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

def isGiftExist(cur, gid):
	select_stmt = "SELECT * FROM product WHERE gift_id = %(gift_id)s"
	cur.execute(select_stmt, {'gift_id': gid})
	return (cur.rowcount > 0)

# row = cursor.fetchone()
# print row
# for row in cursor:
#   print(row)

cursor.close()
cnx.close()