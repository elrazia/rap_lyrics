import pandas as pd
import numpy as np
from datetime import datetime
import os
import pickle

with open('grand_frame.pkl', 'rb') as readfile:
    grand_frame = pickle.load(readfile)

with open('tfidf.pkl', 'rb') as readfile:
    tfidf = pickle.load(readfile)

print tfidf.shape
