class Node:
    def __init__(self,data):
        self.prev = None
        self.data = data
        self.next = None

class circular_double_ll:
    def __init__(self):
        self.head = None

    def display(self):
        if self.head == None:
            print("no ele")
        else:
            temp = self.head
            while temp:
                print(temp.data,end=" <-> ")
                temp = temp.next
                if temp == self.head:
                    break
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
                if temp == self.head:
                    break
            print("Total No of Elements ->",cnt)

    # insert at last
    def insert_at_last(self,ele):
        newnode = Node(ele)
        if self.head == None:
            self.head = newnode
            self.head.prev = self.head
            self.head.next = self.head
        else:
            temp = self.head
            while temp.next != self.head:
                temp = temp.next
            temp.next = newnode
            newnode.next = self.head
            newnode.prev = temp
            self.head.prev = newnode

    # insert at beggining
    def insert_at_begging(self,ele):
        newnode = Node(ele)
        if self.head == None:
            self.head = newnode
            self.head.prev = self.head
            self.head.next = self.head
        else:
            temp = self.head
            while temp.next != self.head:
                temp = temp.next
            newnode.next = self.head
            temp.next = newnode
            newnode.prev = temp
            self.head = newnode
            self.head.prev = newnode

            # newnode.next = self.head
            # newnode.prev = self.head.next
            # self.head = newnode

            # temp = self.head
            # self.head.next = newnode
            # newnode.next = self.head
            # newnode.prev = self.head.prev
            # self.head = newnode
            


cc = circular_double_ll()
while True:
    print("\n Operations performs on double linked list")
    print(" 1)Insert ele at last\n 2)Insert ele at first\n 3)Insert ele at loc\n 4)Display\n 5)Length\n 6)Delete at last\n 7)Delete at Beggining\n 8)Delete at location")
    opt = int(input("Enter your Options ->"))
    match opt:
        case 1:
            val = input("Enter Element ->")
            cc.insert_at_last(val)
        case 2:
            val = input("Enter Element ->")
            cc.insert_at_begging(val)
        case 3:
            val = input("Enter Element ->")
            loc = int(input("Enter loc ->"))
        case 4:
            cc.display()
        case 5:
            cc.length()
        case _:
            exit()





