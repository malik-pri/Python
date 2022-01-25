# IMPLEMENTATION OF LINKED LIST

# creating node class:

class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next


class LinkedList:
    def __init__(self):
        self.head = None

    # add new node at the beginning
    def insert(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

    # add new node after some other node in linked list
    def insertAfter(self, prev_node, new_data):
        if prev_node is None:
            print('Given previous node should exist in the linked list')
            return
        new_node = Node(new_data)
        new_node.next = prev_node.next
        prev_node.next = new_node

    # add a new node at the end of linked list
    def atEnd(self, new_data):
        new_node = Node(new_data)
        if self.head is None:
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node

    # traverse and print the list
    def printList(self):
        temp = self.head
        while temp:  # Till Temp doesn't have Null Value, it will be True
            print(temp.data, end=" ")
            print('---->', end=" ")
            temp = temp.next


# creating a class-object
ll_obj = LinkedList()

# storing data in nodes
ll_obj.head = Node(10)
second = Node(20)
third = Node(30)

# connecting the nodes
ll_obj.head.next = second
second.next = third

# adding new node at beginning
ll_obj.insert(5)
# adding new node between nodes
ll_obj.insertAfter(ll_obj.head.next, 15)     # added after second position(10)
ll_obj.insertAfter(ll_obj.head.next.next.next, 25)     # added after third position(20)
# adding new node at the very end
ll_obj.atEnd(35)

print('The created linked list is: ')
ll_obj.printList()






