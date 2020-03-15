# BST-Simulator
This code creates and uses binary search trees to store and operate on sets of integers.

## Classes
### BinaryTreeVertex
Creates a vertex object. These are used to build the binary trees.

### BinarySearchTree
Creates a binary search tree object with a number of functions to manipuate its structure.

## BinarySearchTree Class Functions
### __init__()
Initializes the new tree.

### Search(x)
Searches for a value in the binary tree.

### Insert(x)
Calls the Rec_Insert() function to insert a new value into the tree.

### Rec_Insert(current, x)
Inserts a value into its proper position in the binary tree.

### Delete(x)
Finds and deletes an item from the binary tree.

### Rec_Delete(x)
Calls the Rec_Delete() function to find and delete an item from the tree.

### Fix_Left_Subtree(v)
Fixes the disordered left subtree after a deletion.

### SearchPath(current, x)
Returns a list of all of the values between the root and a specified value.

### Count_Depth(current, depth)
Calculates the total depth of the tree between all of its' subtrees.

### Count_Vertices(current, numVertices)
Counts the number of vertices present in tree.

### Average_Depth(current)
Uses the depth and number of vertices to calculate the tree's average depth.

### Max_Depth(current)
Calculates the maximum depth of the binary tree.

## Experiments
### Binary Search Trees Without Deletion
In this experiment, I measure the Average Depth and Max Depth of randomly generated Binary Search Trees for various data sets of size n.

### Binary Search Trees With Deletion
In this experiment, I again measure the Average Depth and Max Depth of randomly generated Binary Search Trees for various data sets of size n. This time, I delete some values during the construction sequence.

