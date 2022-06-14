from collections import Iterable
# class Node(object):
#     def __init__(self, data):
#         self.data = data
#         self.next = None
#
#

# class NodeLinkIterator(object):
#     """docstring for NodeLinkIterator"""
#
#     def __init__(self, first_node):
#         self.cur = first_node
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         if self.cur:
#             old_data = self.cur.data
#             self.cur = self.cur.next
#             return old_data
#         else:
#             raise StopIteration
#
#
# class NodeLink(object):
#     """docstring for NodeLink"""
#
#     def __init__(self, datas):
#         self.data = datas
#         cur = Node(datas[0])
#         self.__head = cur
#         for i in datas[1:]:
#             new_node = Node(i)
#             cur.next = new_node
#             cur = new_node
#
#     def __iter__(self):
#         return NodeLinkIterator(self.__head)
#
#     def __str__(self):
#         return "这是一个链表, 存储的数据是:" + str(self.data)
#
#
# a = NodeLink(["apple","qweed","qefqf","qwxef"])
#
# for i in a:
#     print(i)
# print(a)