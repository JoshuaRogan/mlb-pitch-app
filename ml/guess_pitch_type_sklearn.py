from __future__ import print_function

from sklearn.neighbors import KNeighborsClassifier
from sklearn.naive_bayes import GaussianNB, MultinomialNB, BernoulliNB
from sklearn.linear_model import LogisticRegression, SGDClassifier
from sklearn.svm import SVC, LinearSVC, NuSVC
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
import pandas as pd  # data processing, CSV file I/O (e.g. pd.read_csv)

# Guess the pitch type
DEBUG = 1
TRAIN_SIZE = .80
# KEYS = ['pitch_type', 'release_speed', 'release_pos_x', 'release_pos_z', 'release_pos_y',
#         'release_spin_rate', 'zone', 'pfx_x', 'pfx_z', 'plate_x', 'plate_z', 'vx0', 'vy0', 'vz0',
#         'ax', 'ay']

# Adding pitcher increases the accuracy of KNN by from 73% to 88%
KEYS = ['pitch_type', 'release_speed', 'release_spin_rate', 'zone', 'pfx_x', 'pfx_z', 'plate_x',
        'plate_z', 'vx0', 'vy0', 'vz0','ax', 'ay', 'pitcher']
# KEYS = ['pitch_type', 'pfx_x', 'pfx_z']
# KEYS = ['pitch_type', 'release_speed']
LABELS_KEY = 'pitch_type'
# DATA_FILE = '../data/2018_pitchers_all.csv'
# DATA_FILE = '../data/2018_pitchers_inning_1.csv'
DATA_FILE = '../data/braves_pitchers_2018.csv'
# DATA_FILE = '../data/folty.csv'

data = pd.read_csv(DATA_FILE)  # 89 Columns
data = data.dropna(subset=KEYS)  # Delete rows with empty data points
data = data[data.pitch_type != 'PO']
data = data[data.pitch_type != 'KN']
label_names = data.pitch_type.unique()
data = data.replace({label_names[i] : i for i in range(0, len(label_names) ) })
data = data.filter(KEYS)

num_labels = label_names.size
num_rows = data.shape[0]
num_features = data.shape[1]

train_data = data.head((int)(num_rows * TRAIN_SIZE))
test_data = data.tail(num_rows - (int)(num_rows * TRAIN_SIZE))

train_labels = train_data['pitch_type'].values
test_labels = test_data['pitch_type'].values

if train_data.pitch_type.unique().size != test_data.pitch_type.unique().size:
        print("data sizes not equal")
        exit(0)


train_data = train_data.drop(columns=['pitch_type'])
test_data = test_data.drop(columns=['pitch_type'])

# Initialize our classifiers
gnb = GaussianNB()
KNN = KNeighborsClassifier(n_neighbors=1)
MNB = MultinomialNB()
BNB = BernoulliNB()
LR = LogisticRegression(verbose=DEBUG)
SGD = SGDClassifier(verbose=DEBUG)
SVC = SVC(verbose=DEBUG)
LSVC = LinearSVC(verbose=DEBUG)
NSVC = NuSVC(verbose=DEBUG)

print('train', train_data.shape)
print('test', test_data.shape)
print(label_names)

# GaussianNB
# GaussianNB Accuracy : 0.6722359456011292
# gnb.fit(train_data, train_labels)
# y2_GNB_model = gnb.predict(test_data)
# print("GaussianNB Accuracy :", accuracy_score(test_labels, y2_GNB_model))
# print(classification_report(test_labels, y2_GNB_model, target_names=label_names, sample_weight=None, digits=4))
# print(label_names)
# print(confusion_matrix(test_labels, y2_GNB_model))

# K Nearest Keighboars
# KNN Accuracy : 0.6678248595238742
KNN.fit(train_data,train_labels)
y2_KNN_model = KNN.predict(test_data)
print("KNN Accuracy :", accuracy_score(test_labels, y2_KNN_model))
print(classification_report(test_labels, y2_KNN_model, target_names=label_names, sample_weight=None, digits=4))
print(label_names)
print(confusion_matrix(test_labels, y2_KNN_model))

# MultinomialNB
# MNB.fit(train_data,train_labels)
# y2_MNB_model = MNB.predict(test_data)
# print("MNB Accuracy :", accuracy_score(test_labels, y2_MNB_model))
# print(classification_report(test_labels, y2_MNB_model, target_names=label_names, sample_weight=None, digits=4))
# print(confusion_matrix(test_labels, y2_MNB_model))

# BernoulliNB
# BNB Accuracy : 0.4424251472624121
# BNB.fit(train_data,train_labels)
# y2_BNB_model = BNB.predict(test_data)
# print("BNB Accuracy :", accuracy_score(test_labels, y2_BNB_model))
# print(classification_report(test_labels, y2_BNB_model, target_names=label_names, sample_weight=None, digits=4))
# print(label_names)
# print(confusion_matrix(test_labels, y2_BNB_model))

# LogisticRegression
# LR Accuracy : 0.6863107033307093
# LR.fit(train_data,train_labels)
# y2_LR_model = LR.predict(test_data)
# print("LR Accuracy :", accuracy_score(test_labels, y2_LR_model))
# print(classification_report(test_labels, y2_LR_model, target_names=label_names, sample_weight=None, digits=4))
# print(label_names)
# print(confusion_matrix(test_labels, y2_LR_model))

# SGDClassifier
# SDG Accuracy : 0.32730258693232717
# SGD.fit(train_data,train_labels)
# y2_SGD_model = SGD.predict(test_data)
# print("SDG Accuracy :", accuracy_score(test_labels, y2_SGD_model))
# print(classification_report(test_labels, y2_SGD_model, target_names=label_names, sample_weight=None, digits=4))
# print(label_names)
# print(confusion_matrix(test_labels, y2_SGD_model))

# Support Vector Classifier
# SVC Accuracy : 0.4617327607981814
# SVC.fit(train_data,train_labels)
# y2_SVC_model = SVC.predict(test_data)
# print("SVC Accuracy :", accuracy_score(test_labels, y2_SVC_model))
# print(classification_report(test_labels, y2_SVC_model, target_names=label_names, sample_weight=None, digits=4))
# print(label_names)
# print(confusion_matrix(test_labels, y2_SVC_model))

# Linear Support Vector classifier
# LSVC.fit(train_data,train_labels)
# y2_LSVC_model = LSVC.predict(test_data)
# print("LSVC Accuracy :", accuracy_score(test_labels, y2_LSVC_model))
# print(classification_report(test_labels, y2_LSVC_model, target_names=label_names, sample_weight=None, digits=4))
# print(confusion_matrix(test_labels, y2_LSVC_model))

# NuSVC
# NSVC.fit(train_data,train_labels)
# y2_NSVC_model = NSVC.predict(test_data)
# print("NSVC Accuracy :", accuracy_score(test_labels, y2_NSVC_model))
# print(classification_report(test_labels, y2_NSVC_model, target_names=label_names, sample_weight=None, digits=4))
# print(label_names)
# print(confusion_matrix(test_labels, y2_NSVC_model))

