//
// Created by Shubi & Eyal on 21/12/2019.
//

#include "Rooted_Tree.h"
#include "Queue.h"



void Rooted_Tree::Print_By_Layer(std::ostream &stream) const {

    if(this->_root==NULL){
        return;
    }
    // Queue declared as (tree_node, tree_node) to deal with template
    // only the second tree_node is used!
    // The first is just a placeholder with NULL.
    Queue<Tree_Node*, Tree_Node*> Q = Queue<Tree_Node*, Tree_Node*>();
    Q.Enqueue(NULL, this->_root);

    unsigned max_distance = ZERO;
    Tree_Node* u = NULL;
    Tree_Node* v = NULL;
    stream << this->_root->getKey();

    while (!Q.is_empty()){

        QueueItem<Tree_Node*, Tree_Node*>* queue_item = Q.Dequeue();
        u = queue_item->getTreeNode();
        delete queue_item;

        v = u->getLeftChild();

        while (v != NULL) {


            if (max_distance < v->getDistance()) {

                max_distance = v->getDistance();
                stream << "\n";
            }
            else{

                stream << ",";
            }
            stream << v->getKey();

            Q.Enqueue(NULL, v);

            v = v->getRightSibling();
        }
    }
}

void Rooted_Tree::Preorder_Print(std::ostream &stream) const {

    unsigned from = PARENT_SIBLING;
    Tree_Node* x = _root;
    unsigned node_number = ZERO;

    while(x != NULL){

        if(from == PARENT_SIBLING) {

            stream << x->getKey();

            node_number++;

            if(node_number != _number_of_nodes_in_tree){

                stream <<",";
            }

            if (x->getLeftChild() != NULL) {

                x = x->getLeftChild();
            } else {

                if (x->getRightSibling() != NULL) {

                    x = x->getRightSibling();
                } else {

                    from = CHILD;
                    x = x->getParent();
                }
            }

        } else{

            if(x->getRightSibling()!= NULL){

                from = PARENT_SIBLING;
                x = x->getRightSibling();
            } else{

                x = x->getParent();
            }
        }
    }
}

void Rooted_Tree::setNumberOfNodesInTree(unsigned int numberOfNodesInTree) {
    _number_of_nodes_in_tree = numberOfNodesInTree;
}
