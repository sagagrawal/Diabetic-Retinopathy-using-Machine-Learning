from xlrd import *
from xlwt import *
import csv
import glob


class excel:
    def __init__(self):
        self.startrun()

    def startrun(self):
        book = Workbook(encoding='utf-8')
        sheet = book.add_sheet('Sheet1', cell_overwrite_ok=True)

        ann = open_workbook(r"C:\Sagar_Agrawal\Projects\ML\Base11\Annotation_Base11.xls")
        ann_sheet = ann.sheet_by_index(0)

        imagename = ann_sheet.col_values(0, 0)
        rowx = 0
        for name in imagename:
            sheet.write(rowx, 0, imagename[rowx])
            rowx += 1

        files = glob.glob(r"C:\Sagar_Agrawal\Projects\ML\Codes\output\Reports\*.par")
        rowx = 1
        for filename in files:
            inp = open(filename, "r")
            in_txt = csv.reader(inp, delimiter='\t')

            for j in range(0, 18, 1):
                next(in_txt, None)

            colx = 1
            if rowx == 1:
                for row in in_txt:
                    sheet.write(0, colx, row[0])
                    sheet.write(rowx, colx, float(row[1]))
                    colx += 1
            else:
                for row in in_txt:
                    sheet.write(rowx, colx, float(row[1]))
                    colx += 1
            rowx += 1
            inp.close()

        imagename = ann_sheet.col_values(3, 0)
        rowx = 0
        for name in imagename:
            sheet.write(rowx, colx, imagename[rowx])
            rowx += 1

        book.save(r'C:\Sagar_Agrawal\Projects\ML\Codes\output\Reports\out.xls')
