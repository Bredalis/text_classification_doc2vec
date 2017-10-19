# loading libraries
import pandas as pd
import numpy as np


#path to the dataset
test = 'C:\\research\\data_sets\\sogou_news\\sogou_news.csv'

# define column names
names = ['classLabel', 'title', 'desc'] #Used when have 3 column

# names = ['classLabel', 'desc'] #Used when have 3 column

# loading training data
df = pd.read_csv( test, header=None, names=names, delimiter = ",")

sentence = np.array(df.desc)
classLabels = np.array(df.classLabel)

#textFile contains text(Document)
textFile = open('sogou_newsText.txt','wb')
classLabelFile = open('sogou_newsClassLabel.txt', 'wb')

#saved in textFile.txt
np.savetxt(textFile, sentence, delimiter=" ", fmt="%s")
textFile.close()
np.savetxt(classLabelFile, classLabels, delimiter=" ", fmt="%s")
classLabelFile.close()
