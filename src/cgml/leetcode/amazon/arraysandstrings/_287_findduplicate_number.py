import numpy as np

def generate_datapoint():
    N = np.random.randint(10,50)
    start = np.random.randint(0,N-2)
    count = np.random.randint(1,N-1-start)
    arr = np.arange(N,dtype=np.int32)+1
    duplicate = int(count/2+start)
    #print(start,start+count,duplicate)
    for idx in range(start,start+count):
        arr[idx]=duplicate
    np.random.shuffle(arr)
    return arr, duplicate, count

M = 50000

X = np.zeros((M,5))
Y = np.zeros((M))
for i in range(M):
    x, y, cnt = generate_datapoint()
    xfeat = np.array([len(x), sum(x), sum([i**2 for i in x]), sum([i**3 for i in x]), sum(i**4 for i in x)])
    X[i]=xfeat
    Y[i]=y

import pandas as pd
from keras.models import Sequential
from keras.layers import Dense
from keras.wrappers.scikit_learn import KerasRegressor
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import KFold
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline

def baseline_model():
    model = Sequential()
    model.add(Dense(50, input_dim=5, kernel_initializer='normal', activation='sigmoid'))
    model.add(Dense(1, kernel_initializer='normal'))
    model.compile(loss='mean_squared_error', optimizer='adam')
    return model

# fix random seed for reproducibility
seed = 7
np.random.seed(seed)
# evaluate model with standardized dataset
estimator = KerasRegressor(build_fn=baseline_model, epochs=100, batch_size=200, verbose=0)

estimator.fit(X,Y)
#estimator.predict()
# kfold = KFold(n_splits=2, random_state=seed)
# results = cross_val_score(estimator, X, Y, cv=kfold)
#print("Results: %.2f (%.2f) MSE" % (results.mean(), results.std()))

import keras

predicted = estimator.predict(X)
for k in range(len(X)):
    print("Target: {}, Predicted: {}".format(Y[k],predicted[k]))

# estimator.model.save_weights()

# class Solution:
#     def findDuplicate(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: int
#         """
# print(sum([1,2,3,4,5,6,6]))
# print(sum(range(1,8)))
# print(sum([x**2 for x in [1,2,3,4,5,6,6]]))
# print(sum([x**2 for x in range(1,9)]))