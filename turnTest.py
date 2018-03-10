
import math
#import json

'''
get player pos
find closest/lowest HP enemy
get enemy coords
point
shoot



enemy cords-plr coord
'''

#public enemyIDs[]

seenEnemyList=listSeenEnemies()
if (seenEnemyList!=[]):
	closesEnemy=findClosestEnemy(seenEnemyList)
	closesDist=distanceToEnemy(closesEnemy)
	closeLowHPenemy = findLowestHPEnemy(seenEnemyList, closesDist*1.5)
	faceEnemy(closeLowHPenemy)
	shoot()
	#send shoot action
	#if out of ammo, switch weapon
else:
	#search for enemies
	walkFwrd()
	

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
	
	
	
	
	
'''#redundant
def canSeeEnemy():
	canSee = False
	for enemyID in enemyIDs:
		if LOS(prlID,enemyID):
			canSee=True
			break
			
	return canSee
'''


'''

def query():
	#GET info and store
	
def getPlrX():
def getPlrY():

def enemyX(i)
def enemyY(i)
enemyHP(i)

def absTurn(absAngle):
walkFwrd()

def shoot():
	#send shoot action
	#if out of ammo, switch weapon
'''