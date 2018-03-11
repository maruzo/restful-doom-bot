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

	if(currentAmmo() == 0 or currentPlayer[4]==0 or currentPlayer[4]==7): # if no ammo in held gun or fists are equipped, switch to somethin else
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


def useableAmmo():
	total=0
	currentPlayer = readData.getPlayerDetails()
	hasWeapon=[True]+currentPlayer[6]
	for i in range(1,7):
		if (hasWeapon[i]):
			total += currentPlayer[5][mapWeaponToAmmoType(i)]
	return total

def mapWeaponToAmmoType(weaponNo):
	return [-1,0,1,0,3,2,2,-1][weaponNo]



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
	if (objectList != []):
		closestDist = objectList[0][3]
		closestObject = objectList[0][0]
		for obj in objectList:
			dist=obj[3]
			if (dist<closestDist):
				closestDist=dist
				closestObject=obj[0]
	else:
		closestObject = -1
	return closestObject

def findClosestHealth():
	plrId = readData.getPlayerDetails()[0]
	objList = readData.getObjectsDetails(plrId)
	healthObj=[]
	for obj in objList:
		if("health" in obj[1].lower()):
			healthObj.append(obj)
	return findClosestObject(healthObj)

def findClosestAmmo():
	plrId = readData.getPlayerDetails()[0]
	objList = readData.getObjectsDetails(plrId)
	AmmoObj=[]
	for obj in objList:
		if("shells" in obj[1].lower()  or "clips" in obj[1].lower()):
			AmmoObj.append(obj)
	return findClosestObject(AmmoObj)

def faceObject(objectID):
	objectDetails = readData.getObjectDetails(objectID)
	playerDetails = readData.getPlayerDetails()
	if (objectDetails != []):
		dx=objectDetails[2][0] - playerDetails[3][0] #get Xs
		dy=objectDetails[2][1] - playerDetails[3][1] #get Ys
		absRadAngle = math.atan2(dy,dx)
		absDegAngle =math.degrees(absRadAngle)
		if(absDegAngle < 0):absDegAngle += 360
		turnAbsAngle(absDegAngle)

def faceAwayFromObject(objectID):
	objectDetails = readData.getObjectDetails(objectID)
	playerDetails = readData.getPlayerDetails()
	if (objectDetails != []):
		dx=objectDetails[2][0] - playerDetails[3][0] #get Xs
		dy=objectDetails[2][1] - playerDetails[3][1] #get Ys
		absRadAngle = math.atan2(dy,dx)
		absDegAngle =math.degrees(absRadAngle)
		absDegAngle+=180
		if(absDegAngle < 0):absDegAngle += 360
		if(absDegAngle > 360):absDegAngle -= 360
		turnAbsAngle(absDegAngle)

def listSeenEnemies():
	seenEnemyList = []
	currentPlayerID = readData.getPlayerDetails()[0]
	objs = readData.getEnemyDetails(currentPlayerID)
	if (objs != []):
		for enemies in objs:
			print(enemies)
			if readData.LOS(currentPlayerID, enemies[0]):
				seenEnemyList.append(enemies)

	return seenEnemyList

if __name__ == "__main__":
	faceObject(findClosestHealth())

'''print(switchAndShoot(2))'''
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
