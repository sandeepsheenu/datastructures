#implementation of singlr linked list inside stack

class node:
    def __init__(self,data):
        self.data=data
        self.next=None
class stackll_ele:
    def __init__(self):
        self.head=None
           

    def push(self,ele):
        if self.head == None:
            self.head=node(ele)
        else:
            newnode=node(ele)
            newnode.next=self.head
            self.head=newnode
#display method 
# 
    def display(self):
        if self.head==None:
            print("no elements")
        else:
            temp=self.head
            while temp:
                print(temp.data,end=" ")  
                temp=temp.next
            print()

#length in stack linked list
    def length_stackll(self):
        if self.head==None:
            print("no elements")
        else:
            temp=self.head
            cnt=0
            while temp:
                temp=temp.next
                cnt+=1
            print("no of elements present in stackll=",cnt) 

#top of element 
    def top_element(self):
        if self.head==None:
            print(" no elements")
        else:
            res=self.head.data
            return res

# pop element
    def pop_element(self):
        if self.head==None:
            print(" no elements")
#sandeep logic            
        # else:
        #     temp=self.head
        #     self.head=self.head.next 
        #     print(self.head.data)  
# rahul sir logic
        else:
            res=self.head.data
            self.head=self.head.next
            return res

# finding the element in stackll

    # def find_ele(self,ele):
    #     if self.head==None:
    #         print(" no elements")
    #     else:
    #         temp=self.head
    #         while temp.next !=None:
    #             if ele==temp.next.data:
    #                 print("ele_present",ele)
    #             else:
    #                 print(" not present")    

    def search_ele(self,ele):
        if self.head==None:
            print(" no elements")

        else:
            temp=self.head
            cnt=0
            while temp:
                cnt+=1
                if temp.data ==ele:
                    return"element found"
                temp=temp.next
            return "element not found`"        


        


         








s_ll=stackll_ele()
s_ll.push(10)
s_ll.push(20)
s_ll.push(30)
s_ll.display()
s_ll.length_stackll()
print(s_ll.top_element())
s_ll.display()
# s_ll.pop_element()
print("removed element is -->",s_ll.pop_element())
s_ll.display()
print(s_ll.search_ele(20))
print(s_ll.search_ele(60))
s_ll.display()

