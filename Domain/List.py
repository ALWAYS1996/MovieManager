class CircularList:
    def __init__(self, data):
        self.data = data
        self.nextNode = None
        self.prevNode = None

    def insertAtPoint(self, value):
        global head, tail, nodes

        auxNode = head
        newNode = CircularList(value)

        if head.data is None:
            head = newNode
            tail = newNode
            head.nextNode = tail
            head.prevNode = tail
            tail.nextNode = head
            tail.prevNode = head
            nodes += 1
            return
        elif head.data > newNode.data:
            newNode.nextNode = head
            newNode.prevNode = tail
            head.prevNode = newNode
            tail.nextNode = newNode
            head = newNode
            nodes += 1
            return
        elif tail.data < newNode.data:
            tail.nextNode = newNode
            newNode.nextNode = head
            newNode.prevNode = tail
            head.prevNode = newNode
            tail = newNode
            nodes += 1
            return
        else:
            for x in range(0,nodes):
                if auxNode.data < newNode.data:
                    auxNode = auxNode.nextNode
                else:
                    auxNode = auxNode.prevNode
                    break

            newNode.nextNode = auxNode.nextNode
            auxNode.nextNode = newNode
            newNode.prevNode = auxNode
            newNode.nextNode.prevNode = newNode
            tail = head.prevNode
            nodes += 1
            return

    def insertAtTail(self, value):
        global head, tail, nodes

        auxNode = head
        newNode = CircularList(value)

        if head.data is None:
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
            return
            
    def insertAtHead(self, data):
        global head, tail, nodes
        newNode = CircularList(data)

        if head.data is None:
            head = newNode
            tail = newNode
            head.nextNode = tail
            head.prevNode = tail
            tail.nextNode = head
            tail.prevNode = head
            nodes += 1
            return

        else:
            newNode.nextNode = head
            newNode.prevNode = tail
            head.prevNode = newNode
            tail.nextNode = newNode
            head = newNode
            nodes += 1
            return

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
                return
            elif tail.data == value:
                tail.prevNode.nextNode = tail.nextNode
                tail.nextNode.prevNode = tail.prevNode
                tail = tail.prevNode
                print(value, " deleted")
                nodes -= 1
                return
            else:
                while auxNode.nextNode != head:
                    if auxNode.data == value:
                        auxNode.prevNode.nextNode = auxNode.nextNode
                        auxNode.nextNode.prevNode = auxNode.prevNode
                        print(value, " deleted")
                        nodes -= 1
                        return
                    auxNode = auxNode.nextNode
            print(value, "Not found")
            return
        else:
            print("Cannot delete, the list is empty")
            return

    def updateElement(self, value, newValue):
        auxNode = head
        if nodes == 0:
            print("Cannot update, the list is empty")
            return
        for x in range(0,nodes):
            if value == auxNode.data:
                auxNode.data = newValue
                print("Value updated succesfully")
                return
            else:
                auxNode = auxNode.nextNode
        print("The inserted value doesn't coincide with any Node value")
        return

def printList():
    auxNode = head

    if nodes == 0:
        print("The list is empty")
        return
    elif nodes == 1:
        print("(", tail.data, ")<->", head.data, "<->(", head.data, ")")
        return
    else:
        print("(", tail.data, ")", end="")
        for x in range(0, nodes):
            print("<->", auxNode.data, end=" ")
            auxNode = auxNode.nextNode
        print("<->(", head.data, ")")
        return

head = CircularList(None)
tail = CircularList(None)
nodes = 0