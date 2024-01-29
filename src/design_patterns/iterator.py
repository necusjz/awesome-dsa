class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None


class LinkedList:
    def __init__(self, head):
        self.head = head
        self.curr = None

    def __iter__(self):
        self.curr = self.head

        return self

    def __next__(self):
        if self.curr:
            val = self.curr.val
            self.curr = self.curr.next

            return val

        else:
            raise StopIteration
