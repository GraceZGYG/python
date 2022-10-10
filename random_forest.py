import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier, RandomForestRegressor
from time import *

test_df = pd.read_csv("t1000.csv")

def evaluate(path, model_name, num_trees=500, depth=30, num_jobs=1):
    df = pd.read_csv(path)
    y = df.values[:,0]
    x = df.values[:,1:]

    test_y = test_df.values[:,0]
    test_x = test_df.values[:,1:]

    rf = RandomForestClassifier(n_estimators=num_trees, max_depth=depth, n_jobs=num_jobs)
    start = time()
    rf.fit(x, y)
    end = time()
    elapsed = end - start
    print("Time to train model %s: %.9f seconds" % (model_name, elapsed))

    acc = np.mean(test_y == rf.predict(test_x))
    print("Model %s accuracy: %.3f" % (model_name, acc))

evaluate("t10k.csv", "10k", 500, 10, 48)    # choose your own parameter

