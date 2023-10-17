import pandas as pd
from keras.preprocessing.text import Tokenizer
import pickle
from keras.preprocessing.sequence import pad_sequences
from sklearn.model_selection import train_test_split
from keras.models import Sequential
from keras.layers import Dense, Flatten
from keras.layers import Embedding
from keras.utils import to_categorical

#read in data
data = pd.read_csv("input_data.csv")

#data preprocess
data["Location"] = data["Location"].apply(lambda x: 1 if x == "Database" else 0)
X = data["Question"].to_numpy()
y = data["Location"].to_numpy()

#encode y to two classes
y = to_categorical(y, num_classes=2)

#change strings to numerical data
tokenizer = Tokenizer()
tokenizer.fit_on_texts(X)
sequences = tokenizer.texts_to_sequences(X)

max_words = 5000
max_length = 30

X = pad_sequences(sequences, maxlen=max_length)


X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.1, random_state=42)

model = Sequential()
model.add(Embedding(max_words, 32, input_length=max_length))
model.add(Flatten())
model.add(Dense(512, activation='relu'))
model.add(Dense(256, activation='relu'))
model.add(Dense(128, activation='relu'))
model.add(Dense(64, activation='relu'))
model.add(Dense(16, activation='relu'))
model.add(Dense(2, activation='softmax'))
model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy']) 
model.summary()


hist = model.fit(X_train, y_train, validation_split=0.3, epochs=25, batch_size=50)

model_pkl_file = "database_text_question_classifier.pkl"
with open(model_pkl_file, 'wb') as file:  
    pickle.dump(model, file)

token_pkl_file = "tokenizer.pkl"
with open(token_pkl_file, 'wb') as file:
    pickle.dump(tokenizer, file)