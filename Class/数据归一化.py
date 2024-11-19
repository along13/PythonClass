from sklearn.preprocessing import MinMaxScaler
import numpy as np

code = np.array([[10,-5.5,3],[7,-1.2,6],[12,0,9]])
scaler = MinMaxScaler()
x_scale = scaler.fit_transform(code)

print('Scaled Data:')
print(x_scale)