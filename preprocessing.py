import nltk
import string
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer

# Initialize the Porter Stemmer
stemmer = PorterStemmer()  # Initializing the stemmer for word stemming

# Define file paths for input and output
inputPath = 'yelp_review_polarityText.txt'  # Path to the input text file
outputPath = 'yelp_review_polarity_steemed.txt'  # Path to the output text file after stemming

# Open the input file for reading and the output file for writing
with open(inputPath, 'r') as inFile, open(outputPath, 'w') as outFile:
    # Iterate through each line in the input file
    for line in inFile.readlines():
        # Preprocess the text:
        # 1. Convert the text to lowercase
        # 2. Remove punctuation
        # 3. Tokenize the text into words
        # 4. Remove English stopwords
        # 5. Perform stemming on the remaining words
        processed_words = [
            stemmer.stem(word)  # Perform stemming on each word
            for word in line.lower().translate(str.maketrans('', '', string.punctuation)).split()
            if word not in stopwords.words('english')  # Filter out stopwords
        ]
        
        # Write the preprocessed and stemmed words to the output file
        print(" ".join(processed_words), file=outFile)  # Write the stemmed words to the output file
