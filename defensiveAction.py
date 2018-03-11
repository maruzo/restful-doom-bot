import actions, random, readData


def flee(objectID, currentPlayerID, previousDirection = None, futureDirection = None):

    if previousDirection is None:
        previousDirection = random.randint(0,1)

    if futureDirection is None:
        futureDirection = random.randint(0,1)


#    print(readData.getObjectDetails(objectID))
#    if (readData.getObjectDetails(objectID)[3] <= distanceLimit):
#        return previousDirection
    obj = readData.getObjectDetails(objectID)
    if (obj == []):
        return [previousDirection, 0]

    x = readData.getObjectDetails(objectID)[2][0]
    y = readData.getObjectDetails(objectID)[2][1]
    los = readData.LOS(str(currentPlayerID), str(objectID))

    if (los):
        if(previousDirection == 0):
            futureDirection = 1
        else:
            futureDirection = 0

    if futureDirection == 0:
         actions.strafeLeft(10)
         actions.backward(10)
    else:
        actions.strafeRight(10)
        actions.backward(10)

    return [futureDirection, obj[3]]
