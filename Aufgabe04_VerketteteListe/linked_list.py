import random


class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        if not self.head:
            self.head = Node(data)
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = Node(data)

    def length(self):
        current = self.head
        count = 0
        while current:
            count += 1
            current = current.next
        return count

    def elements(self):
        elements = []
        current = self.head
        while current:
            elements.append(current.data)
            current = current.next
        return elements

    def __iter__(self):
        current = self.head
        while current:
            yield current.data
            current = current.next


def main():
    ll = LinkedList()
    for i in range(10):
        ll.append(random.randint(0, 100))

    print("Length:", ll.length())
    print("Elements:", ll.elements())
    print("Iterator:", [x for x in ll])


if __name__ == "__main__":
    main()