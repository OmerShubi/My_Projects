//
// Created by Shubi & Eyal on 23/12/2019.
//

#ifndef DALGO_QUEUE_H
#define DALGO_QUEUE_H

#include "Graph_Node.h"
#include "QueueItem.h"

#include <cstddef>

/*
 * Queue - FIFO Data structure
 *
 * Holds QueueItems that each store a pointer to a Graph_Node and corresponding Tree_Node.
 * _oldest is pointer to oldest queueitem in queue and _newest corresponds to the newest.
 *
 * Supports Enqueue(G graph_node, T tree_node), Dequeue(), Reverse_Dequeue(), is_empty()
 */
template <class G, class T> class Queue {
public:
    Queue() : _oldest(NULL), _newest(NULL) {}


    /*
     * Adds a QueueItem that stores a node to the Queue
     */
    void Enqueue(G graph_node, T tree_node){

        QueueItem<G, T> *new_queue_item = new QueueItem<G, T>(graph_node, tree_node);

        // Empty Queue
        if(_oldest == NULL){

            _oldest = new_queue_item;
            _newest = new_queue_item;
        }
        // Otherwise
        else{

            _newest->setNewerItem(new_queue_item);
            new_queue_item->setOlderItem(_newest);

            _newest = new_queue_item;
        }

    }

    /*
     * Remove and return the oldest  (first inserted) QueueItem from Queue,
     *
     * Does NOT delete memory, rather transfers ownership.
     */
    QueueItem<G, T>* Dequeue() {

        if (_oldest == NULL){
            return NULL;
        }

        QueueItem<G, T>* old_first = _oldest;
        if(_oldest->getNewerItem() == NULL){
            _oldest = NULL;
            _newest = NULL;
        }
        else {
            _oldest = _oldest->getNewerItem();
        }

        return old_first;
    }

    /*
     * Remove and return the newest (last inserted) queueitem
     *
     * Does NOT delete memory, rather transfers ownership.
     */
    QueueItem<G, T>* Reverse_Dequeue(){
        if (_newest == NULL){
            return NULL;
        }

        QueueItem<G, T>* old_last = _newest;

        if(_newest->getOlderItem() == NULL){
            _oldest = NULL;
            _newest = NULL;
        }
        else {
            _newest = _newest->getOlderItem();
        }

        return old_last;
    }

    /*
     * Indicator whether the queue is empty or not. Returns true if empty and false otherwise.
     */
    bool is_empty(){
        return (_oldest == NULL);
    }


private:
    QueueItem<G, T>* _oldest; // pointer to first queue item in queue
    QueueItem<G, T>* _newest; // pointer to last queue item in queue

};


#endif //DALGO_QUEUE_H
