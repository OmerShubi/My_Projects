//
// Created by Shubi & Eyal on 21/12/2019.
//

#ifndef DALGO_GRAPH_NODE_H
#define DALGO_GRAPH_NODE_H

#include <cstddef>
#include "Graph_Edge.h"

#define ZERO 0

/*
 * Each instance represents a graph node
 */


class Graph_Node {
public:
    /*
     * Constructor
     *
     */
    Graph_Node(unsigned int key,
               Graph_Node *prevNode,
               Graph_Node *nextNode):
                    _key(key), _prev_node(prevNode),
                    _next_node(nextNode), _num_of_incoming_edges(ZERO), _num_of_outgoing_edges(ZERO),
                    _out_edges(NULL), _reverse_edges(NULL)
                    {}

     ~Graph_Node(){

    }

    /*
     * Returns the number of edges going into this node
     */
    unsigned Get_out_Degree() const {

        return this->_num_of_outgoing_edges;
    }

    /*
     * Returns the number of edges going out from this node
     */
    unsigned Get_in_Degree() const {

        return this->_num_of_incoming_edges;
    }

    /*
     * Returns the Key of this node
     */
    unsigned Get_key() const{
        return _key;
    }

    /*
     * Previous Node Getter
     */
    Graph_Node *getPrevNode() const {
        return _prev_node;
    }

    /*
     * Previous Node Setter
     */
    void setPrevNode(Graph_Node *prevNode) {
        _prev_node = prevNode;
    }

    /*
     * Next Node Getter
     */
    Graph_Node *getNextNode() const {
        return _next_node;
    }

    /*
     * Next Node Setter
     */
    void setNextNode(Graph_Node *nextNode) {
        _next_node = nextNode;
    }

    /*
     * Returns true if node has any incoming or outgoing edges
     * False otherwise
     */
    bool has_incoming_outgoing_edges(){
        return (_num_of_outgoing_edges != 0) || (_num_of_incoming_edges != 0);
    }

    /*
     * Adds an edge-(this node, target)-'new_first_edge'
     * to linked list maintained by the node
     * Adds it at the beginning to comply with requirements
     */
    void add_edge_to_edges(Graph_Edge* new_first_edge, bool is_reverse) {

        Graph_Edge* edge_list = NULL;

        if(is_reverse){
            edge_list = _reverse_edges;
        }else{
            edge_list = _out_edges;
        }

        Graph_Edge* current_first_edge = edge_list;
        new_first_edge->setNextEdge(current_first_edge);

        if(current_first_edge != NULL) {
            current_first_edge->setPrevEdge(new_first_edge);
        }

        if(is_reverse){
            _reverse_edges = new_first_edge;
        }else{
             _out_edges = new_first_edge;
        }
    }

    /*
     * Color Getter
     */
    unsigned int getColor() const {
        return _color;
    }

    /*
     * Color Setter
     */
    void setColor(unsigned int color) {
        _color = color;
    }

    /*
     * Distance Getter
     */
    unsigned int getDistance() const {
        return _distance;
    }

    /*
     * Distance Setter
     */
    void setDistance(unsigned int distance) {
        _distance = distance;
    }

    unsigned _key; // Unique id of the node

    // for storing graph implementation data structure
    Graph_Node* _prev_node;
    Graph_Node* _next_node;

    unsigned _num_of_incoming_edges;
    unsigned _num_of_outgoing_edges;

    // Pointer to first edge in adjacency list of outgoing edges from the node
    Graph_Edge* _out_edges;

    // Pointer to first edge in adjacency list of incoming edges to the node
    Graph_Edge* _reverse_edges;

    // Attributes for BFS & DFS Algorithms
    unsigned _color; // the discovery status

    // Attributes for BFS Algorithm
    unsigned _distance; // the distance from source to this node in G
};

#endif //DALGO_GRAPH_NODE_H
