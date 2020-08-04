//
// Created by Shubi & Eyal on 21/12/2019.
//

#ifndef DALGO_DYNAMIC_GRAPH_H
#define DALGO_DYNAMIC_GRAPH_H

#include <cstddef>

#include "Graph_Node.h"
#include "Graph_Edge.h"
#include "Rooted_Tree.h"
#include "Queue.h"

//Colors for BFS & DFS
#define WHITE 0 // v is still undiscovered
#define GRAY 1 // v has been discovered but it still has unexplored incident edges
#define BLACK 2 // v has been discovered and all its incident edges have been explored

#define INF -1 // Represents infinity
#define ZERO 0

/*
 * Dynamic Graph Implementation as per the requirements
 *
 * Support edge and node insertion and deletion, BFS, SCC, and DFS(for SCC)
 */
class Dynamic_Graph {
public:

    /*
     * Default Constructor
     *
     * Creates an empty graph without any nodes and/or edges
     */
    Dynamic_Graph():_nodes(NULL), _num_of_edges_in_graph(ZERO),
                    _num_of_nodes_in_graph(ZERO){

                    }

    /*
     * Destructor
     *
     * Deletes the graph and any data stored in it
     */
    ~Dynamic_Graph() {

        Graph_Node* current_node = this->_nodes;

        while(current_node != NULL){
            Graph_Node* next_node = current_node->getNextNode();


            // delete outgoing edges
            Graph_Edge* out_edge = current_node->_out_edges;

            while(out_edge != NULL){

                Graph_Edge* next_out_edge = out_edge->getNextEdge();
                delete out_edge;
                out_edge = next_out_edge;
            }
            current_node = next_node;
        }

        current_node = this->_nodes;

        while(current_node != NULL){
            Graph_Node* next_node = current_node->getNextNode();
            delete current_node;

            current_node = next_node;
        }
        this->_nodes = NULL;
    }

    /*
     * Adds a node to the graph with key 'node_key'
     *
     * Adds the node without any edges
     */
    Graph_Node* Insert_Node(unsigned node_key);

    /*
     * Deletes the given 'node'
     *
     * If nodes has incoming or outgoing edges - does nothing
     */
    void Delete_Node(Graph_Node* node);

    /*
     * Adds an edge from 'from' to 'to' to the graph
     */
    Graph_Edge* Insert_Edge(Graph_Node* from, Graph_Node* to);

    /*
     * Deletes the given 'edge' from the graph
     */
    void Delete_Edge(Graph_Edge* edge);

    /*
     * Identifies all Strongly Connected Components (SCC) in the graph
     *
     * The root of the returned Rooted_Tree is a virtual node with key=0.
     * Each child of the root is a SCC rooted at the same child.
     */
    Rooted_Tree* SCC() const;

    /*
     * Returns a BFS Tree - tree of shortest distances from node 'source'
     */
    Rooted_Tree* BFS(Graph_Node* source) const;


    /*
     * Initialization for BFS algorithm according to learnt in class
     *
     */
    void BFS_Initialization(Graph_Node *source) const;


    /*
     * DFS Algorithm according to learnt in class
     * do_reverse flag is used for determining if first(regular) or second(transpose graph) run of dfs in scc algorithm
     */
    Rooted_Tree *DFS(Queue<Graph_Node*, Tree_Node*>* node_queue, bool do_reverse) const;

    /*
     * DFS Visit is the assistant function for DFS as learnt in class
     */
    void DFS_Visit(Graph_Node *graph_node, Tree_Node* parent_tree_node,
                        Queue<Graph_Node*, Tree_Node*>* node_queue, bool do_reverse) const;

    Graph_Node* _nodes; // Pointer to first node in _nodes list

    // For keeping track of graph
    unsigned _num_of_edges_in_graph;
    unsigned _num_of_nodes_in_graph;
};


#endif //DALGO_DYNAMIC_GRAPH_H
