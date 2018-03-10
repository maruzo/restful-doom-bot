#state = HEALTH_SEARCH | AMMO_SEARCH | FIGHT
FIGHT = 0
HEALTH_SEARCH = 1
AMMO_SEARCH = 2



state = FIGHT

while(): #main loop
	
	if(readData.plrHP<30):
		state = HEALTH_SEARCH
	
	if (state=FIGHT):
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