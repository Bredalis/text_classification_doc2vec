import nltk
import string
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer

stemmer = PorterStemmer() #problem from HERE

inputPath = 'yelp_review_polarityText.txt'
outputPath = 'yelp_review_polarity_steemed.txt'

with open(inputPath,'r') as inFile, open(outputPath,'w') as outFile:
  	for line in inFile.readlines():
  	    print(" ".join([stemmer.stem(word) for word in line.lower().translate(str.maketrans('', '', string.punctuation)).split() 
          	if word not in stopwords.words('english')]), file=outFile)