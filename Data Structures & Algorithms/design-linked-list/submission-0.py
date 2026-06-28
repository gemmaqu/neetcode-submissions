class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class MyLinkedList:

    def __init__(self):
        self.first = ListNode(0)
        self.size = 0

    def get(self, index: int) -> int:
        if index >= self.size or index < 0:
            return -1
        count = 0
        curr = self.first.next # we need to land AT the node
        while curr != None:
            if count == index:
                return curr.val
            curr = curr.next
            count += 1
        return -1

    def addAtHead(self, val: int) -> None:
        new_node = ListNode(val)
        new_node.next = self.first.next
        self.first.next = new_node
        self.size += 1

    def addAtTail(self, val: int) -> None:
        new_node = ListNode(val)
        curr = self.first
        while curr.next != None:
            curr = curr.next
        curr.next = new_node
        self.size += 1

    def addAtIndex(self, index: int, val: int) -> None:
        if index > self.size:
            return 
        if index < 0:
            index = 0

        new_node = ListNode(val)
        curr = self.first # need to land ONE BEFORE the element
        count = 0
        while curr != None:
            if count == index: #will stop at the element BEFORE the element!
                originalnext = curr.next
                curr.next = new_node
                new_node.next = originalnext
                self.size += 1
                return

            curr = curr.next
            count += 1

    def deleteAtIndex(self, index: int) -> None:
        if index >= self.size or index < 0:
            return
        curr = self.first
        count = 0
        while curr != None:
            if count == index: #same as above!
                curr.next = curr.next.next
                self.size -= 1
                return
            curr = curr.next
            count += 1