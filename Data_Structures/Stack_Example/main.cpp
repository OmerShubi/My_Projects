#include "stack.h"
#include <cstdio>
#include <cstring>
#include <iostream>


using std::cin;
using std::string;
using std::cerr;
using std::endl;
enum CommandsEnum{
    NEW = 0, PUSH, POP, TOP, EMPTY_,
    SIZE, PRINT, QUIT
} ;

const string consoleCommands[] = {"new", "push",
                                  "pop", "top", "empty", "size", "print", "quit"};

// Additional enum to handle all the different prints to screen, both errors and regular
const string printCommands[] = {"Bad input type!", "Popped: ", "Top: ",
                                "The stack is empty", "The stack is not empty",
                                "stack size: ", "Bad command",
                                "Bad stack Type: ", "Bad Input: "};
enum PrintCommands {
    BAD_INPUT_TYPE = 0, POPPED, TOPED, IS_EMPTY, IS_NOT_EMPTY,
    STACK_SIZE, BAD_COMMAND, BAD_STACK_TYPE, BAD_INPUT
} ;

/**
 * This method is controlling the session of a stack
 * given a type T.
 */
template<typename T>
void stackSession();

int main()
{
    enum StackTypes {
        INT = 0, FLOAT, STRING
    } ;
    const string stackTypes[] = {"int", "float", "string"};
    cout << "Welcome to Stack builder!" << endl;
    cout << "Type 'new' then 'int' / 'float' / 'string' to initialize stack of corresponding type" << endl;
    string input;
    cin >> input;
    try {
        if (input == consoleCommands[NEW]) {
            string stackType;
            cin >> stackType;
            if (stackType == stackTypes[INT]) {
                stackSession<int>();
            } else if (stackType == stackTypes[FLOAT]) {
                stackSession<float>();
            } else if (stackType == stackTypes[STRING]) {
                stackSession<string>();
            } else {
                throw std::runtime_error(printCommands[BAD_STACK_TYPE] + stackType);
            }
        } else {
            throw std::runtime_error(printCommands[BAD_INPUT] + input);
        }
    } // handles runtime_error of bad input and of bad stack type
    catch (const std::exception &error) {
        cerr << error.what() << endl;
    }

}

template<typename T>
void stackSession() {
    cout << "Great, your options are" << endl;
    // skips 0 (=new) as stack already created
    for (int i = 1; i< sizeof(consoleCommands)/sizeof(consoleCommands[0]); i++){
        cout << consoleCommands[i] << " ";
    }
    cout << "\n*push and pop should be followed by a value" << endl;
    stack<T> stack;
    string input;
    cin >> input;
    while (input != consoleCommands[QUIT])
    {
        if (input == consoleCommands[PUSH]) // performs the push operation
        {
            // Checks whether input is of type T as expected. Throws exception if not.
            T value;
            cin >> value;
            if (cin.fail())
            {
                cin.clear(); // clears buffer on cin failure
                throw std::runtime_error(printCommands[BAD_INPUT_TYPE]);
            } else {
                stack.push(value);
            }
        }
        else if (input == consoleCommands[POP]) // performs the pop operation
        {
            try
            {
                T value = stack.pop();
                cout << printCommands[POPPED] << value << endl;
            }
                //Handles potential range_error (Empty stack) exceptions from pop
            catch (const std::exception &error)
            {
                cerr << error.what() << endl;
            }
        }
        else if (input == consoleCommands[TOP]) //performs the top operation
        {
            try
            {
                T value = stack.top();
                cout << printCommands[TOPED] << value << endl;
            }
                //Handles potential range_error (Empty stack) exceptions from top
            catch (const std::exception &error)
            {
                cerr << error.what() << endl;
            }
        }
        else if (input == consoleCommands[EMPTY_]) // displays whether stack is empty
        {
            if (stack.empty())
            {
                cout << printCommands[IS_EMPTY] << endl;
            }
            else
            {
                cout << printCommands[IS_NOT_EMPTY] << endl;
            }
        }
        else if (input == consoleCommands[SIZE]) // displays stack size
        {
            cout << printCommands[STACK_SIZE] << stack.size() << endl;
        }
        else if (input == consoleCommands[PRINT]) // displays all stack elements' values
        {
            stack.print();
        }
        else
        {
            cerr << printCommands[BAD_COMMAND] << endl;
        }

        cin >> input;
    }
}