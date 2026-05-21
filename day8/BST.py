#BST
class BSTNode:
    def __init__(self,data):
        self.data = data
        self.leftChild = None
        self.rightChild = None

def insertNode(rootnode,nodeValue):
    if rootnode.data == None:
        rootnode.data = nodeValue
    elif nodeValue <= rootnode.data:
        if rootnode.leftChild is None:
            rootnode.leftChild = BSTNode(nodeValue)
        else:
            insertNode(rootnode.leftChild,nodeValue)
    else:
        if rootnode.rightChild is None:
            rootnode.rightChild = BSTNode(nodeValue)
        else:
            insertNode(rootnode.rightChild,nodeValue)



def preOrderTraversal(rootnode):
    if not rootnode:
        return
    print(rootnode.data,end=" ")
    preOrderTraversal(rootnode.leftChild)
    preOrderTraversal(rootnode.rightChild)

def inOrderTraversal(rootnode):
    if not rootnode:
        return
    inOrderTraversal(rootnode.leftChild)
    print(rootnode.data,end=" ")
    inOrderTraversal(rootnode.rightChild)


def postOrderTraversal(rootnode):
    if not rootnode:
        return
    postOrderTraversal(rootnode.leftChild)
    postOrderTraversal(rootnode.rightChild)
    print(rootnode.data,end=" ")

def searchNode(rootnode,nodevalue):
    if rootnode.data == nodevalue:
        print("Value is found")
    elif rootnode.data > nodevalue:
        if rootnode.data == nodevalue:
            print("Value is found")
        else:
            if rootnode.leftChild is None:
                print("Not found")
            else:
                searchNode(rootnode.leftChild,nodevalue)
    elif rootnode.data < nodevalue:
        if rootnode.data == nodevalue:
            print("Node found")
        else:
            if rootnode.rightChild is None:
                print("Not found")
            else:
                searchNode(rootnode.rightChild,nodevalue)
            
    else:
        print("Node not found")


newBST = BSTNode(None) 
insertNode(newBST,70)
insertNode(newBST,50)
insertNode(newBST,90)
insertNode(newBST,30)
insertNode(newBST,60)
insertNode(newBST,80)
insertNode(newBST,100)
insertNode(newBST,20)
insertNode(newBST,40)
# print("PreOrder Traversal: ")
# preOrderTraversal(newBST)
# print()
# print("InOrder Traversal: ")
# inOrderTraversal(newBST)
# print()
# print("PostOrder Traversal: ")
# postOrderTraversal(newBST)
# print()

searchNode(newBST,10)