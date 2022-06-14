class Node(object):
    def __init__(self,data):
        self.data = data
        self.next = None


class LinkIterator(object):
    def __init__(self,head):
        self.temp = head
    def __iter__(self):
        return self
    def __next__(self):
        old_node = self.temp
        if old_node is None:
            raise StopIteration
        else:
            self.temp = self.temp.next
            return old_node


class Link(object):
    """docstring for Link"""
    def __init__(self, data):
        self.head = None
        if data:
            self.temp_node = Node(data[0])
            self.head = self.temp_node
            for i in data[1:]:
                self.temp_node.next = Node(i)
                self.temp_node = self.temp_node.next

    def __iter__(self):
        return LinkIterator(self.head)

    def display(self):
        self.temp = self.head
        while self.temp:
            print("{}->".format(self.temp.data), end="")
            self.temp = self.temp.next
        print("None")
        return

    def linklen(self):
        self.temp=self.head
        t=0
        while self.temp.next:
            t+=1
            self.temp=self.temp.next
        return t

    def insert(self, pos, data):
        self.temp = self.head
        for i in range(pos-1):
            self.temp = self.temp.next
            if self.temp == None:
                print("超出链表长度!!!")
                return False
        new_node = Node(data)
        new_node.next = self.temp.next
        self.temp.next = new_node
        return True

    def delete(self,pos):
        if self.linklen()<=pos:
            print('超出链表长度!!!')
            return False
        self.temp = self.head
        if pos==0:
            self.head=self.temp.next
        elif pos==1:
            if self.temp.next.next:
                self.temp.next = self.temp.next.next
        for i in range(pos-2):
            self.temp = self.temp.next
            if self.temp == None or self.temp.next==None:
                return False
        self.temp.next=self.temp.next.next
        return True

    def change(self,pos,var):
        if self.linklen()<=pos:
            print('超出链表长度!!!')
            return False
        self.temp = self.head
        self.var = Node(var)
        if pos==0:
            self.head=self.temp.next
        elif pos==1:
            if self.temp.next.next:
                self.temp.next = self.temp.next.next
        for i in range(pos-1):
            self.temp = self.temp.next
            if self.temp == None or self.temp.next==None:
                print("超出链表长度!!!")
                return False
        self.var.next = self.temp.next.next
        self.temp.next=self.var
        return True

    def find(self,idex):
        self.temp = self.head
        for i in range(idex-1):
            self.temp = self.temp.next
            if self.temp == None or self.temp.next==None:
                print("超出链表长度!!!")
                return False
        print(self.temp.data)
        return True


# 初始化一个链表
a = Link(range(5))
a.display()


# 添加功能
if a.insert(3,4):
    a.display()

# 删除功能
a.delete(3)
if a.delete(3):
    a.display()

# 查询功能
if a.find(3):
    print(a.find(3))

# 修改功能
a.change(3,6)
if a.delete(3):
    a.display()

# 遍历功能
for i in a:
    i.data += 1
a.display()

# 输出长度动能
print(a.linklen())