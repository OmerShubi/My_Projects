//
// Created by Shubi & Eyal on 21/12/2019.
//

#include "Graph_Node.h"

/*
 * Graph Edge destructor is here to deal with forward declaration issues
 */
Graph_Edge::~Graph_Edge() {

    // 'Fill in' the gap
    Graph_Edge* prev_edge = this->_prev_edge;
    Graph_Edge* next_edge = this->_next_edge;

    if(prev_edge != NULL) {
        prev_edge->setNextEdge(next_edge);
    }
    else{ // Means this is the first edge in linked list
        if (!isReverseEdge()) {
            this->_source_node->_out_edges = next_edge;
        }
        else{
            this->_source_node->_reverse_edges = next_edge;
        }
    }

    if(next_edge != NULL) {// means not last
        next_edge->setPrevEdge(prev_edge);
    }

    // The original edge has ownership of deleting the reverse edge
    if(!isReverseEdge()){
        delete _reverse_edge;
    }
}