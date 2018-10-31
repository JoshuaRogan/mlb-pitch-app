import pandas as pd  # data processing, CSV file I/O (e.g. pd.read_csv)
from keras.models import Sequential
from keras.layers import Dense, Activation
from keras.utils import to_categorical
import numpy as np
from numpy import argmax

# Guess the pitch type

BATCH_SIZE = 32
TRAIN_SIZE = .8
KEYS = ['pitch_type', 'release_speed', 'release_pos_x', 'release_pos_z', 'release_pos_y' 'zone', 'pfx_x', 'pfx_z', 'plate_x', 'plate_z']
KEYS = ['pitch_type', 'release_speed']
LABELS_KEY = 'pitch_type'

data = pd.read_csv("../data/folty.csv")  # 89 Columns
data = data.dropna(subset=[LABELS_KEY])  # Delete rows with empty pitch_types
data = data.replace({'FF': 0, 'SL': 1, 'CH': 2, 'CU': 3, 'FT': 4}) # Convert pitches to nums
data = data.filter(KEYS)

num_rows = data.shape[0]
num_features = data.shape[1]

train_data = data.head((int)(num_rows * TRAIN_SIZE))
test_data = data.tail(num_rows - (int)(num_rows * TRAIN_SIZE))

train_labels = train_data['pitch_type'].values
test_labels = test_data['pitch_type'].values

train_data = train_data.drop(columns=['pitch_type'])
test_data = test_data.drop(columns=['pitch_type'])

model = Sequential()
model.add(Dense(BATCH_SIZE, activation='relu', input_dim=num_features - 1))
model.add(Dense(5, activation='sigmoid'))
model.compile(optimizer='rmsprop',
              loss='categorical_crossentropy',
              metrics=['accuracy'])

model.compile(optimizer='rmsprop',
              loss='categorical_crossentropy',
              metrics=['accuracy'])
#
# # Generate dummy data
#
# data = np.random.random((1000, 100))
# labels = np.random.randint(2, size=(1000, 1))
#
# # Train the model, iterating on the data in batches of 32 samples
model.fit(train_data, to_categorical(train_labels), epochs=20, batch_size=BATCH_SIZE)

# score = model.evaluate(test_data, to_categorical(test_labels),
#                        batch_size=BATCH_SIZE, verbose=1)
# print('Test score:', score[0])
# print('Test accuracy:', score[1])
prediction = model.predict(test_data.iloc[2:3], batch_size=None, verbose=0, steps=None)

print(test_data.iloc[0:3])
print(test_data.iloc[2:3])
print(test_labels[2])
print(argmax(prediction))
# For a single-input model with 10 classes (categorical classification):

# model = Sequential()
# model.add(Dense(32, activation='relu', input_dim=100))
# model.add(Dense(10, activation='softmax'))
# model.compile(optimizer='rmsprop',
#               loss='categorical_crossentropy',
#               metrics=['accuracy'])
#
# # Generate dummy data
# import numpy as np
# data = np.random.random((1000, 100))
# labels = np.random.randint(10, size=(1000, 1))
#
# # Convert labels to categorical one-hot encoding
# one_hot_labels = keras.utils.to_categorical(labels, num_classes=10)
#
# # Train the model, iterating on the data in batches of 32 samples
# model.fit(data, one_hot_labels, epochs=10, batch_size=32)
