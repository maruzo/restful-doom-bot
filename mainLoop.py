
import utilityActions
import actions
import readData
import offensiveAction
import defensiveAction
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
	elif(enoughAmmo and useableAmmo<=5):
		enoughAmmo = False
	elif(not enoughAmmo and useableAmmo>7):
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
			[previousZigZagDirection, distance] = offensiveAction.attack(closestEnemyID, currentPlayerID, previousZigZagDirection)
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
		closestHPID = utilityActions.findClosestHealth()
		[previousZigZagDirection, distance] = defensiveAction.flee(closestHPID, currentPlayerID, previousZigZagDirection)
		utilityActions.faceAwayFromObject(closestHPID)
		if (distance < 1800):
			utilityActions.switchAndShoot(1) #only shoot if I am pointing at an enemy
	elif (state==AMMO_SEARCH):
		closestAmmoID = utilityActions.findClosestAmmo()
		[previousZigZagDirection, distance] = defensiveAction.flee(closestAmmoID, currentPlayerID, previousZigZagDirection)
		utilityActions.faceAwayFromObject(closestAmmoID)
		if (distance < 1800):
			utilityActions.switchAndShoot(1) #only shoot if I am pointing at an enemy

	if(state==ENEMY_SEARCH):#not an else if, as this state could have been assigned during the begging IF statement
		#ENEMY_SEARCH
		ClosestObjectID = utilityActions.findNearestNonEnemy()
		[previousZigZagDirection, distance] = defensiveAction.flee(closestObjectID, currentPlayerID, previousZigZagDirection)
		utilityActions.faceAwayFromObject(closestObjectID)
		
