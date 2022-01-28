# delete Nodes from Linked list
# created by: Preeti Malik

# node class
class Node:
    def __init__(self, data = None, next =None):
        self.data = data
        self.next = next


class LinkedList:
    # initiating the head
    def __init__(self):
        self.head = None

    # entering new node at the beginning of linked list
    def push(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

    # deleting the node from linked list
    def deleteNode(self, value):
        temp = self.head

        # if value to be deleted is head node
        if temp is not None:
            if temp.data == value:
                self.head = temp.next
                temp = None

        # if value to be deleted is another nodes
        while temp:
            if temp.data == value:
                break
            prev = temp
            temp= temp.next
        # if value is not in linked list
        if not temp:
            print('\nValue was not in linked list')
            return
        # delete the node with the value
        prev.next = temp.next
        temp = None

    # traverse and print the list
    def printList(self):
        temp = self.head
        while temp is not None:
            print(temp.data, end=" ")
            print('--->', end=" ")
            temp = temp.next

# create Class object
ll_obj = LinkedList()
# enter elements into linked list
ll_obj.push(7)
ll_obj.push(9)
ll_obj.push(11)
ll_obj.push(13)
ll_obj.push(15)

print('Created linked list is: ')
ll_obj.printList()
# delete node with value 2
ll_obj.deleteNode(2)
# delete node with value
ll_obj.deleteNode(11)
print('\nUpdated Linked list is: ')
ll_obj.printList()





