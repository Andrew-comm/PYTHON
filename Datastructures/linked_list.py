class Node:
    def __init__(self, data=None, next=None) :

        self.data = data
        self.next = next #pointer to the next element

class Linked_list:
    def __init__(self):
        self.head = None  #points to the head of the linked list

    def insert_at_beginning(self, data): #takes data values and insert at the beginning of the linked list
        node = Node(data, self.head)
        self.head = node

    def print(self): #utility function to print linked list
     if self.head is None:
        print("linked list is empty")
        return


     itr = self.head
     llstr = ''

     while itr:
        llstr += str(itr.data) + '---->'
        itr = itr.next

     print(llstr)


    def insert_at_end (self, data):
     if self.head is None:
        self.head = Node(data,None)
        return

     itr = self.head

     while itr.next:
        itr =itr.next

     itr.next = Node( data, None)







if __name__ == '__main__':
        ll = Linked_list()
        ll.insert_at_beginning(5)
        ll.insert_at_beginning(10)
        ll.insert_at_beginning(32)
        ll.insert_at_end(78)
        ll.print()






        




