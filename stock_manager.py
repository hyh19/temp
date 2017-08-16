# -*- coding: UTF-8 -*-
import sys
import openpyxl
from openpyxl.utils.cell import get_column_letter, column_index_from_string
import pprint
wb = openpyxl.load_workbook(sys.argv[1])
sheet = wb.get_sheet_by_name(unicode('上架0815', "utf-8"))

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

# 将某一行的数据构建成一个字典
def buildRowDict(worksheet, row_index):
	row_dict = {}
	for row in worksheet.iter_rows(min_row=row_index, max_row=row_index):
		for cell in row:
			if cell.column in PRD_COLUMN_NAME_DICT:
				row_dict.setdefault(PRD_COLUMN_NAME_DICT[cell.column], cell.value)
	return row_dict

tmp = buildRowDict(sheet, 2)
pprint.pprint(tmp)

