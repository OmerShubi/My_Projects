//
// Created by Shubi & Eyal on 23/12/2019.
//

#ifndef DALGO_QUEUEITEM_H
#define DALGO_QUEUEITEM_H

#include "Graph_Node.h"
template <class G, class T> class Queue;

/*
 * QueueItem that store a pointer to a graph node and corresponding tree node (optional)
 * Is used in Queue.
 */
template <class G, class T> class QueueItem {

public:
    /*
     * Constructor
     */
    QueueItem(G graph_node, T tree_node) :
            _graph_node(graph_node), _tree_node(tree_node),
            _newer_item(NULL),_older_item(NULL) {}

    /*
     * Destructor
     */
    ~QueueItem() {
        QueueItem* newerItem = this->getNewerItem();
        QueueItem* olderItem = this->getOlderItem();

        if (newerItem != NULL){
            newerItem->setOlderItem(olderItem);
        }

        if(olderItem != NULL){
            olderItem->setNewerItem(newerItem);
        }

    }

    /*
     * Getters and Setters
     */
    QueueItem<G, T> *getNewerItem() const {
        return _newer_item;
    }

    void setNewerItem(QueueItem<G, T> *newerItem) {
        _newer_item = newerItem;
    }

    QueueItem<G, T> *getOlderItem() const {
        return _older_item;
    }

    void setOlderItem(QueueItem<G, T> *olderItem) {
        _older_item = olderItem;
    }

    T getTreeNode() const {
        return _tree_node;
    }

    G getGraphNode() const {
        return _graph_node;
    }

private:
    QueueItem<G, T>* _newer_item; // Pointer to next (newer) queue item in queue
    QueueItem<G, T>* _older_item; // Pointer to previous (older) queue item in queue
    T _tree_node; // Pointer to item of type T - in our case usually Tree node
    G _graph_node; // Pointer to item of type G - in our case usually graph node
};


#endif //DALGO_QUEUEITEM_H
