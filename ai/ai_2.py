import numpy as np
import pandas as pd
from sklearn.preprocessing import MinMaxScaler
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense

# Данные из таблицы
data = [80, 79, 85, 80, 75, 68, 65, 68, 65, 62]
data = np.array(data).reshape(-1, 1)

# Нормализация данных
scaler = MinMaxScaler(feature_range=(0, 1))
scaled_data = scaler.fit_transform(data)

# Подготовка данных для LSTM
def create_dataset(dataset, look_back=1):
    X, Y = [], []
    for i in range(len(dataset) - look_back - 1):
        a = dataset[i:(i + look_back), 0]
        X.append(a)
        Y.append(dataset[i + look_back, 0])
    return np.array(X), np.array(Y)

look_back = 3
X, Y = create_dataset(scaled_data, look_back)

# Изменение формы данных для LSTM [samples, time steps, features]
X = np.reshape(X, (X.shape[0], X.shape[1], 1))

# Создание модели LSTM
model = Sequential()
model.add(LSTM(50, return_sequences=True, input_shape=(look_back, 1)))
model.add(LSTM(50))
model.add(Dense(1))
model.compile(loss='mean_squared_error', optimizer='adam')

# Обучение модели
model.fit(X, Y, epochs=100, batch_size=1, verbose=2)

# Прогнозирование на 11-й месяц
last_data = scaled_data[-look_back:].reshape(1, look_back, 1)
predicted_value = model.predict(last_data)
predicted_value = scaler.inverse_transform(predicted_value)

print(f"Прогнозируемый объем продаж на 11-й месяц: {predicted_value[0][0]:.2f} млн руб.")
