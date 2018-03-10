from request import get


#-----------------------------------------------------------------------------------------

#preliminary functions that read the json and formats it into a list

#format of output
#currentPlayerDetails goes [id, health, angle, [x-coord, y-coord], currentWeaponID, [ammo]]
#enemyDetails goes [[id, health, angle, [x-coord, y-coord], currentWeaponID, [ammo]]
#put the IDs in the wrapper function as ints


def getPlayerDetails():

    returnData = []
    xy = []
    ammo = []
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
    returnData.append(list(data["ammo"].values()))

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
            eachEnemy.append(data[i]["weapon"])
            eachEnemy.append(data[i]["ammo"])
            eachEnemy.append(list(data[i]["ammo"].values()))
            returnData.append(eachEnemy)

    return returnData
#-----------------------------------------------------------------------------------------
#Get info about all objects
#[[id, type,[x, y], distance]]

def getObjectsDetails(currentPlayerID):
    returnData = []
    data = get("/api/world/objects")

    for i in range(len(data)):
        eachEnemy = []
        eachEnemyXY = []
        if data[i]["id"] != currentPlayerID:
            eachEnemy.append(data[i]["id"])
            eachEnemy.append(data[i]["type"])
            eachEnemyXY.append(data[i]["position"]["x"])
            eachEnemyXY.append(data[i]["position"]["y"])
            eachEnemy.append(eachEnemyXY)
            eachEnemy.append("distance")
            returnData.append(eachEnemy)

    return returnData

#-----------------------------------------------------------------------------------------
#Get info about one objects
#[[id, type,[x, y], distance]]

def getObjectDetails(objectID):
    returnData = []
    data = get("/api/world/objects")

    for i in range(len(data)):
        eachEnemy = []
        eachEnemyXY = []
        if data[i]["id"] == objectID:
            eachEnemy.append(data[i]["id"])
            eachEnemy.append(data[i]["type"])
            eachEnemyXY.append(data[i]["position"]["x"])
            eachEnemyXY.append(data[i]["position"]["y"])
            eachEnemy.append(eachEnemyXY)
            eachEnemy.append("distance")
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
            return(details[i][4])

#-----------------------------------------------------------------------------------------

def getCurrentAmmoDetails(ID, details):
    for i in range(len(details)):
        if(details[i][0] == ID):
            return(details[i][5])

#-----------------------------------------------------------------------------------------


if __name__ == "__main__":
    currentPlayerDetails = getPlayerDetails()
    enemyDetails = getEnemyDetails(currentPlayerDetails[0])
    allDetails = enemyDetails
    allDetails.append(currentPlayerDetails)
    print(getCurrentAmmoDetails(110, allDetails))
