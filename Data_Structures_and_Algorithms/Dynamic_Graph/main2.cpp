#include <iostream>
#include <cstdlib>
#include "Dynamic_Graph.h"

#define SEED 13658
#define TEST_SIZE 300
#define INITIAL_NODES_NUM 21
#define INITIAL_EDGES_NUM 110
#define MIN_KEY 153
#define MAX_KEY 9999
#define NUM_OF_OPERATIONS 8
#define INSERT_NODE 1
#define INSERT_EDGE 2
#define DELETE_NODE 3
#define DELETE_EDGE 4
#define STRONGLY_CONNECTED_COMPONENTS 5
#define RUN_BFS 6
#define OUT_DEGREE 7
#define IN_DEGREE 8



using namespace std;

class My_Edge
{
public:
    My_Edge(unsigned nfrom, unsigned nto):from(nfrom),to(nto){};
    unsigned get_from(){return from;}
    unsigned get_to(){return to;}
private:
    unsigned from;
    unsigned to;
};


unsigned generate_random_unsigned(const unsigned max_ind)
/*generates a random unsigned int in range [0,max_ind-1]*/
{
    return rand() % max_ind;
}

void generate_unique_keys(unsigned keys_array[], unsigned keys_num)
/*generates keys_num unique keys in the range [MIN_KEY,MAX_KEY].
the keys are stored in keys_array of size keys_num*/
{
    unsigned modulo_array[MAX_KEY - MIN_KEY + 1];
    for (unsigned i = 0;i < MAX_KEY - MIN_KEY + 1;i++)
    {
        modulo_array[i] = 0;
    }
    unsigned unique_keys_counter = 0;
    unsigned key = 0;
    while (unique_keys_counter < keys_num)
    {
        key = generate_random_unsigned(MAX_KEY - MIN_KEY + 1);
        if (modulo_array[key] == 0)
        {
            modulo_array[key] = 1;
            keys_array[unique_keys_counter] = key + MIN_KEY;
            unique_keys_counter = unique_keys_counter + 1;
        }
    }
}

void shift_nodes_arrays(Graph_Node* nodes_array[],unsigned deleted_index, unsigned size)
{
    if (deleted_index <= size)
    {
        for (unsigned i = deleted_index;i<size-1;i++)
        {
            nodes_array[i] = nodes_array[i+1];
        }
        nodes_array[size-1] = NULL;
    }
}

void shift_edges_arrays(Graph_Edge* edges_array[],My_Edge* my_edge_array[],unsigned deleted_index, unsigned size)
{
    if (deleted_index <= size - 1)
    {
        delete my_edge_array[deleted_index];
        my_edge_array[deleted_index] = NULL;
        for (unsigned i = deleted_index;i<size-1;i++)
        {
            edges_array[i] = edges_array[i+1];
            my_edge_array[i] = my_edge_array[i+1];
        }
        edges_array[size-1] = NULL;
        my_edge_array[size-1] = NULL;
    }
}

bool edge_does_not_exists(My_Edge* my_edge_array[], unsigned edges_array_counter, unsigned from, unsigned to)
{
    for (unsigned i=0; i < edges_array_counter;i++)
    {
        if (my_edge_array[i]->get_from() == from && my_edge_array[i]->get_to() == to)
        {
            return false;
        }
    }
    return true;
}

bool deleted_node(unsigned key, My_Edge* my_edge_array[], unsigned edges_array_counter)
{
    for (unsigned i=0;i<edges_array_counter;i++)
    {
        if (my_edge_array[i]->get_from() == key || my_edge_array[i]->get_to() == key)
        {
            return false;
        }
    }
    return true;
}


void exec_and_print_scc(Dynamic_Graph* G)
{
    Rooted_Tree* T  = G->SCC();
    cout<<"Print in layers after SCC:"<<"\n";
    T->Print_By_Layer(cout);
    cout<<"\n";
    cout<<"Preorder print after SCC:"<<"\n";
    T->Preorder_Print(cout);
    cout<<"\n";
    delete T;
}

void exec_and_print_bfs(Dynamic_Graph* G,Graph_Node* nodes_array[],unsigned nodes_array_counter)
{
    if (nodes_array_counter > 0)
    {
        unsigned node_index = generate_random_unsigned(nodes_array_counter);
        Rooted_Tree* T = G->BFS(nodes_array[node_index]);
        cout << "Print in layers after BFS:" << "\n";
        T->Print_By_Layer(cout);
        cout << "\n";
        cout << "Preorder print after BFS:" << "\n";
        T->Preorder_Print(cout);
        cout << "\n";
        delete T;
    }
}

void exec_insert_node(Dynamic_Graph* G, Graph_Node* nodes_array[], unsigned &nodes_array_counter, unsigned &keys_array_counter, unsigned nodes_keys_array[])
{
    nodes_array[nodes_array_counter] = G->Insert_Node(nodes_keys_array[keys_array_counter]);
    nodes_array_counter = nodes_array_counter + 1;
    keys_array_counter = keys_array_counter + 1;
}

void exec_delete_node(Dynamic_Graph* G,unsigned &nodes_array_counter, Graph_Node* nodes_array[], unsigned edges_array_counter, My_Edge* my_edge_array[])
{
    if (nodes_array_counter > 0)
    {
        unsigned node_index = generate_random_unsigned(nodes_array_counter);
        unsigned node_key = nodes_array[node_index]->Get_key();
        G->Delete_Node(nodes_array[node_index]);
        if (deleted_node(node_key,my_edge_array,edges_array_counter))
        {
            shift_nodes_arrays(nodes_array,node_index,nodes_array_counter);
            nodes_array_counter = nodes_array_counter - 1;
        }
    }
}

void exec_insert_edge(Dynamic_Graph* G,Graph_Node* nodes_array[], unsigned nodes_array_counter, My_Edge* my_edge_array[],unsigned &edges_array_counter, Graph_Edge* edges_array[])
{
    if (nodes_array_counter > 1)
    {
        unsigned node_index_1 = generate_random_unsigned(nodes_array_counter);
        unsigned node_index_2 = generate_random_unsigned(nodes_array_counter);
        unsigned node_key_1 = nodes_array[node_index_1]->Get_key();
        unsigned node_key_2 = nodes_array[node_index_2]->Get_key();
        if (node_index_1 != node_index_2 && edge_does_not_exists(my_edge_array, edges_array_counter, node_key_1, node_key_2))
        {
            edges_array[edges_array_counter] = G->Insert_Edge(nodes_array[node_index_1], nodes_array[node_index_2]);
            my_edge_array[edges_array_counter] = new My_Edge(node_key_1, node_key_2);
            edges_array_counter = edges_array_counter + 1;
        }
    }
}

void exec_delete_edge(Dynamic_Graph* G, unsigned &edges_array_counter, Graph_Edge* edges_array[],My_Edge* my_edge_array[])
{
    if (edges_array_counter > 0)
    {
        unsigned edge_index = generate_random_unsigned(edges_array_counter);
        G->Delete_Edge(edges_array[edge_index]);
        shift_edges_arrays(edges_array,my_edge_array,edge_index,edges_array_counter);
        edges_array_counter = edges_array_counter - 1;
    }
}

void exec_and_print_in_degree(unsigned nodes_array_counter, Graph_Node* nodes_array[])
{
    if (nodes_array_counter > 0)
    {
        unsigned node_index = generate_random_unsigned(nodes_array_counter);
        cout<<"The in degree of node "<< nodes_array[node_index]->Get_key()<< " is " << nodes_array[node_index]->Get_in_Degree()<<"\n";
    }
}

void exec_and_print_out_degree(unsigned nodes_array_counter, Graph_Node* nodes_array[])
{
    if (nodes_array_counter > 0)
    {
        unsigned node_index = generate_random_unsigned(nodes_array_counter);
        cout<<"The out degree of node "<< nodes_array[node_index]->Get_key()<< " is " << nodes_array[node_index]->Get_out_Degree()<<"\n";
    }
}
int main()
{
    srand(SEED);
    Graph_Node* nodes_array[TEST_SIZE+INITIAL_NODES_NUM] = {NULL};
    unsigned nodes_keys_array[TEST_SIZE+INITIAL_NODES_NUM*2];

    generate_unique_keys(nodes_keys_array,TEST_SIZE+INITIAL_NODES_NUM*2);

    unsigned nodes_array_counter = 0;
    unsigned keys_array_counter = 0;

    Graph_Edge* edges_array[TEST_SIZE + INITIAL_NODES_NUM*INITIAL_NODES_NUM] = {NULL};
    My_Edge* my_edge_array[TEST_SIZE + INITIAL_NODES_NUM*INITIAL_NODES_NUM] = {NULL};
    unsigned edges_array_counter = 0;

    Dynamic_Graph* G = new Dynamic_Graph();
    for (unsigned i =0;i<INITIAL_NODES_NUM;i++)
    {
        nodes_array[nodes_array_counter] = G->Insert_Node(nodes_keys_array[keys_array_counter]);
        nodes_array_counter = nodes_array_counter + 1;
        keys_array_counter = keys_array_counter + 1;
    }

    for (unsigned i=0;i < nodes_array_counter; i++)
    {
        for (unsigned j = 0; j < nodes_array_counter;j++)
        {
            if (i != j)
            {
                edges_array[edges_array_counter] = G->Insert_Edge(nodes_array[i],nodes_array[j]);
                my_edge_array[edges_array_counter] = new My_Edge(nodes_array[i]->Get_key(),nodes_array[j]->Get_key());
                edges_array_counter = edges_array_counter + 1;
            }
        }
    }
    exec_and_print_in_degree(nodes_array_counter,nodes_array);
    exec_and_print_out_degree(nodes_array_counter,nodes_array);
    exec_and_print_bfs(G,nodes_array,nodes_array_counter);
    exec_and_print_scc(G);

    for (unsigned i = 0 ; i<INITIAL_NODES_NUM*INITIAL_NODES_NUM;i++)
    {
        exec_delete_edge(G,edges_array_counter,edges_array,my_edge_array);
    }

    exec_and_print_in_degree(nodes_array_counter,nodes_array);
    exec_and_print_out_degree(nodes_array_counter,nodes_array);
    exec_and_print_in_degree(nodes_array_counter,nodes_array);
    exec_and_print_out_degree(nodes_array_counter,nodes_array);
    exec_and_print_in_degree(nodes_array_counter,nodes_array);
    exec_and_print_out_degree(nodes_array_counter,nodes_array);
    exec_and_print_bfs(G,nodes_array,nodes_array_counter);
    exec_and_print_scc(G);

    for (unsigned i=0;i < INITIAL_NODES_NUM*INITIAL_NODES_NUM; i++)
    {
        exec_insert_edge(G,nodes_array,nodes_array_counter,my_edge_array,edges_array_counter,edges_array);
    }

    exec_and_print_in_degree(nodes_array_counter,nodes_array);
    exec_and_print_out_degree(nodes_array_counter,nodes_array);
    exec_and_print_in_degree(nodes_array_counter,nodes_array);
    exec_and_print_out_degree(nodes_array_counter,nodes_array);
    exec_and_print_in_degree(nodes_array_counter,nodes_array);
    exec_and_print_out_degree(nodes_array_counter,nodes_array);
    exec_and_print_bfs(G,nodes_array,nodes_array_counter);
    exec_and_print_scc(G);

    delete G;

    for (unsigned i =0;i<nodes_array_counter;i++)
    {
        nodes_array[i] = NULL;
    }

    for (unsigned i =0;i<edges_array_counter;i++)
    {
        delete my_edge_array[i];
        my_edge_array[i] = NULL;
        edges_array[i] = NULL;
    }
    nodes_array_counter = 0;
    edges_array_counter = 0;

    G = new Dynamic_Graph();

    for (unsigned i =0;i<INITIAL_NODES_NUM;i++)
    {
        nodes_array[nodes_array_counter] = G->Insert_Node(nodes_keys_array[nodes_array_counter]);
        nodes_array_counter = nodes_array_counter + 1;
    }

    while(edges_array_counter < INITIAL_EDGES_NUM)
    {
        exec_insert_edge(G,nodes_array,nodes_array_counter,my_edge_array,edges_array_counter,edges_array);
    }

    unsigned operation;

    for (unsigned i = 0;i < TEST_SIZE;i++)
    {
        operation = generate_random_unsigned(NUM_OF_OPERATIONS)+1;
        switch (operation)
        {
            case INSERT_NODE:
                exec_insert_node(G,nodes_array,nodes_array_counter,keys_array_counter ,nodes_keys_array);
                break;
            case INSERT_EDGE:
                exec_insert_edge(G,nodes_array,nodes_array_counter,my_edge_array,edges_array_counter,edges_array);
                break;
            case DELETE_NODE:
                exec_delete_node(G,nodes_array_counter,nodes_array,edges_array_counter,my_edge_array);
                break;
            case DELETE_EDGE:
                exec_delete_edge(G,edges_array_counter,edges_array,my_edge_array);
                break;
            case STRONGLY_CONNECTED_COMPONENTS:
                exec_and_print_scc(G);
                break;
            case RUN_BFS:
                exec_and_print_bfs(G,nodes_array,nodes_array_counter);
                break;
            case OUT_DEGREE:
                exec_and_print_out_degree(nodes_array_counter,nodes_array);
                break;
            case IN_DEGREE:
                exec_and_print_in_degree(nodes_array_counter,nodes_array);
                break;
        }
    }
    for (unsigned i = 0; i<edges_array_counter;i++ )
    {
        delete my_edge_array[i];
    }
    delete G;
}