# loading libraries
import pandas as pd
import numpy as np
import os
import sys
import nltk
import codecs
import gensim

#path of pre-trained model
model = "doc2vec.bin"
start_alpha=0.01
infer_epoch=1000

m = gensim.models.Doc2Vec.load(model)

test_docs = [ x.strip().split() for x in codecs.open( 'mini20Text.txt', "r", "utf-8").readlines() ]

#infer test vectors
output = open("mini20TextVectors.txt", "w")
for d in test_docs:
    output.write( ",".join([str(x) for x in m.infer_vector(d , alpha=start_alpha, steps=infer_epoch)]) + "\n" )
output.flush()
output.close()