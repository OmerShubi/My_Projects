cmake_minimum_required(VERSION 3.15)
project(Dalgo)

set(CMAKE_CXX_STANDARD 14)

include_directories(.)

add_executable(Dalgo
        main2.cpp
        main_output.txt
        names.txt Graph_Node.cpp Graph_Node.h Graph_Edge.h Rooted_Tree.cpp Rooted_Tree.h Dynamic_Graph.cpp Dynamic_Graph.h Queue.h QueueItem.h Tree_Node.h)
