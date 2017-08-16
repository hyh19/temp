# -*- coding: UTF-8 -*-
import mysql.connector
from datetime import datetime

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

def insertNewGift(conn, cur, gift):
	add_gift = ("INSERT INTO product "
                "(gift_id, prd_code, prd_name, origin_point, type, ex_times, start_time, end_time, exchange_type, stock_id, seq_no, module, description, store_scope, card_id, is_del, month_exchange) "
                "VALUES (%(gift_id)s, %(prd_code)s, %(prd_name)s, %(origin_point)s, %(type)s, %(ex_times)s, %(start_time)s, %(end_time)s, %(exchange_type)s, %(stock_id)s, %(seq_no)s, %(module)s, %(description)s, %(store_scope)s, %(card_id)s, %(is_del)s, %(month_exchange)s)")
	cur.execute(add_gift, gift)
	conn.commit()

test_gift = {}
test_gift['gift_id'] = '1-1LZQW899999'
test_gift['prd_code'] = '1115000000122'
test_gift['prd_name'] = '袋鼠妈妈 孕妇天然豆乳洗面奶洁面乳100g'
test_gift['origin_point'] = 2888
test_gift['type'] = '2'
test_gift['ex_times'] = 1
test_gift['start_time'] = datetime(2017, 8, 21, 15, 1, 28)
test_gift['end_time'] = datetime(2017, 12, 21, 15, 1, 28)
test_gift['exchange_type'] = 1
test_gift['stock_id'] = 313
test_gift['seq_no'] = 24
test_gift['module'] = 2
test_gift['description'] = 'xxx'
test_gift['store_scope'] = 0
test_gift['card_id'] = '91'
test_gift['is_del'] = 0
test_gift['month_exchange'] = 1

insertNewGift(cnx, cursor, test_gift)
# row = cursor.fetchone()
# print row
# for row in cursor:
#   print(row)

cursor.close()
cnx.close()