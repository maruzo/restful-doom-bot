import actions, random, readData


def attack(objectID, currentPlayerID, distanceLimit, previousDirection = None, futureDirection = None):

    if previousDirection is None:
        previousDirection = random.randint(0,1)

    if futureDirection is None:
        futureDirection = random.randint(0,1)


#    print(readData.getObjectDetails(objectID))
#    if (readData.getObjectDetails(objectID)[3] <= distanceLimit):
#        return previousDirection
    obj = readData.getObjectDetails(objectID)
    if (obj == []):
        return previousDirection
    #stop moving if I am too close
    if (obj[3] < 70):
        return [previousDirection, obj[3]]

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
         actions.forward(10)
    else:
        actions.strafeRight(10)
        actions.forward(10)

    return [futureDirection, obj[3]]
