from sklearn import svm, model_selection, preprocessing
from sklearn.decomposition import PCA
from sklearn.model_selection import train_test_split,cross_val_score
from sklearn.metrics import confusion_matrix,accuracy_score,roc_auc_score
import random
import numpy as np
from smote import Over

class svm_over():

    def __init__(self):
        f = open("C:\\Users\\Admin\\Desktop\\Final.txt")
        f.readline()  # skip the header
        data = np.loadtxt(f)

        X = data[:, 1:]  # select columns 1 through end
        y = data[:, 0]   # select column 0, the risk

        imageno = len(y)
        healthy = np.zeros(np.sum(y == 0), np.int)
        diseased = np.zeros(np.sum(y == 1), np.int)

        j = 0
        k = 0
        for i in range(0, imageno, 1):
            if y[i] == 0:
                healthy[j] = i
                j += 1
            else:
                diseased[k] = i
                k += 1

        loo = model_selection.LeaveOneOut(imageno)
        self.classify(X, y, healthy, diseased, loo)

    def classify(self, X, y, healthy, diseased, loo):
        cm = np.zeros((2, 2))
        dlen = len(diseased)
        hlen = len(healthy)
        diseased_all = np.zeros(dlen, np.int)
        diseased_all = diseased.copy()
        acc = 0
        perc = (((hlen - dlen) / dlen) + 1) * 100
        
        for train_index, test_index in loo:
            diseased = diseased_all.copy()
            random_healthy = healthy.copy()
            X = preprocessing.normalize(X)
            pca = PCA(n_components=60)
            pca.fit(X)
            X = pca.transform(X)
            diseased_over = Over().SMOTE(X[diseased], perc, 2)
            random.seed(1)
            if y[test_index] == 1:
                random_diseased = random.sample(diseased_over, hlen-dlen+1)
                remaining = np.ones(hlen-dlen+1, dtype=np.int)
                for i in range(0, dlen, 1):
                    if test_index == diseased[i]:
                        diseased = np.delete(diseased, i)
                        break
            else:
                random_diseased = random.sample(diseased_over, hlen-dlen-1)
                remaining = np.ones(hlen - dlen - 1, dtype = np.int)
                for i in range(0, hlen, 1):
                    if test_index == random_healthy[i]:
                        random_healthy = np.delete(random_healthy, i)
                        break

            X_train = np.concatenate((X[random_healthy], X[diseased], random_diseased))
            X_test = X[test_index]
            y_train = np.concatenate((y[random_healthy], y[diseased], remaining))
            y_test = y[test_index]
            classifier = svm.SVC()
            clf = classifier.fit(X_train, y_train)
            y_pred = clf.predict(X_test)
            cm[int(y_test), int(y_pred)] += 1
        acc = (cm[0, 0] + cm[1, 1]) / 4
        print(acc)
        print(cm)
