import xlwt
import xlrd


class excelrep:
    def __init__(self):
        self.startrun()

    def startrun(self):
        workbook = xlrd.open_workbook(r'C:\Sagar_Agrawal\Projects\ML\Codes\output\Reports\out.xls')
        sheet = workbook.sheet_by_index(0)

        workbook1 = xlwt.Workbook()
        sheet1 = workbook1.add_sheet('sheet1')
        count = 0

        for i in range(0, 126, 1):
            if (i == 1) or (i == 13) or (i == 25) or (i == 37) or (i == 49) or (i == 81) or (i == 87):
                pass
            else:
                data = [sheet.cell_value(row, i) for row in range(sheet.nrows)]
                for index, value in enumerate(data):
                    sheet1.write(index, count, value)
                count += 1

        workbook1.save(r'C:\Sagar_Agrawal\Projects\ML\Codes\output\Reports\out.xls')
