
import utilityActions
import actions
import readData
import offensiveAction
import sys


currentPlayerID = readData.getPlayerDetails()[0]

#state = HEALTH_SEARCH | AMMO_SEARCH | FIGHT | ENEMY_SEARCH
FIGHT = 0
HEALTH_SEARCH = 1
AMMO_SEARCH = 2
ENEMY_SEARCH = 3

state = FIGHT
enoughHP = True
enoughAmmo = True


previousZigZagDirection = None
while(True): #main loop

	#I am dead
	if (readData.getObjectDetails(currentPlayerID) == []):
		sys.exit(0)


	plrHP = readData.getPlayerDetails()[1]
	useableAmmo = utilityActions.useableAmmo()

	if (enoughHP and plrHP<30):
		enoughHP = False
	elif (not enoughHP and plrHP>50):
		enoughHP = True
	elif(enoughAmmo and useableAmmo<=2):
		enoughAmmo = False
	elif(not enoughAmmo and useableAmmo>4):
		enoughAmmo = True

	if (not enoughHP):
		state=HEALTH_SEARCH #health search takes priority over ammo search
		print("HEALTH_SEARCH")
	elif (not enoughAmmo):
		state=AMMO_SEARCH
		print("AMMO_SEARCH")
	else:
		state=FIGHT
		print("FIGHT")

	if (state==FIGHT):
		seenEnemyList=utilityActions.listSeenEnemies()
		if (seenEnemyList!=[]):
			closestEnemyID = utilityActions.findClosestObject(seenEnemyList)
			#closesDist=readData.getObjectDetails(closestEnemyID)[3]
			#closeLowHPenemy = utilityActions.findLowestHPEnemy(seenEnemyList, closesDist*1.5)
			[previousZigZagDirection, distance] = offensiveAction.attack(closestEnemyID, currentPlayerID, 100, previousZigZagDirection)
			utilityActions.faceObject(closestEnemyID)
			if (distance < 1800):
				utilityActions.switchAndShoot(1)
			#send shoot action
			#if out of ammo, switch weapon
		else:
			#no one in line of sight, search for enemies
			state = ENEMY_SEARCH
			print("ENEMY_SEARCH")
	elif (state==HEALTH_SEARCH):
		#utilityActions.faceObject(utilityActions.findClosestHealth())
		NotImplemented
	elif (state==AMMO_SEARCH):
		#AMMO_SEARCH
		NotImplemented
	if(state==ENEMY_SEARCH):#not an else if, as this state could have been assigned during the begging IF statement
		#ENEMY_SEARCH
		NotImplemented
