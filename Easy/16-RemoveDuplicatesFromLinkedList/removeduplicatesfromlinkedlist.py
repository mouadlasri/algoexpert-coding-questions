
#   You're given the head of a Singly Linked List whose nodes are in sorted order
#   with respect to their values. Write a function that returns a modified version
#   of the Linked List that doesn't contain any nodes with duplicate values. The
#   Linked List should be modified in place (i.e., you shouldn't create a brand
#   new list), and the modified Linked List should still have its nodes sorted
#   with respect to their values.
#
#   Each LinkedList node has an integer value as well as a next node pointing to
#   the next node in the list or to None / null if it's the tail of the list.
#
#   Sample Input:
#       linkedList = 1 -> 1 -> 3 -> 4 -> 4 -> 4 -> 5 -> 6 -> 6
#   Sample Output:
#       1 -> 3 -> 4 -> 5 -> 6


# This is an input class. Do not edit.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


def removeDuplicatesFromLinkedList(linkedList):

    # because linkedList is a dictionary, 'curr' references the same dictionary
    # so modifying 'curr' will also modify 'linkedin'
    # if I want to create a copy of linkedList, I'd have to do curr = linkedList.copy()
    curr = linkedList
    
    while(curr.next is not None):
        # print(linkedList.value, end='-')
        if(curr.value == curr.next.value):
            curr.next = curr.next.next
        else:
            curr = curr.next

    return linkedList


# sample linked list
linkedList = LinkedList(1)
linkedList.next = LinkedList(1)
linkedList.next.next = LinkedList(3)
linkedList.next.next.next = LinkedList(4)
linkedList.next.next.next.next = LinkedList(4)
linkedList.next.next.next.next.next = LinkedList(4)
linkedList.next.next.next.next.next.next = LinkedList(5)
linkedList.next.next.next.next.next.next.next = LinkedList(6)
linkedList.next.next.next.next.next.next.next.next = LinkedList(6)

# sample output
linkedList = removeDuplicatesFromLinkedList(linkedList)
# 1-3-4-5-6
# print the linkedin list
curr = linkedList
while(curr.next is not None):
    print(curr.value, end='-')
    curr = curr.next
print(curr.value)
