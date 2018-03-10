
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
	if(currentAmmo()>0):
		actions.shoot(a)
	else:
		return#switch to a weapon with ammo

def currentAmmo():
	ammoType = mapWeaponToAmmoType(readData.currentWeapon())
	if(ammoType>0):
		return readData.getAmmo(ammoType)
	else:
		return 9999 #fists or chainsaw dont require ammo

def mapWeaponToAmmoType(weaponNo):
	return [-1,0,1,0,3,2,2][weaponNo]


'''
def findLowestHPEnemy(enemyList, range):
	lowestHP=9999
	lowestEnemy=-1#negative means no enemies in range
	for enemyID in enemyList:
		dist=distanceToEnemy(enemyID)
		if (dist<=range && enemyHP[enemyID]<lowestHP):
			lowestEnemy=enemyID
			lowestHP=enemyHP[enemyID]

	return lowestEnemy

def findClosestObje(enemyList):
	closestDist=distanceToEnemy(enemyID[0])
	closestEnemy=enemyID[0]
	for enemyID in enemyList:
		dist=distanceToEnemy(enemyID)
		if (dist<closestDist):
			closestDist=dist
			closestEnemy=enemyID[0]

	return closestEnemy



def distanceToEnemy(enemyID):
	dx=enemyX(enemyID)-getPlrX()
	dy=enemyY(enemyID)-getPlrY()
	return math.sqrt(dx*dx+dy*dy)

def faceEnemy(enemyID):
	dx=enemyX(enemyID)-getPlrX()
	dy=enemyY(enemyID)-getPlrY()
	absAngle=math.atan2(dy,dx)
	absTurn(absAngle)

def listSeenEnemies():
	seenEnemyList = []
	for enemyID in enemyIDs:
		if LOS(prlID,enemyID):
			canSee=True
			break

	return canSee

'''
if __name__ == "__main__":
    turnAbsAngle(10)

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
