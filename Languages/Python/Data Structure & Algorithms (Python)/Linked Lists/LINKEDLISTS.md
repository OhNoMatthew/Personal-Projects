** Linked Lists **

Though, both Arrays and Linked Lists are stored in memory, they both operate fairly differently.

Arrays:
- An existing data structure in the programming language
- Fixed size in memory
- Elements, or nodes, are stored right after each other in memory (contiguously)
- Memory usage is low
  (each node only contains data, no links to other nodes)
- Elements, or nodes, can be accessed directly (random access)
- Elements, or nodes, can be inserted or deleted in constant time, no shifting operations in memory needed.

Linked Lists:
- Linked lists are not allocated to a fixed size in memory like arrays are, so linked lists do not require to move the whole list into a larger memory space when the fixed memory space fills up, like arrays must.
- Linked list nodes are not laid out one right after the other in memory (contiguously), so linked list nodes do not have to be shifted up or down in memory when nodes are inserted or deleted.
- Linked list nodes require more memory to store one or more links to other nodes. Array elements do not require that much memory, because array elements do not contain links to other elements.
- Linked list operations are usually harder to program and require more lines than similar array operations, because programming languages have better built in support for arrays.
- We must traverse a linked list to find a node at a specific position, but with arrays we can access an element directly by writing myArray[5].

Types of Linked Lists:

1. Singly linked lists
2. Doubly linked lists
3. Circular linked lists


Linked List Operations
Basic things we can do with linked lists are:

1. Traversal
2. Remove a node
3. Insert a node
4. Sort