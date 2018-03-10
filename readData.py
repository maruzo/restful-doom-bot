from request import get

port = 6001

#-----------------------------------------------------------------------------------------

#preliminary functions that read the json and formats it into a list

#format of output
#currentPlayerDetails goes [id, health, angle [x-coord, y-coord]]
#enemyDetails goes [[id, health, angle [x-coord, y-coord]...]
#put the IDs in the wrapper function as ints 


def getPlayerDetails(port):
    returnData = []
    xy = []
    data = get(port, "/api/player")

    xy.append(data["position"]["x"])
    xy.append(data["position"]["y"])

    returnData.append(data["id"])
    if data["health"] < 0:
        returnData.append(0)
    else:
         returnData.append(data["health"])
    returnData.append(data["angle"])
    returnData.append(xy)
    

    
    return returnData
def getEnemyDetails(port, currentPlayerID):
    returnData = []
    data = get(port, "/api/players")

    for i in range(len(data)):
        eachEnemy = []
        eachEnemyXY = []
        if data[i]["id"] != currentPlayerID:
            eachEnemy.append(data[i]["id"])
            if data[i]["health"] < 0:
                eachEnemy.append(0)
            else:
                eachEnemy.append(data[i]["health"])
            eachEnemy.append(data[i]["angle"])
            eachEnemyXY.append(data[i]["position"]["x"])
            eachEnemyXY.append(data[i]["position"]["y"])
            eachEnemy.append(eachEnemyXY)
            returnData.append(eachEnemy)

    return returnData
#-----------------------------------------------------------------------------------------
#nicer functions that return the said data by an ID

def getCoordsByID(ID, details):
    for i in range(len(enemyDetails)):
        if(enemyDetails[i][0] == ID):
            return(details[i][3])

def getHealthByID(ID, details):
    for i in range(len(enemyDetails)):
        if(enemyDetails[i][0] == ID):
            return(deetails[i][1])
        
def getAngleByID(ID, details):
    for i in range(len(enemyDetails)):
        if(enemyDetails[i][0] == ID):
            return(details[i][2])

#-----------------------------------------------------------------------------------------
# Functions that return the nearest health/ammo pack

def getNearestHealthPack(ID):
    pass
def getNearestAmmoPack(ID):
    pass
def getNearestArmour(ID):
    pass

#-----------------------------------------------------------------------------------------
if __name__ == "__main__":
    currentPlayerDetails = getPlayerDetails("6001")
    enemyDetails = getEnemyDetails("6001", currentPlayerDetails[0])
    allDetails = enemyDetails
    allDetails.append(currentPlayerDetails)
    print(getAngleByID(110, allDetails))

