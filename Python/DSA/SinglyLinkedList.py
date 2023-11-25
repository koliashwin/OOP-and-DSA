# singly linked list : In this type of linked list, one can move or traverse the linked list in only one direction. where the next pointer of each node points to other nodes but the next pointer of the last node points to NULL.

# this is Node class. this clas contains the structure of every Nodes/elements in linked list
class Node:
    
    def __init__(self, data):
        self.data = data        # node data
        self.next = None        # next pointer

# this is main class for linked list contains all the required functions
class LinkedList:

    def __init__(self):
        self.head = None                # initialize empty linked list
    
    # to dispaly linked list
    def display(self):
        temp = self.head
        while(temp):
            print(temp.data, end=" ")
            temp = temp.next
        print()
    
    # to insert Node at begining
    def add_begining(self, data):
        ele = Node(data)                # creat Node whith given data
        if(self.head):                  # if linkedlist is not empty then point the next pointer to current head Node
            ele.next = self.head
        self.head = ele                 # make current element as head of linked list
    
    # to insert Node at end
    def add_end(self, data):
        ele = Node(data)                # create Node whith given data
        temp = self.head
        while(temp.next):               # traversed at the end of the linked list
            temp= temp.next
        temp.next = ele                 # use the next pointer of last element to point towords recently created Node
    
    # to delete Node at end
    def del_end(self):
        temp = self.head
        if(temp == None):               # if linked list is empty we don't need to do any thing
            return None
        if(temp.next == None):          # if linked list has only one element(i.e. head) then we'll first set next pointer of that element to None
            temp = None
            return None
        while(temp.next.next):          # traverse till second last element of list and then set next pointer of that element to None
            temp = temp.next
        temp.next = None
        return self.display()
    
    # to delete Node at begining
    def del_begin(self):
        temp = self.head
        if(temp == None):               # if linked list is empty we don't need to do any thing
            return None
        self.head = temp.next           # assign 2nd element as head of the linked list
        temp.next = None                # detached first element form linked list
        return self.display()
    
    # to reverse the linked list
    
        #  up until now this will look like follwoing

        #  initial linked list
        # 
        #                   (prev) -------> None
        # 
        #    _____________             _____________             _____________             _____________             _____________             _____________
        #   |    (curr)   |           |             |           |             |           |             |           |             |           |             |
        #   |    Node 1   | --------> |    Node2    | --------> |    Node3    | --------> |    Node4    | --------> |    Node5    | --------> |    Node(N)  |------> None
        #   |_____________|           |_____________|           |_____________|           |_____________|           |_____________|           |_____________|
        # 
        # 
        #         
        # step 1 : we'll point our next pointer towords curr ka next node (i.e Node 2)
        # 
        #            (prev) -------> None
        #    _____________             _____________             _____________             _____________             _____________             _____________
        #   |    (curr)   |           |    (next)   |           |             |           |             |           |             |           |             |
        #   |    Node 1   | --------> |    Node2    | --------> |    Node3    | --------> |    Node4    | --------> |    Node5    | --------> |    Node(N)  |------> None
        #   |_____________|           |_____________|           |_____________|           |_____________|           |_____________|           |_____________|
        # 
        # 
        # step 2 : now we'll point current ka next to prev                                   
        #    _____________             _____________             _____________             _____________             _____________             _____________
        #   |    (curr)   |           |    (next)   |           |             |           |             |           |             |           |             |
        #   |    Node 1   |           |    Node2    | --------> |    Node3    | --------> |    Node4    | --------> |    Node5    | --------> |    Node(N)  |------> None
        #   |_____________|           |_____________|           |_____________|           |_____________|           |_____________|           |_____________|
        #          |
        #          |
        #          V
        #       (prev) -------> None
        # 
        # step 3 : now will assign same node as curr to the prev 
        #  note : curr is pointing towords prev and prev is pointing towords curr
        # 
        #    _____________             _____________             _____________             _____________             _____________             _____________
        #   |    (curr)   |           |    (next)   |           |             |           |             |           |             |           |             |
        #   |    Node 1   |           |    Node2    | --------> |    Node3    | --------> |    Node4    | --------> |    Node5    | --------> |    Node(N)  |------> None
        #   |    (prev)   |           |_____________|           |_____________|           |_____________|           |_____________|           |_____________|
        #   |_______|_____|
        #           |
        #           |
        #           V
        #          None
        # 
        # step 4 : now will assign current to next
        # 
        #    _____________             _____________             _____________             _____________             _____________             _____________
        #   |             |           |    (next)   |           |             |           |             |           |             |           |             |
        #   |    Node 1   | <-------- |    Node2    | --------> |    Node3    | --------> |    Node4    | --------> |    Node5    | --------> |    Node(N)  |------> None
        #   |    (prev)   |           |    (curr)   |           |_____________|           |_____________|           |_____________|           |_____________|
        #   |_______|_____|           |_____________|
        #           |
        #           |
        #           V
        #          None


        # step 5 : repet setp 1 - step 4 for rest of the nodes
        # step 6 : finally set last Node as head
    def reverse(self):
        curr = self.head
        prev = None
        while(curr):
            self.next = curr.next                       
            curr.next = prev                            
            prev = curr
            curr = self.next
        self.head = prev
        return self.display()
    
    # to add Node at perticular position
    def add_pos(self, data, pos): 
        if(pos == 0):
            self.add_begining(data)
        else:
            ele = Node(data)
            temp = self.head
            i = 1
            while(i<pos):
                if(temp.next == None):
                    self.add_end(data)
                    msg = "your provided position is higher, Node added at end of the list"
                    return msg
                else:
                    temp = temp.next
                    i +=1
            ele.next = temp.next.next
            temp.next = ele
    
    # to find NOde into linked list
    def find_ele(self, data):
        temp = self.head
        i=0
        msg = str('no such Node exist in list')
        while(temp):
            if(data == temp.data):
                msg = "Node {} is found at position : {}".format(data, i)
                break
            i += 1
            temp = temp.next
        print(msg)

# driver code
if __name__ =='__main__':
    # create object 
    llist = LinkedList()

    # create some Nodes for linked list
    first = Node(10)
    second = Node("ashiwn")
    third = Node(25.56)

    llist.del_end()
    # connect Nodes 
    llist.head = first
    first.next = second
    second.next = third
    llist.display()

    # test functions
    # add tests
    llist.add_begining(5)
    llist.add_end(45)
    
    # display test
    llist.display()

    # add at index test
    llist.add_pos(100, 0)
    llist.add_pos(200, 2)
    llist.add_pos(300, 25)

    # reversal test
    llist.display()
    llist.reverse()

    # search/find test
    llist.find_ele(200)

    # delete test
    llist.del_end()
    llist.del_begin()