# DataStructures_Py
## Tree Data Structure
  + [Basics](https://www.programiz.com/dsa/trees)
  + [Youtube Link](https://www.youtube.com/watch?v=-xJvpnenx6Y&list=PLPdtS77PaSutvrLxZJT5gmASGSed0dO_T)
    * 12.17 list to tree 
  + Topics Covered:
    * Create, insert, delete, display, search node, height of tree.
  + Binary Search Tree:
    * Root has max 2 Childs
    * Value of left side child should have less value compared to root
    * Value of right side child should have greater value or equal to root
    * Node data structure has 3 things, left part, data, right part
  + Creating Node:
    * Attached 
  + [Heap_youtube](https://www.youtube.com/watch?v=HqPJF2L5h9U&t=1007s)
  + Array representation of binary Tree
    * Nodes in a tree are stored level by level from left to right in an array. If an element is missing leave it blank in array
    * If a node is at index -> i
    * It's left child -> 2i
    * It's right child -> 2i+1
    * Its parent -> i/2
    * pow(2,h+1)-1 elements or nodes
    * height of a complete binary tree will be minimum(log n), unless level is filled not going to next stage
    ---
  ### Binary Tree:
  + A binary tree is a tree data structure in which each parent node can have at most two children
  + Types:
  + Full Binary Tree:
    * A full Binary tree is a special type of binary tree in which every parent node/internal node has either two or no children
  + Perfect Binary Tree:
    * A perfect binary tree is a type of binary tree in which every internal node has exactly two child nodes and all the leaf nodes are at the same level.
  + Complete Binary Tree: If you represent the tree in an array there will not be any gaps in between 
    * A complete binary tree is just like a full binary tree, but with two major differences 1) Every level must be completely filled 2)All the leaf elements must lean towards the left. 3)The last leaf element might not have a right sibling i.e. a complete binary tree doesn't have to be a full binary tree.
    ---
  #### Heap
  + Heap is a complete binary tree
  + Max Heap: Root node having greater value or equal than its descendants
  + Min Heap: Root node having minimum value or equal than its descendants
  ##### Insertion in Max Heap:
    * The element will be added in the end of an array or at the leaf node.
    * After added, it will be compared with the parent/ancestor. If value is greater it will be swapped with the parent. check (i/2 element).
    * Adjustment from leaf towards root
    * Time Complexity: swapped elements based on height (height of complete binary tree is log n, so it takes O(log n) time for insertion when inserting max element) or no swapping is required if it is a min value compared to parent (in this case it is O(1))
    * So, time complexity for insertion of element ranges from O(1) - O(log n) 
    * for inserting n elements it is O(n log n)
  ##### Deletion in Max Heap:
    * The root element will be deleted and the last element will take the place of root to maintain the complete binary tree.
    * Swapping will be done downwards (comparing node with child node) to maintain the Max heap
    * Adjustment from root towards leaf
    * TimeComplexity depends on height O(log n)
    * for deleting n elements it is O(n log n)
  + Heap Sort:
    * On deletion of elements from heap, store it in the free space of that array upto length, now array will be in sorted form.
  + Heapify:
    * Will start comparing from last node and compare it with parent node and goes on...
    * Time taken is O(n)
  ##### Max Heap create:
    * To find no of leaf nodes ((n//2)+1) to n.
    * Tp find largest non-leaf nodes (n//2)
## Graph
  * A Graph is a collection of Nodes(V[Vertices]) and edges(E)
  * Types: Directed Graph (If graph associated with direction) [Facebook friends] , Undirected Graph (If graph not associated with direction) [Instagram followers] , Weighted Graph (If all edges are associated with weights) [cities (nodes having distance)]
  * [YoutubeLink](https://www.youtube.com/watch?v=xOL7f4cMAAk&list=PLEFU6wcpJoWKoGu2GrMDvQcne8ETo02bV)
  * Total no of vertices represented as |V| and Total no of edges represented as |E|
  * Graph represented as G=<V,E>
### Representation of graph:
  + Adjacency List 
    * Attached Image (Adjacency_list_Representation)
  + Adjacency matrix
    * For Undirected graph A : A = A^T 
#### For Time and space complexity refer attached
