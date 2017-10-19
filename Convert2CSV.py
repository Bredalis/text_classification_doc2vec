# loading libraries
import pandas as pd
import numpy as np

#path to the dataset
test = "/Users/apple/Desktop/research/datasets/20ng.txt"


# define column names
names = ['class', 'text']

# loading training data (File Name : 'test.txt')
df = pd.read_csv(test, header=None, names=names, delimiter = "\t")

# define column names
names1 = []

for i in range(0,300):
    names1.append("x" + str(i+1))

# loading training data
df1 = pd.read_csv('20ngVectors.txt', header=None, names=names1, delimiter = ",")

classLabels = np.array(df['class'])

#adding class labels in vectors data frame
df1.loc[:, 'className'] = classLabels

#saving dataframe in csv 
df1.to_csv('20ngVectors.csv', index=False)