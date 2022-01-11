class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.nextNode = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.numOfNodes = 0

    def insert_new(self, data):
        self.numOfNodes += 1
        new_node = Node(data)

        if not self.head:
            self.head = new_node
        else:
            new_node.nextNode = self.head
            self.head = new_node

    def insert_to_end(self, data):
        self.numOfNodes += 1
        new_node = Node(data)
        actual_node = self.head

        while actual_node.nextNode is not None:
            actual_node = actual_node.nextNode

        actual_node.nextNode = new_node

    def remove(self, data):
        if self.head is None:
            return

        actual_node = self.head
        previous = None

        while actual_node is not None and actual_node.data != data:
            previous = actual_node
            actual_node = actual_node.nextNode

        if actual_node is None:
            return

        if previous is None:
            self.head = actual_node.nextNode
        else:
            previous.nextNode = actual_node.nextNode

    @property
    def get_size(self):
        return self.numOfNodes

    def traverse(self):
        actual = self.head
        while actual is not None:
            print(actual.data)
            actual = actual.nextNode


if __name__ == "__main__":
    t = LinkedList()
    t.insert_new(1)
    t.insert_new(10)
    print(t.get_size)
    t.traverse()
