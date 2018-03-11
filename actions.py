from request import post

repeat = 2

def doAction(name,amount):
    for i in range(repeat):
<<<<<<< HEAD
        if post("/api/player/actions", {'type': 'shoot','amount': amount}) != 201:
            print('Shoot command was not executed')
            continue
        break

def forward(amount):
    for i in range(repeat):
        if post("/api/player/actions", {'type': 'forward','amount': amount}) != 201:
            print('Forward command was not executed')
            continue
        break

def backward(amount):
    for i in range(repeat):
        if post("/api/player/actions", {'type': 'backward','amount': amount}) != 201:
            print('Backward command was not executed')
            continue
        break

def turnLeft(amount):
    for i in range(repeat):
        if post("/api/player/actions", {'type': 'turn-left','amount': amount}) != 201:
            print('Turn Left command was not executed')
            continue
        break

def turnRight(amount):
    for i in range(repeat):
        if post("/api/player/actions", {'type': 'turn-right','amount': amount}) != 201:
            print('Turn righth command was not executed')
            continue
        break

def use(amount):
    for i in range(repeat):
        if post("/api/player/actions", {'type': 'use','amount': amount}) != 201:
            print('Use command was not executed')
            continue
        break

def strafeLeft(amount):
    for i in range(repeat):
        if post("/api/player/actions", {'type': 'strafe-left','amount': amount}) != 201:
            print('Strafe left command was not executed')
            continue
        break


def strafeRight(amount):
    for i in range(repeat):
        if post("/api/player/actions", {'type': 'strafe-right','amount': amount}) != 201:
            print('Strafe right command was not executed')
            continue
        break


def switchWeapon(amount):
    for i in range(repeat):
        if post("/api/player/actions", {'type': 'switch-weapon','amount': amount}) != 201:
            print('Switch weapon command was not executed')
            continue
        break

=======
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
>>>>>>> cc5ab022f8311423b79b7fd28bb89a908f4cf769

def respawn():
    pass

if __name__ == "__main__":
    print(forward(10))
