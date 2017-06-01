import Domain.List

medium = Domain.List.CircularList(None, 0)

#Head controllers for the lists
dramaHead = Domain.List.CircularList(None, 1000)
comedyHead = Domain.List.CircularList(None, 2000)
childishHead = Domain.List.CircularList(None, 3000)
actionHead = Domain.List.CircularList(None, 4000)
romanceHead = Domain.List.CircularList(None, 5000)
fictionHead = Domain.List.CircularList(None, 600)

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

def initalizeList(file):
    readFile = open(file, "r+")
    movies = [line.rstrip('\n') for line in readFile]
    readFile.close()

    for x in range(1,len(movies)):
        singleMovie = movies[x].split(",")
        gendre = singleMovie[2]
        if (gendre != "1000"
            and gendre != "2000"
            and gendre != "3000"
            and gendre != "4000"
            and gendre != "5000"
            and gendre != "6000"):
                gendre = singleMovie[3]

        print(gendre)
        #Drama code block
        if singleMovie[2] == "1000":
            medium.insertAtPoint(movies[x], dramaHead, dramaTail, dramaNodes)
            pass
        #Comedy code block
        elif singleMovie[2] == "2000":
            medium.insertAtPoint(movies[x], comedyHead, comedyTail, comedyNodes)
            pass
        #Childish code block
        elif singleMovie[2] == "3000":
            medium.insertAtPoint(movies[x], childishHead, childishTail, childishNodes)
            pass
        #Action code block
        elif singleMovie[2] == "4000":
            medium.insertAtPoint(movies[x], actionHead, actionTail, actionNodes)
            pass
        #Romance code block
        elif singleMovie[2] == "5000":
            medium.insertAtPoint(movies[x], romanceHead, romanceTail, romanceNodes)
            pass
        #Fiction code block
        else:
            medium.insertAtPoint(movies[x], fictionHead, fictionTail, fictionNodes)
            pass

def updateElements(head, tail, nodes):
    if head.identifier == 1000:
        pass