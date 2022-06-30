import random
class Node:
    def __init__(self, val=0, next=None, count=None) -> None:
        self.count = count
        self.val = val
        self.next = next

    def __repr__(self) -> str:
        return f"Node {self.count}"


class LL:
    def __init__(self, Node: Node = None) -> None:
        self.start_node = None
        self.node_count = 0

    def push(self, data=None):
        """
        This function psushes element in the beginning of the linkedlist
        like stack
        """
        # Step 1; Make a new Node
        new_node = Node(val=data, count=self.node_count)
        # Step2: The new node is the new start_node
        if self.start_node is None:
            self.start_node = new_node
        else:
            new_node.next = self.start_node
            self.start_node = new_node
        self.node_count = self.node_count + 1
        return None

    def enque(self, data=None):
        """
        This function adds element from the end of the
        list like a queue
        """

        new_node = Node(val=data, count=self.node_count)
        new_node.next = None
        if self.start_node is None:
            self.start_node = new_node

        temp = self.start_node
        while temp.next != None:
            temp = temp.next
        temp.next = new_node
        self.node_count = self.node_count + 1

    def deque(self):
        """
        This function helps to deque from end of the list
        """
        if self.start_node is None:
            return "The list is empty,nothing to deque"
        elif self.start_node.next is None:
            print("Only one element in the list")
            self.head = None
            return self.head
        else:
            temp = self.start_node
            while temp.next != None:
               # print(repr(temp.next))
                if temp.next.next == None:
                    temp.next = None
                    break
                temp = temp.next

    def pop(self, key=None):
        if self.start_node is None:
            return "The list is empty,nothing to pop"
        elif self.start_node.next == None:
            self.start_node = None
        else:
            self.start_node = self.start_node.next

    def sort(self):
        """
        Example of sorting the Linked List using the worst case 
        bubble sorting
        """
        if self.start_node == None:
            return "List is empty"
        elif self.start_node.next is None:
            return self.start_node.val
        else:
            # start swapping
            i = self.start_node
            j = None
            while i and i.next != None:
                j = i.next
                while j:
                    if i.val > j.val:
                        i.val, j.val = j.val, i.val
                    j = j.next
                i = i.next

    def reverse(self):
        if self.start_node is None:
            return "List is empty"
        elif self.start_node.next is None:
            pass
        else:
            current_node=self.start_node
            next_node=None
            prev_node=None
            while(current_node!=None):
                next_node=current_node.next
                current_node.next=prev_node
                prev_node=current_node
                current_node=next_node
            self.start_node=prev_node

    def print(self):
        temp = self.start_node
        while temp:
            print(temp.val)
            temp = temp.next
        return NotImplemented
    



LL = LL()
LL.push(20)
LL.push(31)
LL.push(8)
LL.enque(9)
LL.enque(60)
LL.push(79)
LL.deque()
LL.pop()
LL.sort()
LL.reverse()
LL.print()
