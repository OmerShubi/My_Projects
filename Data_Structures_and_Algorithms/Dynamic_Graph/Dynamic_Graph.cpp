//
// Created by Shubi & Eyal on 21/12/2019.
//

#include "Dynamic_Graph.h"


void Dynamic_Graph::Delete_Node(Graph_Node *node) {

    if(node == NULL){
        return;
    }

    // if has incoming/outgoing edges - do nothing
    if(node->has_incoming_outgoing_edges()){
        return;
    }

    this->_num_of_nodes_in_graph--;

    // 'Fill in' the gap
    Graph_Node* prev_node = node->getPrevNode();
    Graph_Node* next_node = node->getNextNode();
    if(prev_node != NULL) {
        prev_node->setNextNode(next_node);
    }else{
        this->_nodes=next_node;
    }

    if(next_node != NULL) {
        next_node->setPrevNode(prev_node);
    }

    // Means it is the only node in the graph
    if(next_node == NULL && prev_node == NULL){
        this->_nodes = NULL;
    }

    delete node;
}

Graph_Node *Dynamic_Graph::Insert_Node(unsigned node_key) {

    this->_num_of_nodes_in_graph++;

    // Generate new node and add it as first node in _nodes doubly-linked list
    Graph_Node* new_node = new Graph_Node(node_key, NULL, this->_nodes);

    if(this->_nodes != NULL){

        this->_nodes->setPrevNode(new_node);
    }

    this->_nodes = new_node;

    return new_node;
}

Graph_Edge *Dynamic_Graph::Insert_Edge(Graph_Node* from, Graph_Node* to){


    if(from == NULL || to == NULL){
        return NULL;
    }

    this->_num_of_edges_in_graph++;

    // Generate new edge and add it as first edge in from's node outgoing edges list
    Graph_Edge* new_edge = new Graph_Edge(from, to);
    Graph_Edge* new_reverse_edge = new Graph_Edge(to, from);

    new_edge->_reverse_edge = new_reverse_edge;

    from->add_edge_to_edges(new_edge, false);
    from->_num_of_outgoing_edges++;

    // Keep track of how many incoming edges into 'to'
    to->add_edge_to_edges(new_reverse_edge, true);
    to->_num_of_incoming_edges++;



    return new_edge;
}

void Dynamic_Graph::Delete_Edge(Graph_Edge *edge) {

    if (edge == NULL) {
        return;
    }

    this->_num_of_edges_in_graph--;

    edge->_target_node->_num_of_incoming_edges--;
    edge->_source_node->_num_of_outgoing_edges--;


    delete edge;
}

Rooted_Tree *Dynamic_Graph::SCC() const {

    /*
     * Pseudo code
     *
     * 1. Run DFS
     * 2. phi = the sequence of vertices v ∈ V in order of decreasing v.retraction_time
     * 3. construct the transpose digraph ←−G of G
     * 4. Run DFS on transpose graph, processing the vertices in ψ-order
     * 5. output the vertices of each tree in the DFS forest as a SCC
     */

    Queue<Graph_Node*, Tree_Node*>* node_queue = new Queue<Graph_Node*, Tree_Node*>();

    // 1 + 2, First dfs run is for updating each v.retraction_time. node_queue gets filled according to phi order
    Rooted_Tree* dfs_forest = DFS(node_queue, false);

    // 3 + 4 + 5 are accomplished in DFS(), with do_reverse flag equal to true
    Rooted_Tree* SCC_forest = DFS(node_queue, true);

    delete dfs_forest; // doesn't save the dfs_tree as it is not needed.
    delete node_queue;

    // We keep count of nodes in graph, for number of nodes in the forest we add one for the virtual root
    SCC_forest->setNumberOfNodesInTree(_num_of_nodes_in_graph + ONE);

    return SCC_forest;
}

Rooted_Tree *Dynamic_Graph::DFS(Queue<Graph_Node*, Tree_Node*>* node_queue, bool do_reverse) const {


    Tree_Node* virtual_root = new Tree_Node(NULL, NULL, NULL, ZERO, ZERO);
    Rooted_Tree* dfs_forest = new Rooted_Tree(virtual_root);

    // DFS Initialization
    Graph_Node* current_graph_node = this->_nodes;
    while(current_graph_node != NULL){

        current_graph_node->setColor(WHITE);
        current_graph_node = current_graph_node->getNextNode();
    }

    if(do_reverse){

        QueueItem<Graph_Node*, Tree_Node*>* queue_item = node_queue->Reverse_Dequeue();
        current_graph_node = queue_item->getGraphNode();
        delete queue_item;
    } else {

        current_graph_node = this->_nodes; // First neighbour
    }

    Tree_Node* prev_sub_tree_root = NULL;

    while(current_graph_node != NULL){

        if(current_graph_node->getColor() == WHITE) {

            Tree_Node* curr_sub_tree_root = new Tree_Node(virtual_root, NULL, NULL,
                                                          current_graph_node->Get_key(), ONE);

            // Means we are at first child, so update u with v as left child.
            if(prev_sub_tree_root == NULL){

                virtual_root->setLeftChild(curr_sub_tree_root);
            }else{ // Means we are at the second or more child of u, means the previous v has a right sibling

                prev_sub_tree_root->setRightSibling(curr_sub_tree_root);
            }

            prev_sub_tree_root = curr_sub_tree_root;

            // Recursive calls
            DFS_Visit(current_graph_node, curr_sub_tree_root, node_queue, do_reverse);
        }


        if(do_reverse){

            QueueItem<Graph_Node*, Tree_Node*>* queue_item = node_queue->Reverse_Dequeue();
            if(queue_item!= NULL){

                current_graph_node = queue_item->getGraphNode();
            }else{

                current_graph_node = NULL;
            }

            delete queue_item;
        } else {

            current_graph_node = current_graph_node->getNextNode();
        }
    }

    return dfs_forest;
}

void Dynamic_Graph::DFS_Visit(Graph_Node *graph_node, Tree_Node* parent_tree_node,
                                  Queue<Graph_Node*, Tree_Node*>* node_queue, bool do_reverse) const {


    graph_node->setColor(GRAY);
    Graph_Edge* current_edge = NULL;

    if(do_reverse){
        current_edge = graph_node->_reverse_edges;
    }
    else {
        current_edge = graph_node->_out_edges;
    }
    Graph_Node* v = NULL;

    Tree_Node* prev_tree_node = NULL;

    while(current_edge != NULL) {

        v = current_edge->_target_node;
        current_edge = current_edge->getNextEdge();

        if(v==NULL){
            return;
        }

        if(v->getColor() == WHITE){

            Tree_Node* curr_tree_node = new Tree_Node(parent_tree_node, NULL, NULL,
                                                      v->Get_key(), parent_tree_node->getDistance()+1);



            // Means we are at first child, so update u with v as left child.
            if(prev_tree_node == NULL){

                parent_tree_node->setLeftChild(curr_tree_node);
            }else{ // Means we are at the second or more child of u, means the previous v has a right sibling

                prev_tree_node->setRightSibling(curr_tree_node);
            }

            prev_tree_node = curr_tree_node;

            DFS_Visit(v, curr_tree_node, node_queue, do_reverse);
        }

    }

    graph_node->setColor(BLACK);

    // Add node to queue in the correct order for SCC
    if(node_queue != NULL && !do_reverse) {
        node_queue->Enqueue(graph_node, NULL);
    }
    return;


}

Rooted_Tree *Dynamic_Graph::BFS(Graph_Node *source) const {


    BFS_Initialization(source);

    Tree_Node* source_tree_node = new Tree_Node(NULL, NULL, NULL, source->Get_key(), source->getDistance());

    Queue<Graph_Node*, Tree_Node*> Q = Queue<Graph_Node*, Tree_Node*>();
    Q.Enqueue(source, source_tree_node);

    // initialize tree with 'source' node as 'root' node
    Rooted_Tree* bfs_tree = new Rooted_Tree(source_tree_node);

    Graph_Node* u = NULL;
    Graph_Edge* current_edge= NULL;
    Graph_Node* v = NULL;
    Tree_Node* u_tree_node = NULL;


    while (!Q.is_empty()){

        QueueItem<Graph_Node*, Tree_Node*>* queue_item = Q.Dequeue();
        u = queue_item->getGraphNode();
        u_tree_node = queue_item->getTreeNode();
        delete queue_item;

        current_edge = u->_out_edges;

        // bfs tree addition

        Tree_Node* prev_v_tree_node = NULL;

        while (current_edge != NULL) {

            v = current_edge->_target_node; // target node of edge sourced at u
            current_edge = current_edge->getNextEdge();

            if (v->getColor() == WHITE) {

                v->setColor(GRAY);
                v->setDistance(u->getDistance() + 1);

                // bfs tree additions from here
                Tree_Node *curr_v_tree_node = new Tree_Node(u_tree_node, NULL, NULL, v->Get_key(), v->getDistance());
                bfs_tree->incrementNumberOfNodesInTree();
                Q.Enqueue(v, curr_v_tree_node);

                // Means we are at first child, so update u with v as left child.
                if(prev_v_tree_node == NULL){

                    u_tree_node->setLeftChild(curr_v_tree_node);
                }else{ // Means we are at the second or more child of u, means the previous v has a right sibling

                    prev_v_tree_node->setRightSibling(curr_v_tree_node);
                }

                prev_v_tree_node = curr_v_tree_node;
            }
        }

        u->setColor(BLACK);
    }

    return bfs_tree;
}

void Dynamic_Graph::BFS_Initialization(Graph_Node *source) const {

    Graph_Node* current_node = this->_nodes;

    while(current_node != NULL){
        current_node->setColor(WHITE);
        current_node->setDistance(INF);
        current_node = current_node->getNextNode();
    }

    source->setColor(GRAY);
    source->setDistance(ZERO);
}
