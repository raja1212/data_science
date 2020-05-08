import pandas as pd
import numpy as np
import tensorflow as tf
from tensorflow.keras import Sequential
from tensorflow.keras.layers import Dense, LSTM

tf.random.set_seed(100)


def create_sequence(input_data, steps):
    i = 0
    x = []
    y = []
    while (i + steps) < len(input_data):
        x.append(input_data[i:i + steps])
        y.append(input_data[i + steps])
        i = i + 1
    return np.asarray(x), np.asarray(y)


def read_input_data():
    df = pd.read_csv('data/germany.csv')
    return df.to_numpy()


def train(x, y):
    row_index = x.shape[0] - 1
    x, x_test = x[:row_index], x[row_index]
    y, y_test = y[:row_index], y[row_index]
    # reshape from [samples, timesteps] into [samples, timesteps, features]
    n_features = 1
    x = x.reshape((x.shape[0], x.shape[1], n_features))
    print(x.shape)

    # define model
    model = Sequential()
    model.add(LSTM(100, activation='relu', return_sequences=True, input_shape=(n_steps, n_features)))
    model.add(LSTM(100, activation='relu'))
    model.add(Dense(1))
    model.compile(optimizer='adam', loss='mse')
    model.summary()

    model.fit(x, y, epochs=1000, verbose=2)

    x_test = x_test.reshape((1, n_steps, n_features))
    yhat = model.predict(x_test, verbose=0)

    print(f"Predicted Value: {yhat[0][0]}")
    print(f"Original value: {y_test}")

    # model.save("germany_prediction_05_april.h5")


n_steps = 3
data = read_input_data()
x, y = create_sequence(data, n_steps)
train(x, y)
