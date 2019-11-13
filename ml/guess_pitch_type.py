import pandas as pd  # data processing, CSV file I/O (e.g. pd.read_csv)
from keras.models import Sequential
from keras.layers import Dense, Activation, Dropout
from keras.utils import print_summary, to_categorical, plot_model
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
from keras.layers.normalization import BatchNormalization

import numpy as np
from numpy import argmax

# Guess the pitch type
BATCH_SIZE = 10
TRAIN_SIZE = .80
KEYS = ['pitch_type', 'release_speed', 'release_pos_x', 'release_pos_z', 'release_pos_y',
        'release_spin_rate', 'zone', 'pfx_x', 'pfx_z', 'plate_x', 'plate_z', 'vx0', 'vy0', 'vz0',
        'ax', 'ay', 'pitcher']
# KEYS = ['pitch_type', 'release_speed', 'release_spin_rate', 'zone', 'pfx_x', 'pfx_z', 'plate_x',
#         'plate_z', 'vx0', 'vy0', 'vz0','ax', 'ay']
# KEYS = ['pitch_type', 'pfx_x', 'pfx_z']
# KEYS = ['pitch_type', 'release_speed']
LABELS_KEY = 'pitch_type'
# DATA_FILE = '../data/2018_pitchers_all.csv'
DATA_FILE = '../data/braves_pitchers_2019.csv'
# DATA_FILE = '../data/folty.csv'

data = pd.read_csv(DATA_FILE)  # 89 Columns
data = data.dropna(subset=KEYS)  # Delete rows with empty data points
data = data[data.pitch_type != 'PO'] # Very rare pitch (pitch out)
data = data[data.pitch_type != 'KN'] # Very rare pitch (knuckle ball)
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

# train_data = train_data.drop(columns=['pitch_type'])
# test_data = test_data.drop(columns=['pitch_type'])

# https://www.reddit.com/r/MachineLearning/comments/6xvnwo/d_my_neural_network_isnt_working_what_should_i_do/
model = Sequential()

# Input Layer
model.add(Dense(num_labels, input_dim=train_data.shape[1]))
model.add(BatchNormalization())
model.add(Activation('relu'))

# Output Layer (more than one values so need a probabilty)
model.add(Dense(num_labels))
model.add(BatchNormalization())
model.add(Activation(activation='sigmoid'))


model.compile(optimizer='rmsprop',
              loss='categorical_crossentropy',
              metrics=['accuracy'])
model.fit(train_data, to_categorical(train_labels), epochs=40, batch_size=BATCH_SIZE)
# classes = model.predict(test_data, batch_size=BATCH_SIZE)


score = model.evaluate(test_data, to_categorical(test_labels), batch_size=BATCH_SIZE, verbose=1)

print_summary(model)
print('Test score:', score)
# print('Test score:', score[0])
print('Test accuracy:', score[1])

prediction = model.predict(test_data, batch_size=None, verbose=True, steps=None)
print(label_names)
print(confusion_matrix(test_labels, prediction.argmax(axis=1)))
#
# print(test_data.iloc[0:4])
# print(test_data.iloc[3:4])
# print(test_labels[3])
# print(argmax(prediction))
# For a single-input model with 10 classes (categorical classification):
