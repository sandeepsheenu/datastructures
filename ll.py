class Node:
    def __init__(self,data):
        self .data=data
        self.next=None
class singlell:
        def __init__(self):
            self.head=None

        def insert_ele(self,value):
            newNode =Node(value)
            if self.head:
                temp=self.head
                while temp.next:
                    temp=temp.next
                temp.next=newNode
            else:
                self.head=newNode

        def display(self):
            if self.head ==None:
                return "no element present inthe linked list"
            else:
                temp=self.head
                while temp:
                    print(temp.data,end="-->")
                    temp=temp.next
                print()

        def length_ll(self):
            if self.head == None:
                print("no element in single linked list")
            else:
                temp = self.head
                cnt=0
                while temp != None:
                    cnt += 1
                    temp = temp.next
                print("total elements",cnt)




sll=singlell()
sll.insert_ele(10)
sll.insert_ele(20)
sll.insert_ele(30)
sll.display()
sll.insert_ele(40)
sll.insert_ele(50)
sll.length_ll()
