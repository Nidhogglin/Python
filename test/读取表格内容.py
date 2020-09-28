#!usr/bin/env python3
# coding: utf-8
# @time :2020/9/21 15:50

import xlrd
from datetime import datetime
import json


def demo():
    wb =xlrd.open_workbook('maidian.xlsx')
    sh = wb.sheet_by_index(0)
    rowName = sh.row_values(0)
    colName = sh.col_values(0)
    row = len(rowName)
    col = len(colName)
    valu = sh.cell(1, 6).value
    print(rowName, '\n', colName)
    print(row, col, valu)
    dt = datetime.fromtimestamp(sh.cell(11, 0).value / 1000)
    print(dt)
    jsons = json.loads(sh.cell(1, 18).value)
    print(jsons['tokenCheck_code'])


if __name__ == '__main__':
    demo()

