
import utilityActions
import actions
import readData

#state = HEALTH_SEARCH | AMMO_SEARCH | FIGHT
FIGHT = 0
HEALTH_SEARCH = 1
AMMO_SEARCH = 2

state = FIGHT
enoughHP = True
enoughAmmo = True

while(): #main loop
	
	if(enoughHP and readData.plrHP<30):enoughHP = False
	if(!enoughHP and readData.plrHP>50):enoughHP = True
	if(enoughAmmo and readData.useableAmmo<=2):enoughAmmo = False
	if(!enoughAmmo and readData.useableAmmo>4):enoughAmmo = True
	
	if(!enoughHP):
		state=HEALTH_SEARCH #health search takes priority over ammo search
	else if(!enoughAmmo):
		state=AMMO_SEARCH
	else:
		state=FIGHT
	
	if (state==FIGHT):
		seenEnemyList=listSeenEnemies()
		if (seenEnemyList!=[]):
			closesEnemy=findClosestEnemy(seenEnemyList)
			closesDist=distanceToEnemy(closesEnemy)
			closeLowHPenemy = findLowestHPEnemy(seenEnemyList, closesDist*1.5)
			faceEnemy(closeLowHPenemy)
			actions.shoot(1)
			#send shoot action
			#if out of ammo, switch weapon
		else:
			#search for enemies
			actions.forward(10)
	else if (state==HEALTH_SEARCH):
		#HEALTH_SEARCH
	else if (state==AMMO_SEARCH):
		#AMMO_SEARCH