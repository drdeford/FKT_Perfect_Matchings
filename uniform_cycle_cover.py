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


def select_edge_clean(H,slow=True):

    G2=H.copy()
    
    ccs = list((G2.subgraph(c) for c in nx.connected_components(G2)))
    
    edges=[]
    adds2 = [[None,0]]
    rsum=0    
    for cc in ccs:
        
        
        G=cc.copy()
        
        
        if len(list(G.nodes())) == 1:
           break
        
        match_all = FKT((nx.adjacency_matrix(G)).todense())
        
        if match_all == 0:
            break
    
        elist = list(G.edges())

        
        temp=0

        for edge in elist:

            G.remove_nodes_from([edge[0],edge[1]])

            C=[G.subgraph(c) for c in nx.connected_components(G)]
            
           
            
            compprod = 1
            for comp in C:
                
                if len(list(comp.nodes())) %2 == 1:
                    compprod = 0

                else:
                    compprod = compprod * round(FKT((nx.adjacency_matrix(comp)).todense()))
                    
            if not C:
                rsum+= match_all
                adds2.append([edge,rsum])
                
            elif compprod > 0:
                rsum += compprod
                adds2.append([edge,rsum])          
                
                
            G=cc.copy()

    r = random.randint(1,rsum)


    
    for x in range(len(adds2)-1):
        if int(adds2[x+1][1])>=r and int(adds2[x][1]) < r:

            return adds2[x+1][0]
                          

        
def select_edge(H,slow=True):
    
    #print("new call")
    
    G2=H.copy()
    
    ccs = list((G2.subgraph(c) for c in nx.connected_components(G2)))
    
    #print(len(ccs))

    edges=[]
    adds2 = [[None,0]]
    rsum=0    
    for cc in ccs:
        
        
        G=cc.copy()
        
        
        if len(list(G.nodes())) == 1:
           break
        
        match_all = FKT((nx.adjacency_matrix(G)).todense())
        
        if match_all == 0:
            break
        
        #print("did all")
        

        

        
        elist = list(G.edges())
        #print(len(elist))
        
        temp=0

        for edge in elist:
            #G.remove_edge(edge[0],edge[1])
            G.remove_nodes_from([edge[0],edge[1]])
            #print("edge",edge)
            C=[G.subgraph(c) for c in nx.connected_components(G)]
            
           
            
            compprod = 1
            for comp in C:
                
                if len(list(comp.nodes())) %2 == 1:
                    compprod = 0
                    #break
                else:
                    compprod = compprod * round(FKT((nx.adjacency_matrix(comp)).todense()))#FKT((nx.adjacency_matrix(comp)).todense())
                    
                   
            #if compprod == match_all:
            #    #edges.append(edge)
            #    rsum += compprod
            #    
            #    adds2.append([edge,rsum])
            #    
            #else:
            #
            #
            #   rsum += compprod
                
            #    adds2.append([edge,rsum])
            
            if not C:
                rsum+= match_all
                adds2.append([edge,rsum])
                
            elif compprod > 0:
                rsum += compprod
                adds2.append([edge,rsum])
            
            #print(edge,compprod)
    
                #for i in range(compprod):
                #    adds.append(edge)
                
            
            
            #print(adds)
            #probs.append(probs[-1]+compprod/match_all)
            #probs.append(probs[-1]+compprod)
            #G.add_edge(edge[0],edge[1])
            G=cc.copy()
    #print(adds2)            
    r = random.randint(1,rsum)

    #print("r",r)
    
    for x in range(len(adds2)-1):
        if int(adds2[x+1][1])>=r and int(adds2[x][1]) < r:
            #print(adds2[x+1])
            return adds2[x+1][0]
            #edges.append(adds2[x+1][0])
            #print(edge)
            #temp+=1
            #print(temp)
        #avlsdkn   
        #if adds:
            #toremove = random.choice(adds)
            #print(toremove)
        
        #edges.append(toremove)
        #edges.append(random.choice(adds))
    #print(edges)
        
    #return edges

"""        
    probs.pop(0)
    print(probs)
    
    #r = random.random()
    r = random.randint(0,rsum)
    print(r)
    
    for x in range(len(elist)):
        if probs[x]>r:
            
            return elist[x]
        
    
    return random.choice(elist)
"""       


def select_edge_leaves(H,slow=True):
    
    #print("new call")
    
    G2=H.copy()
    
    ccs = list((G2.subgraph(c) for c in nx.connected_components(G2)))
    
    #print(len(ccs))

    edges=[]
    adds2 = [[None,0]]
    rsum=0    
    for cc in ccs:
        
        
        G=cc.copy()
        
        
        if len(list(G.nodes())) == 1:
           break
        
        #match_all = FKT((nx.adjacency_matrix(G)).todense())
        
        #if match_all == 0:
        #    break
        
        #print("did all")
        

        

        
        elist = list(G.edges())
        #print(len(elist))
        
        temp=0

        for edge in elist:
            #G.remove_edge(edge[0],edge[1])
            G.remove_nodes_from([edge[0],edge[1]])
            #print("edge",edge)
            C=[G.subgraph(c) for c in nx.connected_components(G)]
            
           
            
            compprod = 1
            for comp in C:
                
                if len(list(comp.nodes())) %2 == 1:
                    compprod = 0
                    break
                else:
                    compprod = compprod * FKT((nx.adjacency_matrix(comp)).todense())
                    
                   
            #if compprod == match_all:
            #    #edges.append(edge)
            #    rsum += compprod
            #    
            #    adds2.append([edge,rsum])
            #    
            #else:
            #
            #
            #   rsum += compprod
                
            #    adds2.append([edge,rsum])
            
            if not C:
                #rsum+= match_all
                #adds2.append([edge,rsum])
                return(edge)
                
            #elif compprod == match_all:
            #    return(edge)
                
            elif compprod > 0:
                rsum += compprod
                adds2.append([edge,rsum])
            
            #print(edge,compprod)
    
                #for i in range(compprod):
                #    adds.append(edge)
                
            
            
            #print(adds)
            #probs.append(probs[-1]+compprod/match_all)
            #probs.append(probs[-1]+compprod)
            #G.add_edge(edge[0],edge[1])
            G=cc.copy()
    #print(adds2)            
    r = random.randint(1,math.ceil(rsum))
    #r=random.random()*rsum + 1

    #print("r",r)
    
    for x in range(len(adds2)-1):
        if adds2[x+1][1]>=r and adds2[x][1] < r:
            #print(adds2[x+1])
            return adds2[x+1][0]
     



def uniform_matching(H):
    
    g=H.copy()
    
    nlist = list(g.nodes())
    
    mlist=[]
    
    if len(nlist)%2 ==1:
        return []
    
    while len(nlist)>0:
                
        edge = select_edge(g)
        
        #for edge in edges:
        
        mlist.append(edge)
    
        #if edge[0] in nlist:
        nlist.remove(edge[0])
        g.remove_node(edge[0])
        #if edge[1] in nlist:
        
        nlist.remove(edge[1])


        g.remove_node(edge[1])
                
        
        
        
        #plt.figure()
        #nx.draw(H,pos={x:x for x in H.nodes()},node_color=['r' for x in H.nodes()])
        #nx.draw(g,pos={x:x for x in g.nodes()})
        #plt.show()
        
    
    return mlist
    
def uniform_cycle_cover(H, two_cycles = False):
    
    attempt = 1
    
    while 0 != 1:
        g = H.copy()
        
        dcmap = {0:'lightgray',1:'k'}
        
        ncolors = {x:dcmap[(x[0]+x[1])%2] for x in g.nodes()}
        
        m1 = uniform_matching(g)
        #print(m1)
        ec = {x:0 for x in g.edges()}
        for edge in g.edges():
            #print(edge)
            if edge in m1 or (edge[1],edge[0]) in m1:
                
                ec[edge] = 'r'
                ec[(edge[1],edge[0])] = 'r'
            else:
                ec[edge]= 'b'
                ec[(edge[1],edge[0])] = 'b'
          
            
        plt.figure()
        nx.draw(g,pos = {x:x for x in g.nodes()}, edge_color = ['b' for x in H.edges()], node_color = [ncolors[x] for x in H.nodes()],width = 4)
        plt.show()
        
        plt.figure()
        nx.draw(g,pos = {x:x for x in g.nodes()}, edge_color = [ec[x] for x in H.edges()], node_color = [ncolors[x] for x in H.nodes()],width = 4)
        plt.show()
        
        D = nx.DiGraph()
        
        for x in m1:
            if (x[0][0]+x[0][1])%2 == 0:
                D.add_edge(x[0],x[1])
            else:
                D.add_edge(x[1],x[0])
                
                
        plt.figure()
        nx.draw(D,pos = {x:x for x in g.nodes()},node_color = [ncolors[x] for x in g.nodes()])
        plt.show()
                
        g= H.copy()
                
        if two_cycles == False:
                
            g.remove_edges_from(m1)
        
        m2 = uniform_matching(g)
        
        ec = {x:0 for x in g.edges()}
        for edge in g.edges():
            if edge in m2 or (edge[1],edge[0]) in m2:
                
                ec[edge] = 'r'
                ec[(edge[1],edge[0])] = 'r'
            else:
                ec[edge]= 'b'
                ec[(edge[1],edge[0])] = 'b'
                
                

        plt.figure()
        nx.draw(g,pos = {x:x for x in g.nodes()}, edge_color = ['b' for x in g.edges()], node_color = [ncolors[x] for x in H.nodes()],width = 4)
        plt.show()
        
        plt.figure()
        #for edge in g.edges():
        #    plt.plot([edge[0][0],edge[1][0]],[edge[0][1],edge[1][1]],linewidth=5,color= ec[edge])

        nx.draw(g,pos = {x:x for x in g.nodes()}, edge_color = [ec[x] for x in g.edges()],node_color = [ncolors[x] for x in H.nodes()],width = 4)
        plt.show()
    
        
        for x in m2:
            if (x[0][0]+x[0][1])%2 == 1:
                D.add_edge(x[0],x[1])
            else:
                D.add_edge(x[1],x[0])
                
                
        if 2 not in [len(x) for x in nx.strongly_connected_components(D)]:
            
            return [D, attempt]
        
        else:
            attempt += 1
            if attempt % 10 == 1:
                print(attempt)
            
    
    #return D
    
    

lens = []

#for i in range(100):
    
#    dg = uniform_cycle_cover(nx.grid_graph([4,4]), two_cycles = True)
#    lens.append(dg[1])
    

dg = uniform_cycle_cover(nx.grid_graph([10,10]), two_cycles = False)

dcmap = {0:'lightgray',1:'k'}
        
ncolors = {x:dcmap[(x[0]+x[1])%2] for x in dg[0].nodes()}
#print(dg[1])
plt.figure()
nx.draw(dg[0], pos = {x:x for x in dg[0].nodes()},node_color = [ncolors[x] for x in dg[0].nodes()])
plt.show()
