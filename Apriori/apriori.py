# Installing Package
import subprocess
import sys

subprocess.call([sys.executable, '-m', 'pip', 'install', 'apyori'])

# Importing Libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from apyori import apriori

# Data Preprocessing
dataset = pd.read_csv('Market_Basket_Optimisation.csv', header = None)
transactions = []
for i in range(0, 7501):
    transactions.append([str(dataset.values[i, j]) for j in range(0, 20)])


# Train the Apriori model on the dataset
rules = apriori(transactions = transactions, min_support = 0.003, min_confidence = 0.2, min_lift = 3, min_length = 2, max_length = 2)

# Visualization of result
results = list(rules)
print(results)

# Put the result well organised into a Pandas DataFrame
def inspect(results):
    lhs = [tuple(result[2][0][0])[0] for result in results]
    rhs = [tuple(result[2][0][1])[0] for result in results]
    supports = [result[1] for result in results]
    confidences = [result[2][0][2] for result in results]
    lifts = [result[2][0][3] for result in results]
    return list(zip(lhs, rhs, supports, confidences, lifts))
resultsinDataFrame = pd.DataFrame(inspect(results), columns = ['Left Hand Side', 'Right Hand Side', 'Support', 'Confidence', 'Lift'])

print("\nNon Sorted Result: ")
print(resultsinDataFrame)

print("\nSorted Result:")
print(resultsinDataFrame.nlargest(n = 10, columns = 'Lift'))