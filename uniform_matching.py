# -*- coding: utf-8 -*-
"""
Created on Sun May 19 21:36:51 2019

@author: daryl
"""

from FKT import *
import networkx as nx #Requires at least networkx 2.3+
import matplotlib.pyplot as plt
import random
import math
import numpy as np
import time


        
def select_edge(H,slow=True):
    
    #print("new call")
    
    G2=H.copy()
    
    ccs = list((G2.subgraph(c) for c in nx.connected_components(G2)))
    
    #print(len(ccs))

    edges=[]

    for cc in ccs:
        
        
        G=cc.copy()
        
        
        #match_all = FKT((nx.adjacency_matrix(G)).todense())
        
        #print("did all")
        
        probs = [0]
        
        adds = []
        
        elist = list(G.edges())
        #print(len(elist))
        
        temp=0
        rsum=0
        for edge in elist:
            #G.remove_edge(edge[0],edge[1])
            G.remove_nodes_from([edge[0],edge[1]])
            C=list((G.subgraph(c) for c in nx.connected_components(G)))
            
            compprod = 1
            for comp in C:
                if len(list(comp.nodes())) %2 == 1:
                    compprod = 0
                    #break
                else:
                    compprod = compprod * round(FKT((nx.adjacency_matrix(comp)).todense()))#FKT((nx.adjacency_matrix(comp)).todense())
            
            rsum += compprod
            
            #print(edge,compprod)
    
            for i in range(compprod):
                adds.append(edge)
            #print(adds)
            #probs.append(probs[-1]+compprod/match_all)
            probs.append(probs[-1]+compprod)
            #G.add_edge(edge[0],edge[1])
            G=cc.copy()
            #print(edge)
            temp+=1
            #print(temp)
        #avlsdkn   
        #if adds:
            #toremove = random.choice(adds)
            #print(toremove)
        
        #edges.append(toremove)
        edges.append(random.choice(adds))
        
    return edges
        
    probs.pop(0)
    print(probs)
    
    #r = random.random()
    r = random.randint(0,rsum)
    print(r)
    
    for x in range(len(elist)):
        if probs[x]>r:
            
            return elist[x]
        
    
    return random.choice(elist)
       

def uniform_matching(H):
    
    g=H.copy()
    
    nlist = list(g.nodes())
    
    mlist=[]
    
    if len(nlist)%2 ==1:
        return []
    
    while len(nlist)>0:
                
        edges = select_edge(g)
        
        for edge in edges:
        
            mlist.append(edge)
        
            nlist.remove(edge[0])
            nlist.remove(edge[1])
        
            g.remove_node(edge[0])
            g.remove_node(edge[1])
        
        
        
            #plt.figure()
            #nx.draw(g)
        
    
    return mlist
