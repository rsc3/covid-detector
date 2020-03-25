#covid-detector data structure
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt #basic plotting is good enough here

#load up the spreadsheet with genes
df = pd.read_excel("covid-detector/Human\ Transcription\ Factors.xlsx ")
