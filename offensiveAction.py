import actions, random, readData


def attack(objectID, currentPlayerID, futureDirection = None, previousDirection = None):
    x = readData.getObjectDetails(objectID)[3][0]
    y = readData.getObjectDetails(objectID)[3][1]
    los = readData.LOS(currentPlayerID, objectID)
    
    if previousDirection is None:
        previousDirection = random.randint(0,1)
    
    if futureDirection is None:
        futureDirection = random.randint(0,1)


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
        
    return direction




