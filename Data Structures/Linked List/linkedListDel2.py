# delete the node based on the position in linked list
class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next


class LinkedList:
    def __init__(self):
        self.head = None

    def push(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

    def deleteNode(self,pos):
        temp = self.head
        temp_loc = 1
        if temp_loc == pos:
            self.head = temp.next
            temp = None
            return
        while temp is not None:
            if temp_loc == pos:
                break
            prev = temp
            temp = temp.next
            temp_loc += 1
        prev.next = temp.next
        temp = None
        if temp is None:
            return
        if temp.next is None:
            return

    def printList(self):
        temp= self.head
        while temp is not None:
            print(temp.data, end=" ")
            print('---->', end=" ")
            temp = temp.next


ll_obj = LinkedList()

ans = 'y'
while ans == 'y':
    value = input('Enter a value to add in linked list: ')
    ll_obj.push(int(value))
    ans = input('Do you want to add another value?(y/n) ')

print('Linked list: ')
ll_obj.printList()
ll_obj.deleteNode(1)
print('\nUpdated linked list: ')
ll_obj.printList()









