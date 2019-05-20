from FKT import *
import networkx as nx #Requires at least networkx 2.3+
import matplotlib.pyplot as plt
import random
import math
import numpy as np
import time
from uniform_matching import *


start_time=time.time()
g = nx.grid_graph([4,4])

num_matchings = round(FKT(nx.adjacency_matrix(g).todense()))

sample_matchings = [uniform_matching(g) for x in range(5000)]

sorted_matchings = []

for k in range(5000):

    sorted_matchings.append(tuple(sorted(tuple([tuple(sorted(x)) for x in sample_matchings[k]]))))
    
    

counts = [sorted_matchings.count(j) for j in list(set(sorted_matchings))]



print(counts)

print(time.time()-start_time,"seconds")


plt.bar(range(len(counts)),counts)

#[157, 138, 169, 125, 158, 148, 135, 133, 117, 131, 131, 149, 127, 127, 136, 147, 131, 118, 143, 142, 146, 145, 134, 159, 137, 125, 149, 140, 152, 120, 126, 142, 145, 134, 140, 144] #from 5000 samples

plt.show()
