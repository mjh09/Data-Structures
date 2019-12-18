class sll_node:
    def __init__(self, value):
        self.value = value
        self.next = None

class SingleLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    def add_to_head(self,value):
        current = self.head
        self.head = sll_node(value)
        self.head.next = current
    def get_mid(self):
        