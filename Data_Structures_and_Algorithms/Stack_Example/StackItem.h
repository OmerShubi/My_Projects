#ifndef STACK_EXAMPLE_STACKITEM_H
#define STACK_EXAMPLE_STACKITEM_H

#define POINTER_ALREADY_SET "Trying to set a pointer that already used!"
#include <exception>
#include <stdexcept>


/*
 * StackItem
 * Template class
 * stores int / float / string and a pointer to the next element
 * internal class for stack class use only.
 */
template <class T> class stack;
template <class T> class StackItem
{
friend class stack<T>;
private:
    // Constructor
    explicit StackItem(const T &item) : _item(item), _nextPtr(NULL) {}

    /*
     * getValue
     * Gets the value stored in this StackItem
     *
     * @return T _item
     */
    T getValue() const
    {
        return _item;
    }

    /*
     * getNext
     * Gets the pointer to the next element in stack
     *
     * @return StackItem* _nextPtr
     */
    StackItem* getNext() const
    {
        return _nextPtr;
    }

    /*
     * setNext
     * Determines to which element current element needs to point (next element in stack)
     * Throws error if already set (!= NULL)
     *
     * @param itemPtr StackItem* the pointer to the next element
     * @return void
     */
    void setNext(StackItem* itemPtr);

    T _item; // stored value
    StackItem* _nextPtr; // pointer to next element, if none - NULL
};

template <typename T>
void StackItem<T>::setNext(StackItem* itemPtr)
{
    // Makes sure we don't 'break' the chain of elements
    if(_nextPtr == NULL)
    {
        _nextPtr = itemPtr;
    }
    else
    {
        throw std::runtime_error(POINTER_ALREADY_SET);
    }
}
#endif //STACK_EXAMPLE_STACKITEM_H
