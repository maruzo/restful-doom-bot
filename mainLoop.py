
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

while(): #main loop
	
	plrHP = currentPlayerDetails
	useableAmmo = 3               ####place holder####
	
	if(enoughHP and plrHP<30):enoughHP = False
	if(!enoughHP and plrHP>50):enoughHP = True
	if(enoughAmmo and useableAmmo<=2):enoughAmmo = False
	if(!enoughAmmo and useableAmmo>4):enoughAmmo = True
	
	if(!enoughHP):
		state=HEALTH_SEARCH #health search takes priority over ammo search
	else if(!enoughAmmo):
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
	else if (state==HEALTH_SEARCH):
		#HEALTH_SEARCH
	else if (state==AMMO_SEARCH):
		#AMMO_SEARCH
	if(state==ENEMY_SEARCH):#not an else if, as this state could have been assigned during the begging IF statement
		#ENEMY_SEARCH
		

	