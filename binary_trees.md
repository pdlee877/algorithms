Binary Trees:

-a tree data structures has a root, branches, and leaves
-the differences between a tree in nature and a tree in computer science
  -is that a tree data structure has its root at the top and its leaves
  -on the bottom
-a second property of trees is that all of the children of one node are
  -independent of the children of another node
-a third property is that each leaf node is unique

example: file system - directories -> folders are structured as a tree
another example: webpage for those familiar with HTML
  -body -> ul -> li or -> h2 -> p

Vocabulary:
Node -
-node is a fundamental part of a tree. It can have a name, which we
  -call the 'key'
-node may also have additional information, called 'payload'
-while the payload information is not central to many tree
  -algorithms, it is often critical in applications that make use of Trees

Edge -
-an edge is another fundamental part of a tree
-an edge connects two nodes to show that there is a relationship
  -between them
-every node(except the root) is connected by exactly one incoming
  -edge from another node
-each node may have several outgoing edges

Root -
-the root of the tree is the only node in the tree that has no
  -incoming edges

Path -
-a path is an ordered list of nodes that are connected by edges
example: Mammal -> Carnivora -> Felidae -> Felis is a Path

Children -
-the set of nodes 'c' that have incoming edges from the same node
  -too are said to be children of that node

Parent -
-a node is the parent of all the nodes it connects to with
  -outgoing edges

Sibling -
-nodes in the tree that are children of the same parent are
  -said to be siblings

SubTree -
-a subtree is a set of nodes and edges comprised of a parent and all the
  -descendants of that parent

Leaf Node -
-a leaf node is a node that has no children

Level -
-the level of a node 'n' is the number of edges on the path from the root
  -node to n

Height -
-the height of a tree is equal to the maximum level of any node in the tree

Full Definition of a Tree:
-a tree consists of a set of nodes and a set of edges that connect pairs
  -of nodes. A tree has the following properties:
    -one node of the tree is designated as the root node
    -every node n, except the root node, is connected by an edge from
      -exactly one other node p, where p is the parent of n
    -a unique path traverses from the root to each node
    -if each node in the tree has a maximum of two children, we say
      -that the tree is a binary tree
