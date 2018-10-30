import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
from keras.models import Sequential
from keras.layers import Dense, Activation
import numpy as np

TRAIN_SIZE = .8

# 89 Columns
data = pd.read_csv("../data/folty.csv")
rows = data.shape[0]
features = data.shape[1]

labels = labels.get('pitch_type') # First column values
train_labels = labels.get(0) # 0-TRAIN_SIZE of

# Get TRAIN_SIZE of data with 88 columns
# train = data

print(train)
model = Sequential()
model.add(Dense(32, activation='relu', input_dim=features - 1))
model.add(Dense(1, activation='sigmoid'))
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
# model.fit(data, labels, epochs=10, batch_size=32)
