"""
2. Add Two Numbers
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.
"""


class ListNode:
    """Definition for singly-linked list."""
    def __init__(self, x):
        self.val = x
        self.next = None


def to_number(l):
    ln = l
    num, i = 0, 0
    num += ln.val
    while ln.next:
        ln = ln.next
        i += 1
        num += 10 ** i * ln.val
    return num


def to_list_node(num):
    list_nodes = []
    for i in str(num)[::-1]:
        list_nodes.append(ListNode(i))

    for index, val in enumerate(list_nodes):
        if index < len(list_nodes) - 1:
            list_nodes[index].next = list_nodes[index + 1]

    return list_nodes[0]

        
def addTwoNumbers(l1, l2):
    num1, num2 = to_number(l1), to_number(l2)  
    return to_list_node(num1 + num2)


ln1 = [ListNode(2), ListNode(4), ListNode(3)]
ln1[1].next = ln1[2]
ln1[0].next = ln1[1]


ln2 = [ListNode(5), ListNode(6), ListNode(4)]
ln2[1].next = ln2[2]
ln2[0].next = ln2[1]
print(addTwoNumbers(ln1[0], ln2[0]))
