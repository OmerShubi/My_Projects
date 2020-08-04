//
// Created by Shubi & Eyal on 21/12/2019.
//

#ifndef DALGO_ROOTED_TREE_H
#define DALGO_ROOTED_TREE_H


#include <ostream>
#include <cstddef>
#include "Tree_Node.h"

#define ZERO 0
#define ONE 1
#define CHILD 0 // Came from child
#define PARENT_SIBLING 1 // Came from parent or left sibling

/*
 * Implementation of a LCRS Rooted tree
 *
 * supports Print_By_Layer() and Preorder_Print()
 */
class Rooted_Tree {

public:

    /*
     *  Default Constructor
     */
    Rooted_Tree() : _root(NULL),_number_of_nodes_in_tree(ZERO) {}

    /*
     * Constructor with a given root
     */
    Rooted_Tree(Tree_Node *root) : _root(root),_number_of_nodes_in_tree(ONE) {}

    /*
     * Destructor
     * Deletes the tree and any data stored in it
     */
    ~Rooted_Tree() {

        // the root then deletes left child &
        // right sibling which in turn delete their child and sibling and so on
        delete _root;
    }

    /*
     * Prints the key of each node according to defined procedure
     */
    void Print_By_Layer(std::ostream& stream) const;

    /*
     * Prints the key of each node according to Preorder order
     */
    void Preorder_Print(std::ostream& stream) const;

    /*
     * Setter
     */
    void setNumberOfNodesInTree(unsigned int numberOfNodesInTree);

    /*
     * Increment number of nodes in tree
     */
    void incrementNumberOfNodesInTree(){
        _number_of_nodes_in_tree++;
    }

private:
    Tree_Node* _root; // pointer to tree root
    unsigned _number_of_nodes_in_tree; // Stores the number of nodes in the tree
};


#endif //DALGO_ROOTED_TREE_H
