
import utilityActions
import actions
import readData

#state = HEALTH_SEARCH | AMMO_SEARCH | FIGHT | ENEMY_SEARCH
FIGHT = 0
HEALTH_SEARCH = 1
AMMO_SEARCH = 2
ENEMY_SEARCH = 3

state = FIGHT
enoughHP = True
enoughAmmo = True

while(True): #main loop

	plrHP = currentPlayerDetails
	useableAmmo = 3               ####place holder####

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
	elif (not enoughAmmo):
		state=AMMO_SEARCH
	else:
		state=FIGHT

	if (state==FIGHT):
		seenEnemyList=utilityActions.listSeenEnemies()
		if (seenEnemyList!=[]):
			closesEnemy=utilityActions.findClosestObject(seenEnemyList)
			closesDist=utilityActions.distanceToEnemy(closesEnemy)
			closeLowHPenemy = utilityActions.findLowestHPEnemy(seenEnemyList, closesDist*1.5)
			utilityActions.faceEnemy(closeLowHPenemy)
			utilityActions.switchAndShoot(2)
			#send shoot action
			#if out of ammo, switch weapon
		else:
			#no one in line of sight, search for enemies
			state = ENEMY_SEARCH
	elif (state==HEALTH_SEARCH):
		return
	elif (state==AMMO_SEARCH):
		#AMMO_SEARCH
	if(state==ENEMY_SEARCH):#not an else if, as this state could have been assigned during the begging IF statement
		#ENEMY_SEARCH
