class HashNode:  # chaining with linked list
    def __init__(self, key=None, value=None):
        self.key = key
        self.value = value
        self.next = None


class HashTable:
    def __init__(self):
        self.size = 997
        self.buckets = [HashNode()] * self.size  # sentinel

    def insert(self, key, value):
        idx = key % self.size

        head = self.buckets[idx]
        while head.next:
            if head.next.key == key:
                head.next.value = value

                return

            head = head.next

        head.next = HashNode(key, value)

    def get(self, key):
        idx = key % self.size

        head = self.buckets[idx]
        while head.next:
            if head.next.key == key:
                return head.next.value

            head = head.next

    def remove(self, key):
        idx = key % self.size

        head = self.buckets[idx]
        while head.next:
            if head.next.key == key:
                head.next = head.next.next

                return

            head = head.next
