class Node:
    def __init__(self,data):
        self.prev = None
        self.data = data
        self.next = None

class double_ll:
    def __init__(self):
        self.head = None

    # insertion at last 
    def insert_at_last(self,ele):
        if self.head is None:
            self.head = Node(ele)
        else:
            newnode = Node(ele)
            temp = self.head
            while temp.next != None:
                temp = temp.next
            temp.next = newnode
            newnode.prev = temp

    # display
    def display(self):
        if self.head is None:
            print("No elements")
        else:
            temp = self.head
            while temp:
                print(temp.data,end=" <-> ")
                temp = temp.next
            print()

    # length
    def length(self):
        if self.head is None:
            print("No elements")
        else:
            temp = self.head
            cnt = 0
            while temp:
                cnt +=1
                temp = temp.next
            print("Total No of Elements ->",cnt)

    # insert at begging
    def inser_at_begginig(self,ele):
        if self.head is None:
            self.head = Node(ele)
        else:
            newnode = Node(ele)
            newnode.next = self.head
            self.head.prev = newnode
            self.head = newnode
             
    # insert at specific locations
    def insert_at_loc(self,ele,loc):
        if self.head is None:
            self.head = Node(ele)
        elif loc == 1:
            newnode = Node(ele)
            newnode.next = self.head
            self.head.prev = newnode
            self.head = newnode
        else:
            newnode = Node(ele)
            temp = self.head
            cnt = 1
            while temp.next != None and cnt < loc -1:
                cnt += 1
                temp = temp.next
            newnode.prev = temp
            newnode.next = temp.next
            temp.next.prev = newnode
            temp.next = newnode

    # delete at last
    def delete_at_last(self):
        if self.head == None:
            print("No elements in likedlist")
        else:
            temp = self.head
            while temp.next.next != None:
                temp = temp.next
            temp.next = None

    # delete at beggining
    def delete_at_begging(self):
        if self.head == None:
            print("No elements in likedlist")
        else:
            temp = self.head
            self.head = temp.next

    #Delete at specific locations
    def delete_at_loc(self,loc):
        if self.head is None:
            print("No elements in likedlist")
        elif loc == 1:
            temp = self.head
            self.head = temp.next
        else:
            pass

dll=double_ll()
while True:
    print("\n Operations performs on double linked list")
    print(" 1)Insert ele at last\n 2)Insert ele at first\n 3)Insert ele at loc\n 4)Display\n 5)Length\n 6)Delete at last\n 7)Delete at Beggining\n 8)Delete at location\n")
    opt = int(input("Enter your Options ->"))
    match opt:
        case 1:
            val = input("Enter Element ->")
            dll.insert_at_last(val)
        case 2:
            val = input("Enter Element ->")
            dll.inser_at_begginig(val)
        case 3:
            val = input("Enter Element ->")
            loc = int(input("Enter loc ->"))
            dll.insert_at_loc(val,loc)
        case 4:
            dll.display()
        case 5:
            dll.length()
        case 6:
            dll.delete_at_last()
        case 7:
            dll.delete_at_begging()
        case 8:
            loc = input("Enter Location:")
            dll.delete_at_loc(loc)
        case _:
            exit()

