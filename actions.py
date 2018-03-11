from request import post

repeat = 2

def shoot(amount):
    for i in range(repeat):
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


def respawn():
    pass

if __name__ == "__main__":
    print(forward(10))
