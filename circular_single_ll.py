class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
class circular_single_ll:
    def __init__(self):
        self.head = None

    # insertion at last
    def insert_at_last(self,ele):
        if self.head == None:
            self.head = Node(ele)
            self.head.next = self.head
        else:
            newnode = Node(ele)
            temp = self.head
            while temp.next != self.head:
                temp = temp.next
            temp.next = newnode
            newnode.next =self.head

    # display elements in circular linked list
    def display(self):
        if self.head == None:
            print("No elements in the linked list")
        else:
            temp =self.head
            while temp:
                print(temp.data,end=" -> ")
                temp = temp.next
                if temp == self.head:
                    break
        print()

    # length of the cicular linked list
    def length_ll(self):
        if self.head == None:
            print("No elements in the liknked list")
        else:
            temp = self.head
            cnt = 0
            while temp:
                cnt += 1
                temp = temp.next
                if self.head == temp:
                    break
            print("Total elements presents in the linked list is -> ",cnt)

    # insert at the beggining
    def insert_at_beggining(self,ele):
        if self.head == None:
            self.head = Node(ele)
            self.head.next = self.head

        else:
            newnode = Node(ele)
            temp = self.head
            while temp.next != self.head:
                temp =temp.next
            temp.next = newnode
            newnode.next = self.head
            self.head = newnode

    # insert at the specified location
    def insert_at_loc(self,ele,loc):
        newnode = Node(ele)
        if self.head == None:
            self.head = Node(ele)
            self.head.next =self.head

        elif loc == 1:
            temp = self.head
            while temp.next != self.head:
                temp = temp.next
            temp.next = newnode
            newnode.next = self.head
            self.head = newnode
        else:
            temp = self.head
            cnt = 1
            while temp and cnt < loc -1:
                cnt += 1
                temp = temp.next
            newnode.next = temp.next
            temp.next = newnode

    # delete at last 
    def delete_at_last(self):
        if self.head == None:
            print("No elements in kinked list")
        else:
            temp = self.head
            while temp.next.next != self.head:
                temp = temp.next
                res = temp.next.data
            temp.next = self.head
            return res

    #delete at begginig
    def delete_at_begginig(self):
        if self.head == None:
            print("No elements in kinked list")

        elif self.head.next == self.head:
            self.head.next = None
            self.head = None
        else:
            temp = self.head
            while temp.next != self.head:
                temp = temp.next
            self.head = self.head.next
            temp.next = self.head              
        
cll=circular_single_ll()
while True:
    print("1.Insert the elements at last\n 2.Insert the elements at beggining\n 3.Insert the elements at specific location\n 4.Display likedlist\n 5.Lenght of linked list\n 6. Delete at last\n 7.Delete at begginig")
    opt = int(input("Enter the option:"))
    match opt:
        case 1:
            val = input("Insert the elements at last ->")
            cll.insert_at_last(val)
        case 2:
            val = input("Insert the elements at begginig ->")
            cll.insert_at_beggining(val)
        case 3:
            val = input("Insert the element->")
            val1 = int(input("Select the location in integer must be grater then 0 ->"))
            cll.insert_at_loc(val,val1)
        case 4:
            cll.display()
        case 5:
            cll.length_ll()
        case 6:
            print("Removed Element is -> ", cll.delete_at_last())
        case 7:
            print("Removed Element is -> ", cll.delete_at_begginig())
        case _:
            exit()