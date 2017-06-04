import Domain.ListController
class CircularList:

    def __init__(self, data, identifier):
        self.data = data
        self.nextNode = None
        self.prevNode = None
        self.identifier = identifier

    def insertAtPoint(self, data, head, tail, nodes):
        auxNode = head
        newNode = CircularList(data, head.identifier)

        if head.data is None:
            head = newNode
            tail = newNode
            head.nextNode = tail
            head.prevNode = tail
            tail.nextNode = head
            tail.prevNode = head
            nodes += 1
            return Domain.ListController.updateElements(head, tail, nodes)

        elif head.data[1] > newNode.data[1]:
            newNode.nextNode = head
            newNode.prevNode = tail
            head.prevNode = newNode
            tail.nextNode = newNode
            head = newNode
            nodes += 1
            return Domain.ListController.updateElements(head, tail, nodes)

        elif tail.data[1] < newNode.data[1]:
            tail.nextNode = newNode
            newNode.nextNode = head
            newNode.prevNode = tail
            head.prevNode = newNode
            tail = newNode
            nodes += 1
            return Domain.ListController.updateElements(head, tail, nodes)

        else:
            for x in range(0,nodes):
                if auxNode.data[1] < newNode.data[1]:
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
            return Domain.ListController.updateElements(head, tail, nodes)

'''
Extra code
Not tested with the project actual functionality

    def deleteNode(self, data, head, tail, nodes):

        auxNode = head
        if nodes != 0:
            if head.data == data:
                auxNode.prevNode.nextNode = auxNode.nextNode
                auxNode.nextNode.prevNode = auxNode.prevNode
                head = head.nextNode
                print(data, " deleted")
                nodes -= 1
                return Domain.ListController.updateElements(head, tail, nodes)
            elif tail.data == data:
                tail.prevNode.nextNode = tail.nextNode
                tail.nextNode.prevNode = tail.prevNode
                tail = tail.prevNode
                print(data, " deleted")
                nodes -= 1
                return Domain.ListController.updateElements(head, tail, nodes)
            else:
                while auxNode.nextNode != head:
                    if auxNode.data == data:
                        auxNode.prevNode.nextNode = auxNode.nextNode
                        auxNode.nextNode.prevNode = auxNode.prevNode
                        print(data, " deleted")
                        nodes -= 1
                        return Domain.ListController.updateElements(head, tail, nodes)
                    auxNode = auxNode.nextNode
            print(data, "Not found")
            return
        else:
            print("Cannot delete, the list is empty")
            return

    def updateElement(self, data, newData, head, tail, nodes):

        auxNode = data
        if nodes == 0:
            print("Cannot update, the list is empty")
            return
        for x in range(0,nodes):
            if data == auxNode.data:
                auxNode.data = newData
                print("Value updated succesfully")
                return Domain.ListController.updateElements(head, tail, nodes)
            else:
                auxNode = auxNode.nextNode
        print("The inserted value doesn't coincide with any Node value")
        return


    def insertAtTail(self, data, head, tail, nodes):

        auxNode = head
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
            auxNode.prevNode.nextNode = newNode
            newNode.nextNode = auxNode
            newNode.prevNode = auxNode.prevNode
            auxNode.prevNode = newNode
            tail = head.prevNode
            nodes += 1
            return
            
    def insertAtHead(self, data, head, tail, nodes):

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
            
        def printList(self, head, tail, nodes):

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
'''