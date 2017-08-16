# -*- coding: UTF-8 -*-
import os
import sys
import openpyxl
from openpyxl.utils.cell import get_column_letter, column_index_from_string
import pprint
# print(os.getcwd())
wb = openpyxl.load_workbook(sys.argv[1])
# sheets = wb.get_sheet_names()
# print sheets
sheet = wb.get_sheet_by_name(unicode('上架0815', "utf-8"))
# print sheet.title
# cell = sheet['F13']
# print cell.value

max_row = sheet.max_row
# print max_row
# max_col = sheet.max_column
# print max_col


PRD_COLUMN_NAME_DICT = {}
PRD_COLUMN_NAME_DICT['D'] = 'gift_id'
PRD_COLUMN_NAME_DICT['E'] = 'prd_code'
PRD_COLUMN_NAME_DICT['F'] = 'prd_name'
PRD_COLUMN_NAME_DICT['G'] = 'origin_point'
PRD_COLUMN_NAME_DICT['I'] = 'type'
PRD_COLUMN_NAME_DICT['J'] = 'ex_times'
PRD_COLUMN_NAME_DICT['K'] = 'month_exchange'
PRD_COLUMN_NAME_DICT['L'] = 'start_time'
PRD_COLUMN_NAME_DICT['M'] = 'end_time'
PRD_COLUMN_NAME_DICT['N'] = 'exchange_type'
PRD_COLUMN_NAME_DICT['O'] = 'total_count'
PRD_COLUMN_NAME_DICT['Q'] = 'module'
PRD_COLUMN_NAME_DICT['R'] = 'seq_no'
PRD_COLUMN_NAME_DICT['S'] = 'store'
PRD_COLUMN_NAME_DICT['T'] = 'card_id'
PRD_COLUMN_NAME_DICT['U'] = 'is_del'

# def getColumnValue(worksheet, row_index):
# 	column_index = column_index_from_string(column_letter)
# 	return worksheet.cell(row=row_index, column=column_index).value

# 将某一行的数据构建成一个字典
def buildRowDict(worksheet, row_index):
	row_dict = {}
	for row in worksheet.iter_rows(min_row=row_index, max_row=row_index):
		for cell in row:
			if cell.column in PRD_COLUMN_NAME_DICT:
				row_dict.setdefault(PRD_COLUMN_NAME_DICT[cell.column], cell.value)
	return row_dict

ttt = buildRowDict(sheet, 2)
pprint.pprint(ttt)


# for row in range(2, max_row):
	# print(getColumnValue(sheet, row, COL_GIFT_ID))
	# print(getColumnValue(sheet, row, COL_PRD_CODE))
	# print(getColumnValue(sheet, row, COL_PRD_NAME))
	# print(getColumnValue(sheet, row, COL_ORIGIN_POINT))
	# print(getColumnValue(sheet, row, COL_PRD_TYPE))
	# print(getColumnValue(sheet, row, COL_EX_TIMES))
	# print(getColumnValue(sheet, row, COL_MONTH_LIMIT))
	# print(getColumnValue(sheet, row, COL_START_TIME))
	# print(getColumnValue(sheet, row, COL_END_TIME))
	# print(getColumnValue(sheet, row, COL_EXPRESS_TYPE))
	# print(getColumnValue(sheet, row, COL_TOTAL_COUNT))
	# print(getColumnValue(sheet, row, COL_PRD_MODULE))
	# print(getColumnValue(sheet, row, COL_SEQ_NO))
	# print(getColumnValue(sheet, row, COL_SPEC_STORE))
	# print(getColumnValue(sheet, row, COL_NEED_CARD))
	# print(getColumnValue(sheet, row, COL_IS_DEL))

