# -*- coding:utf8 -*-

import xlwt
import xlrd
import os
from common.base import consoleLog


class Excel(object):
    """Excel对象
    :param path: Excel路径
    :param sheetIndex: 表索引
    :param sheetName: 表名
    """

    def __init__(self, path=None, sheetIndex=1, sheetName=None):
        self.sheetIndex = sheetIndex - 1
        if path:
            self.path = path
            if not os.path.exists(self.path):
                consoleLog('文件不存在！')
                exit()
            else:
                self.sheetName = sheetName
                self.book = xlrd.open_workbook(self.path)

    def sheet(self, sheetIndex=None, sheetName=None):
        """表格，默认第一张表"""
        if sheetIndex:
            return self.book.sheet_by_index(int(sheetIndex)-1)
        elif sheetName:
            return self.book.sheet_by_name(sheetName)
        else:
            return self.book.sheet_by_index(self.sheetIndex) if not self.sheetName else self.book.sheet_by_name(self.sheetName)

    def create(self, name, sheetNames=['sheet1', 'sheet2', 'sheet3']):
        """创建表格，桌面如果有则不操作没有则创建,并且创建三张表"""
        path = 'C:\Users\Administrator\Desktop\%s.xlsx' % name
        if not os.path.exists(path):
            self.book = xlwt.Workbook(encoding='utf-8', style_compression=0)
            for sheetName in sheetNames:
                self.book.add_sheet(sheetName, cell_overwrite_ok= True)
            self.book.save(path)
        else:
            consoleLog(u'表格:%s 已存在！' % name)
            return

    def writeCell(self, row, col, value, sheetIndex=1, sheetName=None):
        if sheetName:
            self.sheet(sheetName=sheetName).write(row-1, col-1, value.decode('utf-8'))
        else:
            self.sheet(sheetIndex=sheetIndex).write(row-1, col-1, value.decode('utf-8'))

    def readCell(self, row, col):
        """坐标单元格内容"""
        if row ==0 or col == 0:
            consoleLog('行或列不能等于0')
        else:
            return self.sheet().cell_value(row-1, col-1)

    def readRow(self,row):
        """整行数据列表"""
        if row == 0:
            consoleLog('行不能等于0')
        else:
            return self.sheet().row_values(row-1)

    def readCol(self, col):
        """整列数据列列表"""
        if col == 0:
            consoleLog('列不能等于0')
        else:
            return self.sheet().col_values(col-1)


