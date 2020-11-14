import numpy as np
from keras.models import Sequential
from keras.layers import LSTM
from keras.layers import Dense

import data_analysis

# split a univariate sequence into samples


def split_sequence(sequence, n_steps):
    X, y = list(), list()
    for i in range(len(sequence)):
        # find the end of this pattern
        end_ix = i + n_steps
        # check if we are beyond the sequence
        if end_ix > len(sequence)-1:
            break
        # gather input and output parts of the pattern
        seq_x, seq_y = sequence[i:end_ix], sequence[end_ix]
        X.append(seq_x)
        y.append(seq_y)
    return np.array(X), np.array(y)


def lstm_prediction(csv_file, predict_until="2020-11-30"):
    dates, cases, deaths = data_analysis.analysis(csv_file, True)
    # create model
    model = Sequential()
    model.add(LSTM(50, activation="relu", input_shape=(3, 1)))
    model.add(Dense(1))
    model.compile(optimizer='adam', loss='mse')
    # fit model
    data, results = split_sequence(cases, 3)
    data = data.reshape((data.shape[0], data.shape[1], 1))
    model.fit(data, results, epochs=200, verbose=0)
    results = list(results)
    results.reverse()
    # predict data
    print("results", results)
    x = np.linspace(
        min(dates), data_analysis.matplotlib.dates.datestr2num(predict_until))
    print("len", len(x), len(np.linspace(max(dates), data_analysis.matplotlib.dates.datestr2num(predict_until))))
    for date in np.linspace(max(dates), data_analysis.matplotlib.dates.datestr2num(predict_until)):
        last_data = np.array(results[-3:]).astype(np.float32)
        last_data = last_data.reshape((1, 3, 1))
        prediction = model.predict(last_data, verbose=0)
        results.append(float(prediction))

    print(results)
    print(len(x), len(results))
    print(min(dates), max(dates))
    data_analysis.matplotlib.pyplot.plot(x, results)
    data_analysis.matplotlib.pyplot.show()


if __name__ == '__main__':
    lstm_prediction("./France_data.csv")  # prediction explodes, coherent
    lstm_prediction("./United_States_of_America_data.csv")
