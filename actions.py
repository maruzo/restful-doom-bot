from request import post

repeat = 2

def doAction(name,amount):
    for i in range(repeat):
        if post("/api/player/actions", {'type': name,'amount': amount}) != 201:
            print(name+' command was not executed')
        else:
            break

def shoot(amount):doAction("shoot",amount)
def forward(amount):doAction("forward",amount)
def backward(amount):doAction("backward",amount)
def turnLeft(amount):doAction("turn-left",amount)
def turnRight(amount):doAction("turn-right",amount)
def use(amount):doAction("use",amount)
def strafeLeft(amount):doAction("strafe-left",amount)
def strafeRight(amount):doAction("strafe-right",amount)
def switchWeapon(amount):doAction("switch-weapon",amount)

def respawn():
    pass

if __name__ == "__main__":
    print(forward(10))
