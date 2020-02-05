from preprocessing import preprocessing
from mazda import mazda
from excel import excel
from excelrep import excelrep
from logreg_undersampling import lr
from svm_undersampling import svm_under
from random_forest_undersampling import rf
from logreg_oversampling import logreg_over
from svm_oversampling import svm_over
from random_forest_oversampling import rf_over

if not input("Is Image Pre-processing already done?(y/n)").lower() == 'y':
    first = preprocessing()
if not input("Is Image feature extraction already done?(y/n)").lower() == 'y':
    second = mazda()
input("maZda stage completed. Hit Enter")
third = excel()
input("Hit Enter")
fourth = excelrep()
print("Final Data Matrix created.")
print("Which Machine Learning Algorithm do you want to run?")
print("1. Logistic Regression with Undersampling")
print("2. Support Vector Machine with Undersampling")
print("3. Random Forest with Undersampling")
print("4. Logistic Regression with Oversampling")
print("5. Support Vector Machine with Oversampling")
print("6. Random Forest with Oversampling")
choice = int(input())
while choice in [1, 2, 3, 4, 5, 6]:
    if choice == 1:
        fifth = lr()
        choice = 0
    elif choice == 2:
        fifth = svm_under()
        choice = 0
    elif choice == 3:
        fifth = rf()
        choice = 0
    elif choice == 4:
        fifth = logreg_over()
        choice = 0
    elif choice == 5:
        fifth = svm_over()
        choice = 0
    elif choice == 6:
        fifth = rf_over()
        choice = 0
    else:
        print("Wrong Choice, please try again...")
        choice = int(input())
