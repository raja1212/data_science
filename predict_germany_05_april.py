from tensorflow.keras import models
import numpy as np
import datetime

model = models.load_model('model/germany_prediction_05_april.h5')

# germany's last 3 days case
# 3rd april 91159
# 4th april 96092
# 5th april 100123


date = datetime.datetime(2020,4,6)
result = dict()
x = np.array([91159, 96092, 100123], dtype=np.float32)
for i in range(25):
    date += datetime.timedelta(days=1)
    x = x[-3:]
    x = x.reshape([1, 3, 1])
    print(x)
    value = int(model.predict(x)[0][0])
    print(value)
    result[date.strftime("%d.%m.%Y")] = value
    x = np.append(x, value)


with open('prediction.csv', 'w') as f:
    for key, value in result.items():
        f.write(f"{key}, {value}\n")




