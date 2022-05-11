# class Node:
#     def __init__(self,value):
#         self.next=None
#         self.prev=None
#         self.val=value
# class linkedlist:
#     def __init__(self):
#         self.head=None
#         self.tail=None
#         self.size=0
#     def add(self,val):
#         node=Node(val)
#         if self.tail is None:
#             self.head=node
#             self.tail=node
#             self.size+=1
#         else:
#             self.tail.next=node
#             node.prev=self.head
#             self.tail=node
#             self.size+=1
#
#     def __str__(self):
#         vals=[]
#         node=self.head
#         while node is not None:
#             vals.append(node.val)
#             node=node.next
#         return f"[{','.join(str(val) for val in vals)}]"
# my_list=linkedlist()
# my_list.add(1)
# my_list.add(2)
# my_list.add(3)
# print(my_list)

#class iikkkkiiiiiikkiii
class Node:
    def __init__(self,value):
        self.next=None
        self.prev=None
        self.value=value
class linkedlist:
    def __init__(self):
        self.head=None
        self.tail=None
        self.size=0
    def add(self,val):
        node=Node(val)
        #print(node)
        if self.tail is None:
            self.head=node
            self.tail=node
            self.size+=1
        else:
            self.tail.next=node
            node.prev=self.tail
            self.tail=node
            self.size+=1
    def __remove_node(self,node):
        if node.prev is None:
            self.head=node.next
        else:
            node.prev.next=node.next
        if node.next is None:
            self.tail=node.prev
        else:
            node.next.prev = node.prev
    def remove_last(self):
        if self.tail is not None:
            self.__remove_node(self.tail)
    def remove_first(self):
        if self.head is not None:
            self.__remove_node(self.head)
    def remove(self,val):
        node=self.head
        while node is not None:
            if node.value==val:
                self.__remove_node(node)
                break

            node=node.next

    def insert(self,val,pos):
        node=self.head
        c=0
        while node is not None:
            if c==pos:

                    node1=Node(val)
                    self.tail=node1
                    node1.next=node.next
                    node1.prev=node.prev

                    # node1.prev=node
                    # node1.next=node.next

            else:
                self.tail=node
                node=node.next
            c+=1

    def __str__(self):
        vals=[]
        node=self.head
        while node is not None:
            vals.append(node.value)
            node=node.next
        return f"[{','.join(str(val) for val in vals)}]"
my_list=linkedlist()
my_list.add(1)
my_list.add(2)
my_list.add(3)
my_list.add(3)
my_list.insert(9,2)
my_list.add(5)
#my_list.remove_first()
#my_list.remove(1)
#my_list.remove(3)
print(my_list)
# for i in range(int(input())):
#     my_list.add((input()))
# print(my_list)



