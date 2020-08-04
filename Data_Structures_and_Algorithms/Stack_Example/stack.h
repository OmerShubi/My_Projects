#ifndef STACK_EXAMPLE_STACK_H
#define STACK_EXAMPLE_STACK_H

#include <iostream>
#include <exception>
#include <stdexcept>
#include "StackItem.h"


#define ZERO 0
#define EMPTY_STACK "Empty stack"
#define STACK_CONTENT "Stack content:"

using std::cout;
using std::endl;

/*
 * stack
 * Implements a stack data structure by singley (one-way) linked list.
 * Makes use of the StackItem class that stores int / float / string
 * and the pointer to the next element.
 * By itself stores a pointer to the first element in the linked list,
 * and how many elements there are in total.
 * Allows using pop and push functions to manipulate.
 * print, empty, size, top functions to get additional info.
 *
 */
template <class T>
class stack
{
public:

    // Empty stack construct
    stack() : _first(NULL), _size(ZERO) {}

    /*
     * Copy constructor
     * makes use of reverseCopy function to create the copy while
     * maintaining the original element order.
     *
     * @param const stack &otherStack stack to be copied
     */
    stack(const stack &otherStack);

    /*
     * operator=
     * makes use of reverseCopy function to
     * maintain the original element order.
     *
     * @param const stack &rightHandSide stack to be copied
     */
    stack& operator=(const stack &rightHandSide);

    /*
     * empty
     * const function
     * Checks whether stack is empty or not
     *
     * @return bool true if empty, false otherwise
     */
    bool empty() const
    {
        return _size == ZERO;
    }

    /*
     * size
     * const function
     * Retrieves number of elements in the stack
     *
     * @return size_t _size
     */
    size_t size() const
    {
        return _size;
    }

    /*
     * pop
     * Extracts(returns value and deletes) the top element from stack,
     * updates the top element and the number of elements,
     * If stack is empty throws Empty stack
     *
     *     ***handles memory deletion***
     *
     * @return T value of top element in stack before manipulation
     */
    T pop();

    /*
     * top
     * const function
     * Retrieves the value of the top element in the stack.
     * If empty throws "Empty stack"
     *
     * @return T value of the top element in the stack.
     */
    T top() const;

    /*
     * push
     * Inserts a new element to the top stack,
     * updates (_first) accordingly and the number of elements (_size)
     * Handles POINTER_ALREADY_SET exception from StackItem<T>::setNext
     *
     * @param T item the value to be stored
     * @return void
     */
    void push(T item);

    // Prints all stack elements by order, one element per row.
    /*
     * print
     * displays all values, by order, stored in the stack.
     * const function
     *
     * @return void
     */
    void print() const;

    // Class Destructor
    ~stack()
    {
        try
        {
            destroy();
        }
        // Handles potential runtime error (Empty stack) from pop from destroy
        catch (const std::exception &error)
        {
            std::cerr << error.what() << endl;
        }
    }

private:
    StackItem<T> *_first; // stores pointer to the _first (top) StackItem in stack
    size_t _size; // stores how many elements in stack

    /*
     * destroy
     * pops all elements in stack
     * internal use of destructor
     *
     * @return void
     */
    void destroy();

    /*
     * reverseCopy
     * Copies all element values from origin to destination, in reverse order
     * used by copy and operator= only, to maintain original element value order
     * Assumes destination is empty.
     *
     * @param const stack &origin the stack to be copied from
     * @param const stack &destination the stack to be copied to
     *
     * @return void
     */
    void reverseCopy(const stack &origin, stack &destination);


};

template <typename T>
stack<T>::stack(const stack<T> &otherStack): _first(NULL), _size(otherStack._size)
{
	if(!otherStack.empty())
	{
		stack temp;
		reverseCopy(otherStack, temp);
		reverseCopy(temp, (stack<T> &) this);
	}
}

template <typename T>
stack<T>& stack<T>::operator=(const stack<T> &rightHandSide)
{
	if (this  == &rightHandSide) return *this; //check for self assignment
	if(!rightHandSide.empty())
	{
		// if the stack isn't empty, empties and only then copies new elements.
	    try
        {
			destroy();
		}
		// Handles potential runtime error (Empty stack) from pop from destroy
		catch (const std::exception &error)
		{
			std::cerr << error.what() << endl;
		}

		_size = rightHandSide.size();
		stack temp;
		reverseCopy(rightHandSide, temp);
		reverseCopy(temp, (stack<T> &) this);
	}
	return *this;
}

template <typename T>
void stack<T>::destroy()
{
    while (!empty())
        pop();
}

template <typename T>
T stack<T>::pop()
{
    if (!empty())
    {
        T value = _first->getValue();
        StackItem<T> *temp = _first;
        _first = _first->getNext();
        delete temp;
        _size--;
        return value;
    }
    else
    {
        throw std::range_error(EMPTY_STACK);
    }
}

template <typename T>
T stack<T>::top() const
{
    if (!empty())
    {
        return _first->getValue();
    }
    else
    {
        throw std::range_error(EMPTY_STACK);
    }
}

template <typename T>
void stack<T>::push(T item)
{
    // Allocate a new StackItem object
    StackItem<T> *ptr = new StackItem<T>(item);

    try
    {
        ptr->setNext(_first);
        _first = ptr;
        _size++;
    }
    catch (const std::exception &error)
    {
        std::cerr << error.what() << endl;
    }
}

template <typename T>
void stack<T>::print() const
{
    cout << (STACK_CONTENT) << endl;
    if (!empty())
    {
        StackItem<T> *current = _first;
        for (size_t i = ZERO; i < _size; i++)
        {
            cout << current->getValue() << endl;
            current = current->getNext();
        }
    }
}

template <typename T>
void stack<T>::reverseCopy(const stack &origin, stack &destination)
{
	StackItem<T> *current = origin._first;
		for (size_t i = ZERO; i < origin._size; i++)
		{
			destination.push(current->getValue());
			current = current->getNext();
		}
}

#endif //STACK_EXAMPLE_STACK_H


