from tensorflow.keras import models
import numpy as np
import datetime

model = models.load_model('germany_prediction_04_april.h5')

# germany's last 3 days case
# 2nd april 84794
# 3rd april 91159
# 4th april 96092


date = datetime.datetime(2020,4,5)
result = dict()
x = np.array([84794, 91159, 96092])
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




