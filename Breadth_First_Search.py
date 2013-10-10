#!/bin/python

#list used to represent the graph
#OOP required
#pretty hard-coded

#graph is represented as "adjacency-list"
graph={}

def breadth_first_search():
    global graph
    #another parallel dictionary for storing the meta-data of the nodes of the graph
    meta_data_graph={}
    for keys in graph.keys() :
        meta_data_graph[keys]={'visited':0}
        #0=node is not visited, 1=node is visited
       
    #initialize queue
    queue=[]
    current_node=1
                      
    queue.append(current_node)
    meta_data_graph[current_node]['visited']=1
    meta_data_graph[current_node].update({'level':0})

    print "Order of nodes in which they were visited : "
    #while queue is not empty, travel the graph
    while queue :
        current_node=queue.pop(0);
	print current_node

        for neighbour_nodes in graph[current_node]:
            if( meta_data_graph[neighbour_nodes]['visited']==0 ) :
                queue.append(neighbour_nodes)
		meta_data_graph[neighbour_nodes]['visited']=1
		meta_data_graph[neighbour_nodes].update({'level':meta_data_graph[current_node]['level']+1 })

    #printing the meta_data_graph to see the levels of each node.
    for node in meta_data_graph.keys() : 
	    print "Node:(", node, ")" , "Level:(", meta_data_graph[node]['level'] ,")"
   
def add_node(node, node_neighbours ):
    global graph
    graph[node]=node_neighbours
 
def main():
    add_node(1, [2,4] )
    add_node(2, [1,3] )
    add_node(3, [2] )
    add_node(4, [1,5,6] )
    add_node(5, [4,6,7] )
    add_node(6, [4,5,7,8] )
    add_node(7, [5,6,8] )
    add_node(8, [7,6] )
 
    breadth_first_search()
 
main()

