#  Created by Bogdan Trif on 02-08-2018 , 11:42 AM.
# http://interactivepython.org/runestone/static/pythonds/BasicDS/ImplementinganUnorderedListLinkedLists.html
'''
                            ===     3.21. Implementing an Unordered List: Linked Lists      ===


In order to implement an unordered list, we will construct what is commonly known as a linked list.
Recall that we need to be sure that we can maintain the relative positioning of the items.
However, there is no requirement that we maintain that positioning in contiguous memory.
For example, consider the collection of items shown in Figure 1.
It appears that these values have been placed randomly.
If we can maintain some explicit information in each item, namely the location of the next item (see Figure 2),
then the relative position of each item can be expressed by simply following the link from one item to the next.



            ==  3.21.1. The Node Class  ==
The basic building block for the linked list implementation is the node.
Each node object must hold at least two pieces of information.
First, the node must contain the list item itself.
We will call this the data field of the node.
In addition, each node must hold a reference to the next node.
Listing 1 shows the Python implementation.
To construct a node, you need to supply the initial data value for the node.
Evaluating the assignment statement below will yield a node object containing the value 93 (see Figure 3).
You should note that we will typically represent a node object as shown in Figure 4.
The Node class also includes the usual methods to access and modify the data and the next reference.


            ==  3.21.2. The Unordered List Class       ==
As we suggested above, the unordered list will be built from a collection of nodes,
each linked to the next by explicit references. As long as we know where to find the first node (containing the first item),
each item after that can be found by successively following the next links.
With this in mind, the UnorderedList class must maintain a reference to the first node.
Listing 2 shows the constructor.
Note that each list object will maintain a single reference to the head of the list.

'''
class Node:
    def __init__(self,initdata):
        self.data = initdata
        self.next = None

    def getData(self):
        return self.data

    def getNext(self):
        return self.next

    def setData(self,newdata):
        self.data = newdata

    def setNext(self,newnext):
        self.next = newnext


class UnorderedList:

    def __init__(self):
        self.head = None

    def isEmpty(self):
        return self.head == None

    def add(self, item):
        temp = Node(item)
        temp.setNext(self.head)
        self.head = temp

    def size(self):
        current = self.head
        count = 0
        while current != None:
            count = count + 1
            current = current.getNext()

        return count

    def search(self, item):
        current = self.head
        found = False
        while current != None and not found:
            if current.getData() == item:
                found = True
            else:
                current = current.getNext()

        return found

    def remove(self, item):
        current = self.head
        previous = None
        found = False
        while not found:
            if current.getData() == item:
                found = True
            else:
                previous = current
                current = current.getNext()

        if previous == None:
            self.head = current.getNext()
        else:
            previous.setNext(current.getNext())


if __name__ == '__main__':


    mylist = UnorderedList()

    mylist.add(31)
    mylist.add(77)
    mylist.add(17)
    mylist.add(93)
    mylist.add(26)
    mylist.add(54)

    print('size = ',mylist.size())
    print('search : ', mylist.search(93))
    print(mylist.search(100))

    mylist.add(100)
    print(mylist.search(100))
    print(mylist.size())

    print('remove')
    mylist.remove(54)
    print(mylist.size())
    mylist.remove(93)
    print(mylist.size())
    mylist.remove(31)
    print(mylist.size())
    print('search : ', mylist.search(93))
