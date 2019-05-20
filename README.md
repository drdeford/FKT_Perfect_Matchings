# FKT_Perfect_Matchings

This repo provides a Python implementation of the FKT algorithm for perfect matching enumeration based on the <a href="http://numberworld.blogspot.com/2014/03/an-implementation-of-fkt-algorithm.html">Sage version</a> created by Dr. Christian Schridde. The implementation relies on the <a href="https://networkx.github.io/documentation/stable/_modules/networkx/algorithms/planarity.html">planar graph features</a> added in networkx version 2.3. This was used by <a href="https://mggg.org">MGGG</a> to analyze pairings of State House districts to make State Senate districts in <a href="https://github.com/gerrymandr/Alaska">Alaska</a>. 
  
FKT constructs a (+1, -1) weighting of the edges of a planar graph (explicitly making use of a planar embedding) so that the number of perfect matchings is equal to the squareroot of the determinant of the signed matrix. This means that the number of perfect matchings for planar graphs can be computed in polynomial time, which is a little surprising since computing this is #P-complete for arbitrary graphs. 

Having access to quick enumerations also allows us to sample uniformly from the set of perfect matchings of a planar graph as outlined in <a href="https://www.sciencedirect.com/science/article/pii/030439758690174X">this paper</a> of Jerrum, Valiant, and Vazirani.
