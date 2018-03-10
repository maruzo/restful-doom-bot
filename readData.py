from request import get


#-----------------------------------------------------------------------------------------

#preliminary functions that read the json and formats it into a list

#format of output
#currentPlayerDetails goes [id, health, angle [x-coord, y-coord], currentWeaponID]
#enemyDetails goes [[id, health, angle [x-coord, y-coord], currentWeaponID]
#put the IDs in the wrapper function as ints


def getPlayerDetails():

    returnData = []
    xy = []
    data = get("/api/player")

    xy.append(data["position"]["x"])
    xy.append(data["position"]["y"])

    returnData.append(data["id"])
    if data["health"] < 0:
        returnData.append(0)
    else:
         returnData.append(data["health"])
    returnData.append(data["angle"])
    returnData.append(xy)
    returnData.append(data["weapon"])


    return returnData
def getEnemyDetails(currentPlayerID):
    returnData = []
    data = get("/api/players")

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
            eachEnemy.append(data["weapon"])
            returnData.append(eachEnemy)

    return returnData
#-----------------------------------------------------------------------------------------
#nicer functions that return the said data by an ID

def getCoordsByID(ID, details):
    for i in range(len(details)):
        if(details[i][0] == ID):
            return(details[i][3])

def getHealthByID(ID, details):
    for i in range(len(details)):
        if(details[i][0] == ID):
            return(details[i][1])

def getAngleByID(ID, details):
    for i in range(len(details)):
        if(details[i][0] == ID):
            return(details[i][2])

#-----------------------------------------------------------------------------------------
# Function that returns the current weapon ID

def getCurrentWeaponID(ID, details):
    for i in range(len(details)):
        if(details[i][0] == ID):
            return(details[i][3])
    
#-----------------------------------------------------------------------------------------


if __name__ == "__main__":
    currentPlayerDetails = getPlayerDetails("6001")
    enemyDetails = getEnemyDetails("6001", currentPlayerDetails[0])
    allDetails = enemyDetails
    allDetails.append(currentPlayerDetails)
    print(getAngleByID(110, allDetails))
