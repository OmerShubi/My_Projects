//
// Created by Shubi & Eyal on 21/12/2019.
//

#ifndef DALGO_GRAPH_EDGE_H
#define DALGO_GRAPH_EDGE_H

#include <cstddef>

class Graph_Node;

/*
 * Each object in the class Graph_Edge
 * Represents an edge-(source,target) in the graph,
 * stored as doubly linked list,
 * Owner of the corresponding reverse edge (target, source) used for the transpose graph
 */
class Graph_Edge {
public:
    /*
     * Constructor
     */
    Graph_Edge(Graph_Node* from, Graph_Node* to):
                _prev_edge(NULL), _next_edge(NULL),
                _source_node(from), _target_node(to), _reverse_edge(NULL){}

    /*
    * Graph Edge destructor is in Graph_Node.cpp to deal with forward declaration issues
    */
    ~Graph_Edge();

    /*
     * Previous Edge Getter
     */
    Graph_Edge *getPrevEdge() const {
        return _prev_edge;
    }

    /*
     * Previous Edge Setter
     */
    void setPrevEdge(Graph_Edge *prevEdge) {
        _prev_edge = prevEdge;
    }

    /*
     * Next Edge Getter
     */
    Graph_Edge *getNextEdge() const {
        return _next_edge;
    }

    /*
     * Next Edge Setter
     */
    void setNextEdge(Graph_Edge *nextEdge) {
        _next_edge = nextEdge;
    }

    bool isReverseEdge() const{
        return _reverse_edge == NULL;
    }

//private:

    // In linked list
    Graph_Edge* _prev_edge;
    Graph_Edge* _next_edge;

    // The source and target nodes of the edge in the graph
    Graph_Node* _source_node;
    Graph_Node* _target_node;

    Graph_Edge* _reverse_edge; // the corresponding reverse edge
    // if this is null then it means it is the reverse edge.

};




#endif //DALGO_GRAPH_EDGE_H
