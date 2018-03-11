import actions, random


def attack(xy, direction = None):
    x = xy[0]
    y = xy[1]
    if direction is None:
        direction = random.randint(0,1)
    
        
    if direction == 0:
         actions.strafeLeft(10)
         actions.forward(10)
    else:
        actions.strafeRight(10)
        actions.forward(10)
        
    return direction

if __name__ == "__main__":
    attack([0,1])



