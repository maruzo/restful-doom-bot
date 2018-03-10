
import math
import actions
import readData


def turnAbsAngle(_angle):
	angle = readData.getPlayerDetails()[2]
	while (abs(_angle-angle) > 5):
		turn = _angle - angle
		#turn the other way
		if (abs(_angle-angle) > 180):
			if (turn > 0): #if positive
				actions.turnRight(turn*1.5)
			else:
				actions.turnLeft(turn*-1.5)
		else:#turn the right way
			if (turn > 0):
				actions.turnLeft(turn*1.5)
			else:
				actions.turnRight(turn*-1.5)
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

def findClosestEnemy(enemyList):
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
    turnAbsAngle(150)

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
