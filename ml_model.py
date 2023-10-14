import pandas as pd
from keras.preprocessing.text import Tokenizer
import tensorflow
import numpy as np
from keras.preprocessing.sequence import pad_sequences
from sklearn.model_selection import train_test_split
from keras.models import Sequential
from keras.layers import Dense, Flatten
from keras.layers import Embedding

#read in data
data = pd.read_csv("input_data.csv")

#data preprocess
data["Location"] = data["Location"].apply(lambda x: 0 if x == "Database" else 1)
X = data["Question"].to_numpy()
y = data["Location"].to_numpy()

#change strings to numerical data
tokenizer = Tokenizer()
tokenizer.fit_on_texts(X)
sequences = tokenizer.texts_to_sequences(X)


max_words = 5000
max_length = 50

#Length can be changed, try 20 for now
X = pad_sequences(sequences, maxlen=max_length)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.1, random_state=42)


print(X_test, y_test)
print(len(X_test[0]))

model = Sequential()
model.add(Embedding(max_words, 32, input_length=max_length))
model.add(Flatten())
model.add(Dense(128, activation='relu'))
model.add(Dense(64, activation='relu'))
model.add(Dense(32, activation='relu'))
model.add(Dense(1, activation='sigmoid'))
model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy']) 
model.summary()


hist = model.fit(X_train, y_train, validation_split=0.1, epochs=20, batch_size=20)

input = ["What homework is due next week?"]

tokenizer.fit_on_texts(input)
sequences = tokenizer.texts_to_sequences(input)
input = pad_sequences(sequences, maxlen=max_length)

res = model.predict(input)

print(res[0][0])
