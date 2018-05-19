#  Created by Bogdan Trif on 06-05-2018 , 12:36 AM.

### URL :   http://interactivepython.org/runestone/static/pythonds/Trees/SearchTreeImplementation.html
'''
A binary search tree relies on the property that keys that are less than the parent are found in the left subtree,
and keys that are greater than the parent are found in the right subtree.
We will call this the bst property.
As we implement the Map interface as described above, the bst property will guide our implementation.
Figure 1 illustrates this property of a binary search tree, showing the keys without any associated values.
Notice that the property holds for each parent and child.
All of the keys in the left subtree are less than the key in the root.
All of the keys in the right subtree are greater than the root.
'''

class BinarySearchTree:

    def __init__(self):
        self.root = None
        self.size = 0

    def length(self):
        return self.size

    def __len__(self):
        return self.size

    def __iter__(self):
        return self.root.__iter__()


class TreeNode:
    def __init__(self, key, val, left=None, right=None,  parent=None ):
        self.key = key
        self.payload = val
        self.leftChild = left
        self.rightChild = right
        self.parent = parent

    def hasLeftChild(self):
        return self.leftChild

    def hasRightChild(self):
        return self.rightChild

    def isLeftChild(self):
        return self.parent and self.parent.leftChild == self

    def isRightChild(self):
        return self.parent and self.parent.rightChild == self

    def isRoot(self):
        return not self.parent

    def isLeaf(self):
        return not (self.rightChild or self.leftChild)

    def hasAnyChildren(self):
        return self.rightChild or self.leftChild

    def hasBothChildren(self):
        return self.rightChild and self.leftChild

    def replaceNodeData(self,key,value,lc,rc):
        self.key = key
        self.payload = value
        self.leftChild = lc
        self.rightChild = rc
        if self.hasLeftChild():
            self.leftChild.parent = self
        if self.hasRightChild():
            self.rightChild.parent = self




