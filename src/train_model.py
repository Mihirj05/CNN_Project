from tensorflow import keras
import tensorflow as tf
import numpy as np
import pandas as pd 
from datetime import datetime
import matplotlib.pyplot as plt
import os

os.makedirs("logs", exist_ok =True)

print (f"load minst dataset")
(X_train , y_train), (X_test, y_test) = keras.datasets.minst.load_data()

# normalizing of the data

X_train = X_train.astype("float32")/255.0
X_test = X_test.astype("float32")/255.0

#reshping of data to cnn
X_train = X_train.reshape(-1,28,28,3)
X_test = X_test.reshape(-1,28,28,1)

