import csv
import pandas as pd
from pandas import read_csv, DataFrame, Series
import matplotlib.pyplot as plt
from sklearn import cross_validation, svm
from sklearn.neighbors import KNeighborsClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.tree import DecisionTreeClassifier

from sklearn.metrics import roc_curve, auc
import pylab as pl

data = read_csv('ScannedUser.csv')
print(data)

target = data.isBot
train = data.drop(['id', 'isBot'], axis=1)
kfold = 5 #количество подвыборок для валидации
itog_val = {}

ROCtrainTRN, ROCtestTRN, ROCtrainTRG, ROCtestTRG = cross_validation.train_test_split(train, target, test_size=0.25)
model_rfc = RandomForestClassifier(n_estimators = 200, min_samples_leaf = 5, max_depth = 10) #в параметре передаем кол-во деревьев
model_knc = KNeighborsClassifier(n_neighbors = 7) #в параметре передаем кол-во соседей
model_dtc= DecisionTreeClassifier(max_depth=5)
model_svc = svm.SVC(kernel = 'poly', C=100,gamma=100)

scores = cross_validation.cross_val_score(model_rfc, train, target, cv = kfold)
itog_val['RandomForestClassifier'] = scores.mean()
scores = cross_validation.cross_val_score(model_knc, train, target, cv = kfold)
itog_val['KNeighborsClassifier'] = scores.mean()
scores = cross_validation.cross_val_score(model_dtc, train, target, cv = kfold)
itog_val['DecisionTreeClassifier'] = scores.mean()
scores = cross_validation.cross_val_score(model_svc, train, target, cv = kfold)
itog_val['SVC'] = scores.mean()

DataFrame.from_dict(data = itog_val, orient='index').plot(kind='bar', legend=False)
plt.show()

#SVC
model_svc.probability = True
probas = model_svc.fit(ROCtrainTRN, ROCtrainTRG).predict_proba(ROCtestTRN)
fpr, tpr, thresholds = roc_curve(ROCtestTRG, probas[:, 1])
roc_auc  = auc(fpr, tpr)
pl.plot(fpr, tpr, label='%s ROC (area = %0.2f)' % ('SVC', roc_auc))
#RandomForestClassifier
probas = model_rfc.fit(ROCtrainTRN, ROCtrainTRG).predict_proba(ROCtestTRN)
fpr, tpr, thresholds = roc_curve(ROCtestTRG, probas[:, 1])
roc_auc  = auc(fpr, tpr)
pl.plot(fpr, tpr, label='%s ROC (area = %0.2f)' % ('RandomForest',roc_auc))
#KNeighborsClassifier
probas = model_knc.fit(ROCtrainTRN, ROCtrainTRG).predict_proba(ROCtestTRN)
fpr, tpr, thresholds = roc_curve(ROCtestTRG, probas[:, 1])
roc_auc  = auc(fpr, tpr)
pl.plot(fpr, tpr, label='%s ROC (area = %0.2f)' % ('KNeighborsClassifier',roc_auc))
#DecisionTreeClassifier
probas = model_dtc.fit(ROCtrainTRN, ROCtrainTRG).predict_proba(ROCtestTRN)
fpr, tpr, thresholds = roc_curve(ROCtestTRG, probas[:, 1])
roc_auc  = auc(fpr, tpr)
pl.plot(fpr, tpr, label='%s ROC (area = %0.2f)' % ('DecisionTreeClassifier',roc_auc))
pl.plot([0, 1], [0, 1], 'k--')
pl.xlim([0.0, 1.0])
pl.ylim([0.0, 1.0])
pl.xlabel('False Positive Rate')
pl.ylabel('True Positive Rate')
pl.legend(loc=0, fontsize='small')

pl.show()


test = read_csv('SomeScannedUser.csv')
#df = read_csv('SomeScannedUser2.csv')
test = test.drop(['id'], axis=1)

model_knc.fit(train, target)

#print(list(zip(train, model_svc.feature_importances_)))
# knc rfc  svc
x = model_knc.predict(test)
print(model_knc.predict(test))
print(model_knc.predict_proba(test))
#df.insert(len(x),'isBot', x)
#df.to_csv('SomeScannedUser2.csv', index=False)