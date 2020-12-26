import xlrd
import xlwt
from xlutils.copy import copy
import os

def read_sheet():
        workbook = xlrd.open_workbook(r'D:\python\testdat\studentinformation.xlsx')
        sheet1 = workbook.sheets()[0]
        sheet = copy(workbook)
        sheet2 = sheet.get_sheet(0)

        for i in range(1,sheet1.nrows):
            num = sheet1.cell_value(i,2)
            photo_data = list(os.walk('D:\python\testdat' + str(int(num))))[0][2:]
            print(photo_data[0])
            if not photo_data[0]:
                color = xlwt.easyxf('pattern: pattern solid, fore_colour yellow;')
                sheet2.write(i, 1, sheet1.cell_value(i,2), color)
                sheet.save('D:\python\testdat\studentinformation.xlsx')
            elif '.jpg' in photo_data[0][0]:
                sheet2.write(i, 2, 'D:\python\testdat' + str(int(element)))
                sheet.save('D:\python\testdat\studentinformation.xlsx')
    
if __name__ == '__main__':
    read_sheet()
