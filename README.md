# FKT_Perfect_Matchings

This repo provides a Python implementation of the FKT algorithm for perfect matching enumeration based on the <a href="http://numberworld.blogspot.com/2014/03/an-implementation-of-fkt-algorithm.html">Sage version</a> created by Dr. Christian Schridde. The implementation relies on the <a href="https://networkx.github.io/documentation/stable/_modules/networkx/algorithms/planarity.html">planar graph features</a> added in networkx version 2.3. This was used by <a href="https://mggg.org">MGGG</a> to analyze pairings of State House districts to make State Senate districts in <a href="https://github.com/gerrymandr/Alaska>Alaska</a>. 
  
FKT constructs a (+1, -1) weighting of the adjacency matrix of a graph so that the number of perfect matchings is equal to the squareroot of the determinant of the signed matrix. 
