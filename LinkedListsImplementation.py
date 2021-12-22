# Secon Commit

class Node: # create a node, set value to value and pointer to None.
    def __init__(self, value): # constructor to create a node
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self, value):
        # create a new Node by calling the class LinkedList and passing the value
        new_node = Node(value) # creates a node (new_node) with a .value and .next property
        self.head = new_node 
        self.tail = new_node
        self.lenght = 1 # sets the .lenght of the class' instance to 1.

    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next

    def append(self, value): # method to append value to a LinkedList
        new_node = Node(value) # create a new node (instance fo the Node class)
        if self.head is None: # if list is empty, point head and tail to the new node.
            self.head = new_node # point head to the new_node (instance of the Node class)
            self.tail = new_node # point tail to the new_node (instance of the Node class)
        else:
            self.tail.next = new_node
            self.tail = new_node # moves the tail over
        self.lenght += 1
        return True # not neccessary because it's a stand alone method.

    def prepend(self, value): # method to append a value in the begnning of a LL
        new_node = Node(value) # creates the node
        if self.lenght == 0: # empty list
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.lenght += 1
        return True

    def popfirst (self):
        if self.lenght == 0:
            return None
        elif self.lenght == 1:
            self.head = None
            self.tail = None
            return self.

    def pop(self):
        if self.lenght == 0: # empty list
            return None
        temp = self.head
        pre = self.head
        while (temp.next is not None): # test if temp is pointing to a node
            pre = temp # move pre up
            temp = temp.next # move temp over, temp is always one node over
        self.tail = pre
        self.tail.next = None #breaks the Linked List
        self.lenght -= 1 # decreases the lenght of the LL
        if self.lenght == 0: # after it is decremented
            self.head = None # point head to None
            self.tail = None # poits tail to None
        return temp.value


my_linked_list = LinkedList(2)

my_linked_list.append(3)

my_linked_list.prepend(1)

my_linked_list.print_list()