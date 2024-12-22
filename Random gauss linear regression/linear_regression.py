#!/usr/bin/env python
#-*- coding: utf-8 -*-
# Python 3.7

#
# @Author: *
# @License: *
# @Date: *
# @Version: *
# @Purpose: linear regresssion with scikit-learn. 
#           Data used is random.gauss 
#

from sklearn import linear_model

import matplotlib.pyplot as plt
import numpy as np
import random

random.seed(0)
fig, ax = plt.subplots(figsize=(5, 5))
plt.grid(True, linestyle='--', linewidth=0.1, alpha=0.7)

#----------------------------------------------------------------------------------------#
# Step 1: training data
X = [i for i in range(100)]
Y = [random.gauss(x,10) for x in X]

X = np.asarray(X)[:,np.newaxis]
Y = np.asarray(Y)[:,np.newaxis]

plt.scatter(X,Y)

# #----------------------------------------------------------------------------------------#
# # Step 2: define and train a model

model = linear_model.LinearRegression()
model.fit(X, Y)

# print(model.score(X, Y))               # R²
# print(model.coef_, model.intercept_)   # 

# #----------------------------------------------------------------------------------------#
# # Step 3: prediction
plt.plot(X, model.predict(X), color='black', linewidth=3, label="y = " + str(round(model.coef_[0][0], 2)) + "x + " + str(round(model.intercept_[0], 2)) + ", R²=" + str(round(model.score(X, Y), 2)))


plt.xlabel('x')
plt.ylabel('y')
plt.legend(loc="best")
plt.savefig("simple_linear_regression.svg", bbox_inches='tight')
# plt.savefig("simple_linear_regression.pdf", bbox_inches='tight')