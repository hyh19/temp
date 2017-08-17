# -*- coding: UTF-8 -*-
import sys
import openpyxl
from openpyxl.utils.cell import get_column_letter, column_index_from_string
import pprint
wb = openpyxl.load_workbook(sys.argv[1])
sheet = wb.get_sheet_by_name(unicode('上架0815', "utf-8"))

cell = sheet['I6']
print cell.value[0]

# 字段名称
PRD_GIFT_ID = 'gift_id'
PRD_CODE = 'prd_code'
PRD_NAME = 'prd_name'
PRD_POINT = 'origin_point'
PRD_TYPE = 'type'
PRD_EX_TIMES = 'ex_times'
PRD_MONTH_EXCHANGE = 'month_exchange'
PRD_START_TIME = 'start_time'
PRD_END_TIME = 'end_time'
PRD_EX_TYPE = 'exchange_type'
PRD_STOCK_COUNT = 'total_count'
PRD_MODULE = 'module'
PRD_SEQ_NO = 'seq_no'
PRD_STORE = 'store'
PRD_CARD = 'card_id'
PRD_DEL = 'is_del'

# xlsx字母列对应的字段名
PRD_COLUMN_NAME_DICT = {}
PRD_COLUMN_NAME_DICT['D'] = PRD_GIFT_ID
PRD_COLUMN_NAME_DICT['E'] = PRD_CODE
PRD_COLUMN_NAME_DICT['F'] = PRD_NAME
PRD_COLUMN_NAME_DICT['G'] = PRD_POINT
PRD_COLUMN_NAME_DICT['I'] = PRD_TYPE
PRD_COLUMN_NAME_DICT['J'] = PRD_EX_TIMES
PRD_COLUMN_NAME_DICT['K'] = PRD_MONTH_EXCHANGE
PRD_COLUMN_NAME_DICT['L'] = PRD_START_TIME
PRD_COLUMN_NAME_DICT['M'] = PRD_END_TIME
PRD_COLUMN_NAME_DICT['N'] = PRD_MONTH_EXCHANGE
PRD_COLUMN_NAME_DICT['O'] = PRD_STOCK_COUNT
PRD_COLUMN_NAME_DICT['Q'] = PRD_MODULE
PRD_COLUMN_NAME_DICT['R'] = PRD_SEQ_NO
PRD_COLUMN_NAME_DICT['S'] = PRD_STORE
PRD_COLUMN_NAME_DICT['T'] = PRD_CARD
PRD_COLUMN_NAME_DICT['U'] = PRD_DEL

# 将某一行的数据构建成一个字典
def buildRowDict(worksheet, row_index):
	row_dict = {}
	for row in worksheet.iter_rows(min_row=row_index, max_row=row_index):
		for cell in row:
			if cell.column in PRD_COLUMN_NAME_DICT:
				row_dict.setdefault(PRD_COLUMN_NAME_DICT[cell.column], cell.value)
	return row_dict

# tmp = buildRowDict(sheet, 2)
# pprint.pprint(tmp)

