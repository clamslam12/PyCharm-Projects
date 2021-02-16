'''
This function imports a text file and converts all numbers into integers and stores them in a list
Input: A list to store the numbers and file name
Output: Returns a list of imported numbers
'''

import bst
import rbTree

#  function given from instructor to read file
def importFile(randL, fname):
    with open(fname, mode="r") as inFile:
        for line in inFile:
            l1 = line.strip('\n').split(" ") # strip \n at every line and split spaces to put in a list
            for i, val in enumerate(l1):
                if val == '\n':
                    l1.remove(val)
            randL.extend(l1)
    # filters out " in list
    randL = list(filter(None, randL))
    # converts str to int for every element in list
    for i, val in enumerate(randL):
        j = int(val)
        randL[i] = j
    return randL

# depth of tree
def rb_getHeight(root):
    return 1 + max(rb_getHeight(root.left) if root.left is not None else 0,
                   rb_getHeight(root.right) if root.right is not None else 0)

# number of nodes in tree
def rb_countNodes(root) :

    if root is None:
        return 0
    else:
        if root.left is not None  and root.right is not None :
            return rb_countNodes(root.left) + rb_countNodes(root.right) + 1
        elif root.left is None and root.right is not None :
            return rb_countNodes(root.right) + 1
        elif root.right is  None and root.left is not None:
            return rb_countNodes(root.left) + 1
        else :
            return 1

randL = []
randL = importFile(randL,"rand1000000.txt")
print(len(randL))

# create a node instance
tree = bst.Node(randL[0])
tree2 = bst.Node(randL[0]) # tree for printing out 1000 nodes in english format
# insert node to tree
for i in randL :
    # print(i)
    tree.insert(i)
for i in randL[:1000]:
    tree2.insert(i)
print(tree2.countNodes())

# print tree like as tree
tree.print_tree()
# print tree in descending order with yield
for i in tree2.descanding() :
    print(i)
# print height
print(tree.getHeight())
# print number of node
print(tree.countNodes())




# RBTree

rbTree = rbTree.RedBlackTree()
for i in randL :
     rbTree.insert(i)

# print number of node
print(rbTree.countNodes())

# print height
print(rbTree.getHeight())