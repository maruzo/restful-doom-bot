from request import post


def shoot(amount):
    if post("/api/player/actions", {'type': 'shoot','amount': amount}) != 201:
        raise ValueError('Shoot command was not executed')

def forward(amount):
    if post("/api/player/actions", {'type': 'forward','amount': amount}) != 201:
        raise ValueError('Forward command was not executed')

def backward(amount):
    if post("/api/player/actions", {'type': 'backward','amount': amount}) != 201:
        raise ValueError('Backward command was not executed')


def turnLeft(amount):
    if post("/api/player/actions", {'type': 'turn-left','amount': amount}) != 201:
        raise ValueError('Turn Left command was not executed')


def turnRight(amount):
    if post("/api/player/actions", {'type': 'turn-right','amount': amount}) != 201:
        raise ValueError('Turn righth command was not executed')


def use(amount):
    if post("/api/player/actions", {'type': 'use','amount': amount}) != 201:
        raise ValueError('Use command was not executed')


def strafeLeft(amount):
    if post("/api/player/actions", {'type': 'strafe-left','amount': amount}) != 201:
        raise ValueError('Strafe left command was not executed')


def strafeRight(amount):
    if post("/api/player/actions", {'type': 'strafe-right','amount': amount}) != 201:
        raise ValueError('Strafe right command was not executed')

def switchWeapon(amount):
    if post("/api/player/actions", {'type': 'switch-weapon','amount': amount}) != 201:
        raise ValueError('Switch weapon command was not executed')


if __name__ == "__main__":
    print(forward(10))
