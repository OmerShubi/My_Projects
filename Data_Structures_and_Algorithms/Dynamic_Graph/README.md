# Dynamic Tree Graph C++ Implementation

Support edge and node insertion and deletion, BFS, SCC, and DFS(for SCC)

Compile with `main.cpp` or `main2.cpp` to simulate different scenarios. 

Corresponding sample output is in `main_output.txt` 

## commands

 - `g++ *.cpp -o main`
 - `valgrind --tool=memcheck --leak-check=full ./main`
 - `./main > out2.txt`

 
 ## Graph implementation:
 
 - Nodes in doubly-linked list
 - For each node stores the outgoing neighbours, (left child right sibling)
 - Additional info in each class
 
Methods and Time Complexity
----------------------------
 - Graph_Node
   ==========
   - unsigned Get_out_Degree() const - O(#degrees)
   - unsigned Get_in_Degree() const - O(#degrees)
   - unsigned Get_key() const - O(1)

 - Graph_Edge
   ==========
   
 - Rooted_Tree
   ==========
   - Rooted_Tree() - O(1)
   - ~Rooted_Tree() - O(#nodes)
   - void Print_By_Layer(std::ostream& stream) const - O(#nodes)
   - void Preorder_Print(std::ostream& stream) const - No req.

 - Dynamic_Graph
   =============
   - Dynamic_Graph() - O(1)
   - ~Dynamic_Graph() - O(#nodes + #edges)
   - Graph_Node* Insert_Node(unsigned node_key) - O(1)
   - void Delete_Node(Graph_Node* node) - O(1)
   - Graph_Edge* Insert_Edge(Graph_Node* from, Graph_Node* to) - O(1)
   - void Delete_Edge(Graph_Edge* edge) - O(1)
   - Rooted_Tree* SCC() const - O(#nodes + #edges)
   - Rooted_Tree* BFS(Graph_Node* source) const - O(#nodes + #edges)
