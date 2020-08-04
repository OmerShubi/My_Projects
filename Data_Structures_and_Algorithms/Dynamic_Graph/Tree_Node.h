//
// Created by Shubi & Eyal on 23/12/2019.
//

#ifndef DALGO_TREE_NODE_H
#define DALGO_TREE_NODE_H

/*
 *     Tree node in the format of Left-Child Right-Sibling
 *     Does not support insertion and extraction as they are not required
 */
class Tree_Node {

public:
    /*
     * Constructor
     *
     */
    Tree_Node(Tree_Node *parent, Tree_Node *leftChild, Tree_Node *rightSibling,
              unsigned int key, unsigned int distance) : _parent(parent), _left_child(leftChild),
                                  _right_sibling(rightSibling), _key(key), _distance(distance) {}

    /*
     * Destructor
     * In charge of deleting left child and right sibling as well
     * This way the whole tree gets deleted
     */
    ~Tree_Node(){
        delete _left_child;
        delete _right_sibling;
    }

    /*
     * Getters and Setters
     */
    unsigned int getKey() const {
        return _key;
    }

    Tree_Node *getParent() const {
        return _parent;
    }

    Tree_Node *getLeftChild() const {
        return _left_child;
    }

    Tree_Node *getRightSibling() const {
        return _right_sibling;
    }

    unsigned int getDistance() const {
        return _distance;
    }

    void setLeftChild(Tree_Node *leftChild) {
        _left_child = leftChild;
    }

    void setRightSibling(Tree_Node *rightSibling) {
        _right_sibling = rightSibling;
    }

private:
    // Left-Child Right-Sibling Node
    Tree_Node* _parent;
    Tree_Node* _left_child;
    Tree_Node* _right_sibling;

    unsigned _key; // Unique key value
    unsigned _distance; // Distance from tree root

};


#endif //DALGO_TREE_NODE_H
