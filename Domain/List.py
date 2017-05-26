class CircularList:
    def __init__(self, data):
        self.data = data
        self.nextNode = None
        self.prevNode = None

    def insertAtTail(self, value):
        global head, tail, nodes

        auxNode = head
        newNode = CircularList(value)

        if head.data == None:
            head = newNode
            tail = newNode
            head.nextNode = tail
            head.prevNode = tail
            tail.nextNode = head
            tail.prevNode = head
            nodes += 1
            return
        else:
            auxNode.prevNode.nextNode = newNode
            newNode.nextNode = auxNode
            newNode.prevNode = auxNode.prevNode
            auxNode.prevNode = newNode
            tail = head.prevNode
            nodes += 1
            return 0
            
    def insertAtHead(self, data):
        global head, tail, nodes
        auxNode = head
        newNode = CircularList(data)

        if head.data == None:
            head = newNode
            tail = newNode
            head.nextNode = tail
            head.prevNode = tail
            tail.nextNode = head
            tail.prevNode = head
            nodes += 1
            return 0

        else:
            newNode.nextNode = head
            newNode.prevNode = tail
            head.prevNode = newNode
            tail.nextNode = newNode
            head = newNode
            nodes += 1
            return 0

    def deleteNode(self, value):
        global nodes, head, tail
        auxNode = head
        if nodes != 0:
            if head.data == value:
                auxNode.prevNode.nextNode = auxNode.nextNode
                auxNode.nextNode.prevNode = auxNode.prevNode
                head = head.nextNode
                print(value, " deleted")
                nodes -= 1
                return 0
            elif tail.data == value:
                tail.prevNode.nextNode = tail.nextNode
                tail.nextNode.prevNode = tail.prevNode
                tail = tail.prevNode
                print(value, " deleted")
                nodes -= 1
                return 0
            else:
                while(auxNode.nextNode != head):
                    if(auxNode.data == value):
                        auxNode.prevNode.nextNode = auxNode.nextNode
                        auxNode.nextNode.prevNode = auxNode.prevNode
                        print(value, " deleted")
                        nodes -= 1
                        return 0
                    auxNode = auxNode.nextNode
            print(value, "Not found")
            return -1
        else:
            print("Cannot delete, the list is empty")
            return -1

    def updateElement(self, value, newValue):
        auxNode = head
        if nodes == 0:
            print("Cannot update, the list is empty")
            return -1
        for x in range(0,nodes):
            if value == auxNode.data:
                auxNode.data = newValue
                print("Value updated succesfully")
                return 0
            else:
                auxNode = auxNode.nextNode
        print("The inserted value doesn't coincide with any Node value")
        return -1

def printList():
    auxNode = head

    if nodes == 0:
        print("The list is empty")
        return -1
    elif nodes == 1:
        print("(", tail.data, ")<->", head.data, "<->(", head.data, ")")
        return 0
    else:
        print("(", tail.data, ")", end="")
        for x in range(0, nodes):
            print("<->", auxNode.data, end=" ")
            auxNode = auxNode.nextNode
        print("<->(", head.data, ")")
        return 0

head = CircularList(None)
tail = CircularList(None)
nodes = 0

medium = CircularList(None)

medium.insertAtTail(5)
printList()
medium.insertAtTail(10)
printList()
medium.updateElement(10,15)
printList()
medium.insertAtHead(30)
printList()
medium.insertAtTail(50)
printList()
medium.deleteNode(30)
printList()
medium.deleteNode(15)
printList()