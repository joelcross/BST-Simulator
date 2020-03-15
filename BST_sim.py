# AUTHOR: Joel Cross

# This program uses a binary search tree class along with other 
# class functions to manipulate tree data.

# FUNCTIONS: Search, Insert, Delete, SearchPath,
# CountDepth, CountVertices, AverageDepth, MaxDepth

import random

# creates binary tree vertex object
class BinaryTreeVertex:
    def __init__(self, value, left, right):
        self.value = value # an integer value
        self.left_child = left #  pointer to another BinaryTreeVertex object
        self.right_child = right #  pointer to another BinaryTreeVertex object

# creates binary search tree object
class BinarySearchTree:
    def __init__(self):
        self.root = None # pointer to a BinaryTreeVertex object

    # searches for a value in the binary tree
    def Search(self, x):
        current = self.root # current is a BinaryTreeVertex pointer

        while current != None:
            if current.value == x: # value found
                return current
            elif current.value > x: # current value is too big
                current = current.left_child # move to left child
            else: # current value is too small
                current = current.right_child # move to right child
            return None # x is not in the set

    # calls Rec_Insert() to insert value into tree
    def Insert(self, x):
        self.root = self.Rec_Insert(self.root, x)

    # inserts a value into its proper position in the tree
    def Rec_Insert(self, current, x):
        if current == None: # root is empty
            return BinaryTreeVertex(x, None, None) # insert value at root
        elif current.value == x: # check if value is already in the tree
            print(x , "already exists in the tree! Cannot insert.")
            return current
        elif current.value >= x:
            # move to left child
            current.left_child = self.Rec_Insert(current.left_child, x)
        else:
            # move to right child
            current.right_child = self.Rec_Insert(current.right_child, x)
        return current

    # calls Rec_Delete() to delete value from tree
    def Delete(self, x):
        self.root = self.Rec_Delete(self.root, x)

    # deletes a value from the tree
    def Rec_Delete(self, current, x):
        if current == None: # root is empty
            # check if value is actually in the tree
            print(x , " is not in the tree! Cannot delete.")
            return current # case where x is not present in tree
        else:
            if current.value < x:
                # move to right child
                current.right_child = self.Rec_Delete(current.right_child, x)
                return current
            elif current.value > x:
                # move to left child
                current.left_child = self.Rec_Delete(current.left_child, x)
                return current
            else: # value found in tree
                if current.left_child == None:
                    return current.right_child
                elif current.right_child == None:
                    return current.left_child
                else:
                    # now need to fix left subtree
                    tmp = self.Fix_Left_Subtree(current)
                    tmp.right_child = current.right_child
                    return tmp

    # makes largest value in left subtree the root
    def Fix_Left_Subtree(self, v):
        temp = v.left_child # temp is the root of v’s left subtree
        if temp.right_child == None:
            return temp # no fix needed
        else:
            parent = None
            current = temp
            # shuffle around vertices
            while current.right_child != None:
                parent = current
                current = current.right_child
            parent.right_child = current.left_child
            current.left_child = temp
            return current

    # returns a list of all values between the root and a specified value
    def SearchPath(self, current, x):
        if not current: # or 'if not self.root'?  # if the root is empty and there is no tree
            return []
        if current.value == x: # if value is found at root
            return [current.value] # return list holding value at root
        res = self.SearchPath(current.left_child, x)
        if res: # if left child exists
            return [current.value] + res # add child's value to the list
        res = self.SearchPath(current.right_child, x)
        if res: # if left child exists
            return [current.value] + res # add child's value to the list
        return [] # return list of all values in path

    
    # recursive function to calculate total depth between all subtrees
    def Count_Depth(self, current, depth):
        if (current == None): # root is empty
            return 0
        else: # root exists
            # record depth of each subtree
            return depth + self.Count_Depth(current.left_child, depth + 1) + \
                    self.Count_Depth(current.right_child, depth + 1)

    # recursive function to count number of vertices present in tree
    def Count_Vertices(self, current, numVertices):
        if (current == None): # root is empty
            return 0
        
        # add 1 to numVertices each time a new child is traversed
        numVertices += (self.Count_Vertices(current.left_child, numVertices) + \
                        self.Count_Vertices(current.right_child, numVertices))  
        return numVertices

    # calculates average depth based on total depth of tree
    def Average_Depth(self, current):
        # we need the total depth of the tree
        totalDepth = self.Count_Depth(current, 1)
        # we also need the number of nodes in the tree
        totalVertices = self.Count_Vertices(current, 1)

        # calculate average depth
        avgDepth = totalDepth / totalVertices
        return avgDepth

    # calculates the maximum depth of a tree
    def Max_Depth(self, current):
        if current == None: # root is empty
            return 0
        else: # root is not empty
            # Find depth of subtrees
            leftDepth = self.Max_Depth(current.left_child) 
            rightDepth = self.Max_Depth(current.right_child) 
    
            # return larger of the two subtrees
            if (rightDepth < leftDepth): 
                return leftDepth + 1
            else: 
                return rightDepth + 1



### TESTING ###
# create empty tree
tree = BinarySearchTree()

# add random values to tree
tree.Insert(6)
tree.Insert(3)
tree.Insert(17)
tree.Insert(8)
tree.Insert(20)
tree.Insert(7)
tree.Insert(12)
tree.Insert(10)

# search for each value in tree and check its returned SearchPath() val
print("Run SearchPath() function on each value in tree:")
print(tree.SearchPath(tree.root, 6))
print(tree.SearchPath(tree.root, 3))
print(tree.SearchPath(tree.root, 17))
print(tree.SearchPath(tree.root, 8))
print(tree.SearchPath(tree.root, 20))
print(tree.SearchPath(tree.root, 7))
print(tree.SearchPath(tree.root, 12))
print(tree.SearchPath(tree.root, 10))

# test average depth
print()
print("Test Average_Depth() function:")
print(tree.Average_Depth(tree.root))

# test max depth
print()
print("Test Max_Depth() function:")
print(tree.Max_Depth(tree.root))

# delete value 17 and test search path method again
# (ensure the program recognizes that the value has been deleted)
print()
print("Delete value 17 from tree, run SearchPath() on all values again")
tree.Delete(17)
print(tree.SearchPath(tree.root, 6))
print(tree.SearchPath(tree.root, 3))
print(tree.SearchPath(tree.root, 17))
print(tree.SearchPath(tree.root, 8))
print(tree.SearchPath(tree.root, 20))
print(tree.SearchPath(tree.root, 7))
print(tree.SearchPath(tree.root, 12))
print(tree.SearchPath(tree.root, 10))


### EXPERIMENT 1: Binary Search Trees Without Deletion ###
# We will measure the Average Depth and Max Depth of randomly 
# generated Binary Search Trees for data sets of size n.
print()
print("EXPERIMENT 1:")
dataSet = [250, 500, 1000, 2000, 4000, 8000, 16000]
for n in range(len(dataSet)):
    # create lists to store average and max depths for all trees in each n
    avgDepths = []
    maxDepths = []

    # build 500 trees with n values in each
    for i in range (500):
        tree = BinarySearchTree() # new tree
        # generate list of numbers between 1 and n (1-250, 1-500, etc)
        numList = random.sample(range(1, dataSet[n]), dataSet[n]-1)

        # insert all values into tree
        for x in range(len(numList)):
            tree.Insert(numList[x])
        # append average and max depth for current tree to list
        avgDepths.append(tree.Average_Depth(tree.root))
        maxDepths.append(tree.Max_Depth(tree.root))
    
    # find average average depth by taking average value of avgDepths list
    avgAvgDepth = sum(avgDepths) / len(avgDepths)
    # find average max depth by taking average value of maxDepths list
    avgMaxDepth = sum(maxDepths) / len(maxDepths) 

    # find highest value in avgDepth list
    highestAvgDepth = max(avgDepths)
    # find highest value in maxDepth list
    highestMaxDepth = max(maxDepths)

    # print experiment 1 results
    print("For " , dataSet[n] , " vertices:")
    print("Average average depth: " , avgAvgDepth)
    print("Average max depth: " , avgMaxDepth)
    print("Highest average depth: " , highestAvgDepth)
    print("Highest max depth: " , highestMaxDepth)
    print()


### EXPERIMENT 2: Binary Search Trees With Deletion ###
# We will measure the Average Depth and Max Depth of randomly 
# generated Binary Search Trees for data sets of size n, 
# with some values being deleted during the construction sequence.
print()
print("EXPERIMENT 2:")
for n in range(len(dataSet)):
    # create lists to store average and max depths for all trees in each n
    avgDepths = []
    maxDepths = []

    # build 500 trees with n values in each
    for i in range (500):
        tree = BinarySearchTree() # new tree
        # generate list of numbers between 1 and x = 11n/10 (size 11n/10)
        numList = random.sample(range(1, (11*dataSet[n]//10)), (11*dataSet[n]//10)-1)
        # generate list of numbers between 1 and x = 11n/10 (size n/10)
        numList2 = random.sample(range(1, (11*dataSet[n]//10)), (dataSet[n]//10)-1)

        # insert all values  from numList into tree
        for x in range(len(numList)):
            tree.Insert(numList[x])
        # delete n/10 values from tree
        for y in range(len(numList2)):
            tree.Delete(numList2[y])

        # append average and max depth for current tree to list
        avgDepths.append(tree.Average_Depth(tree.root))
        maxDepths.append(tree.Max_Depth(tree.root))
    
    # find average average depth by taking average value of avgDepths list
    avgAvgDepth = sum(avgDepths) / len(avgDepths)
    # find average max depth by taking average value of maxDepths list
    avgMaxDepth = sum(maxDepths) / len(maxDepths) 

    # find highest value in avgDepth list
    highestAvgDepth = max(avgDepths)
    # find highest value in maxDepth list
    highestMaxDepth = max(maxDepths)

    # print experiment 2 results
    print("For " , dataSet[n] , " vertices:")
    print("Average average depth: " , avgAvgDepth)
    print("Average max depth: " , avgMaxDepth)
    print("Highest average depth: " , highestAvgDepth)
    print("Highest max depth: " , highestMaxDepth)
    print()