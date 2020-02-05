import xlrd
import cv2
import numpy as np
 
def open_file(path):
    #Open and read an Excel file
    book = xlrd.open_workbook(path)
     
    # print number of sheets
    '''print book.nsheets
     
    # print sheet names
    print book.sheet_names()
     
    # get the first worksheet'''
    sheet = book.sheet_by_index(0)
     
    ''' read a row
    print first_sheet.row_values(0)
     
    # read a cell 
    cell = first_sheet.cell(0,0)
    print cell
    print cell.value
     
    # read a row slice'''
    for i in range(2, 6, 1):
        Matrix = np.zeros(shape=(850, 2300))
        li = sheet.col_values(colx=i, start_rowx=1, end_rowx=101)
        min_ind = li.index(min(li)) + 2
        max_ind = li.index(max(li)) + 2
        min_name = sheet.cell_value(min_ind, 0)
        max_name = sheet.cell_value(max_ind, 0)
        min_risk = sheet.cell_value(min_ind, 311)
        max_risk = sheet.cell_value(max_ind, 311)
        img1 = cv2.imread(("C:\\Users\\Jags\\Desktop\\DRIVE\\OUTPUT\\" + str(min_name)).replace(".tif",".bmp"), 0)
        img2 = cv2.imread(("C:\\Users\\Jags\\Desktop\\DRIVE\\OUTPUT\\" + str(max_name)).replace(".tif",".bmp"), 0)
        height, width = img2.shape[:2]

        for j in range(0, height, 1):
            for k in range(0, width, 1):
                Matrix[j, k] = img1[j, k]
        
        for j in range(0, height, 1):
            for k in range(0, width, 1):
                Matrix[j, k+1120] = img2[j, k]
                
        cv2.putText(Matrix, min_name,(320, 750), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)
        cv2.putText(Matrix, max_name, (1470, 750), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)
                
        cv2.putText(Matrix, "Min "+sheet.cell_value(0,i)+" = "+str(min(li)),(350,795), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)
        cv2.putText(Matrix, "Max "+sheet.cell_value(0,i)+" = "+str(max(li)),(1500,795), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)
        
        cv2.putText(Matrix, "Risk = "+min_risk, (420, 835), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)
        cv2.putText(Matrix, "Risk = "+max_risk, (1570, 835), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)
        
        cv2.imwrite("C:\\Users\\Jags\\Desktop\\DRIVE\\"+str(i)+".bmp", Matrix)
    
 
if __name__ == "__main__":
    path = "Final.xlsx"
    open_file(path)
