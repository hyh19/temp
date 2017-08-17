# -*- coding: UTF-8 -*-
import string

# 移除字符串左右两侧的空白符
def strippedString(str):
	return string.strip(str)

str = "  hello world  "
print strippedString(str)