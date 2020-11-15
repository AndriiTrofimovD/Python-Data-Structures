class Node:

    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

    def __repr__(self):
        return str(self.data)


class List:

    def __init__(self, head=None):
        self.head = head
        self.tail = None
        self.size = 0

    def add_first(self, value):
        if not self.head:
            self.head = Node(value)
            self.head.next = None
            self.head.prev = None
            self.tail = self.head
            self.size += 1
        else:
            node = Node(value)
            self.head.prev = node
            node.next = self.head
            self.head = node
            self.size += 1

    def add_last(self, value):
        if not self.head:
            self.add_first(value)
        else:
            node = Node(value)
            self.tail.next = node
            node.prev = self.tail
            self.tail = node
            self.size += 1

    def contains(self, value):
        if self.tail.data == value:
            return True
        else:
            temp = self.head
            while temp:
                if temp.data == value:
                    return True
                else:
                    temp = temp.next
            return False

    def insert_before(self, before, value):
        if self.head.data == before:
            self.add_first(value)
        elif not before:
            self.add_last(value)
        else:
            temp = self.head
            node = Node(value)
            while temp.next:
                if temp.next.data != before:
                    temp = temp.next
                else:
                    temp.next.prev = node
                    node.next = temp.next
                    temp.next = node
                    node.prev = temp
                    return
            print(f'{value} is not in the list.')

    def insert_after(self, after, value):
        if self.tail.data == after:
            self.add_last(value)
        elif not after:
            self.add_first(value)
        else:
            temp = self.head
            node = Node(value)
            while temp:
                if temp.data != after:
                    temp = temp.next
                else:
                    node.next = temp.next
                    node.prev = temp
                    temp.next = node
                    return
            print(f"{value} is not in the list.")

    def clear(self):
        self.head = None
        self.tail = None
        self.size = 0

    def delete_first(self):
        if not self.head:
            print("List is empty.")
        else:
            self.head.next.prev = None
            self.head = self.head.next
            self.size -= 1

    def delete_last(self):
        if not self.head:
            print("List is empty")
        else:
            self.tail.prev.next = None
            self.tail = self.tail.prev
            self.size -= 1

    def delete_value(self, value):
        if self.head.data == value:
            self.delete_first()
            return
        if self.tail.data == value:
            self.delete_last()
            return
        temp = self.head.next
        while temp:
            if temp.data != value:
                temp = temp.next
            else:
                temp.next.prev = temp.prev
                temp.prev.next = temp.next
                self.size -= 1
                return
        print(f"{value} is not in the list.")

    def __repr__(self):
        if not self.head:
            return 'None'
        res = []
        temp = self.head
        while temp:
            res.append(str(temp.data))
            temp = temp.next
        return ' ->/<- '.join(res)
