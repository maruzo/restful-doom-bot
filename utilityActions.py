
import math
import actions
import readData
import time

'''
constant_errro = 10
def turnAbsAngle(_angle):
	angle = readData.getPlayerDetails()[2]
	while (abs(_angle-angle) >= constant_errro):
		angle = readData.getPlayerDetails()[2]
		turn = _angle - angle
		#turn the other way
		if (abs(_angle-angle) != 0):
			if (abs(_angle-angle) > 180):
				if (turn > 0): #if positive
					actions.turnRight(3)
				else:
					actions.turnLeft(3)
			else:#turn the right way
				if (turn > 0):
					actions.turnLeft(3)
				else:
					actions.turnRight(3)
		time.sleep(10)




def waitUntilTurnFinished():
	angle = readData.getPlayerDetails()[2]
	lastAngle = -1
	while (abs(angle-lastAngle) != 0):
		angle = readData.getPlayerDetails()[2]
		lastAngle = angle
		time.sleep(10)
'''

'''def turnAbsAngle(_angle):
	angle = readData.getPlayerDetails()[2]
	direction = abs(_angle-angle)>180
	while (abs(_angle-angle) >= 5):
		angle = readData.getPlayerDetails()[2]
		if(direction):
			actions.turnLeft(3)
		else:
			actions.turnRight(3)
'''

def turnAbsAngle(_angle):
	angle = readData.getPlayerDetails()[2]
	turn = _angle - angle
	if (abs(_angle-angle) > 180):
		if (turn > 0): #if positive
			left = False;
		else:
			left = True;
	else:#turn the right way
		if (turn > 0):
			left = True;
		else:
			left = False;
	while (abs(_angle-angle) >= 5):
		angle = readData.getPlayerDetails()[2]
		if(left):
			actions.turnLeft(3)
		else:
			actions.turnRight(3)

def switchAndShoot(a):

	currentPlayer = readData.getPlayerDetails()

	if(currentAmmo() == 0 or currentPlayer[4]==0): # if no ammo in held gun or fists are equipped, switch to somethin else
		hasWeapon = [True]+currentPlayer[6]
	#	hasWeapon=[True]+readData.getWeaponsStatus(plrDetails[0],plrDetails) #add [True] for fists
		for i in range(6, -1, -1):#start checking from back (6) and end on fists (0) if no ammo
			hasAmmo = currentPlayer[5][mapWeaponToAmmoType(i)] > 0
			if (hasAmmo  and hasWeapon[i]):
				actions.switchWeapon(i) #switch to a weapon with ammo
				time.sleep(1)
				break

	actions.shoot(a)

def currentAmmo():
	ammoType = mapWeaponToAmmoType(readData.getPlayerDetails()[4])
	if(ammoType>=0):
		return readData.getPlayerDetails()[5][ammoType]
	else:
		return 9999 #fists or chainsaw dont require ammo

def mapWeaponToAmmoType(weaponNo):
	return [-1,0,1,0,3,2,2][weaponNo]



def findLowestHPEnemy(_range):
	enemyList = readData.getEnemyDetails(readData.getPlayerDetails()[0])

	lowestHP=9999
	lowestEnemy=-1#negative means no enemies in range
	for enemy in enemyList:
		dist = readData.getObjectDetails(enemy[0])[3]
		if (dist <= _range and enemy[1] < lowestHP):
			lowestEnemy = enemy[0]
			lowestHP = enemy[1]

	return lowestEnemy

def findClosestObject(objectList):
	#objects = readData.getObjectsDetails(readData.getPlayerDetails()[0])
	closestDist = objectList[0][3]
	closestObject = objectList[0][0]
	for obj in objectList:
		dist=obj[3]
		if (dist<closestDist):
			closestDist=dist
			closestObject=obj[0]

	return closestObject

def faceObject(objectID):
	objectDetails = readData.getObjectDetails(objectID)
	playerDetails = readData.getPlayerDetails()

	dx=objectDetails[2][0] - playerDetails[3][0] #get Xs
	dy=objectDetails[2][1] - playerDetails[3][1] #get Ys
	absAngle=math.atan2(dy,dx)
	turnAbsAngle(absAngle)

def listSeenEnemies():
	seenEnemyList = []
	currentPlayerID = readData.getPlayerDetails()[0]
	for enemies in readData.getEnemyDetails(currentPlayerID):
		if readData.LOS(str(currentPlayerID), str(enemies[0])):
			seenEnemyList.append(enemies[0])

	return seenEnemyList

if __name__ == "__main__":
    print(switchAndShoot(2))

#redundant function, replaced by listSeenEnemies

'''
def canSeeEnemy():
	canSee = False
	for enemyID in enemyIDs:
		if LOS(prlID,enemyID):
			canSee=True
			break

	return canSee
'''
