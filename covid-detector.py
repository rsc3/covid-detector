#covid-detector data structure
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt #basic plotting is good enough here

#load up the spreadsheet with genes
#df = pd.read_excel("covid-detector/Human\ Transcription\ Factors.xlsx ")

from itertools import groupby

def fasta_iter(fasta_name):
    """
    given a fasta file. yield tuples of header, sequence
    """
    fh = open(fasta_name)
    # ditch the boolean (x[0]) and just keep the header or sequence since
    # we know they alternate.
    faiter = (x[1] for x in groupby(fh, lambda line: line[0] == ">"))
    for header in faiter:
        # drop the ">"
        header = header.next()[1:].strip()
        # join all sequence lines to one.
        seq = "".join(s.strip() for s in faiter.next())
        yield header, seq

data = []   
data2 = [] 
from Bio import SearchIO
for qresult in SearchIO.parse('human_tf_domains.txt', 'hmmscan3-domtab'):
    data.append(qresult)
    #print(qresult[0][0])
    
# for qresult2 in SearchIO.parse('human_tf_table.txt', 'hmmer3-tab'):
#     data2.append(qresult2)
    
#find the c2h2-zf transcription factors
c2h2=[]
zz = []
h2c2=[]
for result in data:
    for i in range(len(result)):
        for j in range(len(result[i])):
            for k in range(len(result[i][j])):
                id = result[i].id
                if id == 'zf-A20':
                    print(1)