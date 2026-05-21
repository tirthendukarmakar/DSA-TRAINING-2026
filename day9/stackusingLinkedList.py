class Node:
    def __init__(self,value = None): #(1)
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def __iter__(self):
        curNode = self.head
        while curNode:
            yield curNode
            curNode = curNode.next



class Stack:
    def __init__(self):
        self.LinkedList = LinkedList()
    
    def __str__(self):
        values = [str(x.value) for x in self.LinkedList]
        return '\n'.join(values)

    def isEmpty(self):
        if self.LinkedList.head == None:
            return True
        else:
            return False


    def push(self,value):
        node = Node(value)
        node.next = self.LinkedList.head
        self.LinkedList.head = node

    def pop(self):
        if self.isEmpty():
            return "There is no any element in the stack"
        else:
            nodeValue = self.LinkedList.head.value
            self.LinkedList.head = self.LinkedList.head.next
            return nodeValue
        
    def peek(self):
        if self.isEmpty():
            return "There is not any element in the stack"
        else:
            nodeValue = self.LinkedList.head.value
            return nodeValue
        
    def delete(self):
        self.LinkedList.head = None
        print("Linked List has deleted ")

    def display(self):
        if self.isEmpty():
            print('Stack is empty')
        else:
            print('Display stack again')
            temp = self.LinkedList.head
            while temp is not None:
                temp = temp.next
            print()
            


customStack = Stack()
customStack.push(1)
customStack.push(2)
customStack.push(3)
print(customStack)
print("Display top value")
print(customStack.peek())
print("Pop top element")
print(customStack.pop())
print("Now check stack again")
print(customStack)
print("Pop top element")
print(customStack.pop())
print("Now check the stack again")
print(customStack)
        
        
