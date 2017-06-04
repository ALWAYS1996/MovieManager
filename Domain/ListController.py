import Domain.List

medium = Domain.List.CircularList(None, 0)

#Head controllers for the lists
dramaHead = Domain.List.CircularList(None, 1000)
comedyHead = Domain.List.CircularList(None, 2000)
childishHead = Domain.List.CircularList(None, 3000)
actionHead = Domain.List.CircularList(None, 4000)
romanceHead = Domain.List.CircularList(None, 5000)
fictionHead = Domain.List.CircularList(None, 6000)

#Tail controllers for the lists
dramaTail = Domain.List.CircularList(None, 0)
comedyTail = Domain.List.CircularList(None, 0)
childishTail = Domain.List.CircularList(None, 0)
actionTail = Domain.List.CircularList(None, 0)
romanceTail = Domain.List.CircularList(None, 0)
fictionTail = Domain.List.CircularList(None, 0)

#Nodes controllers for the lists
dramaNodes = 0
comedyNodes = 0
childishNodes = 0
actionNodes = 0
romanceNodes = 0
fictionNodes = 0

path = ""

def initalizeList(file):
    global path
    path = file
    readFile = open(path, "r+")
    movies = [line.rstrip('\n') for line in readFile]
    readFile.close()

    for x in range(1,len(movies)):

        singleMovie = []
        data = ""
        flag = False

        for y in range(0, len(movies[x])):
            if movies[x][y] == '"':
                flag = not flag
            if movies[x][y] == ",":
                if flag:
                    data += movies[x][y]
                    if data.endswith('"'):
                        data = data[0:-1]
                else:
                    singleMovie.append(data)
                    data = ""
            else:
                data += movies[x][y]
                if data.endswith('"'):
                    data = data[0:-1]
        singleMovie.append(data)

        if singleMovie[2] == "1000":
            medium.insertAtPoint(singleMovie, dramaHead, dramaTail, dramaNodes)
        elif singleMovie[2] == "2000":
            medium.insertAtPoint(singleMovie, comedyHead, comedyTail, comedyNodes)
        elif singleMovie[2] == "3000":
            medium.insertAtPoint(singleMovie, childishHead, childishTail, childishNodes)
        elif singleMovie[2] == "4000":
            medium.insertAtPoint(singleMovie, actionHead, actionTail, actionNodes)
        elif singleMovie[2] == "5000":
            medium.insertAtPoint(singleMovie, romanceHead, romanceTail, romanceNodes)
        else:
            medium.insertAtPoint(singleMovie, fictionHead, fictionTail, fictionNodes)


def updateElements(head, tail, nodes):
    global dramaHead, dramaTail, dramaNodes
    global comedyHead, comedyTail, comedyNodes
    global childishHead, childishTail, childishNodes
    global actionHead, actionTail, actionNodes
    global romanceHead, romanceTail, romanceNodes
    global fictionHead, fictionTail, fictionNodes

    if head.identifier == 1000:
        dramaHead = head
        dramaTail = tail
        dramaNodes = nodes

    elif head.identifier == 2000:
        comedyHead = head
        comedyTail = tail
        comedyNodes = nodes

    elif head.identifier == 3000:
        childishHead = head
        childishTail = tail
        childishNodes = nodes

    elif head.identifier == 4000:
        actionHead = head
        actionTail = tail
        actionNodes = nodes

    elif head.identifier == 5000:
        romanceHead = head
        romanceTail = tail
        romanceNodes = nodes

    else:
        fictionHead = head
        fictionTail = tail
        fictionNodes = nodes

def destroyList():
    global dramaHead, dramaTail, dramaNodes
    global comedyHead, comedyTail, comedyNodes
    global childishHead, childishTail, childishNodes
    global actionHead, actionTail, actionNodes
    global romanceHead, romanceTail, romanceNodes
    global fictionHead, fictionTail, fictionNodes
    global path

    dramaHead = Domain.List.CircularList(None, 1000)
    comedyHead = Domain.List.CircularList(None, 2000)
    childishHead = Domain.List.CircularList(None, 3000)
    actionHead = Domain.List.CircularList(None, 4000)
    romanceHead = Domain.List.CircularList(None, 5000)
    fictionHead = Domain.List.CircularList(None, 6000)

    dramaTail = Domain.List.CircularList(None, 0)
    comedyTail = Domain.List.CircularList(None, 0)
    childishTail = Domain.List.CircularList(None, 0)
    actionTail = Domain.List.CircularList(None, 0)
    romanceTail = Domain.List.CircularList(None, 0)
    fictionTail = Domain.List.CircularList(None, 0)

    dramaNodes = 0
    comedyNodes = 0
    childishNodes = 0
    actionNodes = 0
    romanceNodes = 0
    fictionNodes = 0
    initalizeList(path)