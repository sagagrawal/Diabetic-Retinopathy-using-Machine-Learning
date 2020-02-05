from sklearn import model_selection, preprocessing
from sklearn.decomposition import PCA
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix,accuracy_score
import random
import numpy as np
from sklearn.ensemble import RandomForestClassifier

class rf:

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
        for train_index, test_index in loo:
            flag = 0
            diseased = diseased_all.copy()
            X = preprocessing.normalize(X)
            pca = PCA(n_components=60)
            pca.fit(X)
            X = pca.transform(X)
            random.seed(1)
            if y[test_index] == 1:
                random_healthy = random.sample(healthy, hlen-dlen-1)
                for i in range(0, dlen, 1):
                    if test_index == diseased[i]:
                        diseased = np.delete(diseased, i)
                        break
            else:
                random_healthy = random.sample(healthy, hlen-dlen+1)
                for i in range(0, hlen-dlen+1, 1):
                    if test_index == random_healthy[i]:
                        random_healthy = np.delete(random_healthy, i)
                        flag = 1
                        break
                if flag == 0:
                    random_healthy = np.delete(random_healthy, dlen)

            diseased = diseased.astype(int)
            random_healthy = np.asarray(random_healthy, dtype=int)
            train_indices = np.insert(random_healthy, 0, diseased)

            X_train = X[train_indices]
            X_test = X[test_index]
            y_train = y[train_indices]
            y_test = y[test_index]
            clf = RandomForestClassifier()
            y_pred = clf.fit(X_train,y_train).predict(X_test)
            cm[int(y_test), int(y_pred)] += 1
        acc = (cm[0, 0] + cm[1, 1]) / 4
        print(acc)
        print(cm)
